# Observability Specification

> What this file solves: Defines log fields, SLI/SLO targets, alert rules, and alert response card templates, ensuring system state is visible, faults are locatable, and alerts are actionable.

## 1. Specification Clauses

1. Observability consists of three pillars: logs, metrics, and distributed tracing; all three must be correlated via a unified request identifier.
2. Logs must be structured and include a timestamp, level, and request identifier; recording sensitive information is prohibited, and masking rules are covered in [Security and Privacy Specification](./security-and-privacy-specification.md).
3. Every critical service must define SLIs and SLOs, along with the calculation method and measurement window.
4. Alert rules must have explicit thresholds, durations, and owners; alerts without response guidelines must not go live.
5. Once triggered, an alert must be linkable to the classification and handling process in the [Incident Response Specification](./incident-response-specification.md).
6. Metric definitions must be unified with the [Quality Metrics Specification](./quality-metrics-specification.md); the same name must not have different meanings.

## 2. The Three Pillars and Fields

| Pillar | Required Fields | Requirement | Correlation Key |
| --- | --- | --- | --- |
| Logs | timestamp, level, request identifier, message, context | Structured output; levels limited to DEBUG/INFO/WARN/ERROR | `trace_id` |
| Metrics | metric name, labels, value, collection time | Explicit definition and target value | `service` |
| Distributed Tracing | trace identifier, span identifier, parent span, duration, status | Cross-service calls can be chained | `trace_id` |

## 3. Log Field Template

```markdown
| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| timestamp | ISO 8601 | Yes | UTC time with timezone | 2026-11-18T10:00:00Z |
| level | enum | Yes | DEBUG / INFO / WARN / ERROR | ERROR |
| trace_id | string | Yes | Unique identifier across the entire call chain | 4bf92f3577b34da6 |
| service | string | Yes | Service name | lint-api |
| message | string | Yes | Brief description without sensitive information | rule load failed |
| context | object | No | Context fields that aid localization | {"rule":"spacing"} |
```

## 4. SLI/SLO Definition Template

```markdown
# SLO Definition: {{服务名}}

Version: {{v1.0}} ｜ Owner: {{姓名}} ｜ Review Cycle: {{每季度}}

## Service Boundaries
- Service Responsibility: {{一句话}}
- Dependent Services: {{上游 / 下游}}
- Key User Operations: {{列出 2–5 项}}

## SLI Definition
| SLI | Definition | Calculation Method | Data Source |
| --- | --- | --- | --- |
| Availability | Successful requests / total requests | HTTP status <500 counts as success | {{监控面板}} |
| Latency | Request latency distribution | P95 percentile | {{监控面板}} |
| Error Rate | Failed requests / total requests | 5xx count | {{监控面板}} |

## SLO Targets
| SLI | Target | Measurement Window | Current Value | Compliance Status |
| --- | --- | --- | --- | --- |
| Availability | ≥99.9% | Rolling 30 days | {{值}} | {{达标 / 未达标}} |
| Latency P95 | <300ms | Rolling 7 days | {{值}} | {{达标 / 未达标}} |
| Error Rate | <0.1% | Rolling 24 hours | {{值}} | {{达标 / 未达标}} |

## Error Budget
- Calculation: {{1 - SLO 目标值，按统计窗口换算}}
- Burn Alerts: {{消耗达 50% / 75% / 90% 时分别通知}}
- Exhaustion Policy: {{冻结非关键发布，优先修复稳定性}}
```

## 5. Alert Rule Template

```markdown
### ALERT-{{三位序号}}: {{告警名称}}

- Related SLI: {{可用性 / 延迟 / 错误率}}
- Expression: {{可执行的查询表达式}}
- Threshold: {{数值 + 单位}}
- Duration: {{N 分钟}}
- Severity: {{P0 / P1 / P2}}
- Owner: {{姓名 / 值班组}}
- Trigger Example: {{给出一个会触发的样例数据}}
- Silence Condition: {{何时允许静默，须有到期时间}}

Response Guidelines:
1. {{第一步：确认现象的数据源与命令}}
2. {{第二步：常见原因与对应处理}}
3. {{第三步：升级条件与升级对象}}
- Related Incident Level: {{见事故响应规范的分级表}}
```

## 6. Field Definitions

