# Allgemeine Schreibspezifikation

> Problem, das diese Datei löst: Definiert Stil, Genauigkeit, Terminologiekonsistenz, Formatdetails und unzulässige Inhalte für alle ausgelieferten Dokumente, damit die Formulierungen präzise, eindeutig und reproduzierbar sind.

## 1. Stil

1. Schriftsprache verwenden, Aussage- und Aufforderungssätze einsetzen.
2. Umgangssprachliche Ausdrücke sind unzulässig, zum Beispiel „咱们“, „超简单“, „搞定“, „贼快“, „一键起飞“.
3. Ausrufezeichen, Auslassungspunkte, Netzjargon und Emojis sind unzulässig.
4. Rhetorische Fragen oder Scheinfragen dürfen nicht als Abschnittseinstieg verwendet werden.

## 2. Genauigkeit

1. Jeder Satz muss eine vollständige Bedeutung ausdrücken und darf nicht auf Schlussfolgerungen aus dem Kontext angewiesen sein.
2. Unbestimmte Verweise wie „es“, „dies“, „betreffend“, „einige“, „mehrere“ sind unzulässig; wenn ein Verweis erforderlich ist, ist das vollständige Substantiv zu verwenden.
3. Zeitangaben, Versionsnummern, Pfade, Befehle, Funktionsnamen und Konfigurationsschlüsselnamen müssen präzise und mit dem tatsächlichen Projektstand übereinstimmen.
4. Befehle müssen unmittelbar ausführbar sein und die Angabe des erforderlichen aktuellen Arbeitsverzeichnisses enthalten.
5. Bei Versionsnummern ist die Semantik der Versionsbeschränkung anzugeben, zum Beispiel `>=1.2.0 <2.0.0`.

## 3. Terminologiekonsistenz

1. Bei der ersten Nennung eines Begriffs ist eine Definition anzugeben, im Format „chinesischer Begriff (English Term, Abkürzung)“.
2. Für dasselbe Konzept wird im gesamten Text nur eine Formulierung verwendet; die chinesische und die englische Fassung sind eineindeutig einander zugeordnet.
3. Eine chinesisch-englische Terminologietabelle ist zu pflegen und im README-Anhang oder in einer eigenständigen Datei abzulegen; beide Sprachfassungen nutzen dieselbe Vergleichstabelle (Vorlage siehe [Informationserfassung und Vorlagen](./information-collection-and-templates.md)).

## 4. Formatvorgaben

1. Die Überschriftenhierarchie beginnt bei `##` (`#` ist dem Projektnamen vorbehalten); Ebenen dürfen nicht übersprungen werden.
2. Jede Überschrift der zweiten Ebene entspricht einem Abschnitt gemäß [README-Abschnittsspezifikation](./readme-sections-specification.md); die Reihenfolge darf nicht geändert werden.
3. Tabellen müssen eine Kopfzeile und eine einheitliche Spaltenzahl haben; Befehle, Pfade, Code und Konfigurationsschlüsselnamen sind mit Inline-Code zu kennzeichnen.
4. Codeblöcke müssen eine Sprachkennung tragen; mehrzeilige Befehle müssen als Ganzes kopierbar und ausführbar sein.
5. Externe Links verwenden vollständige URLs, keine Kurzlinks; interne Sprünge verwenden relative Pfad-Anker.
6. Zwischen chinesischen und englischen Zeichen sowie Ziffern ist ein Leerzeichen zu setzen; chinesische und englische Satzzeichen dürfen nicht gemischt werden.

## 5. Platzhalterkonvention

1. Formelle Platzhalter in kopierbaren Vorlagen werden einheitlich als `{{纯名}}` geschrieben, zum Beispiel `{{仓库地址}}`; der Name darf keine Konjunktionen wie „oder“, „，“ enthalten, die eine Auswahl aus mehreren bedeuten, und darf auch kein erklärender Satz sein.
2. Formelle Platzhalter müssen in der Platzhaltertabelle der zugehörigen Vorlage registriert werden; der Eintrag enthält Bedeutung, Beispiel und Angabe zur Pflicht.
3. Inhalt in geschweiften Klammern natürlicher Sprache in Spezifikationsbeispielen oder Ausfüllhinweisen dient nur als Beispiel, ist kein formeller Platzhalter und wird nicht in die Tabelle aufgenommen; bei der Erzeugung des endgültigen Dokuments muss er vollständig durch tatsächliche Inhalte ersetzt werden.
4. Verschachtelte geschweifte Klammern, Backticks oder ein zweiter Platzhalter dürfen nicht als Platzhaltername verwendet werden.

## 6. Verbotsliste

Unzulässig sind: ungeprüfte Leistungszahlen, Vergleiche ohne Quellenangabe, Zusicherungen (etwa „garantiert kompatibel mit allen Umgebungen“, „dauerhaft kostenlos“), abwertende Beschreibungen fremder Projekte sowie projektfremde Werbeinhalte.

## Verwandte Dateien

- Abschnittsstruktur siehe [README-Abschnittsspezifikation](./readme-sections-specification.md)
- Zweisprachige Terminologiezuordnung siehe [Mehrsprachigkeits-Spezifikation](./multilingual-specification.md)
- Qualitätsbeurteilung G1 (Umgangssprache und Mehrdeutigkeit) siehe [Qualitätstor](./quality-gate.md)
