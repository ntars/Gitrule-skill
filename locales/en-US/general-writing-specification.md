# General Writing Specification

> What this file solves: Defines the register, accuracy, terminology consistency, formatting details, and prohibited content for all deliverable documents, ensuring expressions are precise, unambiguous, and reproducible.

## 1. Register

1. Use formal written language, with declarative and imperative sentences.
2. Do not use colloquial expressions, such as "咱们" (let's), "超简单" (super simple), "搞定" (got it done), "贼快" (super fast), or "一键起飞" (one-click takeoff).
3. Do not use exclamation marks, ellipses, internet abbreviations, or emoji.
4. Do not use rhetorical questions as the opening of a section.

## 2. Accuracy

1. Every sentence must express a complete meaning and must not rely on context for inference.
2. Do not use vague references such as "它" (it), "这个" (this), "相关" (related), "一些" (some), or "若干" (several); when reference is necessary, use the full noun.
3. Times, version numbers, paths, commands, function names, and configuration key names must be precise and consistent with the actual situation of the project.
4. Commands must be directly executable and include the necessary current working directory description.
5. When version numbers are involved, the version constraint semantics must be stated, for example `>=1.2.0 <2.0.0`.

## 3. Terminology Consistency

1. When a term first appears, give its definition in the format "Chinese term (English Term, Abbreviation)".
2. Only one expression is used for the same concept throughout the document, and terminology corresponds one-to-one between the Chinese and English versions.
3. A Chinese-English terminology mapping table must be maintained, placed in the README appendix or a separate file, with both language versions sharing the same mapping table (see the [Information Collection and Templates](./information-collection-and-templates.md) for the template).

## 4. Formatting Specification

1. Heading levels start from `##` (`#` is reserved for the project name), and levels must not be skipped.
2. Each second-level heading corresponds to one section specified in the [README Sections Specification](./readme-sections-specification.md), and the order must not be changed.
3. Tables must have a header row with a consistent number of columns; commands, paths, code, and configuration key names use inline code marks.
4. Code blocks must be marked with a language identifier, and multi-line commands must be copyable and executable as a whole.
5. External links use full URLs, not shortened links; internal jumps use relative path anchors.
6. Add a space between Chinese and English or digits; do not mix Chinese and English punctuation.

## 5. Placeholder Conventions

1. Formal placeholders in copy-ready templates are uniformly written as `{{纯名}}`, for example `{{仓库地址}}`; the name must not contain conjunctions expressing a choice among alternatives such as "or" or ",", and must not be written as a sentence of explanatory text.
2. Formal placeholders must be registered in the placeholder mapping table of the template to which they belong; the registration entry includes meaning, example, and whether it is required.
3. Natural-language brace content in specification examples or filling prompts is for illustration only, does not count as a formal placeholder, and is not included in the mapping table; when generating the final document it must all be replaced with actual content.
4. Nested braces, backticks, or a second placeholder must not be used as a placeholder name.
5. When translating, placeholder names must match the source language verbatim; they must not be localized, transliterated, or paraphrased. Only explanatory text outside the placeholders may be translated. A placeholder is the anchor for template substitution; once its name is translated, cross-language mapping and batch replacement break down.

## 6. Prohibition List

The following must not appear: unverified performance numbers, comparison conclusions without sources, commitment-style statements (such as "guaranteed compatible with all environments" or "free forever"), disparaging descriptions of third-party projects, and promotional content unrelated to the project.

## Related Files

- Section structure is in the [README Sections Specification](./readme-sections-specification.md)
- Bilingual terminology correspondence is in the [Multilingual Specification](./multilingual-specification.md)
- Quality determination G1 (colloquialism and ambiguity) is in [Quality Gates](./quality-gate.md)
