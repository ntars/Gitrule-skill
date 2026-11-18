# Roadmap-Spezifikation

> Problem, das diese Datei löst: Sie definiert Roadmap-Vorlage, Felder, Statuskennzeichnung und das Prinzip der Unverbindlichkeit, damit Planungen nicht als Zusage formuliert werden und die Konsistenz mit Änderungsprotokoll und Iterationsretrospektive gewahrt bleibt.

## 1. Spezifikationsregeln

1. Die Roadmap muss an gut sichtbarer Stelle den Hinweis tragen: „Diese Roadmap ist eine Planung, keine Lieferzusage“.
2. Konkrete Liefertermine dürfen nicht zugesagt werden; Zielversionen sind als Versionsbereich oder Quartal zu formulieren.
3. Statusänderungen müssen nachvollziehbar dokumentiert werden; gestrichene Einträge erfordern eine Begründung.
4. Abgeschlossene Einträge müssen auf den entsprechenden Eintrag der [Änderungsprotokoll-Spezifikation](./changelog-specification.md) verweisen, damit keine widersprüchlichen Angaben an zwei Stellen entstehen.
5. Die Roadmap betrifft die künftige Planung und darf angepasst oder gestrichen werden; das Änderungsprotokoll betrifft bereits veröffentlichte Fakten und historische Einträge dürfen nicht umgeschrieben werden.
6. Jeder Planeintrag muss mindestens einer Anforderung oder einer Verbesserungsmaßnahme aus der Iteration zugeordnet sein; die Verfolgungsbeziehung ist in der [Anforderungs-Verfolgungsmatrix-Spezifikation](./requirements-traceability-matrix-specification.md) beschrieben.

## 2. Roadmap-Vorlage

```markdown
# Roadmap: {{项目名称}}

> Diese Roadmap ist eine Planung, keine Lieferzusage. Zielversionen und Quartale sind lediglich Erwartungen und können sich mit der Priorisierung ändern.

Version: {{v1.0}} ｜ Aktualisiert von: {{姓名}} ｜ Letzte Prüfung: {{YYYY-MM-DD}}

## Jetzt / Als Nächstes / Später

| Phase | Planeintrag | Status | Zielversion | Zugeordnete Anforderung | Abhängigkeiten | Abnahmekriterien | Änderungsprotokoll |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Jetzt | {{能力描述}} | In Arbeit | {{v1.0}} | {{REQ-001}} | {{无}} | {{可验证条件}} | — |
| Als Nächstes | {{能力描述}} | In Planung | {{v1.1 ~ v1.2}} | {{REQ-008}} | {{计划项 A}} | {{可验证条件}} | — |
| Später | {{能力描述}} | In Planung | {{待定}} | {{REQ-015}} | {{外部依赖}} | {{可验证条件}} | — |
| Gestrichen | {{能力描述}} | Gestrichen | — | {{REQ-020}} | — | — | — |

Status: In Planung / In Arbeit / Abgeschlossen / Gestrichen

## Protokoll der Statusänderungen
| Datum | Planeintrag | Alter Status → Neuer Status | Begründung | Entscheider |
| --- | --- | --- | --- | --- |
| {{YYYY-MM-DD}} | {{计划项}} | {{规划中 → 已取消}} | {{原因}} | {{姓名}} |

## Begründung der Streichung
- {{计划项}}: {{取消原因，如需求变更、依赖 unavailable}}
```

## 3. Vorlage für Planeinträge

```markdown
### {{计划项名称}}

- Status: {{规划中 / 进行中 / 已完成 / 已取消}}
- Zielversion: {{vX.Y / 季度 / 待定}}
- Zugeordnete Anforderung: {{REQ-NNN}}
- Quelle: {{立项书 / 迭代回顾 A-NN / 用户反馈}}
- Abhängigkeiten: {{前置计划项或外部依赖；无则写「无」}}
- Abnahmekriterien: {{可验证的完成条件，须含阈值}}
- Grund der Nichtfertigstellung: {{仅已取消项填写}}
```

## 4. Felddefinitionen

| Feld | Pflichtfeld | Typ | Hinweise zum Ausfüllen | Beispiel |
| --- | --- | --- | --- | --- |
| Planeintrag | Ja | Nominalphrase | Beschreibt die zu liefernde Fähigkeit, keine Aufgabenaktion | `TOML 配置支持` |
| Status | Ja | Aufzählung | In Planung / In Arbeit / Abgeschlossen / Gestrichen | `In Arbeit` |
| Zielversion | Ja | Version / Quartal / Offen | Konkrete Datumsangaben sind unzulässig | `v1.1 ~ v1.2` |
| Zugeordnete Anforderung | Ja | `REQ-NNN` | Muss mit der Projektstart-Nummer übereinstimmen | `REQ-008` |
| Quelle | Ja | Text | Projektstart, Iterationsretrospektive oder Nutzerfeedback | `Iterationsretrospektive A-01` |
| Abhängigkeiten | Ja | Text | Bei fehlenden Abhängigkeiten „Keine“ schreiben, nicht leer lassen | `Abhängigkeit von Planeintrag A` |
| Abnahmekriterien | Ja | Text | Überprüfbar und mit Schwellenwert | `100 Beispieldateien ohne Fehler geparst` |
| Änderungsprotokoll | Bedingt | Link | Pflicht bei abgeschlossenen Einträgen | `[1.0.0]` |
| Streichungsgrund | Bedingt | Text | Pflicht bei gestrichenen Einträgen | `Abhängige externe API abgeschaltet` |

