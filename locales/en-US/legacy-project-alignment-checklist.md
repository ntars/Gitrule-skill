# Existing-Project Alignment Checklist

> What this file solves: when applying this specification set to an existing project, it provides an item-by-item checklist with judgement methods and pass criteria across metadata, file naming, section structure, bilingual synchronisation, links and release.

## 1. Scope

This checklist serves two situations:

1. Bringing an existing repository under this specification set for the first time;
2. Regression checking an already aligned repository after the specification set changes.

Run the groups in order: metadata, structure, then release. Do not start the next group before the current one passes; otherwise a bulk edit is performed on a wrong basis.

## 2. Checks

### 2.1 Metadata (see [Project Naming Specification](./project-naming-specification.md), section 5)

| ID | Check | Method | Pass criteria |
| --- | --- | --- | --- |
| A1 | Repository name | Compare against the naming formulas and character set | Lowercase kebab-case, 2–25 characters, no version or filler words |
| A2 | Bilingual merged description | Read the About section or `gh repo view --json description` | `national language \| English` with one space on each side of the pipe |
| A3 | Description length | Count characters per language | At most 120 characters each, 350 in total |
| A4 | Topics count and language | `gh repo view --json repositoryTopics` | Exactly 20, English only, lowercase, hyphenated |
| A5 | Topic coverage | Check the five categories: language, domain, form, ecosystem, scenario | All five covered, none contradicting the stack |

When the limit is exceeded, compress the English version first, then the Chinese one; delete modifiers and repeated qualifiers before merging synonymous phrasing.

### 2.2 File naming (see [Multilingual Specification](./multilingual-specification.md))

| ID | Check | Method | Pass criteria |
| --- | --- | --- | --- |
| B1 | Primary README names | List the directory | `README.md` for Chinese, `README_EN.md` for English |
| B2 | Other languages | List the directory | `README_<UPPERCASE LANGUAGE>.md`, e.g. `README_JA.md` |
| B3 | No legacy names | Search the repository | No `README.en.md` or `README.ja.md` remains |
| B4 | References updated | Search for old names | Navigation links, tree examples and script allow-lists updated |
| B5 | Language switch | Open the first line of each version | Every version can switch to all the others |

Rename with `git mv` to keep history. In-repository scripts (preflight, packaging, documentation checks) often hold filename strings as allow-lists; update them or the post-push check fails.

### 2.3 Section structure (see [README Sections Specification](./readme-sections-specification.md))

| ID | Check | Method | Pass criteria |
| --- | --- | --- | --- |
| C1 | All sections present | Extract level-2 headings and compare with the 20-section list | All 20 exist |
| C2 | Section names | Compare wording item by item | Matches the specification; no variants such as "Highlights" or "Design Details and Small Decisions" |
| C3 | Section order | Compare sequence | Matches the specification |
| C4 | Extra sections | Look for additions | Extra content appears as appendices after the 20 sections |
| C5 | Language parity | Compare counts and order of level-2 headings | One-to-one correspondence |

Where an existing section name deviates, rename it to the specification wording; when the section holds substantial content, rename rather than rewrite.

### 2.4 Bilingual synchronisation (see [Multilingual Specification](./multilingual-specification.md))

| ID | Check | Method | Pass criteria |
| --- | --- | --- | --- |
| D1 | Same version | Search version strings | Both languages state the same version and status |
| D2 | Same numbers | Compare feature, test and platform counts | Identical values |
| D3 | Same links | Compare relative link sets | Both point to the same files |
| D4 | Same terminology | Spot-check technical terms | One translation per concept |
| D5 | Same structure | Compare table and list counts | Equal counts per section |

After a factual change in one language, update the other in the same commit; never defer translation to a later commit.

### 2.5 Links and content (see [General Writing Specification](./general-writing-specification.md))

