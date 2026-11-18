# README Standard Template

> What this file solves: Provides a general README template that can be copied directly and applied by replacing placeholders, covering the front-page presentation of the project's complete lifecycle. It includes a placeholder reference table, optional section notes, and a pre-delivery self-check checklist, so that any developer can quickly customize it for their own project.

## 1. Usage Instructions

1. Copy all content of "Template Body" in Section 3 and create it as `README.md` in the project root.
2. Replace each `{{...}}` according to the placeholder reference table in Section 4; delete unused items together with their entire line or section.
3. Each subsection of Section 3 corresponds to the 20 chapters of [README Section Specification](./readme-sections-specification.md), arranged in lifecycle order from inside to outside; when deleting a chapter, the corresponding link in the first-screen navigation must be deleted as well.
4. Unify badge style, color, and quantity according to [Badge Specification](./badge-specification.md); check the placement of screenshots, tables, and code blocks according to [README Visual Layout Specification](./readme-visual-layout-specification.md).
5. Select sections by project type according to [README Category Adaptation Guide](./readme-category-adaptation-guide.md).
6. Before committing, run the self-check checklist in Section 6 to confirm no residual placeholders.

## 2. Customization Principles

- **Required items**: Project name, repository description, one-line positioning, installation, Quick Start, license.
- **Fixed order**: Section order is consistent with [README Section Specification](./readme-sections-specification.md), with Chinese and English versions corresponding chapter by chapter.
- **Evidence first**: Key features, performance, and engineering trade-offs must provide verifiable evidence; qualitative praise is prohibited.
- **Transparent disclosure**: Inapplicable scenarios, limitations, known issues, and unimplemented features must be explicitly listed, not concealed.
- **Not a commitment**: The roadmap is marked "not a commitment", with no specific delivery dates.
- **Authenticity**: All commands, examples, links, and badges must actually work; contact information and reporting channels must be genuinely reachable.

## 3. Template Body

This section is organized "from inside to outside" by project lifecycle, with 20 subsections corresponding one-to-one to the 20 chapters of [README Section Specification](./readme-sections-specification.md). The text inside each code block is the copyable body.

The mapping between chapters and lifecycle stages is as follows, for easy location as needed:

| Lifecycle Stage | Corresponding Subsection | Presentation Focus |
| --- | --- | --- |
| Project Initiation | 3.1–3.2 | Positioning, background, applicable scenarios and limitations |
| Requirements Analysis | 3.2–3.3 | Feature boundaries, applicable and inapplicable scenarios |
| Architecture Design | 3.5–3.6, 3.11 | Engineering trade-offs, tech stack, directory structure |
| Development | 3.3–3.4, 3.9–3.10 | Functions, key features, configuration, API |
| Testing & Verification | 3.8, 3.12 | Quick Start example, performance evidence |
| Deployment | 3.7, 3.14 | Installation/deployment, compatibility matrix |
| Operations & Monitoring | 3.13, 3.15 | Security/privacy, known issues and limitations |
| Iteration & Maintenance | 3.15–3.17 | Unimplemented features, changelog, future roadmap |

Note: The README is the project's front page. Process documents for each stage (complete records of requirements, design, testing, deployment, and operations) are carried by the corresponding specifications, see [Document Matrix](./document-matrix.md); this chapter presents only conclusions visible to users.

### 3.1 Project Name and Positioning (corresponds to Chapter 1)

