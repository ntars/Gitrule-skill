# LICENSE-Spezifikation

> Problem, das diese Datei löst: Definiert die SPDX-Kennzeichnung der Projektlizenz, die Anforderungen an den LICENSE-Volltext, die Position der Copyright-Zeile, den Erkennungsmechanismus von GitHub, die Dateianordnung bei geschichteter Lizenzierung samt Bestätigungsablauf sowie die Regel, dass ohne Bestätigung nichts eingetragen werden darf.

## 1. Grundregeln

1. Die Projektlizenz muss über ihren SPDX-Bezeichner in der README ausdrücklich genannt und mit einer entsprechenden LICENSE-Datei hinterlegt werden.
2. Die LICENSE-Datei muss den offiziellen englischen Volltext dieser Lizenz enthalten; Klauseln dürfen nicht gestrichen oder geändert werden. Umformulieren, Umsortieren der Absätze oder Neuformatierung als Markdown lässt die automatische Erkennung scheitern.
3. Die Copyright-Zeile steht am Dateikopf oder in Kapitel 19 der README; das Format siehe [README-Abschnittsspezifikation](./readme-sections-specification.md).

## 2. Erkennungsmechanismus von GitHub

GitHub bestimmt die Lizenz eines Repositorys mit dem Open-Source-Werkzeug licensee. Das Ergebnis steuert das Abzeichen auf der Repository-Seite, das Feld `license` der API und ob eine Suche nach dem Schlüsselwort `license` das Repository findet. Die Regeln lauten:

1. Gescannt werden nur zwei Orte: das Projektstammverzeichnis und ein `LICENSES/`-Verzeichnis oberster Ebene. Gleichnamige Dateien in `locales/`, `docs/` oder anderen Unterverzeichnissen wirken nicht mit.
2. Im Stammverzeichnis werden Dateien nach ihrem Namen bewertet, die höchste Bewertung gewinnt: `LICENSE` zählt 1.00, `LICENSE.md` 0.95, `COPYING` 0.90, mit Suffix versehene Formen wie `LICENSE-MIT` 0.70.
3. In einem `LICENSES/`-Verzeichnis oberster Ebene zählt ein Dateiname im SPDX-Bezeichnerformat mit der Endung `.txt`, `.md`, `.markdown` oder `.html` als 1.00; alles andere als 0.00.
4. Der Inhalt muss eng mit dem offiziellen Volltext der Lizenz übereinstimmen. Eine Datei, die nur eine Angabe wie „Dieses Projekt verwendet die Lizenz X“ enthält, wird nicht erkannt, und das von ihr erzeugte Ergebnis wäre ein Nicht-Standardwert.
5. Werden mehrere unterschiedliche Lizenzen erkannt, liefert das Ergebnis auf Projektebene möglicherweise keine konkrete Lizenz, und die Repository-Seite zeigt `View license` oder `Other`.
6. Erklärungen in natürlicher Sprache in der README wirken nicht mit. Der Satz „Dieses Projekt steht unter der MIT-Lizenz“ führt nicht zur Erkennung als MIT.

Daher gilt: **Die Erklärung in der README und die LICENSE-Datei sind zwei unabhängige Mechanismen, und beide sind erforderlich.** Liegen im Stammverzeichnis mehrere Lizenzdateien, hängt es zugleich von der Namensbewertung und der Inhaltsübereinstimmung ab, welche letztlich gemeldet wird, und ist nicht vorhersagbar; in Messungen meldeten Repositorys mit Doppellizenz nur eine der beiden.

## 3. Dateianordnung bei geschichteter Lizenzierung

Geschichtete Lizenzierung bedeutet, dass für verschiedene Teile eines Repositorys verschiedene Lizenzen gelten, etwa Code unter MIT und Dokumentation unter CC BY 4.0. Die Anordnung wird in dieser Reihenfolge entschieden:

| Option | Was ins Stammverzeichnis kommt | Ergebnis der Erkennung | Einsatzbedingung |
| --- | --- | --- | --- |
| Einzelschicht (Standard) | Eine `LICENSE` | Stabile Erkennung dieser Lizenz | Alle Schichten nutzen dieselbe Lizenz, oder die Abweichung ändert die Pflichten der Nutzer nicht |
| Schichten mit Erläuterung | `LICENSE` trägt die Hauptlizenz, zusätzlich eine `LICENSING.md` | Stabile Erkennung der Lizenz aus der Stamm-`LICENSE` | Schichtung ist nötig und das Abzeichen soll eindeutig bleiben |
| Schichten mit REUSE | `LICENSES/` oberster Ebene enthält jeden Volltext | Kann zu einem Nicht-Standardwert entarten | Nur wenn die nachgelagerte Seite REUSE-Konformität ausdrücklich verlangt |

Abwägungen:

