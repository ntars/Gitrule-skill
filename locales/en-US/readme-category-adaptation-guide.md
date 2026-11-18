# README Category Adaptation Guide

> What this file solves: For different project types such as libraries, applications, command-line tools, frameworks, and resource collections, it provides differentiated recommendations on README section selection, visual emphasis, and badge configuration, and explains how each type of element improves aesthetics and attractiveness.

The general template applies to all projects, but readers of different project types have different concerns. This file provides type-oriented adjustment recommendations on top of the general specification. Readers should start from the [README Standard Template](./readme-standard-template.md) and tailor it according to the corresponding type in this file.

## 1. Type Overview

| Type | Reader's Primary Question | Front-Page Focus | Required Sections | Omittable Sections |
| --- | --- | --- | --- | --- |
| Library / SDK | How to install, how to use the API | Version and license | Installation, Quick Start, API, Compatibility | Deployment, screenshots |
| Application | Appearance and core features | Screenshots and features | Features, screenshots, installation, Quick Start | API reference |
| Command-line tool | How to use commands, how fast | Command examples and Demo | Installation, usage, command reference, Demo | Architecture, configuration (when minimal) |
| Framework | Ecosystem and learning curve | Documentation entry and examples | Positioning, Quick Start, documentation, community | Performance details (can be linked externally) |
| Resource collection | What is included, how to search | Catalog categorization and navigation | Catalog, categories, contribution guide | Installation, API |

## 2. Library / SDK

Typical representatives: HTTP clients such as axios, utility function libraries, client SDKs.

### 2.1 Section Selection

- Place a "one-line positioning + version + license" up front so readers can judge compatibility.
- Put "Installation" first, with package manager commands (npm, pip, cargo, etc.).
- "Quick Start" must be a complete example that can run independently.
- "API Reference" is detailed in the main README or linked to `docs/api.md`; when there are too many API entries, the README contains only a summary + link.
- "Compatibility" explains supported language versions, runtimes, and platforms.

### 2.2 Visual Emphasis

- Badge focus: version, build status, license, downloads, package size.
- Use images sparingly; screenshots are usually unnecessary; a small Logo can establish recognition.
- Present API parameters in tables to improve readability.

### 2.3 Key Points for Improving Aesthetics

1. Put version and license badges at the top to instantly build credibility.
2. Place the Quick Start code block near the first screen to lower the barrier to trying.
3. Unify column widths and the default-value column in API tables to reduce cognitive load.

## 3. Applications

Typical representatives: editors, desktop tools, end-user products.

### 3.1 Section Selection

- The first screen must include a product screenshot or running view, showing value before implementation.
- Organize "Core Features" by user scenarios, not technical modules.
- "Installation" covers install packages or download entries for each platform.
- "Quick Start" gives the shortest path to getting started.
- Source build instructions can be linked externally to `CONTRIBUTING.md`.

### 3.2 Visual Emphasis

- Badge focus: version, build status, license, downloads.
- Place screenshots after the positioning statement; they are the core element of the front page.
- Pair feature lists with icons or short screenshots to improve scanning efficiency.

### 3.3 Key Points for Improving Aesthetics

1. Center a high-quality product screenshot, adapting to both light and dark themes.
2. Use short sentences + icons for feature points; avoid long paragraphs.
3. Make download entries prominent, using button-style links.

## 4. Command-Line Tools

Typical representatives: terminal tools such as fd and ripgrep.

### 4.1 Section Selection

- Follow the "one-line positioning" with section navigation for easy jumping.
- "Installation" lists mainstream package managers and platform binaries.
- "Usage" is task-oriented, with common command examples.
- "Command Reference" or "Comparison with Similar Tools" is a high-frequency need.
- "Demo" uses GIFs or terminal recordings to show real results.
- Performance data must state the test environment and methodology.

### 4.2 Visual Emphasis

- Badge focus: version, build status, platform support, license.
- Demo animations are the core visual asset, showing speed and user experience.
- Use code blocks with language tags for commands, and `text` blocks for output.

### 4.3 Key Points for Improving Aesthetics

1. Put command examples at the top so readers can copy and use them without scrolling.
2. Use Demo animations to show real terminal effects, reinforcing the impression of "fast".
3. Place multi-language links (e.g., Chinese, Korean translations) near the badge row.

## 5. Frameworks

Typical representatives: full-stack frameworks such as next.js.

### 5.1 Section Selection

- The first screen emphasizes positioning, ecosystem scale, and learning entry points.
- The "Documentation" entry must be prominent, usually pointing to a separate documentation site.
- "Community" describes discussion forums, chat channels, and the code of conduct.
- "Quick Start" gives the command to create a minimal project.
- In-depth content (architecture, API) is linked externally, not expanded in the README.

### 5.2 Visual Emphasis

- Badge focus: version, build status, license, community channels.
- Combine a brand Logo with `for-the-badge` style badges to strengthen the front page.
- Showcase screenshots can be used to display ecosystem cases.

### 5.3 Key Points for Improving Aesthetics

1. Use a centered Logo + large, uniformly styled badges to form a branded first screen.
2. Present documentation and community entries as prominent navigation blocks.
3. Use newcomer entry points such as Good First Issues to lower the barrier to contribution.

## 6. Resource Collections

Typical representatives: awesome-series lists.

### 6.1 Section Selection

- Opening with a Logo and sponsorship information on the first screen is a common practice.
- Organize the body into a catalog by topic, providing clear navigation.
- "Contribution Guide" explains inclusion criteria and submission format.
- No need for Installation, API, Deployment, or similar sections.

### 6.2 Visual Emphasis

- The number of badges can be relaxed, but the style must be unified.
- Use second-level headings + lists for catalog categories, with a short description for each entry.
- Arrange sponsor Logos in a table or grid, keeping them aligned.

### 6.3 Key Points for Improving Aesthetics

1. Keep the catalog structure clear and category heading levels consistent.
2. Add a one-line description to each entry, avoiding links alone.
3. Keep the sponsorship and acknowledgment area aligned and tidy, without disrupting body reading.

## 7. Cross-Type General Principles

1. **Readers first**: The first screen answers readers' most important questions; type differences affect only order, not information completeness.
2. **Unified style**: Badges, headings, and code blocks within the same project must be consistent.
3. **Copyable examples**: Every type must provide at least one directly runnable example.
4. **External links**: In-depth content beyond the front-page responsibility is linked to separate documentation.
5. **Continuous synchronization**: Screenshots, version badges, and feature lists must be updated with each version to avoid stale information damaging credibility.

## Related Files

- General section list: see [README Section Specification](./readme-sections-specification.md)
- Visual element specification: see [README Visual Layout Specification](./readme-visual-layout-specification.md)
- Badge configuration: see [Badge Specification](./badge-specification.md)
- General template: see [README Standard Template](./readme-standard-template.md)
- Type distribution evidence: see [README Template Research Report](./readme-template-research-report.md)
