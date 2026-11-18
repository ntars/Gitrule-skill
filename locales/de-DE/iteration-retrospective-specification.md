# Iterationsretrospektiven-Spezifikation

> Problem, das diese Datei löst: Definiert Vorlage, Felder und Mechanismus zur Nachverfolgung von Verbesserungspunkten nach Abschluss einer Iteration, damit Probleme zu ausführbaren und überprüfbaren Maßnahmen der nächsten Runde werden und Fehler sich nicht wiederholen.

## 1. Spezifikationsbestimmungen

1. Nach Abschluss jeder Iteration ist die Retrospektive innerhalb von fünf Arbeitstagen abzuschließen; Überschreitungen sind zu begründen.
2. Die Retrospektive muss auf Fakten und Daten beruhen; Eindrücke dürfen Messwerte nicht ersetzen; Datenquellen siehe [Spezifikation für Qualitätsmetriken](./quality-metrics-specification.md).
3. Jedes Problem erfordert eine klare Grundursache, Verbesserungsmaßnahme, verantwortliche Person und Verifikationsmethode; Einträge ohne verantwortliche Person oder ohne Verifikationsmethode dürfen nicht in die Maßnahmenliste aufgenommen werden.
4. Die Anzahl der Verbesserungsmaßnahmen ist auf drei begrenzt, geordnet nach Wirkung; darüber hinausgehende sind zusammenzuführen oder zu Empfehlungen herabzustufen.
5. Die Verbesserungsmaßnahmen der vorherigen Runde sind in der aktuellen Retrospektive einzeln zu prüfen; nicht abgeschlossene Punkte sind zu begründen und neu einzuplanen.
6. Das Retrospektivdokument erfasst ausschließlich Prozessverbesserungen, nicht Inhalte von Versionsänderungen; letztere siehe [Änderungsprotokoll-Spezifikation](./changelog-specification.md).

## 2. Vorlage für das Retrospektivdokument

```markdown
# Iterationsretrospektive: {{项目名称}} {{迭代标识}}

Iterationszeitraum: {{YYYY-MM-DD ~ YYYY-MM-DD}} ｜ Moderation: {{姓名}} ｜ Teilnehmende: {{姓名列表}} ｜ Retrospektivdatum: {{YYYY-MM-DD}}

## 1. Rückblick auf die Ziele
| Iterationsziel | Quelle | Zielerreichung | Beurteilungsgrundlage |
| --- | --- | --- | --- |
| {{目标描述}} | {{路线图 / 立项书}} | {{达成 / 未达成 / 部分达成}} | {{数据或交付物}} |

## 2. Datenmomentaufnahme
| Metrik | Wert vorherige Runde | Wert aktuelle Runde | Veränderung | Ziel |
| --- | --- | --- | --- | --- |
| Gelieferte Anforderungen | | | | |
| Entwichene Fehler | | | | |
| Durchschnittliche CI-Dauer | | | | |
| Anforderungsabdeckung | | | | |
| Anzahl Incidents | | | | |

## 3. Faktenliste
- Gut gelaufen: {{基于数据的事实，如「本轮 CI 全绿率 98%」}}
- Hindernisse: {{基于数据的障碍，如「集成环境等待平均 4 小时」}}
- Überraschungen: {{未预见的事件及其影响}}

## 4. Probleme und Grundursachen
| Nummer | Problem | Beleg | Grundursache | Auswirkung |
| --- | --- | --- | --- | --- |
| R-01 | {{问题描述}} | {{数据 / 事件}} | {{根因，非表象}} | {{造成的影响}} |

## 5. Verbesserungsmaßnahmen
| Nummer | Zugehöriges Problem | Maßnahme | Verantwortliche Person | Frist | Verifikationsmethode | Status |
| --- | --- | --- | --- | --- | --- | --- |
| A-01 | R-01 | {{具体动作}} | {{姓名}} | {{YYYY-MM-DD}} | {{如何验证生效}} | Nicht begonnen |

## 6. Prüfung der Maßnahmen der vorherigen Runde
| Nummer | Maßnahme | Status vorherige Runde | Ergebnis aktuelle Runde | Weiteres Vorgehen |
| --- | --- | --- | --- | --- |
| A-00 | {{动作}} | In Bearbeitung | {{完成 / 未完成 / 放弃}} | {{继续 / 重排 / 关闭并说明}} |

## 7. Konsens und Offenes
- Konsens dieser Runde: {{需要长期遵守的约定}}
- Offene Punkte: {{不在本轮处理的问题及原因}}
```