1. Legen Sie nicht mehrere Lizenzdateien im Stammverzeichnis ab. In Messungen meldete jedes Repository mit Doppellizenz nur eine seiner beiden Lizenzen; die andere blieb auf der Repository-Seite und in der API unsichtbar, was einer öffentlichen Erklärung nur einer Lizenz gleichkommt.
2. Die REUSE-Anordnung steht im Konflikt mit der Eindeutigkeit des Abzeichens: Mehrere Lizenzen in `LICENSES/` werden als mehrere Lizenzen gelesen, was ein grünes `reuse lint` um den Preis eines unklaren Erkennungsergebnisses erkauft. Beides lässt sich nicht zugleich vollständig erfüllen; das Projekt muss abwägen.
3. Bei der Option „Schichten mit Erläuterung“ entspricht der Dateiname `LICENSING.md` weder dem Muster `LICENSE` noch dem Muster `COPYING`, wird also nicht für eine Lizenzdatei gehalten und beeinträchtigt die Erkennung der Stamm-`LICENSE` nicht.
4. Unabhängig von der gewählten Anordnung muss Kapitel 19 der README den SPDX-Ausdruck (etwa `MIT AND CC-BY-4.0`) und den Geltungsbereich jeder Schicht nennen. Das ist der einzige Ort, an dem die Information beim menschlichen Lesen erhalten bleibt.

## 4. Entscheidung über Schichtung und Bestätigungsablauf

Geschichtete Lizenzierung hat rechtliche Bedeutung. Vor dem Schreiben oder Optimieren ist Runde für Runde zu bestätigen; nichts darf erfunden werden.

1. Schichten Sie nicht aus eigenem Antrieb. Hat der Nutzer es nicht ausdrücklich verlangt, behandeln Sie das Projekt als einschichtig und vermerken im Bericht: „Falls eine Schichtung nötig ist, sind die möglichen Optionen und ihre Unterschiede folgende.“
2. Jeder Vorschlag zur Schichtung muss seine Grundlage offenlegen: was jede Schicht tatsächlich abdeckt, die Kandidatenlizenzen und den Unterschied ihrer Pflichten, die Wirkung auf nachgelagerte Nutzer und wie sich das Erkennungsergebnis ändern würde.
3. Bestätigen Sie mindestens zweimal vor dem Schreiben: zuerst die Kombination (welche Lizenz für welche Schicht), dann die Dateianordnung (welche Lizenz in die Stammdatei kommt, ob `LICENSES/` angelegt wird).
4. Bestätigen Sie erneut vor dem Push. Nach dem Erzeugen teilen Sie ausdrücklich mit: „Die Dateien wurden erzeugt; bitte prüfen und selbst committen.“ Committen oder pushen Sie niemals für den Nutzer.
5. Nicht bestätigte Optionen gehören nur in einen Bericht oder eine temporäre Datei; sie dürfen nicht als `LICENSE`, `LICENSES/` oder `LICENSING.md` geschrieben werden.
6. Lässt sich ein Teil keiner Schicht zuordnen, kennzeichnen Sie ihn mit „Zu bestätigen: Schichtzuordnung“ und listen die fraglichen Dateien auf; ordnen Sie nicht standardmäßig zu.

## 5. Anforderungen an den Haftungsausschluss

Lizenztexte haben rechtliche Wirkung. Vorlagen und Werkzeuge liefern nur Entscheidungsregeln und Dateianordnungen und stellen keine Rechtsberatung dar.

1. Kapitel 19 der README oder die Datei `LICENSING.md` muss einen Haftungsausschluss enthalten, der klarstellt, dass die Lizenzwahl vom Projektträger selbst bestätigt wird.
2. Der Haftungsausschluss muss mit dem in der NOTICE übereinstimmen; er darf nicht an einer Stelle vorhanden und an der anderen absent sein.
3. Behaupten Sie nicht, „die Konformitätsprüfung sei abgeschlossen“. Teilen Sie nur mit, dass „Dateianordnung und SPDX-Kennzeichnungen nach den Regeln auf Vollständigkeit geprüft wurden“.
4. Die rechtliche Wirkung geschichteter Lizenzierung folgt dem Volltext der jeweiligen Lizenz. Beschreibender Text im Repository ist nur ein Index und ändert die Klauseln nicht.

## Verwandte Dateien

- Ohne LICENSE wird der Push blockiert, harte Regel H2, siehe [Harte Regeln](./hard-rules.md)
- Beurteilung der Lizenzkompatibilität von Abhängigkeiten siehe [Open-Source-Compliance-Spezifikation](./open-source-compliance-specification.md)
- Separate Datei für Erklärungen Dritter siehe [NOTICE-Spezifikation](./notice-specification.md)
- Lizenzgenauigkeit gehört zu den Qualitätstoren G7/G8, siehe [Qualitätstor](./quality-gate.md)
