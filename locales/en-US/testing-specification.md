# Testing Specification

> What this file solves: Defines test layering, templates and fields for test plans and cases, coverage criteria, and execution standards, ensuring every requirement is verifiable and every change is regression-testable.

## 1. Specification Clauses

1. Testing is divided into three layers: unit, integration, and end-to-end; each layer must state the object under test and the out-of-scope items to avoid duplicate coverage.
2. Every "must"-level requirement must have at least one corresponding test case; see [Requirements Traceability Matrix Specification](./requirements-traceability-matrix-specification.md) for the traceability relationship.
3. Defect fixes must first add a regression case, then change the code; the regression case must be able to reproduce the original defect.
4. Coverage thresholds are set per project and written into CI, and must not fall below the established threshold (corresponding to hard rule H9).
5. Tests must be repeatable and free of external state dependencies; those depending on external services must be isolated or mocked.
6. Test names must express the behavior under test and the expected result; tests, lint, format, and type checking must run automatically in CI, and only a fully green CI allows merging (see [Code Review Specification](./code-review-specification.md)).

## 2. Test Layering

| Layer | Object under test | Must cover | Not covered | Typical tools |
| --- | --- | --- | --- | --- |
| Unit test | Functions, pure logic modules | Core logic, boundary conditions, exception branches | Cross-module collaboration, external I/O | Language built-in runner |
| Integration test | Inter-module collaboration | Key call chains, adapters, persistence interactions | Complete user flows | Test container / mock server |
| End-to-end test | Complete user scenarios | Main usage paths, key business loops | Exhaustive branches, performance stress testing | Browser / CLI driver |

## 3. Test Plan Template

```markdown
# Test Plan: {{项目名称}} {{版本号}}

Version: {{v1.0}} ｜ Corresponding requirement scope: {{REQ-001 ~ REQ-020}} ｜ Owner: {{姓名}}

## Test Scope
- Included: {{模块 / 需求编号列表}}
- Excluded: {{不在本期验证的范围及原因}}
- Related project success criteria: {{G1 / G2}}

## Layering Strategy
| Layer | Object under test | Coverage target | Tool | Execution timing |
| --- | --- | --- | --- | --- |
| Unit | {{对象}} | {{覆盖率阈值}} | {{工具}} | Every commit |
| Integration | {{对象}} | {{关键链路清单}} | {{工具}} | Every merge |
| End-to-end | {{场景}} | {{主要路径清单}} | {{工具}} | Every release |

## Environment and Data
- Environment: {{操作系统 / 运行时版本 / 依赖服务版本}}
- Test data: {{构造方式；禁止使用生产敏感数据}}
- External dependencies: {{需 mock 的服务及隔离方式}}

## Entry and Exit Criteria
- Entry: {{进入测试的前置条件，如开发自测通过}}
- Exit: {{通过率 100%、无 P0/P1 缺陷、覆盖率达标}}
- Suspension conditions: {{阻塞性问题清单}}

## Risks and Trade-offs
- Untested scope and reasons: {{例如第三方付费接口以 mock 替代}}
- Known risks: {{例如并发场景仅做 10 路验证}}
```

## 4. Test Case Template

```markdown
### TC-{{三位序号}}: {{用例标题}}

- Related requirement: {{REQ-001}}
- Layer: {{单元 / 集成 / 端到端}}
- Priority: {{P0 / P1 / P2}}
- Type: {{正常 / 边界 / 异常}}
- Preconditions: {{环境与数据准备}}
- Steps and expected results:
  | Step | Operation | Expected result |
  | --- | --- | --- |
  | 1 | {{操作}} | {{可判定的结果}} |
  | 2 | {{操作}} | {{可判定的结果}} |
- Cleanup: {{恢复环境的操作；无则写「无」}}
```

## 5. Field Definitions

### 5.1 Test Plan Fields

| Field | Required | Type | Filling guidelines | Example |
| --- | --- | --- | --- | --- |
| Corresponding requirement scope | Yes | List | Use REQ number ranges | `REQ-001 ~ REQ-020` |
| Excluded scope | Yes | Text | State why it is not tested | `Paid API not tested: no test account` |
| Coverage target | Yes | Threshold | Coverage must be a numeric percentage | `Line coverage ≥80%` |
| Execution timing | Yes | Enum | Commit / Merge / Release | `Every merge` |
| Test data | Yes | Text | Declare the construction method; real sensitive data is forbidden | `Generated with fixtures` |
| Exit criteria | Yes | Text | Determinable, including defect severity threshold | `No open P0/P1 defects` |

