# Audit Report Format

> What this file solves: Defines the unique delivery format, field requirements, and filling examples for the audit report, ensuring the report can be directly executed by another agent.

The report is the sole deliverable of the audit phase. Every issue must have evidence, a responsible party, and an action; conclusions that cannot be executed must not be written into the report.

## 1. Report Skeleton

````markdown
# Push Audit Report · {{仓库名}}

Conclusion: {{结论}}
Mode: {{模式}}
Repository: {{仓库名}} · {{可见性}} · {{许可证}} · Default branch {{默认分支}}

## I. Gate Status
| Gate | Status | Pending Items |
| --- | --- | --- |
| A Security | {{门禁状态}} | {{未决项}} |
| B Quality | {{门禁状态}} | {{未决项}} |
| C Facade | {{门禁状态}} | {{未决项}} |

## II. Issue List
| Level | Dimension | Issue | Evidence (path:line / command output) | Responsible Agent | Action |
| --- | --- | --- | --- | --- | --- |
| {{等级}} | {{维度}} | {{问题}} | {{证据}} | {{责任agent}} | {{动作}} |

## III. Document Matrix Status
| File | Status | Missing / To-Change Items |
| --- | --- | --- |
| {{文件路径}} | {{状态}} | {{待改项}} |

## IV. Push Execution Checklist
- [ ] {{推送规则}}

## V. Clearance Statement
{{放行说明}}
````

## 2. Field Definitions

| Field | Required | Type | Filling Guidance | Example |
| --- | --- | --- | --- | --- |
| Repository name | Yes | Text | Exactly consistent with the GitHub repository name, character for character | `markdown-lint-cli` |
| Conclusion | Yes | Enum | Only `ALLOW PUSH` or `BLOCK PUSH`; if P0 is not cleared, it must be the latter | `BLOCK PUSH` |
| Mode | Yes | Enum | Private temporary script repositories may be written as "Reduced Audit"; all others as "Full Audit" | `Full Audit` |
| Visibility | Yes | Enum | `private` / `public`; license must be reviewed before going public | `private` |
| License | Yes | SPDX identifier | If no license, write `NONE`; in that case the conclusion must be `BLOCK PUSH` | `MIT` |
| Default branch | Yes | Text | Write the actual branch name, not the assumed `main` | `main` |
| Gate status | Yes | Enum ×3 | One row each for A/B/C; `SKIP` must have the reason noted in "Pending Items" | `FAIL` |
| Pending items | Conditionally required | Text | Required when status is `FAIL` or `SKIP`; list the blocking or skipping reason | `D1 detected .env` |
| Level | Yes | Enum | `P0` blocking / `P1` fix or register before push / `P2` suggestion | `P0` |
| Dimension | Yes | `D1`–`D14` | Numbers are listed in [Audit Dimension Matrix](./review-dimension-matrix.md) | `D1` |
| Issue | Yes | Text | One sentence stating a fact; no speculation or emotional wording | `.env exists in the root directory` |
| Evidence | Yes | path:line or command output | Must be verifiable; if evidence cannot be obtained, write `SKIP + reason` | `.env:3` |
| Responsible agent | Yes | Agent name | Write the specific executing role, not "relevant personnel" | `security-auditor` |
| Action | Yes | Text | Directly executable operation, including the target file | `Delete .env, rotate the key, and clean the history` |
| File path | Yes | Text | List item by item according to the checklist in [Document Matrix](./document-matrix.md) | `SECURITY.md` |
| Document Matrix Status | Yes | Row-by-row table | Mark each file as present, missing, or to be changed | `SECURITY.md missing` |
| Push Execution Checklist | Yes | Checkbox list | Expand rule by rule according to [Push and Release Specification](./push-and-release-specification.md) | `- [ ] Confirm .gitignore is effective` |
| Clearance Statement | Yes | Text | When blocked, write reason and conditions for lifting; when allowed, write the satisfied hard rules | `Reviewable after P0 is cleared` |

## 3. Filling Instructions

