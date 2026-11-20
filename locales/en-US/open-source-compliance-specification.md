# Open Source Compliance Specification

> What this file solves: Defines the collection scope of open source compliance, dependency manifest fields, collection methods, license compatibility determination, modification annotation, and asset citation rules, ensuring declarations are complete and verifiable.

## 1. Collection Scope

Four categories of sources must be covered: direct dependencies, indirect and transitive dependencies, build and development toolchains, and asset resources (icons, fonts, images, audio, datasets, algorithm sources).

## 2. Dependency Manifest Fields

| Field | Requirement |
| --- | --- |
| Component name | Consistent with the official repository |
| Version | Actually locked version, not a range expression |
| Reference type | Direct dependency or indirect dependency |
| Copyright holder | Full name of the copyright owner as officially declared |
| License | SPDX identifier; for multiple licenses, the combination method must be stated |
| Official address | Full URL of the repository or homepage |
| Use in this project | Specific call location or function |
| Modified | Yes or No |
| Modification description | Modified files, modification content, modification reason; write "None" if not modified |
| Location of license text | Path within the project or file link |

The dependency manifest table template can be found in [Information Collection and Templates](./information-collection-and-templates.md).

## 3. Collection Method

Use the corresponding command for the tech stack to generate the dependency tree, then complete the license and copyright information item by item: `npm ls --all`, `pip freeze`, `go mod graph`, `cargo tree`, `mvn dependency:tree`, `gradle dependencies`, `composer show --tree`. License scanning can use tools such as `license-checker`, `pip-licenses`, and `cargo-license`. Scan results must be manually reviewed; tool output must not be used directly as the final conclusion.

## 4. License Compatibility

1. The compatibility between the project license and each dependency license must be determined, with focus on the infectious scope of GPL, AGPL, LGPL, and MPL.
2. For Apache-2.0 dependencies, confirm whether their NOTICE file requirements have been satisfied.
3. Asset licenses (such as SIL OFL fonts and the CC series) must be individually checked for attribution and distribution requirements.
4. When compatibility cannot be determined, annotate with "【Pending Confirmation: License Compatibility】" and explain the reason for doubt.
5. When the project uses layered licensing, determine compatibility layer by layer: a dependency is judged against the license of the layer it is used in, and the primary license must not be used to represent the whole repository. For the layout and confirmation workflow, see [LICENSE Specification](./license-specification.md).
6. When a single dependency spans several license layers, record the actual scope of use and judge it against the strictest applicable layer.

## 5. Annotation of Modifications to Others' Code

1. Retain the original copyright notice and license notice at the top of the file.
2. List the modified file paths, a summary of the modifications, and the modification date in NOTICE.
3. Synchronously explain in the corresponding section of the README.

## 6. Citations and Assets

1. When citing others' documents or code snippets, state the source address, author, and license.
2. Images, icons, and fonts must have their source and license recorded; if missing, annotate as pending confirmation and must not be used directly.
3. Assets of unknown origin must not be used.

## Related Files

- The dependency manifest is materialized as NOTICE; see [NOTICE Specification](./notice-specification.md)
- For license selection and full-text requirements, see [LICENSE Specification](./license-specification.md)
- Dependency and copyright authenticity belong to gates G6–G9 and G13; see [Quality Gates](./quality-gate.md)
