# Contributing-Guide-Vorlage

> Problem, das diese Datei löst: Stellt eine direkt kopierbare Vorlage für einen Contributing Guide bereit, damit Projekte `CONTRIBUTING.md` erzeugen können; sie deckt Beteiligungswege, Einrichtung der Umgebung, Branch-Modell, Commit-Regeln, PR-Anforderungen, Testanforderungen, Verhaltenskodex und Lizenzhinweis ab, und die begleitenden Ausfüllhinweise decken die Zuschnittweise für die einzelnen Projekttypen ab.

## 1. Verwendungshinweise

1. Den gesamten Inhalt von „Vorlagentext“ aus Abschnitt 3 kopieren und als `CONTRIBUTING.md` im Projektwurzelverzeichnis neu anlegen.
2. Gemäß Abschnitt 4 die Platzhalter ersetzen; alle Befehle müssen reale, direkt ausführbare Befehle sein.
3. Gemäß den Szenariovarianten in Abschnitt 5 zuschneiden: Bei Dokumentationsprojekten den Abschnitt mit den Testbefehlen entfernen und den Issue- und PR-Ablauf beibehalten.
4. Grundlage der Regeln siehe [Contributing-Guide-Spezifikation](./contribution-guide-specification.md); Details zu Branches und Commits siehe [Git-Workflow- und Branching-Spezifikation](./git-workflow-and-branching-specification.md) sowie [Commit-Nachrichten-Spezifikation](./commit-message-specification.md).

## 2. Anpassungsprinzipien

- **Ausführbar**: Befehle mit vollständigem Arbeitsverzeichnis und Abhängigkeitsvoraussetzungen schreiben; „Abhängigkeiten installieren“ ohne konkreten Befehl ist unzulässig.
- **Mit Auslösebedingung**: Jeder Schritt nennt, wann er auszuführen ist, und das erwartete Ergebnis.
- **Nicht inhaltsleer**: „PRs sind willkommen“ ohne inhaltlichen Ablauf ist unzulässig; dies entspricht der Prüfung zur Community-Governance im [Qualitätstor](./quality-gate.md).
- **Verweisen statt kopieren**: Regeln zu Commits und Tests verweisen auf die jeweilige Spezifikation; der Volltext wird in dieser Datei nicht wiederholt.

## 3. Vorlagentext

````markdown
# Contributing Guide

> Diese Datei erläutert die Beteiligung an {{项目名称}} und richtet sich an externe Beitragende und erstmalig Beteiligte.

## Beteiligungswege

| Weg | Anwendungsfall | Einstieg |
| --- | --- | --- |
| Diskussion in Issues | Funktionsvorschläge, Rückmeldung zu Problemen | {{议题入口}} |
| Verbesserung der Dokumentation | Tippfehler, Ergänzung von Beispielen, strukturelle Optimierung | Direkt einen PR einreichen |
| Code-Beitrag | Fehlerbehebung, Umsetzung von Funktionen | Siehe Ablauf unten |
| Rückmeldung zu Problemen | Blockierte Nutzung, Reproduktion von Anomalien | {{问题反馈入口}} |

## Einrichtung der Entwicklungsumgebung

Voraussetzungen: {{环境前提}}

```bash
# Repository klonen
git clone {{仓库地址}}
cd {{项目目录名}}

# Abhängigkeiten installieren
{{依赖安装命令}}

# Lokal ausführen
{{本地运行命令}}
```

Erwartetes Ergebnis: {{验证本地环境可用的方式}}

## Branch-Modell

- Vom {{基准分支}} einen persönlichen Branch abzweigen, Namensformat `{{分支命名格式}}` (zum Beispiel `feat/kurzbeschreibung`).
- Jeder PR behandelt nur eine Sache; bei zu großem Änderungsumfang bitte aufteilen.
- Direkte Commits auf {{受保护分支}} sind unzulässig; die Zusammenführung muss über einen PR erfolgen.

## Commit-Regeln

