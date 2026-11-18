# Deployment and Rollback Specification

> What this file solves: Defines deployment checklists, change tickets, and rollback plan templates, fields, and execution standards, ensuring controllable go-live, traceable status, and rapid recovery from failures.

## 1. Specification Clauses

1. Before deployment, must pass CI, code review, and quality gates (see [Quality Gates](./quality-gate.md)).
2. Deployment is based on a tagged release version, not an untagged commit (see [Version Management Specification](./version-management-specification.md)).
3. Environment configuration is separated from code; sensitive configuration is injected through configuration management and not stored in the repository (see [Security and Privacy Specification](./security-and-privacy-specification.md)).
4. Database schema changes are executed through migration scripts and must satisfy forward compatibility (see [Database Design Specification](./database-design-specification.md)).
5. Every deployment must record the version number, time, operator, and change content; a deployment without records is considered non-compliant.
6. Every version must have a rollback plan prepared in advance; go-live is not allowed without a prepared rollback plan.
7. After deployment, health checks and smoke verification must be executed; the release is complete only when both pass.

## 2. Deployment Checklist Template

```markdown
# Deployment Checklist: {{项目名称}} {{版本号}}

Version: {{vX.Y.Z}} ｜ Tag: {{vX.Y.Z}} ｜ Target Environment: {{预发布 / 生产}} ｜ Planned Time: {{YYYY-MM-DD HH:MM}}

## Pre-checks
- [ ] CI all green, workflow run URL: {{URL}}
- [ ] Code review passed, approver: {{姓名}}
- [ ] Quality gates A/B/C all PASS
- [ ] Changelog and Release Notes are ready
- [ ] Rollback plan has been reviewed, see end of this section
- [ ] Database migration script has been reviewed and is forward compatible
- [ ] Configuration change list confirmed (injected items not stored in repository)

## Change Content
| Change Item | Type | Scope of Impact | Related Requirement | Verification Method |
| --- | --- | --- | --- | --- |
| {{功能 / 配置 / 数据迁移}} | {{新增 / 修改 / 移除}} | {{受影响模块}} | {{REQ-NNN}} | {{如何确认}} |

## Execution Steps
1. {{步骤，含具体命令或平台操作}}
2. {{灰度比例与观察时长}}
3. {{全量放量条件}}

## Health Check and Smoke Test
| Check Item | Judgment Condition | Execution Method | Result |
| --- | --- | --- | --- |
| Service alive | {{HTTP 200}} | {{命令}} | {{通过 / 未通过}} |
| Critical path | {{主流程完成}} | {{命令}} | {{通过 / 未通过}} |
| Error rate | {{< X%}} | {{监控面板}} | {{通过 / 未通过}} |

## Deployment Record
| Item | Value |
| --- | --- |
| Actual deployment time | {{YYYY-MM-DD HH:MM}} |
| Operator | {{姓名}} |
| Approver | {{姓名}} |
| Actual version number | {{vX.Y.Z}} |
| Result | {{成功 / 回滚 / 中止}} |

## Rollback Plan
- Rollback target version: {{vX.Y.Z}}
- Trigger condition: {{错误率 > X% 持续 N 分钟 / 冒烟失败 / 数据异常}}
- Decision maker: {{姓名}}
- Rollback steps: {{具体命令或操作}}
- Data compatibility: {{是否需要数据回滚；如果需要，说明方式}}
```

## 3. Deployment Record Template

```markdown
## {{YYYY-MM-DD}} {{vX.Y.Z}} → {{环境}}

- Version number: {{vX.Y.Z}}
- Tag: {{vX.Y.Z}}
- Time: {{HH:MM}}
- Operator / Approver: {{姓名 / 姓名}}
- Change summary: {{一句话}}
- Health check: {{通过 / 未通过}}
- Result: {{成功 / 回滚}}
- Related release: {{Release Notes URL}}
- Remarks: {{异常与处理记录；无则写「无」}}
```

## 4. Field Definitions

