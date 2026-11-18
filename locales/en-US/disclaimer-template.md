# Disclaimer Template

> What this file solves: Provides a general disclaimer template that can be copied directly and applied by replacing placeholders, enabling any project to define its content nature, liability boundaries, and user obligations at minimal cost; the accompanying filling instructions and scenario variants cover personal, enterprise, open-source, and closed-source projects.

## 1. Usage Instructions

1. Copy all content of "Template Body" in Section 3 and create it as `DISCLAIMER.md` in the project root, or incorporate it as a separate section of `README.md`.
2. Replace each `{{...}}` according to the placeholder reference table in Section 4; unused sections must be deleted, leaving no empty placeholders.
3. Tailor clauses according to the scenario variants in Section 5: closed-source software emphasizes Section 3.5, while open-source projects must retain Section 3.6 and the explanation of the relationship with the license.
4. This template is general reference text and does not constitute legal advice. When it involves formal public release, cross-border distribution, or regulated industries, it must be used after legal review; see Section 2 of [Disclaimer](./disclaimer.md).
5. Before committing, verify: all placeholders replaced, contact information genuinely reachable, and no conflict with the terms of [LICENSE](../../LICENSE).

## 2. Customization Principles

- **Legality first**: All disclaimer clauses take effect only within the scope permitted by applicable law; absolute statements such as "unconditionally exempt from all liability" are prohibited to avoid the entire clause becoming invalid.
- **No overreach**: Rights granted by the license must not be revoked or reduced; in case of conflict, the license text prevails; see [LICENSE Specification](./license-specification.md).
- **Verifiable**: Contact information, effective dates, and entity names must be real information; example values must not be retained.
- **Independence**: Each clause is independent of the others; the invalidity of one clause does not affect the validity of the remaining clauses.

## 3. Template Body

The following, starting from Section 3.1, is the template body and can be copied directly.

### 3.1 Purpose and Scope of the Statement

```markdown
# Disclaimer

> This statement applies to all content released by {{项目名称}} (hereinafter "the Project"), including source code, documentation, templates, examples, data, and related materials (hereinafter collectively "Project Content"), regardless of whether it is used by human reading, programmatic invocation, or other means.

1. This statement serves to clarify the nature of the Project Content, alert users to usage risks, and define liability boundaries. It does not impose additional restrictions on the rights of any party, nor does it revoke or reduce the rights granted by the project's license.
2. Any party that accesses, copies, quotes, adapts, distributes, or uses all or part of the Project Content (hereinafter "User") is deemed to have read and understood this statement.
3. The last update date of this statement is {{更新日期}}.
```

### 3.2 Nature of Content

```markdown
## Nature of Content

1. The Project Content is {{内容性质描述}} and does not represent the official standards, legal opinions, or professional consulting conclusions of any organization, industry, or jurisdiction.
2. The Project Content provides no fitness warranty for any particular technology stack, runtime environment, or compliance requirement, and does not constitute professional legal, compliance, security, financial, or tax advice; in matters involving the above, Users should consult appropriately qualified professionals themselves.
3. Examples, parameters, and statistical information in the Project Content are only for illustrating methods or demonstrating writing styles and must not be used directly as recommended values for production environments; their validity is subject to {{数据或示例的时点与范围说明}}.
```

### 3.3 Disclaimer of Warranty

```markdown
## Disclaimer of Warranty

To the maximum extent permitted by law, the Project Content is provided "as is", and {{主体名称}} makes no express or implied warranties, including but not limited to:

- Absolute accuracy, completeness, error-freeness, or no omissions of the content;
- Fitness of the content for the User's particular purpose, particular environment, or particular compliance requirements;
- That implementation in accordance with the Project Content will necessarily achieve the expected results, or necessarily pass any review, testing, release, or certification process;
- Continuous availability or immutability of the Project Content, or compatibility with third-party tools, platforms, or services subsequently adopted by the User;
- Non-infringement of any third party's rights by the Project Content.
```

### 3.4 User Responsibilities

```markdown
## User Responsibilities

1. Before adopting the Project Content, Users should independently assess its suitability in light of their own project type, applicable laws and regulations, industry requirements, and risk tolerance, and decide for themselves whether to adopt it, which parts to adopt, and how to adjust it.
2. Users should validate templates, configurations, script snippets, and parameters before use, including syntax checking, build verification, test verification, and security review; they must not apply them directly to production environments, external services, or scenarios involving sensitive data without verification.
3. When adapting, abridging, merging, or redistributing the Project Content, Users should verify for themselves that the result is consistent with their own needs and applicable terms, and are responsible for the resulting documents, configurations, and deliverables.
4. Users should comply with applicable laws and internal policies of their jurisdiction and the project's industry; the Project Content does not replace the performance of relevant obligations.
```

