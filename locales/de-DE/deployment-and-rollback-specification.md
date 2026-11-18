# Bereitstellungs- und Rollback-Spezifikation

> Problem, das diese Datei löst: Definiert Vorlagen, Felder und Ausführungsmaßstäbe für Bereitstellungschecklisten, Änderungsaufträge und Rollback-Pläne, damit das Go-live beherrschbar, der Status nachvollziehbar und eine Störung schnell behebbar ist.

## 1. Spezifikationsbestimmungen

1. Vor der Bereitstellung müssen CI, Code-Review und Qualitätstor bestanden sein (siehe [Qualitätstor](./quality-gate.md)).
2. Die Bereitstellung erfolgt auf Basis einer bereits getaggten Veröffentlichungsversion; nicht getaggte Commits werden nicht verwendet (siehe [Versionsverwaltungsspezifikation](./version-management-specification.md)).
3. Umgebungskonfiguration und Code sind getrennt; sensible Konfigurationen werden über Konfigurationsmanagement injiziert und nicht im Repository abgelegt (siehe [Sicherheits- und Datenschutzspezifikation](./security-and-privacy-specification.md)).
4. Änderungen der Datenbankstruktur werden über Migrationsskripte ausgeführt und müssen vorwärtskompatibel sein (siehe [Datenbank-Designspezifikation](./database-design-specification.md)).
5. Jede Bereitstellung muss Versionsnummer, Zeitpunkt, ausführende Person und Änderungsinhalt aufzeichnen; eine Bereitstellung ohne Aufzeichnung gilt als nicht konforme Bereitstellung.
6. Für jede Version ist vorab ein Rollback-Plan vorzubereiten; ohne vorbereiteten Rollback-Plan darf kein Go-live erfolgen.
7. Nach der Bereitstellung sind Healthcheck und Smoke-Verifikation auszuführen; erst wenn beide bestanden sind, darf die Veröffentlichung abgeschlossen werden.

## 2. Vorlage für die Bereitstellungscheckliste

```markdown
# Bereitstellungscheckliste: {{项目名称}} {{版本号}}

Version: {{vX.Y.Z}} ｜ Tag: {{vX.Y.Z}} ｜ Zielumgebung: {{预发布 / 生产}} ｜ Geplanter Zeitpunkt: {{YYYY-MM-DD HH:MM}}

## Vorabprüfungen
- [ ] CI vollständig grün, Laufadresse des Workflows: {{URL}}
- [ ] Code-Review bestanden, freigebende Person: {{姓名}}
- [ ] Qualitätstore A/B/C alle PASS
- [ ] Änderungsprotokoll und Release Notes liegen vor
- [ ] Rollback-Plan geprüft, siehe Ende dieses Abschnitts
- [ ] Datenbank-Migrationsskript geprüft und vorwärtskompatibel
- [ ] Liste der Konfigurationsänderungen bestätigt (nicht im Repository abgelegte Injektionen)

## Änderungsinhalte
| Änderungsposten | Typ | Auswirkungsbereich | Verknüpfte Anforderung | Verifikationsmethode |
| --- | --- | --- | --- | --- |
| {{功能 / 配置 / 数据迁移}} | {{新增 / 修改 / 移除}} | {{受影响模块}} | {{REQ-NNN}} | {{如何确认}} |

## Ausführungsschritte
1. {{步骤，含具体命令或平台操作}}
2. {{灰度比例与观察时长}}
3. {{全量放量条件}}

## Healthcheck und Smoke-Test
| Prüfpunkt | Beurteilungsbedingung | Ausführungsweise | Ergebnis |
| --- | --- | --- | --- |
| Dienstverfügbarkeit | {{HTTP 200}} | {{命令}} | {{通过 / 未通过}} |
| Kritischer Pfad | {{主流程完成}} | {{命令}} | {{通过 / 未通过}} |
| Fehlerrate | {{< X%}} | {{监控面板}} | {{通过 / 未通过}} |

## Bereitstellungsaufzeichnung
| Punkt | Wert |
| --- | --- |
| Tatsächlicher Bereitstellungszeitpunkt | {{YYYY-MM-DD HH:MM}} |
| Ausführende Person | {{姓名}} |
| Freigebende Person | {{姓名}} |
| Tatsächliche Versionsnummer | {{vX.Y.Z}} |
| Ergebnis | {{成功 / 回滚 / 中止}} |

## Rollback-Plan
- Zielversion des Rollbacks: {{vX.Y.Z}}
- Auslösebedingung: {{错误率 > X% 持续 N 分钟 / 冒烟失败 / 数据异常}}
- Entscheidungsbefugte Person: {{姓名}}
- Rollback-Schritte: {{具体命令或操作}}
- Datenkompatibilität: {{是否需要数据回滚；如果需要，说明方式}}
```

