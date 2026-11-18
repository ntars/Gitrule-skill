# Code Ownership Specification

> What this file solves: Defines the syntax, ownership assignment, and review routing rules of the `.github/CODEOWNERS` file, so that every change is automatically assigned to a responsible reviewer.

## 1. Design Principles

1. **Explicit path-to-person mapping**: Each rule indicates who is responsible for a path, avoiding unreviewed or duplicated reviews.
2. **Minimum necessary owners**: Keep owners of a single path to 1–3 people; too many diffuse responsibility.
3. **Default fallback**: Set a global default owner to cover paths not matched by explicit rules.
4. **Sync with team structure**: Update promptly when membership changes, avoiding stale accounts blocking reviews.

## 2. File Location and Syntax

### 2.1 Paths

The `CODEOWNERS` file can be placed in any of the following locations; the first match by priority is used:

1. Repository root `CODEOWNERS`;
2. `docs/CODEOWNERS`;
3. `.github/CODEOWNERS` (recommended).

### 2.2 Syntax Rules

```text
# Comments start with #
<path pattern>  <owner>  [<owner>...]
```

- One rule per line; a path pattern is followed by one or more owners.
- Owner format is `@username` or `@org/team`.
- Using an email as an owner must be linked to a GitHub account.
- Paths are case-sensitive and support wildcards `*` and `**`.

### 2.3 Examples

```text
# Default owner
*                       @org/maintainers

# Assign by directory
/src/core/              @org/core-team
/src/api/               @org/api-team @alice
/docs/                  @org/docs-team

# Assign by file type
*.md                    @org/docs-team
/.github/workflows/      @org/devops-team
```

## 3. Matching Rules

1. Only the last matching rule takes effect; matches are not cumulative. Therefore, general rules are written first and specific rules later.
2. A directory rule matches that directory and its subdirectories, unless a leading `/` restricts it to the root path.
3. Rule order determines priority; arrange from broad to narrow.
4. Paths with no match are handled by the default owner for review responsibility.

## 4. Ownership Assignment Strategy

| Dimension | Assignment basis |
| --- | --- |
| Directory | Assign by module or subsystem boundary |
| File type | Documentation, configuration, and tests can be assigned uniformly by type |
| Critical paths | Security, release, and CI configuration are exclusively owned by core maintainers |
| New members | First participate as non-required reviewers, then become official owners after familiarization |

## 5. Linkage with the Review Process

1. When a PR is created, GitHub automatically requests review from owners of matching paths.
2. Required review is configured through branch protection rules; see [Git Workflow and Branching Specification](./git-workflow-and-branching-specification.md).
3. Owners should respond within the agreed timeframe; timeouts fall back to the default owner.
4. Owner changes must be synchronized in the file to avoid stale accounts blocking the process (see [Code Review Specification](./code-review-specification.md)).

## 6. Maintenance Requirements

1. Review once after every organizational restructuring or team responsibility change.
2. Repository handovers and member departures must immediately remove the corresponding owners.
3. File changes must be reviewed by at least one existing owner, preventing self-expansion of permissions.
4. Owners must not point to inactive accounts or bot accounts (except those dedicated to automation).

## 7. Forbidden Practices

1. Using overly broad wildcard rules that make everyone an owner is forbidden.
2. Assigning sensitive paths (release, key configuration) to members without review capability is forbidden.
3. Writing private contact information in the file is forbidden.
4. Retaining departed members as owners long-term is forbidden.

## Related Files

- File responsibility boundaries: see [Document Matrix](./document-matrix.md)
- Review standards and responsibilities: see [Code Review Specification](./code-review-specification.md)
- Branch protection: see [Git Workflow and Branching Specification](./git-workflow-and-branching-specification.md)
- Automated checks are dimension D9: see [Review Dimension Matrix](./review-dimension-matrix.md)
