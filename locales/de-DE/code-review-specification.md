# Code-Review-Spezifikation

> Problem, das diese Datei löst: Sie definiert Vorlage der Pull-Request-Beschreibung, Vorlage der Review-Anmerkungen, Review-Protokoll, Felder und Ablauf, um Zusammenführungsqualität und Wissenstransfer sicherzustellen.

## 1. Spezifikationsregeln

1. Autoren müssen in der PR-Beschreibung Zweck der Änderung, Auswirkungsumfang und Ergebnisse der Selbstprüfung angeben; die Vorlage steht in der [Git-Workflow- und Branch-Spezifikation](./git-workflow-and-branching-specification.md).
2. Prüfende müssen konkrete, ausführbare Anmerkungen geben und zwischen „Muss geändert werden“ und „Empfehlung“ unterscheiden.
3. Vor der Zusammenführung muss mindestens eine prüfende Person zugestimmt haben und die CI vollständig grün sein (entspricht der harten Regel H9); Autoren dürfen ihren eigenen PR nicht selbst freigeben.
4. Bei Uneinigkeit über Review-Anmerkungen erfolgt eine Eskalation an die Maintainer zur Entscheidung (siehe [Verhaltenskodex-Spezifikation](./code-of-conduct-specification.md)).
5. Nach der Zusammenführung ist der Quellbranch zu löschen, um die Branchliste übersichtlich zu halten.

## 2. Review-Checkliste

Prüfende müssen die Punkte einzeln bestätigen:

| # | Dimension | Prüfpunkt | Bewertung |
| --- | --- | --- | --- |
| 1 | Korrektheit | Logik korrekt, Grenzfälle und Ausnahmen behandelt | Bestanden / Änderung erforderlich |
| 2 | Tests | Änderung verfügt über zugehörige Tests, Tests bestehen | Bestanden / Änderung erforderlich |
| 3 | Stil | Entspricht der [Code-Stil-Spezifikation](./code-style-specification.md) | Bestanden / Änderung erforderlich |
| 4 | Sicherheit | Keine sensiblen Informationen, kein Injektionsrisiko, korrekte Berechtigungsprüfung | Bestanden / Änderung erforderlich |
| 5 | Dokumentation | Schnittstellen- oder Verhaltensänderungen sind in der Dokumentation nachgeführt | Bestanden / Änderung erforderlich |
| 6 | Umfang | Änderung ist fokussiert, keine sachfremden Anpassungen | Bestanden / Änderung erforderlich |
| 7 | Commit-Nachricht | Entspricht der [Commit-Nachrichten-Spezifikation](./commit-message-specification.md) | Bestanden / Änderung erforderlich |
| 8 | Verfolgung | Anforderungs-Verfolgungsmatrix ist aktualisiert | Bestanden / Änderung erforderlich |

## 3. Vorlage für Review-Anmerkungen

```markdown
### Anmerkung {{序号}}: {{一句话标题}}

- Stufe: {{必须修改 / 建议 / 提问}}
- Position: {{文件路径:行号}}
- Problem: {{描述可观察的问题，不评价人}}
- Grundlage: {{规范条款 / 需求编号 / 风险说明}}
- Empfehlung: {{具体的修改方式或替代方案}}

Beispiel:
### Anmerkung 1: Ausnahmezweig nicht abgedeckt
- Stufe: Muss geändert werden
- Position: `src/rules/spacing.ts:42`
- Problem: Bei unvollständigem Markdown in der Eingabe wird eine Ausnahme ausgelöst, statt ein Regelergebnis zurückzugeben.
- Grundlage: REQ-001 Abnahmebedingung Nr. 2 (Grenzpfad).
- Empfehlung: Parse-Ausnahme hier abfangen und als „Parsing fehlgeschlagen“ zurückgeben, einen Grenzfalltest ergänzen.
```

## 4. Vorlage des Review-Protokolls

```markdown
## Review-Protokoll: {{PR 编号}}

Prüfende Person: {{姓名}} ｜ Prüfdatum: {{YYYY-MM-DD}} ｜ Runde: {{第 N 轮}}

| Anmerkungsnummer | Stufe | Ergebnis | Bearbeitet von | Nachweis |
| --- | --- | --- | --- | --- |
| 1 | Muss geändert werden | Geändert | Autor | Siehe Commit abc1234 |
| 2 | Empfehlung | Nicht übernommen | Autor | Begründung: {{说明}} |

Ergebnis: {{批准 / 需修改后再审 / 拒绝}}
- Bedingungen für die Freigabe: Alle Punkte „Muss geändert werden“ sind erledigt, CI vollständig grün.
- Offene Punkte: {{无 / 列出}}
```

## 5. Felddefinitionen

