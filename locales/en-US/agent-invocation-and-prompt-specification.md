# Agent Invocation and Prompt Specification

> What this file solves: Defines the dispatch contract and prompt writing style when an Agent invokes the specification set, ensuring invocations are verifiable, do not exceed authority, and do not drift.

## 1. Invocation Principles

1. Single responsibility: One invocation completes one thing; doing other tasks "along the way" is prohibited.
2. Separation of read and write: Sub-agents only read and analyze; file writing and git operations are performed centrally by the controller (see [Sub-Agent Dispatch Contract](./sub-agent-dispatch-contract.md)).
3. Evidence requirement: Conclusions must carry evidence (path + line number / command output); without evidence they are considered invalid.
4. No direct communication: Sub-agents do not communicate directly with each other; everything is aggregated through the controller.

## 2. Prompt Structure

An invocation prompt must contain four elements:

```text
TASK:    <one-sentence task>
INPUT:   <necessary context, only the required part>
OUTPUT:  <structured output format, table or JSON, no prose>
FAIL:    <return convention when it cannot be completed, do not fabricate>
```

## 3. Prompt Writing Style

1. Use formal written language and imperative sentences with complete information, not relying on contextual inference (see [General Writing Specification](./general-writing-specification.md)).
2. Specify the output format and failure return; avoid letting the model improvise.
3. Give file paths when referencing specifications (see [Machine-Readable Metadata Specification](./machine-readable-metadata-specification.md)).
4. Use a unified format for templates and placeholders (see [Information Collection and Templates](./information-collection-and-templates.md)).

## 4. Mandatory Rules

1. Do not require the Agent to fabricate check results; mark non-checkable items as SKIP + reason.
2. Do not write internal reasoning into deliverables (see [Prohibited Practices](./prohibited-practices.md)).
3. Security-related content is handled per the [Security and Privacy Specification](./security-and-privacy-specification.md).

## Related Files

- Dispatch contract: [Sub-Agent Dispatch Contract](./sub-agent-dispatch-contract.md)
- Machine metadata: [Machine-Readable Metadata Specification](./machine-readable-metadata-specification.md)
- Skill packaging: [Skill Authoring Specification](./skill-authoring-specification.md)
- MCP tools: [MCP Tool Specification](./mcp-tool-specification.md)
