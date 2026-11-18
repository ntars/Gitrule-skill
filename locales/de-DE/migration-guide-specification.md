# Migrationsleitfaden-Spezifikation

> Problem, das diese Datei löst: Definiert Struktur, Inhaltselemente und Veröffentlichungszeitpunkt von Migrationsleitfäden bei Breaking Changes, damit Nutzende schrittweise und reibungslos von einer alten auf eine neue Version aktualisieren können.

## 1. Auslösebedingungen

Ein Migrationsleitfaden ist erforderlich, wenn einer der folgenden Fälle eintritt:

1. Die Commit-Nachricht enthält `BREAKING CHANGE:` oder `feat!:` / `fix!:` (siehe [Commit-Nachrichten-Spezifikation](./commit-message-specification.md)).
2. Schlüsselname, Standardwert oder Priorität einer Konfiguration ändern sich.
3. Signatur einer API, Rückgabestruktur oder Fehlercode ändern sich.
4. Die minimale Laufzeitversion wird angehoben oder die Unterstützung einer Plattform entfällt.
5. Verzeichnisstruktur oder Dateibenennung ändern sich und beeinflussen die Referenzpfade der Nutzenden.

## 2. Dateispeicherort und Benennung

1. Geringfügige Migrationshinweise werden in den entsprechenden Versionseintrag in `CHANGELOG.md` aufgenommen.
2. Bei größeren Änderungen mit mehrschrittigen Vorgängen wird eine eigene Datei unter `docs/migration/` angelegt und nach Version benannt, etwa `docs/migration/v2.md`.
3. Der vollständige Migrationspfad über Hauptversionen hinweg wird in `docs/migration/README.md` indexiert.
4. Die README enthält nur Migrationshinweise und Links, nicht die Schritte selbst (siehe [Dokumentationsmatrix](./document-matrix.md)).

## 3. Dokumentstruktur

Ein Migrationsleitfaden ist in der folgenden Reihenfolge zu gliedern:

1. **Titel und Version**: Ausgangsversion und Zielversion angeben, etwa „Migration von v1.x auf v2.0“.
2. **Auswirkungsübersicht**: Änderungskategorien und Auswirkungsumfang auflisten und angeben, welche Nutzenden migrieren müssen.
3. **Voraussetzungen**: Vor der Migration abzuschließende Vorbereitungen, etwa Sicherungen und Aktualisierung der Umgebungsversion.
4. **Änderungsliste**: Breaking Changes einzeln auflisten, jeweils mit „altes Verhalten“, „neues Verhalten“ und „Änderungsgrund“.
5. **Migrationsschritte**: Ausführbare Vorgänge nummeriert auflisten und Befehle oder Codebeispiele angeben.
6. **Verifikationsweise**: Wie der Erfolg nach der Migration bestätigt wird, mit Prüfbefehlen oder erwarteter Ausgabe.
7. **Rollback-Verfahren**: Wie bei fehlgeschlagener Migration auf die alte Version zurückgegangen wird.
8. **Häufige Fragen**: Häufige Fragen und Antworten auflisten.
9. **Hilfe erhalten**: Auf Issues, Diskussionsbereich oder Dokumentationsseite verweisen.

### 3.1 Kopierbare Leervorlage

Die folgende Vorlage entspricht Punkt für Punkt der neunteiligen Struktur aus Abschnitt 3; nach dem Kopieren sind nur die Platzhalter zu ersetzen:

````markdown
# Migration von {{源版本}} auf {{目标版本}}

> Dieser Leitfaden beschreibt alle Vorgänge für die Aktualisierung von {{源版本}} auf {{目标版本}} und gilt für {{适用使用者范围}}.

## 1. Auswirkungsübersicht

| Änderungskategorie | Konkreter Inhalt | Auswirkungsumfang | Migration erforderlich |
| --- | --- | --- | --- |
| {{变更类别}} | {{变更内容}} | {{受影响的使用者场景}} | {{是否必须迁移}} |

## 2. Voraussetzungen

- {{前置准备}}
- {{检查项与确认命令}}

## 3. Änderungsliste

### {{变更项名称}}

- Altes Verhalten: {{旧版本行为}}
- Neues Verhalten: {{新版本行为}}
- Änderungsgrund: {{变更原因}}

Vor der Migration:

```{{代码语言}}
{{旧配置或旧代码}}
```

Nach der Migration:

```{{代码语言}}
{{新配置或新代码}}
```

## 4. Migrationsschritte

1. {{迁移步骤}}
2. {{迁移步骤}}
3. {{人工处理步骤}}

## 5. Verifikationsweise

```bash
{{可独立运行的检查命令}}
```

Erwartete Ausgabe: {{预期结果}}

## 6. Rollback-Verfahren

1. {{恢复旧版本的操作}}
2. {{恢复旧配置的操作}}

## 7. Häufige Fragen

### {{问题}}

Antwort: {{解答}}

## 8. Hilfe erhalten

- Problemrückmeldung: {{issue 地址}}
- Diskussionsbereich: {{讨论区地址}}
- Zugehörige Dokumentation: {{文档链接}}
````

Platzhalterreferenz:

