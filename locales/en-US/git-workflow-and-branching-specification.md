# Git Workflow and Branching Specification

> What this file solves: Defines the branching model, naming rules, pull request description template, and merge strategy to keep the mainline stable, collaboration orderly, and changes traceable.

## 1. Specification Provisions

1. The default branch (`main` or `master`) must be protected; direct push is prohibited (corresponds to hard rule H7).
2. All changes are merged into the mainline via a personal branch and a pull request.
3. Long-lived and short-lived branches must be clearly distinguished to avoid branches remaining unmerged for long periods.
4. `git push --force` on public branches is prohibited; use `--force-with-lease` to rewrite personal branches (corresponds to H8).
5. Do not rebase or amend pushed public branches; CI and code review must pass before merging.

## 2. Branching Model

| Branch Type | Lifecycle | Created From | Merged Into | Naming Format | Example |
| --- | --- | --- | --- | --- | --- |
| Default branch | Long-lived | — | — | `main` | `main` |
| Feature branch | Short-lived, ≤2 weeks | `main` | `main` | `feat/<short description>` | `feat/user-login` |
| Fix branch | Short-lived, ≤1 week | `main` | `main` | `fix/<short description>` | `fix/token-expiry` |
| Docs branch | Short-lived | `main` | `main` | `docs/<short description>` | `docs/api-guide` |
| Release branch | Medium-lived | `main` | `main` + tag | `release/<version>` | `release/1.2.0` |
| Hotfix | Short-lived, ≤24 hours | Release tag | `main` + tag | `hotfix/<short description>` | `hotfix/payment-error` |

Naming rules: lowercase kebab-case; the short description must express intent; `test`, `temp`, `wip`, and `my-xxx` are prohibited; when linked to a requirement, append the requirement ID, e.g. `feat/spacing-rule-req001`.

## 3. Pull Request Description Template

```markdown
## Purpose of Change
{{一句话说明为什么需要此变更，关联需求编号}}

## Changes
- {{具体改动 1}}
- {{具体改动 2}}

## Scope of Impact
- Affected modules: {{模块名}}
- Breaking compatibility: {{是 / 否；是则给出迁移说明}}
- Configuration or data migration involved: {{是 / 否；是则说明}}

## Verification
- Self-test command: {{命令}}
- New or modified tests: {{TC 编号}}
- CI run URL: {{URL}}

## References
- Requirement: {{REQ-NNN}}
- Traceability matrix: {{已更新 / 待更新}}
- Documentation: {{docs/api.md#章节 / 无}}
- Issue: {{#编号 / 无}}

## Self-Check
- [ ] Commit messages conform to the specification
- [ ] No sensitive information included
- [ ] Requirements traceability matrix updated
- [ ] Breaking changes recorded in the changelog
```

## 4. Field Definitions

| Field | Required | Type | Filling Notes | Example |
| --- | --- | --- | --- | --- |
| Branch short description | Yes | kebab-case | Must express intent on its own; uninformative words are prohibited | `spacing-rule` |
| Related requirement | Yes | `REQ-NNN` | Consistent with the initiation ID | `REQ-001` |
| Purpose of change | Yes | Text | Explains "why", not "what changed" | `Fix false positives on Chinese punctuation` |
| Scope of impact | Yes | Text | Must clearly state whether compatibility is broken | `No` |
| Self-test command | Yes | Command | Copy-paste executable | `npm test -- -t spacing` |
| Test ID | Yes | `TC-NNN` | Consistent with testing specification IDs | `TC-001` |
| CI URL | Yes | URL | Easy for reviewers to verify | `https://github.com/.../runs/123` |
| Self-check list | Yes | Checkboxes | Check item by item; checking all at once is prohibited | — |

## 5. Filling Instructions

1. **Branch lifecycle**: Feature branches unmerged for more than 2 weeks must have the reason explained in the iteration retrospective and be split or closed.
2. **Short description naming**: Take the core noun + action from the change purpose; vague names such as `fix2` and `new-feature` are prohibited.
3. **Purpose of change**: Write the problem and value; "update code" and "optimize logic" are unacceptable.
4. **Scope of impact**: When marking breaking compatibility, `BREAKING CHANGE:` must also be noted in the changelog.
5. **Self-test command**: Reviewers should be able to copy and execute it directly and reach the same conclusion; for complex steps, provide a script path.
6. **Traceability matrix**: Before the PR is merged, update the implementation PR and status fields in [Requirements Traceability Matrix Specification](./requirements-traceability-matrix-specification.md).
7. **Force push**: Use `--force-with-lease` only on your own branches that have not been reviewed by others, and explain the reason in the PR.

Common mistakes:

| Incorrect Writing | Problem | Correction |
| --- | --- | --- |
| Branch names `test`, `temp` | No intent information | Change to `feat/<specific capability>` |
| PR description saying only "fix bug" | Impact cannot be reviewed | Add purpose, impact, and verification |
| Pushing directly to `main` | Violates H7 | Merge via PR |
| Force-pushing after rewriting a reviewed branch | Review conclusion becomes invalid | Add a new commit to address comments |
| Not deleting the source branch after merge | Branch list bloats | Delete immediately after merge |

## 6. Complete Example

```markdown
## Purpose of Change
Fix the false positives of the spacing rule when Chinese punctuation is adjacent to English words (REQ-004).

## Changes
- Add punctuation boundary detection to the rule engine
- Add corresponding regression tests

## Scope of Impact
- Affected modules: spacing rule
- Breaking compatibility: No
- Configuration or data migration involved: No

## Verification
- Self-test command: `npm test -- -t "中文标点"`
- New or modified tests: TC-007-regression-142
- CI run URL: https://github.com/example/markdown-lint-cli/actions/runs/128

## References
- Requirement: REQ-004
- Traceability matrix: Updated
- Documentation: None
- Issue: #142

## Self-Check
- [x] Commit messages conform to the specification
- [x] No sensitive information included
- [x] Requirements traceability matrix updated
- [x] Breaking changes recorded in the changelog (this change has none)
```

## Related Files

- Review standards and comment severity: [Code Review Specification](./code-review-specification.md)
- Commit format: [Commit Message Specification](./commit-message-specification.md)
- Traceability status updates: [Requirements Traceability Matrix Specification](./requirements-traceability-matrix-specification.md)
- Branching and release belong to dimension D8: [Audit Dimension Matrix](./review-dimension-matrix.md)
- Mandatory rules H7/H8: [Hard Rules](./hard-rules.md)
- Push operations: [Push and Release Specification](./push-and-release-specification.md)