### 5.2 Test Case Fields

| Field | Required | Type | Filling guidelines | Example |
| --- | --- | --- | --- | --- |
| Number | Yes | `TC-NNN` | Consecutive, not reused | `TC-007` |
| Related requirement | Yes | List | At least one REQ number | `REQ-001` |
| Priority | Yes | Enum | P0 / P1 / P2 | `P0` |
| Type | Yes | Enum | Normal / Boundary / Exception | `Boundary` |
| Steps and expected results | Yes | Table | Each step must have a determinable expectation | See template |
| Cleanup | Yes | Text | Write "None" if no cleanup; must not be left blank | `None` |

### 5.3 Coverage Criteria

| Criterion | Definition | Applicable layer | Recommended threshold |
| --- | --- | --- | --- |
| Line coverage | Executed statements / total statements | Unit | ≥80% |
| Branch coverage | Executed branches / total branches | Unit | ≥70% |
| Requirement coverage | "Must"-level requirements with test cases / total "must"-level requirements | All layers | 100% |
| Path coverage | Verified main paths / identified main paths | End-to-end | 100% |

Note on criteria: Coverage is a means of finding untested areas, not a quality goal in itself; high coverage does not replace assertion quality — assertions must verify behavior rather than merely execute code.

## 6. Filling Instructions

1. **Related requirement**: Must fill in a REQ number; cases that cannot be linked should be moved to exploratory testing records and excluded from the formal case set.
2. **Expected result**: Must be determinable. "Returns the correct result" is not acceptable; "returns status code 200 and the `name` field is non-empty" is acceptable.
3. **Type distribution**: Every "must"-level requirement needs at least one normal case and one boundary or exception case.
4. **Cleanup**: Cases involving files, databases, or global state must include cleanup steps; a case without cleanup is considered incomplete.
5. **Regression cases**: Defect fixes must be named with the defect ID as a prefix, e.g. `TC-007-regression-142`.
6. **Isolation**: Cases must not depend on execution order; shared state must be rebuilt in preconditions.

Common mistakes:

| Wrong wording | Problem | Correction |
| --- | --- | --- |
| Expected result written as "works normally" | Not determinable | Write a specific return value or state |
| Case without a related requirement | Traceability chain broken | Add a REQ number |
| Only testing the normal path | Boundary defects missed | Add exception and boundary cases |
| Case depends on the previous case's result | Not repeatable | Rebuild state in preconditions |
| Testing with production data | Privacy and compliance risk | Use fixtures instead |

## 7. Complete Example

```markdown
# Test Plan: markdown-lint-cli v1.0

Version: v1.0 ｜ Corresponding requirement scope: REQ-001 ~ REQ-014 ｜ Owner: Wang Wu

## Test Scope
- Included: Rule engine, CLI argument parsing, report output (REQ-001 ~ REQ-014)
- Excluded: Editor plugin integration (deferred to v1.1, no corresponding requirement)
- Related project success criteria: G1, G2

## Layering Strategy
| Layer | Object under test | Coverage target | Tool | Execution timing |
| --- | --- | --- | --- | --- |
| Unit | Rule functions | Line coverage ≥85% | Language built-in runner | Every commit |
| Integration | CLI → rule engine → report | 3 key chains | Test container | Every merge |
| End-to-end | Batch check of real repositories | 2 main paths | Shell driver | Every release |

### TC-001: Missing space between Chinese and English is detected
- Related requirement: REQ-001
- Layer: Unit
- Priority: P0
- Type: Boundary
- Preconditions: Load the `spacing` rule
- Steps and expected results:
  | Step | Operation | Expected result |
  | --- | --- | --- |
  | 1 | Input "使用Node.js开发" | Returns 1 hit, line 1 |
  | 2 | Input "使用 Node.js 开发" | Returns 0 hits |
- Cleanup: None
```

## Related Files

- Bidirectional traceability from requirements to cases: [Requirements Traceability Matrix Specification](./requirements-traceability-matrix-specification.md)
- Layering criteria and metric definitions: [Quality Metrics Specification](./quality-metrics-specification.md)
- Entry gate: [Quality Gate](./quality-gate.md)
- Review dimension D6: [Review Dimension Matrix](./review-dimension-matrix.md)
- CI automatic execution configuration: [CI Workflow Specification](./ci-workflow-specification.md)
- Local execution before push: [Push and Release Specification](./push-and-release-specification.md)
