# README Template Research Report

> What this file solves: Records the research method, sample size, and quantitative findings of this standard README template, providing a data basis for the [README Standard Template](./readme-standard-template.md) and each specialized specification, and clarifying the boundaries and limitations of the method.

## 1. Research Objectives and Method

### 1.1 Objectives

To research top open-source projects ranked high by star count, summarize the structure, section organization, visual presentation, and badge usage patterns of their READMEs and related documents, and form reusable general specifications and templates.

### 1.2 Data Sources

- Repository metadata: GitHub GraphQL Search API, sorted by stars in descending order, filtered with `is:public archived:false fork:false`.
- README original text: GitHub REST Contents API (`readme` endpoint), obtained in base64 or raw form and then parsed.
- Badge parameters: Shields.io official documentation (Static Badge, Logos pages) and badge-maker format description.
- Chinese community practices: the project documentation, commit messages, and promotion sections of phodal/github (*A Guide to GitHub Tourism*, 11,362 stars), used to supplement writing principles and operational experience that machine-readable statistics cannot cover.

### 1.3 Collection Method

1. **Metadata**: A single GitHub Search API query returns at most 1000 results. To expand the sample, star-range sharding was used — binary search located the star threshold corresponding to every 1000th rank, moving downward batch by batch for a cumulative 11 batches, finally obtaining metadata for 10,995 top repositories.
2. **README sampling**: Stratified sampling by primary language within the top 1000 repositories, covering Python, TypeScript, JavaScript, Rust, Go, C++, and other major languages; 120 repositories were sampled, and all README original texts were successfully obtained.
3. **Statistical criteria**: Section occurrence rates and element usage rates were counted per repository; badge styles and logo parameters were counted by number of occurrences in URLs.

### 1.4 Method Limitations (must be stated explicitly)

- The GitHub Search API imposes a 1000-result limit on a single query; this report expanded the scale through cumulative sharding, but shard boundaries are affected by star ties, so the sample is an approximate top set, not a strictly continuous ranking.
- The README sampling size is 120; conclusions reflect trends and commonalities and do not represent a statistically significant distribution of all top projects.
- Section identification is based on heading keyword matching, which has statistical bias caused by wording differences.
- Badge parameter statistics target parameters explicitly appearing in URLs; default parameters of dynamic badges were not counted.

## 2. Top Repository Distribution (Metadata)

### 2.1 Sample Size

- A single query reliably obtains the top 1000 repositories, with a star range of approximately 563,574 to 30,857.
- After 11 batches of cumulative sharding, expanded to 10,995 top repositories, with a lower star bound of 5,452.

### 2.2 Language Distribution (based on top 1000)

| Language | Count | Percentage |
| --- | --- | --- |
| Python | 223 | 22.3% |
| TypeScript | 178 | 17.8% |
| JavaScript | 112 | 11.2% |
| Rust | 80 | 8.0% |
| No primary language | 74 | 7.4% |
| Go | 68 | 6.8% |
| C++ | 55 | 5.5% |
| Java | 27 | 2.7% |

Top projects are dominated by Python, TypeScript, and JavaScript, which together exceed 50%; system languages such as Rust and Go have a significant share. This determines that the template must cover multi-language package manager installation commands and multi-runtime badges.

### 2.3 License Distribution (based on top 1000)

| License | Count | Percentage |
| --- | --- | --- |
| MIT | 399 | 39.9% |
| Apache-2.0 | 197 | 19.7% |
| Unrecognized (NOASSERTION) | 148 | 14.8% |
| No license (NONE) | 65 | 6.5% |
| GPL-3.0 | 51 | 5.1% |
| AGPL-3.0 | 50 | 5.0% |
| BSD-3-Clause | 17 | 1.7% |

MIT dominates and is the default recommendation for the general template; SPDX identifier placeholders for options such as Apache-2.0 and GPL must also be retained.

## 3. README Structure Findings (N=120)

### 3.1 Section Occurrence Rates

| Section Keyword | Repositories Containing It | Occurrence Rate |
| --- | --- | --- |
| Contributing | 66 | 55.0% |
| License | 52 | 43.3% |
| Install | 49 | 40.8% |
| Quick Start | 28 | 23.3% |
| Documentation | 25 | 20.8% |
| Development | 22 | 18.3% |
| Configuration | 19 | 15.8% |
| Features | 19 | 15.8% |
| Security | 15 | 12.5% |
| Usage | 12 | 10.0% |
| Requirements | 11 | 9.2% |
| API | 10 | 8.3% |
| Examples | 10 | 8.3% |

Finding: contribution guides and licenses are standard for top projects, reflecting the priority of community governance and compliance; installation and quick start follow closely. The template therefore lists both as required.

