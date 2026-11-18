# Issue and PR Template Specification

> What this file solves: Defines the field design, format, and writing requirements for `.github/ISSUE_TEMPLATE/*.yml` structured forms and the `.github/PULL_REQUEST_TEMPLATE.md` self-check list, so that problem feedback and change submission have executable input constraints.

## 1. Design Principles

1. **Structure over free text**: Issue forms are defined in YAML, using drop-downs, checkboxes, and required fields to guide filling and reduce unhelpful feedback.
2. **Minimize required fields**: Keep only fields necessary to locate the problem; optional fields must not be marked as required.
3. **Explicit self-checks**: The PR template lists checkable self-check items as a checklist to prevent contributors from skipping key steps.
4. **Single responsibility**: Issue forms collect information and do not carry project introductions; PR templates handle self-checks and do not repeat feature descriptions (corresponds to [Document Matrix](./document-matrix.md)).

## 2. Issue Form Structure

### 2.1 Files and Naming

- The path is fixed as `.github/ISSUE_TEMPLATE/*.yml`, one file per template.
- File names use lowercase and hyphens, such as `bug-report.yml`, `feature-request.yml`, and `question.yml`.
- Provide at least two templates: "Bug report" and "Feature request".

### 2.2 Standard Fields

| Field | Type | Required | Purpose |
| --- | --- | --- | --- |
| `name` | String | Yes | Template display name |
| `description` | String | Yes | Template purpose description |
| `title` | String prefix | Yes | Auto-generated issue title prefix |
| `labels` | Array | No | Automatically applied labels |
| `body` | Array | Yes | List of form fields |

Common field types in `body`:

| Type | Use Case | Example |
| --- | --- | --- |
| `markdown` | Explanatory text, no input | Filling instructions |
| `textarea` | Long text description | Issue reproduction steps |
| `input` | Single-line short text | Version number |
| `dropdown` | Limited options | Operating system, severity |
| `checkboxes` | Multiple confirmations | Whether duplicate issues were searched |

### 2.3 Bug Report Field Checklist

1. Problem description (`textarea`, required): What happened.
2. Expected behavior (`textarea`, required): What should have happened.
3. Reproduction steps (`textarea`, required): Listed with numbers and independently reproducible.
4. Runtime environment (`input` or `dropdown`): Operating system, runtime, project version.
5. Logs or screenshots (`textarea`): Provide error information; sensitive information must be redacted.
6. Duplicate check confirmation (`checkboxes`, required): Existing issues have been searched.

### 2.4 Feature Request Field Checklist

1. Problem statement (`textarea`, required): What capability is currently missing.
2. Use case (`textarea`, required): Who needs it and under what circumstances.
3. Desired solution (`textarea`): How it is hoped to be implemented.
4. Alternatives (`textarea`): Other approaches already considered.
5. Compatibility impact (`dropdown`): Whether breaking changes are involved.

## 3. PR Template Structure

### 3.1 Required Sections

`PULL_REQUEST_TEMPLATE.md` must contain the following sections in a fixed order:

1. Change description: What this change does and the corresponding issue number.
2. Change type: Select via checkboxes (feature, fix, docs, refactor, test, etc.; see [Commit Message Specification](./commit-message-specification.md) for types).
3. Self-check list: Checkable self-check items.
4. Breaking changes: Write "None" if there are none; if there are, describe the migration path (see [Migration Guide Specification](./migration-guide-specification.md)).
5. Related documentation: Whether README, CHANGELOG, and API documentation were updated synchronously.

### 3.2 Self-Check List Example

```markdown
## Self-Check List

- [ ] Local build passes
- [ ] Related tests pass and tests have been added for new features
- [ ] Commit messages follow [Commit Message Specification](./commit-message-specification.md)
- [ ] Documentation updated synchronously or confirmed not to need updating
- [ ] No secrets, private data, or large files introduced
```

## 4. Copyable Templates

### 4.1 Bug Report Form

Save as `.github/ISSUE_TEMPLATE/bug-report.yml`:

```yaml
name: Bug report
description: Report a reproducible functional anomaly
title: "[Bug]: "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        Search existing issues before submitting to avoid duplicates.
        Do not paste secrets, tokens, or personal private information.
  - type: checkboxes
    id: duplicate-check
    attributes:
      label: Duplicate check
      options:
        - label: I have searched existing issues and confirmed this is not a duplicate
          required: true
  - type: textarea
    id: description
    attributes:
      label: Problem description
      description: What actually happened
      placeholder: After running the install command, the process exits with code 1
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Expected behavior
      description: What should have happened
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: Reproduction steps
      description: List with numbers so others can reproduce independently
      placeholder: |
        1. Execute the command
        2. Observe the output
        3. An error occurs
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: Project version
      placeholder: v1.0.0
    validations:
      required: true
  - type: dropdown
    id: os
    attributes:
      label: Operating system
      options:
        - macOS
        - Linux
        - Windows
        - Other
    validations:
      required: true
  - type: textarea
    id: logs
    attributes:
      label: Logs or screenshots
      description: Provide error information; sensitive information must be redacted
      render: shell
  - type: checkboxes
    id: security
    attributes:
      label: Information security confirmation
      options:
        - label: Confirmed no secrets, tokens, or personal private information included
          required: true
```

