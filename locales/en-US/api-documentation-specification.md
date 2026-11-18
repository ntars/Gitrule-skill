# API Documentation Specification

> What this file solves: Defines the structure and fields of a complete API reference document, serving as the writing basis for docs/api.md and strictly separated from tutorial-type content.

## 1. Required Structure

Every API entry must include:

| Field | Requirement |
| --- | --- |
| Interface signature | Method, path, or function prototype, complete and copyable |
| Parameters | Name, type, whether required, default value, value range, description |
| Return value | Type and structure description |
| Error codes | Error code, trigger condition, handling method |
| Call example | A runnable minimal example, with the language marked |
| Rate limiting and quotas | Call frequency limits, quotas, and over-limit handling |

## 2. Mandatory Rules

1. Parameters and return values must state their types and constraints, and default values must not be omitted.
2. Error codes must be listed completely; writing only "errors may occur" is not acceptable.
3. Code blocks must be marked with a language identifier, and examples must be independently runnable.
4. This file contains only reference information; do not write tutorials, background, or design descriptions (for tutorials and background, see the [README Sections Specification](./readme-sections-specification.md)).

## 3. Consistency Requirements

Interface signatures in the API documentation must be consistent with the actual code implementation; parameter naming must be consistent with the accuracy requirements of the [General Writing Specification](./general-writing-specification.md); for terminology, see the [Glossary](./glossary.md).

## Related Files

- Document responsibility boundaries are in the [Document Matrix](./document-matrix.md)
- The API design specification (how to design interfaces) is in the [API Design Specification](./api-design-specification.md)
- Document quality is dimension D12, see the [Review Dimension Matrix](./review-dimension-matrix.md)
