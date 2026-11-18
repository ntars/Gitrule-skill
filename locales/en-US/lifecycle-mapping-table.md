# Lifecycle Mapping Table

> What this file solves: Maps all specifications to the eight phases of the project lifecycle, providing each phase's entry conditions, key outputs, core specifications, and exit gates, serving as a single navigation entry point for accessing specifications "from inside out and from start to finish".

This file answers only "which specifications are needed at a given phase and when the next phase may be entered." The specific provisions of each specification within a phase remain subject to the corresponding file; see [Execution Process](./execution-process.md) for the operational process and [Specification Selection Guide](./specification-selection-guide.md) for tailoring by project type.

## 1. Phase Overview

| Phase | Name | Core Question | Key Outputs | Exit Gate |
| --- | --- | --- | --- | --- |
| 1 | Project Initiation | What to build, what to call it, and how to set up the repository | Naming conclusion, repository metadata table, information list | Naming compliant, required information complete or marked |
| 2 | Requirements Analysis | What the requirements are and how to accept them | Requirements list, acceptance criteria, traceability matrix | Every requirement has a unique ID and acceptance criteria |
| 3 | Architecture Design | How to decompose, and how to define interfaces and data | Architecture document, API contract, data model | No gaps in requirements-to-design traceability, interfaces reviewed |
| 4 | Development and Implementation | How to write code and commits consistently | Code, commit sequence, CI workflow, API documentation | Review passed, CI green, no high-severity dependency vulnerabilities |
| 5 | Testing and Verification | Whether releasable quality is achieved | Test suite, coverage report, gate decisions | Build and tests passed, P0 cleared |
| 6 | Deployment and Release | How to release, and how the front page is presented | Tag, Release, front-page documentation, rollback plan | All three gate layers green, rollback plan verified |
| 7 | Operations and Monitoring | How to detect issues and how to respond | Monitoring alerts, response process, incident documents | Key metrics have alerts configured, response channels available |
| 8 | Iteration and Maintenance | How to retrospect and how to evolve | Retrospective report, roadmap update, migration guide | Action items registered, breaking changes have migration paths |

Phases 1–5 advance from inside out, while phases 6–8 shift from delivery to operations and evolution. Phases 7 and 8 may occur in parallel, but neither may skip the gate of phase 5.

## 2. Phase One: Project Initiation

- **Phase objective**: Determine the project's positioning, compliant naming, and repository metadata, establishing an information baseline shared by subsequent phases.
- **Entry conditions**: The project idea is formed, and the target users and the problem to be solved can be stated.
- **Core specifications**: [Roles and Responsibilities](./roles-and-responsibilities.md), [Project Initiation and Requirements Specification](./project-initiation-and-requirements-specification.md), [Project Naming Specification](./project-naming-specification.md), [Information Collection and Templates](./information-collection-and-templates.md), [Execution Process](./execution-process.md).
- **Key outputs**: Three naming candidates and name-collision search conclusions; repository metadata table (description, topics, default branch, visibility, license); list of required information and list of missing information.
- **Exit gate**: The repository name complies with all hard rules of [Project Naming Specification](./project-naming-specification.md); the license type is determined; required fields are complete and missing items are marked per [Information Collection and Templates](./information-collection-and-templates.md).

## 3. Phase Two: Requirements Analysis

- **Phase objective**: Break the idea down into verifiable and traceable requirement items, and form a roadmap accordingly.
- **Entry conditions**: The naming and metadata conclusions of phase one are confirmed.
- **Core specifications**: [Project Initiation and Requirements Specification](./project-initiation-and-requirements-specification.md), [Requirements Traceability Matrix Specification](./requirements-traceability-matrix-specification.md), [Roadmap Specification](./roadmap-specification.md), [Information Collection and Templates](./information-collection-and-templates.md).
- **Key outputs**: Requirements list with unique IDs; acceptance criteria for each requirement; initial version of the requirements traceability matrix; roadmap organized by priority.
- **Exit gate**: Every requirement has a unique ID and determinable acceptance criteria; the traceability matrix has established requirement-side fields; planned items in the roadmap are marked as non-delivery commitments.

## 4. Phase Three: Architecture Design