## 5. Hinweise zum Ausfüllen

1. **Phasengliederung**: drei Stufen „Jetzt / Als Nächstes / Später“; „Jetzt“ darf höchstens 3 Einträge enthalten, darüber hinaus muss die Priorisierung neu geordnet werden.
2. **Unverbindlichkeit**: Datumszusagen wie „Release in Q3“ oder „Fertigstellung im Dezember“ sind unzulässig; Erwartungen sind über Versionsnummern oder Quartalsbereiche auszudrücken.
3. **Abnahmekriterien**: Diese müssen objektiv beurteilbar sein; „Verbesserung der Benutzerfreundlichkeit“ ist unzureichend, „Reduktion der Konfigurationsoptionen von 5 auf 2“ ist zulässig.
4. **Statusänderungen**: Bei jeder Änderung wird ein Eintrag ergänzt, der ursprüngliche Wert wird nicht überschrieben; gestrichene Einträge bleiben als Zeile erhalten und erhalten eine Begründung.
5. **Verknüpfung mit dem Abschluss**: Wird der Status auf „Abgeschlossen“ gesetzt, muss zugleich der Anker im Änderungsprotokoll eingetragen werden; ohne entsprechenden Protokolleintrag darf der Abschluss nicht markiert werden.
6. **Verknüpfung mit der Retrospektive**: Werden Verbesserungsmaßnahmen aus der Iterationsretrospektive in die Roadmap aufgenommen, ist in „Quelle“ der Code A-NN anzugeben und die Maßnahme zugleich in der [Iterationsretrospektiven-Spezifikation](./iteration-retrospective-specification.md) zu dokumentieren.
7. **README-Zusammenfassung**: In der README stehen nur die Zusammenfassung der drei Stufen und ein Link; die vollständige Tabelle verbleibt in dieser Datei, siehe [README-Abschnitts-Spezifikation](./readme-sections-specification.md).

Häufige Fehler:

| Fehlerhafte Formulierung | Problem | Korrektur |
| --- | --- | --- |
| „Release im Dezember 2026“ | Stellt eine Zusage dar | Ändern in `v1.2` oder `Q4` |
| Abgeschlossener Eintrag ohne Link zum Änderungsprotokoll | Widersprüchliche Angaben an zwei Stellen | Protokollanker ergänzen |
| Gestrichener Eintrag wird einfach gelöscht | Historie nicht nachvollziehbar | Zeile beibehalten und Begründung angeben |
| Planeintrag lautet „Performance optimieren“ | Kein Abnahmekriterium | Schwellenwertbezogene Kennzahl ergänzen |
| Roadmap mit 20 Einträgen überfüllt | Priorisierung nicht beurteilbar | Auf drei Stufen reduzieren, jede Stufe begrenzen |

## 6. Vollständiges Beispiel

```markdown
# Roadmap: markdown-lint-cli

> Diese Roadmap ist eine Planung, keine Lieferzusage.

Version: v1.0 ｜ Aktualisiert von: Li Si ｜ Letzte Prüfung: 2026-11-20

| Phase | Planeintrag | Status | Zielversion | Zugeordnete Anforderung | Abhängigkeiten | Abnahmekriterien | Änderungsprotokoll |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Jetzt | Kernregelsatz | Abgeschlossen | v1.0.0 | REQ-001~007 | Keine | Erkennungsrate ≥95 % bei 50 Beispieldateien | [1.0.0] |
| Als Nächstes | Integration in Editor-Plugins | In Planung | v1.1 | REQ-003 | Kernregelsatz stabil | In gängigen Editoren aufrufbar | — |
| Später | DSL für benutzerdefinierte Regeln | In Planung | Offen | REQ-018 | Plugin-API stabil | Regeln ohne Quellcodeänderung ergänzbar | — |
| Gestrichen | Cloud-Synchronisierung von Regeln | Gestrichen | — | REQ-020 | — | — | — |

## Protokoll der Statusänderungen
| Datum | Planeintrag | Alter Status → Neuer Status | Begründung | Entscheider |
| --- | --- | --- | --- | --- |
| 2026-11-15 | Cloud-Synchronisierung von Regeln | In Planung → Gestrichen | Keine Ressourcen für serverseitigen Betrieb | Li Si |
```

## Verwandte Dateien

- Versionsbenennung und Zielversion: [Versionsverwaltungs-Spezifikation](./version-management-specification.md)
- Grundlage des Projektstarts und Anforderungsnummern: [Projektstart- und Anforderungs-Spezifikation](./project-initiation-and-requirements-specification.md)
- Externe Dokumentation abgeschlossener Einträge: [Änderungsprotokoll-Spezifikation](./changelog-specification.md)
- Quelle der Verbesserungsmaßnahmen: [Iterationsretrospektiven-Spezifikation](./iteration-retrospective-specification.md)
- Verfolgung von Anforderungen zu Planungen: [Anforderungs-Verfolgungsmatrix-Spezifikation](./requirements-traceability-matrix-specification.md)
- Roadmap-Abschnitt der README: [README-Abschnitts-Spezifikation](./readme-sections-specification.md)
