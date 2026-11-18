# Architecture Design Document Specification

> What this file solves: Defines templates, fields, and writing guidelines for architecture documents and architecture decision records (ADRs), describing system boundaries, module responsibilities, quality attributes, and key trade-offs, and ensuring decisions are traceable.

## 1. Specification Clauses

1. The architecture document (`docs/architecture.md`) describes only structure and boundaries, not usage examples; see [Document Matrix](./document-matrix.md) for responsibility boundaries.
2. Every major technical decision must have a corresponding ADR; a decision without an ADR is considered undocumented.
3. ADR numbers are consecutive and permanently fixed; once adopted, history is not rewritten — status changes are recorded through a new ADR marked as "superseded".
4. Architecture descriptions must stay consistent with the code implementation; when code and documentation diverge, the code takes precedence and the documentation must be revised immediately.
5. Every architecture decision must trace back to one or more requirements; see [Requirements Traceability Matrix Specification](./requirements-traceability-matrix-specification.md).
6. Quality attributes must have verifiable measurement targets; writing only "high performance" or "high availability" is forbidden.

## 2. Architecture Document Template

```markdown
# Architecture Design: {{项目名称}}

Document version: {{v1.0}} ｜ Corresponding code version: {{tag}} ｜ Last verified date: {{YYYY-MM-DD}}

## System Context
- System responsibility: {{一句话说明系统边界内的责任}}
- External actors: {{用户、上游系统、下游系统}}
- Inputs and outputs: {{进入系统的请求与系统产出的结果}}
- Outside the boundary: {{明确不由本系统承担的职责}}

## Module Division
| Module | Unique responsibility | External interface | Dependent modules | Not responsible for |
| --- | --- | --- | --- | --- |
| {{模块名}} | {{仅一件事}} | {{接口名}} | {{模块名}} | {{明确排除}} |

## Key Data Flows
1. {{触发点}} → {{模块 A}}：{{传递的数据}}
2. {{模块 A}} → {{模块 B}}：{{转换与传递}}
3. {{模块 B}} → {{结果}}：{{最终产出}}

## Technology Selection
| Domain | Selection | Alternative | Decision basis | ADR |
| --- | --- | --- | --- | --- |
| {{语言 / 框架 / 存储}} | {{采用项}} | {{未采用项}} | {{取舍理由}} | {{ADR-000N}} |

## Quality Attributes
| Attribute | Target value | Verification method | Related ADR |
| --- | --- | --- | --- |
| Performance | {{P95 延迟 < X ms}} | {{压测方式}} | {{ADR-000N}} |
| Availability | {{月度可用性 ≥ X%}} | {{监控统计}} | {{ADR-000N}} |
| Security | {{敏感数据零明文落盘}} | {{审计方式}} | {{ADR-000N}} |
| Scalability | {{横向扩容至 N 节点无需改代码}} | {{扩容演练}} | {{ADR-000N}} |

## Constraints and Trade-offs
- Technical constraints: {{语言版本、平台、兼容性}}
- Abandoned solutions and reasons: {{方案 A：原因}}
- Known technical debt: {{债务项与偿还条件}}
```

## 3. ADR Template

```markdown
# ADR-{{四位序号}}: {{决策标题}}

- Status: {{提议 / 已采纳 / 已废弃 / 被 ADR-000N 替代}}
- Date: {{YYYY-MM-DD}}
- Decision maker: {{姓名}}
- Related requirements: {{REQ-001 / …}}

## Context
{{面临的客观问题与约束，须可验证，不写主观偏好}}

## Decision
{{采用的方案，一句话陈述，须明确到可执行的程度}}

## Alternatives
| Option | Advantages | Disadvantages | Reason not adopted |
| --- | --- | --- | --- |
| {{方案 A}} | | | |
| {{方案 B（采用）}} | | | — |

## Consequences
- Positive: {{获得的能力}}
- Negative: {{引入的成本或限制}}
- Follow-up tasks: {{需要跟进的事项}}

## Related Files
- {{架构文档中受影响的章节}}
- {{替代或被引用的 ADR}}
```

## 4. Field Definitions

### 4.1 Architecture Document Fields

