# Quality Metrics Specification

> What this file solves: Defines trackable quality metrics and their measurement criteria, avoiding the evaluation of project quality with unsubstantiated numbers.

## 1. Metric Principles

1. Metrics must be measurable and reproducible, with the collection method and measurement criteria explicitly documented.
2. Metrics are used for improvement, not for simple ranking or creating pressure.
3. Each metric must be annotated with a target value and a current value, and reviewed regularly.

## 2. Recommended Metrics

| Category | Metric | Description of Criteria |
| --- | --- | --- |
| Testing | Test coverage | Percentage of code lines covered by tests, with the statistics tool noted |
| Testing | Test pass rate | Number of passing cases / total number of cases |
| Build | Build success rate | Number of successful builds / total number of builds |
| Defects | Defect density | Number of defects found per unit of code size |
| Defects | Mean time to fix | Average elapsed time from discovery to completion of the fix |
| Performance | Response time | Scenario and percentile must be specified (e.g., P95) |
| Dependencies | Number of high-severity vulnerabilities | Number of unfixed high-severity dependency vulnerabilities |

## 3. Mandatory Rules

1. Performance metrics must state the test environment and method; unconditional numbers are prohibited (see [General Writing Specification](./general-writing-specification.md)).
2. Metric data collection must be automated to reduce manual statistical bias.
3. Metric anomalies must have follow-up records, incorporated into the [Roadmap Specification](./roadmap-specification.md) or issue tracking.

## Related Files

- For quality gates, see [Quality Gates](./quality-gate.md)
- For testing requirements, see [Testing Specification](./testing-specification.md)
- For how to write the performance section, see [README Section Specification](./readme-sections-specification.md)
