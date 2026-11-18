# Execution Process

> What this file solves: Defines the complete sequence of phases from initiation to delivery, the entry conditions and deliverables of each phase, and the blocking question rules when information is insufficient.

## 1. Control Push Process (Phase 0–6)

### Phase 0 · Initiation (Project Init)

Output: 3 project name candidates + selection rationale + name-collision search conclusion + repository metadata table (description / topics / default branch / visibility / license). For naming rules, see [Project Naming Specification](./project-naming-specification.md).

### Phase 1 · Inventory

Scan the repository and produce a structured inventory:

- Technology stack, entry files, package manager, lockfile
- Existing documentation, missing documentation
- Top 10 largest files by repository size
- Existing CI / templates / protection rules
- Current git status: untracked files, uncommitted changes, suspicious commits in history

### Phase 2 · Parallel Audit

Per the [Audit Dimension Matrix](./review-dimension-matrix.md), dispatch dimensions to sub-agents for parallel execution; see [Sub-Agent Dispatch Contract](./sub-agent-dispatch-contract.md) for the dispatch method. Each sub-agent returns only structured conclusions, not long prose.

### Phase 3 · Fix

List to-dos in the order P0 → P1 → P2, marking the responsible agent and planned action. Do not enter Phase 5 until P0 is cleared.

### Phase 4 · Documentation Generation

Dispatch each file per the [Document Matrix](./document-matrix.md) to the documentation agent. **Write only one file at a time; verify it before moving to the next.**

### Phase 5 · Push

Execute per the [Push and Release Specification](./push-and-release-specification.md), echoing the results item by item.

### Phase 6 · Post-Push

Create a tag, write Release Notes, verify badges and links are working, confirm CI is green, and confirm the About section information is correct.

## 2. Document Generation Process (Phases 0–5)

Proceed in phase order; do not enter the next phase until the previous one is complete.

| Phase | Name | Entry Condition | Output |
| --- | --- | --- | --- |
| 0 | Information Verification | This specification and project materials have been received | List of confirmed information, list of missing information |
| 1 | Blocking Questions | Required fields are missing (see [Information Collection and Templates](./information-collection-and-templates.md)) | Structured question list, grouped by field |
| 2 | Framework Confirmation | Required fields are complete | README chapter table of contents and key-point outline of each chapter, for user confirmation |
| 3 | Document Generation | The user confirms the framework, or explicitly states no confirmation is needed | All deliverables |
| 4 | Quality Gates | Document generation is complete | [Quality Gates](./quality-gate.md) item-by-item judgment results |
| 5 | Delivery | All gates passed or failed items marked | Output in the order of [Audit Report Format](./audit-report-format.md), with push guidance attached |

## 3. Phase 1 Questioning Rules

1. Ask questions grouped by field, no more than 15 items per round.
2. Each question must state its purpose and the chapters it affects, so the user can judge priority.
3. When the user explicitly states that an item cannot be provided, mark "【To be confirmed: field name】" at the corresponding location in the document and summarize at the end of the document.
4. When the user replies "use your judgment", a suggested value may be given, but it must be marked "【Suggested value, pending user confirmation】".

## Related Files

- For roles and responsibilities, see [Roles and Responsibilities](./roles-and-responsibilities.md)
- For required fields and missing-item markers, see [Information Collection and Templates](./information-collection-and-templates.md)
- For gate judgment, see [Quality Gates](./quality-gate.md)
