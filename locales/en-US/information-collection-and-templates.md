# Information Collection and Templates

> What this file solves: Defines the project information fields that must be collected before writing documentation, the marking rules for unconfirmed information, and provides a placeholder index, a terminology mapping template, a dependency list template, and copy-ready project information collection text.

## 1. Required Fields (a missing field blocks progress)

| Field | Description | Affected Sections |
| --- | --- | --- |
| Project name | The repository name and the display name; when the two differ, this must be explained | Whole document |
| One-sentence positioning | No more than 60 characters, stating what the project is and what problem it solves for whom | Chapter 1 |
| Repository description (native language and English) | No more than 120 characters in each language, stating the project type and core purpose respectively | Chapter 1 |
| Topics | 5–10 lowercase English words joined with `-`; mixed capitalization counts as a missing item | Chapter 1 |
| Project background | Reason for project initiation, shortcomings of existing solutions | Chapter 2 |
| Core feature list | Grouped by module, including user-perceivable behaviors | Chapter 3 |
| Technology stack | Language, framework, runtime version constraints | Chapter 6 |
| Dependency list | Name, version, license, copyright holder, source address | Chapter 6, NOTICE |
| License type | The project's own license, which must be an SPDX identifier | Chapter 19 |
| Copyright holder | Individual name or full organization name, together with the year | Chapter 19, NOTICE |
| Installation and running methods | Environment requirements, commands, expected results | Chapters 7, 8 |

## 2. Optional Fields

Configuration item list, API definitions, directory structure, performance test data, compatibility matrix, known issues, changelog, roadmap, contribution process, security policy, screenshots and demo addresses, external asset sources.

## 3. Field Filling Notes and Examples

| Field | Filling Notes | Example |
| --- | --- | --- |
| Project name | Repository name uses lowercase letters, digits, and `-`; the display name may use brand styling; when the two differ, state the reason | Repository name `markdown-lint-cli`, display name `Markdown Lint CLI` |
| One-sentence positioning | Includes a category word and a qualifier, does not pile up adjectives, no more than 60 characters | `A Markdown specification checking CLI tool for technical documentation teams` |
| Repository description (native language and English) | The native language and English each form an independent sentence, each no more than 120 characters, and a slogan must not replace the description | `中文：检查 Markdown 文档结构的命令行工具` / `English: A CLI tool for checking Markdown document structure` |
| Topics | All lowercase, words joined with `-`, prioritizing language, form, use, and ecosystem | `go cli markdown linter developer-tools` |
| Technology stack | State the primary language, framework, and runtime version constraints; do not write "latest version" | `Go >= 1.22; Cobra v1.8.x` |
| Dependency list | Each item includes version, license, copyright holder, and official address; items of unknown origin are marked as unconfirmed | See the dependency list table template in Appendix C |
| License type | Use an SPDX identifier, not vague phrases such as "open source" or "free to use" | `MIT` |
| Installation and running methods | Give the current working directory, the full command, and a verifiable expected output | Run `go install ./cmd/mdlint` in the repository root; the version number is output |
| Unconfirmed item | Use a fixed marker, state the missing content and the person responsible for supplementing it; do not substitute "tentative" | `【To be confirmed: license type of dependency foo, responsible person: 张三】` |

## 4. Marking Rules for Unconfirmed Information

1. Unified format: `【To be confirmed: specifically what is missing】`; vague expressions such as "tentative", "approximately", or "possibly" must not be used as substitutes.
2. Marking location: one place at the corresponding location in the body text, and list it once more in the "Summary of Items to Be Confirmed" at the end of the document.
3. Unconfirmed items involving licenses, copyright, or dependency sources must be explicitly marked in NOTICE; the entire entry must not be omitted.
4. The summary of items to be confirmed must include the number, field, missing content, person responsible for supplementing it, and planned completion time; entries without a responsible person or time must not enter Phase 0 (see [Execution Flow](./execution-process.md)).

## 5. Appendix A · Placeholder Index

`{{项目名称}}`、`{{一句话定位}}`、`{{当前版本}}`、`{{维护状态}}`、`{{许可证 SPDX}}`、`{{著作权人}}`、`{{年份}}`、`{{分支名}}`、`{{仓库地址}}`、`{{最低运行时版本}}`

Usage rules:

1. This index lists only the basic fields from the collection stage; for the full set of README placeholders and their descriptions, refer to the placeholder mapping table in the [README Standard Template](./readme-standard-template.md).
2. Formal placeholders are uniformly written as `{{纯名}}`; explanatory text, backticks, or a second placeholder must not be nested inside the braces; natural-language content within braces in specification examples is not considered a formal placeholder.
3. Natural-language fields in the collection table do not use placeholders directly; when generating the README, map them to the corresponding placeholders according to the mapping table, and no explanatory brace content may remain in the final document.

## 6. Appendix B · Chinese-English Terminology Mapping Table Template

| Chinese | English | Abbreviation | Description |
| --- | --- | --- | --- |
| TBD | TBD | — | — |

## 7. Appendix C · Dependency List Table Template

| No. | Component Name | Version | Reference Method | Copyright Holder | License | Official Address | Use in This Project | Modified | Modification Notes | Original Location |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TBD | TBD | Direct | TBD | TBD | TBD | TBD | No | None | TBD |

Field requirements are in the [Open Source Compliance Specification](./open-source-compliance-specification.md).

## 8. Project Information Filling Area

After supplementing the project information below, begin Phase 0 (see [Execution Flow](./execution-process.md)).

