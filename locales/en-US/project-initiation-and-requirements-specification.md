# Project Initiation and Requirements Specification

> What this file solves: Defines the templates and fields for objective statements, requirements collection, and scope definition in the initiation phase, ensuring that a project has a clear, verifiable, and traceable basis from the very beginning.

## 1. Specification Provisions

1. The initiation document must answer six questions: what it is, why it is being done, to what extent it will be done, who it is not for, who is using it, and what constraints apply.
2. Requirements must be distinguished into three levels: "must / should / may"; see [General Writing Specification](./general-writing-specification.md) for terminology conventions.
3. Every requirement must be verifiable: provide acceptance conditions in Given/When/Then form, or provide a determinable measurement threshold.
4. Every requirement must have a stable ID and a source; unnumbered requirement items are prohibited.
5. When information is insufficient, mark "【To be confirmed: field name】"; do not guess to fill in; see [Information Collection and Templates](./information-collection-and-templates.md) for the rules.
6. The scope must state both included items and excluded items; empty non-goals are considered an undefined scope.
7. Scope changes must record the reason, impact, and decision maker, and enter the change log of the [Requirements Traceability Matrix Specification](./requirements-traceability-matrix-specification.md).

## 2. Initiation Document Template

```markdown
# Project Initiation Document: {{项目名称}}

Document Version: {{v0.1}} ｜ Status: {{草稿 / 评审中 / 已批准}} ｜ Decision Maker: {{姓名}} ｜ Date: {{YYYY-MM-DD}}

## One-Sentence Positioning
Provide {{核心能力}} for {{目标用户}}, solving {{当前痛点}}.
(≤60 characters; self-praising modifiers such as "powerful", "elegant", or "leading" are prohibited)

## Background and Motivation
- Current situation: {{当前如何运作}}
- Insufficiency of existing solutions: {{具体缺陷 1}}; {{具体缺陷 2}}
- Opportunity window: {{时机、技术或市场变化}}
- Basis for initiation: {{工单号 / 访谈记录 / 数据指标，须可溯源}}

## Goals and Non-Goals
| Type | Item | Verifiable Result |
| --- | --- | --- |
| Goal G1 | {{要达成的结果}} | {{可量化指标 + 阈值}} |
| Goal G2 | {{要达成的结果}} | {{可量化指标 + 阈值}} |
| Non-Goal N1 | {{明确不做的事}} | {{判定边界，说明为何排除}} |

## Success Criteria
| Metric | Baseline | Target Value | Verification Method | Verification Time |
| --- | --- | --- | --- | --- |
| {{指标名}} | {{当前值}} | {{目标值}} | {{如何测量}} | {{何时测量}} |

## Target Users
| User Role | Typical Scenario | Core Need | Current Alternative |
| --- | --- | --- | --- |
| {{角色}} | {{何时何地}} | {{要完成的任务}} | {{现用方案}} |

## Constraints
- Technical: {{语言、平台、兼容性等限制}}
- Time: {{截止日期或窗口}}
- Resources: {{人力、预算、基础设施}}
- Compliance: {{许可证、隐私、行业规范}}

## Scope
- Included: {{本期交付项}}
- Excluded: {{本期明确不交付项}}
- To be confirmed: {{【待确认：字段名】}}

## Decision Records
| Date | Decision | Decision Maker | Basis |
| --- | --- | --- | --- |
```

## 3. Requirement Item Template

```markdown
### REQ-{{三位序号}}: {{需求标题}}

- Source: {{工单号 / 访谈 / 竞品 / 推测}}
- Priority: {{必须 / 应当 / 可以}}
- Related Goals: {{G1 / G2 / …}}
- User story: As a {{角色}}, I want {{行为}}, so that {{价值}}
- Acceptance criteria:
  1. Given {{前置条件}}
     When {{操作}}
     Then {{预期结果}}
  2. Given {{边界或异常前置条件}}
     When {{操作}}
     Then {{预期结果}}
- Status: {{待确认 / 已确认 / 已实现 / 已验证 / 已废弃}}
- Traceability: {{见需求追踪矩阵中的需求 ID}}
```

## 4. Field Definitions

### 4.1 Initiation Document Fields

| Field | Required | Type | Filling Notes | Example |
| --- | --- | --- | --- | --- |
| Document version | Yes | Text | Semantic version or date version | `v0.1` |
| Status | Yes | Enum | Draft / Under review / Approved | `Under review` |
| Decision maker | Yes | Text | Person with final authority over scope and priorities | `Zhang San` |
| One-sentence positioning | Yes | Text | Target users + core capability + pain point, ≤60 characters | Provides front-end developers with… |
| Basis for initiation | Yes | Text | At least one traceable record; "team decision" is prohibited | `ISSUE-142` |
| Goals / Non-goals | Yes | Table | Each goal paired with a verifiable result; at least one non-goal | `G1: cold start <2s` |
| Success criteria | Yes | Table | Metrics must have a baseline, threshold, measurement method, and time | `Error rate <0.1%` |
| Constraints | Yes | List | All four categories must be filled; write "None" if absent | `Must be compatible with Node 18+` |
| To be confirmed | No | List | Use only the 【To be confirmed: field name】 format | `【To be confirmed: budget cap】` |

