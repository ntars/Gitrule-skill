# Abhängigkeitsverwaltungs-Spezifikation

> Problem, das diese Datei löst: Sie definiert Vorlagen und Felder für Antrag auf Einführung einer Abhängigkeit, Abhängigkeitsliste, Fixierung und Aktualisierung, damit Builds reproduzierbar, Abhängigkeiten nachvollziehbar und Lizenzen konform bleiben.

## 1. Spezifikationsregeln

1. Bei der Einführung einer neuen Abhängigkeit sind Zweck, Lizenz und Wartungsstatus anzugeben (siehe [Open-Source-Compliance-Spezifikation](./open-source-compliance-specification.md)).
2. Abhängigkeiten mit kompatibler Lizenz und aktiver Community sind zu bevorzugen; Abhängigkeiten unklarer Herkunft oder unklarer Lizenz dürfen nicht eingeführt werden.
3. Abhängigkeitsversionen müssen in der Lockfile festgeschrieben und im Repository eingecheckt werden, damit ein Build in einer sauberen Umgebung reproduzierbar ist (entspricht der harten Regel H9 und Dimension D5).
4. Versionsnummern müssen die tatsächlich aufgelöste Version fixieren; Bereichsausdrücke dürfen nicht als endgültige Auslieferung dienen.
5. Aktualisierungen von Abhängigkeiten sind durch Automatisierungswerkzeuge zu unterstützen und müssen nach der Aktualisierung die CI bestehen; Schwachstellen sind zeitnah zu beheben oder mit Maßnahmen zur Risikominderung zu erfassen.
6. Die Abhängigkeitsliste muss mit der NOTICE übereinstimmen (siehe [NOTICE-Spezifikation](./notice-specification.md)).

## 2. Vorlage für den Antrag auf Einführung einer Abhängigkeit

```markdown
## Antrag auf Einführung einer Abhängigkeit: {{包名}}

- Antragsnummer: {{DEP-NNN}}
- Antragstellende Person: {{姓名}}
- Zweck: {{一句话说明解决什么问题}}
- Eigenentwicklung möglich: {{是 / 否；是则说明为何仍引入}}
- Bewertung von Alternativen: {{已评估的替代包及未选原因}}

| Feld | Wert |
| --- | --- |
| Paketname | {{包名}} |
| Eingeführte Version | {{精确版本号}} |
| Lizenz | {{SPDX ID}} |
| Lizenzkompatibilität | {{兼容 / 不兼容 / 需法务确认}} |
| Letztes Veröffentlichungsdatum | {{YYYY-MM-DD}} |
| Wartungsstatus | {{活跃 / 低频 / 停滞}} |
| Wöchentliche Downloads | {{数值}} |
| Anzahl transitiver Abhängigkeiten | {{数值}} |
| Bekannte Schwachstellen | {{无 / CVE 编号与处置}} |
| Auswirkung auf Paketgröße | {{增量 KB}} |

- Ergebnis: {{批准 / 拒绝 / 有条件批准}}
- Genehmigt von: {{姓名}}
```

## 3. Vorlage der Abhängigkeitsliste

```markdown
# Abhängigkeitsliste: {{项目名称}}

Aktualisiert am: {{YYYY-MM-DD}} ｜ Lockfile: {{路径}} ｜ Erzeugungswerkzeug: {{工具与版本}}

| Abhängigkeit | Eingeführte Version | Fixierte Version | Typ | Lizenz | Zweck | Letzte Prüfung |
| --- | --- | --- | --- | --- | --- | --- |
| {{包名}} | {{^1.2.0}} | {{1.2.3}} | Direkt / Indirekt | {{MIT}} | {{用途}} | {{YYYY-MM-DD}} |

## Aktualisierungsprotokoll
| Datum | Abhängigkeit | Versionsänderung | Grund | Prüfergebnis |
| --- | --- | --- | --- | --- |
| {{YYYY-MM-DD}} | {{包名}} | {{1.2.2 → 1.2.3}} | {{安全修复}} | {{CI 全绿}} |

## Ausnahmen und Risikominderung
| Abhängigkeit | Problem | Maßnahme | Prüfdatum |
| --- | --- | --- | --- |
| {{包名}} | {{漏洞 / 停滞}} | {{限制使用范围}} | {{YYYY-MM-DD}} |
```

## 4. Felddefinitionen

| Feld | Pflichtfeld | Typ | Hinweise zum Ausfüllen | Beispiel |
| --- | --- | --- | --- | --- |
| Antragsnummer | Ja | `DEP-NNN` | Fortlaufend, keine Wiederverwendung | `DEP-007` |
| Zweck | Ja | Text | Beschreibt das gelöste Problem, „erleichtert die Entwicklung“ ist unzulässig | `TOML-Konfiguration parsen` |
| Bewertung von Alternativen | Ja | Text | Mindestens 1 Alternative bewerten | `toml-js geprüft, wegen stagnierender Wartung nicht gewählt` |
| Eingeführte Version | Ja | Exakte Version | `^` oder `~` sind unzulässig | `1.2.3` |
| Fixierte Version | Ja | Exakte Version | Muss mit der Lockfile übereinstimmen | `1.2.3` |
| Lizenz | Ja | SPDX-ID | Schreibweise wie in der [LICENSE-Spezifikation](./license-specification.md) | `MIT` |
| Wartungsstatus | Ja | Aufzählung | Aktiv / Gering / Stagnierend, mit Begründung | `Aktiv (Commits in den letzten 30 Tagen)` |
| Anzahl transitiver Abhängigkeiten | Ja | Zahl | Bei hoher Anzahl Auswirkung auf Größe und Risiko erläutern | `12` |
| Bekannte Schwachstellen | Ja | Text | Ohne Befund „Keine“ schreiben, nicht leer lassen | `Keine` |
| Prüfdatum | Ja | Datum | Für Ausnahmen ist ein Prüfdatum festzulegen | `2026-12-31` |

