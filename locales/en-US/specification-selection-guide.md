# Specification Selection Guide

> What this file solves: Provides tailoring criteria for specifications by project type, team size, and release stage, offering a minimal viable combination and a fully compliant combination so that "on-demand access" has clear judgment criteria rather than relying on individual judgment.

This file tailors the entire specification set; for type-level differences in README chapters, see [README Category Adaptation Guide](./readme-category-adaptation-guide.md), and for the complete phase mapping, see [Lifecycle Mapping Table](./lifecycle-mapping-table.md).

## 1. Selection Principles

1. **Mandatory constraints cannot be tailored**: [Hard Rules](./hard-rules.md) and [Prohibited Practices](./prohibited-practices.md) apply in full to any project at any phase.
2. **Phase gates set the lower bound**: Before entering a phase, the exit gate marked for that phase in the [Lifecycle Mapping Table](./lifecycle-mapping-table.md) must be passed, and the corresponding core specifications must not be omitted.
3. **Type differences affect only depth**: Project type determines which specifications are emphasized and which details are simplified; it does not constitute a reason to skip quality gates.
4. **Degradation must be explicitly declared**: A private temporary script repository may enforce only P0 gates, but it must mark "degraded mode" in the deliverables and list the items not executed.

## 2. Tailoring Dimensions

| Dimension | Values | Main Impact |
| --- | --- | --- |
| Project type | Library / SDK, application, command-line tool, framework, resource collection | Determines which specifications are strengthened and which details may be simplified |
| Team size | Individual, small team, organization | Determines the necessity of governance and collaboration specifications |
| Release stage | Prototype validation, first public release, stable maintenance | Determines when compliance and operations specifications are introduced |

When the three dimensions overlap, values are taken in the priority order "mandatory constraints → phase gates → release stage → project type → team size"; tailoring at a lower-priority dimension must not weaken the requirements of a higher-priority dimension.

## 3. Tailoring by Project Type

| Project Type | Should Strengthen | May Simplify | Required Deliverables |
| --- | --- | --- | --- |
| Library / SDK | [API Design Specification](./api-design-specification.md), [API Documentation Specification](./api-documentation-specification.md), [Version Management Specification](./version-management-specification.md), [Changelog Specification](./changelog-specification.md) | Deployment and rollback, observability (when only distributing artifacts), screenshot-based visual specifications | README, API documentation, LICENSE, CHANGELOG |
| Application | [README Visual Layout Specification](./readme-visual-layout-specification.md), [Accessibility Specification](./accessibility-specification.md), [Deployment and Rollback Specification](./deployment-and-rollback-specification.md), [Observability Specification](./observability-specification.md), [Troubleshooting Specification](./troubleshooting-specification.md) | API documentation, database design (when using managed services) | README, screenshots, deployment instructions, SECURITY |
| Command-line tool | [Commit Message Specification](./commit-message-specification.md), [Highlights and Engineering Trade-offs Writing](./highlights-and-engineering-tradeoffs-guide.md), [README Category Adaptation Guide](./readme-category-adaptation-guide.md), [Accessibility Specification](./accessibility-specification.md) (terminal output) | Database design, deployment and rollback (when distribution is mainly via packages) | README, usage examples, demo GIF, LICENSE |
| Framework | [Document Matrix](./document-matrix.md), [API Documentation Specification](./api-documentation-specification.md), [Contribution Guide Specification](./contribution-guide-specification.md), [Code of Conduct Specification](./code-of-conduct-specification.md), [Observability Specification](./observability-specification.md) | Database design (when no storage is built in) | README, documentation entry, contribution guide, code of conduct |
| Resource collection | [Document Matrix](./document-matrix.md), [Contribution Guide Template](./contribution-guide-template.md), [Multilingual Specification](./multilingual-specification.md), [General Writing Specification](./general-writing-specification.md) | Testing, deployment, API, database, observability | README, categorized directory, contribution guide, LICENSE |

Resource collection projects usually contain no runnable code, so [Testing Specification](./testing-specification.md) and [CI Workflow Specification](./ci-workflow-specification.md) may be marked as not applicable; however, [General Writing Specification](./general-writing-specification.md) and [Accessibility Specification](./accessibility-specification.md) must still be followed to ensure link text and list structures are usable.

## 4. Tailoring by Team Size

| Team Size | Required Additional Specifications | Specifications That May Be Omitted |
| --- | --- | --- |
| Individual | [Hard Rules](./hard-rules.md), [Project Naming Specification](./project-naming-specification.md), [README Standard Template](./readme-standard-template.md), [LICENSE Specification](./license-specification.md) | Code of conduct, code ownership, iteration retrospective, quality metrics (may be completed before the first public release) |
| Small team | Adds [Code Ownership Specification](./code-ownership-specification.md), [Contribution Guide Specification](./contribution-guide-specification.md), [CI Workflow Specification](./ci-workflow-specification.md), [Quality Gates](./quality-gate.md) to the individual baseline | Incident response, observability (may be completed after the service goes live) |
| Organization | Applies in full; additionally must implement [NOTICE Specification](./notice-specification.md), [SECURITY Template](./security-template.md), [Disclaimer](./disclaimer.md), [Incident Response Specification](./incident-response-specification.md), [Quality Metrics Specification](./quality-metrics-specification.md), [Requirements Traceability Matrix Specification](./requirements-traceability-matrix-specification.md) | None |