- Project name:
- One-sentence positioning:
- Repository description (native language and English):
- Topics:
- Project background:
- Core features:
- Technology stack and versions:
- Dependency list (or dependency list file path):
- License type:
- Copyright holder and year:
- Installation and running methods:
- Repository address and target branch:
- Other supplementary materials:

## 9. Appendix D · Copy-Ready Project Information Collection Text

Copy the following into the target project's `项目信息采集表.md` and replace the content after each "Fill in:" item by item. Fields that cannot be confirmed are marked according to the rules in Section 4 and summarized in Section 8.

````markdown
# Project Information Collection Form

> This file is used for one-time collection of the information needed to generate documentation. After completion, generate the README, NOTICE, and other deliverable documents based on the collection results.

## 1. Basic Information

| Field | Content to Fill In |
| --- | --- |
| Repository name | Fill in: a repository name composed of lowercase letters, digits, and hyphens |
| Display name | Fill in: the externally displayed project name; if identical to the repository name, write "same as repository name" |
| Repository address | Fill in: the full HTTPS address |
| Target branch | Fill in: the default branch name |
| Language code | Fill in: the preferred language code, such as zh-CN |
| Current version | Fill in: a semantic version number or "unreleased" |
| Maintenance status | Fill in: actively maintained / low-frequency maintenance / archived |

## 2. Positioning and Scope

| Field | Content to Fill In |
| --- | --- |
| One-sentence positioning | Fill in: no more than 60 characters, including a category word and a qualifier |
| Repository description (native language) | Fill in: no more than 120 characters |
| Repository description (English) | Fill in: no more than 120 characters |
| Topics | Fill in: 5–10 lowercase English words joined with hyphens |
| Project background | Fill in: the reason for project initiation and the shortcomings of existing solutions |
| Applicable scenarios | Fill in: list item by item, each with a trigger condition |
| Inapplicable scenarios | Fill in: list item by item, each with a reason |
| Advantages | Fill in: each with verifiable evidence |
| Limitations | Fill in: each with scope of impact and workaround |

## 3. Features and Highlights

| Module | User-Perceivable Behavior | Trigger Condition | Result | Evidence or Link |
| --- | --- | --- | --- | --- |
| Fill in: module name | Fill in: behavior description | Fill in: trigger method | Fill in: output or state change | Fill in: test, screenshot, or documentation link |

## 4. Technology and Dependencies

| Field | Content to Fill In |
| --- | --- |
| Primary language and version constraints | Fill in: e.g. `Go >= 1.22` |
| Framework and build tools | Fill in: names and version constraints |
| Runtime and system requirements | Fill in: operating system, runtime, browser, or database version |
| Dependency list | Fill in: the dependency list file path, or insert the Appendix C table in this section |
| External assets | Fill in: the sources and licenses of fonts, images, icons, and datasets |

## 5. Delivery and Usage

| Field | Content to Fill In |
| --- | --- |
| Environment requirements | Fill in: prerequisites that must be met before installation |
| Installation command | Fill in: the full command including the current working directory description |
| Verification command and expected output | Fill in: a directly executable command and a verifiable result |
| Upgrade and uninstall methods | Fill in: commands or operation steps |
| Configuration item list | Fill in: key name, type, default value, whether required, value range, and purpose |
| API or module description | Fill in: interface signature, parameters, return values, error codes, and call examples |
| Compatibility matrix | Fill in: explicitly state supported and unsupported version combinations |
| Performance data | Fill in: test environment, method, metrics, and bottlenecks; if no data, write "not provided, must not be inferred" |

## 6. Risks and Boundaries

| Field | Content to Fill In |
| --- | --- |
| Known issues | Fill in: description, scope of impact, temporary workaround, and tracking link |
| Current limitations | Fill in: explicitly state what the current version cannot do |
| Unimplemented features | Fill in: feature, reason for non-implementation, and planned status |
| Security and privacy | Fill in: data collection, storage, transmission, permission model, and known risks |
| Vulnerability reporting channel | Fill in: email, issue template, or dedicated address |

## 7. Compliance and Responsibility

| Field | Content to Fill In |
| --- | --- |
| License type | Fill in: an SPDX identifier, such as `MIT` |
| Copyright holder | Fill in: individual name or full organization name |
| Copyright year | Fill in: a year or year range |
| Location of full license text | Fill in: the LICENSE file path |
| NOTICE file path | Fill in: the NOTICE file path; if there are no third-party dependencies, write "not applicable, reason: ..." |
| Disclaimer | Fill in: the boundary of responsibility or the adoption status of warranty disclaimers |

## 8. Summary of Items to Be Confirmed

| No. | Field | Missing Content | Person Responsible for Supplementing | Planned Completion Time | Scope of Impact |
| --- | --- | --- | --- | --- | --- |
| T-001 | Fill in: field name | Fill in: specifically what is missing | Fill in: name or role | Fill in: YYYY-MM-DD | Fill in: affected sections or gates |

## 9. Related Specifications

- Section structure: [README Sections Specification](./readme-sections-specification.md)
- Copy-ready template: [README Standard Template](./readme-standard-template.md)
- Dependency field details: [Open Source Compliance Specification](./open-source-compliance-specification.md)
- Gate determination: [Quality Gates](./quality-gate.md)
````

## Related Files

- Question-asking rules and Phase 0 entry conditions are in [Execution Flow](./execution-process.md)
- The section impact mapping is in [README Sections Specification](./readme-sections-specification.md)
- The full README placeholder mapping is in [README Standard Template](./readme-standard-template.md)
- Dependency field details are in [Open Source Compliance Specification](./open-source-compliance-specification.md)
- The summary of items to be confirmed belongs to gate G12, see [Quality Gates](./quality-gate.md)