### 4.2 Feature Request Form

Save as `.github/ISSUE_TEMPLATE/feature-request.yml`:

```yaml
name: Feature request
description: Propose a new capability or improvement
title: "[Feature]: "
labels: ["enhancement"]
body:
  - type: textarea
    id: problem
    attributes:
      label: Problem statement
      description: What capability is currently missing
    validations:
      required: true
  - type: textarea
    id: scenario
    attributes:
      label: Use case
      description: Who needs this capability and under what circumstances
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: Desired solution
      description: How it is hoped to be implemented
  - type: textarea
    id: alternatives
    attributes:
      label: Alternatives
      description: Other approaches already considered
  - type: dropdown
    id: breaking
    attributes:
      label: Whether breaking changes are involved
      options:
        - No
        - Yes
        - Unsure
    validations:
      required: true
```

### 4.3 PR Template

Save as `.github/PULL_REQUEST_TEMPLATE.md`:

````markdown
## Change Description

{{变更说明}}

## Change Type

- [ ] Feature (feat)
- [ ] Fix (fix)
- [ ] Documentation (docs)
- [ ] Style (style)
- [ ] Refactor (refactor)
- [ ] Test (test)
- [ ] Build or toolchain (build / ci)

## Self-Check List

- [ ] Local build passes
- [ ] Related tests pass and tests have been added for new features
- [ ] Commit messages follow the commit message specification
- [ ] Documentation updated synchronously or confirmed not to need updating
- [ ] No secrets, private data, or large files introduced

## Breaking Changes

{{破坏性变更说明}}

## Related Documentation

- [ ] README synchronized or no update needed
- [ ] CHANGELOG registered
- [ ] API documentation synchronized or no update needed
````

### 4.4 Placeholder Correspondence Table

| Placeholder | Required | Filling Notes |
| --- | --- | --- |
| `{{变更说明}}` | Yes | One sentence stating the change, with an issue number in the form `#number` |
| `{{破坏性变更说明}}` | Yes | Write "None" if there are no breaking changes; otherwise write migration steps and link the migration guide |

The `name`, `description`, `title`, and `labels` of the YAML form are template metadata and should be replaced according to the actual project; field types and `required` values in `body` are adjusted per the field checklists in Sections 2 and 3, and required items must not be removed.

### 4.5 Complete Filled Example

A filled example of a bug report:

````markdown
## Problem Description

After running `npm run build`, the process exits with code 1.

## Expected Behavior

The build succeeds and outputs the `dist/` directory.

## Reproduction Steps

1. Check out the v1.0.0 tag
2. Run `npm ci`
3. Run `npm run build` and observe exit code 1

## Project Version

v1.0.0

## Operating System

macOS

## Logs or Screenshots

```
Error: Cannot find module 'mdlint-core'
```

## Information Security Confirmation

- [x] Confirmed no secrets, tokens, or personal private information included
````

## 5. Writing Requirements

1. Use imperative or declarative sentences for field descriptions; do not use colloquial language.
2. Provide a filling example or format requirement for each required field.
3. Hint text must explain "why this information is needed" and avoid vague requirements.
4. Fields involving privacy must include a redaction reminder (see [Security and Privacy Specification](./security-and-privacy-specification.md)).
5. Templates are updated as the project evolves; deprecated fields must be deleted and must not accumulate.

## 6. Prohibited Practices

1. Do not merge all issue types into a single free-text template.
2. Do not set required fields unrelated to locating the problem.
3. Do not put project introductions or marketing content in templates.
4. Do not omit the self-check list and breaking change statement from the PR template.

## Related Files

- For document responsibility boundaries, see [Document Matrix](./document-matrix.md)
- For the contribution process, see [Contribution Guide Specification](./contribution-guide-specification.md)
- For review standards, see [Code Review Specification](./code-review-specification.md)
- For breaking change migration, see [Migration Guide Specification](./migration-guide-specification.md)
- The community governance check belongs to dimension D14; see [Audit Dimension Matrix](./review-dimension-matrix.md)
