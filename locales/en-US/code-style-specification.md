# Code Style Specification

> What this file solves: Defines code style configuration templates, naming convention tables, comment rules, and filling instructions to reduce style disputes and improve readability and review efficiency.

## 1. Specification Provisions

1. Style rules are governed by automated tools; humans handle only what tools cannot cover.
2. Formatting configuration must be committed with the repository (such as a formatting config file) to ensure consistency across environments.
3. CI must integrate format checks; if they fail, merging is not allowed (see [Testing Specification](./testing-specification.md)).
4. Do not use magic numbers or hard-coded constants; extract them into named constants.
5. Use LF uniformly for line endings and end files with a newline (corresponds to dimension D3, repository hygiene).

## 2. Style Configuration Template

```markdown
# Code Style Convention: {{项目名称}}

Config Version: {{v1.0}} ｜ Languages & Versions: {{如 TypeScript 5.x}} ｜ Formatter: {{如 Prettier 3.x}}

## Formatting Rules (Tool-Enforced)
| Rule | Value | Tool Config Key | Negotiable |
| --- | --- | --- | --- |
| Indentation | {{2 空格 / 4 空格 / Tab}} | {{配置项名}} | No |
| Line width | {{100 字符}} | {{配置项名}} | No |
| Quotes | {{单引号 / 双引号}} | {{配置项名}} | No |
| Line ending | LF | `endOfLine: lf` | No |
| Final newline | Required | Tool default | No |
| Semicolons | {{有 / 无}} | {{配置项名}} | No |

## Naming Conventions (Not Tool-Enforced, Manual Review)
| Object | Rule | Good Example | Bad Example |
| --- | --- | --- | --- |
| Variable | {{camelCase}} | `userName` | `UserName` |
| Constant | {{UPPER_SNAKE_CASE}} | `MAX_RETRY` | `maxRetry` |
| Function | {{动词开头 camelCase}} | `parseConfig` | `configParse` |
| Class / Type | {{PascalCase}} | `ConfigLoader` | `config_loader` |
| File name | {{kebab-case}} | `config-loader.ts` | `ConfigLoader.ts` |
| Boolean | {{is/has/can 前缀}} | `isValid` | `valid` |
| Collection | {{复数名词}} | `items` | `itemList` |

## Comment Rules
- Cases requiring comments: {{公开 API 的契约、非直观算法、绕开限制的临时方案}}
- Prohibited comments: {{复述代码、无信息量、失效的旧注释、情绪化表述}}
- Comment language: {{与项目主语言一致}}
- TODO format: `// TODO({{负责人}}): {{事项}} — {{计划版本}}`

## File Organization
1. Import order: {{标准库 → 第三方 → 本地模块，组内字典序}}
2. Declaration order: {{常量 → 类型 → 函数 → 导出}}
3. Maximum lines per file: {{300 行，超出须拆分}}

## Exception List
| Scenario | Exception Rule | Approver | Validity |
| --- | --- | --- | --- |
| {{如生成代码}} | {{不参与格式化}} | {{姓名}} | {{至 v2.0}} |
```

## 3. Configuration Field Definitions

| Field | Required | Type | Filling Notes | Example |
| --- | --- | --- | --- | --- |
| Config version | Yes | Text | Incremented when style rules change | `v1.0` |
| Languages & versions | Yes | Text | Specify the major version to avoid rule drift | `TypeScript 5.x` |
| Formatter | Yes | Text | Consistent with the version in the lockfile | `Prettier 3.2` |
| Rule value | Yes | Enum / Number | Must be unique; "it depends" is prohibited | `2 spaces` |
| Negotiable | Yes | Enum | No / Yes; "Yes" requires negotiation conditions | `No` |
| Naming good example | Yes | Code | Selected from existing project code | `parseConfig` |
| Naming bad example | Yes | Code | Must be a realistic, commonly mistaken form | `configParse` |
| TODO owner | Yes | Text | Writing "team" is prohibited | `Zhang San` |
| Exception validity | Yes | Version / Date | Must be reviewed on expiry | `Until v2.0` |

## 4. Filling Instructions

1. **Tools first**: All rules that can be enforced by tools must be written into the formatting configuration rather than relying on human memory; humans handle only naming, comments, and file organization.
2. **Line width value**: Must be set according to the review interface width, commonly 100 or 120; once determined, it must not be overridden in individual files.
3. **Naming good examples**: Select names that actually exist in the project's code; textbook-style placeholders are prohibited.
4. **Boolean naming**: `is`/`has`/`can` prefixes must match semantics; `isReady` must not represent an action.
5. **TODO**: Must include an owner, the item, and a planned version; TODOs without a plan must not enter the mainline.
6. **Exception list**: Each exception must have an approver and a validity period; it automatically expires if not reviewed by then.

Common mistakes:

| Incorrect Writing | Problem | Correction |
| --- | --- | --- |
| "Keep code as concise as possible" | Not determinable | Rewrite as a checkable rule, such as a function length limit |
| Naming table with rules but no bad examples | Cannot be referenced during review | Add realistic, commonly mistaken bad examples |
| Comment saying "there was a bug here before" | Uninformative and easily outdated | Rewrite to explain the current behavior and reason |
| TODO without an owner | No one follows up | Add an owner and planned version |
| Exception without a validity period | Permanent exemption | Add a validity period and reviewer |

## 5. Complete Example

```markdown
# Code Style Convention: markdown-lint-cli

Config Version: v1.0 ｜ Languages & Versions: TypeScript 5.x ｜ Formatter: Prettier 3.2

## Formatting Rules (Tool-Enforced)
| Rule | Value | Tool Config Key | Negotiable |
| --- | --- | --- | --- |
| Indentation | 2 spaces | `tabWidth: 2` | No |
| Line width | 100 characters | `printWidth: 100` | No |
| Quotes | Single quotes | `singleQuote: true` | No |
| Line ending | LF | `endOfLine: lf` | No |
| Semicolons | Yes | `semi: true` | No |

## Naming Conventions (Manual Review)
| Object | Rule | Good Example | Bad Example |
| --- | --- | --- | --- |
| Function | Verb-first camelCase | `parseRules` | `rulesParser` |
| Constant | UPPER_SNAKE_CASE | `DEFAULT_RULES` | `defaultRules` |
| File name | kebab-case | `rule-loader.ts` | `RuleLoader.ts` |

## Comment Rules
- Cases requiring comments: Matching semantics of rules, workarounds for upstream API behavior.
- Prohibited comments: Restating code, "fixed a bug", TODOs without an owner.
- TODO format: `// TODO(Wang Wu): Replace the temporary parser — v2.0`

## Exception List
| Scenario | Exception Rule | Approver | Validity |
| --- | --- | --- | --- |
| fixtures directory | Not formatted | Li Si | Until v2.0 |
```

## Related Files

- Basis for code review checks: [Code Review Specification](./code-review-specification.md)
- Format checks run in CI: [Testing Specification](./testing-specification.md), [CI Workflow Specification](./ci-workflow-specification.md)
- Repository hygiene belongs to dimension D3: [Audit Dimension Matrix](./review-dimension-matrix.md)
- Pre-push checks: [Push and Release Specification](./push-and-release-specification.md)
- Requirements-to-implementation traceability: [Requirements Traceability Matrix Specification](./requirements-traceability-matrix-specification.md)
