# Haftungsausschluss-Vorlage

> Problem, das diese Datei löst: Stellt eine allgemeine, direkt kopierbare und durch Ersetzen der Platzhalter anwendbare Vorlage für einen Haftungsausschluss bereit, sodass jedes Projekt mit minimalem Aufwand die Natur seiner Inhalte, seine Haftungsgrenzen und die Pflichten der Nutzenden abgrenzen kann; die begleitenden Ausfüllhinweise und Szenariovarianten decken private, unternehmerische, Open-Source- und Closed-Source-Projekte ab.

## 1. Gebrauchsanweisung

1. Den gesamten Inhalt von Abschnitt 3 „Vorlagentext“ kopieren und als `DISCLAIMER.md` im Projektwurzelverzeichnis neu anlegen oder als eigenständigen Abschnitt in `README.md` einfügen.
2. Gemäß der Platzhalterübersicht in Abschnitt 4 die `{{...}}` einzeln ersetzen; nicht verwendete ganze Abschnitte sind zu löschen, leere Platzhalter dürfen nicht verbleiben.
3. Gemäß Abschnitt 5 auf die jeweilige Situation zuschneiden: Bei Closed-Source-Software liegt der Schwerpunkt auf Abschnitt 3.5, bei Open-Source-Projekten ist Abschnitt 3.6 zum Verhältnis zur Lizenz beizubehalten.
4. Diese Vorlage ist allgemeiner Referenztext und stellt keine Rechtsauskunft dar. Bei förmlicher externer Veröffentlichung, grenzüberschreitender Verbreitung oder in regulierten Branchen ist eine juristische Prüfung vor der Verwendung erforderlich; Grundlage siehe Abschnitt 2 des [Haftungsausschlusses](./disclaimer.md).
5. Vor dem Commit prüfen: alle Platzhalter ersetzt, Kontaktdaten real erreichbar, kein Konflikt mit den Bestimmungen der [LICENSE](../../LICENSE).

## 2. Anpassungsgrundsätze

- **Rechtmäßigkeit zuerst**: Alle Haftungsausschlussklauseln gelten nur im Rahmen des anwendbaren Rechts; absolute Formulierungen wie „schließt jegliche Haftung bedingungslos aus“ sind verboten, um die Unwirksamkeit der gesamten Klausel zu vermeiden.
- **Keine Überschreitung**: Die durch die Lizenz eingeräumten Rechte dürfen nicht widerrufen oder eingeschränkt werden; bei Konflikten ist der Lizenztext maßgeblich, Grundsatz siehe [LICENSE-Spezifikation](./license-specification.md).
- **Nachprüfbar**: Kontaktdaten, Wirksamkeitsdatum und Name des Rechtsträgers müssen echte Angaben sein; Beispielwerte dürfen nicht verbleiben.
- **Unabhängigkeit**: Die Klauseln sind voneinander unabhängig; die Unwirksamkeit einer einzelnen Klausel berührt die Wirksamkeit der übrigen nicht.

## 3. Vorlagentext

Der folgende Inhalt ab Abschnitt 3.1 ist der Vorlagentext und kann direkt kopiert werden.

### 3.1 Zweck und Anwendungsbereich der Erklärung

```markdown
# Haftungsausschluss

> Diese Erklärung gilt für sämtliche von {{项目名称}} (im Folgenden „dieses Projekt“) veröffentlichten Inhalte, einschließlich Quellcode, Dokumentation, Vorlagen, Beispiele, Daten und zugehöriger Materialien (im Folgenden zusammenfassend „Projektinhalte“), unabhängig davon, ob sie durch manuelles Lesen, programmatischen Aufruf oder auf andere Weise genutzt werden.

1. Diese Erklärung dient der Klarstellung der Natur der Projektinhalte, dem Hinweis auf Nutzungsrisiken und der Abgrenzung der Haftungsgrenzen. Sie stellt keine zusätzliche Beschränkung von Rechten irgendeines Rechtsträgers dar und auch keinen Widerruf oder eine Einschränkung der durch die Projektlizenz eingeräumten Rechte.
2. Jeder Rechtsträger, der auf die Projektinhalte ganz oder teilweise zugreift, sie kopiert, zitiert, bearbeitet, verbreitet oder nutzt (im Folgenden „Nutzende“), gilt als mit dieser Erklärung vertraut und als habe sie verstanden.
3. Das Datum der letzten Aktualisierung dieser Erklärung ist der {{更新日期}}.
```

### 3.2 Inhaltliche Natur