## 3. Vorlage für die Bereitstellungsaufzeichnung

```markdown
## {{YYYY-MM-DD}} {{vX.Y.Z}} → {{环境}}

- Versionsnummer: {{vX.Y.Z}}
- Tag: {{vX.Y.Z}}
- Zeitpunkt: {{HH:MM}}
- Ausführende Person / freigebende Person: {{姓名 / 姓名}}
- Änderungszusammenfassung: {{一句话}}
- Healthcheck: {{通过 / 未通过}}
- Ergebnis: {{成功 / 回滚}}
- Zugehörige Veröffentlichung: {{Release Notes URL}}
- Anmerkung: {{异常与处理记录；无则写「无」}}
```

## 4. Felddefinitionen

| Feld | Pflicht | Typ | Ausfüllhinweise | Beispiel |
| --- | --- | --- | --- | --- |
| Tag | ja | Text | exakt identisch mit dem Tag der [Versionsverwaltungsspezifikation](./version-management-specification.md) | `v1.2.0` |
| Zielumgebung | ja | Enumeration | Vorabveröffentlichung / Produktion, Konfigurationen dürfen nicht vermischt werden | `Produktion` |
| Änderungsposten.Typ | ja | Enumeration | hinzugefügt / geändert / entfernt | `geändert` |
| Verknüpfte Anforderung | ja | Liste | REQ-Nummer; bei Änderungen ohne Anforderung „keine“ eintragen | `REQ-007` |
| Canary-Anteil | nein | Prozent | Pflicht bei schrittweiser Freigabe | `10% → 50% → 100%` |
| Beurteilungsbedingung | ja | Schwellenwert | beobachtbar und beurteilbar | `HTTP 200` |
| Tatsächliche Versionsnummer | ja | Text | bei Abweichung von der geplanten Versionsnummer ist der Grund anzugeben | `v1.2.1` |
| Rollback-Auslösebedingung | ja | Schwellenwert + Dauer | Formulierungen wie „fühlt sich anomal an“ sind unzulässig | `Fehlerrate >1% über 5 Minuten` |
| Datenkompatibilität | ja | Text | eindeutige Angabe, ob ein Datenrollback erforderlich ist | `kein Datenrollback erforderlich` |

## 5. Ausfüllhinweise

1. **Vorabprüfungen**: Punkt für Punkt abhaken; ein einmaliges Abhaken des gesamten Abschnitts ist unzulässig; ist ein Punkt nicht abgeschlossen, wird die Bereitstellung abgebrochen.
2. **Änderungsinhalte**: Jeder Eintrag muss mit einer REQ-Nummer verknüpft sein; reine Betriebsänderungen ohne Anforderungsbezug sind mit „keine“ zu kennzeichnen und die Änderungsgrundlage zu erläutern.
3. **Healthcheck**: Es müssen automatisch beurteilbare Bedingungen angegeben werden; „der Dienst sieht normal aus“ ist nicht zulässig.
4. **Rollback-Auslösebedingungen**: Schwellenwert und Dauer sind gleichzeitig anzugeben, um Fehlauslösungen durch kurzzeitiges Schwanken zu vermeiden.
5. **Canary-Freigabe**: Nach jeder Stufe ist die festgelegte Dauer zu beobachten und das Beobachtungsergebnis zu protokollieren, erst dann darf die nächste Stufe begonnen werden.
6. **Bereitstellungsaufzeichnung**: Wird chronologisch fortgeschrieben und überschreibt keine Historie; die Versionsnummer stimmt mit Push, Tag und Release Notes überein.
7. **Rollback-Ausführung**: Für den Code-Rollback wird mit `git revert` ein umgekehrter Commit erzeugt; ein Force-Push auf bereits öffentliche Historie ist unzulässig (siehe [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md)).

