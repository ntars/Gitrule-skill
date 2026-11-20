#!/usr/bin/env python3
"""Gitrule 文档检查与优化命令行工具。

零第三方依赖，仅使用 Python 标准库。
默认只检查不写文件；--fix 才会执行安全修复。

退出码：0 无问题，1 发现问题，2 参数或环境错误。
"""

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path

SUPPORTED_LANGS = (
    "zh-CN", "en-US", "zh-TW", "ja-JP", "ko-KR", "fr-FR",
    "de-DE", "es-ES", "pt-BR", "ru-RU", "ar-SA", "hi-IN",
)

# 跨语种比对的计数轴。表格形状与占位符多重集单独比对，不在此列。
CROSS_AXES = ("heading", "fence", "link", "ordered", "unordered")

# 术语译名矩阵的列名。这 6 个术语在十二个语种正文中均有实际用例，
# 故纳入自动校验；SBOM / MVP / NLP / LLM 在正文出现 0 次，不参与校验。
TERM_MATRIX_TERMS = ("SemVer", "ADR", "CoC", "CI/CD", "MCP", "TBD")

# 变格语言的检索词干。俄语、德语正文按语法变格，矩阵取引用形，
# 严格全字匹配会误判为"正文未出现"，故按词干比对。
TERM_STEMS = {
    ("ru-RU", "SemVer"): "семантическ",
    ("ru-RU", "ADR"): "архитектурн",
    ("ru-RU", "CI/CD"): "непрерывн",
    ("de-DE", "SemVer"): "semantisch",
}

# 外部链接前缀：带 URL scheme（https:、mailto:）、协议相对（//）、页内锚点（#）。
EXTERNAL_LINK_RE = re.compile(r"^(?:[a-zA-Z][a-zA-Z0-9+.\-]*:|//|#)")

# Markdown 链接整体，目标地址允许被尖括号包裹，也允许带可选的标题。
LINK_RE = re.compile(r"\[[^\]]*\]\(\s*<?([^)>]+?)>?(?:\s+[\"'][^\"']*[\"'])?\s*\)")

EXIT_OK = 0
EXIT_ISSUES = 1
EXIT_USAGE = 2


