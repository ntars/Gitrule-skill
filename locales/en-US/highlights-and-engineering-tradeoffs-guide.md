# Highlights and Engineering Trade-offs Writing Guide

> What this file solves: Defines how to write the two README sections "Core Highlights" and "Design Details and Engineering Trade-offs", giving a five-part structure for highlights and ten mandatory coverage categories for engineering trade-offs respectively.

## 1. Core Highlights Writing

Each highlight is written in the following five-part structure; missing any part disqualifies it from being listed as a highlight.

1. **Highlight name**: no more than 15 characters, using a noun phrase.
2. **Value**: the specific problem solved, and the consequence if it is not solved.
3. **Implementation method**: the technology, mechanism, or algorithm used, indicating the key file or function.
4. **Differentiation**: the comparison dimension against common solutions, which must be an objectively judgeable dimension.
5. **Evidence**: test data, benchmark results, code location, configuration items, or reproducible steps.

Constraints:

1. Evidence must be reproducible; a highlight for which evidence cannot be provided is marked "【To be supplemented: verification method】" and must not be replaced with a qualitative description.
2. Performance-related evidence must state the test environment and test method.
3. The comparison target must be a named solution; vague references such as "traditional solutions" or "other tools" must not be used.

## 2. Design Details and Engineering Trade-offs Writing

Each item is written in three parts — "scenario → handling method → reason" — explaining why it was designed this way rather than with other solutions.

Mandatory coverage categories:

1. Exceptional inputs and boundary cases (empty values, overlong values, illegal characters, extreme values)
2. Timeout, retry, backoff, circuit-breaking, and degradation strategies
3. Cache levels, invalidation strategies, and protection against cache penetration and stampedes
4. Concurrency control, lock granularity, data consistency, and idempotency
5. Memory and storage optimization (batch processing, streaming reads/writes, compression)
6. Security measures (authentication, rate limiting, input validation, masking of sensitive information)
7. Interaction details (mis-touch prevention, secondary confirmation, reversibility, loading and empty states)
8. Basis for default parameter values
9. Backward compatibility and cross-platform adaptation strategies
10. Weak-network and offline handling, state recovery

## Related Files

- Corresponds to README chapters 4 and 5, see the [README Sections Specification](./readme-sections-specification.md)
- Performance data writing must comply with accuracy requirements, see the [General Writing Specification](./general-writing-specification.md)
- Highlight evidence and trade-off coverage belong to gates G4/G5, see [Quality Gates](./quality-gate.md)
