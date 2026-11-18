# Open Source Promotion Specification

> What this file solves: Defines the promotion channels, release cadence, showcase materials, and community operation specifications for open source projects before and after release, enabling a project with usable documentation to gain exposure matching its target users.

The channel list and principles in this file draw on the promotion chapter of phodal's *A Guide to GitHub*; with 11,362 stars, that project validated the applicability of these practices within the Chinese open source community.

## 1. Basic Principles

1. **Quality before promotion**: Promotion only amplifies existing quality; it does not repair what is missing. Do not begin promotion until the README, examples, documentation, and tests are ready.
2. **The project itself is not the whole of promotion**: Beyond code and the README, prepare detailed documentation, sample programs, and an issue response mechanism.
3. **Clear motivation**: Promotion serves a concrete goal (acquiring early users, recruiting contributors, collecting feedback); do not promote for the sake of chasing star counts.
4. **Channel fit**: Choose channels based on the project's tech stack and target users; avoid indiscriminate posting.
5. **Honest presentation**: Do not fabricate star counts, download counts, or use cases; feature comparisons must be based on verifiable facts.

## 2. Pre-Release Checklist

| Category | Requirement | Basis |
| --- | --- | --- |
| Showcase | README passes the four-question check (what it does / what it solves / features / example) | [README Section Specification](./readme-sections-specification.md) |
| One-line pitch | Clearly states the category and qualifier, can be restated independently | Same, Section 1.1 |
| Example | Provides a hello world runnable in two steps or fewer | [README Standard Template](./readme-standard-template.md) |
| Documentation | Installation, configuration, and API documentation complete | [Documentation Matrix](./document-matrix.md) |
| License | LICENSE exists and matches the README's stated license | [LICENSE Specification](./license-specification.md) |
| Compliance | NOTICE covers third-party dependencies | [NOTICE Specification](./notice-specification.md) |
| Community entry | Issue templates, contribution guide, and code of conduct in place | [Contributing Guide Specification](./contribution-guide-specification.md) |
| Response mechanism | Clear issue responders and response time limits | [Incident Response Specification](./incident-response-specification.md) |

Promoting before completing the above checklist is a prohibited behavior under this specification.

## 3. Channel Categories

### 3.1 International Technical Communities

| Channel | Suitable Content | Notes |
| --- | --- | --- |
| Hacker News | Technical implementation, in-depth engineering design | Titles must be plain; avoid marketing language |
| Relevant Reddit subreddits | Libraries, tools, frameworks | Follow each subreddit's self-promotion rules |
| Lobsters | Systems programming, engineering practices | Community is sensitive to marketing |
| Technical newsletters (JavaScript Weekly, etc.) | Libraries and tools | Provide a concise project summary |
| Official blog and documentation site | In-depth introduction and release notes | Serve as the landing point for other channels |

### 3.2 Chinese Technical Communities

| Channel | Suitable Content |
| --- | --- |
| Juejin | Front-end, mobile, engineering practices |
| Developer Headlines | General technical projects |
| V2EX | Tools, productivity software, startups |
| Zhihu | Technical analysis and design trade-offs |
| WeChat Official Account | In-depth long-form articles, tutorial series |
| Geek Headlines | General technology news |

### 3.3 Project-Owned Channels

1. Community entry points in the project README (Discussions, Discord).
2. Dedicated project social accounts for releasing versions and events.
3. Documentation site and demo site as landing pages for external traffic.

## 4. Release Cadence

1. **Warm-up phase**: Complete the checklist in Section 2; prepare materials such as the one-line pitch, screenshots, and demo GIFs.
2. **Launch phase**: Publish on the 1–2 most relevant channels; avoid spamming the same content across many platforms.
3. **Response phase**: Maintain high-frequency responses for 72 hours after launch, handling issues and feedback.
4. **Iteration phase**: Continue updating with each release; attach release notes to every release.
5. **Consolidation phase**: Organize high-frequency questions into an FAQ to feed back into documentation.

## 5. Showcase Material Requirements

| Material | Specification | Purpose |
| --- | --- | --- |
| One-line pitch | Within 60 Chinese characters / within 25 English words; the repository Description follows the bilingual merged format `national language \| English`, see [Project Naming Specification](./project-naming-specification.md) Section 5 | Repository Description, social summary |
| Screenshots | Both light and dark theme versions, controlled width | README above the fold |
| Demo GIF | Controlled size after compression, shows the core flow | README demo section |
| Logo | SVG format, with light and dark versions | Above the fold and social cards |
| Feature comparison table | Based on verifiable facts, includes unsuitable scenarios | README or documentation site |

Materials must be updated in sync with releases to avoid showing outdated interfaces.

## 6. Community Operation

1. Provide a clear entry point for first-time contributors, such as the `good first issue` label.
2. Issue responses must be recorded to avoid repeated questions recurring.
3. The code of conduct applies to all community channels; see [Code of Conduct Specification](./code-of-conduct-specification.md).
4. Place contributor acknowledgments together rather than scattered throughout the text.
5. Do not use tactics that induce stars or mutual likes to gain false attention.

## 7. Prohibited Practices

1. Promoting before the quality checklist is complete is prohibited.
2. Fabricating or exaggerating project data and use cases is prohibited.
3. Repeatedly spamming the same content across multiple channels is prohibited.
4. Disparaging similar projects to elevate one's own image is prohibited.
5. Using inducements to obtain stars is prohibited.

## Related Files

- Four-question check and one-line pitch: [README Section Specification](./readme-sections-specification.md)
- Visual material specifications: [README Visual Layout Specification](./readme-visual-layout-specification.md)
- Community entry specifications: [Contributing Guide Specification](./contribution-guide-specification.md)
- Issue response mechanism: [Incident Response Specification](./incident-response-specification.md)
- Release notes: [Push and Release Specification](./push-and-release-specification.md)
- Research source: [README Template Research Report](./readme-template-research-report.md)
