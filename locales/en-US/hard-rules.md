# Hard Rules

> What this file solves: Lists inviolable rules whose violation of any one blocks push and does not allow "pushing first and fixing later".

## Hard Rules Table

| # | Rule |
|---|---|
| H1 | The repository name must comply with [Project Naming Specification](./project-naming-specification.md), with letter case, characters, and length all compliant |
| H2 | A `LICENSE` file must exist; no license = copyright reserved by default, must not be made public |
| H3 | Do not commit any secrets, tokens, private keys, `.env`, cloud provider AK/SK, or database connection strings |
| H4 | Do not commit build artifacts, dependency directories, IDE configuration, or system junk files |
| H5 | A single file must not exceed 100MB; files over 50MB must use LFS or be excluded |
| H6 | A `README.md` must exist and contain: a one-sentence positioning, installation, a minimal runnable example, and the license |
| H7 | The default branch must be protected; direct push to `main`/`master` is prohibited |
| H8 | Using `git push --force` on public branches is prohibited; personal branches may only use `--force-with-lease` |
| H9 | `build` and `test` must pass before push; if CI is red, merging into the mainline is prohibited |
| H10 | Commit messages must conform to Conventional Commits; uninformative commits such as `wip`/`update`/`fix bug` are prohibited |
| H11 | Each document must be a separate file with a separate responsibility; piling all content into the README is prohibited (see [Document Matrix](./document-matrix.md)) |
| H12 | Once a secret has been pushed, the secret must be rotated immediately and history cleaned; a deletion-only commit is not acceptable |

## Execution Constraints

- Violation of any one rule **blocks push**; "pushing first and fixing later" is not allowed.
- The judgment results of H1–H12 must be reflected in the issue list of [Audit Report Format](./audit-report-format.md), each with evidence (path:line / command output).
- When H12 is violated, execute per the incident handling process of [Push and Release Specification](./push-and-release-specification.md).

## Related Files

- For naming details, see [Project Naming Specification](./project-naming-specification.md)
- For gate clearance conditions, see [Quality Gates](./quality-gate.md)
- For a summary of prohibited practices, see [Prohibited Practices](./prohibited-practices.md)
