# README-Abschnittsspezifikation

> Problem, das diese Datei löst: Sie definiert die 20 Abschnitte, die eine README in jedem Sprachverzeichnis zwingend enthalten muss, die in den jeweiligen Kapiteln erforderlichen und unzulässigen Inhalte sowie das Standardformat der Copyright-Zeile.

## 1. Allgemeine Anforderungen an die Abschnitte

Die folgenden 20 Kapitel müssen vollständig vorhanden sein, ihre Reihenfolge ist fest, und die Sprachfassungen entsprechen sich eins zu eins.

| Nummer | Abschnitt | Muss enthalten | Darf nicht enthalten |
| --- | --- | --- | --- |
| 1 | Projektname und Positionierung | Projektname, Repository-Beschreibung (zweisprachiges Format `Landessprache \| Englisch`), Themen-Tags (bis 20, nur Englisch), Ein-Satz-Positionierung, Sprachumschaltungs-Link, aktuelle Version, Wartungsstatus | Nichtssagende Adjektive; Repository-Beschreibung über 120 Zeichen; Themen-Tags mit gemischter Groß- und Kleinschreibung oder nicht englischen Wörtern |
| 2 | Projektkurzvorstellung | Hintergrund, zu lösendes Problem, Kernansatz, geeignete Szenarien, ungeeignete Szenarien sowie getrennt aufgeführte Stärken und Einschränkungen (Einschränkungen müssen Auswirkungsbereich und Umgehung enthalten) | In einem Satz abgehandelt; nur Stärken ohne Einschränkungen |
| 3 | Kernfunktionen | Nach Modulen gruppierte Funktionseinträge, jeder mit Auslösebedingung und Ergebnis | Nur Funktionsnamen |
| 4 | Kernmerkmale | Nach der Struktur des [Leitfadens für Merkmale und technische Abwägungen](./features-and-engineering-tradeoffs-guide.md) gegliedert | Lob ohne Belege |
| 5 | Entwurfsdetails und technische Abwägungen | Nach der Struktur des [Leitfadens für Merkmale und technische Abwägungen](./features-and-engineering-tradeoffs-guide.md) gegliedert | Beschreibungen, die Funktionen wiederholen |
| 6 | Technologie-Stack und Abhängigkeitsliste | Laufzeit-, Build- und Test-Toolchain mit Versionsvorgaben; Abhängigkeitsdetails verweisen auf NOTICE | Fehlende Versionsnummern |
| 7 | Installation und Bereitstellung | Umgebungsanforderungen, Installationsschritte, Prüfbefehl, Aktualisierungs- und Deinstallationsweg, Hinweise zur Containerisierung | Übersprungene Schritte oder ausgelassene Prüfung |
| 8 | Schnellstart | Minimales lauffähiges Beispiel mit vollständigem Befehl und erwarteter Ausgabe | Nicht ausführbarer Pseudocode |
| 9 | Konfiguration | Tabelle der Konfigurationsoptionen (Schlüssel, Typ, Standardwert, erforderlich, Wertebereich, Wirkung, Beispiel), Konfigurationspriorität, Hot-Reload-Unterstützung | Fehlender Standardwert |
| 10 | API- oder Modulbeschreibung | Schnittstellensignatur, Parameter, Rückgabewert, Fehlercodes, Aufrufbeispiel, Ratenbegrenzung und Kontingente | Fehlende Fehlercodes |
| 11 | Verzeichnisstruktur | Baumstruktur mit Erläuterung der Zuständigkeiten jeder Ebene | Dateiweise Auflistung ohne Erläuterung |
| 12 | Leistungsverhalten | Testumgebung, Testmethode, Kennzahldaten, Engpassanalyse, Optimierungsempfehlungen | Zahlen ohne Testbedingungen |
| 13 | Sicherheit und Datenschutz | Datenerhebung und -speicherung, Transportverschlüsselung, Berechtigungsmodell, Meldeweg für Schwachstellen, bekannte Risiken | Zusicherung absoluter Sicherheit |
| 14 | Kompatibilität | Matrix zu Betriebssystem, Laufzeit, Browser und Datenbankversion sowie ausdrücklich nicht unterstützte Punkte | Unklare Formulierungen |
| 15 | Bekannte Probleme und Einschränkungen | Bekannte Probleme (Beschreibung, Auswirkungsbereich, vorläufige Umgehung, Tracking-Link), aktuelle Einschränkungen, Liste nicht implementierter Funktionen (Funktion, Grund der Nichtumsetzung, Planungsstatus) | Verschweigen schwerwiegender Mängel; nicht implementierte Funktionen als implementiert darstellen |
| 16 | Änderungsprotokoll | Struktur nach Keep a Changelog, Versionsnummern nach Semantischer Versionierung | Einträge ohne Datum |
| 17 | Weitere Roadmap | Planungspunkte, Status, Zielversion, Kennzeichnung „keine Zusage“ | Zusage von Lieferterminen |
| 18 | Beitragen | Einrichtung der Entwicklungsumgebung, Branch-Modell, Commit-Konvention, PR-Anforderungen, Verhaltenskodex, Issue-Vorlagen | Nur „PRs willkommen“ |
| 19 | Urheberrecht und Lizenz | Copyright-Zeile, Lizenzname, SPDX-Kennung, Fundstelle des vollständigen Lizenztexts | Fehlender Urheberrechtsinhaber |
| 20 | NOTICE-Konformitätserklärung | Zusammenfassung der Abhängigkeiten Dritter, relativer Link zur NOTICE-Datei | Ersetzen der NOTICE durch dieses Kapitel |

