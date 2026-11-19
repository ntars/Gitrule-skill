# Informationserhebung und Vorlagen

> Problem, das diese Datei löst: Definiert die vor dem Verfassen der Dokumentation zu erhebenden Projektinformationsfelder und die Kennzeichnungsregeln für unbestätigte Angaben und stellt einen Platzhalterindex, eine Terminologie-Vorlage, eine Abhängigkeitslisten-Vorlage sowie einen direkt kopierbaren Text zur Projektdatenerhebung bereit.

## 1. Pflichtfelder (Fehlen blockiert)

| Feld | Beschreibung | Betroffene Kapitel |
| --- | --- | --- |
| Projektname | Repository-Name und Anzeigename; bei Abweichung ist diese zu erläutern | Gesamtes Dokument |
| Positionierung in einem Satz | höchstens 60 Zeichen; beschreibt, was das Projekt ist und welches Problem es für wen löst | Kapitel 1 |
| Repository-Beschreibung (Landessprache und Englisch) | je höchstens 120 Zeichen pro Sprache; beschreibt jeweils Projekttyp und Kernnutzen | Kapitel 1 |
| Themen-Tags | alle 20 kleingeschriebenen englischen Begriffe ausschöpfen, mit `-` verbunden; gemischte Groß-/Kleinschreibung oder Nicht-Englisch gilt als fehlend | Kapitel 1 |
| Projekthintergrund | Grund des Projektstarts, Unzulänglichkeiten bestehender Lösungen | Kapitel 2 |
| Liste der Kernfunktionen | nach Modulen gruppiert, inklusive für Nutzer wahrnehmbaren Verhaltens | Kapitel 3 |
| Technologie-Stack | Sprache, Framework, Versionsbeschränkungen der Laufzeitumgebung | Kapitel 6 |
| Abhängigkeitsliste | Name, Version, Lizenz, Rechteinhaber, Quelladresse | Kapitel 6, NOTICE |
| Lizenztyp | Lizenz des Projekts selbst, muss ein SPDX-Bezeichner sein | Kapitel 19 |
| Rechteinhaber | persönlicher Name oder vollständige Organisationsbezeichnung, sowie Jahr | Kapitel 19, NOTICE |
| Installation und Ausführung | Umgebungsanforderungen, Befehle, erwartetes Ergebnis | Kapitel 7, 8 |

## 2. Optionale Felder

Liste der Konfigurationsoptionen, API-Definition, Verzeichnisstruktur, Leistungstestdaten, Kompatibilitätsmatrix, bekannte Probleme, Änderungsprotokoll, Roadmap, Beitragsprozess, Sicherheitsstrategie, Screenshots und Demo-Adresse, Herkunft externer Materialien.

## 3. Ausfüllhinweise und Beispiele

| Feld | Ausfüllhinweis | Beispiel |
| --- | --- | --- |
| Projektname | Repository-Name verwendet Kleinbuchstaben, Ziffern und `-`; der Anzeigename darf eine Markenschreibweise verwenden; bei Abweichung ist der Grund anzugeben | Repository-Name `markdown-lint-cli`, Anzeigename `Markdown Lint CLI` |
| Positionierung in einem Satz | enthält Gattungswort und einschränkende Bestimmung, keine Anhäufung von Adjektiven, höchstens 60 Zeichen | `面向技术文档团队的 Markdown 规范检查命令行工具` |
| Repository-Beschreibung (Landessprache und Englisch) | Landessprache und Englisch jeweils als eigener Satz, je höchstens 120 Zeichen, kein Slogan als Ersatz für die Beschreibung | `中文：检查 Markdown 文档结构的命令行工具` / `English: A CLI tool for checking Markdown document structure` |
| Themen-Tags | ausschließlich kleingeschriebenes Englisch, Begriffe mit `-` verbunden, alle 20 ausschöpfen, Sprache, Form, Zweck, Ökosystem und Szenario vollständig abdecken | `go cli markdown linter developer-tools` |
| Technologie-Stack | Hauptsprache, Framework und Versionsbeschränkungen der Laufzeitumgebung angeben, nicht „neueste Version“ schreiben | `Go >= 1.22；Cobra v1.8.x` |
| Abhängigkeitsliste | jeder Eintrag mit Version, Lizenz, Rechteinhaber und offizieller Adresse; bei unklarer Herkunft als unbestätigten Punkt kennzeichnen | siehe Tabellenvorlage der Abhängigkeitsliste in Anhang C |
| Lizenztyp | SPDX-Bezeichner verwenden, keine unscharfen Formulierungen wie „Open Source“ oder „frei nutzbar“ | `MIT` |
| Installation und Ausführung | aktuelles Arbeitsverzeichnis, vollständigen Befehl und überprüfbare erwartete Ausgabe angeben | im Repository-Stammverzeichnis `go install ./cmd/mdlint` ausführen, Versionsnummer wird ausgegeben |
| Unbestätigte Punkte | feste Markierung verwenden, fehlenden Inhalt und zuständige Person für die Ergänzung angeben, nicht durch „vorläufig“ ersetzen | `【待确认：依赖 foo 的许可证类型，责任人：张三】` |

