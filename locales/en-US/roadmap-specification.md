# Roadmap Specification

> What this file solves: Defines the roadmap template, fields, status annotations, and non-commitment principle, avoiding presenting plans as commitments and ensuring consistency with the changelog and iteration retrospectives.

## 1. Specification Clauses

1. The roadmap must prominently state "This roadmap is a plan, not a delivery commitment."
2. Specific delivery dates must not be promised; target versions are expressed as version ranges or quarters.
3. Status changes must leave a trace, and cancelled items must state the reason.
4. Completed items must point to the corresponding entry in the [Changelog Specification](./changelog-specification.md) to avoid inconsistent information between the two places.
5. The roadmap addresses future plans and allows adjustment and cancellation; the changelog addresses released facts and historical entries must not be rewritten.
6. Each planned item must be associated with at least one requirement or iteration improvement action; see the [Requirements Traceability Matrix Specification](./requirements-traceability-matrix-specification.md) for the traceability relationship.

## 2. Roadmap Template

```markdown
# Roadmap: {{项目名称}}

> This roadmap is a plan, not a delivery commitment. Target versions and quarters are estimates only and may be adjusted as priorities change.

Version: {{v1.0}} | Updater: {{姓名}} | Last reviewed: {{YYYY-MM-DD}}

## Now / Next / Later

| Phase | Planned Item | Status | Target Version | Related Requirement | Dependency | Acceptance Criteria | Changelog |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Now | {{能力描述}} | In progress | {{v1.0}} | {{REQ-001}} | {{无}} | {{可验证条件}} | — |
| Next | {{能力描述}} | Planned | {{v1.1 ~ v1.2}} | {{REQ-008}} | {{计划项 A}} | {{可验证条件}} | — |
| Later | {{能力描述}} | Planned | {{待定}} | {{REQ-015}} | {{外部依赖}} | {{可验证条件}} | — |
| Cancelled | {{能力描述}} | Cancelled | — | {{REQ-020}} | — | — | — |

Status: Planned / In progress / Completed / Cancelled

## Status Change Log
| Date | Planned Item | Old Status → New Status | Reason | Decision Maker |
| --- | --- | --- | --- | --- |
| {{YYYY-MM-DD}} | {{计划项}} | {{规划中 → 已取消}} | {{原因}} | {{姓名}} |

## Cancellation Notes
- {{计划项}}: {{取消原因，如需求变更、依赖 unavailable}}
```

## 3. Planned Item Template

```markdown
### {{计划项名称}}

- Status: {{规划中 / 进行中 / 已完成 / 已取消}}
- Target Version: {{vX.Y / 季度 / 待定}}
- Related Requirement: {{REQ-NNN}}
- Source: {{立项书 / 迭代回顾 A-NN / 用户反馈}}
- Dependency: {{前置计划项或外部依赖；无则写「无」}}
- Acceptance Criteria: {{可验证的完成条件，须含阈值}}
- Reason Not Completed: {{仅已取消项填写}}
```

## 4. Field Definitions

| Field | Required | Type | Filling Notes | Example |
| --- | --- | --- | --- | --- |
| Planned Item | Yes | Noun phrase | Describes the capability to be delivered, not a task action | `TOML configuration support` |
| Status | Yes | Enumeration | Planned / In progress / Completed / Cancelled | `In progress` |
| Target Version | Yes | Version / Quarter / TBD | Specific dates are prohibited | `v1.1 ~ v1.2` |
| Related Requirement | Yes | `REQ-NNN` | Consistent with the project initiation number | `REQ-008` |
| Source | Yes | Text | Project initiation, iteration retrospective, or user feedback | `Iteration retrospective A-01` |
| Dependency | Yes | Text | Write "None" if none; must not be left blank | `Depends on planned item A` |
| Acceptance Criteria | Yes | Text | Verifiable, includes thresholds | `Parses 100 samples with no failures` |
| Changelog | Conditionally required | Link | Required for completed items | `[1.0.0]` |
| Cancellation Reason | Conditionally required | Text | Required for cancelled items | `The dependent external API was discontinued` |

## 5. Filling Instructions

1. **Phase division**: three tiers of "Now / Next / Later"; "Now" must not exceed 3 items; any excess requires reprioritization.
2. **Non-commitment**: date commitments such as "release in Q3" or "complete in December" are prohibited; express expectations with version numbers or quarter ranges.
3. **Acceptance criteria**: must be objectively determinable; "improve usability" is unacceptable, "reduce configuration items from 5 to 2" is acceptable.
4. **Status changes**: append a record for each change without overwriting the original value; cancelled items retain their row and state the reason.
5. **Completion linkage**: when the status changes to "Completed", the changelog anchor must be filled in at the same time; an item without a corresponding log must not be marked complete.
6. **Retrospective linkage**: when improvement actions from an iteration retrospective are included in the roadmap, mark A-NN in "Source" and record them synchronously in the [Iteration Retrospective Specification](./iteration-retrospective-specification.md).
7. **README summary**: the README contains only the three-tier summary and links; the full table stays in this file, see the [README Sections Specification](./readme-sections-specification.md).

Common mistakes:

| Incorrect Wording | Problem | Correction |
| --- | --- | --- |
| "Release in December 2026" | Constitutes a commitment | Change to `v1.2` or `Q4` |
| Completed item with no changelog link | Inconsistent information between two places | Add the log anchor |
| Deleting the row directly for a cancelled item | History is not traceable | Retain the row and state the reason |
| Planned item written as "optimize performance" | No acceptance criteria | Add threshold metrics |
| Roadmap crammed with 20 items | Priorities cannot be determined | Converge to three tiers with a limit per tier |

## 6. Complete Example

```markdown
# Roadmap: markdown-lint-cli

> This roadmap is a plan, not a delivery commitment.

Version: v1.0 | Updater: 李四 | Last reviewed: 2026-11-20

| Phase | Planned Item | Status | Target Version | Related Requirement | Dependency | Acceptance Criteria | Changelog |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Now | Core rule set | Completed | v1.0.0 | REQ-001~007 | None | Detection rate ≥95% on 50 samples | [1.0.0] |
| Next | Editor plugin integration | Planned | v1.1 | REQ-003 | Core rule set stable | Callable from mainstream editors | — |
| Later | Custom rule DSL | Planned | TBD | REQ-018 | Plugin API stable | Users can add rules without changing source | — |
| Cancelled | Cloud rule sync | Cancelled | — | REQ-020 | — | — | — |

## Status Change Log
| Date | Planned Item | Old Status → New Status | Reason | Decision Maker |
| --- | --- | --- | --- | --- |
| 2026-11-15 | Cloud rule sync | Planned → Cancelled | No server-side maintenance resources | 李四 |
```

## Related Files

- Version naming and target versions: [Version Management Specification](./version-management-specification.md)
- Project initiation basis and requirement numbering: [Project Initiation and Requirements Specification](./project-initiation-and-requirements-specification.md)
- External record of completed items: [Changelog Specification](./changelog-specification.md)
- Source of improvement actions: [Iteration Retrospective Specification](./iteration-retrospective-specification.md)
- Requirements-to-plan traceability: [Requirements Traceability Matrix Specification](./requirements-traceability-matrix-specification.md)
- README roadmap section: [README Sections Specification](./readme-sections-specification.md)