### 3.5 Limitation of Liability

```markdown
## Limitation of Liability

1. To the maximum extent permitted by law, {{主体名称}} is not liable for any loss, damage, liability, cost, or expense arising or claimed to arise from the following circumstances, whether based on contract, tort (including negligence), or other legal grounds, and whether or not the party has been advised of the possibility:
   - Use, quotation, copying, adaptation, distribution, or implementation of all or part of the Project Content;
   - Decisions made, actions taken, or actions refrained from based on the Project Content;
   - Results of documents, configurations, and templates prepared in accordance with the Project Content when run in workflows;
   - Interruptions, failures, or data anomalies caused by compatibility issues between the Project Content and third-party tools, platforms, or services;
   - Changes to, suspension of provision of, or cessation of maintenance of the Project Content.
2. Losses and damages referred to in the preceding paragraph include but are not limited to: direct, indirect, incidental, consequential, and punitive damages, as well as loss of profits, loss of revenue, business interruption, data loss or corruption, damage to goodwill, additional procurement costs, and third-party claims.
3. The limitation clauses of this statement take effect only within the scope permitted by applicable law. If any jurisdiction does not permit the limitation or exclusion of certain liability, such limitations do not apply within that jurisdiction, and the remaining clauses remain valid.
```

### 3.6 Third-Party Content and Relationship with the License

```markdown
## Third-Party Content and Relationship with the License

1. External links, tools, services, icons, fonts, and materials referenced in the Project Content are provided by the respective third parties and are subject to their own terms; {{主体名称}} assumes no responsibility for their content, availability, accuracy, security, or legality, nor does it imply endorsement. Users should verify their terms and suitability themselves; the licensing obligations of third-party resources are not transferred or waived by their reference in the Project Content.
2. This project adopts the {{许可证名称及 SPDX 标识符}} license, the full text of which is in [LICENSE](./LICENSE). This statement is a user-side explanation of the license's disclaimer clauses and does not replace, modify, or weaken those license terms.
3. In case of any conflict in interpretation between this statement and the license terms, the license text prevails. Nothing in this statement may be construed as imposing additional charges, conditions, or restrictions on the granted rights.
4. When redistributing the Project Content or derivative content, copyright and license notices must be retained in accordance with the license, and this statement may be attached so downstream users understand the liability boundaries.
```

### 3.7 Changes and Effective Date

```markdown
## Changes and Effective Date

1. This statement is revised from time to time by {{维护主体}} as needed for content updates and compliance; the latest version in {{仓库地址或发布渠道}} prevails after revision.
2. This statement takes effect from {{生效日期}}. If a User continues to use the Project Content after revision, the revised version prevails; if a User does not agree with the revised content, they should stop using it.
3. The clauses of this statement are independent. If any clause is found invalid or unenforceable, the validity of the remaining clauses is not affected.
4. Contact: {{真实可达的联系邮箱或渠道}}.
```

## 4. Placeholder Reference Table and Field Definitions

| Placeholder | Required | Field Definition | Filling Example |
| --- | --- | --- | --- |
| `{{项目名称}}` | Yes | Public project name, consistent with the first line of the README | `FooBar` |
| `{{主体名称}}` | Yes | Full name of the entity assuming or waiving liability; for personal projects write the name, for enterprise projects write the legal name | `Some Technology Co., Ltd.` |
| `{{维护主体}}` | Yes | Organization or individual responsible for revising the statement | `FooBar Maintenance Team` |
| `{{更新日期}}` | Yes | Date of the most recent revision of this statement, uniformly formatted as YYYY-MM-DD | `2026-11-18` |
| `{{生效日期}}` | Yes | Date from which this statement takes effect; may be the same as the update date | `2026-11-18` |
| `{{内容性质描述}}` | Yes | One-line description of what the project is and its maturity level | An example implementation for developer reference, not a production-grade component |
| `{{数据或示例的时点与范围说明}}` | No | Time point and scope of collection for data or parameters in examples | Statistics from 120 samples collected in October 2026 |
| `{{许可证名称及 SPDX 标识符}}` | Yes | Full name and SPDX identifier of the project license | MIT License (MIT) |
| `{{仓库地址或发布渠道}}` | Yes | Authoritative publication location of the latest version of the statement | `https://github.com/owner/repo` |
| `{{真实可达的联系邮箱或渠道}}` | Yes | Real address through which Users can reach the maintainers | `security@example.com` |

