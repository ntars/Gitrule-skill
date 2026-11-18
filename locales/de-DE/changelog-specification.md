# Änderungsprotokoll-Spezifikation

> Problem, das diese Datei löst: Definiert Vorlage, Felder und Schreibweise der nutzerseitigen Versionsänderungsaufzeichnung, damit jede Änderung nachvollziehbar, jede Version zuordenbar und jeder Upgrade-Pfad beurteilbar ist.

## 1. Spezifikationsbestimmungen

1. Das Änderungsprotokoll folgt der Struktur von Keep a Changelog; die Versionsnummer folgt der semantischen Versionierung der [Versionsverwaltungsspezifikation](./version-management-specification.md).
2. Jede Version muss ein Veröffentlichungsdatum im Format `YYYY-MM-DD` besitzen; nicht veröffentlichte Inhalte stehen im Abschnitt `Unreleased`.
3. Einträge werden in sechs Kategorien gruppiert: `Added` hinzugefügt / `Changed` geändert / `Deprecated` veraltet / `Removed` entfernt / `Fixed` behoben / `Security` Sicherheit.
4. Jede Änderung ist nutzerseitig auszurichten, muss Auswirkung und Migrationsweg erläutern und darf keine internen Refactoring-Details nennen.
5. Brechende Änderungen sind mit `BREAKING CHANGE:` zu kennzeichnen und mit Migrationsschritten zu versehen (siehe [Migrationsleitfaden-Spezifikation](./migration-guide-specification.md)).
6. Die Versionsnummer muss mit Tag und Release Notes übereinstimmen; brechende Änderungen müssen `feat!:` oder `BREAKING CHANGE:` in der Commit-Nachricht entsprechen.

## 2. Vorlage für das Änderungsprotokoll

```markdown
# Änderungsprotokoll

Diese Datei zeichnet alle nutzerseitigen Änderungen auf. Das Format folgt Keep a Changelog, die Versionen folgen der semantischen Versionierung.

## [Unreleased]

### Added
- {{新增能力，说明对使用者的价值}}

### Changed
- {{行为变更，说明影响范围}}

### Deprecated
- {{即将移除的能力，说明替代方案与移除版本}}

### Removed
- {{已移除的能力，说明迁移路径}}

### Fixed
- {{缺陷修复，说明触发条件}}

### Security
- {{安全修复，说明影响与升级建议}}

## [{{X.Y.Z}}] - {{YYYY-MM-DD}}

### {{类型}}
- {{变更条目}}
- {{BREAKING CHANGE: 原行为 → 新行为；迁移步骤见链接}}

[Unreleased]: https://github.com/{{owner}}/{{repo}}/compare/v{{X.Y.Z}}...HEAD
[{{X.Y.Z}}]: https://github.com/{{owner}}/{{repo}}/compare/v{{prev}}...v{{X.Y.Z}}
```

## 3. Vorlage für Einträge

```markdown
- {{动词开头的一句话变更描述}}（{{关联 REQ 编号}}）
  - Auswirkung: {{哪些使用者或场景受影响}}
  - Migration: {{需要执行的动作；无则省略此行}}
  - Referenz: {{Issue / PR 链接}}
```

## 4. Felddefinitionen

| Feld | Pflicht | Typ | Ausfüllhinweise | Beispiel |
| --- | --- | --- | --- | --- |
| Versionsnummer | ja | `X.Y.Z` | exakt identisch mit dem Tag, ohne Präfix `v` ebenfalls zulässig, jedoch im gesamten Text einheitlich | `1.2.0` |
| Veröffentlichungsdatum | ja | `YYYY-MM-DD` | maßgeblich ist das Datum des Tag-Setzens | `2026-11-18` |
| Gruppentyp | ja | Enumeration | eine der sechs Kategorien; bei fehlenden Einträgen dieser Kategorie entfällt der gesamte Abschnitt | `Fixed` |
| Änderungsbeschreibung | ja | Text | mit Verb beginnend, nutzerseitig, den Nutzen erläuternd | `Prüfung auf GFM-Tabellen hinzugefügt` |
| Auswirkung | bedingt Pflicht | Text | Pflicht bei Verhaltensänderungen, Veraltungen, Entfernungen und brechenden Änderungen | `alte Konfigurationsdatei muss umbenannt werden` |
| Migration | bedingt Pflicht | Text | Pflicht bei brechenden Änderungen, verweist auf den Migrationsleitfaden | `siehe Migrationsleitfaden v1.0` |
| BREAKING CHANGE | bedingt Pflicht | Kennzeichnung | Pflicht bei brechenden Änderungen, am Anfang des Eintrags | `BREAKING CHANGE:` |
| Vergleichslink | ja | URL | für jeden Versionsabschnitt ist ein compare-Link anzugeben | `compare/v1.1.0...v1.2.0` |
| Verknüpfte REQ | nein | Liste | erleichtert den Abgleich mit der Anforderungs-Verfolgungsmatrix | `REQ-007` |