## 1.1 Vier Fragen des Startbildschirms und Ein-Satz-Text

Der Startbildschirm der README muss vier Fragen in fester Reihenfolge beantworten:

1. Was macht das Projekt;
2. Welches Problem löst das Projekt;
3. Welche Merkmale hat das Projekt;
4. Das minimale Hello-World-Beispiel.

Frage 1 entspricht der „Ein-Satz-Positionierung“ und muss drei Punkte gleichzeitig erfüllen: Projekttyp benennen, präzise Bestimmungswörter verwenden, direkt wiederholbar sein. Öffentliche Texte etablierter Projekte können als Referenz dienen:

| Projekt | Ein-Satz-Text | Strukturanalyse |
| --- | --- | --- |
| Angular | One framework. Mobile & desktop. | Kategorie + Abdeckung |
| React | A declarative, efficient, and flexible JavaScript library for building user interfaces. | Drei Bestimmungswörter + Kategorie + Zweck |
| Vue | A progressive, incrementally-adoptable JavaScript framework for building UI on the web. | Zwei Merkmale + Kategorie + Zweck |

Vorgaben zur Schreibweise:

- Informationslose Adjektive wie „leistungsstark“, „hervorragend“ oder „revolutionär“ sind unzulässig;
- Ein Kategoriewort (Bibliothek, Framework, Werkzeug, Anwendung) muss genannt werden, damit Lesende das Projekt auf einen Blick einordnen können;
- Höchstens drei bestimmende Merkmalswörter, um Anhäufungen zu vermeiden;
- Die chinesische Fassung muss auf 60 Zeichen begrenzt werden, die englische Fassung auf 25 Wörter.

Frage 3 „Welche Merkmale“ muss zugleich ungeeignete Szenarien offenlegen. Wirksame Schreibweise: Es wird angegeben, dass ein Message-Broker „nur QoS-Stufe 0 unterstützt und für Szenarien mit Stufe 1 nicht geeignet ist“; unwirksam ist die bloße Auflistung von Vorteilen. Merkmalsvergleiche müssen auf überprüfbaren Fakten beruhen; vergleichbare Projekte dürfen nicht abgewertet werden.

Das Hello-World-Beispiel zu Frage 4 muss Installation und Ausführung in zwei Schritten ermöglichen; bei Projekten mit aufwendiger Installation sollte ein Container-Image oder eine Online-Demo-Umgebung bereitgestellt werden, damit Lesende nach der Lektüre der README nicht aufgeben.

## 2. Standardformat der Copyright-Zeile

```text
Copyright © {{年份}} {{著作权人}}. Licensed under {{SPDX 标识符}}.
```

## Verwandte Dateien

- Abgrenzung der Abschnittsinhalte siehe [Dokumentationsmatrix](./document-matrix.md)
- Regeln zu Repository-Beschreibung und Themen-Tags siehe Abschnitt 5 der [Projekt-Namensspezifikation](./project-naming-specification.md)
- Konsistenz zwischen chinesischer und englischer Fassung siehe [Mehrsprachigkeitsspezifikation](./multilingual-specification.md)
- Die bei den Abhängigkeitsdetails referenzierte NOTICE siehe [NOTICE-Spezifikation](./notice-specification.md)
- Schreibstandards siehe [Allgemeine Schreibspezifikation](./general-writing-specification.md)
