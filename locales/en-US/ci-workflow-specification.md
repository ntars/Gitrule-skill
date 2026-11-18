# CI Workflow Specification

> What this file solves: Defines trigger conditions, job splitting, caching strategies, and security configuration for `.github/workflows/*.yml` continuous integration workflows, making builds, tests, and checks reproducible and auditable.

## 1. Design Principles

1. **Single responsibility**: Each workflow handles only one category of goal (build, test, release, documentation deployment); release and testing must not be mixed in one workflow.
2. **Fast feedback**: Lightweight checks (lint, format) come first, time-consuming jobs (full test matrix) come later.
3. **Reproducibility**: Lock dependency versions, use fixed-version Actions; caching is only for speedup and must not change results.
4. **Least privilege**: Workflows are granted permissions per job, read-only by default, with release jobs separately elevated (see [Security and Privacy Specification](./security-and-privacy-specification.md)).

## 2. File Structure

### 2.1 Naming and Paths

- The path is fixed as `.github/workflows/*.yml`.
- File names use lowercase letters and hyphens, named by responsibility, such as `ci.yml`, `release.yml`, `docs.yml`.
- The workflow `name` field must be semantically consistent with the file name.

### 2.2 Required Blocks

| Block | Purpose | Requirement |
| --- | --- | --- |
| `name` | Workflow display name | Concise, responsibility readable from it |
| `on` | Trigger conditions | Explicit branches, paths, or events |
| `permissions` | Permission declaration | Explicitly declared, least privilege by default |
| `jobs` | Job collection | Split by responsibility |

### 2.3 Trigger Condition Design

| Trigger event | Applies to | Notes |
| --- | --- | --- |
| `push` | Main trunk and release branches | Limit branch scope; avoid triggering on all branches |
| `pull_request` | All PRs | Ensure checks run before merge |
| `workflow_dispatch` | Manual trigger | For controlled operations such as release and rollback |
| `schedule` | Scheduled tasks | For dependency update checks and nightly builds |
| `release` | Post-release actions | For artifact upload and announcements |

## 3. Job Splitting

Recommended stage order:

1. **Static checks**: Format, lint, type checking.
2. **Build**: Produce build artifacts for reuse by later jobs.
3. **Test**: Unit tests, integration tests, can be parallelized by matrix.
4. **Artifact validation**: Check artifact size, signature, or integrity.
5. **Release**: Execute only when CI is fully green and conditions are met (see [Push and Release Specification](./push-and-release-specification.md)).

Declare dependencies between jobs via `needs`, ensuring failures halt the chain; later jobs must not continue in a failed state.

## 4. Matrix Builds

Use `strategy.matrix` to cover multiple versions and platforms:

```yaml
strategy:
  fail-fast: false
  matrix:
    os: [ubuntu-latest, macos-latest, windows-latest]
    node-version: [18, 20, 22]
```

Requirements:

- Version coverage includes the minimum and latest versions declared as supported by the project (see [Compatibility Notes](./readme-sections-specification.md), chapter 14).
- `fail-fast` is set to `false` so all combinations run fully, aiding compatibility issue location.
- No more than three matrix dimensions, to avoid combinatorial explosion.

## 5. Caching Strategy

| Cache object | Key suggestion | Notes |
| --- | --- | --- |
| Dependency directory | Package manager lockfile hash | Invalidates when the lockfile changes |
| Build artifacts | Hash of source and configuration | Consistent with build inputs |
| Toolchain | Version number | Invalidates when the version is upgraded |

Caching only speeds things up and does not change build results; full tests must still run on a cache hit.

## 6. Security Configuration

1. Secrets are injected via repository Secrets; writing them into workflow files or logs is forbidden.
2. Each workflow explicitly declares `permissions`, defaulting to `contents: read`.
3. Third-party Actions reference a fixed version or commit hash; avoid floating tags.
4. When a PR comes from a Fork, injecting Secrets is forbidden to prevent privilege escalation attacks.
5. Release jobs are separated from main checks and triggered only on protected branches or tags.

## 7. Status Badges

Workflows should provide status badges for the README, in the format:

```markdown
[![CI](https://github.com/{owner}/{repo}/actions/workflows/ci.yml/badge.svg)](https://github.com/{owner}/{repo}/actions/workflows/ci.yml)
```

Badge parameters and ordering are in [Badge Specification](./badge-specification.md).

## 8. Forbidden Practices

1. Hardcoding secrets or internal addresses in workflows is forbidden.
2. Using `continue-on-error` to mask test failures is forbidden.
3. Configuring multiple mutually conflicting trigger rules for the same condition is forbidden.
4. Executing a release while main trunk checks have not passed is forbidden.

## Related Files

- File responsibility boundaries: see [Document Matrix](./document-matrix.md)
- Local build and testing: see [Testing Specification](./testing-specification.md)
- Release linkage: see [Push and Release Specification](./push-and-release-specification.md)
- Automated checks are dimension D9: see [Review Dimension Matrix](./review-dimension-matrix.md)
- Secrets red line: see H3 in [Hard Rules](./hard-rules.md)
