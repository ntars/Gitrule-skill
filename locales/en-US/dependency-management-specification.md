# Dependency Management Specification

> What this file solves: Defines templates and fields for dependency introduction requests, dependency manifests, locking, and updates, ensuring reproducible builds, traceable dependencies, and license compliance.

## 1. Specification Clauses

1. Introducing a new dependency must state its purpose, license, and maintenance status (see [Open Source Compliance Specification](./open-source-compliance-specification.md)).
2. Prefer dependencies with compatible licenses and active communities; dependencies of unknown origin or with unknown licenses are forbidden.
3. Dependency versions must be written into a lockfile and committed to the repository, ensuring reproducible builds in a clean environment (corresponding to hard rule H9 and dimension D5).
4. Version numbers must lock the actually resolved version; range expressions must not be used as the final deliverable.
5. Dependency updates must be assisted by automation tools, and CI must pass after updating; vulnerabilities must be handled promptly or mitigations must be recorded.
6. The dependency manifest must be consistent with NOTICE (see [NOTICE Specification](./notice-specification.md)).

## 2. Dependency Introduction Request Template

```markdown
## Dependency Introduction Request: {{包名}}

- Request ID: {{DEP-NNN}}
- Requester: {{姓名}}
- Purpose: {{一句话说明解决什么问题}}
- Can be self-built: {{是 / 否；是则说明为何仍引入}}
- Alternative evaluation: {{已评估的替代包及未选原因}}

| Field | Value |
| --- | --- |
| Package name | {{包名}} |
| Introduced version | {{精确版本号}} |
| License | {{SPDX ID}} |
| License compatibility | {{兼容 / 不兼容 / 需法务确认}} |
| Last release date | {{YYYY-MM-DD}} |
| Maintenance status | {{活跃 / 低频 / 停滞}} |
| Weekly downloads | {{数值}} |
| Number of transitive dependencies | {{数值}} |
| Known vulnerabilities | {{无 / CVE 编号与处置}} |
| Package size impact | {{增量 KB}} |

- Conclusion: {{批准 / 拒绝 / 有条件批准}}
- Approver: {{姓名}}
```

## 3. Dependency Manifest Template

```markdown
# Dependency Manifest: {{项目名称}}

Updated: {{YYYY-MM-DD}} ｜ lockfile: {{路径}} ｜ Generation tool: {{工具与版本}}

| Dependency | Introduced version | Locked version | Type | License | Purpose | Last reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| {{包名}} | {{^1.2.0}} | {{1.2.3}} | Direct / Indirect | {{MIT}} | {{用途}} | {{YYYY-MM-DD}} |

## Update Records
| Date | Dependency | Version change | Reason | Verification result |
| --- | --- | --- | --- | --- |
| {{YYYY-MM-DD}} | {{包名}} | {{1.2.2 → 1.2.3}} | {{安全修复}} | {{CI 全绿}} |

## Exceptions and Mitigations
| Dependency | Problem | Mitigation | Review date |
| --- | --- | --- | --- |
| {{包名}} | {{漏洞 / 停滞}} | {{限制使用范围}} | {{YYYY-MM-DD}} |
```

## 4. Field Definitions

| Field | Required | Type | Filling guidelines | Example |
| --- | --- | --- | --- | --- |
| Request ID | Yes | `DEP-NNN` | Consecutive, not reused | `DEP-007` |
| Purpose | Yes | Text | State the problem solved; "for convenience" is forbidden | `Parse TOML configuration` |
| Alternative evaluation | Yes | Text | Evaluate at least 1 alternative | `Evaluated toml-js, not chosen due to stalled maintenance` |
| Introduced version | Yes | Exact version | Must not use `^` or `~` | `1.2.3` |
| Locked version | Yes | Exact version | Consistent with the lockfile | `1.2.3` |
| License | Yes | SPDX ID | Written consistently with [LICENSE Specification](./license-specification.md) | `MIT` |
| Maintenance status | Yes | Enum | Active / Low frequency / Stalled, with basis attached | `Active (commits in the last 30 days)` |
| Number of transitive dependencies | Yes | Number | If too many, explain the size and risk impact | `12` |
| Known vulnerabilities | Yes | Text | Write "None" if none; must not be left blank | `None` |
| Review date | Yes | Date | Exception items must set a review date | `2026-12-31` |

## 5. Filling Instructions

1. **Self-build evaluation**: First answer "Can this be implemented with the standard library or existing capabilities?" If it can be self-built but is still introduced, explain why.
2. **License**: Must be an SPDX ID; `UNLICENSED` and custom licenses must be treated as "legal confirmation required" and must not be introduced directly.
3. **Maintenance status**: Based on the last release date and issue response; "seems to be maintained" is forbidden.
4. **Version locking**: At delivery, the lockfile must contain exact resolved versions; `package.json` may keep range expressions, but the lockfile must be exact.
5. **Update cadence**: Automated updates should be enabled, with manual confirmation before merging; each update must pass CI and verify license changes.
6. **Vulnerability handling**: Prefer upgrading to a secure version; when upgrading is impossible, state the mitigations and review date, and enter the risk register in [Incident Response Specification](./incident-response-specification.md).
7. **Manifest sync**: After adding or removing a dependency, update the dependency manifest and NOTICE; the three (lockfile, manifest, NOTICE) must be consistent.

Common mistakes:

| Wrong wording | Problem | Correction |
| --- | --- | --- |
| "Use a library to handle config" | No specific package name or purpose | Write the package name, version, and problem solved |
| License written as "open source" | Compatibility not determinable | Write the SPDX ID |
| lockfile not committed | Build not reproducible | Commit the lockfile (corresponding to H9) |
| Transitive dependency count left blank | Risk invisible | Fill in a specific number |
| Vulnerability without mitigation | Risk untracked | Add mitigation and review date |

## 6. Complete Example

```markdown
## Dependency Introduction Request: remark

- Request ID: DEP-001
- Requester: Wang Wu
- Purpose: Serves as the Markdown parsing layer, supporting node location for the rule engine (REQ-001, REQ-004).
- Can be self-built: No; self-building cannot cover GFM boundary cases within the staffing limit.
- Alternative evaluation: Evaluated marked, not chosen due to insufficient Chinese node location capability.

| Field | Value |
| --- | --- |
| Package name | remark |
| Introduced version | 15.0.1 |
| License | MIT |
| License compatibility | Compatible |
| Last release date | 2026-11-02 |
| Maintenance status | Active (commits in the last 30 days) |
| Weekly downloads | 4,200,000 |
| Number of transitive dependencies | 18 |
| Known vulnerabilities | None |
| Package size impact | +42 KB |

- Conclusion: Approved, to be implemented together with ADR-0002
- Approver: Li Si
```

## Related Files

- License compatibility judgment: [Open Source Compliance Specification](./open-source-compliance-specification.md)
- License SPDX notation: [LICENSE Specification](./license-specification.md)
- NOTICE consistency: [NOTICE Specification](./notice-specification.md)
- Reproducible builds are dimension D5: [Review Dimension Matrix](./review-dimension-matrix.md)
- Automated updates are dimension D9: [Review Dimension Matrix](./review-dimension-matrix.md)
- Testing and vulnerability handling: [Testing Specification](./testing-specification.md), [Security and Privacy Specification](./security-and-privacy-specification.md)
- Architecture decision linkage: [Architecture Design Document Specification](./architecture-design-document-specification.md)