## 4. Kennzeichnungsregeln für unbestätigte Angaben

1. Einheitliches Format: `【待确认：具体缺什么】`; unscharfe Formulierungen wie „vorläufig“, „ungefähr“ oder „möglicherweise“ sind als Ersatz unzulässig.
2. Position der Kennzeichnung: einmal an der entsprechenden Stelle im Haupttext, zusätzlich erneut in der „Zusammenfassung der zu bestätigenden Punkte“ am Dokumentende.
3. Unbestätigte Punkte zu Lizenz, Urheberrecht oder Herkunft von Abhängigkeiten müssen in der NOTICE ausdrücklich gekennzeichnet werden; der gesamte Eintrag darf nicht entfallen.
4. Die Zusammenfassung der zu bestätigenden Punkte muss Nummer, Feld, fehlenden Inhalt, zuständige Person für die Ergänzung und geplanten Termin enthalten; Einträge ohne zuständige Person oder Termin dürfen nicht in Phase 0 eintreten (siehe [Ausführungsprozess](./execution-process.md)).

## 5. Anhang A · Platzhalterindex

`{{项目名称}}`, `{{一句话定位}}`, `{{当前版本}}`, `{{维护状态}}`, `{{许可证 SPDX}}`, `{{著作权人}}`, `{{年份}}`, `{{分支名}}`, `{{仓库地址}}`, `{{最低运行时版本}}`

Anwendungsregeln:

1. Dieser Index führt nur die Basisfelder der Erhebungsphase auf; für alle Platzhalter der README und deren Erläuterung gilt die Platzhaltertabelle der [README-Standardvorlage](./readme-standard-template.md) als maßgeblich.
2. Offizielle Platzhalter werden einheitlich als `{{纯名}}` geschrieben; innerhalb der geschweiften Klammern dürfen weder erläuternder Text noch Backticks noch ein zweiter Platzhalter verschachtelt werden; natürlichsprachige Inhalte in geschweiften Klammern in Spezifikationsbeispielen gelten nicht als offizielle Platzhalter.
3. Die natürlichsprachigen Felder der Erhebungstabelle verwenden keine Platzhalter unmittelbar; bei der Erzeugung der README werden sie gemäß der Tabelle auf die entsprechenden Platzhalter abgebildet; im finalen Dokument dürfen keine erläuternden Inhalte in geschweiften Klammern verbleiben.

## 6. Anhang B · Vorlage für die Terminologietabelle Chinesisch-Englisch

| Chinesisch | English | Abkürzung | Beschreibung |
| --- | --- | --- | --- |
| 待补充 | TBD | — | — |

## 7. Anhang C · Tabellenvorlage für die Abhängigkeitsliste

| Nr. | Komponentenname | Version | Einbindungsart | Rechteinhaber | Lizenz | Offizielle Adresse | Zweck in diesem Projekt | Geändert | Änderungsbeschreibung | Position im Originaltext |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Zu ergänzen | Zu ergänzen | direkt | Zu ergänzen | Zu ergänzen | Zu ergänzen | Zu ergänzen | nein | keine | Zu ergänzen |

Feldanforderungen siehe [Open-Source-Compliance-Spezifikation](./open-source-compliance-specification.md).

## 8. Bereich zum Ausfüllen der Projektinformationen

Nach Ergänzung der Projektinformationen unten mit der Ausführung von Phase 0 beginnen (siehe [Ausführungsprozess](./execution-process.md)).

