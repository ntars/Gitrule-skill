# Version Management Specification

> What this file solves: Defines semantic versioning rules, version decision records, increment basis, and linkage relationships, ensuring version numbers can express the nature of changes, be parsed by tools, and be consistent with release artifacts.

## 1. Specification Clauses

1. Version numbers follow semantic versioning: `MAJOR.MINOR.PATCH`.
2. Version numbers do not use years, dates, or build serial numbers as the semantic subject; released version numbers must not be reused.
3. Breaking changes must be handled centrally when the major version is upgraded, with a migration method provided.
4. The version number is consistent with the tag, whose format is `vMAJOR.MINOR.PATCH` (see [Push and Release Specification](./push-and-release-specification.md)).
5. Pre-release versions use the suffixes `-alpha`, `-beta`, `-rc`, and must be validated before the stable release.

## 2. Version Number Format and Increment Basis

| Position | Increment Condition | Triggering Commit Type | Example |
| --- | --- | --- | --- |
| MAJOR | Incompatible breaking changes | `feat!:` / `fix!:` / `BREAKING CHANGE:` | `1.9.2 → 2.0.0` |
| MINOR | Backward-compatible new features | `feat` | `1.2.3 → 1.3.0` |
| PATCH | Backward-compatible bug fixes | `fix` | `1.2.3 → 1.2.4` |

Pre-release format: `vMAJOR.MINOR.PATCH-alpha.N` / `-beta.N` / `-rc.N`, with the number increasing from 1; the suffix is removed when the stable version is released.

## 3. Version Decision Record Template

```markdown
## Version Decision: {{X.Y.Z}}

- Decision date: {{YYYY-MM-DD}}
- Decision maker: {{姓名}}
- Current version: {{X.Y.Z}}
- Target version: {{X.Y.Z}}
- Increment position: {{MAJOR / MINOR / PATCH}}
- Basis: {{列举触发的提交类型与变更内容}}

| Change | Commit Type | Related Requirement | Breaks Compatibility |
| --- | --- | --- | --- |
| {{变更描述}} | {{feat / fix / BREAKING CHANGE}} | {{REQ-NNN}} | {{是 / 否}} |

- Breaking change handling: {{迁移指南链接 / 不适用}}
- Changelog entry: {{链接}}
- Tag: {{vX.Y.Z}}
- Release check: {{已通过 / 待通过}}
```

## 4. Version Ledger Template

```markdown
# Version Ledger: {{项目名称}}

| Version | Release Date | Type | Main Changes | Tag | Changelog | Status |
| --- | --- | --- | --- | --- | --- | --- |
| {{X.Y.Z}} | {{YYYY-MM-DD}} | {{主版本 / 次版本 / 修订}} | {{一句话}} | {{vX.Y.Z}} | {{链接}} | {{当前 / 历史 / 已废弃}} |
| {{X.Y.Z-rc.1}} | {{YYYY-MM-DD}} | Pre-release | {{一句话}} | {{vX.Y.Z-rc.1}} | {{链接}} | Superseded |

Status: Current / Historical / Deprecated / Superseded
```

## 5. Field Definitions

| Field | Required | Type | Filling Guidance | Example |
| --- | --- | --- | --- | --- |
| Current version | Yes | `X.Y.Z` | Consistent with the most recent tag | `1.2.3` |
| Target version | Yes | `X.Y.Z` | Increment only one position | `1.3.0` |
| Increment position | Yes | Enum | MAJOR / MINOR / PATCH | `MINOR` |
| Basis | Yes | List | List the triggering changes; "routine update" is prohibited | `Added TOML support` |
| Breaking change handling | Conditionally required | Link | Required when MAJOR is incremented | `[Migration Guide]` |
| Changelog entry | Yes | Link | Points to the corresponding version section | `[1.3.0]` |
| Tag | Yes | `vX.Y.Z` | One-to-one correspondence with the version number | `v1.3.0` |
| Release date | Yes | `YYYY-MM-DD` | Based on the tag date | `2026-11-20` |
| Status | Yes | Enum | Current / Historical / Deprecated / Superseded | `Current` |

## 6. Filling Instructions

1. **Single-position increment**: Increment only one position per release; when feat and BREAKING CHANGE coexist, take the highest position (MAJOR), and fold the remaining changes into that version.
2. **Centralized breaking changes**: Merge multiple breaking changes into the same major version release, avoiding consecutive MAJOR increments.
3. **No reuse**: Released version numbers are permanently occupied; when withdrawing a release, increment PATCH to release a revision, do not reuse the original number.
4. **Pre-release**: `alpha` for internal validation, `beta` for public trial, `rc` for release candidate; every level must pass CI.
5. **Consistency check**: The version number must be consistent in five places: tag, changelog, Release Notes, deployment record, and version ledger; if inconsistent, the tag prevails and the others are corrected.
6. **Linkage**: The increment basis comes from the type in [Commit Message Specification](./commit-message-specification.md); external descriptions are in [Changelog Specification](./changelog-specification.md); the upgrade path is in [Migration Guide Specification](./migration-guide-specification.md).

Common mistakes:

| Incorrect Wording | Problem | Correction |
| --- | --- | --- |
| `v2026.11` | Uses date as the semantic subject | Change to `v2.1.0` |
| Two positions incremented in the same release | Semantic confusion | Increment only the highest position |
| Reusing a withdrawn version number | Artifacts cannot be distinguished | Increment PATCH to release a revision |
| MAJOR increment without a migration guide | Users cannot upgrade | Add a migration guide and link it |
| Version number exists only in the tag | Ledger and log inconsistent | Sync all five places |

## 7. Complete Example

```markdown
## Version Decision: 2.0.0

- Decision date: 2026-12-01
- Decision maker: Li Si
- Current version: 1.9.2
- Target version: 2.0.0
- Increment position: MAJOR
- Basis: The configuration file format changed from an object to a file path, an incompatible change.

| Change | Commit Type | Related Requirement | Breaks Compatibility |
| --- | --- | --- | --- |
| Configuration file pathification | BREAKING CHANGE | REQ-021 | Yes |
| Added TOML parsing | feat | REQ-001 | No |

- Breaking change handling: [Migration Guide v2.0]
- Changelog entry: [2.0.0]
- Tag: v2.0.0
- Release check: Passed
```

## Related Files

- Commit types and breaking markers: [Commit Message Specification](./commit-message-specification.md)
- Tag and Release Notes: [Push and Release Specification](./push-and-release-specification.md)
- Changelog entries: [Changelog Specification](./changelog-specification.md)
- Upgrade path: [Migration Guide Specification](./migration-guide-specification.md)
- Source of target version: [Roadmap Specification](./roadmap-specification.md)
- Version consistency in deployment records: [Deployment and Rollback Specification](./deployment-and-rollback-specification.md)
