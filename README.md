# GitHub 规范化交付规范集

[English](./README_EN.md) | [简体中文](./README.md) | [繁體中文](./locales/zh-TW/README.md) | [日本語](./locales/ja-JP/README.md) | [한국어](./locales/ko-KR/README.md) | [Français](./locales/fr-FR/README.md) | [Deutsch](./locales/de-DE/README.md)

![状态](https://img.shields.io/badge/status-8%20of%208%20语言已交付-brightgreen?style=flat-square)

> 一套覆盖项目全生命周期的通用规范模板：从立项、开发、文档、合规到发布运维与 AI 程序化调用。全仓库采用 MIT 许可证，可自由使用、修改与再发布。

> **本仓库即本规范集的首个实现案例**：本 README 与 `locales/`、`cli/`、`mcp/`、`skill/`、`expert/` 下的全部文档均按本规范集编写，并通过其结构校验（断链、孤岛、索引计数、占位符登记均为 0 问题）。

## 用途

- **人工查阅**：每个规范独立成文件、各司其职，按需取用，不必通读。
- **专家 / Skill / MCP / 命令行**：文档采用稳定文件名与语言码路径，便于程序化检索（约定见 `locales/zh-CN/机器可读元数据规范.md`）。
- **多语言**：按语言码分目录平铺，同一规范在各语言目录中一一对应。

## 仓库信息

- 仓库描述（`简体中文 | English`）：一套覆盖项目全生命周期的通用规范模板：从立项、开发、文档、合规到发布运维与 AI 程序化调用 | A universal set of documentation templates covering the full project lifecycle, from planning and development to compliance, release, operations, and programmatic access.
- 话题标签（20 个，仅英文）：`documentation`、`templates`、`markdown`、`github`、`guidelines`、`open-source`、`developer-tools`、`readme`、`specification`、`standards`、`best-practices`、`multilingual`、`software-development`、`project-management`、`code-review`、`changelog`、`versioning`、`compliance`、`contribution`、`ai-agents`

## 核心特性

1. 一文件一职责：67 篇规范各自独立，按七域导航，不必通读。
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
| 简体中文 | zh-CN | 已完成（67 篇） | [进入](./locales/zh-CN/README.md) |
| 英语 | en-US | 已完成（67 篇） | [进入](./locales/en-US/README.md) |
| 繁体中文 | zh-TW | 已完成（67 篇） | [进入](./locales/zh-TW/README.md) |
| 日语 | ja-JP | 已完成（67 篇） | [进入](./locales/ja-JP/README.md) |
| 韩语 | ko-KR | 已完成（67 篇） | [进入](./locales/ko-KR/README.md) |
| 法语 | fr-FR | 已完成（67 篇） | [进入](./locales/fr-FR/README.md) |
| 德语 | de-DE | 已完成（67 篇） | [进入](./locales/de-DE/README.md) |
| 西班牙语 | es-ES | 已完成（67 篇） | [进入](./locales/es-ES/README.md) |
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
| 六、发布与运维 | 推送与发布、版本管理、部署与回滚、可观测性、事故响应、开源推广、迁移指南、故障排查、迭代回顾、存量项目对齐检查 |
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