As team size grows, governance specifications should be completed before the repository becomes publicly visible, not added after the first release.

## 5. Tailoring by Release Stage

| Release Stage | Should Introduce | May Defer | Declaration Requirement |
| --- | --- | --- | --- |
| Prototype validation | [Hard Rules](./hard-rules.md), [Project Naming Specification](./project-naming-specification.md), [README Standard Template](./readme-standard-template.md), [General Writing Specification](./general-writing-specification.md) | Quality gates, observability, incident response, legal documents | Must mark "degraded mode" and list deferred items |
| First public release | Adds [Quality Gates](./quality-gate.md), [Open Source Compliance Specification](./open-source-compliance-specification.md), [LICENSE Specification](./license-specification.md), [Disclaimer Template](./disclaimer-template.md), [Contribution Guide Template](./contribution-guide-template.md), [Code of Conduct Template](./code-of-conduct-template.md), [SECURITY Template](./security-template.md), [Badge Specification](./badge-specification.md) to the prototype baseline | Migration guide, iteration retrospective (may be completed after the first version iteration) | P0 gate items must not be omitted |
| Stable maintenance | Adds [Changelog Specification](./changelog-specification.md), [Version Management Specification](./version-management-specification.md), [Migration Guide Specification](./migration-guide-specification.md), [Observability Specification](./observability-specification.md), [Incident Response Specification](./incident-response-specification.md), [Troubleshooting Specification](./troubleshooting-specification.md), [Iteration Retrospective Specification](./iteration-retrospective-specification.md), [Requirements Traceability Matrix Specification](./requirements-traceability-matrix-specification.md) to the first-public baseline | None | Breaking changes must have a migration path and announcement |

## 6. Combination Schemes

### 6.1 Minimal Viable Combination

Applicable to individual prototypes or private validation repositories, 10 specifications in total:

| Purpose | Specifications |
| --- | --- |
| Constraints | [Hard Rules](./hard-rules.md), [Prohibited Practices](./prohibited-practices.md) |
| Initiation | [Project Initiation and Requirements Specification](./project-initiation-and-requirements-specification.md), [Project Naming Specification](./project-naming-specification.md) |
| Front page | [README Standard Template](./readme-standard-template.md), [General Writing Specification](./general-writing-specification.md) |
| Engineering | [Code Style Specification](./code-style-specification.md), [Commit Message Specification](./commit-message-specification.md), [Testing Specification](./testing-specification.md) |
| Release | [Push and Release Specification](./push-and-release-specification.md), [LICENSE Specification](./license-specification.md) |

When using this combination, degraded mode must be declared in the deliverables, and the full combination in Section 6.3 must be completed before the first public release.

### 6.2 Standard Public Combination

Building on the minimal viable combination, complete the fundamentals of quality, compliance, governance, and operations: add [Quality Gates](./quality-gate.md), [README Sections Specification](./readme-sections-specification.md), [README Visual Layout Specification](./readme-visual-layout-specification.md), [Badge Specification](./badge-specification.md), [Document Matrix](./document-matrix.md), [Open Source Compliance Specification](./open-source-compliance-specification.md), [Disclaimer Template](./disclaimer-template.md), [SECURITY Template](./security-template.md), [Contribution Guide Template](./contribution-guide-template.md), [Code of Conduct Template](./code-of-conduct-template.md), [Changelog Specification](./changelog-specification.md), [Version Management Specification](./version-management-specification.md), [Accessibility Specification](./accessibility-specification.md), [CI Workflow Specification](./ci-workflow-specification.md), [Issue and PR Template Specification](./issue-and-pr-template-specification.md), [Security and Privacy Specification](./security-and-privacy-specification.md).

This combination satisfies all Gate A, Gate B, and Gate C clearance conditions for public repositories and is the recommended starting point for most projects.

### 6.3 Fully Compliant Combination

Applies all specifications, for organization-level projects, projects distributed in regulated scenarios, or projects requiring programmatic access via expert / Skill / MCP / command-line. The number of specifications is subject to the [Simplified Chinese Index](./README.md); when enabling, verify the phase gates of the [Lifecycle Mapping Table](./lifecycle-mapping-table.md) item by item.

## 7. Conflict Resolution

1. When a conflict arises within the same dimension, the requirements of the later release stage prevail; simplifications from the prototype stage must not carry over to the public stage.
2. When a conflict arises across dimensions, handle it according to the priority in Section 2; mandatory constraints and phase gates must not be overridden by any dimension.
3. When a project has special circumstances requiring deviation from this guide, record the deviated specifications, reasons, and compensating measures in the deliverables and submit for review.
4. Degraded mode must not be used for publicly visible repositories, nor as a basis for skipping license or security gates.

## Related Files

- For the complete mapping of phases to specifications, see [Lifecycle Mapping Table](./lifecycle-mapping-table.md)
- For type-based tailoring of README chapters, see [README Category Adaptation Guide](./readme-category-adaptation-guide.md)
- For non-tailorable constraints, see [Hard Rules](./hard-rules.md) and [Prohibited Practices](./prohibited-practices.md)
- For gate clearance conditions, see [Quality Gates](./quality-gate.md)