- Projektname:
- Positionierung in einem Satz:
- Repository-Beschreibung (Landessprache und Englisch):
- Themen-Tags:
- Projekthintergrund:
- Kernfunktionen:
- Technologie-Stack und Version:
- Abhängigkeitsliste (oder Pfad der Abhängigkeitslistendatei):
- Lizenztyp:
- Rechteinhaber und Jahr:
- Installation und Ausführung:
- Repository-Adresse und Zielbranch:
- Weitere ergänzende Materialien:

## 9. Anhang D · Kopierbarer Text zur Projektdatenerhebung

Den folgenden Inhalt in die Datei `项目信息采集表.md` des Zielprojekts kopieren und die Inhalte nach „Ausfüllen:“ Punkt für Punkt ersetzen. Nicht bestätigbare Felder gemäß den Regeln aus Abschnitt 4 kennzeichnen und in Abschnitt 8 zusammenfassen.

````markdown
# Projektdatenerhebungstabelle

> Diese Datei dient der einmaligen Erhebung der für die Dokumenterzeugung benötigten Informationen. Nach dem Ausfüllen werden anhand der Ergebnisse README, NOTICE und weitere Lieferdokumente erzeugt.

## 1. Grundinformationen

| Feld | Auszufüllender Inhalt |
| --- | --- |
| Repository-Name | Ausfüllen: Repository-Name aus Kleinbuchstaben, Ziffern und Bindestrichen |
| Anzeigename | Ausfüllen: nach außen sichtbarer Projektname; bei Übereinstimmung mit dem Repository-Namen „wie Repository-Name“ schreiben |
| Repository-Adresse | Ausfüllen: vollständige HTTPS-Adresse |
| Zielbranch | Ausfüllen: Name des Standardbranches |
| Sprachcode | Ausfüllen: vorrangiger Sprachcode, z. B. zh-CN |
| Aktuelle Version | Ausfüllen: Semantische Versionsnummer oder „nicht veröffentlicht“ |
| Wartungsstatus | Ausfüllen: aktive Wartung / seltene Wartung / archiviert |

## 2. Positionierung und Geltungsbereich

| Feld | Auszufüllender Inhalt |
| --- | --- |
| Positionierung in einem Satz | Ausfüllen: höchstens 60 Zeichen, mit Gattungswort und einschränkender Bestimmung |
| Repository-Beschreibung (Landessprache) | Ausfüllen: höchstens 120 Zeichen |
| Repository-Beschreibung (English) | Ausfüllen: höchstens 120 Zeichen |
| Themen-Tags | Ausfüllen: alle 20 kleingeschriebenen englischen Begriffe, mit Bindestrichen verbunden |
| Projekthintergrund | Ausfüllen: Grund des Projektstarts und Unzulänglichkeiten bestehender Lösungen |
| Anwendungsfälle | Ausfüllen: einzeln aufführen, jeder mit Auslösebedingung |
| Nicht geeignete Fälle | Ausfüllen: einzeln aufführen, jeweils mit Begründung |
| Stärken | Ausfüllen: jeweils mit überprüfbarer Grundlage |
| Grenzen | Ausfüllen: jeweils mit Auswirkungsbereich und Umgehungsmöglichkeit |

## 3. Funktionen und Eigenschaften

| Modul | Für Nutzer wahrnehmbares Verhalten | Auslösebedingung | Ergebnis | Beleg oder Link |
| --- | --- | --- | --- | --- |
| Ausfüllen: Modulname | Ausfüllen: Verhaltensbeschreibung | Ausfüllen: Auslöseart | Ausfüllen: Ausgabe oder Zustandsänderung | Ausfüllen: Test, Screenshot oder Dokumentlink |

## 4. Technik und Abhängigkeiten

| Feld | Auszufüllender Inhalt |
| --- | --- |
| Hauptsprache und Versionsbeschränkung | Ausfüllen: z. B. `Go >= 1.22` |
| Framework und Build-Werkzeuge | Ausfüllen: Namen und Versionsbeschränkungen |
| Anforderungen an Laufzeit und System | Ausfüllen: Betriebssystem, Laufzeitumgebung, Browser- oder Datenbankversion |
| Abhängigkeitsliste | Ausfüllen: Pfad der Abhängigkeitslistendatei oder Einfügen der Tabelle aus Anhang C in diesen Abschnitt |
| Externe Materialien | Ausfüllen: Herkunft und Lizenz von Schriften, Bildern, Icons und Datensammlungen |

## 5. Auslieferung und Nutzung

