# Machine-Readable Metadata Specification

> What this file solves: Defines the manifest structure of metadata consumed programmatically by experts, Skills, MCP, command line tools, and so on, ensuring stable machine access and discoverability.

## 1. Design Goals

1. Stable identifiers: Each document has a unique, immutable identifier for programmatic reference.
2. Language-independent: Identifiers do not change with language; language is reflected only in paths.
3. Discoverable: The manifest lists the type, path, language, and summary of every document.

## 2. Manifest Structure

A machine manifest must contain:

| Field | Requirement |
| --- | --- |
| id | Stable unique identifier, lowercase kebab-case, containing no language or version |
| title | Document title |
| summary | One sentence describing what problem it solves |
| domain | The domain it belongs to (one of the seven domains) |
| paths | Mapping from language code to relative path, e.g. `zh-CN`: `./locales/zh-CN/角色与职责.md` |
| version | Specification set version |

## 3. Mandatory Rules

1. Adding a language only appends a mapping in `paths`; do not change `id` or the paths of other languages.
2. Renaming a document must keep `id` unchanged and only update `paths`.
3. Identifiers and paths must match the actual files; CI validates the manifest's validity.
4. This specification provides a copyable manifest example; the target project should create an actual manifest instance using the fields in Section 2 and ensure that `paths` match the files on disk.

## 4. Manifest Example (Copyable)

The following example lists three document entries. An actual manifest must cover all specifications in the target language directories; `id` does not change with language, and `paths` are appended by language code.

```json
{
  "version": "1.0.0",
  "entries": [
    {
      "id": "role-and-responsibility",
      "title": "角色与职责",
      "summary": "定义执行者身份、职责边界、触发条件、适用范围与硬性约束",
      "domain": "总纲与治理",
      "paths": {
        "zh-CN": "./locales/zh-CN/角色与职责.md"
      },
      "version": "1.0.0"
    },
    {
      "id": "readme-standard-template",
      "title": "README标准模板",
      "summary": "提供可直接套用的通用 README 模板与占位符对照表",
      "domain": "命名与文档",
      "paths": {
        "zh-CN": "./locales/zh-CN/README标准模板.md"
      },
      "version": "1.0.0"
    },
    {
      "id": "machine-readable-metadata",
      "title": "机器可读元数据规范",
      "summary": "定义供专家、Skill、MCP、命令行消费的元数据清单结构",
      "domain": "AI 与机器适配",
      "paths": {
        "zh-CN": "./locales/zh-CN/机器可读元数据规范.md"
      },
      "version": "1.0.0"
    }
  ]
}
```

When adding a language, append a mapping only in the corresponding entry's `paths`, for example `"en-US": "./locales/en-US/role-and-responsibility.md"`; do not modify `id`.

## Related Files

- How Skills consume metadata: [Skill Authoring Specification](./skill-authoring-specification.md)
- How MCP tools expose documents: [MCP Tool Specification](./mcp-tool-specification.md)
- Agent invocation conventions: [Agent Invocation and Prompt Specification](./agent-invocation-and-prompt-specification.md)
