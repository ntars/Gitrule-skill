# Database Design Specification

> What this file solves: Defines design rules for database table structures, fields, indexes, and migrations, ensuring data consistency, evolvability, and traceability.

## 1. Naming Conventions

1. Table names and field names use a unified naming style with clear meaning.
2. Primary keys, foreign keys, and indexes follow a unified prefix rule for naming.
3. Reserved words and abbreviations must have explicit conventions to avoid ambiguity.

## 2. Field Design

1. Every field must clearly specify its type, nullability, default value, and meaning.
2. Time fields use a unified time zone and precision.
3. Precision-sensitive fields such as amounts use fixed-point types, not floating-point.
4. Status fields use explicit enumerations, with the meaning of each value noted.

## 3. Indexes and Constraints

1. Indexes are designed based on query scenarios; avoid over-indexing.
2. Data integrity is guaranteed through constraints, not by relying on application-layer validation.
3. Foreign keys and cascade rules must be explicitly declared.

## 4. Migration Management

1. Schema changes are managed through migration scripts, which are versioned and committed to the repository.
2. Migrations must be rollback-capable; breaking changes must provide a data migration plan.
3. Migration scripts must be validated in a test environment before being applied to production (see [Deployment and Rollback Specification](./deployment-and-rollback-specification.md)).

## 5. Security

1. Sensitive data must be stored encrypted or masked (see [Security and Privacy Specification](./security-and-privacy-specification.md)).
2. Database connection strings must not be committed to the repository (corresponding to hard rule H3).

## Related Files

- Sensitive information red lines: see [Security and Privacy Specification](./security-and-privacy-specification.md)
- Change management: see [Deployment and Rollback Specification](./deployment-and-rollback-specification.md)
- Position in the architecture: see [Architecture Design Document Specification](./architecture-design-document-specification.md)
