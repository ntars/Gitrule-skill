# Project Naming Specification

> What this file solves: Defines hard rules for repository names — characters, case, word splitting, length, semantics, and more — along with the naming formula, conventional suffixes, lookup process, and accompanying metadata requirements.

## 1. Hard Rules

| Rule | Requirement | Counterexample |
| --- | --- | --- |
| Character set | Only `a-z`, `0-9`, `-` | `My_Proj`, `我的项目` |
| Case | All lowercase | `MyProject` |
| Word splitting | kebab-case, joined with `-` | `myproject`, `my_project` |
| Length | 2–25 characters | An excessively long concatenated name |
| Ending | A noun or ending with a morphological suffix | Ending with `-project`, `-test` |
| Version | No version number, year, or date | `tool-v2`, `app2024` |
| Non-informative words | `my`/`demo`/`test`/`new`/`tmp` are forbidden | `my-new-demo` |
| Uniqueness | Search once each on GitHub / npm / PyPI | Same name as a well-known library |
| Semantics | The name itself should read as "what it does" | `xyz`, `abc123` |

## 2. Naming Formula (Choose One of Four)

```text
<技术>-<对象>          vue-virtual-table      go-ratelimit
<对象>-<形态>          note-cli   image-api   config-loader
<动词>-<对象>          parse-markdown   sync-dotfiles
<领域>-<子领域>        web-ui-kit   data-pipeline
```

## 3. Conventional Suffixes

`-cli` command line / `-sdk` client library / `-api` `-server` server side / `-template` `-boilerplate` scaffolding / `-loader` `-parser` middleware / `-kit` component set / `-notes` `-guide` documentation / `dotfiles` configuration repository / `awesome-xxx` resource collection.

## 4. Naming Process

1. Write in one sentence "for whom the project solves what problem".
2. Take the core noun + form from that sentence and apply any formula from section 2.
3. Generate 3 candidates and check each for name collisions.
4. Choose the one that is most understandable without reading the README.
5. Do not write the Chinese name into the repository name; place it after the first-line title in the README.

## 5. Accompanying Metadata

### 5.1 Repository Description

- Shares the same origin as the repository name, using the pattern `<what it does> for <whom>`.
- Bilingual merged format: `national language | English` — write the national-language version first, then a half-width vertical bar with one space on each side, then the English version. Example for a Chinese project:

```text
轻量级 Go 命令行 JSON 处理工具 | A lightweight Go CLI for JSON processing
```

- Length: the national language and English versions are each no more than 120 characters, with a combined total of no more than 350 characters (GitHub limit).
- Trade-off when the combined total exceeds the limit: compress the English version first rather than the national-language version — Chinese carries higher information density, so trimming it loses more meaning; when compressing, first drop modifiers and repeated qualifiers, then merge synonymous phrasing, and finally keep an intact subject–predicate structure in both language versions.
- No line breaks, Markdown syntax, or emoji; end-of-sentence punctuation style must be consistent across the two languages (either always or never).

### 5.2 Topics

- Fill all 20 slots (GitHub limit) for full coverage; never leave empty slots.
- English only — Chinese or any other language is forbidden; all lowercase, joined with `-`, no spaces or special characters.
- Fully cover five categories — language, domain, form, ecosystem, and scenario — optionally with generic terms such as `documentation` and `open-source`.
- Set them at repository creation and never leave them empty; re-verify after a repository rename or repositioning.

## Related Files

- Naming compliance is hard rule H1: see [Hard Rules](./hard-rules.md)
- Metadata review is dimension D10: see [Review Dimension Matrix](./review-dimension-matrix.md)
- The resulting document is `docs/naming.md`: see [Document Matrix](./document-matrix.md)
