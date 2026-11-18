# Gitrule Specification Set

[简体中文](./README.md) | [English](./README_EN.md) | [繁體中文](./locales/zh-TW/README.md) | [日本語](./locales/ja-JP/README.md) | [한국어](./locales/ko-KR/README.md)

![Status](https://img.shields.io/badge/status-5%20of%205%20languages%20delivered-brightgreen?style=flat-square)

> A universal set of specification templates covering the full project lifecycle: from planning, development, and documentation to compliance, release, operations, and programmatic access for AI. The entire repository is MIT-licensed and may be freely used, modified, and redistributed.

> **This repository is the first implementation case of its own specification set**: this README and all documents under `locales/`, `cli/`, `mcp/`, `skill/`, and `expert/` are written according to this specification set and pass its structural checks (broken links, orphan files, index counts, and placeholder registration all report zero issues).

## Purpose

- **Human reading**: each specification is an independent file with a single responsibility; take only what you need, no need to read everything.
- **Expert / Skill / MCP / CLI**: documents use stable file names and language-code paths for programmatic retrieval (conventions in `locales/en-US/machine-readable-metadata-specification.md`).
- **Multilingual**: laid out flat by language code under `locales/`; the same specification maps one to one across language directories.

## Repository Information

- Repository description (`Simplified Chinese | English`): 一套覆盖项目全生命周期的通用规范模板：从立项、开发、文档、合规到发布运维与 AI 程序化调用 | A universal set of documentation templates covering the full project lifecycle, from planning and development to compliance, release, operations, and programmatic access.
- Topics (20, English only): `documentation`, `templates`, `markdown`, `github`, `guidelines`, `open-source`, `developer-tools`, `readme`, `specification`, `standards`, `best-practices`, `multilingual`, `software-development`, `project-management`, `code-review`, `changelog`, `versioning`, `compliance`, `contribution`, `ai-agents`

## Key Features

1. One file, one responsibility: 67 specifications, independently navigable across seven domains.
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
| Simplified Chinese | zh-CN | Complete (67 specs) | [Enter](./locales/zh-CN/README.md) |
| English | en-US | Complete (67 specs) | [Enter](./locales/en-US/README.md) |
| Traditional Chinese | zh-TW | Completed (67 specs) | [Enter](./locales/zh-TW/README.md) |
| Japanese | ja-JP | Completed (67 specs) | [Enter](./locales/ja-JP/README.md) |
| Korean | ko-KR | Completed (67 specs) | [Enter](./locales/ko-KR/README.md) |
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
| 6. Release and operations | Push and release, version management, deployment and rollback, observability, incident response, open-source promotion, migration guide, troubleshooting, iteration retrospective, existing-project alignment checklist |
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