```markdown
## Inhaltliche Natur

1. Die Projektinhalte sind {{内容性质描述}} und stellen keine offizielle Norm, Rechtsauskunft oder professionelle Beratung eines Unternehmens, einer Branche oder eines Rechtsraums dar.
2. Die Projektinhalte enthalten keine Eignungszusage für einen bestimmten Technologie-Stack, eine bestimmte Laufzeitumgebung oder bestimmte Compliance-Anforderungen und stellen keine professionelle Auskunft in rechtlicher, Compliance-, Sicherheits-, Finanz- oder Steuerfragen dar; in diesen Angelegenheiten haben Nutzende eigenständig eine entsprechend qualifizierte Fachperson hinzuzuziehen.
3. Beispiele, Parameter und statistische Angaben in den Projektinhalten dienen ausschließlich der Erläuterung von Methoden oder der Demonstration von Schreibweisen und dürfen nicht unmittelbar als empfohlene Werte für Produktivumgebungen übernommen werden; ihre Gültigkeit richtet sich nach {{数据或示例的时点与范围说明}}.
```

### 3.3 Gewährleistungsausschluss

```markdown
## Gewährleistungsausschluss

Im größtmöglichen gesetzlich zulässigen Umfang werden die Projektinhalte „wie besehen“ bereitgestellt; {{主体名称}} übernehmen keinerlei ausdrückliche oder stillschweigende Gewährleistung, einschließlich, aber nicht beschränkt auf:

- die Inhalte seien absolut richtig, vollständig, fehlerfrei oder ohne Auslassungen;
- die Inhalte seien für den bestimmten Zweck, die bestimmte Umgebung oder die bestimmten Compliance-Anforderungen der Nutzenden geeignet;
- eine Umsetzung nach den Projektinhalten führe zwangsläufig zu den erwarteten Ergebnissen oder führe zwangsläufig durch ein Prüf-, Test-, Veröffentlichungs- oder Zertifizierungsverfahren;
- die Projektinhalte blieben fortlaufend verfügbar, unverändert oder mit später von den Nutzenden eingesetzten Drittanbieterwerkzeugen, Plattformen und Diensten kompatibel;
- die Projektinhalte verletzten keine Rechte Dritter.
```

### 3.4 Pflichten der Nutzenden

```markdown
## Pflichten der Nutzenden

1. Nutzende haben vor der Übernahme der Projektinhalte deren Eignung unter Berücksichtigung ihres Projekttyps, der anwendbaren Rechtsvorschriften, der Branchenanforderungen und ihrer Risikotragfähigkeit eigenständig zu bewerten und selbst zu entscheiden, ob und in welchen Teilen sie übernommen werden und wie sie angepasst werden.
2. Nutzende haben Vorlagen, Konfigurationen, Skriptausschnitte und Parameter vor der Verwendung zu verifizieren, einschließlich Syntaxprüfung, Build-Verifikation, Testverifikation und Sicherheitsprüfung; eine ungeprüfte unmittelbare Anwendung in Produktivumgebungen, in Diensten für Dritte oder in Szenarien mit sensiblen Daten ist unzulässig.
3. Bearbeiten, kürzen, zusammenführen oder veröffentlichen Nutzende die Projektinhalte erneut, haben sie eigenständig zu prüfen, ob das Ergebnis mit ihren eigenen Anforderungen und den anwendbaren Bestimmungen übereinstimmt, und tragen die Verantwortung für die daraus entstehenden Dokumente, Konfigurationen und Liefergegenstände.
4. Nutzende haben die in ihrem Rechtsraum und in der Branche des Projekts geltenden Gesetze und internen Regelungen einzuhalten; die Projektinhalte ersetzen nicht die Erfüllung der damit verbundenen Pflichten.
```

### 3.5 Haftungsbeschränkung

