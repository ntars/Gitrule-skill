# Code Review Specification

> What this file solves: Defines the pull request description template, review comment template, review records, fields, and process, ensuring merge quality and knowledge sharing.

## 1. Specification Clauses

1. The author must state the purpose of the change, scope of impact, and self-test results in the PR description; the template is in [Git Workflow and Branching Specification](./git-workflow-and-branching-specification.md).
2. Reviewers must give specific, actionable comments, distinguishing "must fix" from "suggestion".
3. At least 1 reviewer must approve before merging, with CI fully green (corresponding to hard rule H9); authors are forbidden from approving their own PRs.
4. When review comments are disputed, escalate to the maintainers for a decision (see [Code of Conduct Specification](./code-of-conduct-specification.md)).
5. Delete the source branch after merging to keep the branch list clean.

## 2. Review Checklist

Reviewers must confirm each item:

| # | Dimension | Check Point | Verdict |
| --- | --- | --- | --- |
| 1 | Correctness | Logic is correct; boundaries and exceptions handled | Pass / Needs changes |
| 2 | Testing | Changes have corresponding tests, and tests pass | Pass / Needs changes |
| 3 | Style | Complies with [Code Style Specification](./code-style-specification.md) | Pass / Needs changes |
| 4 | Security | No sensitive information, no injection risk, permission checks correct | Pass / Needs changes |
| 5 | Documentation | Interface or behavior changes are reflected in documentation | Pass / Needs changes |
| 6 | Scope | Changes are focused, with no unrelated changes | Pass / Needs changes |
| 7 | Commit message | Complies with [Commit Message Specification](./commit-message-specification.md) | Pass / Needs changes |
| 8 | Traceability | Requirements traceability matrix has been updated | Pass / Needs changes |

## 3. Review Comment Template

```markdown
### Comment {{序号}}: {{一句话标题}}

- Level: {{必须修改 / 建议 / 提问}}
- Location: {{文件路径:行号}}
- Problem: {{描述可观察的问题，不评价人}}
- Basis: {{规范条款 / 需求编号 / 风险说明}}
- Suggestion: {{具体的修改方式或替代方案}}

Example:
### Comment 1: Exception branch not covered
- Level: Must fix
- Location: `src/rules/spacing.ts:42`
- Problem: Throws an exception when input contains incomplete Markdown, instead of returning a rule-hit result.
- Basis: REQ-001 acceptance criterion 2 (boundary path).
- Suggestion: Catch the parse exception here and return a hit as "parse failed", and add a boundary test case.
```

## 4. Review Record Template

```markdown
## Review Record: {{PR 编号}}

Reviewer: {{姓名}} ｜ Review date: {{YYYY-MM-DD}} ｜ Round: {{第 N 轮}}

| Comment # | Level | Disposition | Handler | Verification |
| --- | --- | --- | --- | --- |
| 1 | Must fix | Fixed | Author | See commit abc1234 |
| 2 | Suggestion | Not adopted | Author | Reason: {{说明}} |

Conclusion: {{批准 / 需修改后再审 / 拒绝}}
- Approval conditions: All "must fix" items resolved, CI fully green.
- Outstanding items: {{无 / 列出}}
```

## 5. Field Definitions

| Field | Required | Type | Filling guidelines | Example |
| --- | --- | --- | --- | --- |
| Level | Yes | Enum | Must fix / Suggestion / Question | `Must fix` |
| Location | Yes | `path:line` | Precise to the line; writing only the filename is forbidden | `src/parser.ts:42` |
| Problem | Yes | Text | Describe the phenomenon, do not evaluate the author | `Parse exception not caught` |
| Basis | Yes | Text | Specification clause or REQ number | `REQ-001 acceptance criterion 2` |
| Suggestion | Yes | Text | Actionable, not just "please optimize" | `Catch exception and return a hit` |
| Disposition | Yes | Enum | Fixed / Not adopted / Deferred | `Fixed` |
| Verification | Yes | Text | Commit hash or review method | `See commit abc1234` |
| Conclusion | Yes | Enum | Approve / Needs re-review after changes / Reject | `Approve` |

## 6. Filling Instructions

1. **Level distinction**: "Must fix" refers to issues that block merging (correctness, security, missing tests); "Suggestion" does not affect merging; "Question" requires the author to clarify but does not require changes.
2. **Comment wording**: Describe observable problems; evaluative language such as "this is poorly written" is forbidden.
3. **Location**: Precise to the line number; cross-file issues must be labeled separately in each comment.
4. **Basis**: Trace where possible; when there is no specification basis, state the risk or impact; "I think" is forbidden.
5. **Disposition**: "Not adopted" must include a reason; "Deferred" must state where it will be tracked.
6. **Approval**: Confirm all "must fix" items are closed, and CI is fully green; authors must not approve their own PRs.
7. **Disputes**: When reviewer and author disagree, escalate to maintainers and record the decision in the review record.

Common mistakes:

| Wrong wording | Problem | Correction |
| --- | --- | --- |
| "This won't do" | No problem, no basis, no suggestion | Add the three elements |
| "Suggest optimizing performance" | Not actionable | Give a specific approach and acceptance metric |
| Only writing the filename without the line number | Hard to locate | Be precise to the line |
| Author self-approving | Violates the rule | Have someone else review |
| Using "must fix" for personal preference | Level abuse | Downgrade to "suggestion" |

## 7. Complete Example

```markdown
## Review Record: #12

Reviewer: Li Si ｜ Review date: 2026-11-18 ｜ Round: 1

| Comment # | Level | Disposition | Handler | Verification |
| --- | --- | --- | --- | --- |
| 1 | Must fix | Fixed | Wang Wu | See commit a1b2c3d |
| 2 | Suggestion | Not adopted | Wang Wu | Reason: Current QPS has not reached a bottleneck; avoid over-engineering |
| 3 | Question | Clarified | Wang Wu | Supplemented in the PR body |

Conclusion: Approve
- Approval conditions: All "must fix" items resolved, CI fully green (run #128).
- Outstanding items: None
```

## Related Files

- PR description and branching model: [Git Workflow and Branching Specification](./git-workflow-and-branching-specification.md)
- Style check basis: [Code Style Specification](./code-style-specification.md)
- Test pass criteria: [Testing Specification](./testing-specification.md)
- Traceability status updates: [Requirements Traceability Matrix Specification](./requirements-traceability-matrix-specification.md)
- Quality gate: [Quality Gate](./quality-gate.md)
- Dispute decision basis: [Code of Conduct Specification](./code-of-conduct-specification.md)
- Automated checks are dimension D9: [Review Dimension Matrix](./review-dimension-matrix.md)
