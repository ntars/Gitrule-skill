# Contribution Guide Specification

> What this file solves: Defines the complete process and standards for external contributors participating in a project, serving as the writing basis for CONTRIBUTING.md.

## 1. Required Content

The contribution guide must contain the following sections:

1. **Ways to participate**: Channels such as issue discussions, documentation improvements, code contributions, and problem feedback.
2. **Development environment setup**: Dependency installation, environment requirements, and local run commands.
3. **Branching model**: Branch naming rules, which branch to branch from, and the target branch.
4. **Commit conventions**: Commit message format (see [Commit Message Specification](./commit-message-specification.md)).
5. **PR requirements**: Scope of change, self-test items, description template, and review criteria.
6. **Testing requirements**: Test commands that must pass and coverage thresholds (see [Testing Specification](./testing-specification.md)).
7. **Code of conduct**: Point to CODE_OF_CONDUCT.md (see [Code of Conduct Specification](./code-of-conduct-specification.md)).
8. **Issue conventions**: Filling requirements for questions and bug reports.
9. **License statement**: Contributions follow the project license by default (see [LICENSE Specification](./license-specification.md)).

## 2. Writing Requirements

1. Commands must be directly executable, including necessary working directory instructions.
2. Each process step must state its trigger condition and expected result.
3. Do not merely write "PRs welcome" without a substantive process (corresponds to the community governance check of [Quality Gates](./quality-gate.md)).

## Related Files

- For document responsibility boundaries, see [Document Matrix](./document-matrix.md)
- PR templates and Issue templates belong to dimension D14; see [Audit Dimension Matrix](./review-dimension-matrix.md)
- For branching and commit specifications, see [Git Workflow and Branching Specification](./git-workflow-and-branching-specification.md)
