# Document Matrix

> What this file solves: Defines the unique responsibility of each deliverable document, the content strictly prohibited from being placed in it, and the splitting constraints, ensuring one file with one responsibility and no merging.

## 1. Files and Responsibilities

| File | Unique Responsibility | Strictly Prohibited From Being Placed In It |
| --- | --- | --- |
| `README.md` | Front page: what this is, how to install it, how to run it, where to see details | Full API, contribution process, changelog |
| `LICENSE` | Full license text | Any explanatory text |
| `CHANGELOG.md` | User-facing version changes | Internal refactoring details, development plans |
| `CONTRIBUTING.md` | Process and specifications for external contributors | Project feature descriptions |
| `CODE_OF_CONDUCT.md` | Code of conduct | Technical content |
| `SECURITY.md` | Vulnerability reporting channel and response policy | List of known vulnerabilities |
| `docs/api.md` | Complete API reference | Tutorials |
| `docs/architecture.md` | Architecture and module boundaries | Usage examples |
| `docs/naming.md` | Naming specification | Other specifications |
| `docs/release.md` | Release process and version strategy | Change records |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR self-check list | Project introduction |
| `.github/ISSUE_TEMPLATE/*.yml` | Structured issue forms | Free text |
| `.github/workflows/*.yml` | CI/CD | Documentation |

> Note: The specification text for `docs/naming.md` is in the [Project Naming Specification](./project-naming-specification.md); the specification text for `docs/release.md` is in the [Push and Release Specification](./push-and-release-specification.md).

## 2. Constraints

- A single file exceeding 300 lines must be split into `docs/`, with the README keeping only a summary + links.
- File names are fixed in uppercase, paths are fixed, and directory hierarchies must not be invented.
- Every document begins with one sentence stating "what this file solves" and ends with cross-links to related files.

## Related Files

- The 20-chapter structure of the README is in the [README Sections Specification](./readme-sections-specification.md)
- The standalone NOTICE specification is in the [NOTICE Specification](./notice-specification.md)
- The standalone LICENSE specification is in the [LICENSE Specification](./license-specification.md)
- Document completeness/quality is dimension D11/D12, see the [Review Dimension Matrix](./review-dimension-matrix.md)
