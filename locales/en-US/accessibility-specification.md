# Accessibility Specification

> What this file solves: Defines accessibility requirements for project documentation, READMEs, and user interfaces, making content usable for readers who use screen readers, keyboard operation, and different visual conditions.

## 1. Scope

1. Documentation accessibility: READMEs, documentation sites, example code, tables, images.
2. Interface accessibility: User interfaces of applications and web projects.
3. Command-line accessibility: Help text, error messages, and output formats.

## 2. Documentation Accessibility

### 2.1 Images and Media

1. Every image must provide `alt` text describing its content and purpose; decorative images use an empty `alt`.
2. Non-informative text such as "image", "screenshot", or "picture" must not be used as `alt`.
3. Animated GIFs must have their content explained in nearby text, avoiding conveying information through animation alone.
4. Charts must also provide a text description or data table; data series must not be distinguished by color alone.

### 2.2 Headings and Structure

1. Heading levels are continuous and must not skip levels (see [README Visual Layout Specification](./readme-visual-layout-specification.md)).
2. There is only one level-one heading in the whole document.
3. Lists use proper Markdown syntax, ensuring screen readers can identify them as lists.
4. Tables must have a header row; table layouts without headers must not be used to lay out a page.

### 2.3 Links and Text

1. Link text must independently describe the target; "click here" and "more" are forbidden.
2. Color must not be the only means of conveying information; it must be paired with text or icons.
3. Keep spaces when mixing Chinese and foreign languages, ensuring correct word breaking and reading aloud.
4. Give the full form when an abbreviation first appears.

### 2.4 Code and Tables

1. Code blocks are tagged with a language to help assistive tools identify them (see [README Visual Layout Specification](./readme-visual-layout-specification.md)).
2. Table cell content is concise; avoid merged rows that make parsing difficult for readers.
3. Long commands are given in a line-broken form, not relying on horizontal scrolling.

## 3. Interface Accessibility

### 3.1 Keyboard Operation

1. All interactive elements are reachable and operable by keyboard.
2. Focus order matches visual order, and focus state is clearly visible.
3. Provide a shortcut to skip repeated content (such as jumping to the main content).

### 3.2 Semantics and Labels

1. Use semantic tags to express structure and roles; avoid simulating controls with non-semantic elements.
2. Form controls must have associated labels; error messages are bound to the corresponding field.
3. Dynamic state changes are communicated to assistive technology via accessibility announcements.

### 3.3 Visual Conditions

1. Text-to-background contrast meets readability requirements: body text no less than 4.5:1, large text no less than 3:1.
2. Support system light and dark themes; theme switching must not change the information structure (see [README Visual Layout Specification](./readme-visual-layout-specification.md)).
3. Provide a reduced-motion option; avoid auto-playing high-frequency flashing content.
4. Layout remains usable when text is scaled to 200%, with no content truncation.

## 4. Command-Line Accessibility

1. Error messages explain the cause and a feasible fix action; outputting only an error code is forbidden.
2. `--help` output is clearly categorized, listing required parameters and default values.
3. Support an environment variable to disable colored output, aiding screen readers and log processing.
4. Interactive prompts provide non-interactive equivalents, supporting automation scenarios.

## 5. Verification Checklist

- [ ] All images have informative `alt` text.
- [ ] Heading levels are continuous, with one level-one heading in the whole document.
- [ ] Link text can be understood independently.
- [ ] Tables have headers; color is not the sole information carrier.
- [ ] Code blocks are tagged with a language.
- [ ] Interface elements are keyboard-operable, with visible focus.
- [ ] Contrast meets minimum requirements, readable in both light and dark themes.
- [ ] Help text and error messages can guide the next action.

## 6. Forbidden Practices

1. Conveying critical information with images alone without a text alternative is forbidden.
2. Using color alone to indicate status or errors is forbidden.
3. Using meaningless link text is forbidden.
4. Removing focus indicator styles without providing an alternative is forbidden.

## Related Files

- Document layout: see [README Visual Layout Specification](./readme-visual-layout-specification.md)
- Badge accessibility requirements: see [Badge Specification](./badge-specification.md)
- Writing standards: see [General Writing Specification](./general-writing-specification.md)
- Document quality is dimension D12: see [Review Dimension Matrix](./review-dimension-matrix.md)