## 3. Vorlage für einen Verbesserungspunkt

```markdown
### A-{{两位序号}}：{{动作标题}}

- Zugehöriges Problem: {{R-NN}}
- Maßnahme: {{一个可执行的动作，含具体对象}}
- Verantwortliche Person: {{姓名，唯一}}
- Frist: {{YYYY-MM-DD}}
- Verifikationsmethode: {{可判定的检查和阈值}}
- Erwartete Wirkung: {{用指标描述}}
- Status: Nicht begonnen / In Bearbeitung / Abgeschlossen / Verworfen
```

## 4. Felddefinitionen

| Feld | Pflicht | Typ | Ausfüllhinweise | Beispiel |
| --- | --- | --- | --- | --- |
| Iterationskennung | ja | Text | Identisch mit der Phasennummer der [Roadmap-Spezifikation](./roadmap-specification.md) | `Sprint-12` |
| Zielerreichung | ja | Enumeration | Erreicht / Nicht erreicht / Teilweise erreicht | `Teilweise erreicht` |
| Beurteilungsgrundlage | ja | Text | Daten- oder Liefergegenstandslink, darf nicht leer sein | `REQ-001 veröffentlicht` |
| Datenmomentaufnahme | ja | Tabelle | Mindestens 3 Metriken mit Werten der vorherigen und der aktuellen Runde | `Entwichene Fehler 2 → 0` |
| Grundursache | ja | Text | Symptom und Grundursache unterscheiden; mit „weil“ verknüpft überprüfbar machen | `Weil die Umgebung nicht in die CI eingebunden war` |
| Maßnahme | ja | Text | Einzelne Maßnahme mit Objekt und Handlung | `Integrationsumgebung in die CI aufnehmen` |
| Verantwortliche Person | ja | Text | Genau eine Person; „Team“ ist unzulässig | `Wang Wu` |
| Verifikationsmethode | ja | Text | Beurteilbar, mit Prüfzeitpunkt | `CI-Dauer der nächsten Runde <10 Minuten` |
| Status | ja | Enumeration | Einer von vier Zuständen | `Abgeschlossen` |

## 5. Ausfüllhinweise

1. **Rückblick auf die Ziele**: Maßgeblich sind die ursprünglichen Ziele aus Projektstart oder Roadmap; Ziele dürfen nicht nachträglich an Ergebnisse angepasst werden.
2. **Datenmomentaufnahme**: Es ist dieselbe Erhebungsgrundlage wie in der vorherigen Runde zu verwenden; bei geänderter Grundlage sind „Grundlage geändert“ sowie alte und neue Definition anzugeben.
3. **Faktenliste**: Nur überprüfbare Fakten; subjektive Einschätzungen wie „schlechte Kommunikation“ sind in konkrete Ereignisse und Zeitpunkte zu überführen.
4. **Grundursache**: So lange nachfragen, bis eine handlungsfähige Ebene erreicht ist; „weil zu wenig getestet wurde“ ist noch ein Symptom, „weil Anforderungen nicht mit Testfällen verknüpft waren“ ist die Grundursache.
5. **Anzahl der Maßnahmen**: Höchstens drei; bei mehr als drei Problemen nach Wirkung ordnen und nicht berücksichtigte unter „Offene Punkte“ eintragen.
6. **Verifikationsmethode**: Prüfzeitpunkt und Beurteilungsschwelle sind zu nennen; „später beobachten“ ist unzureichend.
7. **Prüfung der vorherigen Runde**: Jeder Punkt erhält ein Ergebnis; ein pauschales Überspringen ist unzulässig; bei Verzicht ist der Grund anzugeben.

