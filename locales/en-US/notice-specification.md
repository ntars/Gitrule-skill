# NOTICE Specification

> What this file solves: Defines the seven parts that a NOTICE file must contain and the consistency requirements with the README, ensuring third-party declarations are in a standalone file and the information is accurate.

## 1. Standalone File

NOTICE must be a standalone file; it must not be merged with the README, nor replaced by a list in the README. It must contain the following parts:

1. **Project's own declaration**: Project name, copyright holder, year, license, SPDX identifier.
2. **Third-party component list**: Listed item by item according to the dependency manifest fields in the [Open Source Compliance Specification](./open-source-compliance-specification.md).
3. **License full-text appendix**: If a license requires the full text to be attached, attach the original text of each; the original text remains in English and is not translated.
4. **Modification declaration**: The locations and content of modifications to third-party code.
5. **Asset and data source declaration**.
6. **Disclaimer**: Retain the English original; a Chinese translation may be appended.
7. **Pending items**: Items whose license or copyright ownership cannot be verified must be explicitly marked as "pending confirmation".

## 2. Consistency Requirements

The component and license information in NOTICE and in the README Chapter 6 (Technology Stack and Dependency Manifest), Chapter 19 (Copyright and Licensing), and Chapter 20 (NOTICE Compliance Declaration) must be exactly consistent; there must be no discrepancies in versions, license identifiers, or copyright holders.

## Related Files

- For dependency manifest fields and collection methods, see [Open Source Compliance Specification](./open-source-compliance-specification.md)
- For license full-text requirements, see [LICENSE Specification](./license-specification.md)
- For related README sections, see [README Section Specification](./readme-sections-specification.md)
- Consistency belongs to gates G7–G9; see [Quality Gates](./quality-gate.md)