## 5. Ausfüllhinweise

1. **Granularität der Einträge**: Eine Änderung beschreibt ein für Nutzende wahrnehmbares Ergebnis; mehrere Ergebnisse sind in mehrere Einträge aufzuteilen.
2. **Mit Verb beginnen**: „Hinzugefügt“, „Unterstützt“, „Behoben“, „Entfernt“, „Veraltet“, „Angepasst“ verwenden; „aktualisiert“, „einige Dinge getan“ nicht verwenden.
3. **Unzulässige Inhalte**: Einträge ohne Datum, interne Refactorings, Entwicklungspläne, Roadmap-Inhalte, unbestimmte Formulierungen („Erlebnis verbessert“, „mehrere Probleme behoben“).
4. **Brechende Änderungen**: Erforderlich sind gleichzeitig die Kennzeichnung `BREAKING CHANGE:`, die Auswirkungsbeschreibung, die Migrationsschritte und der Link zum Migrationsleitfaden; keines der vier darf fehlen.
5. **Veraltete Punkte**: Alternativlösung und geplante Versionsnummer der Entfernung sind anzugeben, beispielsweise „wird in v2.0 entfernt“.
6. **Unreleased**: Unmittelbar nach der Zusammenführung eintragen und nicht bis zum Veröffentlichungstag aufschieben.
7. **Konsistenz**: Versionsnummer und Veröffentlichungsdatum müssen an drei Stellen übereinstimmen – Tag, Release Notes und Bereitstellungsprotokoll; bei Abweichung ist der Tag maßgeblich und die übrigen drei Stellen sind zu korrigieren.

Häufige Fehler:

| Fehlerhafte Schreibweise | Problem | Korrektur |
| --- | --- | --- |
| „Interne Modulstruktur refaktoriert“ | interne Details, für Nutzende nicht wahrnehmbar | löschen oder in eine wahrnehmbare Wirkung umschreiben |
| „Mehrere Probleme behoben“ | nicht beurteilbar | behobene Inhalte einzeln auflisten |
| brechende Änderung nur als „es gibt Änderungen“ | kein Migrationspfad | Auswirkung, Migrationsschritte und Leitfadenlink ergänzen |
| Versionsnummer weicht vom Tag ab | Zuordnung der Versionen bricht | Tag als maßgeblich vereinheitlichen |
| kein compare-Link | Differenzen nicht einsehbar | GitHub-compare-URL ergänzen |

## 6. Vollständiges Beispiel

```markdown
## [1.0.0] - 2026-11-20

### Added
- Prüfregel für Leerzeichen bei gemischtsprachigem Satz aus Chinesisch und Englisch hinzugefügt (REQ-001); direkter Aufruf über die Befehlszeile wird unterstützt.
- JSON-Berichtsausgabe hinzugefügt, um die Anbindung an CI-Statistiken zu erleichtern.

### Changed
- BREAKING CHANGE: Der Name der Konfigurationsdatei wurde von `.mdlint.json` in `.mdlintrc.json` geändert. Alte Dateien werden nicht mehr gelesen; Migrationsschritte siehe [Migrationsleitfaden](./migration-guide-specification.md).

### Deprecated
- Der Parameter `--format=table` wird in v2.0 entfernt; bitte auf `--reporter=table` umstellen.

### Fixed
- Falschmeldung behoben, wenn chinesische Satzzeichen direkt an englische Wörter angrenzen.

### Security
- Problem behoben, dass der Ladepfad von Regel-Plugins durch externe Eingaben überschrieben werden konnte; allen Nutzenden wird ein Upgrade auf v1.0.0 empfohlen.

[1.0.0]: https://github.com/example/markdown-lint-cli/compare/v0.9.3...v1.0.0
```

## Verwandte Dateien

- Regeln zur Versionsinkrementierung: [Versionsverwaltungsspezifikation](./version-management-specification.md)
- Migrationsdokumentation für brechende Änderungen: [Migrationsleitfaden-Spezifikation](./migration-guide-specification.md)
- Abgrenzung der Dokumentverantwortlichkeiten: [Dokumentationsmatrix](./document-matrix.md)
- Kennzeichnung brechender Änderungen in Commit-Nachrichten: [Commit-Nachrichten-Spezifikation](./commit-message-specification.md)
- Abschnitt zur Änderungsaufzeichnung in der README: [README-Abschnittsspezifikation](./readme-sections-specification.md)
- Tag und Release Notes: [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md)
