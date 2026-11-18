# Gitrule 优化规则

## 问题类型与判定

| 类型 | 判定依据 | 是否自动修复 |
| --- | --- | --- |
| missing-purpose | 文件开头 600 字符内无「本文件解决什么问题」或「What this file solves」 | 否 |
| missing-related | 无「## 相关文件」或「## Related Files」 | 否 |
| bare-code-fence | 代码围栏开口未标注语言 | 是，补 `text` |
| unclosed-code-fence | 代码围栏未配对 | 否，需人工定位 |
| broken-link | 相对 Markdown 链接目标不存在 | 否 |
| orphan | 除索引外未被任何其他文档引用 | 否 |
| index-count | 索引域计数合计与表格条目数不一致 | 否 |
| index-declaration | 索引声明合计与表格条目数不一致 | 否 |
| unregistered-placeholder | README 模板正文占位符未登记到对照表 | 否 |

## 人工修正规则

1. `broken-link`：确认目标文件是否改名或跨语言路径是否写错；修正链接路径，不删除链接。
2. `orphan`：在相关规范或索引中补一条引用，说明该文件的使用场景；不删除孤立文件。
3. `index-count` / `index-declaration`：以磁盘文件数为准，统一域计数、表格条目与声明合计。
4. `unregistered-placeholder`：将占位符登记到对照表，写明含义、示例与是否必填；不得删除正文占位符。
5. `missing-purpose` / `missing-related`：在文件开头补职责句、结尾补相关文件区，保持一文件一职责。

## 修复后复验

每次修复后重新执行 `check`，要求问题数为零；若仍有残留，按问题类型逐条人工核对。
