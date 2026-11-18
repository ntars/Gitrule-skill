# Open-Source-Compliance-Spezifikation

> Problem, das diese Datei löst: Definiert Erfassungsumfang der Open-Source-Compliance, Felder der Abhängigkeitsliste, Erfassungsmethoden, Beurteilung der Lizenzkompatibilität, Kennzeichnung von Änderungen sowie Regeln für die Quellenangabe von Materialien, damit Deklarationen vollständig und nachprüfbar sind.

## 1. Erfassungsumfang

Vier Quellentypen sind abzudecken: direkte Abhängigkeiten, indirekte und transitive Abhängigkeiten, Build- und Entwicklungswerkzeugketten sowie Materialressourcen (Icons, Schriftarten, Bilder, Audio, Datensätze, Algorithmusquellen).

## 2. Felder der Abhängigkeitsliste

| Feld | Anforderung |
| --- | --- |
| Komponentenname | Identisch mit dem offiziellen Repository |
| Version | Tatsächlich fixierte Version, kein Bereichsausdruck |
| Bezugsart | Direkte oder indirekte Abhängigkeit |
| Rechteinhaber | Vollständiger Name des offiziell angegebenen Urhebers |
| Lizenz | SPDX-Kennung; bei mehreren Lizenzen ist die Kombinationsart anzugeben |
| Offizielle Adresse | Vollständige URL des Repositorys oder der Projektseite |
| Verwendungszweck in diesem Projekt | Konkrete Aufrufstelle oder Funktion |
| Geändert | Ja oder Nein |
| Änderungsbeschreibung | Geänderte Datei, Änderungsinhalt, Änderungsgrund; ohne Änderung „keine“ eintragen |
| Ort des Lizenztexts | Pfad im Projekt oder Dateilink |

Die Tabellenvorlage für die Abhängigkeitsliste steht in [Informationserfassung und Vorlagen](./information-collection-and-templates.md).

## 3. Erfassungsmethoden

Je nach Technologie-Stack ist der Abhängigkeitsbaum mit dem entsprechenden Befehl zu erzeugen und anschließend Lizenz- und Urheberinformationen Punkt für Punkt zu ergänzen: `npm ls --all`, `pip freeze`, `go mod graph`, `cargo tree`, `mvn dependency:tree`, `gradle dependencies`, `composer show --tree`. Für den Lizenz-Scan können Werkzeuge wie `license-checker`, `pip-licenses`, `cargo-license` verwendet werden; die Scanergebnisse sind manuell zu prüfen, Werkzeugausgaben dürfen nicht unmittelbar als abschließendes Ergebnis dienen.

## 4. Lizenzkompatibilität

1. Die Kompatibilität der Projektlizenz mit den Lizenzen aller Abhängigkeiten ist zu beurteilen; besonderes Augenmerk gilt dem viralen Wirkungsbereich von GPL, AGPL, LGPL und MPL.
2. Bei Apache-2.0-Abhängigkeiten ist zu prüfen, ob deren NOTICE-Anforderungen erfüllt sind.
3. Lizenzen für Materialien (etwa SIL-OFL-Schriftarten, CC-Serien) sind gesondert auf Namensnennungs- und Verbreitungsanforderungen zu prüfen.
4. Ist die Kompatibilität nicht beurteilbar, ist „【待确认：许可证兼容性】“ zu kennzeichnen und der Grund der Unklarheit anzugeben.

## 5. Kennzeichnung von Änderungen an fremdem Code

1. Die ursprüngliche Urheber- und Lizenzangabe ist im Dateikopf beizubehalten.
2. In der NOTICE sind Pfad der geänderten Datei, Zusammenfassung der Änderung und Änderungsdatum anzugeben.
3. Im entsprechenden README-Abschnitt ist dies synchron zu erläutern.

## 6. Zitate und Materialien

1. Bei Zitaten aus fremder Dokumentation oder fremden Codeausschnitten sind Quelladresse, Autor und Lizenz anzugeben.
2. Bilder, Icons und Schriftarten sind mit Quelle und Lizenz zu erfassen; fehlen diese, ist „zu bestätigen“ zu kennzeichnen, und eine Verwendung ist unzulässig.
3. Materialien ungeklärter Herkunft dürfen nicht verwendet werden.

## Verwandte Dateien

- Zur Überführung der Abhängigkeitsliste in die NOTICE siehe [NOTICE-Spezifikation](./notice-specification.md)
- Zur Lizenzauswahl und den Anforderungen an den Volltext siehe [LICENSE-Spezifikation](./license-specification.md)
- Echtheit von Abhängigkeiten und Urheberrechten betrifft die Tore G6–G9, G13, siehe [Qualitätstor](./quality-gate.md)
