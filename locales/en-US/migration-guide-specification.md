# Migration Guide Specification

> What this file solves: Defines the structure, content elements, and release timing of migration guides for breaking changes, enabling users to smoothly upgrade from an old version to a new one step by step.

## 1. Trigger Conditions

A migration guide must be provided when any of the following occurs:

1. A commit message contains `BREAKING CHANGE:` or `feat!:` / `fix!:` (see [Commit Message Specification](./commit-message-specification.md)).
2. A configuration key, default value, or precedence changes.
3. An API signature, return structure, or error code changes.
4. The minimum runtime version is raised, or support for a platform is dropped.
5. The directory structure or file naming changes, affecting users' reference paths.

## 2. File Location and Naming

1. Minor migration notes go into the corresponding version entry in `CHANGELOG.md`.
2. For larger changes involving multi-step operations, create a separate file under `docs/migration/`, named by version, e.g. `docs/migration/v2.md`.
3. A complete migration path across major versions is indexed in `docs/migration/README.md`.
4. The README contains only migration notices and links, not the steps themselves (see [Documentation Matrix](./document-matrix.md)).

## 3. Document Structure

A migration guide must be organized in the following order:

1. **Title and Version**: State the source version and target version, e.g. "Migrating from v1.x to v2.0".
2. **Impact Overview**: List change categories and impact scope, stating which users must migrate.
3. **Prerequisites**: Preparations to complete before migration, such as backups and environment version upgrades.
4. **Change List**: List breaking changes item by item, each including "old behavior", "new behavior", and "reason for change".
5. **Migration Steps**: Number the executable operations and provide commands or code examples.
6. **Verification Method**: How to confirm success after migration, with check commands or expected output.
7. **Rollback Method**: How to restore the old version if migration fails.
8. **FAQ**: List high-frequency questions and answers.
9. **Getting Help**: Point to issues, discussion forums, or the documentation site.

### 3.1 Copyable Blank Template

The template below corresponds item by item to the nine-part structure in Section 3; copy it and replace the placeholders to use:

````markdown
# Migrating from {{源版本}} to {{目标版本}}

> This guide describes all operations required to upgrade from {{源版本}} to {{目标版本}}, and applies to {{适用使用者范围}}.

## 1. Impact Overview

| Change Category | Details | Impact Scope | Migration Required |
| --- | --- | --- | --- |
| {{变更类别}} | {{变更内容}} | {{受影响的使用者场景}} | {{是否必须迁移}} |

## 2. Prerequisites

- {{前置准备}}
- {{检查项与确认命令}}

## 3. Change List

### {{变更项名称}}

- Old Behavior: {{旧版本行为}}
- New Behavior: {{新版本行为}}
- Reason for Change: {{变更原因}}

Before migration:

```{{代码语言}}
{{旧配置或旧代码}}
```

After migration:

```{{代码语言}}
{{新配置或新代码}}
```

## 4. Migration Steps

1. {{迁移步骤}}
2. {{迁移步骤}}
3. {{人工处理步骤}}

## 5. Verification

```bash
{{可独立运行的检查命令}}
```

Expected Output: {{预期结果}}

## 6. Rollback

1. {{恢复旧版本的操作}}
2. {{恢复旧配置的操作}}

## 7. FAQ

### {{问题}}

Answer: {{解答}}

## 8. Getting Help

- Issue Feedback: {{issue 地址}}
- Discussion Forum: {{讨论区地址}}
- Related Documentation: {{文档链接}}
````

Placeholder reference:

| Placeholder | Required | Filling Guidelines |
| --- | --- | --- |
| `{{源版本}}` / `{{目标版本}}` | Yes | Consistent with the target tag, format `vX.Y.Z` |
| `{{适用使用者范围}}` | Yes | State which users must migrate; avoid vague wording |
| `{{变更类别}}` | Yes | At least one of the four categories: configuration, API, runtime, directory |
| `{{是否必须迁移}}` | Yes | State whether this change requires users to perform migration |
| `{{旧行为}}` / `{{新行为}}` | Yes | Compare item by item; do not write only one side |
| `{{代码语言}}` | Yes | Code block language tag, e.g. `yaml`, `json`, `js` |
| `{{前置准备}}` | Yes | Backups and environment checks to complete before migration |
| `{{迁移步骤}}` | Yes | Each step directly executable, with commands or code |
| `{{人工处理步骤}}` | Yes | Steps that cannot be auto-migrated must be explicitly marked here |
| `{{检查命令}}` / `{{预期结果}}` | Yes | Command runs independently, result determinable |
| `{{回滚方式}}` | Yes | Must not be omitted; see Prohibited Practices in Section 7 |

## 4. Content Requirements

### 4.1 Change Comparison Example

```markdown
### Configuration item `timeout` renamed to `timeoutMs`

- Old Behavior: Use `timeout: 5000` in the config file, in seconds.
- New Behavior: Use `timeoutMs: 5000` instead, in milliseconds.
- Reason for Change: Unify time units to avoid inconsistency with API parameters.

Before migration:

```yaml
timeout: 5
```

After migration:

```yaml
timeoutMs: 5000
```

### 4.2 Writing Requirements

1. Give a directly executable command or code for each step; do not merely describe "modify configuration".
2. Provide a before/after comparison to facilitate item-by-item verification.
3. Clearly mark steps that cannot be auto-migrated and require manual handling.
4. Impact scope must be specific; avoid vague wording like "may affect some users".
5. Verification commands must run independently and include expected output.

## 5. Release Timing and Linkage

1. A migration guide must be released in sync with the version containing breaking changes; no delays.
2. The corresponding `CHANGELOG.md` entry must link to the migration guide (see [Changelog Specification](./changelog-specification.md)).
3. The breaking-changes section of the PR template must prompt for the migration method (see [Issue and PR Template Specification](./issue-and-pr-template-specification.md)).
4. Version numbers follow semantic versioning; a breaking change must increment the major version (see [Version Management Specification](./version-management-specification.md)).
5. The README must prominently prompt users of old versions to read the migration guide.

## 6. Deprecation and Retention Policy

1. Migration guides must be retained long-term and must not be deleted after a new version is released.
2. Old-version documentation may be marked "no longer maintained", but its entry must be retained.
3. Upgrades spanning multiple major versions must provide a step-by-step path; requiring a single jump across all changes is prohibited.

## 7. Prohibited Practices

1. Merely writing "there are breaking changes, adjust accordingly" is prohibited.
2. Omitting the rollback method is prohibited.
3. Using non-executable pseudocode in migration steps is prohibited.
4. Deleting migration guides for historical versions is prohibited.

## Related Files

- Changelog structure: [Changelog Specification](./changelog-specification.md)
- Version increment rules: [Version Management Specification](./version-management-specification.md)
- Breaking declarations in commit messages: [Commit Message Specification](./commit-message-specification.md)
- Documentation responsibility boundaries: [Documentation Matrix](./document-matrix.md)
- Release process: [Push and Release Specification](./push-and-release-specification.md)
