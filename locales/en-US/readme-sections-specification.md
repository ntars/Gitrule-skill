# README Sections Specification

> What this file solves: Defines the 20 sections that the README of each language directory must contain, what each section must include and must not contain, and the standard format for the copyright line.

## 1. General Section Requirements

All of the following 20 sections must be present, in a fixed order, with a one-to-one correspondence across language versions.

| No. | Section | Must Include | Must Not Contain |
| --- | --- | --- | --- |
| 1 | Project name and positioning | Project name, repository description (native language and English bilingual comparison), topics (5–10), one-sentence positioning, language switch links, current version, maintenance status | Vague adjectives; repository description exceeding 120 characters; mixed capitalization in topics |
| 2 | Project introduction | Background, problem to be solved, core approach, applicable scenarios, inapplicable scenarios, and separately listed advantages and limitations (limitations must include scope of impact and workaround) | A single passing sentence; listing advantages but not limitations |
| 3 | Core features | Feature items grouped by module, each including a trigger condition and result | Only listing feature names |
| 4 | Core highlights | Expanded according to the structure in the [Highlights and Engineering Trade-offs Writing Guide](./highlights-and-engineering-tradeoffs-guide.md) | Praise without evidence |
| 5 | Design details and engineering trade-offs | Expanded according to the structure in the [Highlights and Engineering Trade-offs Writing Guide](./highlights-and-engineering-tradeoffs-guide.md) | Descriptions duplicated from the features section |
| 6 | Technology stack and dependency list | Runtime, build, and test toolchains with version constraints; dependency details pointing to NOTICE | Missing version numbers |
| 7 | Installation and deployment | Environment requirements, installation steps, verification commands, upgrade and uninstall methods, containerization notes | Skipping steps or omitting verification |
| 8 | Quick start | A minimal runnable example with full commands and expected output | Pseudocode that cannot be executed |
| 9 | Configuration | Configuration item table (key name, type, default value, whether required, value range, purpose, example), configuration precedence, hot-reload support | Missing default values |
| 10 | API or module description | Interface signature, parameters, return values, error codes, call examples, rate limiting and quotas | Missing error codes |
| 11 | Directory structure | Tree structure with a description of each level's responsibility | Listing files one by one without explanation |
| 12 | Performance | Test environment, test method, metric data, bottleneck analysis, tuning recommendations | Numbers without test conditions |
| 13 | Security and privacy | Data collection and storage, transmission encryption, permission model, vulnerability reporting channel, known risks | Promises of absolute security |
| 14 | Compatibility | Operating system, runtime, browser, database version matrix, explicitly stating unsupported items | Vague wording |
| 15 | Known issues and limitations | Known issues (description, scope of impact, temporary workaround, tracking link), current limitations, list of unimplemented features (feature, reason for non-implementation, planned status) | Concealing serious defects; writing unimplemented features as implemented |
| 16 | Changelog | Follows the Keep a Changelog structure, version numbers follow semantic versioning | Entries without dates |
| 17 | Future roadmap | Planned items, status, target version, marked "non-commitment" | Promising delivery dates |
| 18 | Contributing | Development environment setup, branch model, commit specification, PR requirements, code of conduct, issue templates | Only writing "PRs are welcome" |
| 19 | Copyright and license | Copyright line, license name, SPDX identifier, location of full license text | Missing copyright holder |
| 20 | NOTICE compliance statement | Summary of third-party dependencies, a relative link to the NOTICE file | Using this section as a replacement for NOTICE |

## 1.1 The Four Front-Page Questions and One-Sentence Copy

The first screen of the README must answer four questions, in a fixed order:

1. What the project does;
2. What problem the project solves;
3. What features the project has;
4. A minimal hello world example.

Of these, the first question corresponds to the "one-sentence positioning", which must satisfy three points simultaneously: state the project type, use precise qualifiers, and be directly repeatable. Public copy from mature projects can serve as a reference:

| Project | One-Sentence Copy | Structure Analysis |
| --- | --- | --- |
| Angular | One framework. Mobile & desktop. | Category + coverage |
| React | A declarative, efficient, and flexible JavaScript library for building user interfaces. | Three qualifiers + category + purpose |
| Vue | A progressive, incrementally-adoptable JavaScript framework for building UI on the web. | Two features + category + purpose |

Writing constraints:

- Do not use uninformative adjectives such as "powerful", "excellent", or "revolutionary";
- Provide a category word (library, framework, tool, application) so readers can classify at a glance;
- No more than three feature qualifiers, avoiding accumulation;
- The Chinese version must be kept within 60 characters, the English version within 25 words.

The third question "what features" must simultaneously disclose inapplicable scenarios. An effective example: describing a message middleware as "only supports QoS level 0, not applicable for scenarios requiring level 1"; an ineffective approach is listing only advantages. Feature comparisons must be based on verifiable facts and must not disparage similar projects.

The hello world example for the fourth question must complete installation and running within two steps; projects with cumbersome installation steps should provide a container image or an online demo environment, to avoid readers giving up after finishing the README.

## 2. Standard Copyright Line Format

```text
Copyright © {{年份}} {{著作权人}}. Licensed under {{SPDX 标识符}}.
```

## Related Files

- Section content boundaries are in the [Document Matrix](./document-matrix.md)
- Repository description and topics rules are in Section 5 of the [Project Naming Specification](./project-naming-specification.md)
- Chinese-English version consistency is in the [Multilingual Specification](./multilingual-specification.md)
- The NOTICE that dependency details point to is in the [NOTICE Specification](./notice-specification.md)
- Writing standards are in the [General Writing Specification](./general-writing-specification.md)
