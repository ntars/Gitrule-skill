# Contribution Guide Template

> What this file solves: Provides a directly copyable contribution guide template for projects to generate `CONTRIBUTING.md`, covering participation methods, environment setup, branching model, commit convention, PR requirements, testing requirements, code of conduct, and license statement; the accompanying filling instructions cover how to tailor it for various project types.

## 1. Usage Instructions

1. Copy all content of "Template Body" in Section 3 and create it as `CONTRIBUTING.md` in the project root.
2. Replace placeholders according to Section 4; all commands must be real commands that can be executed directly.
3. Tailor according to the scenario variants in Section 5: documentation projects delete the test command section and retain the Issue and PR workflow.
4. For the basis of the rules, see [Contribution Guide Specification](./contribution-guide-specification.md); for branching and commit details, see [Git Workflow and Branching Specification](./git-workflow-and-branching-specification.md) and [Commit Message Specification](./commit-message-specification.md), respectively.

## 2. Customization Principles

- **Executable**: Commands must include the full working directory and dependency prerequisites; writing only "install dependencies" without a specific command is prohibited.
- **With trigger conditions**: Each step must state when to execute it and the expected result.
- **Not vague**: Writing only "PRs are welcome" without a substantive process is prohibited; this corresponds to the community governance check of the [Quality Gate](./quality-gate.md).
- **Reference rather than copy**: Commit and testing rules reference the corresponding specifications; the full text is not repeated in this file.

## 3. Template Body

````markdown
# Contribution Guide

> This file explains how to contribute to {{项目名称}} and applies to external contributors and first-time participants.

## Ways to Participate

| Method | Applicable Scenario | Entry Point |
| --- | --- | --- |
| Issue discussion | Feature suggestions, problem reports | {{议题入口}} |
| Documentation improvement | Typos, example additions, structural optimization | Submit a PR directly |
| Code contribution | Bug fixes, feature implementation | See the workflow below |
| Problem feedback | Blocked usage, anomaly reproduction | {{问题反馈入口}} |

## Development Environment Setup

Prerequisites: {{环境前提}}

```bash
# Clone the repository
git clone {{仓库地址}}
cd {{项目目录名}}

# Install dependencies
{{依赖安装命令}}

# Run locally
{{本地运行命令}}
```

Expected result: {{验证本地环境可用的方式}}

## Branching Model

- Create a personal branch from {{基准分支}}, with the naming format `{{分支命名格式}}` (e.g., `feat/short-description`).
- Each PR handles only one thing; please split changes that are too large in scope.
- Direct commits to {{受保护分支}} are prohibited; changes must be merged via PR.

## Commit Convention