Commit-Nachrichten folgen den Conventional Commits, Format `type(scope): subject`. Häufige Typen: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`. Beispiel:

```text
feat(cli): add config file support
```

Vollständige Regeln siehe [Commit-Nachrichten-Spezifikation]({{提交规范链接}}).

## PR-Anforderungen

Vor dem Einreichen eines PR bitte die folgenden Selbstprüfungen abschließen:

- [ ] Der Änderungsumfang ist einheitlich und es existiert ein zugehöriges Issue oder eine Erläuterung.
- [ ] Die Commit-Nachrichten entsprechen dem obigen Format.
- [ ] Der lokale Aufruf von `{{测试命令}}` läuft vollständig durch.
- [ ] Die Dokumentation wird mit dem Code synchron aktualisiert.
- [ ] Es wurden keine Schlüssel, privaten Schlüssel oder sensiblen Informationen eingebracht.
- [ ] Die Beschreibung nennt Änderungsinhalt, Grund und Verifikationsweise.

## Testanforderungen

| Prüfpunkt | Befehl | Bestehenskriterium |
| --- | --- | --- |
| Unit-Tests | `{{单元测试命令}}` | Vollständig bestanden |
| Statische Analyse | `{{lint 命令}}` | Keine Fehler |
| Build-Verifikation | `{{构建命令}}` | Build erfolgreich |

Abdeckungsschwelle: {{覆盖率要求}}.

## Verhaltenskodex

Die Beteiligung an diesem Projekt gilt als Zustimmung zur Einhaltung des [Verhaltenskodex](./CODE_OF_CONDUCT.md).

## Issue-Regeln

- Vor dem Fragen vorhandene Issues durchsuchen, um Doppelungen zu vermeiden.
- Fehlerberichte müssen enthalten: Umgebungsinformationen, Reproduktionsschritte, erwartetes Ergebnis, tatsächliches Ergebnis, Fehlerprotokoll.
- Funktionsvorschläge müssen den Anwendungsfall und die Alternative bei Nichtumsetzung nennen.

## Lizenzhinweis

Beiträge unterliegen standardmäßig der Lizenz dieses Projekts {{许可证名称及 SPDX 标识符}}, deren Volltext in [LICENSE](./LICENSE) steht. Mit dem Einreichen wird bestätigt, dass die Berechtigung besteht, den Beitrag unter dieser Lizenz zu lizenzieren.
````

## 4. Platzhaltertabelle und Felddefinitionen

| Platzhalter | Pflicht | Felddefinition | Ausfüllbeispiel |
| --- | --- | --- | --- |
| `{{项目名称}}` | ja | Öffentlicher Projektname | `FooBar` |
| `{{议题入口}}` | ja | Real erreichbare Issue-Adresse | `https://github.com/owner/repo/issues` |
| `{{问题反馈入口}}` | nein | Gesonderter Kanal, sofern abweichend vom Issue-Einstieg | `https://github.com/owner/repo/issues/new` |
| `{{环境前提}}` | ja | Sprachversion, Paketmanager und Systemabhängigkeiten | `Node.js 20+, pnpm 8+` |
| `{{仓库地址}}` | ja | Klonbare Repository-Adresse | `https://github.com/owner/repo.git` |
| `{{项目目录名}}` | ja | Verzeichnisname nach dem Klonen | `repo` |
| `{{依赖安装命令}}` | ja | Tatsächlicher Installationsbefehl | `pnpm install` |
| `{{本地运行命令}}` | ja | Tatsächlicher Startbefehl | `pnpm dev` |
| `{{验证本地环境可用的方式}}` | ja | Beobachtbares Erfolgsmerkmal | `Aufruf von localhost:3000 zeigt die Startseite` |
| `{{基准分支}}` | ja | Ausgangsbranch, von dem abgezweigt wird | `main` |
| `{{分支命名格式}}` | ja | Regel für die Branch-Benennung | `feat/kurzbeschreibung` |
| `{{受保护分支}}` | ja | Branch, auf dem direkte Commits unzulässig sind | `main` |
| `{{提交规范链接}}` | nein | Adresse der internen oder externen Commit-Regeln | `./docs/COMMIT_CONVENTION.md` |
| `{{测试命令}}` | ja | Tatsächlicher Testbefehl | `pnpm test` |
| `{{lint 命令}}` | ja | Tatsächlicher Befehl der statischen Analyse | `pnpm lint` |
| `{{构建命令}}` | ja | Tatsächlicher Build-Befehl | `pnpm build` |
| `{{覆盖率要求}}` | nein | Abdeckungsschwelle für neuen Code | `Neuer Code nicht unter 80 %` |
| `{{许可证名称及 SPDX 标识符}}` | ja | Vollständiger Name und SPDX-Kennung der Projektlizenz | `MIT-Lizenz (MIT)` |

## 5. Ausfüllhinweise und Szenariovarianten

| Szenario | Beizubehaltende Abschnitte | Entfallende Abschnitte | Anpassungsschwerpunkte |
| --- | --- | --- | --- |
| Codeprojekt | Alle | Keine | Befehle müssen tatsächlich ausgeführt und verifiziert werden |
| Dokumentationsprojekt | Beteiligungswege, PR-Anforderungen, Verhaltenskodex, Lizenz | Testanforderungen, Einrichtung der Entwicklungsumgebung | Testtabelle entfernen, PR-Selbstprüfung beibehalten |
| Persönliches Projekt | Beteiligungswege, PR-Anforderungen, Verhaltenskodex, Lizenz | Einrichtung der Umgebung kann gestrafft werden | Klarstellen, ob externe Beiträge angenommen werden |
| Unternehmensprojekt | Alle | Keine | Link zum Contributor License Agreement (CLA) und rechtliche Anforderungen ergänzen |

Gegenüberstellung häufiger Fehler:

| Fehlerhafte Schreibweise | Folge | Korrekte Schreibweise |
| --- | --- | --- |
| „Jede Form von Beitrag ist willkommen“ | Kein konkreter Weg, Beitragende wissen nicht, wo sie ansetzen sollen | Tabelle der Beteiligungswege und Einstiege auflisten |
| „Einfach die Tests ausführen“ | Befehl und Bestehenskriterium unbekannt | Befehl, Bestehenskriterium und Abdeckungsschwelle nennen |
| Befehl `npm install` bei einem Projekt mit pnpm | Befehl nicht ausführbar | Übereinstimmung mit der tatsächlichen Lockfile |

## 6. Vollständiges Beispiel

Im Folgenden ein ausgefülltes Beispiel des Befehlsabschnitts, nur als Formatreferenz.

```bash
# Repository klonen
git clone https://github.com/owner/repo.git
cd repo

# Abhängigkeiten installieren
pnpm install

# Lokal ausführen
pnpm dev
```

Erwartetes Ergebnis: Aufruf von localhost:3000 zeigt die Startseite.

## Verwandte Dateien

- Zugehörige Spezifikation: [Contributing-Guide-Spezifikation](./contribution-guide-specification.md)
- Begleitende Vorlagen: [Verhaltenskodex-Vorlage](./code-of-conduct-template.md), [SECURITY-Vorlage](./security-template.md)
- Testdetails: [Test-Spezifikation](./testing-specification.md)
- Dimension Community-Governance: [Audit-Dimensionsmatrix](./review-dimension-matrix.md)
- Zurück zum chinesischen Index: [README](./README.md)
