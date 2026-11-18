# CI-Workflow-Spezifikation

> Problem, das diese Datei löst: Sie definiert Auslösebedingungen, Aufgabenaufteilung, Cache-Strategie und Sicherheitskonfiguration der Workflows für kontinuierliche Integration in `.github/workflows/*.yml`, damit Build, Tests und Prüfungen reproduzierbar und auditierbar bleiben.

## 1. Designprinzipien

1. **Einzelverantwortung**: Jeder Workflow ist nur für eine Zielkategorie zuständig (Build, Tests, Veröffentlichung, Dokumentationsbereitstellung); Veröffentlichung und Tests dürfen nicht in einem Workflow vermischt werden.
2. **Schnelles Feedback**: Leichtgewichtige Prüfungen (Lint, Formatierung) zuerst, zeitintensive Aufgaben (vollständige Testmatrix) danach.
3. **Reproduzierbarkeit**: Abhängigkeitsversionen sind festzuschreiben und Actions in fester Version zu verwenden; Caches dienen nur der Beschleunigung und verändern das Ergebnis nicht.
4. **Minimale Berechtigungen**: Workflows erhalten Berechtigungen aufgabenbezogen, standardmäßig nur Leserechte; Veröffentlichungsaufgaben erhalten gesonderte erhöhte Rechte (siehe [Sicherheits- und Datenschutz-Spezifikation](./security-and-privacy-specification.md)).

## 2. Dateistruktur

### 2.1 Benennung und Pfad

- Der Pfad ist fest auf `.github/workflows/*.yml` festgelegt.
- Dateinamen verwenden Kleinbuchstaben und Bindestriche und werden nach Zuständigkeit benannt, etwa `ci.yml`, `release.yml`, `docs.yml`.
- Das Feld `name` eines Workflows muss semantisch zum Dateinamen passen.

### 2.2 Pflichtblöcke

| Block | Zweck | Anforderung |
| --- | --- | --- |
| `name` | Anzeigename des Workflows | Prägnant, Zuständigkeit erkennbar |
| `on` | Auslösebedingungen | Branch, Pfad oder Ereignis eindeutig benennen |
| `permissions` | Berechtigungserklärung | Explizit deklariert, standardmäßig minimal |
| `jobs` | Aufgabensammlung | Nach Zuständigkeit aufgeteilt |

### 2.3 Gestaltung der Auslösebedingungen

| Auslösendes Ereignis | Geeignet für | Hinweis |
| --- | --- | --- |
| `push` | Haupt- und Veröffentlichungsbranches | Branch-Bereich einschränken, um Auslösung auf allen Branches zu vermeiden |
| `pull_request` | Alle PRs | Prüfung vor der Zusammenführung sicherstellen |
| `workflow_dispatch` | Manuelle Auslösung | Für kontrollierte Vorgänge wie Veröffentlichung und Rollback |
| `schedule` | Zeitgesteuerte Aufgaben | Für Prüfung von Abhängigkeitsaktualisierungen und nächtliche Builds |
| `release` | Aktionen nach der Veröffentlichung | Für das Hochladen von Artefakten und Ankündigungen |

## 3. Aufgabenaufteilung

Empfohlene Phasenreihenfolge:

1. **Statische Analyse**: Formatierung, Lint, Typprüfung.
2. **Build**: Erzeugung der Build-Artefakte zur Wiederverwendung durch nachfolgende Aufgaben.
3. **Tests**: Unit-Tests, Integrationstests, parallelisierbar über eine Matrix.
4. **Artefaktprüfung**: Prüfung von Größe, Signatur oder Integrität der Build-Artefakte.
5. **Veröffentlichung**: Nur bei vollständig grüner CI und erfüllten Bedingungen (siehe [Push- und Veröffentlichungs-Spezifikation](./push-and-release-specification.md)).

Abhängigkeiten zwischen Aufgaben werden über `needs` deklariert, damit ein Fehler sofort abbricht; nachfolgende Aufgaben dürfen im Fehlerzustand nicht fortgesetzt werden.

## 4. Matrix-Build

`strategy.matrix` wird zur Abdeckung mehrerer Versionen und Plattformen verwendet:

```yaml
strategy:
  fail-fast: false
  matrix:
    os: [ubuntu-latest, macos-latest, windows-latest]
    node-version: [18, 20, 22]
```

Anforderungen:

- Die Versionen decken die im Projekt als unterstützt erklärte minimale und maximale Version ab (siehe [Kompatibilitätshinweise](./readme-sections-specification.md) Kapitel 14).
- `fail-fast` wird auf `false` gesetzt, damit alle Kombinationen vollständig durchlaufen und Kompatibilitätsprobleme lokalisiert werden können.
- Höchstens drei Matrixdimensionen, um eine Kombinationslawine zu vermeiden.

## 5. Cache-Strategie

| Cache-Objekt | Empfohlener Schlüssel | Hinweis |
| --- | --- | --- |
| Abhängigkeitsverzeichnis | Hash der Lock-Datei des Paketmanagers | Bei Änderung der Lock-Datei ungültig |
| Build-Artefakte | Hash von Quellcode und Konfiguration | Identisch mit den Build-Eingaben |
| Toolchain | Versionsnummer | Bei Versionsaktualisierung ungültig |

Caches beschleunigen nur und verändern das Build-Ergebnis nicht; bei einem Cache-Treffer sind die vollständigen Tests dennoch auszuführen.

## 6. Sicherheitskonfiguration

1. Geheimnisse werden über Repository-Secrets injiziert; das Schreiben in Workflow-Dateien oder Logs ist verboten.
2. Jeder Workflow deklariert `permissions` explizit, standardmäßig `contents: read`.
3. Referenzen auf Actions von Drittanbietern verwenden feste Versionen oder Commit-Hashes; floatende Tags sind zu vermeiden.
4. Bei PRs aus Forks ist die Injektion von Secrets verboten, um Rechteausweitungsangriffe zu verhindern.
5. Veröffentlichungsaufgaben sind von den Hauptprüfungen getrennt und werden nur auf geschützten Branches oder Tags ausgelöst.

## 7. Status-Badge

Der Workflow muss für die README ein Status-Badge bereitstellen, im Format:

```markdown
[![CI](https://github.com/{owner}/{repo}/actions/workflows/ci.yml/badge.svg)](https://github.com/{owner}/{repo}/actions/workflows/ci.yml)
```

Parameter und Anordnung der Badges siehe [Badge-Spezifikation](./badge-specification.md).

## 8. Verbotene Praktiken

1. Das Hartkodieren von Geheimnissen oder internen Adressen in Workflows ist verboten.
2. Die Verwendung von `continue-on-error` zur Verschleierung von Testfehlern ist verboten.
3. Das Konfigurieren mehrerer widersprüchlicher Auslöseregeln für dieselbe Bedingung ist verboten.
4. Die Ausführung einer Veröffentlichung bei nicht bestandener Hauptprüfung ist verboten.

## Verwandte Dateien

- Abgrenzung der Dateizuständigkeiten: [Dokumentationsmatrix](./document-matrix.md)
- Lokaler Build und lokale Tests: [Test-Spezifikation](./testing-specification.md)
- Verknüpfung mit der Veröffentlichung: [Push- und Veröffentlichungs-Spezifikation](./push-and-release-specification.md)
- Automatisierte Prüfungen gehören zu Dimension D9, siehe [Prüfungsdimensionsmatrix](./review-dimension-matrix.md)
- Rote Linie für Geheimnisse: H3 der [Harten Regeln](./hard-rules.md)
