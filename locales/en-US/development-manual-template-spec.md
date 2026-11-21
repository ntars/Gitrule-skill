# Development Manual Template Specification

> What this file solves: Defines the skeleton of a "cloud-authored, locally executed" two-phase development manual, the task card format, the handoff protocol, and the validation gates, so that a single idea can be transcribed by a cloud model into unambiguous task cards and executed part by part, in relay, by a local coding model.

## 1. Positioning and Workflow

1. This specification targets a division of labor between "one cloud reasoning model + one local coding model": the cloud transcribes vague ideas into an explicit plan, and the local model executes that plan deterministically.
2. The workflow is fixed at four steps, and none may be skipped:
   - Upfront verification: check whether the idea contains faulty premises, logical jumps, or missing information; if information is insufficient, ask the user first — no guesswork is allowed.
   - Cloud authoring: scan open-source solutions per the rules in Section 9 and fill in the manual.
   - User review: focus the review on acceptance commands, adoption records, and forbidden zones.
   - Local execution: inject the relevant chapters and handoff records per the machine-readable index, and execute part by part.
3. The manual body must not contain vague words such as "etc.", "related", "appropriate", "as much as possible", or "when necessary"; every instance must either give a precise value or a decision rule.

## 2. Manual Skeleton

Every development manual contains the following sections in a fixed, unchanging order:

| Section | Responsibility |
| --- | --- |
| Machine-readable index | A navigation table of chapter paths, corresponding code directories, acceptance commands, and phase markers |
| Adoption record | The open-source supply-chain record table, the single source of truth for the whole project (see Section 11) |
| Project constitution | Whole-project invariants, injected into every part |
| Glossary | Terms with plain-language explanations and their mapping to the code |
| Module chapters | One chapter per module, written per the Section 4 structure |
| Release chapter | Build and distribution rules; release actions require user confirmation |
| Website copy chapter | Copy rules aimed at ordinary users; not injected into the local model |
| Change log | Date, chapter, change, and decision owner |

## 3. Project Constitution

The project constitution is the set of invariants injected into every locally executed part; it always contains exactly five items:

1. Tech stack and versions: precise down to the version number.
2. Directory structure convention: a tree diagram plus a one-sentence responsibility for each directory.
3. Coding standards: tailored to the project type, with the baseline being modular on-demand loading, minimal and direct code, no features beyond what was asked, complete comments, and technical concepts explained in plain language; interface-facing projects follow the Apple HIG, font sizes use only px or rem, and rpx is prohibited.
4. Global forbidden zone: things that are absolutely off-limits, for example introducing dependencies not present in the adoption record, or modifying contract files.
5. Output language rule: explanations, logs, progress messages, and error messages are written in Simplified Chinese; code, commands, file paths, and proper nouns may keep their original form.

## 4. Module Chapter Structure

Every module chapter contains exactly nine sections in a fixed, unchanging order:

| Section | Responsibility |
| --- | --- |
| Module responsibility | 1-3 sentences stating clearly what it does and what it does not do |
| Open-source solutions used | Name, purpose, and adoption record ID |
| File list | Path, action (create/modify/read-only), and responsibility; the total must not exceed 10 files, otherwise split the chapter |
| Interface contracts | Signatures, routes, and protocol fields precise to their types, with complete input/output samples attached |
| Data and state | What is stored, where, and in what format; technical concepts annotated in plain language |
| Dependencies | Three file lists: must read first, will call, and must never modify |
| Task cards | The parts the module is split into; each card executes independently |
| Chapter forbidden zone | Things this module specifically must not do |
| Design notes | Rationale for choices, rejected alternatives, and the distinction between fact and speculation; not injected into the local model |

## 5. Task Card Format

One task card equals one local session equals one acceptance command. The fields are fixed:

| Field | Requirement |
| --- | --- |
| Goal | One sentence, machine-verifiable |
| Preconditions | The preceding part and all files it depends on already exist |
| Steps | Listed by number, each step a single deterministic action, completed in one pass with no interruptions and no follow-up questions |
| Acceptance command | Copy-and-run ready; when no acceptance system exists yet, the first card must build the acceptance command first |
| Expected result | Exact output, exit code, or assertion count |
| Failure handling | Handling for each typical error, item by item; after 3 consecutive failures the card must stop and write a handoff record |
| Handoff requirements | Declares which fields must be written into the handoff record |

Hard constraints:

1. If a card touches more than 10 files, split the card; if a chapter exceeds 6 cards, split the chapter.
2. Any card involving delivery self-checks must explicitly list redundant-code cleanup and the README, NOTICE, and LICENSE sync points.
3. Actions that delete or overwrite files must always stop, be written to the block field of the handoff record, and wait for user confirmation.
4. A task too vague to write an acceptance command for must not fill in a card; mark it separately as "requires user decision".

## 6. PROGRESS Handoff Protocol

The handoff record file PROGRESS.md is the single source of truth between parts, in a fixed format:

| Field | Requirement |
| --- | --- |
| done | Whether this card's goal was achieved |
| files | The list of files actually changed |
| decisions | Decisions made along the way, in the form "chose A because B" |
| next | The next card's number and entry point, written down to the file path and entry function; "keep improving" is not allowed |
| block | Unresolved issues; leave empty if none |

