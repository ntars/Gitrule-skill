# GitHub 规范化交付规范集

> 一套覆盖项目全生命周期的通用规范模板：从立项、开发、文档、合规到发布运维与 AI 程序化调用。全仓库采用 MIT 许可证，可自由使用、修改与再发布。

> **本仓库即本规范集的首个实现案例**：本 README 与 `locales/`、`cli/`、`mcp/`、`skill/`、`expert/` 下的全部文档均按本规范集编写，并通过其结构校验（断链、孤岛、索引计数、占位符登记均为 0 问题）。

## 用途

- **人工查阅**：每个规范独立成文件、各司其职，按需取用，不必通读。
- **专家 / Skill / MCP / 命令行**：文档采用稳定文件名与语言码路径，便于程序化检索（约定见 `locales/zh-CN/机器可读元数据规范.md`）。
- **多语言**：按语言码分目录平铺，同一规范在各语言目录中一一对应。

## 仓库信息

- 仓库描述（简体中文）：一套覆盖项目全生命周期的通用规范模板：从立项、开发、文档、合规到发布运维与 AI 程序化调用。
- Repository description (English): A universal set of documentation templates covering the full project lifecycle, from planning and development to compliance, release, operations, and programmatic access.
- 话题标签（建议）：`documentation`、`templates`、`markdown`、`github`、`guidelines`、`open-source`、`developer-tools`

## 核心特性

1. 一文件一职责：66 篇规范各自独立，按七域导航，不必通读。
2. 全生命周期：八阶段映射覆盖立项、需求、架构、开发、测试、部署、运维与迭代。
3. 多语言就绪：语言码集中在 `locales/`，新增语言不改动已有文件。
4. 机器可读：每条规范有稳定标识与路径映射，并提供可复制清单示例。

## 优势与局限

- 优势：字段定义、填写说明与完整示例齐备；MIT 许可与免责声明边界明确；核心交付物提供可复制模板；附带零依赖 CLI、MCP 服务器、Skill 与专家包四种程序化接入方式。
- 局限：内容为方法论模板，不含可执行校验脚本；示例参数须按项目实际替换；法律文本译文仅供参考，以原文为准。

## 已知问题与未实现功能

- 已完成简体中文与英文两套规范；其余语言按指令逐次新增。
- 机器可读清单以规范与示例形式提供，仓库内未放置独立 `manifest.json`；程序化接入时需按示例生成。
- 自动化校验脚本目前只覆盖结构类问题（断链、孤岛、代码围栏、索引计数、占位符登记），语义级校对仍需人工。

## 后续路线图

- 按指令逐次新增 `ja-JP`、`ko-KR` 等语言目录，并同步根语言导航。
- 如需程序化接入，可基于清单示例生成独立 `manifest.json`。
- 按需扩展 CLI 的自动修复范围与 CI 集成。
- 以上均为非承诺计划，按实际需要调整。

## AI 可调用适配器

仓库自带四种 AI 程序化接入方式，全部零第三方依赖（仅需 Python 3.8+），支持一键检查与一键优化：

| 接入方式 | 位置 | 用途 |
| --- | --- | --- |
| 命令行 | [cli/gitrule.py](./cli/gitrule.py) | `check` 检查断链、孤岛、职责句、代码围栏、索引计数、占位符登记；`optimize` 执行安全自动修复；`list` / `spec` / `status` 浏览规范文件与语言状态 |
| MCP 服务器 | [mcp/server.py](./mcp/server.py) | stdio JSON-RPC，提供 `gitrule_check`、`gitrule_optimize`、`gitrule_list_specs`、`gitrule_get_spec`、`gitrule_language_status` 五个工具，可直接注册到任意 MCP 客户端 |
| WorkBuddy Skill | [skill/SKILL.md](./skill/SKILL.md) | 一键优化文档规范，含优化规则参考，已按 Skill 规范打包（`dist/gitrule-optimize.zip`） |
| WorkBuddy 专家包 | [expert/](./expert/) | 文档规范优化专家，面向对话式检查与修复，含头像与快速提示词 |

CLI 示例：

```bash
# 只读检查全部语言
python3 cli/gitrule.py check --path . --lang all --json

# 列出某语言目录内全部规范
python3 cli/gitrule.py list --lang zh-CN --path .

# 对中文规范执行安全自动修复
python3 cli/gitrule.py optimize --path . --lang zh-CN
```

MCP 注册示例（写入 MCP 配置的 `mcpServers`）：

```json
{
  "gitrule": {
    "command": "python3",
    "args": ["/绝对路径/Gitrule-skill/mcp/server.py"]
  }
}
```

