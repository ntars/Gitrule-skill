# Sub-Agent Dispatch Contract

> What this file solves: Defines the four elements that must be written clearly when dispatching tasks to sub-agents, along with collaboration constraints, ensuring structured, verifiable conclusions with no rule drift.

## 1. Four Elements of Dispatch

Every dispatch must clearly state the four elements:

```text
TASK:    <one-sentence task>
INPUT:   <required files/context, only the necessary parts>
OUTPUT:  <structured format, table or JSON, no prose>
FAIL:    <what to return when it cannot be done, instead of making things up>
```

## 2. Constraints

- A sub-agent does only one thing at a time; "while you're at it, also write the README" is forbidden.
- Sub-agents may only read and may only produce proposals; **file writing and git operations are performed uniformly by the controller**.
- Sub-agent conclusions must carry evidence (file path + line number / command output); conclusions without evidence are considered invalid.
- Sub-agents do not communicate directly with each other; everything is aggregated through the controller, avoiding rule drift.

## Related Files

- Dispatch targets and dimensions: see [Review Dimension Matrix](./review-dimension-matrix.md)
- Document writing dispatch: see [Document Matrix](./document-matrix.md)
- Dispatch occurs in Phase 2 and Phase 4 of [Execution Flow](./execution-process.md)
