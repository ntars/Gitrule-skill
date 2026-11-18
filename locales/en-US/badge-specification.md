# Badge Specification

> What this file solves: Defines the URL syntax, style parameters, color coding, information selection, arrangement order, and quantity control of badges (Badges) in the README. Using Shields.io as the primary implementation, it provides directly copyable format examples and recommended parameter configurations.

All parameters described in this file are verified against the official Shields.io documentation (the Static Badge and Logos pages, and the badge-maker format description). Occurrence data comes from this project's sampling statistics of README files from leading open-source projects and is marked as "measured".

## 1. Basic Syntax

### 1.1 Static Badge URL Structure

Static badges pass parameters through the URL path. The standard structure is as follows:

```text
https://img.shields.io/badge/<label>-<message>-<color>?style=<style>&<other query parameters>
```

The three path segments are separated by hyphens `-`:

| Segment | Name | Required | Description |
| --- | --- | --- | --- |
| 1st segment | Label | No | Left-side text, indicating the metric name |
| 2nd segment | Message | Yes | Right-side text, displaying the metric value |
| 3rd segment | Color | Yes | Right-side background color |

The two-segment form (omitting the label, with only the message and color) is also valid:

```text
https://img.shields.io/badge/<message>-<color>
```

### 1.2 Character Escaping Rules

Spaces and special characters in the URL path must be escaped. The rules are as follows:

| Input Character | URL Notation | Example |
| --- | --- | --- |
| Space | `_` or `%20` | `v0.1 prototype` → `v0.1%20prototype` |
| Underscore `_` | `__` (double underscore) | `my_label` → `my__label` |
| Hyphen `-` | `--` (double hyphen) | `dev-build` → `dev--build` |

The prototype example provided by the user conforms to this syntax and can be used directly:

```markdown
![Status](https://img.shields.io/badge/status-v0.1%20prototype-8957e5?style=flat-square)
```

Its meaning is: label `status`, message `v0.1 prototype` (space encoded as `%20`), color `8957e5` (hexadecimal purple), style `flat-square`.

### 1.3 Markdown Embedding Format

```markdown
![Version](https://img.shields.io/badge/version-1.2.0-blue?style=flat-square)
```

When a click-through is needed, wrap the image in a link:

```markdown
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
```

## 2. Style Parameter (style)

`style` determines the overall visual design of the badge. It can take five values, with a default of `flat`.

| Value | Visual Features | Applicable Scenario | Measured Occurrences (N=120) |
| --- | --- | --- | --- |
| `flat` | Square corners, flat, Shields.io default | General first choice, compatible with most themes | 32 |
| `flat-square` | Square corners, no rounding, slightly compact | For a neat, crisp front page | 60 |
| `for-the-badge` | Large bold type, high contrast | Top hero visuals, emphasis badges | 65 |
| `social` | Rounded corners, split left/right colors, flat | Social-style front page | 12 |
| `plastic` | Highlight gradient, skeuomorphic | Retro style, rarely used now | 1 |

**Recommended Configuration**:

- All badges within the same README must use a unified `style`; mixing is prohibited. This is the primary requirement for visual consistency.
- General projects prefer `flat` or `flat-square`; when a stronger brand front page is needed, use `for-the-badge` uniformly.
- In measurements, `for-the-badge` (65 times) and `flat-square` (60 times) are the most popular; either can serve as the default.

Format example:

```markdown
![build](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)
![build](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)
```

## 3. Color Parameters (color / labelColor)

### 3.1 Three Color Notation Methods

According to badge-maker, both `color` (right side) and `labelColor` (left background) support the following three notations:

**Method 1: Shields.io Named Colors**

| Semantics | Named Color |
| --- | --- |
| Success | `brightgreen`, `green`, `success` |
| Notice | `yellow`, `yellowgreen`, `orange`, `important` |
| Warning | `red`, `critical` |
| Information | `blue`, `informational` |
| Neutral | `grey` / `gray`, `lightgrey` / `lightgray`, `inactive` |

Note: The default value of `labelColor` is `grey` and the default value of `color` is `lightgrey` (the documentation also notes that `inactive` is one of the default colors); some named color values differ slightly from the CSS colors of the same name, and the Shields.io rendering result takes precedence.

**Method 2: Hexadecimal Colors**

Three- or six-digit hexadecimal is supported, and the `#` prefix may be omitted or retained:

```text
?color=8957e5
?color=007fff
?color=%23007fff    ← when keeping #, it must be encoded as %23
```

**Method 3: CSS Color Values**

`rgb(...)`, `rgba(...)`, `hsl(...)`, `hsla(...)`, and CSS named colors (such as `aqua`, `fuchsia`, `lightslategray`) are supported; URL encoding is required when using them.

### 3.2 Color Semantic Mapping (Recommended Configuration)

| Information Type | Recommended Color | Example Message |
| --- | --- | --- |
| Build passing, tests passing | `brightgreen` / `success` | `passing` |
| Build failing | `red` / `critical` | `failing` |
| Stable version | `blue` | `v1.2.0` |
| Pre-release, prototype | Custom purple `8957e5` / `orange` | `v0.1 prototype` |
| License | `blue` / `green` | `MIT` |
| Documentation status | `yellowgreen` | `docs` |
| Deprecated, unmaintained | `red` / `inactive` | `deprecated` |

