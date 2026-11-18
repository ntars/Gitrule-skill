# Iteration Retrospective Specification

> What this file solves: Defines the retrospective template, fields, and improvement-item tracking mechanism after an iteration ends, ensuring problems are distilled into actionable and verifiable actions for the next iteration and mistakes are not repeated.

## 1. Specification Clauses

1. A retrospective must be completed within five working days after each iteration ends; delays require an explanation.
2. Retrospectives must be based on factual data; substituting impressions for measurement is prohibited; data sources are covered in the [Quality Metrics Specification](./quality-metrics-specification.md).
3. Every problem must have a clear root cause, improvement action, owner, and verification method; items without an owner or verification method must not enter the action list.
4. The maximum number of improvement actions is three, ranked by impact; more than three must be merged or downgraded to suggestions.
5. The previous iteration's improvement actions must be verified item by item in this iteration's retrospective; incomplete ones require an explanation and rescheduling.
6. Retrospective documents record only process improvements, not version change content, which is covered in the [Changelog Specification](./changelog-specification.md).

## 2. Retrospective Document Template

```markdown
# Iteration Retrospective: {{项目名称}} {{迭代标识}}

Iteration Period: {{YYYY-MM-DD ~ YYYY-MM-DD}} ｜ Facilitator: {{姓名}} ｜ Participants: {{姓名列表}} ｜ Retrospective Date: {{YYYY-MM-DD}}

## 1. Goal Review
| Iteration Goal | Source | Achievement | Basis |
| --- | --- | --- | --- |
| {{目标描述}} | {{路线图 / 立项书}} | {{达成 / 未达成 / 部分达成}} | {{数据或交付物}} |

## 2. Data Snapshot
| Metric | Previous | Current | Change | Target |
| --- | --- | --- | --- | --- |
| Requirements Delivered | | | | |
| Escaped Defects | | | | |
| Average CI Duration | | | | |
| Requirement Coverage | | | | |
| Incident Count | | | | |

## 3. Fact List
- Went Well: {{基于数据的事实，如「本轮 CI 全绿率 98%」}}
- Obstacles: {{基于数据的障碍，如「集成环境等待平均 4 小时」}}
- Surprises: {{未预见的事件及其影响}}

## 4. Problems and Root Causes
| No. | Problem | Evidence | Root Cause | Impact |
| --- | --- | --- | --- | --- |
| R-01 | {{问题描述}} | {{数据 / 事件}} | {{根因，非表象}} | {{造成的影响}} |

## 5. Improvement Actions
| No. | Related Problem | Action | Owner | Due Date | Verification | Status |
| --- | --- | --- | --- | --- | --- | --- |
| A-01 | R-01 | {{具体动作}} | {{姓名}} | {{YYYY-MM-DD}} | {{如何验证生效}} | Not Started |

## 6. Previous Action Verification
| No. | Action | Previous Status | Current Conclusion | Follow-up |
| --- | --- | --- | --- | --- |
| A-00 | {{动作}} | In Progress | {{完成 / 未完成 / 放弃}} | {{继续 / 重排 / 关闭并说明}} |

## 7. Consensus and Carryover
- This Iteration's Consensus: {{需要长期遵守的约定}}
- Carryover Issues: {{不在本轮处理的问题及原因}}
```

## 3. Improvement Action Entry Template

```markdown
### A-{{两位序号}}: {{动作标题}}

- Related Problem: {{R-NN}}
- Action: {{一个可执行的动作，含具体对象}}
- Owner: {{姓名，唯一}}
- Due Date: {{YYYY-MM-DD}}
- Verification: {{可判定的检查和阈值}}
- Expected Effect: {{用指标描述}}
- Status: Not Started / In Progress / Completed / Abandoned
```

## 4. Field Definitions

