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

## 跨语种问题类型（`xcheck`）

以参考语种为基准，通过比对各语种索引页 `README.md` 的链接顺序建立篇目一一映射，逐篇比对以下七个轴：

| 类型 | 判定依据 | 是否自动修复 |
| --- | --- | --- |
| cross-heading | 标题（`#`~`######`）数量与参考语种不同 | 否 |
| cross-fence | 代码围栏数量不同 | 否 |
| cross-link | Markdown 链接数量不同（索引页允许目标比参考多 1，用于语言切换） | 否 |
| cross-ordered | 有序列表项数量不同 | 否 |
| cross-unordered | 无序列表项数量不同 | 否 |
| cross-table-rows | 表格数据行数不同 | 否 |
| cross-table-columns | 某张表格某行的列数与参考语种不同 | 否 |
| cross-placeholder | 占位符集合不同（按多重集比对，含名称与出现次数） | 否 |

映射建立阶段的错误（早于逐篇比对）：

| 类型 | 判定依据 | 是否自动修复 |
| --- | --- | --- |
| cross-missing-language | 目标语种目录 `locales/<lang>/` 不存在 | 否 |
| cross-no-reference | 参考语种索引页取不到任何规范链接，无法建立映射基准 | 否 |
| cross-index-count | 目标索引页的规范链接数与参考语种不同；命中后该语种不再逐篇比对 | 否 |
| cross-broken-index | 索引页列出了某篇，但该语种目录里没有这个文件 | 否 |
| cross-missing-reference | 参考语种索引列出了某篇，但参考语种目录里缺这个文件 | 否 |

注意：`cross-missing-reference` 是参考语种自身的完整性缺陷，因逐语种独立比对，同一个缺失会在 N 个语种上各报一条（12 语种时 11 条）。修复时应改参考语种的索引或文件，不要逐条改目标语种。

## 人工修正规则

1. `broken-link`：确认目标文件是否改名或跨语言路径是否写错；修正链接路径，不删除链接。
2. `orphan`：在相关规范或索引中补一条引用，说明该文件的使用场景；不删除孤立文件。
3. `index-count` / `index-declaration`：以磁盘文件数为准，统一域计数、表格条目与声明合计。
4. `unregistered-placeholder`：将占位符登记到对照表，写明含义、示例与是否必填；不得删除正文占位符。
5. `missing-purpose` / `missing-related`：在文件开头补职责句、结尾补相关文件区，保持一文件一职责。
6. `cross-placeholder`：**占位符名称必须与参考语种逐字一致**，不得本地化、音译或意译；仅占位符之外的说明文字可翻译。定位时按出现顺序对齐，不可全文按序批量替换——同名占位符在译文中被合并或拆分会导致错位。
7. 其余 `cross-*`：以参考语种为结构基准补齐或删除多余标题、列表项、表格行列；不得为凑数添加无实质内容的条目。

## 修复后复验

每次修复后重新执行 `check` 与 `xcheck`，要求问题数均为零；若仍有残留，按问题类型逐条人工核对。
