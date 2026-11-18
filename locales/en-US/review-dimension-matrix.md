# Review Dimension Matrix

> What this file solves: Defines the 14 dimensions of Phase 2 parallel review, each dimension's check points, recommended agent, and failure level, serving as the basis for dispatch and verdicts.

## Review Dimension Matrix

| # | Dimension | Check points (keywords; details expanded by sub-agents) | Recommended agent | Failure level |
|---|---|---|---|---|
| D1 | Security and privacy | Secret scanning, `.env`, private keys, internal domains/IPs, personal information, log residue | security-auditor | P0 |
| D2 | License and legal | LICENSE existence and type, dependency license compatibility, NOTICE, third-party notices | license-checker | P0 |
| D3 | Repository hygiene | .gitignore coverage, artifacts and dependency directories, .gitattributes, LF line endings, executable bit, filename case conflicts | repo-hygienist | P0/P1 |
| D4 | Size and binaries | Files >50MB, image compression, LFS configuration, history bloat | repo-hygienist | P1 |
| D5 | Reproducible build | lockfile committed, engine version declared, build scripts, runnable in a clean environment | build-verifier | P0 |
| D6 | Testing and static checks | Unit tests pass, coverage, lint, format, type checking | ci-runner | P0/P1 |
| D7 | Commit history | Conventional Commits, atomicity, no WIP, author information, no sensitive commit messages | commit-reviewer | P1 |
| D8 | Branch and release | main protection, branch naming, tag SemVer, annotated tag, Release Notes | release-manager | P1 |
| D9 | Automation | CI workflows runnable, status badges, dependabot, CODEOWNERS, issue/PR templates | ci-runner | P1 |
| D10 | Repository metadata | description (bilingual merged format `national language \| English`, each language ≤120 characters), topics (all 20, English only, all lowercase), default branch, About links, social preview | metadata-agent | P1 |
| D11 | Documentation completeness | Item-by-item existence check against the document matrix | docs-orchestrator | P0/P1 |
| D12 | Document quality | Heading levels, code block language tags, link validity, image alt, Chinese-English spacing, no placeholders | docs-orchestrator | P1/P2 |
| D13 | README front page | One-sentence positioning, installation, quick start, badges ≤4, screenshots, no local absolute paths | readme-writer | P1 |
| D14 | Community governance | CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, Issue templates, support channels | docs-orchestrator | P2 |

## Level Meanings

- **P0**: Blocks push.
- **P1**: Should be fixed before push or must be registered as a to-do.
- **P2**: Suggested optimization.

## Dispatch and Aggregation

- The dispatch method for each dimension is in [Sub-Agent Dispatch Contract](./sub-agent-dispatch-contract.md).
- Verdict results are aggregated into the issue list of [Audit Report Format](./audit-report-format.md), each with evidence.
- The verification basis for D11/D12 is in [Document Matrix](./document-matrix.md) and [Quality Gate](./quality-gate.md).

## Related Files

- Execution timing: see Phase 2 of [Execution Flow](./execution-process.md)
- Gate release conditions: see [Quality Gate](./quality-gate.md)