````markdown
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="{{LOGO_DARK_URL}}">
    <img alt="{{项目名称}} Logo" src="{{LOGO_LIGHT_URL}}" width="{{LOGO_WIDTH}}">
  </picture>

  <h1>{{项目名称}}</h1>

  [![build](https://img.shields.io/github/actions/workflow/status/{{OWNER}}/{{REPO}}/{{WORKFLOW}}?style=flat-square&logo=github)](https://github.com/{{OWNER}}/{{REPO}}/actions)
  [![version](https://img.shields.io/badge/version-{{VERSION}}-blue?style=flat-square)]({{RELEASE_URL}})
  [![license](https://img.shields.io/badge/license-{{LICENSE_SPDX}}-blue?style=flat-square)](./LICENSE)

  **Repository Description**: 【{{仓库描述中文}} | {{REPO_DESCRIPTION_EN}}】

  **Topics**: {{TOPICS}}

  {{一句话定位}}

  {{语言切换链接}}

  [Installation](#installation) · [Quick Start](#quick-start) · [Key Features](#key-features) · [Known Issues and Limitations](#known-issues-and-limitations) · [Future Roadmap](#future-roadmap) · [Documentation](#documentation) · [Contributing](#contributing)
</div>
````

### 3.2 Project Introduction (corresponds to Chapter 2)

````markdown
## Project Introduction

{{背景}}

{{核心思路}}

**Applicable Scenarios**

- {{适用场景一}}
- {{适用场景二}}

**Inapplicable Scenarios**

- {{不适用场景一}}
- {{不适用场景二}}

### Advantages and Limitations

**Advantages**

| Advantage | Description | Verification Method |
| --- | --- | --- |
| {{优势名称}} | {{优势说明}} | {{证据}} |
| {{优势名称}} | {{优势说明}} | {{证据}} |

**Limitations**

| Limitation | Scope of Impact | Temporary Workaround |
| --- | --- | --- |
| {{局限描述}} | {{影响范围}} | {{规避方式}} |
| {{局限描述}} | {{影响范围}} | {{规避方式}} |
````

### 3.3 Core Features (corresponds to Chapter 3)

````markdown
## Core Features

- {{功能一}}: {{触发条件与结果}}
- {{功能二}}: {{触发条件与结果}}
- {{功能三}}: {{触发条件与结果}}
````

### 3.4 Key Features (corresponds to Chapter 4)

Each key feature must fully contain the five-part structure; if any part is missing, it must not be listed. See [Features and Engineering Trade-offs Writing Guide](./features-and-engineering-tradeoffs-guide.md) for the writing basis.

````markdown
## Key Features

### {{特性名称}}

- **Value**: {{价值}}
- **Implementation**: {{实现方式}}
- **Differentiation**: {{差异化}}
- **Evidence**: {{证据}}
````

### 3.5 Design Details and Engineering Trade-offs (corresponds to Chapter 5)

Write in the three-part structure "scenario → approach → reason"; for covered categories, see Section 2 of [Features and Engineering Trade-offs Writing Guide](./features-and-engineering-tradeoffs-guide.md).

````markdown
## Design Details and Engineering Trade-offs

### {{取舍主题}}

- **Scenario**: {{场景}}
- **Approach**: {{处理方式}}
- **Reason**: {{原因}}
````

### 3.6 Tech Stack and Dependency List (corresponds to Chapter 6)

````markdown
## Tech Stack and Dependency List

| Category | Technology or Component | Version Constraint | Purpose |
| --- | --- | --- | --- |
| Runtime | {{运行时与版本}} | {{运行时版本约束}} | {{运行时用途}} |
| Build | {{构建工具与版本}} | {{构建版本约束}} | {{构建用途}} |
| Test | {{测试工具与版本}} | {{测试版本约束}} | {{测试用途}} |

For details and licenses of third-party dependencies, see [NOTICE](./NOTICE).
````

### 3.7 Installation and Deployment (corresponds to Chapter 7)

````markdown
## Installation

Environment requirements: {{运行时 / 操作系统 / 版本}}

```bash
{{包管理器安装命令}}
```

Verify installation:

```bash
{{验证命令}}
```

Output:

```text
{{预期输出}}
```

Upgrade: `{{升级命令}}`. Uninstall: `{{卸载命令}}`.

Containerized deployment: {{容器化说明}}
````

### 3.8 Quick Start (corresponds to Chapter 8)

````markdown
## Quick Start

{{一句话说明本示例完成什么}}

```{{语言标识}}
{{最小可运行示例}}
```

Expected output:

```text
{{输出}}
```
````

### 3.9 Configuration (corresponds to Chapter 9)

````markdown
## Configuration

| Key | Type | Default | Required | Value Range | Function | Example |
| --- | --- | --- | --- | --- | --- | --- |
| {{键名}} | {{类型}} | {{默认值}} | {{是否必填}} | {{取值范围}} | {{作用}} | {{示例值}} |

Configuration precedence: {{配置优先级}}.

Hot reload: {{热更新支持说明}}
````

### 3.10 API or Module Description (corresponds to Chapter 10)

````markdown
## API

{{模块概述}}

```{{语言标识}}
{{接口签名}}
```

Parameters:

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| {{参数名}} | {{参数类型}} | {{参数是否必填}} | {{参数说明}} |

Return value: {{返回值说明}}

Error codes:

| Error Code | Meaning | Handling |
| --- | --- | --- |
| {{错误码}} | {{错误含义}} | {{错误处理方式}} |

Call example:

```{{语言标识}}
{{调用示例}}
```

Rate limiting and quota: {{限流与配额说明}}

For details, see [API Documentation]({{API_DOC_PATH}}).
````

### 3.11 Directory Structure (corresponds to Chapter 11)

````markdown
## Directory Structure

```text
{{项目名}}/
├── {{目录条目}}   # {{职责}}
├── {{目录条目}}   # {{职责}}
└── {{目录条目}}   # {{职责}}
```
````

### 3.12 Performance (corresponds to Chapter 12)

````markdown
## Performance

Test environment: {{测试环境}}

Test method: {{测试方法}}

| Metric | Value | Comparison Baseline |
| --- | --- | --- |
| {{性能指标}} | {{指标数值}} | {{对比基线}} |

Bottleneck analysis: {{瓶颈分析}}

Tuning recommendations: {{调优建议}}
````

### 3.13 Security and Privacy (corresponds to Chapter 13)

````markdown
## Security and Privacy

Data collection and storage: {{数据收集与存储说明}}

Transport encryption: {{传输加密说明}}

Permission model: {{权限模型说明}}

Known risks: {{已知风险}}

Vulnerability reporting channel: {{漏洞上报渠道}}

See [SECURITY.md](./SECURITY.md) for the security policy.
````

### 3.14 Compatibility (corresponds to Chapter 14)

````markdown
## Compatibility

| Dimension | Supported Range | Verification Status |
| --- | --- | --- |
| Operating System | {{操作系统}} | {{操作系统验证状态}} |
| Runtime | {{运行时兼容版本}} | {{运行时验证状态}} |
| Browser | {{浏览器}} | {{浏览器验证状态}} |
| Database | {{数据库版本}} | {{数据库验证状态}} |

Explicitly unsupported: {{明确不支持项}}
````

### 3.15 Known Issues, Limitations, and Unimplemented Features (corresponds to Chapter 15)

````markdown
## Known Issues and Limitations

**Known Issues**

| Issue Description | Scope of Impact | Temporary Workaround | Tracking Link |
| --- | --- | --- | --- |
| {{问题描述}} | {{影响范围}} | {{临时规避方案}} | {{跟踪链接}} |

**Current Limitations**

{{当前限制说明}}

**Unimplemented Features**

| Feature | Reason Not Implemented | Planned Status |
| --- | --- | --- |
| {{未实现功能}} | {{未实现原因}} | {{计划状态}} |
````

### 3.16 Changelog (corresponds to Chapter 16)

````markdown
## Changelog

Version changes follow Semantic Versioning and the Keep a Changelog structure; for the complete record, see [CHANGELOG.md](./CHANGELOG.md).
````

### 3.17 Future Roadmap (corresponds to Chapter 17)

For the writing of planned item status and target versions, see [Roadmap Specification](./roadmap-specification.md), which must be marked "not a commitment".

````markdown
## Future Roadmap

> The following are planned items, not delivery commitments; the actual scope and timing are subject to release records.

| Planned Item | Status | Target Version |
| --- | --- | --- |
| {{计划项}} | {{计划状态}} | {{目标版本}} |
| {{计划项}} | {{计划状态}} | {{目标版本}} |
````

### 3.18 Contributing (corresponds to Chapter 18)

````markdown
## Contributing

- Development environment setup: {{搭建步骤}}
- Branching model: {{说明}}
- Commit convention: {{Conventional Commits 等}}
- PR requirements: {{要求}}
- Code of conduct: see [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
- Issue templates: see [.github/ISSUE_TEMPLATE/](./.github/ISSUE_TEMPLATE/)
````

### 3.19 Copyright and License (corresponds to Chapter 19)

````markdown
## License

Copyright © {{年份}} {{著作权人}}. Licensed under {{SPDX 标识符}}.

This project is licensed under the {{许可证名称}} license; see [LICENSE](./LICENSE) for the full text.
````

### 3.20 NOTICE Compliance Statement (corresponds to Chapter 20)

````markdown
## NOTICE Compliance Statement

This project uses third-party components and materials; a summary of their licenses and copyright information is in [NOTICE](./NOTICE). This chapter does not replace the NOTICE file.
````

## 4. Placeholder Reference Table

The table lists all placeholders appearing in the template body. They are arranged by section order; unused items are deleted together with their row.

| Placeholder | Meaning | Example | Required |
| --- | --- | --- | --- |
| `{{项目名称}}` | Project display name | `Awesome Tool` | Yes |
| `{{LOGO_DARK_URL}}` | Dark-theme Logo URL | `media/logo-dark.svg` | No |
| `{{LOGO_LIGHT_URL}}` | Light-theme Logo URL | `media/logo-light.svg` | No |
| `{{LOGO_WIDTH}}` | Logo display width (px) | `200` | No |
| `{{OWNER}}` | Repository owner | `octocat` | No |
| `{{REPO}}` | Repository name | `awesome-tool` | No |
| `{{WORKFLOW}}` | CI workflow file name | `ci.yml` | No |
| `{{VERSION}}` | Current version number | `1.2.0` | No |
| `{{LICENSE_SPDX}}` | License SPDX identifier | `MIT` | Yes |
| `{{RELEASE_URL}}` | Release page URL | GitHub Releases link | No |
| `{{仓库描述中文}}` | Chinese part of the repository description, ≤120 characters | A lightweight Go CLI tool for JSON processing | Yes |
| `{{REPO_DESCRIPTION_EN}}` | English part of the repository description, ≤120 characters | A lightweight Go CLI for JSON processing | Yes |
| `{{TOPICS}}` | Topic tags, all 20 lowercase English words joined by `-` | `go cli json command-line developer-tools` | No |
| `{{一句话定位}}` | One-line statement of what the project is, who it is for, and what problem it solves | A lightweight Go command-line tool for JSON processing | Yes |
| `{{语言切换链接}}` | Language switch link | Link text `English`, target path filled according to the actual language directory, e.g., `../en-US/README.md` | No |
| `{{背景}}` | The reason the project was created and the problem it solves | Depends on the project | Yes |
| `{{核心思路}}` | Key approach or design trade-off adopted | Depends on the project | Yes |
| `{{适用场景一}}` / `{{适用场景二}}` | Situations suitable for use | Need to process small JSON files quickly | Yes |
| `{{不适用场景一}}` / `{{不适用场景二}}` | Situations explicitly not recommended and the reasons | Need to stream GB-scale files | Yes |
| `{{优势名称}}` | Noun-form name of the advantage | Zero dependencies | No |
| `{{优势说明}}` | Specific description of the advantage | No third-party runtime dependencies | No |
| `{{证据}}` | Verifiable evidence or reproducible steps for the advantage | `ldd` output is empty | No |
| `{{局限描述}}` | Specific description of the limitation | No concurrent write support | No |
| `{{影响范围}}` | Features or scenarios affected by the limitation | When multiple processes write simultaneously | No |
| `{{规避方式}}` | Temporary workaround for the limitation | Use external locking | No |
| `{{功能一}}` / `{{功能二}}` / `{{功能三}}` | Feature names | Filtering | Yes |
| `{{触发条件与结果}}` | Trigger condition and result of the feature | Pass `--filter` to output by condition | Yes |
| `{{特性名称}}` | Key feature name, no more than 15 characters | Single-file distribution | No |
| `{{价值}}` | The specific problem solved by the key feature and the consequence of not solving it | Depends on the project | No |
| `{{实现方式}}` | Technology, mechanism, or algorithm adopted, including key files or functions | Depends on the project | No |
| `{{差异化}}` | Objectively comparable dimension against a named alternative | Depends on the project | No |
| `{{证据}}` | Reproducible tests, benchmarks, code locations, or steps | Depends on the project | No |
| `{{取舍主题}}` | Engineering trade-off topic | Concurrent writes | No |
| `{{场景}}` | Specific situation triggering this design | Depends on the project | No |
| `{{处理方式}}` | Approach taken | Depends on the project | No |
| `{{原因}}` | Reason for not adopting other approaches | Depends on the project | No |
| `{{运行时与版本}}` / `{{构建工具与版本}}` / `{{测试工具与版本}}` | Tech stack component name and version | `Go 1.22` | No |
| `{{运行时版本约束}}` / `{{构建版本约束}}` / `{{测试版本约束}}` | Version constraint range | `>=1.22` | No |
| `{{运行时用途}}` / `{{构建用途}}` / `{{测试用途}}` | Component purpose | Compilation and execution | No |
| `{{运行时 / 操作系统 / 版本}}` | Installation environment requirements | `Go 1.22+, Linux/macOS` | Yes |
| `{{包管理器安装命令}}` | Actual installation command | `go install example.com/tool@latest` | Yes |
| `{{验证命令}}` | Command to verify installation | `tool --version` | No |
| `{{预期输出}}` | Expected result of the verification command | `tool 1.2.0` | No |
| `{{升级命令}}` / `{{卸载命令}}` | Upgrade and uninstall commands | `go install example.com/tool@latest` | No |
| `{{容器化说明}}` | Containerization notes or image address | `docker run ...` | No |
| `{{一句话说明本示例完成什么}}` | Goal of the Quick Start example | Filter JSON by field and output | Yes |
| `{{语言标识}}` | Code block language identifier | `bash` | Yes |
| `{{最小可运行示例}}` | Minimal runnable example | Depends on the project | Yes |
| `{{输出}}` | Expected output of the example | Depends on the project | Yes |
| `{{键名}}` | Configuration key name | `output.format` | No |
| `{{类型}}` | Configuration value type | `string` | No |
| `{{默认值}}` | Configuration default value | `json` | No |
| `{{是否必填}}` | Whether the field is required | No | No |
| `{{取值范围}}` | Allowed value range | `json / yaml` | No |
| `{{作用}}` | Configuration function | Specify the output format | No |
| `{{示例值}}` | Configuration example | `yaml` | No |
| `{{配置优先级}}` | Precedence of multi-source configuration | Command-line arguments > environment variables > config file | No |
| `{{热更新支持说明}}` | Whether hot reload is supported and how | Not supported; restart required | No |
| `{{模块概述}}` | Overview of the module's purpose | Depends on the project | No |
| `{{接口签名}}` | Function or interface signature | `func Filter(in io.Reader, key string) error` | No |
| `{{参数名}}` / `{{参数类型}}` / `{{参数是否必填}}` / `{{参数说明}}` | Interface parameter fields | in / io.Reader / Yes / input stream | No |
| `{{返回值说明}}` | Meaning of the return value | Returns `nil` on success | No |
| `{{错误码}}` / `{{错误含义}}` / `{{错误处理方式}}` | Error code fields | E001 / empty input / check the input | No |
| `{{调用示例}}` | Interface call code | Depends on the project | No |
| `{{限流与配额说明}}` | Rate limiting and quota rules | No rate limiting | No |
| `{{API_DOC_PATH}}` | Relative path of the API documentation | `./docs/api.md` | No |
| `{{项目名}}` | Root node name of the directory tree | `awesome-tool` | Yes |
| `{{目录条目}}` / `{{职责}}` | Directory tree entries and responsibilities | cmd/ / command entry point | Yes |
| `{{测试环境}}` | Hardware, OS, and runtime version | Intel i7 / Ubuntu 22.04 / Go 1.22 | No |
| `{{测试方法}}` | Performance test method | `go test -bench` | No |
| `{{性能指标}}` / `{{指标数值}}` / `{{对比基线}}` | Performance metric fields | Throughput / 120 MB/s / 80 MB/s | No |
| `{{瓶颈分析}}` | Performance bottleneck description | Depends on the project | No |
| `{{调优建议}}` | Performance tuning recommendations | Depends on the project | No |
| `{{数据收集与存储说明}}` | Scope of data collection and storage method | No user data collected | No |
| `{{传输加密说明}}` | Transport encryption method | `HTTPS` | No |
| `{{权限模型说明}}` | Permission model description | Token-based | No |
| `{{已知风险}}` | Known security risks | Depends on the project | No |
| `{{漏洞上报渠道}}` | Genuinely reachable vulnerability reporting channel | `security@example.com` | No |
| `{{操作系统}}` / `{{操作系统验证状态}}` | OS support range and verification status | Linux, macOS / Verified | No |
| `{{运行时兼容版本}}` / `{{运行时验证状态}}` | Runtime compatibility range and verification status | Go 1.20+ / Verified | No |
| `{{浏览器}}` / `{{浏览器验证状态}}` | Browser support range and verification status | Chrome 100+ / Verified | No |
| `{{数据库版本}}` / `{{数据库验证状态}}` | Database version and verification status | PostgreSQL 14+ / Verified | No |
| `{{明确不支持项}}` | Explicitly unsupported environments | 32-bit Windows | No |
| `{{问题描述}}` | Description of a known issue | High memory usage with very long input | No |
| `{{影响范围}}` | Features or scenarios affected by the issue | When input exceeds 100 MB | No |
| `{{临时规避方案}}` | Temporary workaround | Process in batches | No |
| `{{跟踪链接}}` | Issue tracking address | GitHub Issue link | No |
| `{{当前限制说明}}` | Current feature limitations | Concurrent writes not yet supported | No |
| `{{未实现功能}}` | Features not yet implemented | Configuration hot reload | No |
| `{{未实现原因}}` | Reason for not implementing | Low priority | No |
| `{{计划状态}}` | Planned status (for unimplemented features and roadmap) | Scheduled | No |
| `{{计划项}}` | Roadmap planned item | Support configuration file hot reload | No |
| `{{目标版本}}` | Target version of the planned item | `v1.3.0` | No |
| `{{搭建步骤}}` | Development environment setup steps or link | See CONTRIBUTING.md | No |
| `{{说明}}` | Branching model description | Create `feat` branches from `main` | No |
| `{{Conventional Commits 等}}` | Commit convention description | Conventional Commits | No |
| `{{要求}}` | PR requirements | Single-purpose change, tests passing | No |
| `{{年份}}` | Copyright year | `2026` | Yes |
| `{{著作权人}}` | Copyright holder | Ntarstudio | Yes |
| `{{SPDX 标识符}}` | SPDX identifier in the copyright line | `MIT` | Yes |
| `{{许可证名称}}` | Full license name | `MIT` | Yes |

## 5. Optional Section Notes

Section 3 provides copyable body text for all 20 chapters. The following are supplementary notes on adding/removing sections by project type; when deleting a section, the first-screen navigation link must be deleted as well.

| Section | Recommended Types to Keep | Condition for Deletion |
| --- | --- | --- |
| Key Features | All | May be deleted when no verifiable evidence exists; must not be replaced with qualitative descriptions |
| Design Details and Engineering Trade-offs | Frameworks, applications, services | May be deleted when there are no key trade-offs |
| Tech Stack and Dependency List | Libraries, frameworks | May be deleted when there are no external dependencies |
| Performance | CLI, libraries, services | May be deleted when no test data exists; estimated numbers are prohibited |
| Security and Privacy | Services, applications, projects processing personal information | Purely local tools may be simplified |
| Compatibility | Libraries, SDKs, cross-platform applications | Single-environment projects may be simplified |
| Changelog | All | Only when CHANGELOG does not exist, replace with an embedded change summary |
| Future Roadmap | All | May be deleted when there are no public plans |
| NOTICE Compliance Statement | With third-party dependencies | May be deleted when there are no third-party dependencies |

## 6. Pre-Delivery Self-Check Checklist

- [ ] No residual `{{...}}` placeholders.
- [ ] The first screen includes the repository description [Chinese | English] and topic tags, both consistent with repository metadata.
- [ ] Chinese and English repository descriptions are each no more than 120 characters.
- [ ] All 20 topic tags are lowercase English words joined by `-`.
- [ ] One-line positioning includes a category term, no more than 60 Chinese characters or 25 English words.
- [ ] Each key feature contains the five-part structure and has verifiable evidence.
- [ ] Advantages and limitations are listed separately; limitations include scope of impact and workarounds.
- [ ] Known issues include tracking links; unimplemented features include reasons and planned status.
- [ ] Roadmap is marked "not a commitment", with no specific delivery dates.
- [ ] Inapplicable scenarios and explicitly unsupported items are listed.
- [ ] Unique first-level heading, continuous second-level heading hierarchy, section order consistent with the 20 chapters of the specification.
- [ ] Badge styles unified, links valid, alt text clear.
- [ ] Installation commands and Quick Start examples are tested and runnable.
- [ ] All code blocks have language tags; all images have alt text.
- [ ] Relative paths work in forks and offline.
- [ ] LICENSE exists and the SPDX identifier is consistent with the README.
- [ ] Chinese and English versions' section order corresponds one-to-one.

## Related Files

- Full definition of sections: see [README Section Specification](./readme-sections-specification.md)
- Badge configuration: see [Badge Specification](./badge-specification.md)
- Visual specification: see [README Visual Layout Specification](./readme-visual-layout-specification.md)
- Type-based tailoring: see [README Category Adaptation Guide](./readme-category-adaptation-guide.md)
- Research basis: see [README Template Research Report](./readme-template-research-report.md)
- Key feature and trade-off writing: see [Features and Engineering Trade-offs Writing Guide](./features-and-engineering-tradeoffs-guide.md)
- Metadata rules: see [Project Naming Specification](./project-naming-specification.md)
- Roadmap rules: see [Roadmap Specification](./roadmap-specification.md)