| Field | Required | Type | Filling guidelines | Example |
| --- | --- | --- | --- | --- |
| Corresponding code version | Yes | tag | Consistent with the tag in [Version Management Specification](./version-management-specification.md) | `v1.2.0` |
| Last verified date | Yes | Date | Must be updated after every code change | `2026-11-18` |
| Module unique responsibility | Yes | Text | One thing per module | `Parse and validate Markdown rules` |
| Not responsible for | Yes | Text | State boundaries clearly to prevent responsibility drift | `Not responsible for text rewriting` |
| Technology selection.decision basis | Yes | Text | Must reference an ADR number | `See ADR-0002` |
| Quality attribute.target value | Yes | Metric | Includes unit and threshold, verifiable | `P95 < 150ms` |
| Known technical debt | No | List | State repayment trigger conditions | `Replace parser in v2` |

### 4.2 ADR Fields

| Field | Required | Type | Filling guidelines | Example |
| --- | --- | --- | --- | --- |
| Number | Yes | `ADR-NNNN` | Four-digit number, consecutive, permanently fixed | `ADR-0002` |
| Status | Yes | Enum | Proposed / Accepted / Deprecated / Superseded | `Accepted` |
| Related requirements | Yes | List | REQ numbers from the project proposal | `REQ-001` |
| Context | Yes | Text | State objective constraints; "I think" is forbidden | `Must be compatible with Node 18` |
| Decision | Yes | Text | One sentence, actionable | `Adopt remark as the parser` |
| Alternatives | Yes | Table | Must include at least 1 non-adopted option | See template |
| Rejection reason | Yes | Text | Must be given for every non-adopted option | See template |
| Consequences | Yes | List | Positive, negative, and follow-up tasks — all three present | See template |

## 5. Filling Instructions

1. **Module division**: If a row's "unique responsibility" contains two things joined by "and", split it into two modules.
2. **Data flows**: Number in chronological order, indicating the data being passed; writing only module names with arrows is forbidden.
3. **Quality attributes**: Each must have a target value, verification method, and ADR reference; missing any one is considered incomplete.
4. **ADR context**: Write the problem and constraints, not the decision itself; the decision appears only once, in the "Decision" section.
5. **Alternatives**: Even if there is only one option, state "considered self-implementation, not adopted due to high maintenance cost"; no alternatives is considered insufficient justification.
6. **Status changes**: Do not modify the original ADR body; create a new ADR and change the original status to "superseded by ADR-000N".
7. **Technical debt**: Must state repayment trigger conditions; listing only symptoms is forbidden.

Common mistakes:

| Wrong wording | Problem | Correction |
| --- | --- | --- |
| API usage examples in the architecture document | Overlaps with [API Documentation Specification](./api-documentation-specification.md) | Move to the API documentation; keep only interface names in the architecture |
| "The system needs high performance" | No threshold, not verifiable | Give a P95 latency target and stress test method |
| ADR with only a decision and no alternatives | Not justified | Add at least 1 non-adopted option and the reason |
| Modifying the body of an accepted ADR | History rewritten | Create a new ADR marking the supersession |
| Decision cannot be linked to a requirement | Traceability chain broken | Add the related REQ number |

## 6. Complete Example

```markdown
# ADR-0002: Adopt remark as the Markdown parsing layer

- Status: Accepted
- Date: 2026-11-18
- Decision maker: Li Si
- Related requirements: REQ-001, REQ-004

## Context
Need to support GFM and Chinese text node location, with runtime dependencies compatible with Node 18; the team's staffing cap for maintaining a parser is 0.5 person-month/quarter.

## Decision
Adopt the remark ecosystem as the sole Markdown parsing layer, with rules implemented as plugins.

## Alternatives
| Option | Advantages | Disadvantages | Reason not adopted |
| --- | --- | --- | --- |
| Custom parser | Full control | Requires long-term maintenance of boundary cases | Exceeds staffing limit |
| marked | Lightweight | Weak Chinese node location | Does not satisfy REQ-004 |

## Consequences
- Positive: GFM compatibility is maintained upstream; node location satisfies acceptance criteria.
- Negative: Plugin API changes require tracking upstream versions.
- Follow-up tasks: Lock the major version of remark in CI and subscribe to its release notifications.
```

## Related Files

- Responsibility boundaries and forbidden content: [Document Matrix](./document-matrix.md)
- Reverse tracing from decisions to requirements: [Requirements Traceability Matrix Specification](./requirements-traceability-matrix-specification.md)
- How to write engineering trade-offs externally: [Features and Engineering Trade-offs Writing Guide](./features-and-engineering-tradeoffs-guide.md)
- Interface design conventions: [API Design Specification](./api-design-specification.md)
- Data models and migrations: [Database Design Specification](./database-design-specification.md)
- Terminology consistency: [Glossary](./glossary.md)