Häufige Fehler:

| Fehlerhafte Schreibweise | Problem | Korrektur |
| --- | --- | --- |
| „Alle sollten Qualität ernster nehmen“ | Keine Maßnahme, keine verantwortliche Person | Durch konkrete Maßnahme und Verantwortliche ersetzen |
| Grundursache als „Unachtsamkeit“ | Nicht überprüfbar, nicht verbesserbar | Bis auf Prozess- oder Werkzeugebene nachfragen |
| Acht Verbesserungsmaßnahmen aufgelistet | Nicht umsetzbar | Nach Wirkung ordnen und die ersten drei übernehmen |
| Verifikationsmethode „Wirkung ansehen“ | Nicht beurteilbar | Schwelle und Prüfzeitpunkt ergänzen |
| Maßnahmen der vorherigen Runde nicht geprüft | Verbesserungskreis unterbrochen | Ergebnisse der aktuellen Runde einzeln eintragen |

## 6. Vollständiges Beispiel

```markdown
# Iterationsretrospektive: markdown-lint-cli Sprint-12

Iterationszeitraum: 2026-11-10 ~ 2026-11-21 ｜ Moderation: Li Si ｜ Teilnehmende: Wang Wu, Zhao Liu ｜ Retrospektivdatum: 2026-11-23

## 1. Rückblick auf die Ziele
| Iterationsziel | Quelle | Zielerreichung | Beurteilungsgrundlage |
| --- | --- | --- | --- |
| Kernregeln von v1.0.0 veröffentlichen | Roadmap S12 | Erreicht | Tag v1.0.0 veröffentlicht |
| Anforderungsabdeckung 100 % | Projektauftrag G1 | Teilweise erreicht | 13/14 Muss-Anforderungen abgeschlossen |

## 2. Datenmomentaufnahme
| Metrik | Wert vorherige Runde | Wert aktuelle Runde | Veränderung | Ziel |
| --- | --- | --- | --- | --- |
| Gelieferte Anforderungen | 6 | 14 | +8 | 14 |
| Entwichene Fehler | 2 | 1 | -1 | 0 |
| Anforderungsabdeckung | 85 % | 92,9 % | +7,9 % | 100 % |

## 4. Probleme und Grundursachen
| Nummer | Problem | Beleg | Grundursache | Auswirkung |
| --- | --- | --- | --- | --- |
| R-01 | REQ-003 ohne Testfälle | Feld TC in der Verfolgungsmatrix steht auf „ausstehend“ | Weil die Vollständigkeit der Verfolgungsmatrix bei der Anforderungsprüfung nicht verpflichtend geprüft wurde | Ziel der Anforderungsabdeckung verfehlt |

## 5. Verbesserungsmaßnahmen
| Nummer | Zugehöriges Problem | Maßnahme | Verantwortliche Person | Frist | Verifikationsmethode | Status |
| --- | --- | --- | --- | --- | --- | --- |
| A-01 | R-01 | Prüfpunkt „Verfolgungsmatrix ausgefüllt“ in die Checkliste der Anforderungsprüfung aufnehmen | Wang Wu | 2026-11-27 | Die nächsten 5 Prüfprotokolle enthalten alle diesen Haken | Nicht begonnen |
```

## Verwandte Dateien

- Verfolgungsdaten von der Anforderung bis zur Veröffentlichung: [Anforderungs-Verfolgungsmatrix-Spezifikation](./requirements-traceability-matrix-specification.md)
- Metrikdefinitionen und Erhebungsweise: [Spezifikation für Qualitätsmetriken](./quality-metrics-specification.md)
- Quellen von Phasen und Zielen: [Roadmap-Spezifikation](./roadmap-specification.md)
- Inhalte von Versionsänderungen: [Änderungsprotokoll-Spezifikation](./changelog-specification.md)
- Incident-Nachbetrachtung und Verbesserung: [Incident-Reaktionsspezifikation](./incident-response-specification.md)
- Phase der Nachverfolgung: [Ausführungsprozess](./execution-process.md)