| ID | Check | Method | Pass criteria |
| --- | --- | --- | --- |
| E1 | Relative links resolve | Resolve each link and test file existence | Zero broken links |
| E2 | Code fence language | Inspect fences | All labelled; no bare fences |
| E3 | Table columns | Compare separator and data rows | Consistent column counts |
| E4 | Prohibited expressions | Search colloquialisms, exclamation marks, ellipses, emoji | No hits; quotations must be quoted and attributed |
| E5 | Unverified figures | Search performance numbers | Every number carries test environment and method |
| E6 | Promissory wording | Search "guarantee", "permanent", "fully" | Technical qualifiers may stay; promises to users must be removed |

### 2.6 Community files and release (see [Document Matrix](./document-matrix.md), [Push and Release Specification](./push-and-release-specification.md))

| ID | Check | Method | Pass criteria |
| --- | --- | --- | --- |
| F1 | Required files | List the directory | `LICENSE`, `NOTICE`, `CONTRIBUTING.md`, `SECURITY.md` all present |
| F2 | Licence and NOTICE agree | Compare the routing table | Directory-level licences match NOTICE |
| F3 | Ignore rules | Inspect `.gitignore` | Build output, dependencies, `.DS_Store`, `.workbuddy/` ignored |
| F4 | Commit messages | Read `git log` | Match `<type>(<scope>): <subject>` |
| F5 | Remote in sync | Compare local `HEAD` with `origin/main` | Identical, working tree clean |

## 3. Additional checks for multilingual repositories

For repositories with three or more languages, add:

1. **Section titles per language**: every language carries all 20 sections with the same meaning as the Chinese or English baseline;
2. **Equal table rows**: project lists, status tables and parameter tables have the same row count in every language;
3. **Shared glossary**: one glossary file referenced by all versions.

## 4. Common errors and handling

| Error | Symptom | Handling |
| --- | --- | --- |
| Chinese numerals mis-parsed in bulk renumbering | "十、" read as "二十、", overwriting chapter 10 with chapter 20's title | Replace explicit old strings with new ones and assert every hit before writing |
| Link path changed, display text not | Link works, prose still names the old chapter | Search old chapter names and update text and path together |
| Renamed file, scripts untouched | Local documentation fine, post-push check fails | Search every filename string, including scripts, configs and doc examples |
| Only one language updated | The two versions disagree on facts | Use the repository state as truth; update the primary version, then the other in the same commit |
| Index not updated | New file is an orphan | Update index counts and entries immediately, then re-add domain counts |
| Description and body disagree | About says seven projects, body says nine | Update the description from the body and note it in the commit message |

## 5. Acceptance record template

```text
Repository: {{仓库名}}
Date: {{日期}}
Specification version: {{版本或提交号}}

Metadata: A1 {{通过/不通过}} A2 {{通过/不通过}} A3 {{通过/不通过}} A4 {{通过/不通过}} A5 {{通过/不通过}}
File naming: B1 {{ }} B2 {{ }} B3 {{ }} B4 {{ }} B5 {{ }}
Section structure: C1 {{ }} C2 {{ }} C3 {{ }} C4 {{ }} C5 {{ }}
Bilingual: D1 {{ }} D2 {{ }} D3 {{ }} D4 {{ }} D5 {{ }}
Links and content: E1 {{ }} E2 {{ }} E3 {{ }} E4 {{ }} E5 {{ }} E6 {{ }}
Community and release: F1 {{ }} F2 {{ }} F3 {{ }} F4 {{ }} F5 {{ }}

Failures and handling: {{逐条列出}}
Release conclusion: {{通过 / 有条件通过 / 阻断}}
```

## 6. Field definitions

| Field | Meaning | Values |
| --- | --- | --- |
| Repository | Full repository name under check | `owner/repository` |
| Specification version | State of the specification set used | Commit or version |
| Pass | Whether the item meets the criteria | Boolean |
| Release conclusion | Disposition of the result | Pass / conditional pass / blocked |

## Related Files

- Naming and metadata: [Project Naming Specification](./project-naming-specification.md)
- Section list: [README Sections Specification](./readme-sections-specification.md)
- Bilingual rules: [Multilingual Specification](./multilingual-specification.md)
- Writing and prohibited expressions: [General Writing Specification](./general-writing-specification.md)
- Release actions: [Push and Release Specification](./push-and-release-specification.md)