def strip_code(text):
    """移除代码块与行内代码，只保留用于扫描的正文。"""
    text = re.sub(r"````.*?````", "", text, flags=re.S)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]+`", "", text)


def local_md_links(text):
    """取出正文中的站内 Markdown 链接目标。

    跳过外部链接、页内锚点与协议相对地址，只返回 .md 结尾的站内路径。
    返回值保留原始写法（可能带 `./` 前缀或子目录），由调用方按需解析。
    """
    targets = []
    for match in LINK_RE.finditer(strip_code(text)):
        target = match.group(1).strip()
        if not target or EXTERNAL_LINK_RE.match(target):
            continue
        path_part = target.split("#", 1)[0].strip()
        if not path_part.lower().endswith(".md"):
            continue
        targets.append(path_part)
    return targets


def analyze_fences(text):
    """检查代码围栏是否配对、哪些开口缺少语言标识。

    围栏长度不同的行视为内层内容，不参与配对，因此四重围栏内嵌
    三重围栏不会被误判为提前闭合。
    """
    lines = text.splitlines()
    stack = []
    bare_open = []
    for number, line in enumerate(lines, 1):
        match = re.match(r"^(`{3,})([^`]*)$", line)
        if not match:
            continue
        length = len(match.group(1))
        language = match.group(2).strip()
        if not stack:
            stack.append((length, number))
            if not language:
                bare_open.append(number)
        elif length == stack[-1][0] and not language:
            stack.pop()
    return {
        "bare_open": bare_open,
        "unclosed": [{"line": number} for _, number in stack],
    }


def has_purpose(text):
    """判断文件开头是否写明唯一职责：不依赖具体语种，取位置与结构判定。

    约定为首个二级标题之前存在一段以 `>` 引出的说明块。
    """
    head = text[:600]
    if "本文件解决什么问题" in head or "What this file solves" in head:
        return True
    return bool(re.search(r"(?m)^> ", head))


def has_related(text):
    """判断文件结尾是否有相关文件区：末段存在二级标题且其后接列表或表格。"""
    if "## 相关文件" in text or "## Related Files" in text:
        return True
    tail = text[int(len(text) * 0.55):]
    return bool(re.search(r"(?m)^## .+\n\n(- |\|)", tail))


def check_links(directory, texts):
    """检查同一语言目录内的相对 Markdown 链接是否存在。

    外部链接（http、mailto 等）与页内锚点不属于本地校验范围，直接跳过。
    """
    issues = []
    for name, text in texts.items():
        for target in local_md_links(text):
            if not (directory / target).exists():
                issues.append({
                    "file": name,
                    "type": "broken-link",
                    "detail": target,
                })
    return issues


def check_index(directory, texts):
    """检查索引域计数、表格条目数与声明合计是否一致。"""
    text = texts.get("README.md")
    if text is None:
        return []
    numbers = [int(value) for value in re.findall(r"[（(](\d+)\s*(?:篇|files?|specs?)\s*[）)]", text)]
    listed = len(re.findall(r"^\| \[[^\]]+\]\(\./[^)]+\.md\)", text, flags=re.M))
    declared_match = re.search(r"(?:合计|合計|total)[^\d]{0,12}(\d+)", text, flags=re.I)
    declared = int(declared_match.group(1)) if declared_match else None
    issues = []
    if numbers and sum(numbers) != listed:
        issues.append({
            "file": "README.md",
            "type": "index-count",
            "detail": f"域计数合计 {sum(numbers)}，表格条目 {listed}",
        })
    if declared is not None and declared != listed:
        issues.append({
            "file": "README.md",
            "type": "index-declaration",
            "detail": f"声明合计 {declared}，表格条目 {listed}",
        })
    return issues


def find_template_file(texts):
    """按语言无关的结构特征定位 README 模板：同时含模板正文与占位符对照表。"""
    for name, text in texts.items():
        if "{{" not in text:
            continue
        has_body = re.search(r"(?mi)^##\s+.*(模板正文|template body|模板內文)", text)
        has_table = re.search(r"(?mi)^##\s+.*(占位符对照表|placeholder reference|佔位符對照表)", text)
        if has_body and has_table:
            return name
    return None


def check_placeholders(texts):
    """检查 README 模板正文占位符是否全部登记到对照表。"""
    name = find_template_file(texts)
    if not name:
        return []
    chunks = re.split(r"(?m)^##\s+", texts[name])
    body, table = "", ""
    for chunk in chunks:
        low = chunk.lower()
        if re.search(r"(模板正文|template body|模板內文)", chunk) or "template body" in low:
            body = chunk
        if re.search(r"(占位符对照表|placeholder reference|佔位符對照表)", chunk) or "placeholder reference" in low:
            table = chunk
    if not body or not table:
        return []
    body_names = set(re.findall(r"\{\{([^{}]+)\}\}", body))
    table_names = set(re.findall(r"\{\{([^{}]+)\}\}", table))
    missing = sorted(body_names - table_names)
    if missing:
        return [{
            "file": name,
            "type": "unregistered-placeholder",
            "detail": ", ".join(missing),
        }]
    return []


def read_language(directory):
    """一次性读入某语种目录的全部 Markdown，供各检查复用。

    单个文件读失败时跳过并给出提示，不让一个坏文件中断整轮检查。
    """
    texts = {}
    for path in sorted(directory.glob("*.md")):
        try:
            texts[path.name] = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            print(f"警告：跳过 {path.name}，读取失败：{exc}", file=sys.stderr)
    return texts


def check_language(root, lang):
    """检查单个语言目录，返回结构化问题列表。"""
    directory = Path(root) / "locales" / lang
    if not directory.exists():
        return [{"file": lang, "type": "missing-language", "detail": str(directory)}]
    texts = read_language(directory)
    issues = []
    for name, text in texts.items():
        if not has_purpose(text):
            issues.append({"file": name, "type": "missing-purpose", "detail": ""})
        if not has_related(text):
            issues.append({"file": name, "type": "missing-related", "detail": ""})
        fences = analyze_fences(text)
        for line in fences["bare_open"]:
            issues.append({"file": name, "type": "bare-code-fence", "detail": f"line {line}"})
        for item in fences["unclosed"]:
            issues.append({"file": name, "type": "unclosed-code-fence", "detail": f"line {item['line']}"})
    issues.extend(check_links(directory, texts))
    issues.extend(check_index(directory, texts))
    issues.extend(check_placeholders(texts))

    referenced = set()
    for text in texts.values():
        for target in local_md_links(text):
            referenced.add(Path(target).name)
    for name in texts:
        if name != "README.md" and name not in referenced:
            issues.append({"file": name, "type": "orphan", "detail": ""})
    return issues


def cross_metrics(text):
    """提取用于跨语种比对的八轴结构指标。

    章号形态（`## 一、` 与 `## 1.`）先归一，其余数字保留，供占位符与数字比对。
    """
    normalized = re.sub(r"^## [一二三四五六七八九十]+、", "## ", text, flags=re.M)
    normalized = re.sub(r"^## \d+\. ", "## ", normalized, flags=re.M)
    table = [line for line in text.split("\n") if line.strip().startswith("|")]
    return {
        "heading": len(re.findall(r"^#{1,6} ", text, re.M)),
        "fence": len(re.findall(r"^```", text, re.M)),
        "link": len(re.findall(r"\]\(", text)),
        "ordered": len(re.findall(r"^\d+\. ", text, re.M)),
        "unordered": len(re.findall(r"^[-*] ", text, re.M)),
        "table": table,
        "placeholder": sorted(re.findall(r"\{\{[^{}]*\}\}", normalized)),
    }


def table_shape(table):
    """把表格行转为「每行列数」序列，用于逐行比对列数是否一致。"""
    shape = []
    for line in table:
        cells = line.strip().strip("|")
        shape.append(cells.count("|") + 1 if cells else 0)
    return shape


def index_links(directory):
    """按出现顺序读取索引页的规范链接，作为跨语种文件名的一一映射依据。"""
    index = directory / "README.md"
    if not index.exists():
        return []
    try:
        text = index.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []
    return re.findall(r"\]\(\./([^)#]+\.md)\)", text)


def cross_check_language(root, lang, reference="zh-CN"):
    """以参考语种为基准，比对某一语种的结构是否一致。

    文件名映射完全依赖两个语种索引页的链接顺序，不依赖外部映射表，
    因此新增语种时无需额外维护清单。

    检查顺序固定，前面的分支一旦命中即返回，不再进入后续比对：
    目标目录缺失 -> 参考索引无链接 -> 两索引链接数不等 -> 逐篇比对。

    注意 cross-missing-reference 表示**参考语种自己**索引里有、但目录里
    没有该文件；因为逐语种独立调用，同一个缺失会按语种数各报一条。
    """
    base_dir = Path(root) / "locales" / reference
    target_dir = Path(root) / "locales" / lang
    if not target_dir.exists():
        return [{"file": lang, "type": "cross-missing-language", "detail": str(target_dir)}]
    base_names = index_links(base_dir)
    target_names = index_links(target_dir)
    if not base_names:
        return [{"file": reference, "type": "cross-no-reference", "detail": "索引页无规范链接"}]
    if len(base_names) != len(target_names):
        return [{
            "file": lang,
            "type": "cross-index-count",
            "detail": f"索引链接 {len(target_names)}，参考 {reference} 为 {len(base_names)}",
        }]

    issues = []
    for base_name, target_name in zip(base_names, target_names):
        base_path = base_dir / base_name
        target_path = target_dir / target_name
        if not base_path.exists():
            issues.append({"file": base_name, "type": "cross-missing-reference", "detail": reference})
            continue
        if not target_path.exists():
            issues.append({
                "file": target_name,
                "type": "cross-broken-index",
                "detail": f"{lang} 索引指向不存在的文件",
            })
            continue
        try:
            base_m = cross_metrics(base_path.read_text(encoding="utf-8"))
            target_m = cross_metrics(target_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError) as exc:
            issues.append({"file": target_name, "type": "cross-unreadable", "detail": str(exc)})
            continue
        # 索引页的语言切换条比参考语种多一个本语种自链接，属固有条目。
        is_index = target_name == "README.md"
        for axis in CROSS_AXES:
            base_v, target_v = base_m[axis], target_m[axis]
            if is_index and axis == "link" and target_v - base_v == 1:
                continue
            if base_v != target_v:
                issues.append({
                    "file": target_name,
                    "type": f"cross-{axis}",
                    "detail": f"{lang} {target_v}，参考 {base_v}",
                })
        base_shape = table_shape(base_m["table"])
        target_shape = table_shape(target_m["table"])
        if len(base_shape) != len(target_shape):
            issues.append({
                "file": target_name,
                "type": "cross-table-rows",
                "detail": f"{lang} {len(target_shape)}，参考 {len(base_shape)}",
            })
        else:
            for row, (base_col, target_col) in enumerate(zip(base_shape, target_shape), 1):
                if base_col != target_col:
                    issues.append({
                        "file": target_name,
                        "type": "cross-table-columns",
                        "detail": f"第 {row} 行 {lang} {target_col} 列，参考 {base_col} 列",
                    })
                    break
        if base_m["placeholder"] != target_m["placeholder"]:
            missing = sorted(set(base_m["placeholder"]) - set(target_m["placeholder"]))
            extra = sorted(set(target_m["placeholder"]) - set(base_m["placeholder"]))
            detail = f"缺失 {len(missing)} 个，多出 {len(extra)} 个"
            if missing:
                detail += f"；首个缺失 {missing[0]}"
            if extra:
                detail += f"；首个多出 {extra[0]}"
            issues.append({"file": target_name, "type": "cross-placeholder", "detail": detail})
    return issues


def matrix_header_terms(line):
    """若该行是译名矩阵表头，返回其中的术语列名，否则返回空列表。

    避免把普通表格误认成矩阵：要求表头同时出现两个以上已知术语列名。
    """
    if not line.strip().startswith("|"):
        return []
    header = [cell.strip() for cell in line.strip().strip("|").split("|")]
    known = set(TERM_MATRIX_TERMS)
    terms = [cell for cell in header[2:] if cell in known]
    return terms if len(terms) >= 2 else []


def parse_term_matrix_of_text(text):
    """从文本中解析译名矩阵表头，返回 (表头列名, 首个表头行号)。

    读不到则返回 ([], -1)。行号用于后续从紧随的表体取本语种行。
    """
    for index, line in enumerate(text.splitlines()):
        if matrix_header_terms(line):
            header = [cell.strip() for cell in line.strip().strip("|").split("|")]
            return header, index
    return [], -1


def parse_term_matrix(texts, lang):
    """从已读入的术语表中取回本语种的译名。

    矩阵形态：表头为「语种 | 语种名称 | 术语1 | 术语2 ...」，
    每行以反引号包裹的语言码开头。

    返回 (术语列表, {术语: 该语种译名})，读不到则返回 ([], {})。
    """
    for text in texts.values():
        header, start = parse_term_matrix_of_text(text)
        if start < 0:
            continue
        lines = text.splitlines()
        for row in lines[start + 2:]:
            if not row.strip().startswith("|"):
                break
            cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
            if len(cells) < len(header):
                continue
            if cells[0].strip("`") != lang:
                continue
            return header[2:], dict(zip(header[2:], cells[2:]))
    return [], {}


def term_corpus(texts, glossary_name):
    """拼接某语种全部正文，用于术语检索。

    排除术语表本身与索引页：前者是矩阵的出处，计入会自证；
    后者是导航，不承载术语定义。
    """
    return "\n".join(
        text for name, text in texts.items()
        if name != glossary_name and name != "README.md"
    )


def term_check_language(root, lang):
    """校验某语种的术语矩阵与正文用词是否自洽。

    检查四类问题：
    1. term-not-in-corpus：矩阵登记的译名在正文一次都没出现。
    2. term-doubtful-stem：变格语言的矩阵值与登记词干对不上。
    3. term-no-matrix：术语表存在但找不到译名矩阵。
    4. term-missing-language：语种目录不存在。

    只做"矩阵 -> 正文"的单向核对。不做"正文缺术语"检查：技术规范按
    主题分篇，某篇不涉及某术语是正常的，强行要求出现会产生大量误报。
    """
    directory = Path(root) / "locales" / lang
    if not directory.exists():
        return [{"file": lang, "type": "term-missing-language", "detail": str(directory)}]

    texts = read_language(directory)
    # 术语表文件名随语种变化（术语表.md / glossary.md / 用語集.md），
    # 按"文件含矩阵"识别比按文件名匹配更可靠。
    glossary = next((name for name in texts if parse_term_matrix_of_text(texts[name])[1] >= 0), None)
    if glossary is None:
        return [{"file": lang, "type": "term-no-matrix", "detail": "术语表未找到译名矩阵"}]

    terms, rendering = parse_term_matrix({glossary: texts[glossary]}, lang)
    if not terms:
        return [{"file": lang, "type": "term-no-matrix", "detail": "术语表未找到译名矩阵"}]

    corpus = term_corpus(texts, glossary).lower()
    issues = []
    for term in terms:
        value = rendering.get(term, "").strip()
        if not value or value in ("—", "-"):
            continue
        # 先查矩阵值本身是否见于正文。变格语言允许用词干命中，
        # 但前提是矩阵值的词干必须与登记词干一致，否则视为矩阵填错。
        stem = TERM_STEMS.get((lang, term))
        if stem:
            consistent = value.lower().startswith(stem.lower()[:6]) or stem.lower() in value.lower()
            if not consistent:
                issues.append({
                    "file": lang,
                    "type": "term-doubtful-stem",
                    "detail": f"{term} 矩阵作「{value}」，与登记词干「{stem}」不符",
                })
                continue
            hit = stem.lower() in corpus
        else:
            hit = value.lower() in corpus
        if not hit:
            issues.append({
                "file": lang,
                "type": "term-not-in-corpus",
                "detail": f"{term} 矩阵作「{value}」，正文未出现",
            })
    # 说明：曾尝试用「全称（缩写）」展开式自动发现同义异写，但自然语言的
    # 短语边界无法可靠切分（会把定语、从句一并吞入，且单复数与冠词差异
    # 造成大量误报），误报率高于价值，故不纳入自动检查。
    return issues


def list_specs(root, lang):
    """列出语言目录内全部规范文件名。"""
    directory = Path(root) / "locales" / lang
    if not directory.exists():
        return []
    return sorted(path.name for path in directory.glob("*.md"))


def get_spec(root, lang, name):
    """读取指定规范全文。

    只允许读取 locales/<lang>/ 下顶层的 Markdown 文件。名称含路径分隔、
    绝对路径或跳出语种目录的写法一律拒绝，避免被用来读取仓库外文件。
    """
    directory = (Path(root) / "locales" / lang).resolve()
    if not directory.is_dir():
        return ""
    candidate = (directory / name).resolve()
    if candidate.parent != directory or candidate.suffix.lower() != ".md":
        raise ValueError(f"非法文件名：{name}（只允许 {lang} 目录下的 .md 文件）")
    return candidate.read_text(encoding="utf-8") if candidate.exists() else ""


def language_status(root):
    """从根 README 语言表读取各语言完成状态。"""
    readme = Path(root) / "README.md"
    if not readme.exists():
        return []
    try:
        text = readme.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []
    rows = []
    for line in text.splitlines():
        match = re.match(r"^\|\s*([^|]+?)\s*\|\s*([a-zA-Z]{2}-[A-Z]{2})\s*\|\s*([^|]+?)\s*\|", line)
        if match:
            rows.append({
                "language": match.group(1).strip(),
                "code": match.group(2),
                "status": match.group(3).strip(),
            })
    return rows


def optimize(root, lang, fix, backup):
    """执行安全优化：仅为裸代码围栏补充 text 语言标识。

    按文件分组处理，每个文件只读写一次、只备份一次；修改前后行数不变，
    因此同一文件内多处裸围栏可以一次性全部修好。

    支持任意长度的反引号围栏（三重、四重等），补齐时保留原长度：
    四重围栏加语言标识后仍是四重，不会与其内嵌的三重围栏混淆。
    changes 中每项带 fixed 标记，用于区分"已写入"与"仅报告"。
    """
    directory = Path(root) / "locales" / lang
    if not directory.exists():
        return {"fixed": 0, "planned": 0, "changes": []}

    planned = []
    for path in sorted(directory.glob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            print(f"警告：跳过 {path.name}，读取失败：{exc}", file=sys.stderr)
            continue
        for line in analyze_fences(text)["bare_open"]:
            planned.append({"file": path.name, "line": line, "fixed": False})
    if not fix:
        return {"fixed": 0, "planned": len(planned), "changes": planned}

    grouped = {}
    for item in planned:
        grouped.setdefault(item["file"], []).append(item)

    fixed = 0
    for name, items in grouped.items():
        path = directory / name
        try:
            lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        except (OSError, UnicodeDecodeError) as exc:
            print(f"警告：跳过 {name}，读取失败：{exc}", file=sys.stderr)
            continue
        changed = False
        for item in items:
            index = item["line"] - 1
            if not 0 <= index < len(lines):
                continue
            # 拆分行尾再匹配，避免直接用 \s* 把换行符一起吞掉（会造成行数减少）。
            body = lines[index].rstrip("\r\n")
            ending = lines[index][len(body):]
            match = re.match(r"^(`{3,})[ \t]*$", body)
            if not match:
                continue
            lines[index] = f"{match.group(1)}text{ending}"
            item["fixed"] = True
            changed = True
            fixed += 1
        if not changed:
            continue
        if backup:
            shutil.copy2(path, str(path) + ".bak")
        path.write_text("".join(lines), encoding="utf-8")
    return {"fixed": fixed, "planned": len(planned), "changes": planned}


def print_report(report, as_json):
    """输出文本或 JSON 报告。

    按 report["kind"] 显式分发，不靠键名猜测：check 与 status 都含
    "languages" 键，语义却完全不同（一个是语言码列表，一个是状态行）。
    """
    if as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return

    kind = report.get("kind")
    if kind == "check":
        print(f"检查语言：{', '.join(report['languages'])}")
        print(f"文档数：{report['files']}，问题数：{len(report['issues'])}")
        for item in report["issues"]:
            print(f"- {item['file']} / {item['type']}：{item['detail']}")
    elif kind == "xcheck":
        print(f"参考语种：{report['reference']}")
        print(f"比对语种：{', '.join(report['compared']) or '无'}")
        print(f"检查篇目：{report['documents']}，问题数：{len(report['issues'])}")
        for item in report["issues"]:
            print(f"- {item['file']} / {item['type']}：{item['detail']}")
    elif kind == "termcheck":
        print(f"检查语言：{', '.join(report['languages'])}")
        print(f"校验术语：{', '.join(report['terms'])}")
        print(f"问题数：{len(report['issues'])}")
        for item in report["issues"]:
            print(f"- {item['file']} / {item['type']}：{item['detail']}")
    elif kind == "optimize":
        print(f"计划修复：{report['planned']}，已修复：{report['fixed']}")
        for item in report["changes"]:
            mark = "" if item.get("fixed", True) else "（仅报告）"
            print(f"- {item['file']}:{item['line']} → 补 text 语言标识{mark}")
    elif kind == "list":
        for name in report["specs"]:
            print(name)
    elif kind == "spec":
        print(report["content"])
    elif kind == "status":
        for row in report["languages"]:
            print(f"{row['code']}\t{row['status']}\t{row['language']}")
    else:
        raise ValueError(f"未知报告类型：{kind}")


def fail(message):
    """向标准错误输出错误信息，并返回参数错误退出码。"""
    print(f"错误：{message}", file=sys.stderr)
    return EXIT_USAGE


def resolve_langs(lang):
    """把 --lang 解析为语言码列表，对未知语言码给出提示但不阻断。"""
    if lang != "all" and lang not in SUPPORTED_LANGS:
        print(f"警告：{lang} 不在支持列表中，仍按该语言码检查", file=sys.stderr)
    return SUPPORTED_LANGS if lang == "all" else (lang,)


def main():
    """命令行入口。"""
    parser = argparse.ArgumentParser(prog="gitrule", description="Gitrule 文档规范检查与一键优化工具")
    sub = parser.add_subparsers(dest="command", required=True)

    check = sub.add_parser("check", help="检查文档规范一致性")
    check.add_argument("--path", default=".", help="仓库根目录")
    check.add_argument("--lang", default="all", help="语言码或 all")
    check.add_argument("--json", action="store_true", help="输出 JSON")

    optimize_cmd = sub.add_parser("optimize", help="安全优化文档")
    optimize_cmd.add_argument("--path", default=".", help="仓库根目录")
    optimize_cmd.add_argument("--lang", default="all", help="语言码或 all")
    optimize_cmd.add_argument("--fix", action="store_true", help="实际写入修改")
    optimize_cmd.add_argument("--backup", action="store_true", help="写入前生成 .bak")
    optimize_cmd.add_argument("--json", action="store_true", help="输出 JSON")

    listing = sub.add_parser("list", help="列出规范文件")
    listing.add_argument("--path", default=".", help="仓库根目录")
    listing.add_argument("--lang", default="zh-CN", help="语言码")
    listing.add_argument("--json", action="store_true", help="输出 JSON")

    spec = sub.add_parser("spec", help="读取单篇规范全文")
    spec.add_argument("--path", default=".", help="仓库根目录")
    spec.add_argument("--lang", default="zh-CN", help="语言码")
    spec.add_argument("--name", required=True, help="文件名，例如 硬规则.md")
    spec.add_argument("--json", action="store_true", help="输出 JSON")

    status = sub.add_parser("status", help="查看语言适配状态")
    status.add_argument("--path", default=".", help="仓库根目录")
    status.add_argument("--json", action="store_true", help="输出 JSON")

    xcheck = sub.add_parser("xcheck", help="跨语种结构一致性校验")
    xcheck.add_argument("--path", default=".", help="仓库根目录")
    xcheck.add_argument("--lang", default="all", help="待比对语言码或 all")
    xcheck.add_argument("--reference", default="zh-CN", help="参考语种")
    xcheck.add_argument("--json", action="store_true", help="输出 JSON")

    termcheck = sub.add_parser("termcheck", help="术语矩阵与正文用词一致性校验")
    termcheck.add_argument("--path", default=".", help="仓库根目录")
    termcheck.add_argument("--lang", default="all", help="语言码或 all")
    termcheck.add_argument("--json", action="store_true", help="输出 JSON")

    args = parser.parse_args()
    root = os.path.abspath(args.path)

    locales_root = Path(root) / "locales"
    if not locales_root.is_dir():
        return fail(f"未找到 {locales_root}，请用 --path 指定仓库根目录")

    if args.command == "check":
        langs = resolve_langs(args.lang)
        issues = []
        total_files = 0
        for lang in langs:
            directory = locales_root / lang
            if directory.exists():
                total_files += len(list(directory.glob("*.md")))
            issues.extend(check_language(root, lang))
        report = {"kind": "check", "languages": list(langs), "files": total_files, "issues": issues}
        print_report(report, args.json)
        return EXIT_ISSUES if issues else EXIT_OK

    if args.command == "optimize":
        langs = resolve_langs(args.lang)
        all_changes = []
        fixed = 0
        planned = 0
        for lang in langs:
            result = optimize(root, lang, args.fix, args.backup)
            planned += result["planned"]
            fixed += result["fixed"]
            for item in result["changes"]:
                all_changes.append({"lang": lang, **item})
        print_report({"kind": "optimize", "planned": planned, "fixed": fixed, "changes": all_changes}, args.json)
        return EXIT_OK

    if args.command == "list":
        print_report({"kind": "list", "specs": list_specs(root, args.lang)}, args.json)
        return EXIT_OK

    if args.command == "spec":
        try:
            content = get_spec(root, args.lang, args.name)
        except ValueError as exc:
            return fail(str(exc))
        if not content:
            return fail(f"{args.lang} 目录下没有 {args.name}")
        print_report({"kind": "spec", "content": content}, args.json)
        return EXIT_OK

    if args.command == "status":
        print_report({"kind": "status", "languages": language_status(root)}, args.json)
        return EXIT_OK

    if args.command == "xcheck":
        reference_dir = locales_root / args.reference
        if not reference_dir.is_dir():
            return fail(f"参考语种目录不存在：{reference_dir}")
        if args.lang != "all" and args.lang == args.reference:
            return fail("待比对语种与参考语种相同，无需比对")
        langs = [lang for lang in SUPPORTED_LANGS if lang != args.reference]
        if args.lang != "all":
            if args.lang not in SUPPORTED_LANGS:
                print(f"警告：{args.lang} 不在支持列表中，仍按该语言码检查", file=sys.stderr)
            langs = [args.lang]
        issues = []
        for lang in langs:
            issues.extend(cross_check_language(root, lang, args.reference))
        report = {
            "kind": "xcheck",
            "reference": args.reference,
            "compared": langs,
            "documents": len(index_links(reference_dir)),
            "issues": issues,
        }
        print_report(report, args.json)
        return EXIT_ISSUES if issues else EXIT_OK

    if args.command == "termcheck":
        langs = resolve_langs(args.lang)
        issues = []
        for lang in langs:
            issues.extend(term_check_language(root, lang))
        report = {
            "kind": "termcheck",
            "languages": list(langs),
            "terms": list(TERM_MATRIX_TERMS),
            "issues": issues,
        }
        print_report(report, args.json)
        return EXIT_ISSUES if issues else EXIT_OK

    return EXIT_USAGE


if __name__ == "__main__":
    sys.exit(main())
