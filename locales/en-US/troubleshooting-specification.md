# Troubleshooting Specification

> What this file solves: Defines the structure, entry writing style, and maintenance mechanism of troubleshooting documentation (Troubleshooting / FAQ), enabling users to locate causes from symptoms and resolve common problems themselves.

## 1. Applicable Scenarios

Troubleshooting documentation must be provided in the following situations:

1. Installation or build failures have multiple common causes.
2. Configuration items conflict, and error messages do not adequately explain the solution.
3. Specific platforms or versions have known limitations.
4. Users repeatedly ask the same type of question, and the answer can be standardized.

## 2. File Location and Naming

1. When there is little content, include it as a README section titled "FAQ" or "Troubleshooting".
2. When there is substantial content, create a separate `docs/troubleshooting.md` or `FAQ.md`, with the README retaining an entry link.
3. Group problems by topic, such as "Installation", "Configuration", "Runtime", "Performance", and "Network".

## 3. Document Structure

1. **Opening Note**: The range of common problems covered and the applicable versions.
2. **Problem Index**: List problem titles by topic to support quick navigation.
3. **Problem Entries**: Expand each entry using a uniform structure.
4. **Still Unresolved**: Point to issues, discussion forums, and other help channels.

## 4. Entry Structure

Each problem entry must contain the following parts:

| Part | Content | Requirement |
| --- | --- | --- |
| Symptom | The concrete manifestation the user sees | Include the complete error message; do not merely write "error" |
| Trigger Condition | When it occurs | Specify version, platform, and operation |
| Cause | The root cause | Explain the mechanism, not just the conclusion |
| Solution | Executable steps | Numbered, with commands or configuration |
| Verification | How to confirm the fix | Give the expected output |
| Related | Related documentation or issue link | Optional |

## 5. Entry Writing Example

```markdown
### Installation reports `EACCES: permission denied`

**Symptom**: Running `npm install -g <package>` reports insufficient permissions.

**Trigger Condition**: Installing a global package as a regular user on Linux or macOS.

**Cause**: Write permission to the global install directory belongs to the system administrator; the current user has no write access.

**Solution**:

```bash
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
npm install -g <package>
```

**Verification**: Running `<package> --version` and getting a version number means success.

## 6. Writing Requirements

1. Problem titles should use wording users would search for, rather than internal jargon.
2. Keep error messages verbatim for user comparison; sensitive information must be masked (see [Security and Privacy Specification](./security-and-privacy-specification.md)).
3. Solutions should give complete commands and not assume the user has set environment variables.
4. One entry solves one problem; do not merge multiple causes.
5. When a known defect is involved, state the impact scope and workaround; do not promise a fix time.
6. Link migration-related problems to the migration guide (see [Migration Guide Specification](./migration-guide-specification.md)).

## 7. Maintenance Mechanism

1. When the same question is asked more than three times, add or rewrite an entry.
2. After a version upgrade, review all entries and delete invalidated content.
3. Each entry may be marked with the version last verified, to help judge whether it still applies.
4. The problem index is updated in sync with entry additions and removals.

## 8. Prohibited Practices

1. Writing troubleshooting documentation as a feature introduction is prohibited.
2. Writing answers with no diagnostic value, such as "try restarting", is prohibited.
3. Omitting error messages and trigger conditions is prohibited.
4. Retaining entries that are fixed or no longer valid is prohibited.

## Related Files

- README section placement: [README Section Specification](./readme-sections-specification.md), Chapter 15
- Known issue disclosure requirements: [README Section Specification](./readme-sections-specification.md), Chapter 15
- Upgrade-related issues: [Migration Guide Specification](./migration-guide-specification.md)
- Issue collection channels: [Issue and PR Template Specification](./issue-and-pr-template-specification.md)
- Documentation quality is dimension D12: [Audit Dimension Matrix](./review-dimension-matrix.md)