| Feld | Pflichtfeld | Typ | Hinweise zum Ausfüllen | Beispiel |
| --- | --- | --- | --- | --- |
| Stufe | Ja | Aufzählung | Muss geändert werden / Empfehlung / Frage | `Muss geändert werden` |
| Position | Ja | `Pfad:Zeile` | Genau bis zur Zeile, nur Dateiname ist unzulässig | `src/parser.ts:42` |
| Problem | Ja | Text | Phänomen beschreiben, nicht die Person bewerten | `Parse-Ausnahme nicht abgefangen` |
| Grundlage | Ja | Text | Spezifikationsregel oder REQ-Nummer | `REQ-001 Abnahmebedingung 2` |
| Empfehlung | Ja | Text | Ausführbar, nicht nur „bitte optimieren“ | `Ausnahme abfangen und Treffer zurückgeben` |
| Ergebnis | Ja | Aufzählung | Geändert / Nicht übernommen / Zurückgestellt | `Geändert` |
| Nachweis | Ja | Text | Commit-Hash oder Art der Nachprüfung | `Siehe Commit abc1234` |
| Fazit | Ja | Aufzählung | Freigabe / Erneute Prüfung nach Änderung / Ablehnung | `Freigabe` |

## 6. Hinweise zum Ausfüllen

1. **Unterscheidung der Stufen**: „Muss geändert werden“ bezeichnet blockierende Probleme (Korrektheit, Sicherheit, fehlende Tests); „Empfehlung“ beeinflusst die Zusammenführung nicht; „Frage“ erfordert eine Klärung durch den Autor, aber keine Änderung.
2. **Formulierung der Anmerkung**: Beobachtbare Probleme beschreiben; wertende Formulierungen wie „das ist hier schlecht geschrieben“ sind unzulässig.
3. **Position**: Genau bis zur Zeilennummer; dateiübergreifende Probleme sind in jeder Anmerkung separat zu kennzeichnen.
4. **Grundlage**: Soweit zurückführbar, ist die Grundlage zu belegen; ohne Spezifikationsgrundlage sind Risiko oder Auswirkung zu benennen, „ich denke“ ist unzulässig.
5. **Ergebnis**: Bei „Nicht übernommen“ ist eine Begründung anzugeben; bei „Zurückgestellt“ ist die Stelle der weiteren Verfolgung zu benennen.
6. **Freigabe**: Bestätigen, dass alle Punkte „Muss geändert werden“ abgeschlossen sind und die CI vollständig grün ist; Autoren dürfen ihren eigenen PR nicht selbst freigeben.
7. **Uneinigkeit**: Bei abweichenden Auffassungen zwischen prüfender Person und Autor erfolgt eine Eskalation an die Maintainer; die Entscheidung wird im Review-Protokoll festgehalten.

Häufige Fehler:

| Fehlerhafte Formulierung | Problem | Korrektur |
| --- | --- | --- |
| „Das geht hier nicht“ | Kein Problem, keine Grundlage, keine Empfehlung | Drei Elemente ergänzen |
| „Bitte die Performance optimieren“ | Nicht ausführbar | Konkretes Vorgehen und Beurteilungskennzahl angeben |
| Nur Dateiname ohne Zeilennummer | Auffinden erschwert | Genau bis zur Zeile |
| Autor gibt selbst frei | Verstoß gegen die Regel | Durch eine andere Person prüfen lassen |
| „Muss geändert werden“ für persönliche Vorlieben | Missbrauch der Stufe | Auf „Empfehlung“ herabstufen |

## 7. Vollständiges Beispiel

```markdown
## Review-Protokoll: #12

Prüfende Person: Li Si ｜ Prüfdatum: 2026-11-18 ｜ Runde: 1. Runde

| Anmerkungsnummer | Stufe | Ergebnis | Bearbeitet von | Nachweis |
| --- | --- | --- | --- | --- |
| 1 | Muss geändert werden | Geändert | Wang Wu | Siehe Commit a1b2c3d |
| 2 | Empfehlung | Nicht übernommen | Wang Wu | Begründung: Aktuelle QPS erreichen keinen Engpass, Überkonstruktion vermeiden |
| 3 | Frage | Geklärt | Wang Wu | Im PR-Text ergänzend erläutert |

Ergebnis: Freigabe
- Bedingungen für die Freigabe: Alle Punkte „Muss geändert werden“ sind erledigt, CI vollständig grün (run #128).
- Offene Punkte: Keine
```

## Verwandte Dateien

- PR-Beschreibung und Branch-Modell: [Git-Workflow- und Branch-Spezifikation](./git-workflow-and-branching-specification.md)
- Grundlage der Stilprüfung: [Code-Stil-Spezifikation](./code-style-specification.md)
- Kriterien für bestandene Tests: [Test-Spezifikation](./testing-specification.md)
- Aktualisierung des Verfolgungsstatus: [Anforderungs-Verfolgungsmatrix-Spezifikation](./requirements-traceability-matrix-specification.md)
- Qualitätstor: [Qualitätstor](./quality-gate.md)
- Grundlage der Entscheidung bei Uneinigkeit: [Verhaltenskodex-Spezifikation](./code-of-conduct-specification.md)
- Automatisierte Prüfungen als Dimension D9: [Prüfungsdimensionsmatrix](./review-dimension-matrix.md)
