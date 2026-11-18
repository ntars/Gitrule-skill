# Commit-Nachrichten-Spezifikation

> Problem, das diese Datei löst: Sie definiert Felder, Format, Hinweise zum Ausfüllen und Beispiele von Conventional Commits, damit die Historie lesbar bleibt und Änderungsprotokoll sowie Versionsnummern automatisch erzeugt werden können.

## 1. Format

```text
<类型>[可选作用域][可选 !]: <描述>

[可选正文]

[可选脚注]
```

## 2. Typen

Die vollständigen zehn Typen lauten wie folgt und decken die Commit-Situationen gängiger Open-Source-Projekte ab:

| Typ | Bedeutung |
| --- | --- |
| `feat` | Neue Funktion |
| `fix` | Behebung eines Defekts |
| `docs` | Änderung der Dokumentation |
| `style` | Formatanpassung ohne Änderung der Logik (Leerraum, Formatierung, fehlende Semikolons usw.) |
| `refactor` | Refactoring ohne neue Funktion und ohne Defektbehebung |
| `perf` | Codeänderung zur Performance-Optimierung |
| `test` | Ergänzung fehlender Tests oder Korrektur bestehender Tests |
| `build` | Änderung mit Auswirkung auf das Build-System oder externe Abhängigkeiten (z. B. npm, gulp) |
| `ci` | Änderung an Konfiguration und Skripten der kontinuierlichen Integration (z. B. GitHub Actions, CircleCI) |
| `chore` | Sonstiges wie Build, Abhängigkeiten, Toolchain |

### 2.1 Vergleich und Abwägung gängiger Team-Schreibweisen

In unterschiedlichen Kollaborationsmodellen existieren drei verbreitete Schreibweisen; ein Projekt sollte beim Projektstart eine davon festlegen und im gesamten Team einheitlich verwenden:

| Schreibweise | Format | Geeignet für | Einschränkung |
| --- | --- | --- | --- |
| Arbeitsweise | `[任务卡号] 作者: 修改内容` | Teams mit Kanban und Pair Programming | Setzt ein Taskcard-System voraus, ohne Kartennummern nicht anwendbar |
| Konventionelle Weise | `[分类] 组件（可选）: 修改内容` | Teams, die die Historie nach Geschäftsmodulen filtern | Erfordert eine teamweit vereinbarte Kategorienliste, zusätzlicher Aufwand |
| Open-Source-Weise | `<type>(<scope>): <subject>` | Open-Source-Bibliotheken und Anwendungen mit automatischer CHANGELOG-Erzeugung | Viele Typen und Scopes, höherer Lernaufwand |

Dieses Projekt verwendet einheitlich die Open-Source-Schreibweise (also Conventional Commits), da sie maschinenlesbar ist und Änderungsprotokoll sowie Versionsnummern automatisch erzeugt werden können. Arbeitsweise und konventionelle Weise werden ausschließlich in geschlossenen Teams nach Vereinbarung verwendet und dürfen nicht in öffentliche Repositories gelangen.

## 3. Felddefinitionen

| Feld | Pflichtfeld | Typ | Hinweise zum Ausfüllen | Beispiel |
| --- | --- | --- | --- | --- |
| Typ | Ja | Aufzählung | Einer der zehn Typen, keine Eigenkreationen | `feat` |
| Scope | Nein | Text | Modulname, kurzes Wort in Kleinschreibung, ohne Leerzeichen | `parser` |
| Breaking-Markierung | Nein | `!` | Nach Typ oder Scope, vor dem Doppelpunkt | `feat!:` |
| Beschreibung | Ja | Text | Imperativ, Kleinbuchstabe am Anfang, ≤72 Zeichen, kein Punkt am Ende | `add TOML config support` |
| Textkörper | Nein | Text | Erläutert Motivation und Umsetzung, eine Leerzeile Abstand zur Beschreibung | `Allow the parser to read TOML...` |
| Fußnote | Nein | Text | `BREAKING CHANGE:` oder `Refs: #N` | `BREAKING CHANGE: ...` |
| Zugeordnete Anforderung | Nein | `REQ-NNN` | In Textkörper oder Fußnote eintragen, erleichtert die Verfolgung | `Refs: REQ-001` |

