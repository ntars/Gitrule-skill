# README Visual Layout Specification

> What this file solves: Defines the README's layout hierarchy, paragraph organization, and the usage scenarios and placement of tables, screenshots, and GIFs, so that the document strikes a balance between information density and visual appeal.

The "measured" data in this document comes from this project's sampling statistics of top open-source project READMEs (sample N=120); the benchmark practices are taken from first-screen structure evidence of several high-star projects.

## 1. Layout Hierarchy

### 1.1 Heading Levels

The README must establish a clear heading hierarchy, following these constraints:

1. Keep only one first-level heading (`#`) in the whole document, namely the project name, located on the first line of the file.
2. Second-level headings (`##`) are the main sections, preferably 6–12 in number; the measured median is 7.
3. Third-level headings (`###`) are used for subdivisions within a section, only when the content of a second-level heading is long.
4. Heading levels must not be skipped (for example, jumping directly from `#` to `###`).
5. Heading text is concise, using a noun or noun phrase, with no period at the end.

### 1.2 First-Screen Structure Order

The first screen refers to content visible without scrolling, organized in the following order:

1. Centered logo or project banner (optional);
2. First-level heading (project name);
3. Badge row (see the [Badge Specification](./badge-specification.md) for details);
4. One-sentence positioning (stating what the project is, who it is for, and what problem it solves);
5. Section navigation link row (optional, for long READMEs);
6. Summary of core features.

Benchmark evidence: `fd` and `ripgrep` place section navigation immediately after the positioning; `next.js` and `rust-lang/rust` open with a centered logo and banner; `vscode` inserts a product screenshot right after the positioning.

### 1.3 Paragraphs and Whitespace

- Keep each paragraph to 1–4 lines, avoiding large blocks of dense text.
- Leave one blank line between paragraphs to ensure a sense of breathing room after rendering.
- Put key conclusions first, explanations after.
- Keep one space between Chinese and English or digits; use Chinese and English punctuation according to their respective contexts.

## 2. Table Usage Specification

### 2.1 Usage Scenarios

Tables are suitable for multi-dimensional, comparable information. Measured: 36.7% of samples use tables, the recommended form for configuration descriptions, compatibility matrices, and command comparisons. Applicable scenarios include:

- Configuration item descriptions (key name, type, default value, purpose);
- Platform / version compatibility matrices;
- Command or parameter comparisons;
- Feature comparisons (this project versus other solutions);
- Roadmap and status.

### 2.2 Placement

A table immediately follows its second-level heading, preceded by one guiding sentence explaining the table's purpose; if there are exceptions after the table, add a separate paragraph.

### 2.3 Writing Requirements

| Requirement | Description |
| --- | --- |
| Column count control | 3–6 columns; consider splitting if more than 6 |
| Clear headers | Give each column a short noun header, avoiding empty headers |
| Consistent alignment | Table alignment is unified throughout the document |
| Concise content | Do not write long paragraphs in cells; use footnotes or links to expand if necessary |
| No empty cells | Write "None" or "Not applicable" where there is no content |

## 3. Code Block Usage Specification

### 3.1 Usage Scenarios

Code blocks are used for commands, configuration, API calls, and sample output. Measured: 66.7% of samples contain code blocks, an essential element of the "Quick Start" section, with a median of 2.

### 3.2 Writing Requirements

1. Every code block must be marked with a language, such as `bash`, `json`, `python`, `javascript`, to facilitate syntax highlighting.
2. Command examples give complete executable commands; prerequisite steps must not be omitted.
3. When results need to be shown, start a separate code block marked `text` and explain the expected output in the text.
4. Leave one blank line before and after each code block.
5. Keep a single block within 20 lines; overly long examples are split into multiple blocks or moved into the `examples/` directory with a link provided.
6. When interactive commands use the `$` prompt, it must be unified throughout the document.

Format example:

```bash
npm install <package-name>
```

```text
✓ Installation complete
```

## 4. Screenshot and GIF Usage Specification

### 4.1 Usage Scenarios and Trade-offs

| Element | Applicable Scenario | Notes |
| --- | --- | --- |
| Static screenshot | Application interface, running result, chart | Measured usage rate 63.3%, most commonly used |
| GIF / animation | Command-line demo, interaction flow, before-and-after comparison | Large file size, must be compressed, control duration |
| Logo / banner | Brand identity, first-screen front page | Provide dual versions for light and dark themes |
| Diagram | Architecture, flow, data flow | Must be updated synchronously with the document version |

Measured: 63.3% of samples contain images. Benchmark evidence: `fd` uses `doc/screencast.svg` as a demo, `ripgrep` uses a search result screenshot, `vscode` uses a product running screenshot, and `rust` and `next.js` use light/dark adaptive logo banners.

### 4.2 Placement

1. Logo / banner: at the very top of the file, centered.
2. Product screenshot: after the one-sentence positioning and before "Quick Start", to establish intuitive understanding.
3. GIF demo: a separate "Demo" section, immediately after "Core Features".
4. Architecture diagram: placed in the "Architecture" or "Design" section, or moved into `docs/architecture.md` and linked in the README.

### 4.3 Writing Requirements

- Every image must provide `alt` text describing its content; meaningless text such as `image` or `screenshot` must not be used.
- Images use relative paths to reference in-repository assets, or stable absolute URLs; avoid time-sensitive temporary links.
- For images that need theme adaptation, use the HTML `<picture>` element with `prefers-color-scheme` to provide light and dark versions.
- Control image size: prefer WebP or optimized PNG for screenshots, and convert GIFs to short videos or compressed animations where possible.
- Adapt image width: use the `width` attribute or an outer container limit to avoid breaking the page layout.

## 5. Links and Navigation

### 5.1 Section Navigation

When the README exceeds 200 lines, add a navigation link row to the first screen pointing to the main sections:

```markdown
[Installation](#安装) · [Quick Start](#快速开始) · [Documentation](#文档) · [Contributing](#参与贡献)
```

### 5.2 Relative Links First

Documents, images, and licenses inside the repository all use relative paths, ensuring they still work when forked or read offline. External links must be authoritative sources (official documentation, package manager pages, CI pages).

## 6. Checklist for Aesthetics and Appeal

1. The first screen has a logo or clear title, conveying the project positioning within 3 seconds.
2. Badges use a unified style, semantic colors, and a moderate number.
3. One unique first-level heading, 6–12 second-level headings, with no level skipping.
4. At least one copyable, runnable code example.
5. At least one screenshot or demo that demonstrates the product's value.
6. Tables are used for comparison-type information, with controlled columns and clear headers.
7. All images have `alt` text, all code blocks have language markers.
8. Long documents have section navigation.
9. Images and badges remain readable under both light and dark themes.

## Related Files

- Badge styles and colors are in the [Badge Specification](./badge-specification.md)
- The full list of sections is in the [README Sections Specification](./readme-sections-specification.md)
- The visual emphasis for different project types is in the [README Category Adaptation Guide](./readme-category-adaptation-guide.md)
- The directly applicable layout skeleton is in the [README Standard Template](./readme-standard-template.md)
- The measured samples and method are in the [README Template Research Report](./readme-template-research-report.md)