- **Phase objective**: Determine module boundaries, interface contracts, and the data model so that requirements can be assigned to specific design units.
- **Entry conditions**: The requirements list and acceptance criteria are confirmed.
- **Core specifications**: [Architecture Design Document Specification](./architecture-design-document-specification.md), [API Design Specification](./api-design-specification.md), [Database Design Specification](./database-design-specification.md), [Document Matrix](./document-matrix.md), [General Writing Specification](./general-writing-specification.md).
- **Key outputs**: Architecture design document; API contract; data model and migration strategy; document matrix list.
- **Exit gate**: Every requirement points to at least one design unit in the traceability matrix; interfaces and the data model are reviewed; responsibilities of files in the document matrix do not overlap.

## 5. Phase Four: Development and Implementation

- **Phase objective**: Implement the design with consistent code style, commit format, and review process, keeping dependencies and automation under control.
- **Entry conditions**: The architecture and interface contracts have passed review.
- **Core specifications**: [Code Style Specification](./code-style-specification.md), [Git Workflow and Branching Specification](./git-workflow-and-branching-specification.md), [Commit Message Specification](./commit-message-specification.md), [Code Review Specification](./code-review-specification.md), [Dependency Management Specification](./dependency-management-specification.md), [Code Ownership Specification](./code-ownership-specification.md), [API Documentation Specification](./api-documentation-specification.md), [CI Workflow Specification](./ci-workflow-specification.md).
- **Key outputs**: Code conforming to the style specification; commit sequence conforming to Conventional Commits; CI workflow; API documentation synchronized with the implementation.
- **Exit gate**: Commit messages and branch naming conform to specifications; code is reviewed and ownership routing is correct; CI workflow passes; no untreated high-severity dependency vulnerabilities.

## 6. Phase Five: Testing and Verification

- **Phase objective**: Use reproducible tests and gate decisions to confirm that deliverables meet the quality baseline required for release.
- **Entry conditions**: Feature implementation is complete and the CI workflow is runnable.
- **Core specifications**: [Testing Specification](./testing-specification.md), [Quality Gates](./quality-gate.md), [Quality Metrics Specification](./quality-metrics-specification.md), [Accessibility Specification](./accessibility-specification.md), [Security and Privacy Specification](./security-and-privacy-specification.md).
- **Key outputs**: Test suite and coverage report; item-by-item gate decisions; security and accessibility check records.
- **Exit gate**: Build, tests, and static checks pass; all P0 items of Gate A, Gate B, and Gate C are cleared; P1 items are registered as to-dos or completed.

## 7. Phase Six: Deployment and Release

- **Phase objective**: Release the version through a controlled process and complete the front-page documentation and user-visible deliverables.
- **Entry conditions**: The phase five gate is passed with no uncleared P0 items.
- **Core specifications**: [Push and Release Specification](./push-and-release-specification.md), [Version Management Specification](./version-management-specification.md), [Changelog Specification](./changelog-specification.md), [Deployment and Rollback Specification](./deployment-and-rollback-specification.md), [Migration Guide Specification](./migration-guide-specification.md), [CI Workflow Specification](./ci-workflow-specification.md), [Issue and PR Template Specification](./issue-and-pr-template-specification.md); for front-page documentation see [README Standard Template](./readme-standard-template.md), [README Sections Specification](./readme-sections-specification.md), [README Visual Layout Specification](./readme-visual-layout-specification.md), [Badge Specification](./badge-specification.md), [README Category Adaptation Guide](./readme-category-adaptation-guide.md).
- **Key outputs**: Semantic version and annotated tag; Release Notes and changelog; front-page README and community templates; deployment record and rollback plan.
- **Exit gate**: All three gate layers are green; the tag is annotated and conforms to SemVer; the rollback plan is verified; front-page documentation contains no local absolute paths or residual placeholders.

## 8. Phase Seven: Operations and Monitoring