## 4. Hinweise zum Ausfüllen

1. **Beschreibung**: Imperativ verwenden (add, fix, remove) und „was getan wurde“ statt „eine Änderung vorgenommen“ schreiben; chinesische Projekte dürfen eine chinesische Beschreibung verwenden, jedoch muss das gesamte Repository einheitlich bleiben.
2. **Scope**: Den Modulnamen statt des Dateinamens verwenden; bei modulübergreifenden Änderungen den Scope weglassen, nicht `all` oder `global` schreiben.
3. **Textkörper**: Nur schreiben, wenn die Beschreibung die Motivation nicht ausreichend erklärt; die Beschreibung nicht wiederholen, keine Prozesschronik verfassen.
4. **Breaking Change**: `feat!:` / `fix!:` und die Fußnote `BREAKING CHANGE:` entweder alternativ oder gemeinsam verwenden; treten sie auf, sind sie zugleich im [Änderungsprotokoll-Spezifikation](./changelog-specification.md) und im [Migrationsleitfaden-Spezifikation](./migration-guide-specification.md) zu dokumentieren.
5. **Atomarität**: Ein Commit behandelt genau eine Sache; Formatierung und Logikänderung werden in zwei Commits getrennt.
6. **Sicherheit**: Schlüssel, Token, personenbezogene Daten und interne Adressen dürfen nicht enthalten sein; vor dem Commit ist ein Secret-Scan durchzuführen (siehe [Sicherheits- und Datenschutz-Spezifikation](./security-and-privacy-specification.md)).
7. **Versionskopplung**: `feat` löst die Erhöhung der Minor-Version aus, `fix` die Erhöhung der Patch-Version, `BREAKING CHANGE` die Erhöhung der Major-Version; Einzelheiten in der [Versionsverwaltungs-Spezifikation](./version-management-specification.md).

Häufige Fehler:

| Fehlerhafte Formulierung | Problem | Korrektur |
| --- | --- | --- |
| `wip`, `update`, `fix bug` | Informationslos, Verstoß gegen H10 | Objekt und Verhalten benennen |
| `feat: Added new feature.` | Kein Imperativ, Großbuchstabe am Anfang, Punkt am Ende | `feat: add config loader` |
| `feat(全部): 优化` | Scope ungültig, Beschreibung unklar | Konkreten Modulnamen und die Änderung angeben |
| Ein Commit enthält Formatierung und Funktionsänderung | Verletzt die Atomarität | In zwei Commits `style:` und `feat:` aufteilen |
| Commit-Nachricht enthält interne Adresse | Informationsleck | Entfernen und Secret-Scan durchführen |

## 5. Vollständiges Beispiel

```text
feat(parser): add support for TOML config

Allow the parser to read TOML configuration files in addition to YAML.
Refs: REQ-001

BREAKING CHANGE: the `config` option now accepts a file path instead of an object.
```

Bedeutung der Felder: `feat` ist der Typ, `parser` der Scope, nach dem Doppelpunkt folgt die kurze Beschreibung; der Textkörper erläutert Motivation und Umsetzung, die Fußnote referenziert die Anforderung; die abschließende Fußnote erklärt den Breaking Change und gibt die Migrationsrichtung an.

Beispiel für eine Fehlerbehebung:

```text
fix(spacing): avoid false positives before Chinese punctuation

The spacing rule previously flagged strings such as 「使用Node.js，」 because
the punctuation check ran after whitespace normalization.

Refs: REQ-004, #142
```

## Verwandte Dateien

- Prüfung der Commit-Historie als Dimension D7: [Prüfungsdimensionsmatrix](./review-dimension-matrix.md)
- Erzeugung des Änderungsprotokolls: [Änderungsprotokoll-Spezifikation](./changelog-specification.md)
- Grundlage der Versionserhöhung: [Versionsverwaltungs-Spezifikation](./version-management-specification.md)
- Prüfpunkte des Code-Reviews: [Code-Review-Spezifikation](./code-review-specification.md)
- Anforderungsverfolgung: [Anforderungs-Verfolgungsmatrix-Spezifikation](./requirements-traceability-matrix-specification.md)
