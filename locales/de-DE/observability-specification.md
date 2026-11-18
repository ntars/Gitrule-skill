# Observability-Spezifikation

> Problem, das diese Datei löst: Definiert Logfelder, SLI/SLO-Ziele, Alarmregeln und die Vorlage für Alarmreaktionskarten, damit der Systemzustand sichtbar, eine Störung lokalisierbar und ein Alarm ausführbar ist.

## 1. Spezifikationsbestimmungen

1. Observability besteht aus den drei Säulen Logs, Metriken und Tracing; alle drei müssen über eine einheitliche Anfragekennung verknüpft sein.
2. Logs müssen strukturiert sein und Zeitstempel, Level sowie Anfragekennung enthalten; die Aufzeichnung sensibler Informationen ist verboten, Anonymisierungsregeln siehe [Sicherheits- und Datenschutzspezifikation](./security-and-privacy-specification.md).
3. Für jeden kritischen Dienst sind SLI und SLO zu definieren und Berechnungsgrundlage sowie Statistikfenster anzugeben.
4. Alarmregeln müssen einen eindeutigen Schwellenwert, eine Dauer und eine verantwortliche Person besitzen; Alarme ohne Handlungsanleitung dürfen nicht in Betrieb gehen.
5. Nach Auslösung eines Alarms muss eine Zuordnung zur Einstufung und zum Behandlungsablauf der [Incident-Reaktionsspezifikation](./incident-response-specification.md) möglich sein.
6. Die Metrikgrundlage muss mit der [Spezifikation für Qualitätsmetriken](./quality-metrics-specification.md) übereinstimmen; gleichnamige Metriken mit abweichender Bedeutung sind verboten.

## 2. Die drei Säulen und Felder

| Säule | Zwingend enthaltene Felder | Anforderung | Verknüpfungsschlüssel |
| --- | --- | --- | --- |
| Logs | Zeitstempel, Level, Anfragekennung, Nachricht, Kontext | strukturierte Ausgabe, Level ausschließlich DEBUG/INFO/WARN/ERROR | `trace_id` |
| Metriken | Metrikname, Labels, Wert, Erfassungszeit | eindeutige Grundlage und Zielwert | `service` |
| Tracing | Trace-Kennung, Span-Kennung, Parent-Span, Dauer, Status | dienstübergreifende Aufrufe verknüpfbar | `trace_id` |

## 3. Vorlage für Logfelder

```markdown
| Feld | Typ | Pflicht | Beschreibung | Beispiel |
| --- | --- | --- | --- | --- |
| timestamp | ISO 8601 | ja | UTC-Zeit mit Zeitzone | 2026-11-18T10:00:00Z |
| level | Enumeration | ja | DEBUG / INFO / WARN / ERROR | ERROR |
| trace_id | Zeichenkette | ja | eindeutige Kennung der gesamten Aufrufkette | 4bf92f3577b34da6 |
| service | Zeichenkette | ja | Dienstname | lint-api |
| message | Zeichenkette | ja | kurze Beschreibung ohne sensible Informationen | rule load failed |
| context | Objekt | nein | Felder zur Lokalisierung des Kontexts | {"rule":"spacing"} |
```

## 4. Vorlage für die SLI/SLO-Definition

```markdown
# SLO-Definition: {{服务名}}

Version: {{v1.0}} ｜ Verantwortliche Person: {{姓名}} ｜ Überprüfungszyklus: {{每季度}}

## Dienstgrenzen
- Dienstverantwortlichkeit: {{一句话}}
- Abhängige Dienste: {{上游 / 下游}}
- Kritische Nutzeraktionen: {{列出 2–5 项}}

## SLI-Definition
| SLI | Definition | Berechnungsgrundlage | Datenquelle |
| --- | --- | --- | --- |
| Verfügbarkeit | Erfolgreiche Anfragen / Gesamtanfragen | HTTP-Statuscode <500 gilt als erfolgreich | {{监控面板}} |
| Latenz | Verteilung der Anfragedauer | P95-Perzentil | {{监控面板}} |
| Fehlerrate | Fehlgeschlagene Anfragen / Gesamtanfragen | 5xx-Zählung | {{监控面板}} |

## SLO-Ziele
| SLI | Zielwert | Statistikfenster | Aktueller Wert | Zielstatus |
| --- | --- | --- | --- | --- |
| Verfügbarkeit | ≥99.9% | rollierend 30 Tage | {{值}} | {{达标 / 未达标}} |
| Latenz P95 | <300ms | rollierend 7 Tage | {{值}} | {{达标 / 未达标}} |
| Fehlerrate | <0.1% | rollierend 24 Stunden | {{值}} | {{达标 / 未达标}} |

## Fehlerbudget
- Berechnungsweise: {{1 - SLO 目标值，按统计窗口换算}}
- Verbrauchsalarm: {{消耗达 50% / 75% / 90% 时分别通知}}
- Erschöpfungsstrategie: {{冻结非关键发布，优先修复稳定性}}
```

