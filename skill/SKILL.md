---
name: gitrule-optimize
description: Use this skill when a user asks to check, audit, or one-click optimize Markdown documentation sets against the Gitrule specification, including broken links, placeholder registration, code fences, index counts, language coverage, and cross-language structural consistency. Trigger phrases include 文档规范检查, 一键优化文档, 文档一致性检查, Gitrule, 断链检查, 占位符校验, 跨语种校验.
agent_created: true
---

# Gitrule 文档一键优化

## 用途

对 Gitrule 规范文档集执行确定性检查与安全优化。默认只读检查；写入修复必须使用 `--fix`，并建议先备份。

## 何时使用

- 用户要求检查文档集的断链、孤岛、占位符、代码围栏或索引计数。
- 用户要求校验多语种之间的结构一致性（标题、表格、占位符是否漂移）。
- 用户要求“一键优化”文档规范一致性。
- 用户要求按语言码列出规范、读取某篇规范全文，或查看语言适配状态。

## 可执行命令

CLI 位于 `../cli/gitrule.py`，零第三方依赖。

```bash
# 只读检查（默认）
python3 ../cli/gitrule.py check --path <仓库根目录> --lang all

# 输出 JSON，便于程序消费
python3 ../cli/gitrule.py check --path <仓库根目录> --lang all --json

# 预览可安全修复项，不写文件
python3 ../cli/gitrule.py optimize --path <仓库根目录> --lang all

# 执行安全修复并备份
python3 ../cli/gitrule.py optimize --path <仓库根目录> --lang all --fix --backup

# 跨语种结构一致性校验（以某语种为基准，逐篇比对）
python3 ../cli/gitrule.py xcheck --path <仓库根目录> --reference zh-CN

# 只校验单个语种，或输出 JSON
python3 ../cli/gitrule.py xcheck --path <仓库根目录> --lang en-US --reference zh-CN
python3 ../cli/gitrule.py xcheck --path <仓库根目录> --reference zh-CN --json

# 术语矩阵与正文用词一致性校验
python3 ../cli/gitrule.py termcheck --path <仓库根目录>
python3 ../cli/gitrule.py termcheck --path <仓库根目录> --lang ja-JP

# 列出规范 / 读取单篇 / 查看语言状态
python3 ../cli/gitrule.py list --path <仓库根目录> --lang zh-CN
python3 ../cli/gitrule.py spec --path <仓库根目录> --lang zh-CN --name 硬规则.md
python3 ../cli/gitrule.py status --path <仓库根目录>
```

## 工作流程

1. 确定仓库根目录与语言码；未指定时检查 `zh-CN` 与 `en-US`。
2. 先执行只读 `check`，把问题按 `file / type / detail` 汇总给用户。
3. 涉及多语种时，再执行 `xcheck` 以 `zh-CN` 为基准逐篇比对标题、围栏、链接、有序/无序列表、表格形状与占位符集合；差异项定位到具体文件与轴。
4. 术语表有译名矩阵时，执行 `termcheck` 核对矩阵译名与正文用词是否自洽，重点看 `term-not-in-corpus`（矩阵填了正文没有的写法）。
5. 对 `bare-code-fence` 类问题，执行 `optimize` 预览；用户确认后再加 `--fix --backup`。
6. 对 `broken-link`、`unregistered-placeholder`、`index-count`、`cross-*` 等问题，只报告不自动改写，依据 `references/optimization-rules.md` 给出人工修正建议。
7. 修复后再次执行 `check`、`xcheck` 与 `termcheck`，确认问题数归零。

## 安全边界

- 禁止在未经确认的情况下写入文件。
- 禁止自动删除文件、自动重命名规范、自动改写占位符名称。
- `--fix` 仅允许为裸代码块补 `text` 语言标识。
- 其他修复必须先给出差异说明并获得明确确认。

## 资源

- `references/optimization-rules.md`：问题类型、判定依据与人工修正规则。
- `../cli/gitrule.py`：零依赖命令行实现。
- `../mcp/server.py`：MCP stdio 服务器，暴露同名工具。
