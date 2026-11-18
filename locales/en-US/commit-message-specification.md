# Commit Message Specification

> What this file solves: Defines the fields, format, filling instructions, and examples of Conventional Commits to keep history readable and enable automatic generation of changelogs and version numbers.

## 1. Format

```text
<type>[optional scope][optional !]: <description>

[optional body]

[optional footer]
```

## 2. Types

The complete set of ten types is as follows, covering commit scenarios in common open source projects:

| Type | Meaning |
| --- | --- |
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation changes |
| `style` | Formatting changes that do not change logic (whitespace, formatting, missing semicolons, etc.) |
| `refactor` | Refactoring that neither adds features nor fixes bugs |
| `perf` | Code changes for performance improvement |
| `test` | Add missing tests or correct existing tests |
| `build` | Changes affecting the build system or external dependencies (e.g. npm, gulp) |
| `ci` | Changes to CI configuration and scripts (e.g. GitHub Actions, CircleCI) |
| `chore` | Miscellaneous changes to build, dependencies, toolchain, etc. |

### 2.1 Comparison and Trade-offs of Team Conventions

Three common conventions exist under different collaboration models; a project should select one at initiation and use it across the whole team:

| Convention | Format | Suitable For | Limitation |
| --- | --- | --- | --- |
| Work style | `[Task card ID] Author: Change description` | Teams using kanban and pair programming | Depends on a task card system; not applicable without card IDs |
| Conventional style | `[Category] Component (optional): Change description` | Teams that need to filter history by business module | Requires a team-agreed category list, with extra cost |
| Open source style | `<type>(<scope>): <subject>` | Open source libraries and applications needing automatic CHANGELOG generation | Many types and scopes; higher learning cost |

This project uniformly adopts the open source style (i.e. Conventional Commits) because it is machine-readable and enables automatic generation of changelogs and version numbers. The work style and conventional style are used only in closed-source teams by agreement and must not be mixed into public repositories.

## 3. Field Definitions

| Field | Required | Type | Filling Notes | Example |
| --- | --- | --- | --- | --- |
| Type | Yes | Enum | One of the ten types; do not invent new ones | `feat` |
| Scope | No | Text | Module name, lowercase short word, no spaces | `parser` |
| Breaking marker | No | `!` | Placed after the type or scope and before the colon | `feat!:` |
| Description | Yes | Text | Imperative sentence, lowercase start, ≤72 characters, no trailing period | `add TOML config support` |
| Body | No | Text | Explains motivation and implementation, separated from the description by a blank line | `Allow the parser to read TOML...` |
| Footer | No | Text | `BREAKING CHANGE:` or `Refs: #N` | `BREAKING CHANGE: ...` |
| Related requirement | No | `REQ-NNN` | Written in the body or footer for traceability | `Refs: REQ-001` |

## 4. Filling Instructions

1. **Description**: Use imperative sentences (add, fix, remove) and write "what was done" rather than "a change was made"; Chinese projects may write descriptions in Chinese, but the whole repository must be consistent.
2. **Scope**: Use the module name rather than the file name; omit the scope for cross-module changes, and do not write `all` or `global`.
3. **Body**: Write it only when the description is insufficient to explain the motivation; do not restate the description or write a step-by-step account.
4. **Breaking changes**: Use either `feat!:` / `fix!:` or the `BREAKING CHANGE:` footer, or both; when either appears, it must be recorded in [Changelog Specification](./changelog-specification.md) and [Migration Guide Specification](./migration-guide-specification.md).
5. **Atomicity**: One commit does one thing; formatting and logic changes are committed separately.
6. **Security**: Do not include secrets, tokens, personal information, or internal addresses; verify with a secret scan before committing (see [Security and Privacy Specification](./security-and-privacy-specification.md)).
7. **Version linkage**: `feat` triggers a minor version increment, `fix` triggers a patch version increment, and `BREAKING CHANGE` triggers a major version increment; see [Version Management Specification](./version-management-specification.md).

Common mistakes:

| Incorrect Writing | Problem | Correction |
| --- | --- | --- |
| `wip`, `update`, `fix bug` | Uninformative, violates H10 | State the object and action |
| `feat: Added new feature.` | Not imperative, uppercase start, trailing period | `feat: add config loader` |
| `feat(all): optimize` | Invalid scope, vague description | Use a specific module name and state the change |
| A commit containing both formatting and feature changes | Breaks atomicity | Split into two commits: `style:` and `feat:` |
| Commit message containing an internal network address | Information leakage | Remove it and run a secret scan |

## 5. Complete Example

```text
feat(parser): add support for TOML config

Allow the parser to read TOML configuration files in addition to YAML.
Refs: REQ-001

BREAKING CHANGE: the `config` option now accepts a file path instead of an object.
```

Meaning of each field: `feat` is the type, `parser` is the scope, and the short description follows the colon; the body explains the motivation and implementation, the footer references the requirement; the final footer declares the breaking change and gives the migration direction.

Example of a fix:

```text
fix(spacing): avoid false positives before Chinese punctuation

The spacing rule previously flagged strings such as "using Node.js," because
the punctuation check ran after whitespace normalization.

Refs: REQ-004, #142
```

## Related Files

- Commit history review belongs to dimension D7: [Audit Dimension Matrix](./review-dimension-matrix.md)
- Changelog generation: [Changelog Specification](./changelog-specification.md)
- Basis for version increments: [Version Management Specification](./version-management-specification.md)
- Code review check items: [Code Review Specification](./code-review-specification.md)
- Requirements traceability: [Requirements Traceability Matrix Specification](./requirements-traceability-matrix-specification.md)
