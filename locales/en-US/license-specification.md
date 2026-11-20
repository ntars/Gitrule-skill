# LICENSE Specification

> What this file solves: Defines the SPDX annotation of the project license, LICENSE full-text requirements, the location of the copyright line, the GitHub detection mechanism, file layout for layered licensing, the confirmation workflow, and rules prohibiting writing unconfirmed content.

## 1. Basic Rules

1. The project license must be explicitly written in the README using its SPDX identifier, and a corresponding LICENSE file must be provided.
2. The LICENSE file must be the official English full text of that license; terms must not be deleted or altered. Rewording, reordering paragraphs, or reformatting as Markdown all cause automatic detection to fail.
3. The copyright line is placed at the top of the file or in Chapter 19 of the README; see [README Section Specification](./readme-sections-specification.md) for the format.

## 2. GitHub Detection Mechanism

GitHub determines a repository's license using the open-source licensee tool. The result drives the repository page badge, the API `license` field, and whether the repository is returned by `license:` keyword searches. The rules are:

1. Only two locations are scanned: the project root, and a top-level `LICENSES/` directory. Files with similar names inside `locales/`, `docs/`, or other subdirectories do not participate.
2. Root files are scored by filename, highest wins: `LICENSE` scores 1.00, `LICENSE.md` 0.95, `COPYING` 0.90, suffixed forms such as `LICENSE-MIT` 0.70.
3. Inside a top-level `LICENSES/` directory, a filename in SPDX identifier format with a `.txt`, `.md`, `.markdown`, or `.html` extension scores 1.00; anything else scores 0.00.
4. File content must closely match the official full text of that license. A file containing only a statement like "This project uses the X license" will not be detected, and any result it produces is a non-standard value.
5. When multiple distinct licenses are detected, the project-level result may omit a specific license, and the repository page shows `View license` or `Other`.
6. Natural-language statements in the README do not participate. Writing "This project is MIT licensed" does not make it detected as MIT.

Therefore: **the README statement and the LICENSE file are two independent mechanisms, and both are required.** When several license files exist at the root, which one is finally reported depends on both filename score and content match and is not predictable; in measurement, dual-licensed repositories reported only one of the two.

## 3. File Layout for Layered Licensing

Layered licensing means different parts of a repository are under different licenses, for example code under MIT and documentation under CC BY 4.0. Decide the layout in this order:

| Option | What goes at the root | Detection result | When to use |
| --- | --- | --- | --- |
| Single layer (default) | One `LICENSE` | Detectably that license | All layers use the same license, or the difference does not change downstream obligations |
| Layered with a statement | `LICENSE` holds the primary license, plus a `LICENSING.md` | Detectably the license in the root `LICENSE` | Layering is needed and the badge must stay unambiguous |
| Layered with REUSE | Top-level `LICENSES/` holds each full text | May degrade to a non-standard value | Only when downstream explicitly requires REUSE compliance |

Trade-offs:

1. Do not place multiple license files at the root. In measurement, every dual-licensed repository was reported as only one of its two licenses; the other remained invisible on the repository page and in the API, which amounts to declaring only one license publicly.
2. The REUSE layout conflicts with badge clarity: multiple licenses in `LICENSES/` are read as multiple licenses, buying a green `reuse lint` at the cost of an ambiguous detection result. The two cannot both be fully satisfied; the project must choose.
3. For the "layered with a statement" option, the filename `LICENSING.md` does not match the `LICENSE` or `COPYING` patterns, so it is not mistaken for a license file and does not affect detection of the root `LICENSE`.
4. Whichever layout is chosen, Chapter 19 of the README must state the SPDX expression (for example `MIT AND CC-BY-4.0`) and the scope of each layer. This is the only place where the information survives at the human-reading level.

## 4. Layering Decisions and Confirmation Workflow

Layered licensing carries legal meaning. Before writing or optimizing anything, confirm round by round; do not invent.

1. Do not introduce layering on your own initiative. When the user has not explicitly requested it, treat the project as single-layer and state in the report: "If layering is needed, the candidate options and differences are as follows."
2. Any layering proposal must report its basis: what content each layer actually covers, the candidate licenses and how their obligations differ, the effect on downstream users, and how the detection result would change.
3. Confirm at least twice before writing: first the combination (which license for which layer), then the file layout (which license goes in the root file, whether to create `LICENSES/`).
4. Confirm again before pushing. After generating files, explicitly state "The files have been generated; please review and commit them yourself" and never commit or push on the user's behalf.
5. Unconfirmed candidate options go only into a report or a temporary file; they must not be written out as `LICENSE`, `LICENSES/`, or `LICENSING.md`.
6. When it is unclear which layer a part belongs to, mark it "Pending confirmation: layer assignment" and list the files in question; do not classify by default.

## 5. Disclaimer Requirements

License texts have legal effect. Templates and tooling provide only decision rules and file layout guidance, not legal advice.

1. Chapter 19 of the README or the `LICENSING.md` file must contain a disclaimer stating that the license choice is confirmed by the project owner.
2. The disclaimer must match the one in NOTICE; it must not exist in one place and be missing in the other.
3. Do not claim that "compliance review is complete." State only that "the file layout and SPDX annotations have been checked against the rules for completeness."
4. The legal effect of layered licensing follows the full text of each license. Descriptive text inside the repository is an index only and does not alter the terms.

## Related Files

- A missing LICENSE blocks push; this is hard rule H2, see [Hard Rules](./hard-rules.md)
- For dependency license compatibility determination, see [Open Source Compliance Specification](./open-source-compliance-specification.md)
- For the standalone file of third-party declarations, see [NOTICE Specification](./notice-specification.md)
- License accuracy belongs to gates G7/G8; see [Quality Gates](./quality-gate.md)