**Recommended Configuration**: Each project fixes one set of brand colors and status colors; they must not be changed arbitrarily. The same semantics use the same color code across the entire repository.

Format example:

```markdown
![Coverage](https://img.shields.io/badge/coverage-95%25-orange?style=flat-square)
![Status](https://img.shields.io/badge/status-v0.1%20prototype-8957e5?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
```

## 4. Icon Parameters (logo / logoColor / logoSize)

### 4.1 Using Simple Icons

The `logo` parameter takes an icon slug from Simple Icons, in the format `?logo=<slug>`. Common slugs are as follows:

| Purpose | slug | Measured Occurrences (N=120) |
| --- | --- | --- |
| GitHub repository | `github` | 35 |
| Discord community | `discord` | 20 |
| npm package | `npm` | 4 |
| Apple platform | `apple` | 3 |
| Docker | `docker` | 3 |
| Social platform X | `x` | 3 |
| Python package | `pypi` | 2 |

The complete list of slugs is based on the Simple Icons site or the `slugs.md` file in the simple-icons repository.

### 4.2 Icon Coloring and Size

- `logoColor`: Sets the color of Simple Icons icons; supports hexadecimal, rgb, hsl, and CSS named colors; only applies to Simple Icons icons and has no effect on custom icons.
- `logoSize`: When set to `auto`, the icon scales adaptively to its content, suitable for wider icons; likewise only applies to Simple Icons.

Format example:

```markdown
![repo](https://img.shields.io/badge/github-repo-blue?logo=github)
![logo color](https://img.shields.io/badge/logo-javascript-blue?logo=javascript&logoColor=f5f5f5)
```

Custom icons can be passed via `logo=data:image/svg+xml;base64,...`, but the URL is extremely long and difficult to maintain, so it is not recommended unless specifically needed.

## 5. Other Query Parameters

| Parameter | Function | Example |
| --- | --- | --- |
| `label` | Overrides the default left-side text (spaces must be encoded) | `?label=healthiness` |
| `labelColor` | Left-side background color | `?labelColor=abcdef` |
| `color` | Right-side background color | `?color=fedcba` |
| `cacheSeconds` | HTTP cache duration (seconds); values below the default are ignored | `?cacheSeconds=3600` |
| `link` | Specifies the click-through URL for the left/right halves | Only effective within `<object>` tags; ineffective for Markdown images |

## 6. Dynamic Badges

Dynamic badges are pulled in real time by Shields.io from external services, with no need to manually update values. Common types:

| Category | URL Pattern | Purpose |
| --- | --- | --- |
| Build status | `https://img.shields.io/github/actions/workflow/status/<owner>/<repo>/<workflow>` | CI status |
| Version | `https://img.shields.io/npm/v/<package>` | Latest npm version |
| License | `https://img.shields.io/npm/l/<package>` | Package license |
| Star count | `https://img.shields.io/github/stars/<owner>/<repo>` | Popularity |
| Issue count | `https://img.shields.io/github/issues/<owner>/<repo>` | Open issues |
| Downloads | `https://img.shields.io/npm/dt/<package>` | Cumulative downloads |

Dynamic badges can have `?style=`, `?logo=`, and other parameters appended, with rules consistent with static badges. Benchmark projects commonly adopt the combination of "dynamic badges showing real metrics + static badges supplementing custom status".

## 7. Information Selection and Arrangement Order

### 7.1 Information Selection

Badges should convey status information that is "verifiable and useful to readers". It is recommended to keep only the following categories:

1. Build / test status;
2. Version or latest release;
3. License;
4. Documentation status;
5. Community channels (Discord, discussion forums);
6. Project-custom status (prototype, maintained, deprecated).

Must not include: download counts without a source, marketing tags unrelated to the project, unverifiable ratings, and purely decorative color blocks.

### 7.2 Arrangement Order

The recommended order is "status → version → license → platform/community → custom status", with importance decreasing from left to right. Rationale: build status determines whether readers adopt the project, version determines compatibility assessment, and license determines whether it can be used; all are pre-decision information.

### 7.3 Quantity Control

- Regular projects: 4–6 badges.
- Resource collections or ecosystem projects: can be relaxed to 8–10.
- All badges are placed after the project name and one-line positioning statement and before the main body, on their own line or in a centered container, not scattered throughout the body.

## 8. Accessibility and Theme Adaptation

- Each badge's `alt` text must state its actual meaning, e.g., `![build status]` rather than `![badge]`.
- Under dark/light themes, the badge image source can be switched via `<picture>`; using `for-the-badge` with `labelColor=000` maintains stable contrast in both themes.
- Badges must be clickable to jump to the corresponding data source (build status to CI, version to the package manager page, license to the LICENSE file).

## Related Files

- Section attribution and order: see [README Section Specification](./readme-sections-specification.md)
- Visual hierarchy and placement: see [README Visual Layout Specification](./readme-visual-layout-specification.md)
- Differentiated badge recommendations for each project type: see [README Category Adaptation Guide](./readme-category-adaptation-guide.md)
- A complete, directly applicable badge row: see [README Standard Template](./readme-standard-template.md)
- Research methodology and measured samples: see [README Template Research Report](./readme-template-research-report.md)