| Field | Required | Type | Filling Guidance | Example |
| --- | --- | --- | --- | --- |
| Tag | Yes | Text | Exactly consistent with the tag in [Version Management Specification](./version-management-specification.md) | `v1.2.0` |
| Target environment | Yes | Enum | Staging / Production; configurations must not be mixed | `Production` |
| Change Item.Type | Yes | Enum | Add / Modify / Remove | `Modify` |
| Related requirement | Yes | List | REQ number; write "None" if no requirement change | `REQ-007` |
| Canary ratio | No | Percentage | Required during gradual rollout | `10% → 50% → 100%` |
| Judgment condition | Yes | Threshold | Observable and determinable | `HTTP 200` |
| Actual version number | Yes | Text | If different from the planned version, explain the reason | `v1.2.1` |
| Rollback trigger condition | Yes | Threshold + Duration | Expressions like "feels abnormal" are prohibited | `Error rate >1% for 5 minutes` |
| Data compatibility | Yes | Text | Clearly state whether data rollback is needed | `No data rollback needed` |

## 5. Filling Instructions

1. **Pre-checks**: Check item by item; checking the whole block at once is prohibited; if any item is incomplete, abort the deployment.
2. **Change content**: Each item must be associated with a REQ number; purely operational changes with no requirement association write "None" and explain the basis for the change.
3. **Health check**: Must be automatically determinable conditions; "the service looks normal" is unacceptable.
4. **Rollback trigger condition**: Must give both a threshold and a duration, to avoid false triggers from transient jitter.
5. **Canary rollout**: After each stage of rollout, observe for the specified duration and record the observation conclusion before moving to the next stage.
6. **Deployment record**: Append by time, do not overwrite history; consistent with the version numbers in push, tag, and Release Notes.
7. **Rollback execution**: For code rollback, use `git revert` to generate a reverse commit; do not force-push to published history (see [Push and Release Specification](./push-and-release-specification.md)).

Common mistakes:

| Incorrect Wording | Problem | Correction |
| --- | --- | --- |
| Deploy an untagged commit | Version cannot be reproduced | Tag before deploying |
| Rollback plan written as "roll back if there is a problem" | No trigger condition or steps | Add threshold, decision maker, and steps |
| Database changes incompatible with the old version | Data unavailable after rollback | Use the expand-migrate-contract three-step method |
| Deployment record written after the fact | Status is untrustworthy | Record at the time of deployment |
| Health check only tests the homepage | Critical path not verified | Add smoke test cases for the main flow |

## 6. Complete Example

```markdown
# Deployment Checklist: markdown-lint-cli v1.0.0

Version: v1.0.0 ｜ Tag: v1.0.0 ｜ Target Environment: Production ｜ Planned Time: 2026-11-20 10:00

## Pre-checks
- [x] CI all green: https://github.com/example/markdown-lint-cli/actions/runs/123
- [x] Code review passed, approver: Li Si
- [x] Quality gates A/B/C all PASS
- [x] Changelog and Release Notes are ready
- [x] Rollback plan has been reviewed
- [x] No database migration
- [x] Configuration change list confirmed: None

## Change Content
| Change Item | Type | Scope of Impact | Related Requirement | Verification Method |
| --- | --- | --- | --- | --- |
| CJK/English spacing rule | Add | Rule engine | REQ-001 | Execute TC-001 |
| CLI report output | Modify | Report module | REQ-007 | Execute TC-012 |

## Execution Steps
1. Pull the v1.0.0 tag and verify the checksum
2. Canary 10%, observe for 10 minutes
3. Ramp up to 100% after the error rate is <0.1%

## Health Check and Smoke Test
| Check Item | Judgment Condition | Execution Method | Result |
| --- | --- | --- | --- |
| Service alive | HTTP 200 | curl /healthz | Pass |
| Critical path | 50 documents checked | shell script | Pass |
| Error rate | <0.1% | Monitoring dashboard | Pass |

## Rollback Plan
- Rollback target version: v0.9.3
- Trigger condition: Error rate >1% for 5 minutes
- Decision maker: Li Si
- Rollback steps: Switch the deployment tag to v0.9.3 and run the data compatibility check
- Data compatibility: No database changes, no data rollback needed
```

## Related Files

- Version and tag rules: [Version Management Specification](./version-management-specification.md)
- Push actions and incident handling: [Push and Release Specification](./push-and-release-specification.md)
- Incident classification and retrospective: [Incident Response Specification](./incident-response-specification.md)
- Metrics and alerting support: [Observability Specification](./observability-specification.md)
- Migration scripts and compatibility: [Database Design Specification](./database-design-specification.md)
- Sensitive configuration injection: [Security and Privacy Specification](./security-and-privacy-specification.md)