Commit messages follow Conventional Commits, with the format `type(scope): subject`. Common types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`. Example:

```text
feat(cli): add config file support
```

For complete rules, see [Commit Message Specification]({{提交规范链接}}).

## PR Requirements

Please complete the following self-checks before submitting a PR:

- [ ] The change is single-purpose and has a corresponding issue or explanation.
- [ ] Commit messages conform to the format above.
- [ ] All tests pass when running `{{测试命令}}` locally.
- [ ] Documentation is updated along with the code.
- [ ] No secrets, private keys, or sensitive information introduced.
- [ ] The description states what changed, why, and how it was verified.

## Testing Requirements

| Check Item | Command | Passing Criteria |
| --- | --- | --- |
| Unit tests | `{{单元测试命令}}` | All pass |
| Static checks | `{{lint 命令}}` | No errors |
| Build verification | `{{构建命令}}` | Build succeeds |

Coverage threshold: {{覆盖率要求}}.

## Code of Conduct

Participating in this project implies agreement to comply with the [Code of Conduct](./CODE_OF_CONDUCT.md).

## Issue Specification

- Search existing issues before asking, to avoid duplication.
- Bug reports must include: environment information, reproduction steps, expected results, actual results, and error logs.
- Feature requests must state the use case and alternatives if not adopted.

## License Statement

Contributions are by default subject to this project's license {{许可证名称及 SPDX 标识符}}, the full text of which is in [LICENSE](./LICENSE). Submitting implies that you have the right to license your contribution under that license.
````

## 4. Placeholder Reference Table and Field Definitions

| Placeholder | Required | Field Definition | Filling Example |
| --- | --- | --- | --- |
| `{{项目名称}}` | Yes | Public project name | `FooBar` |
| `{{议题入口}}` | Yes | Genuinely accessible issue address | `https://github.com/owner/repo/issues` |
| `{{问题反馈入口}}` | No | Dedicated channel when different from the issue entry | `https://github.com/owner/repo/issues/new` |
| `{{环境前提}}` | Yes | Language version, package manager, and system dependencies | `Node.js 20+, pnpm 8+` |
| `{{仓库地址}}` | Yes | Cloneable repository address | `https://github.com/owner/repo.git` |
| `{{项目目录名}}` | Yes | Directory name after cloning | `repo` |
| `{{依赖安装命令}}` | Yes | Actual installation command | `pnpm install` |
| `{{本地运行命令}}` | Yes | Actual startup command | `pnpm dev` |
| `{{验证本地环境可用的方式}}` | Yes | Observable sign of success | The homepage appears at `localhost:3000` |
| `{{基准分支}}` | Yes | Source branch from which to create a branch | `main` |
| `{{分支命名格式}}` | Yes | Branch naming rule | `feat/short-description` |
| `{{受保护分支}}` | Yes | Branch to which direct commits are prohibited | `main` |
| `{{提交规范链接}}` | No | Internal or external commit convention address | `./docs/COMMIT_CONVENTION.md` |
| `{{测试命令}}` | Yes | Actual test command | `pnpm test` |
| `{{lint 命令}}` | Yes | Actual static check command | `pnpm lint` |
| `{{构建命令}}` | Yes | Actual build command | `pnpm build` |
| `{{覆盖率要求}}` | No | Coverage threshold for new code | No less than 80% for new code |
| `{{许可证名称及 SPDX 标识符}}` | Yes | Full name and SPDX identifier of the project license | MIT License (MIT) |

## 5. Filling Instructions and Scenario Variants

| Scenario | Sections to Keep | Sections That May Be Tailored | Key Adjustments |
| --- | --- | --- | --- |
| Code project | All | None | Commands must actually run successfully |
| Documentation project | Ways to Participate, PR Requirements, Code of Conduct, License | Testing Requirements, Development Environment Setup | Delete the test table, retain the PR self-check |
| Personal project | Ways to Participate, PR Requirements, Code of Conduct, License | Environment setup may be simplified | State clearly whether external contributions are accepted |
| Enterprise project | All | None | Add a Contributor License Agreement (CLA) link and legal requirements |

Common error comparison:

| Incorrect Writing | Consequence | Correct Writing |
| --- | --- | --- |
| "All forms of contribution are welcome" | No specific path, contributors don't know where to start | List the participation methods table and entry points |
| "Just run the tests" | Command and passing criteria unknown | State the command, passing criteria, and coverage threshold |
| Writing `npm install` when the project uses pnpm | Command not executable | Be consistent with the actual lockfile |

## 6. Complete Example

The following is a filled-in example of the command section, for format reference only.

```bash
# Clone the repository
git clone https://github.com/owner/repo.git
cd repo

# Install dependencies
pnpm install

# Run locally
pnpm dev
```

Expected result: The homepage appears at `localhost:3000`.

## Related Files

- Corresponding specification: [Contribution Guide Specification](./contribution-guide-specification.md)
- Companion templates: [Code of Conduct Template](./code-of-conduct-template.md), [SECURITY Template](./security-template.md)
- Testing details: [Testing Specification](./testing-specification.md)
- Community governance dimension: [Audit Dimension Matrix](./review-dimension-matrix.md)
- Back to the Simplified Chinese index: [README](./README.md)
