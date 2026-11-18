# Quality Gate

> What this file solves: Defines the release conditions, verdict checklist template, and fields of the three-layer gate, ensuring push release verdicts are unified, executable, and reviewable.

## 1. Three-Layer Gate

| Layer | Meaning | Release condition |
| --- | --- | --- |
| Gate A · Security gate | Secrets, privacy, licenses, large files | Zero P0 |
| Gate B · Quality gate | Build, test, lint, commit conventions, branch protection | Zero P0, P1 recorded as to-dos |
| Gate C · Front-page gate | README, metadata, document matrix, badges, links | Zero P0, P1 ≤ 3 and scheduled |

Only when A, B, and C are all green is `✅ ALLOW PUSH` output. Failed items must be corrected or annotated with reasons, and the results are written into [Audit Report Format](./audit-report-format.md).

## 2. Fourteen Verdicts Before Delivery

Before document delivery, verdicts are given item by item; failed items must be corrected or annotated with reasons.

| # | Check item | Verdict standard |
| --- | --- | --- |
| G1 | Colloquialisms and ambiguity | Full-text search for colloquial words and vague references yields 0 hits |
| G2 | Section completeness | Both Chinese and English versions have 20 chapters, in the same order |
| G3 | Feature-to-directory consistency | All features described in the README can be found as corresponding modules in the directory structure |
| G4 | Key feature evidence | Every key feature has evidence or is marked as pending |
| G5 | Design detail coverage | All 10 categories in section 8 have entries or are marked not applicable |
| G6 | Dependency completeness | Direct and indirect dependency counts match the dependency tree |
| G7 | License accuracy | Each dependency's SPDX identifier matches the official declaration |
| G8 | License full text | Licenses requiring the full text attached have the English full text included |
| G9 | Copyright notices | Both the project's own and third-party copyright notices are complete |
| G10 | Bilingual sync | Sections, tables, terminology, and code blocks are consistent on both sides |
| G11 | Command executability | Installation, quick start, and push commands are all directly executable |
| G12 | Pending-confirmation summary | All pending items are summarized and their locations locatable |
| G13 | Asset sources | All assets have source and license records |
| G14 | Sensitive information | No secrets, tokens, internal addresses, or personal privacy information |

## 3. Gate Verdict Checklist Template

```markdown
# Gate Verdict: {{项目名称}} {{版本号}}

Verdict date: {{YYYY-MM-DD}} ｜ Verifier: {{姓名}} ｜ Repository: {{owner/repo}}

## Gate A · Security gate
| # | Check item | Verdict | Evidence | Level | Disposition |
| --- | --- | --- | --- | --- | --- |
| A1 | Workspace secrets | PASS / FAIL / SKIP | {{命令输出}} | {{P0}} | {{动作}} |
| A2 | Historical secrets | PASS / FAIL / SKIP | {{命令输出}} | {{P0}} | {{动作}} |
| A3 | Sensitive information cleanup | PASS / FAIL / SKIP | {{证据}} | {{P0}} | {{动作}} |
| A4 | LICENSE existence and type | PASS / FAIL / SKIP | {{路径}} | {{P0}} | {{动作}} |
| A5 | Large files and LFS | PASS / FAIL / SKIP | {{命令输出}} | {{P0}} | {{动作}} |

Conclusion: {{PASS / FAIL}}, outstanding items: {{列出 / 无}}

## Gate B · Quality gate
| # | Check item | Verdict | Evidence | Level | Disposition |
| --- | --- | --- | --- | --- | --- |
| B1 | Build passes | PASS / FAIL / SKIP | {{CI URL}} | {{P0}} | {{动作}} |
| B2 | Tests pass | PASS / FAIL / SKIP | {{CI URL}} | {{P0}} | {{动作}} |
| B3 | lint / format | PASS / FAIL / SKIP | {{CI URL}} | {{P1}} | {{动作}} |
| B4 | Commit message conventions | PASS / FAIL / SKIP | {{git log}} | {{P1}} | {{动作}} |
| B5 | Branch protection | PASS / FAIL / SKIP | {{平台设置截图说明}} | {{P0}} | {{动作}} |

Conclusion: {{PASS / FAIL}}, outstanding items: {{列出 / 无}}

## Gate C · Front-page gate
| # | Check item | Verdict | Evidence | Level | Disposition |
| --- | --- | --- | --- | --- | --- |
| C1 | README four elements | PASS / FAIL / SKIP | {{路径:行号}} | {{P1}} | {{动作}} |
| C2 | Document matrix complete | PASS / FAIL / SKIP | {{清单}} | {{P1}} | {{动作}} |
| C3 | Metadata complete | PASS / FAIL / SKIP | {{平台设置}} | {{P1}} | {{动作}} |
| C4 | Badges usable | PASS / FAIL / SKIP | {{HTTP 检查}} | {{P2}} | {{动作}} |
| C5 | Links valid | PASS / FAIL / SKIP | {{校验输出}} | {{P1}} | {{动作}} |

Conclusion: {{PASS / FAIL}}, outstanding items: {{列出 / 无}}

## Fourteen Verdicts Before Delivery
| # | Verdict | Evidence | Disposition |
| --- | --- | --- | --- |
| G1 ~ G14 | {{PASS / FAIL / SKIP}} | {{证据}} | {{动作}} |

## Overall Verdict
- A: {{PASS / FAIL}} ｜ B: {{PASS / FAIL}} ｜ C: {{PASS / FAIL}}
- Release verdict: {{✅ ALLOW PUSH / ⛔ BLOCK PUSH}}
- Blocking reasons: {{无 / 列出 P0}}
```