Häufige Fehler:

| Fehlerhafte Schreibweise | Problem | Korrektur |
| --- | --- | --- |
| Bereitstellung eines nicht getaggten Commits | Version nicht reproduzierbar | zuerst Tag setzen, dann bereitstellen |
| Rollback-Plan lautet „bei Problemen zurückrollen“ | keine Auslösebedingung und Schritte | Schwellenwert, Entscheidungsbefugte und Schritte ergänzen |
| Datenbankänderung ist nicht abwärtskompatibel | Daten nach dem Rollback unbrauchbar | dreistufiges Verfahren Erweitern-Migrieren-Zurückbauen anwenden |
| Bereitstellungsaufzeichnung nachträglich erstellt | Status nicht vertrauenswürdig | unmittelbar während der Bereitstellung aufzeichnen |
| Healthcheck prüft nur die Startseite | kritischer Pfad nicht validiert | Smoke-Testfälle für den Hauptablauf ergänzen |

## 6. Vollständiges Beispiel

```markdown
# Bereitstellungscheckliste: markdown-lint-cli v1.0.0

Version: v1.0.0 ｜ Tag: v1.0.0 ｜ Zielumgebung: Produktion ｜ Geplanter Zeitpunkt: 2026-11-20 10:00

## Vorabprüfungen
- [x] CI vollständig grün: https://github.com/example/markdown-lint-cli/actions/runs/123
- [x] Code-Review bestanden, freigebende Person: 李四
- [x] Qualitätstore A/B/C alle PASS
- [x] Änderungsprotokoll und Release Notes liegen vor
- [x] Rollback-Plan geprüft
- [x] Keine Datenbankmigration
- [x] Liste der Konfigurationsänderungen bestätigt: keine

## Änderungsinhalte
| Änderungsposten | Typ | Auswirkungsbereich | Verknüpfte Anforderung | Verifikationsmethode |
| --- | --- | --- | --- | --- |
| Regel für Leerzeichen zwischen Chinesisch und Englisch | hinzugefügt | Regel-Engine | REQ-001 | Ausführung TC-001 |
| CLI-Berichtsausgabe | geändert | Berichtsmodul | REQ-007 | Ausführung TC-012 |

## Ausführungsschritte
1. Tag v1.0.0 abrufen und Prüfsumme verifizieren
2. Canary 10%, Beobachtung 10 Minuten
3. Nach Fehlerrate <0.1% Freigabe auf 100%

## Healthcheck und Smoke-Test
| Prüfpunkt | Beurteilungsbedingung | Ausführungsweise | Ergebnis |
| --- | --- | --- | --- |
| Dienstverfügbarkeit | HTTP 200 | curl /healthz | bestanden |
| Kritischer Pfad | Prüfung von 50 Dokumenten abgeschlossen | Shell-Skript | bestanden |
| Fehlerrate | <0.1% | Monitoring-Dashboard | bestanden |

## Rollback-Plan
- Zielversion des Rollbacks: v0.9.3
- Auslösebedingung: Fehlerrate >1% über 5 Minuten
- Entscheidungsbefugte Person: 李四
- Rollback-Schritte: Bereitstellungs-Tag auf v0.9.3 umstellen und Datenkompatibilitätsprüfung ausführen
- Datenkompatibilität: keine Datenbankänderung, kein Datenrollback erforderlich
```

## Verwandte Dateien

- Versions- und Tag-Regeln: [Versionsverwaltungsspezifikation](./version-management-specification.md)
- Push-Aktionen und Incident-Behandlung: [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md)
- Incident-Einstufung und Nachbetrachtung: [Incident-Reaktionsspezifikation](./incident-response-specification.md)
- Unterstützung durch Metriken und Alarme: [Observability-Spezifikation](./observability-specification.md)
- Migrationsskripte und Kompatibilität: [Datenbank-Designspezifikation](./database-design-specification.md)
- Injektion sensibler Konfigurationen: [Sicherheits- und Datenschutzspezifikation](./security-and-privacy-specification.md)
