---
name: gitrule-optimize
description: Use this skill when a user asks to check, audit, or one-click optimize Markdown documentation sets against the Gitrule specification, including broken links, placeholder registration, code fences, index counts, and language coverage. Trigger phrases include 文档规范检查, 一键优化文档, Gitrule, 断链检查, 占位符校验.
agent_created: true
---

# Gitrule 文档一键优化

## 用途

对 Gitrule 规范文档集执行确定性检查与安全优化。默认只读检查；写入修复必须使用 `--fix`，并建议先备份。

## 何时使用

- 用户要求检查文档集的断链、孤岛、占位符、代码围栏或索引计数。
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

# 列出规范 / 读取单篇 / 查看语言状态
python3 ../cli/gitrule.py list --path <仓库根目录> --lang zh-CN
python3 ../cli/gitrule.py spec --path <仓库根目录> --lang zh-CN --name 硬规则.md
python3 ../cli/gitrule.py status --path <仓库根目录>
```

## 工作流程

1. 确定仓库根目录与语言码；未指定时检查 `zh-CN` 与 `en-US`。
2. 先执行只读 `check`，把问题按 `file / type / detail` 汇总给用户。
3. 对 `bare-code-fence` 类问题，执行 `optimize` 预览；用户确认后再加 `--fix --backup`。
4. 对 `broken-link`、`unregistered-placeholder`、`index-count` 等问题，只报告不自动改写，依据 `references/optimization-rules.md` 给出人工修正建议。
5. 修复后再次执行 `check`，确认问题数归零。

## 安全边界

- 禁止在未经确认的情况下写入文件。
- 禁止自动删除文件、自动重命名规范、自动改写占位符名称。
- `--fix` 仅允许为裸代码块补 `text` 语言标识。
- 其他修复必须先给出差异说明并获得明确确认。

## 资源

- `references/optimization-rules.md`：问题类型、判定依据与人工修正规则。
- `../cli/gitrule.py`：零依赖命令行实现。
- `../mcp/server.py`：MCP stdio 服务器，暴露同名工具。
