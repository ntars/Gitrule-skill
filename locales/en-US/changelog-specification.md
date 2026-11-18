# Changelog Specification

> What this file solves: Defines the user-facing version change record template, fields, and writing style, ensuring every change is traceable, versions can be matched, and upgrade paths can be determined.

## 1. Specification Clauses

1. The changelog follows the Keep a Changelog structure, and version numbers follow semantic versioning in the [Version Management Specification](./version-management-specification.md).
2. Every version must have a release date in the format `YYYY-MM-DD`; unreleased content is placed in the `Unreleased` section.
3. Entries are grouped into six categories: `Added` / `Changed` / `Deprecated` / `Removed` / `Fixed` / `Security`.
4. Every change is user-facing, must state the impact and migration method, and must not include internal refactoring details.
5. Breaking changes must be marked `BREAKING CHANGE:` and provide migration steps (see the [Migration Guide Specification](./migration-guide-specification.md)).
6. Version numbers must be consistent with tags and Release Notes; breaking changes must correspond to `feat!:` or `BREAKING CHANGE:` in the commit message.

## 2. Changelog Template

```markdown
# Changelog

This file records all user-facing changes. The format follows Keep a Changelog, and versions follow semantic versioning.

## [Unreleased]

### Added
- {{新增能力，说明对使用者的价值}}

### Changed
- {{行为变更，说明影响范围}}

### Deprecated
- {{即将移除的能力，说明替代方案与移除版本}}

### Removed
- {{已移除的能力，说明迁移路径}}

### Fixed
- {{缺陷修复，说明触发条件}}

### Security
- {{安全修复，说明影响与升级建议}}

## [{{X.Y.Z}}] - {{YYYY-MM-DD}}

### {{类型}}
- {{变更条目}}
- {{BREAKING CHANGE: 原行为 → 新行为；迁移步骤见链接}}

[Unreleased]: https://github.com/{{owner}}/{{repo}}/compare/v{{X.Y.Z}}...HEAD
[{{X.Y.Z}}]: https://github.com/{{owner}}/{{repo}}/compare/v{{prev}}...v{{X.Y.Z}}
```

## 3. Entry Template

```markdown
- {{动词开头的一句话变更描述}}（{{关联 REQ 编号}}）
  - 影响：{{哪些使用者或场景受影响}}
  - 迁移：{{需要执行的动作；无则省略此行}}
  - 参考：{{Issue / PR 链接}}
```

## 4. Field Definitions

| Field | Required | Type | Filling Notes | Example |
| --- | --- | --- | --- | --- |
| Version number | Yes | `X.Y.Z` | Exactly consistent with the tag; omitting the `v` prefix is acceptable, but must be consistent throughout | `1.2.0` |
| Release date | Yes | `YYYY-MM-DD` | Based on the tag creation date | `2026-11-18` |
| Group type | Yes | Enumeration | One of the six categories; omit the whole section if there are no entries of that category | `Fixed` |
| Change description | Yes | Text | Starts with a verb, user-facing, states the value | `Added GFM table checking` |
| Impact | Conditionally required | Text | Required for behavior changes, deprecations, removals, and breaking changes | `Old configuration file must be renamed` |
| Migration | Conditionally required | Text | Required for breaking changes, pointing to the migration guide | `See migration guide v1.0` |
| BREAKING CHANGE | Conditionally required | Marker | Required for breaking changes, placed at the beginning of the entry | `BREAKING CHANGE:` |
| Compare link | Yes | URL | Every version section must provide a compare link | `compare/v1.1.0...v1.2.0` |
| Related REQ | No | List | Facilitates comparison with the requirements traceability matrix | `REQ-007` |

## 5. Filling Instructions

1. **Entry granularity**: one change description covers one user-perceivable result; multiple results are split into multiple entries.
2. **Start with a verb**: use "Add", "Support", "Fix", "Remove", "Deprecate", "Adjust"; do not use "Updated" or "Did some".
3. **Prohibited content**: entries without dates, internal refactoring, development plans, roadmap content, and vague expressions ("optimize experience", "fix several issues").
4. **Breaking changes**: must have all four of the `BREAKING CHANGE:` marker, impact statement, migration steps, and migration guide link; none may be missing.
5. **Deprecated items**: must state the replacement and the planned version for removal, for example "will be removed in v2.0".
6. **Unreleased**: registered immediately after merging, not accumulated and written on release day.
7. **Consistency**: version numbers and release dates must be consistent across tags, Release Notes, and deployment records; if inconsistent, the tag prevails and the other three are corrected.

Common mistakes:

| Incorrect Wording | Problem | Correction |
| --- | --- | --- |
| "Refactored the internal module structure" | Internal detail, imperceptible to users | Delete, or rewrite as a perceivable effect |
| "Fixed several issues" | Not determinable | List each fix individually |
| A breaking change stated only as "there is a change" | No migration path | Add the impact, migration steps, and guide link |
| Version number inconsistent with the tag | Version correspondence is broken | Unify based on the tag |
| No compare link | Differences cannot be viewed | Add the GitHub compare URL |

## 6. Complete Example

```markdown
## [1.0.0] - 2026-11-20

### Added
- Added a mixed Chinese-English spacing check rule (REQ-001), callable directly from the command line.
- Added JSON report output for easy integration with CI statistics.

### Changed
- BREAKING CHANGE: The configuration file name changed from `.mdlint.json` to `.mdlintrc.json`. The old file will no longer be read; see the [Migration Guide](./migration-guide-specification.md) for migration steps.

### Deprecated
- The `--format=table` parameter will be removed in v2.0; use `--reporter=table` instead.

### Fixed
- Fixed the false positive when Chinese punctuation is adjacent to an English word.

### Security
- Fixed the issue where the rule plugin loading path could be overridden by external input; all users are advised to upgrade to v1.0.0.

[1.0.0]: https://github.com/example/markdown-lint-cli/compare/v0.9.3...v1.0.0
```

## Related Files

- Version increment rules: [Version Management Specification](./version-management-specification.md)
- Migration documentation for breaking changes: [Migration Guide Specification](./migration-guide-specification.md)
- Document responsibility boundaries: [Document Matrix](./document-matrix.md)
- Breaking markers in commit messages: [Commit Message Specification](./commit-message-specification.md)
- README changelog section: [README Sections Specification](./readme-sections-specification.md)
- Tags and Release Notes: [Push and Release Specification](./push-and-release-specification.md)