## 5. Vorlage für Alarmregeln

```markdown
### ALERT-{{三位序号}}：{{告警名称}}

- Zugehöriges SLI: {{可用性 / 延迟 / 错误率}}
- Ausdruck: {{可执行的查询表达式}}
- Schwellenwert: {{数值 + 单位}}
- Dauer: {{N 分钟}}
- Schweregrad: {{P0 / P1 / P2}}
- Verantwortliche Person: {{姓名 / 值班组}}
- Auslösebeispiel: {{给出一个会触发的样例数据}}
- Stummschaltungsbedingung: {{何时允许静默，须有到期时间}}

Handlungsanleitung:
1. {{第一步：确认现象的数据源与命令}}
2. {{第二步：常见原因与对应处理}}
3. {{第三步：升级条件与升级对象}}
- Zugehörige Incident-Stufe: {{见事故响应规范的分级表}}
```

## 6. Felddefinitionen

| Feld | Pflicht | Typ | Ausfüllhinweise | Beispiel |
| --- | --- | --- | --- | --- |
| SLI-Definition | ja | Text | muss ein berechenbares Verhältnis oder Perzentil sein | Erfolgreiche Anfragen / Gesamtanfragen |
| Berechnungsgrundlage | ja | Text | Einschluss- und Ausschlussbedingungen eindeutig angeben | Healthcheck-Anfragen ausgeschlossen |
| SLO-Zielwert | ja | Schwellenwert | Zahl + Einheit + Prozent | `≥99.9%` |
| Statistikfenster | ja | Dauer | rollierendes Fenster, unbestimmte Angaben wie Kalendermonat sind unzulässig | `rollierend 30 Tage` |
| Fehlerbudget | ja | Zahl | aus dem SLO-Zielwert abgeleitet | `43 Minuten Nichtverfügbarkeit pro Monat zulässig` |
| Alarmausdruck | ja | Abfrage | direkt einfügbar und ausführbar | `rate(http_5xx[5m]) > 0.01` |
| Dauer | ja | Dauer | verhindert Fehlmeldungen durch kurzzeitiges Schwanken | `5 Minuten` |
| Handlungsanleitung | ja | Liste | mindestens 3 Schritte einschließlich Eskalationsbedingung | siehe Vorlage |
| Stummschaltungsbedingung | ja | Text | muss ein Ablaufdatum besitzen | `innerhalb des Veröffentlichungsfensters, maximal 30 Minuten` |

## 7. Ausfüllhinweise

1. **SLI-Auswahl**: 2–5 Punkte aus nutzerseitig wahrnehmbaren Dimensionen wählen; interne Ressourcenmetriken wie CPU oder Arbeitsspeicher dürfen nutzerseitige SLIs nicht ersetzen.
2. **Einheitliche Grundlage**: Gleichnamige Metriken müssen in Logs, Monitoring-Dashboards und Alarmausdrücken dieselbe Berechnungsgrundlage verwenden.
3. **Zielsetzung**: SLO-Ziele sollten auf aktuellen Messwerten und der fachlichen Toleranz beruhen; die unbegründete Übernahme von „vier Neunen“ ist unzulässig.
4. **Fehlerbudget**: Das Umrechnungsergebnis und die abgestuften Verbrauchsmaßnahmen sind anzugeben; bei erschöpftem Budget werden nicht kritische Veröffentlichungen eingefroren.
5. **Ausführbare Alarme**: Jeder Alarm muss die drei Fragen „worauf achten, wie untersuchen, wann eskalieren“ beantworten; fehlt eine Antwort, darf er nicht in Betrieb gehen.
6. **Umgang mit Alarmmüdigkeit**: Alarme, die 30 Tage in Folge keine wirksame Behandlung ausgelöst haben, sind herabzustufen oder zu löschen, mit Begründung.
7. **Anonymisierung**: Können in Kontextfeldern der Logs Schlüssel, Tokens oder personenbezogene Daten auftreten, ist vor der Ausgabe zu anonymisieren.

