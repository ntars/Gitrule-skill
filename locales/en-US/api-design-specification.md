# API Design Specification

> What this file solves: Defines consistency principles and conventions for interface design, ensuring APIs are easy to use, predictable, and evolvable.

## 1. Design Principles

1. Consistent naming: Use unified naming rules for similar resources and operations.
2. Predictability: Operations with the same semantics have the same structure.
3. Explicit over implicit: Default values, required fields, and error behavior must be explicit.
4. Backward compatibility: Changes should preserve compatibility first; breaking changes must be versioned (see [Version Management Specification](./version-management-specification.md)).

## 2. Required Conventions

1. **Naming**: Naming rules for resources, methods, and fields.
2. **Parameters**: Type, required/optional, default value, and value range.
3. **Errors**: Unified error structure, error codes, HTTP status, or equivalent mechanism.
4. **Pagination and filtering**: Conventions for pagination, sorting, and filtering in large-data scenarios.
5. **Idempotency**: Idempotency guarantees for write operations.
6. **Rate limiting and quotas**: Frequency limits and over-limit responses.
7. **Versioning**: API version strategy and evolution approach.

## 3. Mandatory Rules

1. Error responses must contain a locatable error code and explanation, without exposing internal implementation details.
2. Breaking changes must bump the version and provide a migration period (see [Changelog Specification](./changelog-specification.md)).
3. Interfaces must have corresponding documentation with complete fields (see [API Documentation Specification](./api-documentation-specification.md)).

## Related Files

- API reference documentation writing: see [API Documentation Specification](./api-documentation-specification.md)
- Security-related: see [Security and Privacy Specification](./security-and-privacy-specification.md)
- Error handling is an engineering trade-off: see [Features and Engineering Trade-offs Writing Guide](./features-and-engineering-tradeoffs-guide.md)