### 4.2 Requirement Item Fields

| Field | Required | Type | Filling Notes | Example |
| --- | --- | --- | --- | --- |
| ID | Yes | `REQ-NNN` | Three-digit sequence, continuous, not reused, not reordered | `REQ-007` |
| Source | Yes | Text | Traceable to a specific record | `User interview #3` |
| Priority | Yes | Enum | Must / Should / May | `Must` |
| Related goals | Yes | List | Corresponds to the G IDs in the initiation document | `G1` |
| User story | Yes | Text | Contains all three elements: role + action + value | As a… I want… so that… |
| Acceptance criteria | Yes | List | At least 1 set of Given/When/Then, including a boundary or exception | See template |
| Status | Yes | Enum | One of five states; only advances and never reverts | `Confirmed` |

## 5. Filling Instructions

1. **One-sentence positioning**: Write in the three-part form "for whom + what is provided + what problem is solved"; if the sentence does not hold after removing the modifiers, substantive information is missing.
2. **Success criteria**: Each must have both a baseline and a threshold. "Improve performance" and "better experience" are judged unacceptable and must be rewritten as "P95 startup time reduced from 3s to <1.5s".
3. **Non-goals**: State the explicitly excluded scope and judgment boundaries rather than "we'll see later"; if there is no non-empty non-goal, the scope is considered undefined.
4. **Requirement IDs**: Permanently fixed once assigned; when a requirement is discarded, its status changes to "Discarded" and the ID must not be reclaimed or reused.
5. **Acceptance criteria**: Must cover the normal path and at least one boundary or exception path; conditions that cannot be objectively judged (such as "the interface is beautiful") must be converted into verifiable metrics or check items.
6. **Items to be confirmed**: Initiation may contain items to be confirmed, but they must be listed in full with a designated confirmer; they must be cleared before development begins.

Common mistakes:

| Incorrect Writing | Problem | Correction |
| --- | --- | --- |
| "Build a useful tool" | No target users, no verifiable results | Add user roles and threshold metrics |
| Writing "None" for non-goals | Scope undefined, prone to creep | List the items explicitly excluded this time |
| Requirements without IDs, described directly in text | Cannot be traced or referenced | Assign `REQ-NNN` and reference globally |
| Writing "function works normally" for acceptance criteria | Not determinable | Break into Given/When/Then |
| Treating speculation as established requirements | Source not traceable | Mark the source as "speculation" and convert to to-be-confirmed |

## 6. Complete Example

```markdown
# Project Initiation Document: markdown-lint-cli

Document Version: v0.1 ｜ Status: Under review ｜ Decision Maker: Li Si ｜ Date: 2026-11-18

## One-Sentence Positioning
Provide a command-line Markdown specification checking tool for Chinese technical writers, solving the problem of inconsistent documentation styles across multiple repositories with no automated validation.

## Background and Motivation
- Current situation: READMEs in 12 repositories are hand-written by individual maintainers, with inconsistent styles.
- Insufficiency of existing solutions: General English lint tools do not support Chinese-English spacing rules; manual review takes an average of 25 minutes per document.
- Opportunity window: The team is unifying its open source front pages and needs to establish the specification in one pass.
- Basis for initiation: ISSUE-142, minutes of the 2026-11-10 documentation review.

## Goals and Non-Goals
| Type | Item | Verifiable Result |
| --- | --- | --- |
| Goal G1 | Automatically check 8 categories of formatting issues | Detection rate ≥95% on 50 sample documents |
| Goal G2 | Single check time is controlled | Checking a 1000-line document <2s |
| Non-Goal N1 | No document content polishing | Only outputs rule-match locations, does not rewrite text |

## Success Criteria
| Metric | Baseline | Target Value | Verification Method | Verification Time |
| --- | --- | --- | --- | --- |
| Manual review time | 25 minutes/document | <5 minutes/document | Controlled experiment with 5 maintainers | Before v1.0 release |

### REQ-001: Check spacing in mixed Chinese-English text
- Source: ISSUE-142
- Priority: Must
- Related Goals: G1
- User story: As a documentation maintainer, I want missing spaces between Chinese and English automatically marked, so that layout can be unified.
- Acceptance criteria:
  1. Given the document contains "使用Node.js开发"
     When the check is executed
     Then output the line number and a "missing space between Chinese and English" message
  2. Given the document already has a space there
     When the check is executed
     Then do not output a rule match
- Status: Confirmed
```

## Related Files

- Traceability from requirements to design, testing, and release: [Requirements Traceability Matrix Specification](./requirements-traceability-matrix-specification.md)
- Information fields and missing-item markers: [Information Collection and Templates](./information-collection-and-templates.md)
- Phase division and entry conditions: [Execution Process](./execution-process.md)
- Naming is performed after the initiation conclusion is determined: [Project Naming Specification](./project-naming-specification.md)
- External explanation of scope changes: [Changelog Specification](./changelog-specification.md)
