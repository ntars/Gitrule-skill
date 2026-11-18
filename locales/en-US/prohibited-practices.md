# Prohibited Practices

> What this file solves: Aggregates all prohibited behaviors that must not be violated, serving as the final red-line checklist for review and writing.

## 1. Control and Push Red Lines

1. Do not output "you can push first and supplement later" when P0 is not cleared.
2. Do not fabricate check results; mark items that cannot be checked as `SKIP + reason`, and do not write PASS.
3. Do not deliver multiple documents merged into a single file.
4. Do not stuff the full API, contribution guide, or changelog into the README.
5. Do not use `--force` to push public branches, under any circumstances.
6. Do not handle a leaked secret by making only a "deletion commit".
7. Do not invent repository names outside of [Project Naming Specification](./project-naming-specification.md).
8. Do not write internal thought processes into deliverable documents.

## 2. Document Writing Red Lines

1. Do not fabricate project names, features, performance data, dependency versions, licenses, author information, or test results.
2. Do not copy others' READMEs, documents, code, images, or copy; when a citation is truly needed, the source and license must be indicated.
3. Do not select a license type without confirmation.
4. Do not include unverified performance figures, comparison conclusions without sources, commitment statements (such as "guaranteed" or "free forever"), derogatory descriptions of third-party projects, or promotional content unrelated to the project.
5. Do not use materials of unknown origin; when images, icons, or fonts lack a source and license, mark them as pending confirmation and do not use them directly.

## Related Files

- For hard rules whose violation blocks push, see [Hard Rules](./hard-rules.md)
- For incident handling (secret leakage, etc.), see Section 5 of [Push and Release Specification](./push-and-release-specification.md)
- For role hard constraints, see [Roles and Responsibilities](./roles-and-responsibilities.md)
