# MCP Tool Specification

> What this file solves: Defines the interface design and description rules when exposing the specification set as tools via the Model Context Protocol (MCP), ensuring tools can be correctly discovered and invoked by models.

## 1. Tool Design Principles

1. Single responsibility: One tool does one thing; avoid large, all-encompassing interfaces.
2. Clear descriptions: A tool description explains its purpose and applicable scenarios so the model can judge when to invoke it.
3. Explicit parameters: Each parameter has a type, whether it is required, a value range, and a description.
4. Structured output: Return structured data; avoid long passages of prose.

## 2. Required Fields

| Field | Requirement |
| --- | --- |
| name | Unique identifier, lowercase kebab-case |
| description | Purpose and trigger conditions, specific and determinable |
| inputSchema | Parameter types, required items, constraints |
| Return value | Structured format and field descriptions |
| Error | Return format on failure; results must not be fabricated |

## 3. Specification-Set-Related Tools

1. Document retrieval: Return specification content by language code + identifier (identifiers are covered in the [Machine-Readable Metadata Specification](./machine-readable-metadata-specification.md)).
2. Manifest: Return the list of available documents and their language mappings.
3. Validation: Check the completeness of the documentation matrix (see [Documentation Matrix](./document-matrix.md)) and gate status (see [Quality Gate](./quality-gate.md)).

## 4. Mandatory Rules

1. A tool must not return PASS for a result that cannot be checked; it must mark SKIP with a reason (see [Prohibited Practices](./prohibited-practices.md)).
2. Output must be machine-parsable and contain no internal reasoning process.
3. Security-related content must not be leaked through tools (see [Security and Privacy Specification](./security-and-privacy-specification.md)).

## Related Files

- Metadata structure: [Machine-Readable Metadata Specification](./machine-readable-metadata-specification.md)
- Skill packaging: [Skill Authoring Specification](./skill-authoring-specification.md)
- Agent invocation conventions: [Agent Invocation and Prompt Specification](./agent-invocation-and-prompt-specification.md)
