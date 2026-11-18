# Versionsverwaltungsspezifikation

> Problem, das diese Datei löst: Definiert Regeln der semantischen Versionierung, Versionsentscheidungsaufzeichnungen, Inkrementierungsgrundlagen und Wechselbeziehungen, damit die Versionsnummer die Art der Änderung ausdrücken kann, von Werkzeugen auswertbar ist und mit den Veröffentlichungsartefakten übereinstimmt.

## 1. Spezifikationsbestimmungen

1. Die Versionsnummer folgt der semantischen Versionierung: `MAJOR.MINOR.PATCH`.
2. Die Versionsnummer enthält weder Jahr, Datum noch Build-Nummer als semantischen Kern; veröffentlichte Versionen dürfen ihre Versionsnummer nicht erneut verwenden.
3. Brechende Änderungen sind gebündelt beim Inkrement der Hauptversion zu behandeln und mit einem Migrationsweg zu versehen.
4. Die Versionsnummer stimmt mit dem Tag überein; das Tag-Format lautet `vMAJOR.MINOR.PATCH` (siehe [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md)).
5. Vorabversionen verwenden die Suffixe `-alpha`, `-beta`, `-rc` und müssen vor der Veröffentlichung der stabilen Version validiert werden.

## 2. Format der Versionsnummer und Inkrementierungsgrundlage

| Stelle | Inkrementierungsbedingung | auslösender Commit-Typ | Beispiel |
| --- | --- | --- | --- |
| MAJOR | inkompatible brechende Änderung | `feat!:` / `fix!:` / `BREAKING CHANGE:` | `1.9.2 → 2.0.0` |
| MINOR | abwärtskompatible neue Funktion | `feat` | `1.2.3 → 1.3.0` |
| PATCH | abwärtskompatible Fehlerbehebung | `fix` | `1.2.3 → 1.2.4` |

Format der Vorabversion: `vMAJOR.MINOR.PATCH-alpha.N` / `-beta.N` / `-rc.N`, die Zahl beginnt bei 1 und wird inkrementiert; bei der Veröffentlichung der stabilen Version entfällt das Suffix.

## 3. Vorlage für die Versionsentscheidungsaufzeichnung

```markdown
## Versionsentscheidung: {{X.Y.Z}}

- Entscheidungsdatum: {{YYYY-MM-DD}}
- Entscheidungsbefugte Person: {{姓名}}
- Aktuelle Version: {{X.Y.Z}}
- Zielversion: {{X.Y.Z}}
- Inkrementierte Stelle: {{MAJOR / MINOR / PATCH}}
- Grundlage: {{列举触发的提交类型与变更内容}}

| Änderung | Commit-Typ | Verknüpfte Anforderung | Abwärtskompatibel |
| --- | --- | --- | --- |
| {{变更描述}} | {{feat / fix / BREAKING CHANGE}} | {{REQ-NNN}} | {{是 / 否}} |

- Behandlung brechender Änderungen: {{迁移指南链接 / 不适用}}
- Änderungsprotokolleintrag: {{链接}}
- Tag: {{vX.Y.Z}}
- Veröffentlichungsprüfung: {{已通过 / 待通过}}
```

## 4. Vorlage für das Versionsregister

```markdown
# Versionsregister: {{项目名称}}

| Version | Veröffentlichungsdatum | Typ | Wesentliche Änderung | Tag | Änderungsprotokoll | Status |
| --- | --- | --- | --- | --- | --- | --- |
| {{X.Y.Z}} | {{YYYY-MM-DD}} | {{主版本 / 次版本 / 修订}} | {{一句话}} | {{vX.Y.Z}} | {{链接}} | {{当前 / 历史 / 已废弃}} |
| {{X.Y.Z-rc.1}} | {{YYYY-MM-DD}} | Vorabveröffentlichung | {{一句话}} | {{vX.Y.Z-rc.1}} | {{链接}} | bereits ersetzt |

Status: aktuell / historisch / veraltet / ersetzt
```

## 5. Felddefinitionen

| Feld | Pflicht | Typ | Ausfüllhinweise | Beispiel |
| --- | --- | --- | --- | --- |
| Aktuelle Version | ja | `X.Y.Z` | identisch mit dem letzten Tag | `1.2.3` |
| Zielversion | ja | `X.Y.Z` | nur eine Stelle wird inkrementiert | `1.3.0` |
| Inkrementierte Stelle | ja | Enumeration | MAJOR / MINOR / PATCH | `MINOR` |
| Grundlage | ja | Liste | auslösende Änderungen auflisten, „Routineaktualisierung“ ist unzulässig | `TOML-Unterstützung hinzugefügt` |
| Behandlung brechender Änderungen | bedingt Pflicht | Link | Pflicht bei MAJOR-Inkrement | `[Migrationsleitfaden]` |
| Änderungsprotokolleintrag | ja | Link | verweist auf den entsprechenden Versionsabschnitt | `[1.3.0]` |
| Tag | ja | `vX.Y.Z` | entspricht eins zu eins der Versionsnummer | `v1.3.0` |
| Veröffentlichungsdatum | ja | `YYYY-MM-DD` | maßgeblich ist das Datum des Tag-Setzens | `2026-11-20` |
| Status | ja | Enumeration | aktuell / historisch / veraltet / ersetzt | `aktuell` |

