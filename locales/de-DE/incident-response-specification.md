# Incident-Reaktionsspezifikation

> Problem, das diese Datei löst: Definiert Vorlage für Incident-Berichte, Zeitachse, Kommunikationsvorlagen und Felder der Nachbetrachtung, damit Störungen beherrschbar bleiben, Informationen synchron sind und Erfahrungen festgehalten werden.

## 1. Spezifikationsbestimmungen

1. Incident-Einstufung: P0 Kernfunktion nicht verfügbar oder Daten beschädigt; P1 schwerwiegende Funktionsbeeinträchtigung mit Auswirkung auf die Mehrheit der Nutzer; P2 lokales Problem mit begrenzter Auswirkung.
2. Reaktionsablauf: Erkennen → Einstufen → Eindämmen → Lokalisieren → Beheben → Ankündigen; Eindämmen hat Vorrang vor Lokalisieren.
3. Jeder P0/P1-Incident erfordert eine Nachbetrachtung mit Zeitachse, Ursache, Auswirkung, Behandlung und Verbesserungspunkten.
4. Verbesserungspunkte sind zur Nachverfolgung bis zum Abschluss in die [Roadmap-Spezifikation](./roadmap-specification.md) aufzunehmen.
5. Die Nachbetrachtung konzentriert sich auf Systemverbesserungen und weist keine persönliche Schuld zu.
6. Schlüsselleck: sofort rotieren → Historie bereinigen → ankündigen; ein reiner Lösch-Commit genügt nicht (siehe [Sicherheits- und Datenschutzspezifikation](./security-and-privacy-specification.md)).
7. Versehentlich gepushte große Dateien: LFS-Migration oder Historien-Rewrite (siehe [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md)).

## 2. Vorlage für den Incident-Bericht

```markdown
# Incident-Bericht: {{INC-YYYYMMDD-NN}}

- Incident-Stufe: {{P0 / P1 / P2}}
- Erkennungszeit: {{YYYY-MM-DD HH:MM}}
- Wiederherstellungszeit: {{YYYY-MM-DD HH:MM}}
- Dauer: {{N 分钟}}
- Einsatzleitung: {{姓名}}
- Aktueller Status: {{处理中 / 已恢复 / 已复盘}}

## Auswirkungsbereich
| Dimension | Erläuterung |
| --- | --- |
| Betroffene Funktion | {{具体功能}} |
| Anteil betroffener Nutzer | {{估算值与依据}} |
| Datenauswirkung | {{无 / 描述}} |
| Geschäftsauswirkung | {{可量化的损失或阻塞}} |

## Zeitachse
| Zeit | Ereignis | Quelle | Ausführende Person |
| --- | --- | --- | --- |
| {{HH:MM}} | Alarm ausgelöst | {{监控面板}} | {{姓名}} |
| {{HH:MM}} | Einstufung als P1 | {{判断依据}} | {{姓名}} |
| {{HH:MM}} | Rollback ausgeführt | {{命令 / 平台}} | {{姓名}} |
| {{HH:MM}} | Dienst wiederhergestellt | {{验证方式}} | {{姓名}} |

## Ursache
- Direkte Ursache: {{触发故障的具体事件}}
- Grundursache: {{为何未被预防或及时检测}}
- Verstärkende Faktoren: {{扩大影响的因素}}

## Behandlung und Verifikation
1. {{止血措施}}
2. {{修复措施}}
3. {{验证方式与结果}}

## Verbesserungspunkte
| Nummer | Maßnahme | Verantwortliche Person | Frist | Verifikationsmethode | Status |
| --- | --- | --- | --- | --- | --- |
| {{A-NN}} | {{具体动作}} | {{姓名}} | {{YYYY-MM-DD}} | {{可判定阈值}} | {{待开始}} |
```

## 3. Kommunikationsvorlagen

```markdown
## Incident-Mitteilung (erstmalig)

- Zeit: {{YYYY-MM-DD HH:MM}}
- Stufe: {{P0 / P1 / P2}}
- Symptom: {{用户可感知的现象，不写内部细节}}
- Auswirkung: {{受影响范围}}
- Aktuelle Maßnahmen: {{正在做什么}}
- Nächste Aktualisierung: {{HH:MM}}

## Incident-Mitteilung (Wiederherstellung)

- Wiederherstellungszeit: {{HH:MM}}
- Wiederherstellungsbestätigung: {{验证方式与结果}}
- Verbleibende Auswirkung: {{无 / 描述}}
- Weiteres Vorgehen: {{复盘安排}}
```

## 4. Felddefinitionen

| Feld | Pflicht | Typ | Ausfüllhinweis | Beispiel |
| --- | --- | --- | --- | --- |
| Incident-Nummer | ja | `INC-YYYYMMDD-NN` | Laufende Nummer des Tages, fortlaufend ohne Wiederverwendung | `INC-20261118-01` |
| Incident-Stufe | ja | Enumeration | P0 / P1 / P2 | `P1` |
| Dauer | ja | Dauer | Minuten von Erkennung bis Wiederherstellung | `42 Minuten` |
| Einsatzleitung | ja | Text | Eindeutig, verantwortlich für Entscheidungen und Abstimmung | `Li Si` |
| Anteil betroffener Nutzer | ja | Text | Schätzgrundlage erforderlich | `ca. 8 %, Grundlage: Zählung der Fehlerlogs` |
| Zeitachse | ja | Tabelle | Jeder Knoten mit Zeit und Quelle | siehe Vorlage |
| Grundursache | ja | Text | Direkte Ursache und Grundursache unterscheiden | `fehlende Rollback-Übungen` |
| Verbesserungspunkt.Verifikationsmethode | ja | Text | Beurteilbar, mit Schwellenwert | `Rollback bei der nächsten Übung <5 Minuten` |
| Nächste Aktualisierung | ja | Uhrzeit | Pflicht bei laufender Behandlung; „jederzeit aktuell“ unzulässig | `18:30` |

