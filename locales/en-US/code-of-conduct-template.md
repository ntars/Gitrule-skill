# Code of Conduct Template

> What this file solves: Provides a directly copyable code of conduct template for projects to generate `CODE_OF_CONDUCT.md`, specifying participation commitments, expected behavior, unacceptable behavior, enforcement responsibilities, and reporting channels; the accompanying filling instructions cover adaptation sources and version statements.

## 1. Usage Instructions

1. Copy all content of "Template Body" in Section 3 and create it as `CODE_OF_CONDUCT.md` in the project root.
2. Replace placeholders according to Section 4; the reporting channel must be a genuinely reachable address.
3. If adopting or adapting an existing version of a code of conduct, the version and license must be stated in Section 5 according to the source requirements; see item 8 of Section 1 in [Code of Conduct Specification](./code-of-conduct-specification.md).
4. Link this file in the [Contribution Guide Template](./contribution-guide-template.md) and the README's contributing section, keeping bidirectional reachability.

## 2. Customization Principles

- **Technology-agnostic**: The code of conduct contains no technical content and only specifies norms of participation; see [Document Matrix](./document-matrix.md) for boundaries.
- **Enforceable**: Graded handling must specify trigger conditions and measures; writing only principles without consequences is prohibited.
- **Reachability**: Reporting channels must be genuinely valid; example addresses must not be left.
- **Compliant sources**: Adapted third-party codes of conduct must retain their attribution and licensing requirements; see [Open-Source Compliance Specification](./open-source-compliance-specification.md).

## 3. Template Body

```markdown
# Code of Conduct

## Our Pledge

We, as participants, contributors, and maintainers of {{项目名称}}, pledge to collectively foster an open, welcoming, and harassment-free participation environment, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, or sexual orientation.

## Scope

This code of conduct applies within project spaces, issues, pull requests, code reviews, social channels, and public spaces when an individual is representing the project or its community.

## Expected Behavior

- Respect differing viewpoints and experiences; communicate in good faith.
- Accept constructive feedback; focus on the issue itself rather than the person.
- Focus on the overall interests of the community; avoid harming the project and its participants.
- Be patient with newcomers and provide actionable improvement suggestions.

## Unacceptable Behavior

- Personal attacks, insulting, or derogatory comments.
- Discriminatory language and harassment based on any protected characteristic.
- Public or private harassment, stalking, or sustained unwanted contact.
- Publishing others' private information without authorization.
- Other conduct that could reasonably be considered inappropriate in a professional setting.

## Enforcement Responsibilities

Project maintainers are responsible for clarifying the application of this code of conduct, adjudicating violations, and have the right to remove, edit, or reject content that does not conform to this code of conduct. Maintainers must exercise their duties in a consistent and fair manner and must proactively recuse themselves from disputes involving themselves.

## Enforcement Measures

Violations are handled in grades according to severity:

| Level | Applicable Situation | Measure |
| --- | --- | --- |
| Level 1 | Unintentional offense, minor impropriety | Private reminder and explanation |
| Level 2 | Repeated occurrence or clear violation | Public warning, correction within a deadline |
| Level 3 | Severe harassment, malicious attacks | Temporary suspension of participation privileges |
| Level 4 | Persistent or irredeemable severe behavior | Permanent ban with records retained |

## Reporting Channel

If you experience or witness behavior that violates this code of conduct, please contact the maintenance team via {{真实可达的举报邮箱或渠道}}. All reports will be handled confidentially; maintainers must not disclose the reporter's identity to the reported party unless the reporter explicitly consents.

## Attribution and Source

{{准则来源声明}}
```

## 4. Placeholder Reference Table and Field Definitions

| Placeholder | Required | Field Definition | Filling Example |
| --- | --- | --- | --- |
| `{{项目名称}}` | Yes | Public project name, consistent with the first line of the README | `FooBar` |
| `{{真实可达的举报邮箱或渠道}}` | Yes | Real address through which maintainers can be directly contacted | `conduct@example.com` |
| `{{准则来源声明}}` | Yes | For original work write "original"; for adaptations write the source name, version, and license | Adapted from Contributor Covenant 2.1 (CC BY 4.0) |

## 5. Filling Instructions and Scenario Variants

| Scenario | Key Adjustments |
| --- | --- |
| Personal project | Write yourself as the maintainer; use an email address that can be held long-term |
| Enterprise project | Specify the legal or community team as the enforcing body; enforcement measures must be consistent with internal policies |
| Adopting a well-known code of conduct | Retain its full original text and version, adding only the reporting channel and attribution |
| Multilingual project | Clauses in each language version correspond one-to-one; designate the English or Chinese version as authoritative and note it |

Common error comparison:

| Incorrect Writing | Consequence | Correct Writing |
| --- | --- | --- |
| Only writing "friendly communication is welcome" | No basis for enforcement, cannot adjudicate disputes | List expected behavior, unacceptable behavior, and graded enforcement |
| Leaving a placeholder email as the reporting channel | Unreachable, reporting mechanism fails | Fill in a real, long-term valid address |
| Adapting a code of conduct without attribution | Violates the source's licensing requirements | State the source, version, and license |

## 6. Complete Example

The following is an excerpt for an adaptation scenario, for format reference only.

```markdown
## Reporting Channel

If you experience or witness behavior that violates this code of conduct, please contact the maintenance team via conduct@example.com. All reports will be handled confidentially.

## Attribution and Source

This code of conduct is adapted from Contributor Covenant 2.1, under the CC BY 4.0 license.
```

## Related Files

- Corresponding specification: [Code of Conduct Specification](./code-of-conduct-specification.md)
- Companion templates: [Contribution Guide Template](./contribution-guide-template.md), [SECURITY Template](./security-template.md)
- Community governance dimension: [Audit Dimension Matrix](./review-dimension-matrix.md)
- Back to the Simplified Chinese index: [README](./README.md)
