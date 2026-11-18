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

- The description shares the same origin as the repository name, ≤120 characters, using the pattern `<做什么> for <谁>`.
- 5–10 topics, all lowercase, joined with `-`, covering the three categories of language, domain, and form.

## Related Files

- Naming compliance is hard rule H1: see [Hard Rules](./hard-rules.md)
- Metadata review is dimension D10: see [Review Dimension Matrix](./review-dimension-matrix.md)
- The resulting document is `docs/naming.md`: see [Document Matrix](./document-matrix.md)
