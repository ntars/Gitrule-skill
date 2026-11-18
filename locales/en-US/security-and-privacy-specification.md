# Security and Privacy Specification

> What this file solves: Defines sensitive information protection, the data privacy inventory, the SECURITY.md template, and vulnerability reporting fields, ensuring no leaks before publication, compliant data processing, and reachable vulnerability channels.

## 1. Specification Clauses

1. Keys, tokens, private keys, `.env`, cloud provider AK/SK, and database connection strings must not be committed (corresponds to hard rule H3).
2. Key scanning must cover the workspace and the complete history, and be executed before push (see [Push and Release Specification](./push-and-release-specification.md)).
3. Internal domains, IPs, personal information, and log residue must be cleaned up before publication (corresponds to dimension D1).
4. Once a key has been pushed, it must be immediately rotated + the history cleaned; a deletion-only commit is not sufficient (corresponds to H12).
5. State what data is collected, its purpose, storage location, and retention period; encrypt data in transit and at rest, and mask data when displayed.
6. The permission model follows the principle of least necessity; data involving cross-border transfer must be assessed separately.
7. Provide a vulnerability reporting channel that reaches the maintainers directly, with commitments to confidentiality and response time; state known risks truthfully, and do not promise absolute security.

## 2. Sensitive Information Self-Check Template

```markdown
# Sensitive Information Self-Check: {{项目名称}}

Check date: {{YYYY-MM-DD}} ｜ Executor: {{姓名}} ｜ History covered: {{是 / 否}}

| Check Item | Tool / Command | Result | Action |
| --- | --- | --- | --- |
| Workspace secrets | {{扫描工具}} | {{命中数}} | {{已清理 / 无}} |
| Secrets in commit history | {{扫描工具 --all}} | {{命中数}} | {{已轮换 / 无}} |
| `.env` and credential files | `git ls-files \| grep -E ...` | {{文件数}} | {{已移除 / 无}} |
| Internal domains / IPs | {{检索命令}} | {{命中数}} | {{已替换 / 无}} |
| Personal information | {{检索命令}} | {{命中数}} | {{已脱敏 / 无}} |
| Log and snapshot residue | {{检查命令}} | {{命中数}} | {{已清理 / 无}} |

Conclusion: {{通过 / 不通过}}
- Rotated key list: {{无 / 列出}}
- Reviewer: {{姓名}}
```

## 3. Data Privacy Inventory Template

```markdown
# Data Privacy Inventory: {{项目名称}}

## Data Items
| Data Item | Collection Purpose | Collection Method | Storage Location | Retention Period | Encrypted | Masked | Third-Party Sharing |
| --- | --- | --- | --- | --- | --- | --- | --- |
| {{如邮箱}} | {{账号识别}} | {{用户填写}} | {{数据库字段}} | {{删除账号后 30 天}} | {{是}} | {{展示时掩码}} | {{无}} |

## Permission Model
| Role | Accessible Data | Basis for Permission | Review Cycle |
| --- | --- | --- | --- |
| {{角色}} | {{最小必要范围}} | {{业务需要}} | {{每季度}} |

## Compliance Assessment
- Applicable regional regulations: {{列举}}
- Cross-border data transfer: {{无 / 评估结论与措施}}
- User rights response: {{查询 / 更正 / 删除的渠道与时限}}
```

## 4. SECURITY.md Template

```markdown
# Security Policy

## Supported Versions
| Version | Accepts Security Reports |
| --- | --- |
| {{最新主版本}} | Yes |
| {{旧版本}} | No / Critical issues only |

## Reporting Channel
- Preferred: {{私密渠道，如 GitHub Security Advisories}}
- Backup: {{加密邮箱}}
- Do not report vulnerabilities through public Issues.

## Response Commitment
| Stage | Time Limit |
| --- | --- |
| Acknowledgment of receipt | {{2 个工作日}} |
| Preliminary confirmation | {{5 个工作日}} |
| Fix and disclosure | {{视严重程度，目标 30 天}} |

## Handling Process
Receive → Confirm → Fix → Disclose → Announce

## Known Risks
{{如实说明当前已知风险；无则写「暂无已知风险」，不得承诺绝对安全}}
```

## 5. Field Definitions

| Field | Required | Type | Filling Guidance | Example |
| --- | --- | --- | --- | --- |
| History covered | Yes | Enum | Must select "Yes" to be judged as passing | `Yes` |
| Check Item.Result | Yes | Number | Fill in the number of hits; "probably none" is prohibited | `0` |
| Rotated key list | Conditionally required | List | Required when keys are hit; list rotation credentials | `API_KEY rotated` |
| Data Item.Retention Period | Yes | Text | Specific duration; "long-term" is not allowed | `30 days after account deletion` |
| Data Item.Third-Party Sharing | Yes | Text | Write "None" if none | `None` |
| Supported Versions | Yes | Table | Clearly state which versions accept reports | `2.x: Yes` |
| Reporting Channel | Yes | Text | At least one non-public channel | `Security Advisories` |
| Response Time Limit | Yes | Duration | Every stage has a numeric value | `2 business days` |

## 6. Filling Instructions

1. **History scanning**: Key scanning must include the complete git history; scanning only the workspace is considered invalid.
2. **Key hits**: Once a pushed key is found, rotate first, then clean the history; the order must not be reversed (corresponds to H12).
3. **Masking**: Sensitive fields appearing in displays and logs must be masked; printing full tokens, ID card numbers, or phone numbers is prohibited.
4. **Retention period**: "Stored long-term" is unacceptable; a specific period or an event that triggers deletion must be given.
5. **Supported versions**: List at least the current major version; if older versions are unsupported, state this explicitly to avoid false reports from users.
6. **Reporting channel**: Must be a non-public channel; disclosing vulnerabilities in public Issues increases risk.
7. **Known risks**: List truthfully; "this system is absolutely secure" is a prohibited statement.

Common mistakes:

| Incorrect Wording | Problem | Correction |
| --- | --- | --- |
| Delete the key commit without rotating | Violates H12 | Rotate first, then clean the history |
| Self-check scans only the workspace | Historical leaks go undetected | Add history scanning |
| Data retention written as "permanent" | No boundary | Give a specific period |
| Vulnerability reported via public Issue | Increases exposure | Switch to a private channel and write it into SECURITY.md |
| Promise "absolute security" | Untruthful statement | Change to a truthful description of known risks |

## 7. Complete Example

```markdown
## Sensitive Information Self-Check: markdown-lint-cli

Check date: 2026-11-18 ｜ Executor: Wang Wu ｜ History covered: Yes

| Check Item | Tool / Command | Result | Action |
| --- | --- | --- | --- |
| Workspace secrets | gitleaks detect | 0 | None |
| Secrets in commit history | gitleaks detect --log-opts=--all | 0 | None |
| `.env` and credential files | git ls-files | 0 | None |
| Internal domains / IPs | Regex search | 0 | None |

Conclusion: Pass
- Rotated key list: None
- Reviewer: Li Si
```

## Related Files

- Key red lines H3/H12: [Hard Rules](./hard-rules.md)
- Incident handling for leaked keys: [Incident Response Specification](./incident-response-specification.md)
- Pre-push scanning execution: [Push and Release Specification](./push-and-release-specification.md)
- Log masking: [Observability Specification](./observability-specification.md)
- SECURITY document boundary: [Document Matrix](./document-matrix.md)
- Statement of known risks in README: [README Section Specification](./readme-sections-specification.md)
- Community conduct conventions: [Code of Conduct Specification](./code-of-conduct-specification.md)