1. **Conclusion first**: First determine the number of P0 issues, then write the conclusion. If any P0 is not cleared, `ALLOW PUSH` must not be output.
2. **Evidence mandatory**: Every issue must have `path:line number` or copyable command output. Conclusions without evidence should be marked `SKIP` with the reason written, not `PASS`.
3. **Responsibility to role**: The responsible agent uses the role names in [Audit Dimension Matrix](./review-dimension-matrix.md); one issue corresponds to one responsible party.
4. **Action executable**: The action must specify the target file and operation type; "handle later" and "adjust as needed" are considered invalid.
5. **Gate consistency**: The A/B/C statuses correspond to the issue list; if any gate is `FAIL`, the conclusion must be `BLOCK PUSH`.
6. **Document matrix item by item**: List file by file according to the checklist; do not merely write "documentation is basically complete".
7. **Checklist expanded**: The push execution checklist must expand the rules item by item; "execute according to specification" must not be used as a substitute.

Common mistakes:

| Incorrect Wording | Problem | Correction |
| --- | --- | --- |
| Evidence column says "suspected problem" | No path, no output, not verifiable | Add `file path:line number` or command output |
| P0 not cleared but writes `ALLOW PUSH` | Violates hard rules | Change to `BLOCK PUSH`, list conditions for lifting |
| Uncheckable item written as `PASS` | Fabricated result | Write `SKIP` and note reason in pending items |
| Responsible party written as "relevant personnel" | No responsible entity | Write the specific agent name |
| Action written as "handle later" | Not executable | Write the target file and specific operation |
| Default branch written as `main` without verification | Inconsistent with reality | Use `git branch` output as the basis |

## 4. Complete Example

The following is a complete filling example for `BLOCK PUSH`:

````markdown
# Push Audit Report · markdown-lint-cli

Conclusion: BLOCK PUSH
Mode: Full Audit
Repository: markdown-lint-cli · private · NONE · Default branch main

## I. Gate Status
| Gate | Status | Pending Items |
| --- | --- | --- |
| A Security | FAIL | D1 detected .env, D2 no LICENSE |
| B Quality | SKIP | Dependencies not installed in the repository; build and test cannot be executed |
| C Facade | FAIL | README missing installation section and minimal example |

## II. Issue List
| Level | Dimension | Issue | Evidence (path:line / command output) | Responsible Agent | Action |
| --- | --- | --- | --- | --- | --- |
| P0 | D1 | .env exists in the root directory | `.env:3` contains DATABASE_URL | security-auditor | Delete .env, rotate database credentials, and clean the history |
| P0 | D2 | No license file | `ls LICENSE` outputs `No such file or directory` | license-checker | Repository owner confirms the license, then generate LICENSE |
| P1 | D13 | README missing installation section | `README.md:1-28` has no "Installation" heading | readme-writer | Add installation and minimal example per README Standard Template |

## III. Document Matrix Status
| File | Status | Missing / To-Change Items |
| --- | --- | --- |
| README.md | To change | Missing installation section and minimal example |
| LICENSE | Missing | Awaiting owner confirmation of license type |
| SECURITY.md | Missing | Not yet created |

## IV. Push Execution Checklist
- [ ] Confirm git status is clean
- [ ] Run key scan once (including history)
- [ ] Run build + test + lint locally
- [ ] Document matrix is complete

## V. Clearance Statement
Blocking reason: There are 2 P0 issues (credential leak, no license), and the quality gate cannot be determined because dependencies are not installed. Conditions for lifting: complete key rotation and history cleaning, determine the license, rerun tests in a buildable environment, and clear all P0 issues before re-review.
````

For `ALLOW PUSH`, section V may state: "All hard rules are satisfied, all three gates are PASS, and push can be executed." Fill in other sections according to actual conditions; evidence and checklists must not be omitted.

## 5. Delivery Order

1. Full content of the root README language navigation.
2. Full content of the README in each completed language directory, listing the language code and file path one by one.
3. Contents of the NOTICE file.
4. LICENSE option description (if the user has not specified a license, provide only candidates and differences, do not generate directly).
5. Summary of pending items.
6. Audit report (this report).
7. GitHub push guide.

## Related Files

- For gate status determination, see [Quality Gates](./quality-gate.md)
- For dimension numbers in the issue list, see [Audit Dimension Matrix](./review-dimension-matrix.md)
- For document matrix status, see [Document Matrix](./document-matrix.md)
- The push execution checklist comes from [Push and Release Specification](./push-and-release-specification.md)
- For dispatch method, see [Sub-Agent Dispatch Contract](./sub-agent-dispatch-contract.md)