| Feld | Auszufüllender Inhalt |
| --- | --- |
| Umgebungsanforderungen | Ausfüllen: vor der Installation zwingend erforderliche Voraussetzungen |
| Installationsbefehl | Ausfüllen: vollständiger Befehl einschließlich Angabe des aktuellen Arbeitsverzeichnisses |
| Prüfbefehl und erwartete Ausgabe | Ausfüllen: direkt ausführbarer Befehl und überprüfbares Ergebnis |
| Aktualisierung und Deinstallation | Ausfüllen: Befehle oder Arbeitsschritte |
| Liste der Konfigurationsoptionen | Ausfüllen: Schlüsselname, Typ, Standardwert, Pflichtfeld, Wertebereich, Wirkung |
| API- oder Modulbeschreibung | Ausfüllen: Signatur, Parameter, Rückgabewerte, Fehlercodes, Aufrufbeispiel |
| Kompatibilitätsmatrix | Ausfüllen: ausdrücklich unterstützte und nicht unterstützte Versionskombinationen |
| Leistungsdaten | Ausfüllen: Testumgebung, Verfahren, Kennzahlen und Engpässe; ohne Daten „nicht bereitgestellt, keine Ableitung zulässig“ schreiben |

## 6. Risiken und Grenzen

| Feld | Auszufüllender Inhalt |
| --- | --- |
| Bekannte Probleme | Ausfüllen: Beschreibung, Auswirkungsbereich, vorläufige Umgehung, Tracking-Link |
| Aktuelle Einschränkungen | Ausfüllen: was die aktuelle Version ausdrücklich nicht leistet |
| Nicht umgesetzte Funktionen | Ausfüllen: Funktion, Grund der Nichtumsetzung, Planungsstatus |
| Sicherheit und Datenschutz | Ausfüllen: Datenerhebung, Speicherung, Übertragung, Berechtigungsmodell, bekannte Risiken |
| Meldeweg für Schwachstellen | Ausfüllen: E-Mail, Issue-Vorlage oder spezielle Adresse |

## 7. Compliance und Verantwortung

| Feld | Auszufüllender Inhalt |
| --- | --- |
| Lizenztyp | Ausfüllen: SPDX-Bezeichner, z. B. `MIT` |
| Rechteinhaber | Ausfüllen: persönlicher Name oder vollständige Organisationsbezeichnung |
| Copyright-Jahr | Ausfüllen: Jahr oder Jahresbereich |
| Position des Lizenzvolltextes | Ausfüllen: Pfad der LICENSE-Datei |
| Pfad der NOTICE-Datei | Ausfüllen: Pfad der NOTICE-Datei; ohne Abhängigkeiten Dritter „nicht anwendbar, Grund: ……“ schreiben |
| Haftungsausschluss | Ausfüllen: Verwendung von Haftungsabgrenzung oder Gewährleistungsausschluss |

## 8. Zusammenfassung der zu bestätigenden Punkte

| Nummer | Feld | Fehlender Inhalt | Zuständige Person für die Ergänzung | Geplanter Termin | Auswirkungsbereich |
| --- | --- | --- | --- | --- | --- |
| T-001 | Ausfüllen: Feldname | Ausfüllen: was konkret fehlt | Ausfüllen: Name oder Rolle | Ausfüllen: YYYY-MM-DD | Ausfüllen: betroffene Kapitel oder Qualitätstore |

## 9. Zugehörige Spezifikationen

- Kapitelstruktur: [README-Abschnittsspezifikation](./readme-sections-specification.md)
- Kopierbare Vorlage: [README-Standardvorlage](./readme-standard-template.md)
- Detailregeln zu Abhängigkeitsfeldern: [Open-Source-Compliance-Spezifikation](./open-source-compliance-specification.md)
- Bewertung der Qualitätstore: [Qualitätstor](./quality-gate.md)
````

## Verwandte Dateien

- Frageregeln und Eintrittsbedingungen für Phase 0 siehe [Ausführungsprozess](./execution-process.md)
- Zuordnung der Kapitelauswirkungen siehe [README-Abschnittsspezifikation](./readme-sections-specification.md)
- Vollständige Platzhalterzuordnung der README siehe [README-Standardvorlage](./readme-standard-template.md)
- Detailregeln zu Abhängigkeitsfeldern siehe [Open-Source-Compliance-Spezifikation](./open-source-compliance-specification.md)
- Zusammenfassung der zu bestätigenden Punkte gehört zum Qualitätstor G12, siehe [Qualitätstor](./quality-gate.md)
