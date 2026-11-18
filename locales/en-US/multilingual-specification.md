# Multilingual Specification

> What this file solves: Defines the file layout organized by language code directories, language switching, translation consistency, code consistency, and the rules for synchronizing one-sided modifications.

## 1. Directory Layout

1. The `README.md` in the repository root serves only as the project front page and language navigation, and does not carry the body text of specific specifications.
2. Specific specifications are laid out flat in `locales/<language-code>/` directories by language code, for example `locales/zh-CN/角色与职责.md` and `locales/en-US/roles-and-responsibilities.md`.
3. Language codes follow the BCP 47 style, for example `zh-CN`, `en-US`, `ja-JP`, `ko-KR`; the language code appears only in the directory name and is never embedded in file names.
4. **File names must use the language itself**: the Chinese directory uses Chinese file names (`角色与职责.md`), the English directory uses lowercase hyphenated English file names (`roles-and-responsibilities.md`), and other languages follow the same rule; Chinese file names must not be reused in non-Chinese directories.
5. File names across language directories are not required to match character by character, but they must map one to one: the same specification has the same responsibility in every language directory, and the mapping is recorded in the `paths` field of the manifest (see [Machine-Readable Metadata Specification](./machine-readable-metadata-specification.md)).
6. Simplified Chinese and English are the first completed versions; other languages are marked "to be supplemented" or "completed" in the language table of the root `README.md`, and languages without an established directory must not provide empty links.
7. Adding a language only requires creating the corresponding language directory and translating each document, without modifying existing language files; other completed languages are updated only when a source-language revision needs to be synchronized.

## 2. Language Switching

1. The top of the `README.md` in each language directory must provide language switch links.
2. Links use paths relative to the current language directory, for example, in the Simplified Chinese directory:
   `[English](../en-US/README.md) | [简体中文](./README.md)`.
3. Link text uses the endonym of the target language, such as `English`, `简体中文`, `日本語`, not abbreviations such as `CN` or `EN`.
4. Switch links point only to established language directories; unestablished language directories are uniformly marked by the language table in the root `README.md`, and no broken links are left in the body text.

## 3. Translation Consistency

1. A translation must be a complete translation; the number of sections, section order, number of table columns, and number of code blocks must match the source language; summary-style or unproofread machine-translation output must not be provided.
2. Commands, paths, configuration key names, placeholder names, and parameter values inside code blocks remain unchanged; only comments and explanatory text are translated.
3. Terminology is unified according to the Chinese-English terminology mapping table in the [Information Collection and Templates](./information-collection-and-templates.md); the same concept uses the same correspondence in all languages.
4. Any one-sided modification must be synchronized to all completed languages, and the synchronized language codes and versions recorded in the changelog; a revision must not be judged complete until synchronization is finished.
5. Consistency checking belongs to gate G10, see [Quality Gates](./quality-gate.md).

## 4. Legal Text

1. NOTICE is provided in Chinese by default; legal text involving original license text, copyright notices, and disclaimers retains the original English text and is neither translated nor rewritten.
2. Legal text requiring Chinese-English comparison must display the original and the translation side by side, marked "the translation is for reference only; the original text prevails".
3. The language handling of legal text is in the [NOTICE Specification](./notice-specification.md) and the [Disclaimer](./disclaimer.md).

## Related Files

- Root language navigation: [Repository Front Page](../../README.md)
- Language list and stable identifiers: [Machine-Readable Metadata Specification](./machine-readable-metadata-specification.md)
- Section count and order are based on the 20 sections of the [README Sections Specification](./readme-sections-specification.md)
- The terminology mapping table template is in the [Information Collection and Templates](./information-collection-and-templates.md)
- Writing standards are in the [General Writing Specification](./general-writing-specification.md)
- Bilingual synchronization belongs to gate G10, see [Quality Gates](./quality-gate.md)