### 3.2 Visual Element Usage Rates

| Element | Repositories Containing It | Occurrence Rate | Median (per repository) |
| --- | --- | --- | --- |
| Code blocks | 80 | 66.7% | 2 |
| Images | 76 | 63.3% | 2 |
| Badges (Shields.io) | 61 | 50.8% | 1 |
| Tables | 44 | 36.7% | 0 |

Median heading levels: 7 second-level headings, median file length 171 lines. This indicates that top READMEs are generally kept at a moderate length, organized with 6–12 second-level headings.

### 3.3 Theme Adaptation (first 40 samples)

| Feature | Repositories Containing It |
| --- | --- |
| Centered container (`align="center"`) | 27 |
| `<picture>` element | 12 |
| Light/dark theme switching (`prefers-color-scheme`) | 12 |
| `for-the-badge` with `labelColor` | 2 |

Centered containers are the mainstream front-page technique; about one third of projects provide dual versions of images for light and dark themes.

## 4. Badge Findings

### 4.1 Style Parameters (by number of URL occurrences, N=120)

| style | occurrences |
| --- | --- |
| `for-the-badge` | 65 |
| `flat-square` | 60 |
| `flat` | 32 |
| `social` | 12 |
| `plastic` | 1 |

`for-the-badge` and `flat-square` are the most popular; `plastic` has been largely abandoned. For details, see the [Badge Specification](./badge-specification.md).

### 4.2 logo Parameters (by number of occurrences, N=120)

| logo slug | occurrences |
| --- | --- |
| `github` | 35 |
| `discord` | 20 |
| `npm` | 4 |
| `apple` / `docker` / `linkedin` / `x` | 2–3 each |

GitHub and Discord are the most common icons, corresponding to the two categories of "source repository" and "community channel".

## 5. Benchmark Project First-Screen Evidence

| Project | Type | Front-Page Features |
| --- | --- | --- |
| `sindresorhus/awesome` | Resource collection | Centered logo, sponsor area, themed category directory |
| `axios/axios` | Library | Important notice, sponsor table, multilingual |
| `sharkdp/fd` | CLI | Badges + multilingual links, section navigation, demo animation |
| `BurntSushi/ripgrep` | CLI | Badges, quick links, search screenshot, performance comparison |
| `vercel/next.js` | Framework | Centered logo, `for-the-badge` badges, documentation and community entry points |
| `microsoft/vscode` | Application | Badges, repository description, product screenshot, contribution and feedback entry points |
| `rust-lang/rust` | Language | Centered banner, navigation row, Why Rust value points |
| `phodal/github` | Chinese e-book | Four front-page questions, one-sentence copy examples, installation simplification principle, promotion channel list |

Commonality: the first screen answers "what it is, how to use it, where to see details"; badges sit right next to the title; screenshots or demos follow closely after the positioning; contribution and community entry points are placed lower down but are indispensable.

## 6. Summary Conclusions

1. The general template must use "positioning → installation → quick start → documentation → contribution → license" as its backbone.
2. Badges default to `flat-square` or `for-the-badge`, unified throughout, 4–6 in number.
3. Images and code blocks are the core of an attractive front page and must be provided with `alt` text and language markers.
4. Project type determines section selection, see the [README Category Adaptation Guide](./readme-category-adaptation-guide.md).
5. Compliance and community governance (license, contribution guide) are a consensus among top projects and are listed as required.

## 7. Data Scale Notes

Cumulative sharding results for top repository metadata: 10,995 repositories, with a star range of 563,575 to 5,452. The license and language distributions of this ten-thousand-scale sample are as follows, consistent with the conclusions from the top 1000 sample:

| Dimension | Distribution |
| --- | --- |
| Language | Python 1,995, TypeScript 1,529, JavaScript 1,279, no primary language 888, Go 847, C++ 531, Java 528, Rust 507 |
| License | MIT 4,160 (37.8%), Apache-2.0 2,073 (18.9%), unrecognized 1,463, no license 1,106, GPL-3.0 747 |

The README in-depth statistics sample is 120, all successfully obtained. Sharding uses approximate star thresholds, and the scale is an approximate top set, not a strictly continuous ranking.

## Related Files

- The directly applicable template is in the [README Standard Template](./readme-standard-template.md)
- The badge specification is in the [Badge Specification](./badge-specification.md)
- The visual specification is in the [README Visual Layout Specification](./readme-visual-layout-specification.md)
- Category adaptation is in the [README Category Adaptation Guide](./readme-category-adaptation-guide.md)
- Section definitions are in the [README Sections Specification](./readme-sections-specification.md)
