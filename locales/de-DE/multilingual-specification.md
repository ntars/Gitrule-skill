# Mehrsprachigkeits-Spezifikation

> Problem, das diese Datei löst: Definiert die Dateianordnung nach Sprachcode-Verzeichnissen, den Sprachwechsel, die Übersetzungskonsistenz, die Codekonsistenz und die Regeln zur Synchronisierung einseitiger Änderungen.

## 1. Verzeichnisstruktur

1. Die `README.md` im Repository-Wurzelverzeichnis dient ausschließlich als Projektstartseite und Sprachnavigation und enthält keinen eigentlichen Spezifikationstext.
2. Die eigentlichen Spezifikationen liegen flach im Verzeichnis `locales/<language-code>/`, zum Beispiel `locales/zh-CN/角色与职责.md`.
3. Sprachcodes folgen dem BCP 47-Stil, zum Beispiel `zh-CN`, `en-US`, `ja-JP`, `ko-KR`; Sprachcodes erscheinen nur im Verzeichnisnamen, nicht im Dateinamen.
4. **Dateinamen müssen die jeweilige Sprache selbst verwenden**: Das chinesische Verzeichnis nutzt chinesische Dateinamen (`角色与职责.md`), das englische Verzeichnis englische Dateinamen in Kleinschreibung mit Bindestrichen (`roles-and-responsibilities.md`), für andere Sprachen gilt dasselbe; in nicht-chinesischen Verzeichnissen dürfen keine chinesischen Dateinamen weiterverwendet werden.
5. Die Dateinamen der Sprachverzeichnisse müssen nicht wörtlich übereinstimmen, aber eine eindeutige Zuordnung muss gewährleistet sein: Dieselbe Spezifikation hat in jedem Sprachverzeichnis dieselbe inhaltliche Verantwortung; die Zuordnung wird im Feld `paths` der Manifestdatei registriert (siehe [Spezifikation für maschinenlesbare Metadaten](./machine-readable-metadata-specification.md)).
6. Vereinfachtes Chinesisch und Englisch sind die zuerst fertiggestellten Fassungen; weitere Sprachen werden in der Sprachliste der Root-`README.md` als „ausstehend“ oder „abgeschlossen“ gekennzeichnet; für Sprachen ohne angelegtes Verzeichnis dürfen keine leeren Links angeboten werden.
7. Eine neue Sprache erfordert nur das Anlegen des entsprechenden Sprachverzeichnisses und die Übersetzung Dokument für Dokument, ohne Änderung bestehender Sprachdateien; andere abgeschlossene Sprachen werden nur dann aktualisiert, wenn eine Revision der Ausgangssprache synchronisiert werden muss.

## 2. Sprachwechsel

1. Die `README.md` jedes Sprachverzeichnisses muss oben Links zum Sprachwechsel anbieten.
2. Die Links verwenden Pfade relativ zum aktuellen Sprachverzeichnis, zum Beispiel die Schreibweise im Verzeichnis für vereinfachtes Chinesisch:
   `[English](../en-US/README.md) | [简体中文](./README.md)`.
3. Der Linktext verwendet die Eigenbezeichnung der Zielsprache, zum Beispiel `English`, `简体中文`, `日本語`; Abkürzungen wie `CN`, `EN` sind nicht zulässig.
4. Wechsellinks verweisen nur auf angelegte Sprachverzeichnisse; nicht angelegte Sprachverzeichnisse werden einheitlich in der Sprachliste der Root-`README.md` gekennzeichnet, im Text dürfen keine toten Links verbleiben.

## 3. Übersetzungskonsistenz

1. Übersetzungen müssen vollständig sein: Anzahl der Abschnitte, Reihenfolge der Abschnitte, Spaltenzahl der Tabellen und Anzahl der Codeblöcke müssen mit der Ausgangssprache übereinstimmen; zusammenfassende oder unkorrigierte maschinelle Übersetzungen sind nicht zulässig.
2. Befehle, Pfade, Konfigurationsschlüsselnamen, Platzhalternamen und Parameterwerte in Codeblöcken bleiben unverändert; nur Kommentare und Erläuterungstexte werden übersetzt.
3. **Benutzersichtbare Vorlagenfelder müssen lokalisiert werden**: In der `yaml`-Konfiguration eines Issue-Formulars werden `name`, `label`, `description`, `placeholder` und die Optionen der Auswahlliste direkt auf der GitHub-Seite angezeigt und müssen in die Zielsprache übersetzt werden; strukturierte Felder wie `type`, `id`, `labels`, `required` und `render` bleiben englisch. Maßgeblich ist, ob ein Eintrag einer Person angezeigt wird, nicht ob er innerhalb eines Codeblocks steht. Ebenso wird der kopierbare Vorlagentext innerhalb eines `markdown`-Blocks stets übersetzt.
4. Termini werden gemäß der chinesisch-englischen Terminologietabelle in [Informationserfassung und Vorlagen](./information-collection-and-templates.md) vereinheitlicht; dasselbe Konzept verwendet in allen Sprachen dieselbe Zuordnung.
5. Jede einseitige Änderung muss in alle abgeschlossenen Sprachen synchronisiert werden, und im Änderungsprotokoll sind die synchronisierten Sprachcodes und Versionen zu erfassen; ohne abgeschlossene Synchronisierung gilt die Revision nicht als abgeschlossen.
6. Die Konsistenzprüfung gehört zum Qualitätstor G10, siehe [Qualitätstor](./quality-gate.md).

## 4. Rechtliche Texte

1. NOTICE wird standardmäßig in chinesischer Fassung bereitgestellt; rechtliche Texte mit Lizenz-Originaltext, Urheberrechtshinweisen und Haftungsausschlüssen behalten den englischen Originaltext und werden weder übersetzt noch umgeschrieben.
2. Rechtliche Texte, die eine chinesisch-englische Gegenüberstellung erfordern, müssen Original und Übersetzung nebeneinander zeigen und den Hinweis „Die Übersetzung dient nur zur Information, maßgeblich ist der Originaltext“ tragen.
3. Die sprachliche Behandlung rechtlicher Texte siehe [NOTICE-Spezifikation](./notice-specification.md) und [Haftungsausschluss](./disclaimer.md).

## Verwandte Dateien

- Sprachnavigation im Wurzelverzeichnis: [Repository-Startseite](../../README.md)
- Sprachmanifest und stabile Kennungen: [Spezifikation für maschinenlesbare Metadaten](./machine-readable-metadata-specification.md)
- Grundlage für Anzahl und Reihenfolge der Abschnitte sind die 20 Kapitel der [README-Abschnittsspezifikation](./readme-sections-specification.md)
- Vorlage der Terminologietabelle siehe [Informationserfassung und Vorlagen](./information-collection-and-templates.md)
- Schreibstandards siehe [Allgemeine Schreibspezifikation](./general-writing-specification.md)
- Die zweisprachige Synchronisierung gehört zum Qualitätstor G10, siehe [Qualitätstor](./quality-gate.md)
