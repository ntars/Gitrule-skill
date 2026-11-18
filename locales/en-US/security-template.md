# SECURITY Template

> What this file solves: Provides a copyable security policy template for projects to generate SECURITY.md, specifying supported versions, vulnerability reporting channels, response process, and disclosure principles; the accompanying filling instructions cover reporting channel selection and handling of sensitive information.

## 1. Usage Instructions

1. Copy all of the "Template Body" in Section 3 and create it as `SECURITY.md` in the project root.
2. Replace the placeholders per Section 4; the reporting channel must be a real, reachable address that does not publicly expose the attack surface.
3. Tailor according to the scenario variants in Section 5: projects without multi-version maintenance should delete the old version rows from the supported versions table.
4. For security rules and sensitive information requirements, see [Security and Privacy Specification](./security-and-privacy-specification.md); for the community governance dimension, see [Audit Dimension Matrix](./review-dimension-matrix.md).

## 2. Customization Principles

- **Private channels first**: Vulnerability reports go through private channels; requiring reporters to disclose details in public issues is prohibited.
- **Clear timeframes**: Give time ranges for first response and fix to avoid indefinite commitments.
- **Information minimization**: Require reporters to provide the minimum information needed for reproduction; submission of real production data is prohibited.
- **Legal consistency**: Disclosure principles must be consistent with applicable laws and platform policies; regulated industries must obtain legal review.

## 3. Template Body

```markdown
# Security Policy

> This file explains the security support scope and vulnerability reporting method of {{项目名称}}, and applies to security researchers, contributors, and users.

## Supported Versions

| Version | Security Reports Accepted |
| --- | --- |
| {{当前版本}} | Yes |
| {{上一版本}} | {{是否接受}} |
| Older versions | No |

## Reporting Channels

Do not report security vulnerabilities through public issues, discussion forums, or social channels. Please submit through the following private channels:

- Security email: {{真实可达的安全邮箱}}
- Private report portal: {{私有漏洞报告地址}}

If none of the above channels is available, contact the maintainers via {{备用私有联系方式}}.

## Report Content

To improve handling efficiency, please provide as much of the following as possible:

- Affected versions and components;
- Vulnerability type and potential impact;
- Minimal reproduction steps or proof of concept;
- Suggested fix direction (optional).

Do not submit real production data, secrets, or personally identifiable information.

## Response Process

| Stage | Time Range | Description |
| --- | --- | --- |
| Acknowledgment | {{首次响应时限}} | Maintainers confirm receipt of the report |
| Initial assessment | {{评估时限}} | Determine whether it is a security issue and its scope of impact |
| Fix and verification | {{修复时限}} | Complete the fix and verify it; complex issues are negotiated separately |
| Public release | {{发布延迟}} after the fix is complete | Publish the security advisory and fixed version |

## Disclosure Principles

- Maintainers will keep the reporter's identity and report content confidential until the fix is released.
- Without maintainer consent, reporters must not disclose vulnerability details before the fix is released.
- After the fix is released, maintainers will acknowledge the reporter in the security advisory (with the reporter's consent).
- Good-faith security research conducted in accordance with this policy will not be subject to legal action.

## Exceptions and Disclaimer

This policy does not constitute a commitment to any security guarantee; the project content is provided "as is", see [Disclaimer](./DISCLAIMER.md) and [LICENSE](./LICENSE).
```

## 4. Placeholder Correspondence Table and Field Definitions

| Placeholder | Required | Field Definition | Example |
| --- | --- | --- | --- |
| `{{项目名称}}` | Yes | Public project name | `FooBar` |
| `{{当前版本}}` | Yes | Latest maintained version or `main` | `v2.3.0` |
| `{{上一版本}}` | No | Previous version still under maintenance | `v2.2.x` |
| `{{是否接受}}` | Yes | Whether this version accepts security reports | `Yes` |
| `{{真实可达的安全邮箱}}` | Yes | Email dedicated to security reports | `security@example.com` |
| `{{私有漏洞报告地址}}` | Yes | Private report portal | `https://github.com/owner/repo/security/advisories/new` |
| `{{备用私有联系方式}}` | No | Backup method when the primary channel is unavailable | `Direct message via maintainer account` |
| `{{首次响应时限}}` | Yes | Time range for acknowledging receipt of the report | `3 business days` |
| `{{评估时限}}` | Yes | Time range for completing the initial assessment | `7 business days` |
| `{{修复时限}}` | Yes | Time range for completing the fix | `30 days` |
| `{{发布延迟}}` | Yes | Interval between the fix and public release | `7 days` |

## 5. Filling Instructions and Scenario Variants

| Scenario | Sections to Keep | Sections That May Be Trimmed | Key Adjustments |
| --- | --- | --- | --- |
| Single-version project | Reporting channels, report content, response process, disclosure principles | Delete old version rows from the supported versions table | Write `main` or the latest tag as the current version |
| Multi-version maintenance | All | None | List each version that still accepts reports |
| Individual project | All | Supported versions may be simplified | Use a long-term email as the private channel |
| Enterprise project | All | None | Timeframes must align with internal security policies and obtain legal review |
| Regulated industry | All | None | Add compliance reporting obligations and data retention requirements |

Common mistakes:

| Incorrect Writing | Consequence | Correct Writing |
| --- | --- | --- |
| "Please report vulnerabilities in an Issue" | Publicly discloses details and increases risk | Use a private channel |
| "We will handle it as soon as possible" | No clear expectation; reporters cannot judge | Give time ranges by stage |
| Writing "fix within 24 hours" for the timeframe | Overcommitment that cannot be fulfilled | Write a reasonable range and note that complex issues are negotiated separately |
| No redaction requirement | Reporters may submit real production data | Explicitly prohibit submitting real data and secrets |

## 6. Complete Example

The following is a filled-in example of the reporting channels section, for format reference only.

```markdown
## Reporting Channels

Do not report security vulnerabilities through public issues, discussion forums, or social channels. Please submit through the following private channels:

- Security email: security@example.com
- Private report portal: https://github.com/example/democli/security/advisories/new

Do not submit real production data, secrets, or personally identifiable information.
```

## Related Files

- Corresponding specification: [Security and Privacy Specification](./security-and-privacy-specification.md)
- Companion templates: [Code of Conduct Template](./code-of-conduct-template.md), [Contribution Guide Template](./contribution-guide-template.md), [Disclaimer Template](./disclaimer-template.md)
- Vulnerability reporting dimension: [Audit Dimension Matrix](./review-dimension-matrix.md)
- Incident handling for secret leakage: [Push and Release Specification](./push-and-release-specification.md)
- Return to the Simplified Chinese index: [README](./README.md)