## 5. Filling Instructions and Scenario Variants

| Scenario | Clauses to Keep | Clauses That May Be Tailored | Key Adjustments |
| --- | --- | --- | --- |
| Personal project | 3.1 / 3.2 / 3.3 / 3.5 / 3.7 | 3.4 may be simplified | Write the real name as the entity name; use an email address that can be held long-term |
| Enterprise project | All clauses | None | Write the legal name from the business license as the entity name; publish only after legal review |
| Open-source project | All clauses, especially 3.6 | None | Retain the explanation of the relationship with the license; do not reduce rights granted by the license |
| Closed-source software | 3.1 / 3.2 / 3.3 / 3.4 / 3.5 / 3.7 | Paragraphs 2–4 of 3.6 may be deleted | Remove references to open-source licenses and replace with references to the end-user license agreement |
| Experimental prototype | 3.1 / 3.2 / 3.3 / 3.7 | 3.5 may be simplified | Explicitly mark "prototype" in the nature of content to avoid being taken as a stable version |
| Involving personal information processing | All clauses | None | Add data processing roles, retention periods, and channels for exercising data subject rights; see also [Security and Privacy Specification](./security-and-privacy-specification.md) |

Common error comparison:

| Incorrect Writing | Consequence | Correct Writing |
| --- | --- | --- |
| "This project assumes no liability whatsoever" | Absolute wording, easily deemed invalid | "To the maximum extent permitted by law, no liability is assumed..." |
| "The author reserves the right of final interpretation" | Conflicts with license authorization, causing disputes | "In case of conflict, the license text prevails" |
| Leaving `test@example.com` as the contact | Unreachable, losing the communication channel | Fill in a real, long-term valid email address |
| Copying another project's statement without changing the entity | Entity mismatch, statement loses meaning | Replace each placeholder and verify entity consistency |

## 6. Complete Example

The following is a filled-in example for a personal open-source project, for format reference only; it must not be copied directly as your own statement.

```markdown
# Disclaimer

> This statement applies to all content released by DemoCLI (hereinafter "the Project"), including source code, documentation, templates, examples, data, and related materials (hereinafter collectively "Project Content").

1. This statement serves to clarify the nature of the Project Content, alert users to usage risks, and define liability boundaries. It does not impose additional restrictions on the rights of any party, nor does it revoke or reduce the rights granted by the project's license.
2. Any party that accesses, copies, quotes, adapts, distributes, or uses all or part of the Project Content is deemed to have read and understood this statement.
3. The last update date of this statement is 2026-11-18.

## Nature of Content

1. The Project Content is a command-line example tool for developer reference and does not represent the official standards, legal opinions, or professional consulting conclusions of any organization, industry, or jurisdiction.
2. The Project Content provides no fitness warranty for any particular technology stack, runtime environment, or compliance requirement, and does not constitute professional legal, compliance, security, financial, or tax advice.
3. Example parameters in the Project Content are only for demonstrating writing styles and must not be used directly as recommended values for production environments.

## Disclaimer of Warranty

To the maximum extent permitted by law, Zhang San makes no express or implied warranties, including but not limited to absolute accuracy of the content, fitness for a particular purpose, that implementation will necessarily achieve the expected results, continuous availability, and non-infringement of third-party rights.

## Limitation of Liability

To the maximum extent permitted by law, Zhang San is not liable for any loss arising from the use, adaptation, or implementation of the Project Content, whether based on contract, tort, or other legal grounds. If any jurisdiction does not permit the limitation or exclusion of certain liability, such limitations do not apply within that jurisdiction, and the remaining clauses remain valid.

## Third-Party Content and Relationship with the License

This project adopts the MIT License (MIT), the full text of which is in [LICENSE](./LICENSE). This statement is a user-side explanation of the license's disclaimer clauses and does not replace, modify, or weaken those license terms; in case of conflict in interpretation, the license text prevails.

## Changes and Effective Date

This statement takes effect from 2026-11-18, is revised by the DemoCLI Maintenance Team, and the latest version at https://github.com/example/democli prevails. The clauses are independent. Contact: maintainer@example.com.
```

## Related Files

- This project's instance statement: [Disclaimer](./disclaimer.md)
- License rules: [LICENSE Specification](./license-specification.md)
- Security and privacy: [Security and Privacy Specification](./security-and-privacy-specification.md)
- Open-source compliance: [Open-Source Compliance Specification](./open-source-compliance-specification.md)
- General writing conventions: [General Writing Specification](./general-writing-specification.md)
- Back to the Simplified Chinese index: [README](./README.md)
- Back to the repository front page: [README](../../README.md)