```markdown
## Haftungsbeschränkung

1. Im größtmöglichen gesetzlich zulässigen Umfang haften {{主体名称}} nicht für Verluste, Schäden, Verbindlichkeiten, Kosten oder Aufwendungen, die aus den folgenden Umständen entstehen oder angeblich entstehen, unabhängig davon, ob sie auf Vertrag, unerlaubter Handlung (einschließlich Fahrlässigkeit) oder einem anderen Rechtsgrund beruhen und ob der Rechtsträger auf die Möglichkeit eines solchen Eintritts hingewiesen wurde:
   - Nutzung, Zitierung, Vervielfältigung, Bearbeitung, Verbreitung oder Umsetzung der Projektinhalte ganz oder teilweise;
   - Entscheidungen, die auf Grundlage der Projektinhalte getroffen werden, Handlungen, die ergriffen werden, oder Handlungen, die unterlassen werden;
   - Ergebnisse des Einsatzes von Dokumenten, Konfigurationen und Vorlagen, die nach den Projektinhalten erstellt wurden, in Arbeitsabläufen;
   - Unterbrechungen, Fehlschläge oder Datenanomalien infolge von Kompatibilitätsproblemen zwischen den Projektinhalten und Drittanbieterwerkzeugen, Plattformen oder Diensten;
   - Änderung, Aussetzung der Bereitstellung oder Einstellung der Pflege der Projektinhalte.
2. Die im vorstehenden Absatz genannten Verluste und Schäden umfassen insbesondere: unmittelbare Schäden, mittelbare Schäden, Begleitschäden, Folgeschäden, Strafschadensersatz sowie entgangenen Gewinn, entgangene Einnahmen, Betriebsunterbrechung, Datenverlust oder Datenbeschädigung, Schäden am Ruf des Unternehmens, zusätzliche Beschaffungskosten und Ansprüche Dritter.
3. Die beschränkenden Bestimmungen dieser Erklärung gelten nur im Rahmen des anwendbaren Rechts. Erlaubt ein Rechtsraum die Beschränkung oder den Ausschluss einer bestimmten Haftung nicht, so findet diese Beschränkung in diesem Rechtsraum keine Anwendung; die übrigen Bestimmungen bleiben wirksam.
```

### 3.6 Inhalte Dritter und Verhältnis zur Lizenz

```markdown
## Inhalte Dritter und Verhältnis zur Lizenz

1. Externe Links, Werkzeuge, Dienste, Icons, Schriftarten und Materialien, auf die in den Projektinhalten verwiesen wird, werden von den jeweiligen Dritten bereitgestellt und unterliegen deren eigenen Bedingungen; {{主体名称}} übernehmen keine Haftung für deren Inhalte, Verfügbarkeit, Richtigkeit, Sicherheit oder Rechtmäßigkeit und bringen damit keine Befürwortung zum Ausdruck. Nutzende haben deren Bedingungen und Eignung eigenständig zu prüfen; Lizenzpflichten aus Ressourcen Dritter gehen durch die Bezugnahme in den Projektinhalten weder über noch entfallen sie.
2. Dieses Projekt verwendet die Lizenz {{许可证名称及 SPDX 标识符}}, deren Volltext in der [LICENSE](./LICENSE) enthalten ist. Diese Erklärung erläutert die Haftungsausschlussklauseln der Lizenz aus Sicht der Nutzung und ersetzt, ändert oder schwächt diese Lizenzbestimmungen nicht.
3. Bei Auslegungskonflikten zwischen dieser Erklärung und den Lizenzbestimmungen ist der Lizenztext maßgeblich. Keine Formulierung dieser Erklärung darf dahingehend ausgelegt werden, dass sie für die eingeräumten Rechte ein zusätzliches Entgelt, zusätzliche Bedingungen oder zusätzliche Beschränkungen begründet.
4. Bei erneuter Veröffentlichung der Projektinhalte oder daraus abgeleiteter Inhalte sind gemäß den Lizenzanforderungen Urheber- und Lizenzhinweise beizubehalten; diese Erklärung kann beigefügt werden, damit nachgelagerte Nutzende die Haftungsgrenzen kennen.
```

### 3.7 Änderung und Wirksamkeit

```markdown
## Änderung und Wirksamkeit

1. Diese Erklärung wird von {{维护主体}} nach Bedarf anhand inhaltlicher Aktualisierungen und Compliance-Anforderungen überarbeitet; nach der Überarbeitung ist die neueste Fassung unter {{仓库地址或发布渠道}} maßgeblich.
2. Diese Erklärung tritt am {{生效日期}} in Kraft. Nutzen Nutzende die Projektinhalte nach einer Überarbeitung weiter, ist die überarbeitete Fassung maßgeblich; stimmen Nutzende den überarbeiteten Inhalten nicht zu, haben sie die Nutzung einzustellen.
3. Die Bestimmungen dieser Erklärung sind voneinander unabhängig. Wird eine Bestimmung für unwirksam oder nicht durchsetzbar erklärt, bleibt die Wirksamkeit der übrigen Bestimmungen unberührt.
4. Kontakt: {{真实可达的联系邮箱或渠道}}.
```

## 4. Platzhalterübersicht und Felddefinitionen