## 语言

| 语言 | 代码 | 状态 | 入口 |
| --- | --- | --- | --- |
| 简体中文 | zh-CN | 已完成（66 篇） | [进入](./locales/zh-CN/README.md) |
| 英语 | en-US | 已完成（66 篇） | [进入](./locales/en-US/README.md) |
| 繁体中文 | zh-TW | 待补充 | — |
| 日语 | ja-JP | 待补充 | — |
| 韩语 | ko-KR | 待补充 | — |
| 法语 | fr-FR | 待补充 | — |
| 德语 | de-DE | 待补充 | — |
| 西班牙语 | es-ES | 待补充 | — |
| 葡萄牙语（巴西） | pt-BR | 待补充 | — |
| 俄语 | ru-RU | 待补充 | — |
| 阿拉伯语 | ar-SA | 待补充 | — |
| 印地语 | hi-IN | 待补充 | — |

新增语言只需新建对应语言目录并按同一规范翻译，不改动已有语言文件。

## 规范分类（七大域）

| 域 | 内容 |
| --- | --- |
| 一、总纲与治理 | 生命周期映射、规范选用指南、角色职责、执行流程、硬规则、禁止事项、术语表、贡献指南、行为准则、免责声明 |
| 二、规划与立项 | 立项与需求、路线图、信息采集与模板 |
| 三、命名与文档 | 项目命名、文档矩阵、README 章节、写作规范、多语言、特性写法、变更日志、API 文档、Issue 与 PR 模板，基于头部项目调研的 README 模板、视觉排版、徽章规范与分类适配，以及免责声明、行为准则、贡献指南、SECURITY 四类可复制模板 |
| 四、开发与工程 | 代码风格、Git 工作流、提交信息、代码审查、测试、依赖管理、架构设计、API 设计、数据库设计、CI 工作流、代码所有权、可访问性 |
| 五、质量与合规 | 审核维度、质量门禁、质量度量、开源合规、NOTICE、LICENSE、安全与隐私、审核报告格式、需求追踪矩阵 |
| 六、发布与运维 | 推送与发布、版本管理、部署与回滚、可观测性、事故响应、开源推广、迁移指南、故障排查、迭代回顾 |
| 七、AI 与机器适配 | 机器可读元数据、Skill 编写、MCP 工具、Agent 调用与提示词 |

完整文件清单与阅读路径见 [简体中文入口](./locales/zh-CN/README.md)。

## 快速开始

1. 确定使用场景：人工查阅、文档生成，还是程序化接入。
2. 先读[规范选用指南](./locales/zh-CN/规范选用指南.md)确定裁剪范围，再按[生命周期映射表](./locales/zh-CN/生命周期映射表.md)定位当前阶段所需的规范；阶段之间无强制前后依赖，但退出门禁不可跳过。
3. 程序化接入时，先读机器可读元数据规范，再按语言码 + 标识取用文档。

## 可复制模板

下列文件已含占位符对照表、填写说明与完整示例，可直接复制到目标项目后替换：

| 模板 | 用途 | 配套规范 |
| --- | --- | --- |
| [README标准模板](./locales/zh-CN/README标准模板.md) | 覆盖 20 章的项目首页 | README章节规范 |
| [免责声明模板](./locales/zh-CN/免责声明模板.md) | 界定责任边界与不担保条款 | 免责声明 |
| [贡献指南模板](./locales/zh-CN/贡献指南模板.md) | 外部贡献者的参与流程 | 贡献指南规范 |
| [行为准则模板](./locales/zh-CN/行为准则模板.md) | 社区行为准则与处置机制 | 行为准则规范 |
| [SECURITY模板](./locales/zh-CN/SECURITY模板.md) | 漏洞上报渠道与响应时限 | 安全与隐私规范 |
| [信息采集与模板](./locales/zh-CN/信息采集与模板.md) | 立项前一次性采集字段与待确认事项 | 项目立项与需求规范 |
| [审核报告格式](./locales/zh-CN/审核报告格式.md) | 推送前逐维度证据与放行结论 | 质量门禁 |
| [迁移指南规范](./locales/zh-CN/迁移指南规范.md) | 破坏性变更的分版本迁移步骤 | 变更日志规范 |
| [Issue与PR模板规范](./locales/zh-CN/Issue与PR模板规范.md) | 结构化 Issue 表单与 PR 自查清单 | 贡献指南规范 |

## 许可证与免责

本项目采用 MIT 许可证，全文见 [LICENSE](./LICENSE)。各语言规范内容同样适用 MIT。