| Platzhalter | Pflicht | Ausfüllhinweise |
| --- | --- | --- |
| `{{源版本}}` / `{{目标版本}}` | ja | Identisch mit dem Ziel-Tag, Format `vX.Y.Z` |
| `{{适用使用者范围}}` | ja | Angeben, welche Nutzenden migrieren müssen; vage Formulierungen vermeiden |
| `{{变更类别}}` | ja | Mindestens eine der vier Kategorien Konfiguration, API, Laufzeit, Verzeichnis |
| `{{是否必须迁移}}` | ja | Angeben, ob diese Änderung eine Migration durch die Nutzenden erfordert |
| `{{旧行为}}` / `{{新行为}}` | ja | Punkt für Punkt gegenüberstellen; nur eine Seite ist unzulässig |
| `{{代码语言}}` | ja | Sprachkennung des Codeblocks, etwa `yaml`, `json`, `js` |
| `{{前置准备}}` | ja | Vor der Migration abzuschließende Sicherungen und Umgebungsprüfungen |
| `{{迁移步骤}}` | ja | Jeder Schritt direkt ausführbar, mit Befehl oder Code |
| `{{人工处理步骤}}` | ja | Nicht automatisch migrierbare Schritte sind hier ausdrücklich zu kennzeichnen |
| `{{检查命令}}` / `{{预期结果}}` | ja | Befehl unabhängig ausführbar, Ergebnis beurteilbar |
| `{{回滚方式}}` | ja | Darf nicht entfallen, siehe verbotene Praktiken in Abschnitt 7 |

## 4. Inhaltliche Anforderungen

### 4.1 Beispiel für die Änderungsgegenüberstellung

```markdown
### Konfigurationseintrag `timeout` umbenannt in `timeoutMs`

- Altes Verhalten: In der Konfigurationsdatei wird `timeout: 5000` verwendet, Einheit Sekunden.
- Neues Verhalten: Stattdessen wird `timeoutMs: 5000` verwendet, Einheit Millisekunden.
- Änderungsgrund: Zeiteinheiten vereinheitlichen, um Abweichungen zu API-Parametern zu vermeiden.

Vor der Migration:

```yaml
timeout: 5
```

Nach der Migration:

```yaml
timeoutMs: 5000
```

### 4.2 Anforderungen an die Abfassung

1. Für jeden Schritt einen direkt ausführbaren Befehl oder Code angeben; die bloße Beschreibung „Konfiguration ändern“ ist unzulässig.
2. Eine Gegenüberstellung vor und nach der Migration angeben, um den punktweisen Abgleich zu erleichtern.
3. Schritte, die nicht automatisch migrierbar sind und manuelle Bearbeitung erfordern, ausdrücklich kennzeichnen.
4. Der Auswirkungsumfang muss konkret sein; vage Formulierungen wie „kann einige Nutzende betreffen“ sind zu vermeiden.
5. Prüfbefehle müssen unabhängig ausführbar sein und die erwartete Ausgabe enthalten.

## 5. Veröffentlichungszeitpunkt und Verknüpfungen

1. Der Migrationsleitfaden ist zeitgleich mit der Version zu veröffentlichen, die Breaking Changes enthält; eine Verzögerung ist unzulässig.
2. Der entsprechende Eintrag in `CHANGELOG.md` muss auf den Migrationsleitfaden verlinken (siehe [Änderungsprotokoll-Spezifikation](./changelog-specification.md)).
3. Der Abschnitt zu Breaking Changes in der PR-Vorlage muss zum Ausfüllen der Migrationsweise auffordern (siehe [Issue- und PR-Vorlagen-Spezifikation](./issue-and-pr-template-specification.md)).
4. Versionsnummern folgen der semantischen Versionierung; bei Breaking Changes ist die Hauptversion zu erhöhen (siehe [Versionsverwaltungs-Spezifikation](./version-management-specification.md)).
5. Die README weist an prominenter Stelle darauf hin, dass Nutzende älterer Versionen den Migrationsleitfaden lesen sollen.

## 6. Abschreibungs- und Aufbewahrungsstrategie

1. Migrationsleitfäden sind dauerhaft aufzubewahren und dürfen nach Veröffentlichung einer neuen Version nicht gelöscht werden.
2. Dokumentation älterer Versionen kann als „nicht mehr gepflegt“ gekennzeichnet werden, der Einstieg ist jedoch zu erhalten.
3. Aktualisierungen über mehrere Hauptversionen hinweg müssen einen schrittweisen Pfad bieten; ein Sprung über alle Änderungen auf einmal darf nicht verlangt werden.

## 7. Verbotene Praktiken

1. Die bloße Angabe „es gibt Breaking Changes, bitte selbst anpassen“ ist unzulässig.
2. Das Weglassen des Rollback-Verfahrens ist unzulässig.
3. Die Verwendung nicht ausführbaren Pseudocodes in Migrationsschritten ist unzulässig.
4. Das Löschen von Migrationsleitfäden historischer Versionen ist unzulässig.

## Verwandte Dateien

- Struktur des Änderungsprotokolls siehe [Änderungsprotokoll-Spezifikation](./changelog-specification.md)
- Regeln zur Versionserhöhung siehe [Versionsverwaltungs-Spezifikation](./version-management-specification.md)
- Breaking-Erklärungen in Commit-Nachrichten siehe [Commit-Nachrichten-Spezifikation](./commit-message-specification.md)
- Abgrenzung der Dokumentationszuständigkeiten siehe [Dokumentationsmatrix](./document-matrix.md)
- Veröffentlichungsablauf siehe [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md)