| Field | Required | Type | Filling Guidelines | Example |
| --- | --- | --- | --- | --- |
| SLI Definition | Yes | Text | Must be a computable ratio or percentile | Successful requests / total requests |
| Calculation Method | Yes | Text | Specify inclusion and exclusion criteria | Exclude health check requests |
| SLO Target | Yes | Threshold | Value + unit + percentage | `≥99.9%` |
| Measurement Window | Yes | Duration | Rolling window; vague calendar-month expressions are prohibited | `Rolling 30 days` |
| Error Budget | Yes | Number | Derived from the SLO target | `43 minutes of downtime allowed per month` |
| Alert Expression | Yes | Query | Can be pasted and executed directly | `rate(http_5xx[5m]) > 0.01` |
| Duration | Yes | Duration | Prevents false positives from transient jitter | `5 minutes` |
| Response Guidelines | Yes | List | At least 3 steps, including escalation criteria | See template |
| Silence Condition | Yes | Text | Must have an expiration time | `Within release window, max 30 minutes` |

## 7. Filling Instructions

1. **SLI Selection**: Choose 2–5 items from user-perceivable dimensions; do not replace user SLIs with internal resource metrics such as CPU or memory.
2. **Unified Definitions**: A metric with the same name must use the same calculation method across logs, monitoring dashboards, and alert expressions.
3. **Target Setting**: SLO targets should be based on current measurements and business tolerance; directly applying "four nines" without justification is prohibited.
4. **Error Budget**: The conversion result and tiered burn actions must be stated; when the budget is exhausted, non-critical releases are frozen.
5. **Actionable Alerts**: Every alert must answer three questions: "what to look at, how to investigate, and when to escalate"; missing any one question means it must not go live.
6. **Alert Fatigue Management**: Alerts that have produced no effective response for 30 consecutive days should be downgraded or removed, with the reason stated.
7. **Masking**: If log context fields may contain keys, tokens, or personal privacy, they must be masked before output.

Common Mistakes:

| Incorrect Practice | Problem | Correction |
| --- | --- | --- |
| Using CPU utilization as SLI | Not user-perceivable | Use availability, latency, and error rate instead |
| Alert only says "service anomaly" | No threshold, no guidelines | Add expression, threshold, and response steps |
| Logging full request headers | Privacy and secret leakage risk | Whitelist only the necessary fields |
| Alert has no silence expiration | Long-term silence causes missed reports | Set a maximum silence duration |
| SLO has no measurement window | Target cannot be evaluated | Add a rolling window |

## 8. Complete Example

```markdown
# SLO Definition: lint-api

Version: v1.0 ｜ Owner: Wang Wu ｜ Review Cycle: Quarterly

## SLI Definition
| SLI | Definition | Calculation Method | Data Source |
| --- | --- | --- | --- |
| Availability | Successful requests / total requests | Status <500, excluding health checks | Grafana lint-overview |
| Latency | Check request latency P95 | Only /check path | Grafana lint-overview |

## SLO Targets
| SLI | Target | Measurement Window | Current Value | Compliance Status |
| --- | --- | --- | --- | --- |
| Availability | ≥99.9% | Rolling 30 days | 99.94% | Compliant |
| Latency P95 | <300ms | Rolling 7 days | 268ms | Compliant |

## Error Budget
- Calculation: 0.1% × 30 days = 43 minutes/month
- Burn Alerts: 50% notifies owner, 75% notifies on-call team, 90% freezes non-critical releases
- Exhaustion Policy: Pause feature releases; only stability fixes are allowed

### ALERT-001: 5xx Error Rate Exceeds Threshold
- Related SLI: Availability
- Expression: `rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])`
- Threshold: >0.01
- Duration: 5 minutes
- Severity: P1
- Owner: Wang Wu
- Response Guidelines:
  1. Open Grafana lint-overview to identify the source service of the errors
  2. Query ERROR logs and correlate the call chain by trace_id; a common cause is rule plugin load failure
  3. If not located within 10 minutes, escalate to Li Si and enter the P1 incident process
```

## Related Files

- Metric definitions and measurement: [Quality Metrics Specification](./quality-metrics-specification.md)
- Post-alert response process: [Incident Response Specification](./incident-response-specification.md)
- Deployment health checks: [Deployment and Rollback Specification](./deployment-and-rollback-specification.md)
- Log masking and privacy protection: [Security and Privacy Specification](./security-and-privacy-specification.md)
- Common troubleshooting entries: [Troubleshooting Specification](./troubleshooting-specification.md)