| Platzhalter | Pflicht | Felddefinition | Ausfüllbeispiel |
| --- | --- | --- | --- |
| `{{项目名称}}` | ja | Externer Projektname, identisch mit der ersten Zeile der README | `FooBar` |
| `{{主体名称}}` | ja | Vollständiger Name des Rechtsträgers, der Haftung trägt oder ausschließt; bei privaten Projekten der Name der Person, bei Unternehmensprojekten die gesetzliche Firmenbezeichnung | `Muster GmbH` |
| `{{维护主体}}` | ja | Organisation oder Person, die die Überarbeitung der Erklärung verantwortet | `FooBar-Maintainer-Team` |
| `{{更新日期}}` | ja | Datum der letzten Überarbeitung dieser Erklärung, einheitlich im Format YYYY-MM-DD | `2026-11-18` |
| `{{生效日期}}` | ja | Datum, an dem diese Erklärung wirksam wird; kann mit dem Aktualisierungsdatum übereinstimmen | `2026-11-18` |
| `{{内容性质描述}}` | ja | Ein Satz dazu, was das Projekt ist und welchen Reifegrad es hat | `Beispielimplementierung als Referenz für Entwickelnde, keine produktionsreife Komponente` |
| `{{数据或示例的时点与范围说明}}` | nein | Erhebungszeitpunkt und Anwendungsbereich der Daten oder Parameter in den Beispielen | `Statistik über 120 Stichproben im Oktober 2026` |
| `{{许可证名称及 SPDX 标识符}}` | ja | Vollständiger Name und SPDX-Kennung der Projektlizenz | `MIT-Lizenz (MIT)` |
| `{{仓库地址或发布渠道}}` | ja | Maßgeblicher Veröffentlichungsort der neuesten Fassung der Erklärung | `https://github.com/owner/repo` |
| `{{真实可达的联系邮箱或渠道}}` | ja | Für Nutzende erreichbare echte Adresse der Maintainer | `security@example.com` |

## 5. Ausfüllhinweise und Szenariovarianten

| Szenario | Beizubehaltende Klauseln | Kürzbare Klauseln | Anpassungspunkte |
| --- | --- | --- | --- |
| Privates Projekt | 3.1 / 3.2 / 3.3 / 3.5 / 3.7 | 3.4 kann verkürzt werden | Name des Rechtsträgers als echter Name; Kontakt über eine dauerhaft betreute E-Mail-Adresse |
| Unternehmensprojekt | alle Klauseln | keine | Name des Rechtsträgers gemäß Handelsregister; Veröffentlichung erst nach juristischer Prüfung |
| Open-Source-Projekt | alle Klauseln, insbesondere 3.6 | keine | Erläuterung zum Verhältnis zur Lizenz beibehalten; die durch die Lizenz eingeräumten Rechte dürfen nicht eingeschränkt werden |
| Closed-Source-Software | 3.1 / 3.2 / 3.3 / 3.4 / 3.5 / 3.7 | Absätze 2–4 von 3.6 können entfallen | Open-Source-Lizenzbezüge entfernen und stattdessen auf die Endbenutzer-Lizenzvereinbarung verweisen |
| Experimenteller Prototyp | 3.1 / 3.2 / 3.3 / 3.7 | 3.5 kann verkürzt werden | In der inhaltlichen Natur ausdrücklich „Prototyp“ kennzeichnen, um eine Einstufung als stabile Version zu vermeiden |
| Mit Verarbeitung personenbezogener Daten | alle Klauseln | keine | Rollen der Datenverarbeitung, Aufbewahrungsfristen und Kanäle für Betroffenenrechte ergänzen, siehe auch [Sicherheits- und Datenschutzspezifikation](./security-and-privacy-specification.md) |

Übersicht häufiger Fehler:

| Fehlerhafte Schreibweise | Folge | Korrekte Schreibweise |
| --- | --- | --- |
| „Dieses Projekt übernimmt keinerlei Haftung“ | Absolute Formulierung, leicht als unwirksam eingestuft | „Im größtmöglichen gesetzlich zulässigen Umfang wird keine Haftung übernommen für …“ |
| „Die abschließende Auslegung liegt ausschließlich beim Autor“ | Konflikt mit der Lizenzeinräumung, führt zu Streit | „Bei Konflikten ist der Lizenztext maßgeblich“ |
| Kontakt als `test@example.com` belassen | Nicht erreichbar, Kommunikationskanal entfällt | Echte und dauerhaft gültige E-Mail-Adresse eintragen |
| Erklärung eines anderen Projekts übernehmen, ohne den Rechtsträger zu ändern | Falscher Rechtsträger, Erklärung verliert ihre Bedeutung | Platzhalter einzeln ersetzen und Konsistenz des Rechtsträgers prüfen |

## 6. Vollständiges Beispiel

Nachfolgend ein ausgefülltes Beispiel für ein privates Open-Source-Projekt, nur als Formatreferenz; es darf nicht unmittelbar als eigene Erklärung kopiert werden.