Häufige Fehler:

| Fehlerhafte Schreibweise | Problem | Korrektur |
| --- | --- | --- |
| CPU-Auslastung als SLI verwenden | nicht nutzerseitig wahrnehmbar | auf Verfügbarkeit, Latenz, Fehlerrate wechseln |
| Alarm nur als „Dienst anomal“ | kein Schwellenwert, keine Anleitung | Ausdruck, Schwellenwert und Behandlungsmaßnahmen ergänzen |
| Log gibt vollständige Request-Header aus | Risiko der Preisgabe von Privatsphäre und Schlüsseln | nur notwendige Felder per Whitelist ausgeben |
| Alarm ohne Ablaufzeit der Stummschaltung | dauerhafte Stummschaltung führt zu ausbleibenden Meldungen | maximale Stummschaltungsdauer festlegen |
| SLO ohne Statistikfenster | Ziel nicht beurteilbar | rollierendes Fenster ergänzen |

## 8. Vollständiges Beispiel

```markdown
# SLO-Definition: lint-api

Version: v1.0 ｜ Verantwortliche Person: 王五 ｜ Überprüfungszyklus: vierteljährlich

## SLI-Definition
| SLI | Definition | Berechnungsgrundlage | Datenquelle |
| --- | --- | --- | --- |
| Verfügbarkeit | Erfolgreiche Anfragen / Gesamtanfragen | Statuscode <500, Healthchecks ausgeschlossen | Grafana lint-overview |
| Latenz | Dauer der Prüfanfragen P95 | nur Pfad /check gezählt | Grafana lint-overview |

## SLO-Ziele
| SLI | Zielwert | Statistikfenster | Aktueller Wert | Zielstatus |
| --- | --- | --- | --- | --- |
| Verfügbarkeit | ≥99.9% | rollierend 30 Tage | 99.94% | erreicht |
| Latenz P95 | <300ms | rollierend 7 Tage | 268ms | erreicht |

## Fehlerbudget
- Berechnungsweise: 0.1% × 30 Tage = 43 Minuten/Monat
- Verbrauchsalarm: 50% Benachrichtigung der verantwortlichen Person, 75% Benachrichtigung der Bereitschaftsgruppe, 90% Einfrieren nicht kritischer Veröffentlichungen
- Erschöpfungsstrategie: Funktionsveröffentlichungen aussetzen, nur Stabilitätskorrekturen zulassen

### ALERT-001: 5xx-Fehlerrate überschreitet Schwellenwert
- Zugehöriges SLI: Verfügbarkeit
- Ausdruck: `rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])`
- Schwellenwert: >0.01
- Dauer: 5 Minuten
- Schweregrad: P1
- Verantwortliche Person: 王五
- Handlungsanleitung:
  1. Grafana lint-overview öffnen und den Dienst der Fehlerquelle bestätigen
  2. ERROR-Logs abfragen und die Aufrufkette über trace_id verknüpfen; häufige Ursache ist ein fehlgeschlagenes Laden von Regel-Plugins
  3. Ohne Lokalisierung innerhalb von 10 Minuten an 李四 eskalieren und den P1-Incident-Ablauf starten
```

## Verwandte Dateien

- Metrikgrundlage und Messdefinition: [Spezifikation für Qualitätsmetriken](./quality-metrics-specification.md)
- Behandlungsablauf nach einem Alarm: [Incident-Reaktionsspezifikation](./incident-response-specification.md)
- Healthcheck bei der Bereitstellung: [Bereitstellungs- und Rollback-Spezifikation](./deployment-and-rollback-specification.md)
- Log-Anonymisierung und Datenschutz: [Sicherheits- und Datenschutzspezifikation](./security-and-privacy-specification.md)
- Einträge zur Fehlerbehebung: [Fehlerbehebungsspezifikation](./troubleshooting-specification.md)