## 5. Ausfüllhinweise

1. **Einstufung**: Nach Auswirkungsbereich und Schweregrad einstufen; bei Unsicherheit höher einstufen und später mit Begründung anpassen.
2. **Eindämmen zuerst**: Zuerst den Dienst wiederherstellen (Rollback, Herabstufung, Drosselung), dann die Ursache lokalisieren; die Lokalisierung darf das Eindämmen nicht verzögern.
3. **Zeitachse**: In chronologischer Reihenfolge erfassen; Quellen müssen nachprüfbar sein (Alarm-ID, Befehl, Logausschnitt); nachträgliches Ergänzen aus dem Gedächtnis ist verboten.
4. **Ursache**: Die direkte Ursache ist das auslösende Ereignis, die Grundursache ein Systemmangel; beide sind auszufüllen.
5. **Kommunikation**: Die erstmalige Mitteilung muss den nächsten Aktualisierungszeitpunkt nennen; die Wiederherstellungsmitteilung muss Verifikationsmethode und verbleibende Auswirkung erläutern.
6. **Verbesserungspunkte**: Höchstens drei, in der Roadmap nachverfolgen; Verbesserungspunkte ohne Verantwortliche dürfen nicht in den Bericht aufgenommen werden.
7. **Nachbetrachtung**: Auf System- und Prozessverbesserungen fokussieren, keine Bewertung von Personen; keine Schuldzuweisung und keine Formulierungen wie „jemand war unachtsam“.
8. **Sonderfälle**: Schlüsselleck nach H12 behandeln; versehentlich gepushte große Dateien per LFS-Migration behandeln; beides ist gesondert zu dokumentieren.

Häufige Fehler:

| Fehlerhafte Schreibweise | Problem | Korrektur |
| --- | --- | --- |
| Zuerst Ursache lokalisieren, dann eindämmen | Verlängert die Störungsdauer | Zuerst per Rollback wiederherstellen |
| Zeitachse nachträglich ergänzen | Fakten nicht glaubwürdig | Während der Behandlung sofort erfassen |
| Ursache als „jemand war unachtsam“ schreiben | Zuweisung an Personen, kein Verbesserungswert | Bis auf Prozess- oder Werkzeugebene nachfragen |
| Mitteilung mit „wird schnellstmöglich behoben“ | Kein nächster Aktualisierungszeitpunkt | Konkrete Uhrzeit angeben |
| Verbesserungspunkt ohne Verifikationsmethode | Abschluss nicht beurteilbar | Schwellenwert und Prüfzeitpunkt ergänzen |

## 6. Vollständiges Beispiel

```markdown
# Incident-Bericht: INC-20261118-01

- Incident-Stufe: P1
- Erkennungszeit: 2026-11-18 10:12
- Wiederherstellungszeit: 2026-11-18 10:54
- Dauer: 42 Minuten
- Einsatzleitung: Li Si
- Aktueller Status: Nachbetrachtung abgeschlossen

## Auswirkungsbereich
| Dimension | Erläuterung |
| --- | --- |
| Betroffene Funktion | Schnittstelle zur Regelprüfung liefert 5xx |
| Anteil betroffener Nutzer | ca. 8 %, Grundlage: Zählung der 5xx-Logs |
| Datenauswirkung | keine |
| Geschäftsauswirkung | 42 Minuten lang konnten keine Prüfaufträge eingereicht werden |

## Ursache
- Direkte Ursache: Der Ladepfad des Regel-Plugins wurde durch eine neue Konfiguration überschrieben, wodurch der Start fehlschlug.
- Grundursache: Konfigurationsänderungen wurden nicht in die Vorabversions-Verifikation einbezogen.

## Verbesserungspunkte
| Nummer | Maßnahme | Verantwortliche Person | Frist | Verifikationsmethode | Status |
| --- | --- | --- | --- | --- | --- |
| A-01 | Konfigurationsänderungen in die Checkliste der Vorabversionsprüfung aufnehmen | Wang Wu | 2026-11-25 | Nächste 5 Änderungen enthalten alle Prüfnachweise | Ausstehend |
```

## Verwandte Dateien

- Alarmquellen und Handlungsleitfaden: [Observability-Spezifikation](./observability-specification.md)
- Rollback-Operationen: [Bereitstellungs- und Rollback-Spezifikation](./deployment-and-rollback-specification.md)
- Behandlung von Schlüsseln und sensiblen Informationen: [Sicherheits- und Datenschutzspezifikation](./security-and-privacy-specification.md)
- Große Dateien und Historien-Rewrite: [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md)
- Nachverfolgung von Verbesserungspunkten: [Roadmap-Spezifikation](./roadmap-specification.md)
- Prozessverbesserung in der Nachbetrachtung: [Iterationsretrospektiven-Spezifikation](./iteration-retrospective-specification.md)
- Beurteilungsmaßstab für Alarme: [Spezifikation für Qualitätsmetriken](./quality-metrics-specification.md)