## 4. Field Definitions

| Field | Required | Type | Filling guidelines | Example |
| --- | --- | --- | --- | --- |
| Verifier | Yes | Text | Unique; "team" is forbidden | `Wang Wu` |
| Verdict | Yes | Enum | PASS / FAIL / SKIP | `PASS` |
| Evidence | Yes | Text | Path + line number or command output; verdicts without evidence are forbidden | `gitleaks: 0 findings` |
| Level | Conditionally required | Enum | Required when FAIL: P0 / P1 / P2 | `P0` |
| Disposition | Conditionally required | Text | When FAIL, required: specific action and responsible person | `Rotate the secret and clean history` |
| SKIP reason | Conditionally required | Text | Required when SKIP; skipping without reason is forbidden | `No build script` |
| Release verdict | Yes | Enum | ALLOW PUSH / BLOCK PUSH | `BLOCK PUSH` |
| Blocking reason | Conditionally required | Text | Required when BLOCK, listing P0 | `A2 historical secret hit` |

## 5. Filling Instructions

1. **Evidence mandatory**: Every verdict must have evidence; a PASS without evidence is invalid and should be changed to SKIP with a reason stated.
2. **Level correspondence**: FAIL must be marked with a level; P0 directly blocks release, P1 must be registered as a to-do, P2 goes into suggestions.
3. **Gate C threshold**: PASS only when P1 ≤ 3 and scheduled; exceeding requires downgrading or blocking.
4. **SKIP usage**: When a check cannot be performed, mark SKIP + reason; do not write PASS; re-check once conditions are met.
5. **Consistency**: Gate verdicts must be consistent with the P0/P1/P2 levels in [Review Dimension Matrix](./review-dimension-matrix.md) and the blocking rules in [Hard Rules](./hard-rules.md).
6. **Release**: Only when all three are green may `✅ ALLOW PUSH` be output; any FAIL outputs `⛔ BLOCK PUSH`, with blocking reasons listed.
7. **Delivery format**: Verdict results are output per [Audit Report Format](./audit-report-format.md); after passing, execute [Push and Release Specification](./push-and-release-specification.md).

Common mistakes:

| Wrong wording | Problem | Correction |
| --- | --- | --- |
| Verdict PASS but evidence empty | Verdict invalid | Add evidence or change to SKIP |
| ALLOW PUSH written while P0 not cleared | Violates hard rules | Change to BLOCK PUSH |
| SKIP without reason | Suspected missed check | Add a reason |
| Gate C has 5 P1 items but still PASS | Exceeds threshold | Downgrade or block |
| Verdict result written as text only, without a checklist | Not reviewable | Fill in item by item using the template |

## 6. Complete Example

```markdown
# Gate Verdict: markdown-lint-cli v1.0.0

Verdict date: 2026-11-20 ｜ Verifier: Wang Wu ｜ Repository: example/markdown-lint-cli

## Gate A · Security gate
| # | Check item | Verdict | Evidence | Level | Disposition |
| --- | --- | --- | --- | --- | --- |
| A1 | Workspace secrets | PASS | gitleaks detect: 0 findings | — | — |
| A2 | Historical secrets | PASS | gitleaks --log-opts=--all: 0 findings | — | — |
| A4 | LICENSE existence and type | PASS | LICENSE line 1 MIT | — | — |
| A5 | Large files and LFS | PASS | find -size +50M: none | — | — |

Conclusion: PASS, outstanding items: none

## Gate B · Quality gate
| # | Check item | Verdict | Evidence | Level | Disposition |
| --- | --- | --- | --- | --- | --- |
| B1 | Build passes | PASS | run #128 | — | — |
| B2 | Tests pass | PASS | 132/132 passed | — | — |
| B4 | Commit message conventions | PASS | git log --oneline all compliant | — | — |

Conclusion: PASS, outstanding items: none

## Overall Verdict
- A: PASS ｜ B: PASS ｜ C: PASS
- Release verdict: ✅ ALLOW PUSH
- Blocking reasons: none
```

## Related Files

- Verdict basis and failure levels: [Review Dimension Matrix](./review-dimension-matrix.md)
- Rules whose violation blocks: [Hard Rules](./hard-rules.md)
- Verdict result output format: [Audit Report Format](./audit-report-format.md)
- Executed after gate passage: [Push and Release Specification](./push-and-release-specification.md)
- Security gate evidence sources: [Security and Privacy Specification](./security-and-privacy-specification.md)
- Quality gate evidence sources: [Testing Specification](./testing-specification.md), [CI Workflow Specification](./ci-workflow-specification.md)
- Front-page gate verdict basis: [README Standard Template](./readme-standard-template.md), [Document Matrix](./document-matrix.md)
