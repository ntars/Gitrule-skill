# LICENSE Specification

> What this file solves: Defines the SPDX annotation of the project license, LICENSE full-text requirements, the location of the copyright line, multi-license descriptions, and rules prohibiting writing unconfirmed content.

## LICENSE Rules

1. The project license must be explicitly written in the README using its SPDX identifier, and a corresponding LICENSE file must be provided.
2. The LICENSE file must be the official English full text of that license; terms must not be deleted or altered.
3. The copyright line is placed at the top of the file or in Chapter 19 of the README; see [README Section Specification](./readme-sections-specification.md) for the format.
4. When dual licensing or multiple licenses are used, the applicable conditions and selection method must be explained.
5. When the license selection has not been confirmed by the user, it must not be written directly into the document; only candidate options and a description of differences may be provided.

## Related Files

- A missing LICENSE blocks push; this is hard rule H2, see [Hard Rules](./hard-rules.md)
- For dependency license compatibility determination, see [Open Source Compliance Specification](./open-source-compliance-specification.md)
- For the standalone file of third-party declarations, see [NOTICE Specification](./notice-specification.md)
- License accuracy belongs to gates G7/G8; see [Quality Gates](./quality-gate.md)