## 6. Ausfüllhinweise

1. **Inkrement einer Stelle**: Pro Veröffentlichung wird nur eine Stelle inkrementiert; liegen feat und BREAKING CHANGE gleichzeitig vor, gilt die höchste Stelle (MAJOR), die übrigen Änderungen werden in diese Version aufgenommen.
2. **Bündelung brechender Änderungen**: Mehrere brechende Änderungen werden in derselben Hauptversion veröffentlicht, um aufeinanderfolgende MAJOR-Inkremente zu vermeiden.
3. **Keine Wiederverwendung**: Eine veröffentlichte Versionsnummer bleibt dauerhaft belegt; bei Rücknahme einer Veröffentlichung wird PATCH inkrementiert und eine Revisionsversion veröffentlicht, die ursprüngliche Nummer wird nicht wiederverwendet.
4. **Vorabversionen**: `alpha` dient der internen Validierung, `beta` dem öffentlichen Probelauf, `rc` der Veröffentlichungskandidatur; jede Stufe muss CI bestehen.
5. **Konsistenzprüfung**: Die Versionsnummer muss an fünf Stellen übereinstimmen – Tag, Änderungsprotokoll, Release Notes, Bereitstellungsprotokoll und Versionsregister; bei Abweichung ist der Tag maßgeblich und die übrigen Stellen sind zu korrigieren.
6. **Wechselbeziehungen**: Die Inkrementierungsgrundlage stammt aus dem Typ der [Commit-Nachrichten-Spezifikation](./commit-message-specification.md); die nutzerseitige Erläuterung siehe [Änderungsprotokoll-Spezifikation](./changelog-specification.md); den Upgrade-Pfad siehe [Migrationsleitfaden-Spezifikation](./migration-guide-specification.md).

Häufige Fehler:

| Fehlerhafte Schreibweise | Problem | Korrektur |
| --- | --- | --- |
| `v2026.11` | Datum als semantischer Kern | auf `v2.1.0` ändern |
| zwei Stellen im selben Versionsschritt inkrementiert | semantische Verwirrung | nur die höchste Stelle inkrementieren |
| Wiederverwendung einer zurückgezogenen Versionsnummer | Artefakte nicht unterscheidbar | PATCH inkrementieren und Revisionsversion veröffentlichen |
| MAJOR-Inkrement ohne Migrationsleitfaden | Nutzende können nicht upgraden | Migrationsleitfaden ergänzen und verlinken |
| Versionsnummer nur im Tag vorhanden | Register und Protokoll weichen ab | an fünf Stellen synchronisieren |

## 7. Vollständiges Beispiel

```markdown
## Versionsentscheidung: 2.0.0

- Entscheidungsdatum: 2026-12-01
- Entscheidungsbefugte Person: 李四
- Aktuelle Version: 1.9.2
- Zielversion: 2.0.0
- Inkrementierte Stelle: MAJOR
- Grundlage: Das Format der Konfigurationsdatei wurde von einem Objekt auf einen Dateipfad geändert, was eine inkompatible Änderung darstellt.

| Änderung | Commit-Typ | Verknüpfte Anforderung | Abwärtskompatibel |
| --- | --- | --- | --- |
| Konfigurationsdatei auf Pfadangabe umgestellt | BREAKING CHANGE | REQ-021 | ja |
| TOML-Parsing hinzugefügt | feat | REQ-001 | nein |

- Behandlung brechender Änderungen: [Migrationsleitfaden v2.0]
- Änderungsprotokolleintrag: [2.0.0]
- Tag: v2.0.0
- Veröffentlichungsprüfung: bestanden
```

## Verwandte Dateien

- Commit-Typen und Kennzeichnung brechender Änderungen: [Commit-Nachrichten-Spezifikation](./commit-message-specification.md)
- Tag und Release Notes: [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md)
- Änderungsprotokolleinträge: [Änderungsprotokoll-Spezifikation](./changelog-specification.md)
- Upgrade-Pfad: [Migrationsleitfaden-Spezifikation](./migration-guide-specification.md)
- Herkunft der Zielversion: [Roadmap-Spezifikation](./roadmap-specification.md)
- Versionskonsistenz der Bereitstellungsaufzeichnung: [Bereitstellungs- und Rollback-Spezifikation](./deployment-and-rollback-specification.md)