规范内容按「现状」提供参考，不构成法律意见或专业咨询，使用前应自行评估适用性并验证结果。责任边界与不担保条款见 [简体中文免责声明](./locales/zh-CN/免责声明.md)；其他语言目录建立后提供对应译本。

---

# Gitrule Specification Set (English)

> A universal set of specification templates covering the full project lifecycle: from planning, development, and documentation to compliance, release, operations, and programmatic access for AI. The entire repository is MIT-licensed and may be freely used, modified, and redistributed.

> **This repository is the first implementation case of its own specification set**: this README and all documents under `locales/`, `cli/`, `mcp/`, `skill/`, and `expert/` are written according to this specification set and pass its structural checks (broken links, orphan files, index counts, and placeholder registration all report zero issues).

## Purpose

- **Human reading**: each specification is an independent file with a single responsibility; take only what you need, no need to read everything.
- **Expert / Skill / MCP / CLI**: documents use stable file names and language-code paths for programmatic retrieval (conventions in `locales/en-US/machine-readable-metadata-specification.md`).
- **Multilingual**: laid out flat by language code under `locales/`; the same specification maps one to one across language directories.

## Repository Information

- Repository description (Simplified Chinese): 一套覆盖项目全生命周期的通用规范模板：从立项、开发、文档、合规到发布运维与 AI 程序化调用。
- Repository description (English): A universal set of documentation templates covering the full project lifecycle, from planning and development to compliance, release, operations, and programmatic access.
- Suggested topics: `documentation`, `templates`, `markdown`, `github`, `guidelines`, `open-source`, `developer-tools`

## Key Features

1. One file, one responsibility: 66 specifications, independently navigable across seven domains.
2. Full lifecycle: eight-stage mapping from planning, requirements, architecture, development, and testing to deployment, operations, and iteration.
3. Multilingual ready: language codes centralized in `locales/`; adding a language changes no existing file.
4. Machine readable: stable identifiers and path mappings per specification, with a copy-ready manifest example.

## Strengths and Limitations

- Strengths: field definitions, filling instructions, and complete examples; clear MIT licensing and disclaimer boundaries; copy-ready templates for core deliverables; four programmatic adapters with zero third-party dependencies (CLI, MCP server, Skill, and Expert package).
- Limitations: methodology templates only; sample parameters must be replaced per project; translations of legal text are for reference only and the original text prevails.

## Known Issues and Unimplemented Features

- Simplified Chinese and English specification sets are complete; other languages are added on instruction.
- The machine-readable manifest is provided as specification and example only; no standalone `manifest.json` is placed in the repository.
- Automated checks currently cover structural issues only (broken links, orphans, code fences, index counts, placeholder registration); semantic proofreading remains manual.

## Roadmap

- Add `ja-JP`, `ko-KR`, and other language directories on instruction, and keep root navigation in sync.
- Generate a standalone `manifest.json` from the manifest example when programmatic access requires it.
- Extend CLI auto-fix coverage and CI integration as needed.
- All items are non-committal plans, adjusted to actual needs.

## AI-Callable Adapters

Four programmatic adapters ship with the repository, all with zero third-party dependencies (Python 3.8+ only), supporting one-click checking and one-click optimization:

| Adapter | Location | Purpose |
| --- | --- | --- |
| CLI | [cli/gitrule.py](./cli/gitrule.py) | `check` for broken links, orphans, responsibility lines, code fences, index counts, and placeholder registration; `optimize` for safe auto-fixes; `list` / `spec` / `status` to browse specifications and language status |
| MCP server | [mcp/server.py](./mcp/server.py) | stdio JSON-RPC exposing five tools: `gitrule_check`, `gitrule_optimize`, `gitrule_list_specs`, `gitrule_get_spec`, `gitrule_language_status` |
| WorkBuddy Skill | [skill/SKILL.md](./skill/SKILL.md) | One-click documentation optimization with optimization rules reference, packaged per the Skill specification (`dist/gitrule-optimize.zip`) |
| WorkBuddy Expert | [expert/](./expert/) | Documentation standards optimizer for conversational checking and fixing, with avatar and quick prompts |

CLI examples:

```bash
# Read-only check across all languages
python3 cli/gitrule.py check --path . --lang all --json

# List specifications in a language directory
python3 cli/gitrule.py list --lang zh-CN --path .

# Run safe auto-fixes on the Chinese set
python3 cli/gitrule.py optimize --path . --lang zh-CN
```

MCP registration example (into the `mcpServers` block of an MCP configuration):

```json
{
  "gitrule": {
    "command": "python3",
    "args": ["/absolute/path/Gitrule-skill/mcp/server.py"]
  }
}
```

