# Requirements Traceability Matrix Specification

> What this file solves: Defines the bidirectional traceability matrix template and fields from requirements to design, implementation, testing, and release, ensuring consistent cross-references among artifacts at each lifecycle stage, assessable change impact, and detectable coverage gaps.

## 1. Specification Clauses

1. Every "Must"-level requirement must occupy one row in the traceability matrix and record the full chain of artifacts from initiation to release.
2. Traceability relationships must be queryable in both directions: forward from a requirement to downstream artifacts, and backward from an artifact to upstream requirements.
3. When one requirement corresponds to multiple artifacts, use a comma-separated list of numbers; the numbers must be exactly consistent with the definitions in the corresponding documents.
4. Requirement changes must be tracked in the matrix, recording the reason for change, scope of impact, and decision maker; original values must not be overwritten directly.
5. The matrix must be checked before every version release; "Must"-level requirements that are not closed must not be released.
6. Coverage calculation method: Requirements coverage = Number of released "Must"-level requirements / Total number of "Must"-level requirements.

## 2. Traceability Matrix Template

```markdown
# Requirements Traceability Matrix: {{项目名称}}

Version: {{vX.Y.Z}} ｜ Updated by: {{姓名}} ｜ Last checked: {{YYYY-MM-DD}}

| Requirement ID | Requirement Title | Priority | Initiation Goal | Architecture Decision | Design Document | Implementation PR | Test Case | Release Version | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | {{标题}} | Must | G1 | ADR-0002 | docs/api.md#check | #12 | TC-001, TC-002 | v1.0.0 | Verified |
| REQ-002 | {{标题}} | Should | G2 | — | — | #15 | TC-005 | — | Implemented |
| REQ-003 | {{标题}} | Must | G1 | ADR-0003 | docs/architecture.md#flow | — | — | — | Pending Implementation |

Status: Pending Confirmation / Confirmed / Pending Implementation / Implemented / Verified / Released / Deprecated
```

## 3. Reverse Index Template

```markdown
## Reverse Lookup by Artifact

| Artifact Type | Artifact Number | Covered Requirement IDs |
| --- | --- | --- |
| Architecture Decision | ADR-0002 | REQ-001, REQ-004 |
| Test Case | TC-001 | REQ-001 |
| Implementation PR | #12 | REQ-001, REQ-007 |
| Release Version | v1.0.0 | REQ-001, REQ-002 |
```

## 4. Change Record Template

```markdown
## Change Record

| Date | Requirement ID | Change Content | Reason | Scope of Impact | Decision Maker |
| --- | --- | --- | --- | --- | --- |
| {{YYYY-MM-DD}} | {{REQ-NNN}} | {{字段：原值 → 新值}} | {{依据}} | {{受影响的下游产物}} | {{姓名}} |
```

## 5. Field Definitions

| Field | Required | Type | Filling Guidance | Example |
| --- | --- | --- | --- | --- |
| Requirement ID | Yes | `REQ-NNN` | Consistent with the numbering in [Project Initiation and Requirements Specification](./project-initiation-and-requirements-specification.md) | `REQ-001` |
| Priority | Yes | Enum | Must / Should / Could | `Must` |
| Initiation Goal | Yes | `G-N` | Corresponds to the goal number in the project initiation document | `G1` |
| Architecture Decision | No | `ADR-NNNN` | If none, write "—"; must not be left blank | `ADR-0002` |
| Design Document | No | `path#anchor` | Precise to the section anchor | `docs/api.md#check` |
| Implementation PR | No | `#number` | PR number, not a commit hash | `#12` |
| Test Case | Yes | `TC-NNN` list | At least one; if none, explain the reason | `TC-001` |
| Release Version | No | `vX.Y.Z` | Consistent with the tag | `v1.0.0` |
| Status | Yes | Enum | One of seven states, forward only, except for deprecation | `Verified` |
| Change Record.Scope of Impact | Yes | Text | List the affected ADRs, PRs, and TCs | `ADR-0002, TC-001` |

## 6. Filling Instructions

1. **Consistent numbering**: Requirement IDs, ADR numbers, and TC numbers in the matrix must be character-for-character consistent with the source documents; abbreviations or aliases are prohibited.
2. **Null value convention**: Write "—" for not applicable, and "To be supplemented" for not yet produced; the two have different meanings and must not be confused.
3. **Reverse index**: After each update of the forward matrix, synchronously update the reverse index; if the two are inconsistent, the forward matrix prevails and must be corrected immediately.
4. **Change tracking**: Before modifying any field, first append a row in the change record stating the old and new values; direct overwriting is prohibited.
5. **Release check**: Before release, check item by item whether "Must"-level requirements have test cases and release versions; missing either item blocks release.
6. **Deprecated requirements**: Keep the row without deleting it, change the status to "Deprecated", and state the reason for deprecation in the change record.

Common mistakes:

| Incorrect Wording | Problem | Correction |
| --- | --- | --- |
| Test case field left blank | Coverage gaps are invisible | Fill in "To be supplemented" and clear before release |
| PR field filled with a commit hash | Review records cannot be located | Use the PR number instead |
| Value changed directly during modification | Impact cannot be traced | Append a change record first |
| Status regressed from "Verified" to "Implemented" | Violates the forward-only principle | Open a new defect and start a new trace row |
| Forward and reverse indexes inconsistent | Reference mismatch | Sync with the forward matrix as the basis before release |

## 7. Complete Example

```markdown
# Requirements Traceability Matrix: markdown-lint-cli

Version: v1.0.0 ｜ Updated by: Wang Wu ｜ Last checked: 2026-11-20

| Requirement ID | Requirement Title | Priority | Initiation Goal | Architecture Decision | Design Document | Implementation PR | Test Case | Release Version | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | CJK/English spacing check | Must | G1 | ADR-0002 | docs/api.md#rules-spacing | #12 | TC-001, TC-002 | v1.0.0 | Released |
| REQ-002 | JSON report output | Should | G1 | — | docs/api.md#reporter | #15 | TC-011 | v1.0.0 | Released |
| REQ-003 | Editor plugin integration | Could | G2 | To be supplemented | To be supplemented | — | To be supplemented | — | Pending Confirmation |

## Change Record

| Date | Requirement ID | Change Content | Reason | Scope of Impact | Decision Maker |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | REQ-003 | Priority: Should → Could | Insufficient schedule for v1.0 | ADR-0005, TC-020 | Li Si |
```

## Related Files

- Requirement numbering and acceptance criteria: [Project Initiation and Requirements Specification](./project-initiation-and-requirements-specification.md)
- Architecture decision numbering: [Architecture Design Document Specification](./architecture-design-document-specification.md)
- Test case numbering: [Testing Specification](./testing-specification.md)
- Release versions and tags: [Version Management Specification](./version-management-specification.md)
- External change descriptions of versions: [Changelog Specification](./changelog-specification.md)
- Process retrospective after iteration ends: [Iteration Retrospective Specification](./iteration-retrospective-specification.md)
