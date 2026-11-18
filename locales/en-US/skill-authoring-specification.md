# Skill Authoring Specification

> What this file solves: Defines the structure, trigger conditions, and progressive loading approach when packaging the specification set as a Skill, ensuring the Skill is discoverable, maintainable, and free of duplicate content.

## 1. Directory Structure

A Skill uses an "entry point + on-demand resources" structure:

```text
skill-name/
├── SKILL.md           Required: metadata + core workflow
├── references/        Specification body, loaded on demand
└── assets/            Templates and assets (optional)
```

## 2. SKILL.md Requirements

1. Metadata includes `name` and `description`; the description must state "what it does + when to use" to enable triggering.
2. The body retains only resident core rules and workflows; detailed lookup content goes into `references/`.
3. Use imperative/infinitive style; avoid second person.
4. When referencing resources, give explicit paths and the conditions for "when to read" them.

## 3. Mandatory Rules

1. The specification body is maintained in only one place: the Skill references files from this specification set rather than copying the full text, avoiding two-copy drift.
2. One Skill does one thing; cramming multiple responsibilities into the same Skill is prohibited.
3. Write concrete phrases in trigger conditions; avoid overly broad triggering.
4. The version is updated in sync with the specification set version.

## Related Files

- Manifest structure: [Machine-Readable Metadata Specification](./machine-readable-metadata-specification.md)
- Single responsibility of documents: [Documentation Matrix](./document-matrix.md)
- Agent invocation conventions: [Agent Invocation and Prompt Specification](./agent-invocation-and-prompt-specification.md)