```markdown
# Haftungsausschluss

> Diese Erklärung gilt für sämtliche von DemoCLI (im Folgenden „dieses Projekt“) veröffentlichten Inhalte, einschließlich Quellcode, Dokumentation, Vorlagen, Beispiele, Daten und zugehöriger Materialien (im Folgenden zusammenfassend „Projektinhalte“).

1. Diese Erklärung dient der Klarstellung der Natur der Projektinhalte, dem Hinweis auf Nutzungsrisiken und der Abgrenzung der Haftungsgrenzen. Sie stellt keine zusätzliche Beschränkung von Rechten irgendeines Rechtsträgers dar und auch keinen Widerruf oder eine Einschränkung der durch die Projektlizenz eingeräumten Rechte.
2. Jeder Rechtsträger, der auf die Projektinhalte ganz oder teilweise zugreift, sie kopiert, zitiert, bearbeitet, verbreitet oder nutzt, gilt als mit dieser Erklärung vertraut und als habe sie verstanden.
3. Das Datum der letzten Aktualisierung dieser Erklärung ist der 2026-11-18.

## Inhaltliche Natur

1. Die Projektinhalte sind ein Befehlszeilen-Beispielwerkzeug zur Orientierung für Entwickelnde und stellen keine offizielle Norm, Rechtsauskunft oder professionelle Beratung eines Unternehmens, einer Branche oder eines Rechtsraums dar.
2. Die Projektinhalte enthalten keine Eignungszusage für einen bestimmten Technologie-Stack, eine bestimmte Laufzeitumgebung oder bestimmte Compliance-Anforderungen und stellen keine professionelle Auskunft in rechtlicher, Compliance-, Sicherheits-, Finanz- oder Steuerfragen dar.
3. Beispielparameter in den Projektinhalten dienen ausschließlich der Demonstration von Schreibweisen und dürfen nicht unmittelbar als empfohlene Werte für Produktivumgebungen übernommen werden.

## Gewährleistungsausschluss

Im größtmöglichen gesetzlich zulässigen Umfang übernimmt Zhang San keinerlei ausdrückliche oder stillschweigende Gewährleistung, einschließlich, aber nicht beschränkt auf die absolute Richtigkeit der Inhalte, ihre Eignung für einen bestimmten Zweck, das zwangsläufige Erreichen der erwarteten Ergebnisse bei einer Umsetzung, ihre fortlaufende Verfügbarkeit sowie die Nichtverletzung von Rechten Dritter.

## Haftungsbeschränkung

Im größtmöglichen gesetzlich zulässigen Umfang haftet Zhang San nicht für Verluste, die aus der Nutzung, Bearbeitung oder Umsetzung der Projektinhalte entstehen, unabhängig davon, ob sie auf Vertrag, unerlaubter Handlung oder einem anderen Rechtsgrund beruhen. Erlaubt ein Rechtsraum die Beschränkung oder den Ausschluss einer bestimmten Haftung nicht, so findet diese Beschränkung in diesem Rechtsraum keine Anwendung; die übrigen Bestimmungen bleiben wirksam.

## Inhalte Dritter und Verhältnis zur Lizenz

Dieses Projekt verwendet die MIT-Lizenz (MIT), deren Volltext in der [LICENSE](./LICENSE) enthalten ist. Diese Erklärung erläutert die Haftungsausschlussklauseln der Lizenz aus Sicht der Nutzung und ersetzt, ändert oder schwächt diese Lizenzbestimmungen nicht; bei Auslegungskonflikten ist der Lizenztext maßgeblich.

## Änderung und Wirksamkeit

Diese Erklärung tritt am 2026-11-18 in Kraft, wird vom DemoCLI-Maintainer-Team überarbeitet, und maßgeblich ist die neueste Fassung unter https://github.com/example/democli. Die Klauseln sind voneinander unabhängig. Kontakt: maintainer@example.com.
```

## Verwandte Dateien

- Instanzerklärung dieses Projekts: [Haftungsausschluss](./disclaimer.md)
- Lizenzregeln: [LICENSE-Spezifikation](./license-specification.md)
- Sicherheit und Datenschutz: [Sicherheits- und Datenschutzspezifikation](./security-and-privacy-specification.md)
- Open-Source-Compliance: [Open-Source-Compliance-Spezifikation](./open-source-compliance-specification.md)
- Allgemeine Schreibkonventionen: [Allgemeine Schreibspezifikation](./general-writing-specification.md)
- Zurück zum chinesischen Index: [README](./README.md)
- Zurück zur Repository-Startseite: [README](../../README.md)
