# Incident Response Specification

> What this file solves: Defines incident report templates, timeline records, communication templates, and postmortem fields, ensuring faults are controllable, information is synchronized, and experience is retained.

## 1. Specification Clauses

1. Incident classification: P0 — core functionality unavailable or data corruption; P1 — severe functionality impaired affecting most users; P2 — localized issue with limited impact.
2. Response process: Detect → Classify → Stop the bleeding → Locate → Fix → Announce; stopping the bleeding takes priority over locating the root cause.
3. Every P0/P1 incident must be postmortemed, recording the timeline, root cause, impact, handling, and improvement items.
4. Improvement items must be tracked to closure via the [Roadmap Specification](./roadmap-specification.md).
5. Postmortems focus on system improvement and do not assign personal blame.
6. Key leakage: immediately rotate → purge history → announce; merely making a deletion commit is not sufficient (see [Security and Privacy Specification](./security-and-privacy-specification.md)).
7. Accidentally pushing large files: LFS migration or history rewrite (see [Push and Release Specification](./push-and-release-specification.md)).

## 2. Incident Report Template

```markdown
# Incident Report: {{INC-YYYYMMDD-NN}}

- Incident Level: {{P0 / P1 / P2}}
- Detected At: {{YYYY-MM-DD HH:MM}}
- Recovered At: {{YYYY-MM-DD HH:MM}}
- Duration: {{N 分钟}}
- Incident Commander: {{姓名}}
- Current Status: {{处理中 / 已恢复 / 已复盘}}

## Impact Scope
| Dimension | Description |
| --- | --- |
| Affected Functionality | {{具体功能}} |
| Affected User Ratio | {{估算值与依据}} |
| Data Impact | {{无 / 描述}} |
| Business Impact | {{可量化的损失或阻塞}} |

## Timeline
| Time | Event | Source | Operator |
| --- | --- | --- | --- |
| {{HH:MM}} | Alert triggered | {{监控面板}} | {{姓名}} |
| {{HH:MM}} | Classified as P1 | {{判断依据}} | {{姓名}} |
| {{HH:MM}} | Rollback executed | {{命令 / 平台}} | {{姓名}} |
| {{HH:MM}} | Service recovered | {{验证方式}} | {{姓名}} |

## Root Cause
- Direct Cause: {{触发故障的具体事件}}
- Root Cause: {{为何未被预防或及时检测}}
- Amplifying Factors: {{扩大影响的因素}}

## Handling and Verification
1. {{止血措施}}
2. {{修复措施}}
3. {{验证方式与结果}}

## Improvement Items
| No. | Action | Owner | Due Date | Verification Method | Status |
| --- | --- | --- | --- | --- | --- |
| {{A-NN}} | {{具体动作}} | {{姓名}} | {{YYYY-MM-DD}} | {{可判定阈值}} | {{待开始}} |
```

## 3. Communication Templates

```markdown
## Incident Notification (Initial)

- Time: {{YYYY-MM-DD HH:MM}}
- Level: {{P0 / P1 / P2}}
- Symptom: {{用户可感知的现象，不写内部细节}}
- Impact: {{受影响范围}}
- Current Actions: {{正在做什么}}
- Next Update At: {{HH:MM}}

## Incident Notification (Recovery)

- Recovery Time: {{HH:MM}}
- Recovery Confirmation: {{验证方式与结果}}
- Remaining Impact: {{无 / 描述}}
- Follow-up: {{复盘安排}}
```

## 4. Field Definitions

| Field | Required | Type | Filling Guidelines | Example |
| --- | --- | --- | --- | --- |
| Incident ID | Yes | `INC-YYYYMMDD-NN` | Daily sequence, continuous and never reused | `INC-20261118-01` |
| Incident Level | Yes | Enum | P0 / P1 / P2 | `P1` |
| Duration | Yes | Duration | Minutes from detection to recovery | `42 minutes` |
| Incident Commander | Yes | Text | Single person, responsible for decisions and synchronization | `Li Si` |
| Affected User Ratio | Yes | Text | Estimation basis must be given | `~8%, based on error log counts` |
| Timeline | Yes | Table | Each node includes time and source | See template |
| Root Cause | Yes | Text | Distinguish direct cause from root cause | `No rollback drills` |
| Improvement Item Verification Method | Yes | Text | Determinable, with threshold | `Next drill rollback <5 minutes` |
| Next Update At | Yes | Time point | Required while in progress; "update anytime" is prohibited | `18:30` |

## 5. Filling Instructions

1. **Classification**: Classify by impact scope and severity; when uncertain, classify higher and adjust later while recording the reason.
2. **Stop the Bleeding First**: Restore service first (rollback, degrade, rate limit), then locate the root cause; locating must not delay stopping the bleeding.
3. **Timeline**: Record in chronological order; sources must be verifiable (alert ID, command, log snippet); writing from memory afterward is prohibited.
4. **Root Cause**: The direct cause is the triggering event; the root cause is a systemic deficiency; both must be filled in.
5. **Communication**: The initial notification must give the next update time; the recovery notification must state the verification method and remaining impact.
6. **Improvement Items**: At most three, tracked in the roadmap; improvement items without an owner must not enter the report.
7. **Postmortem**: Focus on system and process improvement, do not evaluate individuals; do not assign blame or use phrases like "someone was careless."
8. **Special Incidents**: Key leakage is handled per H12; accidentally pushing large files is handled via LFS migration; both require separate records.

Common Mistakes:

| Incorrect Practice | Problem | Correction |
| --- | --- | --- |
| Locating root cause before stopping the bleeding | Prolongs the outage | Roll back to restore service first |
| Writing timeline from memory afterward | Facts are untrustworthy | Record immediately while handling |
| Root cause written as "someone was careless" | Blames an individual, no improvement value | Drill down to the process or tooling level |
| Notification says "fix as soon as possible" | No next update time | Give a specific time point |
| Improvement item has no verification method | Closure cannot be determined | Add threshold and check timing |

## 6. Complete Example

```markdown
# Incident Report: INC-20261118-01

- Incident Level: P1
- Detected At: 2026-11-18 10:12
- Recovered At: 2026-11-18 10:54
- Duration: 42 minutes
- Incident Commander: Li Si
- Current Status: Postmortemed

## Impact Scope
| Dimension | Description |
| --- | --- |
| Affected Functionality | Rule check API returning 5xx |
| Affected User Ratio | About 8%, based on 5xx log counts |
| Data Impact | None |
| Business Impact | Unable to submit check tasks for 42 minutes |

## Root Cause
- Direct Cause: The rule plugin load path was overwritten by new configuration, causing startup failure.
- Root Cause: Configuration changes were not included in pre-release verification.

## Improvement Items
| No. | Action | Owner | Due Date | Verification Method | Status |
| --- | --- | --- | --- | --- | --- |
| A-01 | Add configuration changes to the pre-release checklist | Wang Wu | 2026-11-25 | Next 5 changes all include check records | Not Started |
```

## Related Files

- Alert sources and response guidelines: [Observability Specification](./observability-specification.md)
- Rollback operations: [Deployment and Rollback Specification](./deployment-and-rollback-specification.md)
- Key and sensitive information handling: [Security and Privacy Specification](./security-and-privacy-specification.md)
- Large files and history rewrite: [Push and Release Specification](./push-and-release-specification.md)
- Improvement item tracking: [Roadmap Specification](./roadmap-specification.md)
- Process improvement postmortems: [Iteration Retrospective Specification](./iteration-retrospective-specification.md)
- Alert evaluation criteria: [Quality Metrics Specification](./quality-metrics-specification.md)