- **Phase objective**: Establish observability and response mechanisms so that production issues can be detected, located, and handled.
- **Entry conditions**: The version is released and the service or artifact is in an available state.
- **Core specifications**: [Observability Specification](./observability-specification.md), [Incident Response Specification](./incident-response-specification.md), [Troubleshooting Specification](./troubleshooting-specification.md), [Security and Privacy Specification](./security-and-privacy-specification.md), [SECURITY Template](./security-template.md), [Disclaimer](./disclaimer.md), [Disclaimer Template](./disclaimer-template.md).
- **Key outputs**: Key metrics and alert rules; incident classification and response process; FAQ and troubleshooting documents; vulnerability intake channels.
- **Exit gate**: All key metrics have alerts configured; vulnerability reporting channels are available and verified; the incident response process has completed at least one drill or tabletop exercise.

## 9. Phase Eight: Iteration and Maintenance

- **Phase objective**: Retrospect delivered iterations, manage the evolution path, and maintain ongoing alignment of requirements with design and testing.
- **Entry conditions**: At least one release or iteration cycle is completed.
- **Core specifications**: [Iteration Retrospective Specification](./iteration-retrospective-specification.md), [Roadmap Specification](./roadmap-specification.md), [Requirements Traceability Matrix Specification](./requirements-traceability-matrix-specification.md), [Changelog Specification](./changelog-specification.md), [Migration Guide Specification](./migration-guide-specification.md), [Version Management Specification](./version-management-specification.md), [Open Source Promotion Specification](./open-source-promotion-specification.md).
- **Key outputs**: Iteration retrospective report and action items; updated roadmap and traceability matrix; migration guide for breaking changes; version change records.
- **Exit gate**: Action items from the previous round have registered owners and deadlines; breaking changes have migration paths and announcements; no broken links appear in the traceability matrix.

## 10. Cross-Cutting Specifications

The following specifications do not belong to a single phase and must remain in effect across all phases:

| Category | Specifications | How It Takes Effect |
| --- | --- | --- |
| Mandatory constraints | [Hard Rules](./hard-rules.md), [Prohibited Practices](./prohibited-practices.md) | Violation at any phase blocks progress; no exemption may be granted on grounds of schedule |
| Process and terminology | [Roles and Responsibilities](./roles-and-responsibilities.md), [Execution Process](./execution-process.md), [Glossary](./glossary.md) | Unify role division, phase terminology, and delivery order |
| Community and governance | [Contribution Guide Specification](./contribution-guide-specification.md), [Contribution Guide Template](./contribution-guide-template.md), [Code of Conduct Specification](./code-of-conduct-specification.md), [Code of Conduct Template](./code-of-conduct-template.md) | Complete before the repository becomes publicly visible, then adjust as the community grows |
| Legal and compliance | [Open Source Compliance Specification](./open-source-compliance-specification.md), [LICENSE Specification](./license-specification.md), [NOTICE Specification](./notice-specification.md), [Disclaimer](./disclaimer.md), [Disclaimer Template](./disclaimer-template.md) | Determine the license in phase one and complete all legal documents before phase six |
| Writing and multilingual | [General Writing Specification](./general-writing-specification.md), [Multilingual Specification](./multilingual-specification.md), [Highlights and Engineering Trade-offs Writing](./highlights-and-engineering-tradeoffs-guide.md), [Document Matrix](./document-matrix.md) | Run through all document production to ensure consistent expression |
| Programmatic access | [Machine-Readable Metadata Specification](./machine-readable-metadata-specification.md), [Skill Authoring Specification](./skill-authoring-specification.md), [MCP Tool Specification](./mcp-tool-specification.md), [Agent Invocation and Prompt Specification](./agent-invocation-and-prompt-specification.md) | Applied in addition when expert, Skill, MCP, or command-line invocation is required |

## 11. Degradation and Rollback

1. A private temporary script repository may be degraded to enforce only P0 gates, but it must declare "degraded mode" in the deliverables and state the items not executed.
2. When the exit gate of any phase is not passed, the next phase must not be entered; issues, responsibilities, and actions must be registered per [Audit Report Format](./audit-report-format.md).
3. When a P0 issue is found after phase six, return to phase five for re-judgment and, if necessary, execute the incident handling process in [Push and Release Specification](./push-and-release-specification.md).

## Related Files

- For the operational process within a phase, see [Execution Process](./execution-process.md)
- For tailoring specifications by project type, see [Specification Selection Guide](./specification-selection-guide.md)
- For gate judgment criteria, see [Quality Gates](./quality-gate.md)
- For the format for recording audit issues, see [Audit Report Format](./audit-report-format.md)