## 5. Hinweise zum Ausfüllen

1. **Bewertung der Eigenentwicklung**: Zuerst ist zu klären, ob die Aufgabe mit der Standardbibliothek oder vorhandenen Fähigkeiten umsetzbar ist; wird trotz Machbarkeit eingeführt, ist der Grund anzugeben.
2. **Lizenz**: Es muss eine SPDX-ID sein; `UNLICENSED` und eigene Lizenzen sind in „Rechtliche Prüfung erforderlich“ zu überführen und dürfen nicht direkt eingeführt werden.
3. **Wartungsstatus**: Maßgeblich sind letztes Veröffentlichungsdatum und Reaktionszeit auf Issues; „scheint gepflegt zu werden“ ist unzulässig.
4. **Versionsfixierung**: Bei der Auslieferung muss die Lockfile die exakt aufgelöste Version enthalten; `package.json` darf Bereichsausdrücke behalten, die Lockfile muss jedoch exakt sein.
5. **Aktualisierungsrhythmus**: Automatische Updates werden regelmäßig aktiviert, die Zusammenführung erfolgt nach manueller Bestätigung; jede Aktualisierung muss die CI bestehen und Lizenzänderungen prüfen.
6. **Umgang mit Schwachstellen**: Vorrangig auf eine sichere Version aktualisieren; ist dies nicht möglich, sind Maßnahmen zur Risikominderung und ein Prüfdatum zu dokumentieren und in das Risikoregister der [Incident-Reaktions-Spezifikation](./incident-response-specification.md) aufzunehmen.
7. **Synchronisierung der Liste**: Nach Einführung oder Entfernung einer Abhängigkeit sind Abhängigkeitsliste und NOTICE zu aktualisieren; alle drei (Lockfile, Liste, NOTICE) müssen übereinstimmen.

Häufige Fehler:

| Fehlerhafte Formulierung | Problem | Korrektur |
| --- | --- | --- |
| „Eine Bibliothek für die Konfiguration verwenden“ | Kein konkreter Paketname und Zweck | Paketname, Version und gelöstes Problem angeben |
| Lizenz als „Open Source“ angegeben | Kompatibilität nicht beurteilbar | SPDX-ID angeben |
| Lockfile nicht eingecheckt | Build nicht reproduzierbar | Lockfile einchecken (entspricht H9) |
| Anzahl transitiver Abhängigkeiten bleibt leer | Risiko nicht sichtbar | Konkreten Zahlenwert eintragen |
| Schwachstelle ohne Maßnahme | Risiko bleibt unverfolgt | Maßnahme und Prüfdatum ergänzen |

## 6. Vollständiges Beispiel

```markdown
## Antrag auf Einführung einer Abhängigkeit: remark

- Antragsnummer: DEP-001
- Antragstellende Person: Wang Wu
- Zweck: Als Markdown-Parsing-Schicht zur Unterstützung der Knotenlokalisierung der Regel-Engine (REQ-001, REQ-004).
- Eigenentwicklung möglich: Nein; eine Eigenentwicklung kann GFM-Grenzfälle nicht innerhalb des Personalrahmens abdecken.
- Bewertung von Alternativen: marked wurde geprüft und wegen unzureichender Lokalisierung chinesischer Knoten nicht gewählt.

| Feld | Wert |
| --- | --- |
| Paketname | remark |
| Eingeführte Version | 15.0.1 |
| Lizenz | MIT |
| Lizenzkompatibilität | Kompatibel |
| Letztes Veröffentlichungsdatum | 2026-11-02 |
| Wartungsstatus | Aktiv (Commits in den letzten 30 Tagen) |
| Wöchentliche Downloads | 4.200.000 |
| Anzahl transitiver Abhängigkeiten | 18 |
| Bekannte Schwachstellen | Keine |
| Auswirkung auf Paketgröße | +42 KB |

- Ergebnis: Genehmigt, Umsetzung zusammen mit ADR-0002
- Genehmigt von: Li Si
```

## Verwandte Dateien

- Beurteilung der Lizenzkompatibilität: [Open-Source-Compliance-Spezifikation](./open-source-compliance-specification.md)
- SPDX-Kennzeichnung der Lizenz: [LICENSE-Spezifikation](./license-specification.md)
- Konsistenz der NOTICE: [NOTICE-Spezifikation](./notice-specification.md)
- Reproduzierbarer Build als Dimension D5: [Prüfungsdimensionsmatrix](./review-dimension-matrix.md)
- Automatisierte Aktualisierung als Dimension D9: [Prüfungsdimensionsmatrix](./review-dimension-matrix.md)
- Tests und Behandlung von Schwachstellen: [Test-Spezifikation](./testing-specification.md), [Sicherheits- und Datenschutz-Spezifikation](./security-and-privacy-specification.md)
- Bezug zu Architekturentscheidungen: [Architekturdesign-Dokumentations-Spezifikation](./architecture-design-document-specification.md)