## Languages

| Language | Code | Status | Entry |
| --- | --- | --- | --- |
| Simplified Chinese | zh-CN | Complete (66 specs) | [Enter](./locales/zh-CN/README.md) |
| English | en-US | Complete (66 specs) | [Enter](./locales/en-US/README.md) |
| Traditional Chinese | zh-TW | Planned | — |
| Japanese | ja-JP | Planned | — |
| Korean | ko-KR | Planned | — |
| French | fr-FR | Planned | — |
| German | de-DE | Planned | — |
| Spanish | es-ES | Planned | — |
| Portuguese (Brazil) | pt-BR | Planned | — |
| Russian | ru-RU | Planned | — |
| Arabic | ar-SA | Planned | — |
| Hindi | hi-IN | Planned | — |

Adding a language only requires creating the corresponding directory and translating according to the same specifications, without changing existing language files.

## Specification Categories (Seven Domains)

| Domain | Content |
| --- | --- |
| 1. Governance | Lifecycle mapping, specification selection guide, roles and responsibilities, execution process, hard rules, prohibited practices, glossary, contribution guide, code of conduct, disclaimer |
| 2. Planning | Project initiation and requirements, roadmap, information collection and templates |
| 3. Naming and documentation | Project naming, document matrix, README sections, writing standards, multilingual, feature writing, changelog, API documentation, Issue and PR templates, plus README template research, visual layout, badges, and category adaptation based on top-project research, and four copy-ready templates (disclaimer, code of conduct, contribution guide, SECURITY) |
| 4. Development and engineering | Code style, Git workflow, commit messages, code review, testing, dependency management, architecture design, API design, database design, CI workflow, code ownership, accessibility |
| 5. Quality and compliance | Review dimension matrix, quality gates, quality metrics, open-source compliance, NOTICE, LICENSE, security and privacy, audit report format, requirements traceability matrix |
| 6. Release and operations | Push and release, version management, deployment and rollback, observability, incident response, open-source promotion, migration guide, troubleshooting, iteration retrospective |
| 7. AI and machine adaptation | Machine-readable metadata, Skill authoring, MCP tools, Agent invocation and prompts |

The full file list and reading paths are in the [English entry](./locales/en-US/README.md).

## Quick Start

1. Determine the use case: human reading, document generation, or programmatic access.
2. Read the [specification selection guide](./locales/en-US/specification-selection-guide.md) to determine the trimmed scope, then locate the specifications for the current stage via the [lifecycle mapping table](./locales/en-US/lifecycle-mapping-table.md); stages have no mandatory ordering, but exit gates cannot be skipped.
3. For programmatic access, read the machine-readable metadata specification first, then retrieve documents by language code + identifier.

## Copy-Ready Templates

The following files contain placeholder tables, filling instructions, and complete examples; copy them into a target project and replace the placeholders:

| Template | Purpose | Companion specification |
| --- | --- | --- |
| [README standard template](./locales/en-US/readme-standard-template.md) | Project front page covering 20 sections | README sections specification |
| [Disclaimer template](./locales/en-US/disclaimer-template.md) | Responsibility boundaries and warranty disclaimer | Disclaimer |
| [Contribution guide template](./locales/en-US/contribution-guide-template.md) | Participation process for external contributors | Contribution guide specification |
| [Code of conduct template](./locales/en-US/code-of-conduct-template.md) | Community conduct rules and enforcement | Code of conduct specification |
| [SECURITY template](./locales/en-US/security-template.md) | Vulnerability reporting channels and response timelines | Security and privacy specification |
| [Information collection and templates](./locales/en-US/information-collection-and-templates.md) | One-time field collection before project initiation | Project initiation and requirements specification |
| [Audit report format](./locales/en-US/audit-report-format.md) | Per-dimension evidence and release decisions before push | Quality gates |
| [Migration guide specification](./locales/en-US/migration-guide-specification.md) | Per-version migration steps for breaking changes | Changelog specification |
| [Issue and PR template specification](./locales/en-US/issue-and-pr-template-specification.md) | Structured Issue forms and PR checklists | Contribution guide specification |

## License and Disclaimer

This project is MIT-licensed; see [LICENSE](./LICENSE) for the full text. Specification content in all languages is equally covered by the MIT license.

Specifications are provided "as is" for reference and do not constitute legal advice or professional consulting; evaluate applicability and verify results before use. Responsibility boundaries and warranty disclaimer: see the [English disclaimer](./locales/en-US/disclaimer.md); translations for other languages follow once those language directories are established.
