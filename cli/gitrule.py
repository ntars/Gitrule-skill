#!/usr/bin/env python3
"""Gitrule 文档检查与优化命令行工具。

零第三方依赖，仅使用 Python 标准库。
默认只检查不写文件；--fix 才会执行安全修复。
"""

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path

SUPPORTED_LANGS = ("zh-CN", "en-US", "zh-TW", "ja-JP", "ko-KR", "fr-FR", "de-DE")
PLACEHOLDER_FILE = "README标准模板.md"
INDEX_MARKERS = ("规范总索引", "Specification Master Index", "規範總索引")


def strip_code(text):
    """移除代码块与行内代码，只保留用于扫描的正文。"""
    text = re.sub(r"````.*?````", "", text, flags=re.S)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]+`", "", text)


def analyze_fences(text):
    """检查代码围栏是否配对、哪些开口缺少语言标识。"""
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


def check_links(directory, files):
    """检查同一语言目录内的相对 Markdown 链接是否存在。"""
    issues = []
    for name in files:
        text = (directory / name).read_text(encoding="utf-8")
        for match in re.finditer(
            r"\[([^\]]+)\]\((\.?/?[^)#]+\.md)(?:#[^)]*)?\)", strip_code(text)
        ):
            target = (directory / match.group(2)).resolve()
            if not target.exists():
                issues.append({
                    "file": name,
                    "type": "broken-link",
                    "detail": match.group(2),
                })
    return issues


def check_index(directory, files):
    """检查索引域计数、表格条目数与声明合计是否一致。"""
    if "README.md" not in files:
        return []
    text = (directory / "README.md").read_text(encoding="utf-8")
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


def find_template_file(directory):
    """按语言无关的结构特征定位 README 模板：同时含模板正文与占位符对照表。"""
    for path in sorted(directory.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if "{{" not in text:
            continue
        has_body = re.search(r"(?mi)^##\s+.*(模板正文|template body|模板內文)", text)
        has_table = re.search(r"(?mi)^##\s+.*(占位符对照表|placeholder reference|佔位符對照表)", text)
        if has_body and has_table:
            return path.name
    return None


def check_placeholders(directory):
    """检查 README 模板正文占位符是否全部登记到对照表。"""
    name = find_template_file(directory)
    if not name:
        return []
    text = (directory / name).read_text(encoding="utf-8")
    chunks = re.split(r"(?m)^##\s+", text)
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


def check_language(root, lang):
    """检查单个语言目录，返回结构化问题列表。"""
    directory = Path(root) / "locales" / lang
    if not directory.exists():
        return [{"file": lang, "type": "missing-language", "detail": str(directory)}]
    files = sorted(path.name for path in directory.glob("*.md"))
    issues = []
    for name in files:
        text = (directory / name).read_text(encoding="utf-8")
        if not has_purpose(text):
            issues.append({"file": name, "type": "missing-purpose", "detail": ""})
        if not has_related(text):
            issues.append({"file": name, "type": "missing-related", "detail": ""})
        fences = analyze_fences(text)
        for line in fences["bare_open"]:
            issues.append({"file": name, "type": "bare-code-fence", "detail": f"line {line}"})
        for item in fences["unclosed"]:
            issues.append({"file": name, "type": "unclosed-code-fence", "detail": f"line {item['line']}"})
    issues.extend(check_links(directory, files))
    issues.extend(check_index(directory, files))
    issues.extend(check_placeholders(directory))
    referenced = set()
    for name in files:
        text = (directory / name).read_text(encoding="utf-8")
        for match in re.finditer(r"\]\(\./([^)#]+\.md)\)", strip_code(text)):
            referenced.add(match.group(1))
    for name in files:
        if name != "README.md" and name not in referenced:
            issues.append({"file": name, "type": "orphan", "detail": ""})
    return issues


def list_specs(root, lang):
    """列出语言目录内全部规范文件名。"""
    directory = Path(root) / "locales" / lang
    if not directory.exists():
        return []
    return sorted(path.name for path in directory.glob("*.md"))


def get_spec(root, lang, name):
    """读取指定规范全文。"""
    path = Path(root) / "locales" / lang / name
    return path.read_text(encoding="utf-8") if path.exists() else ""


def language_status(root):
    """从根 README 语言表读取各语言完成状态。"""
    readme = Path(root) / "README.md"
    if not readme.exists():
        return []
    text = readme.read_text(encoding="utf-8")
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
    """执行安全优化：仅为裸代码围栏补充 text 语言标识。"""
    directory = Path(root) / "locales" / lang
    if not directory.exists():
        return {"fixed": 0, "planned": 0, "changes": []}
    planned = []
    for path in sorted(directory.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines(keepends=True)
        for line in analyze_fences("\n".join(lines))["bare_open"]:
            planned.append({"file": path.name, "line": line})
    if not fix:
        return {"fixed": 0, "planned": len(planned), "changes": planned}
    for item in planned:
        path = directory / item["file"]
        if backup:
            shutil.copy2(path, str(path) + ".bak")
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        index = item["line"] - 1
        if lines[index].strip() == "```":
            lines[index] = lines[index].replace("```", "```text", 1)
        path.write_text("".join(lines), encoding="utf-8")
    return {"fixed": len(planned), "planned": len(planned), "changes": planned}


def print_report(report, as_json):
    """输出文本或 JSON 报告。"""
    if as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return
    if "issues" in report:
        issues = report["issues"]
        print(f"检查语言：{', '.join(report['languages'])}")
        print(f"文档数：{report['files']}，问题数：{len(issues)}")
        for item in issues:
            print(f"- {item['file']} / {item['type']}：{item['detail']}")
    elif "changes" in report:
        print(f"计划修复：{report['planned']}，已修复：{report['fixed']}")
        for item in report["changes"]:
            print(f"- {item['file']}:{item['line']} → ```text")
    elif "specs" in report:
        for name in report["specs"]:
            print(name)
    elif "content" in report:
        print(report["content"])
    elif "languages" in report and isinstance(report["languages"], list):
        for row in report["languages"]:
            print(f"{row['code']}\t{row['status']}\t{row['language']}")


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

    args = parser.parse_args()
    root = os.path.abspath(args.path)

    if args.command == "check":
        langs = SUPPORTED_LANGS if args.lang == "all" else (args.lang,)
        issues = []
        total_files = 0
        for lang in langs:
            directory = Path(root) / "locales" / lang
            if directory.exists():
                total_files += len(list(directory.glob("*.md")))
            issues.extend(check_language(root, lang))
        report = {"languages": list(langs), "files": total_files, "issues": issues}
        print_report(report, args.json)
        return 1 if issues else 0

    if args.command == "optimize":
        langs = SUPPORTED_LANGS if args.lang == "all" else (args.lang,)
        all_changes = []
        fixed = 0
        planned = 0
        for lang in langs:
            result = optimize(root, lang, args.fix, args.backup)
            planned += result["planned"]
            fixed += result["fixed"]
            for item in result["changes"]:
                all_changes.append({"lang": lang, **item})
        print_report({"planned": planned, "fixed": fixed, "changes": all_changes}, args.json)
        return 0

    if args.command == "list":
        print_report({"specs": list_specs(root, args.lang)}, args.json)
        return 0

    if args.command == "spec":
        print_report({"content": get_spec(root, args.lang, args.name)}, args.json)
        return 0

    if args.command == "status":
        print_report({"languages": language_status(root)}, args.json)
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())