1. Every card must append one entry when it finishes; the format must not change.
2. During local execution, only the latest entry is injected; historical entries are not injected.
3. Resuming from a breakpoint: on receiving a "continue" instruction, first read the latest entry to confirm the breakpoint, then proceed from the entry point that next points to; redoing completed steps from memory or guesswork is prohibited.

## 7. Local Injection Budget

The harness assembles each part's context per the table below, with a total budget of no more than 24K (75% of a 32K working window):

| Injected item | Budget |
| --- | --- |
| Project constitution | 2-3K |
| The chapter owning the current task card | 2-5K |
| Latest handoff record entry | about 0.5K |
| Handoff prompt skeleton | about 0.3K |
| Code and tool output | remaining budget |

Not injected: the full adoption record table (only the entries involved in the current card are injected), design notes, and the website copy chapter.

## 8. Handoff Prompt Iron Rules

Every part opens with a fixed injected preamble; the iron rules are fixed at six:

1. Output in Simplified Chinese throughout; code, commands, paths, and proper nouns may keep their original form.
2. Do only what the task card says; add no features, configuration, or extensions beyond what was asked.
3. No inventing or fabricating; if an API signature is uncertain, state the uncertainty directly; fact and speculation are always explicitly distinguished.
4. When an acceptance command fails, follow the card's failure handling; altering the acceptance criteria on your own is not allowed.
5. Actions involving file deletion or overwrite must always stop and wait for user confirmation.
6. When done, write the handoff record exactly per the handoff requirements, then stop.

## 9. Cloud Authoring Rules

Before filling in the manual, the cloud model completes two upfront tasks, then fills in chapter by chapter:

1. Premise verification: check for faulty premises, logical jumps, and missing information; ask the user first when anything is insufficient.
2. Open-source solution scan: search the open-source ecosystem for ready-made solutions; scan before filling, prefer mature solutions over reinventing the wheel, and register the results in the adoption record.

While filling in the manual, follow these rules:

1. Eliminate every vague word; give a precise value or a decision rule for every instance.
2. Design decisions go into the design notes, including the rationale for choices and rejected alternatives, for user review; they are not injected into the local model.
3. Instructions for the local model are written assuming "it knows nothing about the project background"; all premises are spelled out explicitly.
4. Compliance baseline: mark licenses that are unclear as "pending confirmation"; mark strong-copyleft solutions with a notice of derivative obligations; modified open-source code retains its original copyright and a modification note; adopted items must keep README, README_EN, NOTICE, and LICENSE in sync, with the sync written as an explicit step and acceptance content of the corresponding task card.
5. Documentation format rules reference the corresponding specifications in this repository; do not copy specification text into the manual.

## 10. Phase Status and Working Window

Every chapter in the machine-readable index carries a phase marker, which adjusts the local working window:

| Phase | Characteristics | Working window |
| --- | --- | --- |
| Greenfield | Implement against a frozen contract | 16-24K |
| Growth | Cross-module features, the default tier | 32K |
| Maintenance | Refactoring and cross-module troubleshooting | 48-64K, with parallelism reduced accordingly |

Maintenance-phase chapters must additionally attach a troubleshooting guide with three columns: symptom, likely location, and verification command.

## 11. Adoption Record, Release, and Website Copy

1. The adoption record table has fixed fields: name, category, version, purpose, license, copyright holder, official address, modified or not, modification notes, declaration method, and adoption status; adoption status comes in three tiers: "ready to adopt", "needs evaluation", and "currently unavailable".
2. The release chapter covers build scripts, the CI matrix, checksums, and signing environment variable templates; the release card's acceptance command is the build artifact check; public release actions do not enter the local model and are executed only after user confirmation.
3. The website copy chapter targets ordinary users: code, command lines, technical jargon, and empty words are prohibited; the structure is hero positioning, pain points, highlights, trust, download, scenario stories, and FAQ; the tone is calm and restrained.

## 12. Cross-Project Reference and Validation

1. When a target project references this specification, read the full text via `gitrule spec` and copy the manual skeleton as the initial skeleton of the project's own manual; this specification is not revised along with the project, and the project manual's evolution closes the loop inside the project repository.
2. Task cards that produce documents append `gitrule check` to their acceptance commands; multilingual projects also append `gitrule xcheck`; after any glossary change, run `gitrule termcheck`.
3. Document violations found by `gitrule check` are auto-fixable: run `gitrule optimize` first and re-check; if it still fails, write it into the block field of the handoff record.
4. Gitrule specifications govern documents and repository rules only; code quality belongs to each project's tests and verification scripts, and neither substitutes for the other.

## Related Files

- [Machine-Readable Index](./README.md): the registration entry for this specification
- [Hard Rules](./hard-rules.md): the higher-level constraints behind this specification's acceptance gates
- [Document Matrix](./document-matrix.md): the unique responsibility definition of the deliverable document this manual belongs to
- [General Writing Specification](./general-writing-specification.md): the writing standard for the manual body
- [Multilingual Specification](./multilingual-specification.md): the multilingual synchronization rules for this specification
- [Machine-Readable Metadata Specification](./machine-readable-metadata-specification.md): the stable identifier and path mapping of this specification
- [Information Collection and Templates](./information-collection-and-templates.md): terminology correspondence table and template field conventions
