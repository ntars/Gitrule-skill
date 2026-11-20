# NOTICE-Spezifikation

> Problem, das diese Datei löst: Definiert die sieben Pflichtbestandteile der NOTICE-Datei und die Konsistenzanforderungen gegenüber der README, damit Erklärungen Dritter in einer eigenen Datei stehen und die Angaben korrekt sind.

## 1. Eigene Datei

Die NOTICE liegt als eigene Datei vor; sie darf nicht in die README integriert und nicht durch eine Liste in der README ersetzt werden. Sie muss folgende Teile enthalten:

1. **Erklärung des Projekts selbst**: Projektname, Rechteinhaber, Jahr, Lizenz, SPDX-Bezeichner.
2. **Liste der Komponenten Dritter**: Punktweise aufgeführt nach den Feldern der Abhängigkeitsliste in der [Open-Source-Compliance-Spezifikation](./open-source-compliance-specification.md).
3. **Anhang der Lizenzoriginaltexte**: Fordert eine Lizenz die Beilage des Volltextes, ist der Originaltext jeweils beizufügen; der Originaltext bleibt englisch und wird nicht übersetzt.
4. **Änderungserklärung**: Ort und Inhalt der Änderungen an Code Dritter.
5. **Erklärung zu Herkunft von Materialien und Daten**.
6. **Haftungsausschluss**: englischer Originaltext bleibt erhalten, eine chinesische Paralleldarstellung kann beigefügt werden.
7. **Zu bestätigende Punkte**: Einträge, deren Lizenz oder Rechteinhaberschaft nicht verifiziert werden kann, sind ausdrücklich mit „Zu bestätigen“ zu kennzeichnen.

## 2. Konsistenzanforderungen

Die Komponenten- und Lizenzinformationen in der NOTICE müssen mit Kapitel 6 (Technologie-Stack und Abhängigkeitsliste), Kapitel 19 (Copyright und Lizenzierung) und Kapitel 20 (NOTICE-Compliance-Erklärung) der README vollständig übereinstimmen; bei Version, Lizenzkennung und Rechteinhaber dürfen keine Abweichungen auftreten.

## 3. Erklärungsweise bei geschichteter Lizenzierung

Verwendet das Projekt geschichtete Lizenzen, ist die „Erklärung des Projekts selbst“ aus Abschnitt 1 nach Schichten aufzuteilen und darf nicht auf die Hauptlizenz beschränkt bleiben.

1. Jede Schicht erhält eine eigene Zeile mit Geltungsbereich (etwa „Quellcode unter `cli/` und `mcp/`“), Lizenzname, SPDX-Bezeichner und Ort des Volltextes.
2. Der aus allen Schichten zusammengefasste SPDX-Ausdruck muss mit Kapitel 19 der README wortgleich übereinstimmen; nicht an einer Stelle `MIT AND CC-BY-4.0` und an der anderen nur `MIT`.
3. Der Grund der Schichtung ist in einem Satz anzugeben, etwa „Code und Dokumentation haben unterschiedliche Wiederverwendungsanforderungen“, damit nachfolgende Maintainer die Schichtzugehörigkeit einer Datei bestimmen können.
4. Gibt es Inhalte, die keiner Schicht zugeordnet werden können, sind ihre Pfade unter „Zu bestätigende Punkte“ aufzuführen; sie dürfen nicht standardmäßig der Hauptlizenz zugerechnet werden.
5. Der Haftungsausschluss muss in Kapitel 19 der README und in `LICENSING.md`, falls vorhanden, gleichlautend sein und klarstellen, dass Lizenzwahl und Schichtaufteilung vom Projektträger selbst bestätigt werden und Werkzeuge und Vorlagen keine Rechtsberatung darstellen.

## Verwandte Dateien

- Felder der Abhängigkeitsliste und Erhebungsmethoden siehe [Open-Source-Compliance-Spezifikation](./open-source-compliance-specification.md)
- Anforderungen an Lizenzvolltexte siehe [LICENSE-Spezifikation](./license-specification.md)
- Relevante README-Kapitel siehe [README-Abschnittsspezifikation](./readme-sections-specification.md)
- Konsistenz gehört zu den Qualitätstoren G7–G9, siehe [Qualitätstor](./quality-gate.md)