| Field | Required | Type | Filling Guidelines | Example |
| --- | --- | --- | --- | --- |
| Iteration ID | Yes | Text | Consistent with the phase number in the [Roadmap Specification](./roadmap-specification.md) | `Sprint-12` |
| Achievement | Yes | Enum | Achieved / Not Achieved / Partially Achieved | `Partially Achieved` |
| Basis | Yes | Text | Data or deliverable link; must not be empty | `REQ-001 released` |
| Data Snapshot | Yes | Table | At least 3 metrics, with previous and current values | `Escaped defects 2 → 0` |
| Root Cause | Yes | Text | Distinguish symptom from root cause; use "because" to link verifiable facts | `Because the environment was not included in CI` |
| Action | Yes | Text | Single action, with object and behavior | `Include the integration environment in CI` |
| Owner | Yes | Text | Single person; writing "team" is prohibited | `Wang Wu` |
| Verification | Yes | Text | Determinable, with check timing | `Next CI duration <10 minutes` |
| Status | Yes | Enum | One of four states | `Completed` |

## 5. Filling Instructions

1. **Goal Review**: Use the original goals from the project charter or roadmap as the baseline; do not rewrite goals to match results.
2. **Data Snapshot**: Must use the same measurement basis as the previous iteration; when the basis changes, mark "basis changed" and state both the old and new definitions.
3. **Fact List**: Only verifiable facts; subjective judgments such as "poor communication" must be converted into concrete events and times.
4. **Root Cause**: Keep drilling down to an actionable level; "because testing was insufficient" is still a symptom; "because requirements were not linked to test cases" is the root cause.
5. **Number of Actions**: At most three; if there are more than three problems, rank by impact and put the rest in "Carryover Issues".
6. **Verification**: Must state the check timing and the determination threshold; "observe later" is unacceptable.
7. **Previous Verification**: Give a conclusion for each item; do not skip whole sections; abandonment must state the reason.

Common Mistakes:

| Incorrect Practice | Problem | Correction |
| --- | --- | --- |
| "Everyone should care more about quality" | No action, no owner | Replace with a concrete action and an owner |
| Root cause written as "carelessness" | Not verifiable or improvable | Drill down to the process or tooling level |
| 8 improvement actions listed | Cannot be implemented | Rank by impact and take the top three |
| Verification written as "see the effect" | Not determinable | Add a threshold and check timing |
| Previous actions not verified | Improvement loop broken | Fill in this iteration's conclusion for each item |

## 6. Complete Example

```markdown
# Iteration Retrospective: markdown-lint-cli Sprint-12

Iteration Period: 2026-11-10 ~ 2026-11-21 ｜ Facilitator: Li Si ｜ Participants: Wang Wu, Zhao Liu ｜ Retrospective Date: 2026-11-23

## 1. Goal Review
| Iteration Goal | Source | Achievement | Basis |
| --- | --- | --- | --- |
| Release v1.0.0 core rules | Roadmap S12 | Achieved | tag v1.0.0 released |
| Requirement coverage 100% | Charter G1 | Partially Achieved | 13/14 mandatory requirements closed |

## 2. Data Snapshot
| Metric | Previous | Current | Change | Target |
| --- | --- | --- | --- | --- |
| Requirements Delivered | 6 | 14 | +8 | 14 |
| Escaped Defects | 2 | 1 | -1 | 0 |
| Requirement Coverage | 85% | 92.9% | +7.9% | 100% |

## 4. Problems and Root Causes
| No. | Problem | Evidence | Root Cause | Impact |
| --- | --- | --- | --- | --- |
| R-01 | REQ-003 has no test cases | TC field in the traceability matrix is "to be filled" | Because traceability matrix completeness was not enforced during requirement review | Requirement coverage target missed |

## 5. Improvement Actions
| No. | Related Problem | Action | Owner | Due Date | Verification | Status |
| --- | --- | --- | --- | --- | --- | --- |
| A-01 | R-01 | Add a "traceability matrix filled" check item to the requirement review checklist | Wang Wu | 2026-11-27 | Next 5 review records all include this check | Not Started |
```

## Related Files

- Traceability data from requirements to release: [Requirement Traceability Matrix Specification](./requirements-traceability-matrix-specification.md)
- Metric definitions and measurement: [Quality Metrics Specification](./quality-metrics-specification.md)
- Sources of phases and goals: [Roadmap Specification](./roadmap-specification.md)
- Version change content: [Changelog Specification](./changelog-specification.md)
- Incident postmortems and improvement: [Incident Response Specification](./incident-response-specification.md)
- Tracking execution phases: [Execution Process](./execution-process.md)
