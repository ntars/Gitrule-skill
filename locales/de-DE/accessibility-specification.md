# Barrierefreiheits-Spezifikation

> Problem, das diese Datei löst: Sie definiert Anforderungen an die Barrierefreiheit von Projektdokumentation, README und Benutzeroberflächen, damit Inhalte für Leser mit Screenreader, Tastaturbedienung und unterschiedlichen visuellen Bedingungen gleichermaßen nutzbar sind.

## 1. Anwendungsbereich

1. Dokumentations-Barrierefreiheit: README, Dokumentationsseite, Beispielcode, Tabellen, Bilder.
2. Oberflächen-Barrierefreiheit: Benutzeroberflächen von Anwendungen und Webprojekten.
3. Kommandozeilen-Barrierefreiheit: Hilfetexte, Fehlermeldungen und Ausgabeformate.

## 2. Dokumentations-Barrierefreiheit

### 2.1 Bilder und Medien

1. Jedes Bild muss einen `alt`-Text bereitstellen, der Bildinhalt und Zweck beschreibt; dekorative Bilder erhalten einen leeren `alt`.
2. Informationslose Texte wie „Bild“, „Screenshot“ oder „image“ dürfen nicht als `alt` verwendet werden.
3. Bei animierten GIFs ist der Inhalt im angrenzenden Text zu erläutern, damit Informationen nicht ausschließlich über die Animation vermittelt werden.
4. Diagramme müssen zusätzlich eine Textbeschreibung oder Datentabelle bereitstellen; Datenreihen dürfen nicht ausschließlich durch Farbe unterschieden werden.

### 2.2 Überschriften und Struktur

1. Die Überschriftenhierarchie ist durchgängig und darf keine Stufen überspringen (siehe [README-Visual-Layout-Spezifikation](./readme-visual-layout-specification.md)).
2. Der gesamte Text enthält genau eine Überschrift der ersten Ebene.
3. Listen verwenden die reguläre Markdown-Syntax, damit Screenreader sie als Liste erkennen.
4. Tabellen müssen eine Kopfzeile besitzen; Tabellen ohne Kopfzeile dürfen nicht zum Seitenlayout verwendet werden.

### 2.3 Links und Text

1. Der Linktext muss das Ziel eigenständig beschreiben; „hier klicken“ und „mehr“ sind verboten.
2. Farbe darf nicht das einzige Mittel zur Informationsvermittlung sein, sondern muss durch Text oder Symbole ergänzt werden.
3. Bei gemischtsprachigem Text sind Leerzeichen zu erhalten, damit Worttrennung und Vorlesen korrekt funktionieren.
4. Abkürzungen sind bei der ersten Verwendung auszuschreiben.

### 2.4 Code und Tabellen

1. Codeblöcke sind mit einer Sprache zu kennzeichnen, damit Hilfsmittel sie erkennen (siehe [README-Visual-Layout-Spezifikation](./readme-visual-layout-specification.md)).
2. Der Inhalt von Tabellenzellen bleibt knapp; zusammengeführte Zellen über mehrere Zeilen sind zu vermeiden, da sie die Auswertung durch Screenreader erschweren.
3. Lange Befehle werden mit Zeilenumbrüchen dargestellt und dürfen nicht auf horizontales Scrollen angewiesen sein.

## 3. Oberflächen-Barrierefreiheit

### 3.1 Tastaturbedienung

1. Alle interaktiven Elemente müssen per Tastatur erreichbar und bedienbar sein.
2. Die Fokusreihenfolge entspricht der visuellen Reihenfolge; der Fokuszustand ist deutlich sichtbar.
3. Ein Schnelleinstieg zum Überspringen wiederholter Inhalte ist bereitzustellen (etwa ein Sprung zum Hauptinhalt).

### 3.2 Semantik und Beschriftung

1. Semantische Elemente drücken Struktur und Rolle aus; nicht-semantische Elemente dürfen nicht zur Nachbildung von Steuerelementen verwendet werden.
2. Formularsteuerelemente benötigen zugeordnete Beschriftungen; Fehlermeldungen sind mit dem zugehörigen Feld zu verknüpfen.
3. Dynamische Statusänderungen werden über barrierefreie Hinweise an assistive Technologien übermittelt.

### 3.3 Visuelle Bedingungen

1. Der Kontrast zwischen Text und Hintergrund erfüllt die Lesbarkeitsanforderungen; der Kontrast für Fließtext beträgt mindestens 4,5:1, für großen Text mindestens 3:1.
2. Helle und dunkle Systemthemen werden unterstützt; der Themenwechsel verändert die Informationsstruktur nicht (siehe [README-Visual-Layout-Spezifikation](./readme-visual-layout-specification.md)).
3. Animationen bieten eine Option zur Reduzierung; automatisch abspielende hochfrequente Blinkinhalte sind zu vermeiden.
4. Bei Textskalierung auf 200 % bleibt das Layout nutzbar, ohne dass Inhalte abgeschnitten werden.

## 4. Kommandozeilen-Barrierefreiheit

1. Fehlermeldungen nennen Ursache und mögliche Korrekturmaßnahme; die Ausgabe eines Fehlercodes allein ist unzulässig.
2. Die Ausgabe von `--help` ist klar gegliedert und führt Pflichtparameter sowie Standardwerte auf.
3. Eine Umgebungsvariable zum Deaktivieren farbiger Ausgabe wird unterstützt, um Screenreader und Logverarbeitung zu erleichtern.
4. Interaktive Eingabeaufforderungen bieten äquivalente nicht-interaktive Parameter für Automatisierungsszenarien.

## 5. Prüfliste

- [ ] Alle Bilder besitzen aussagekräftige `alt`-Texte.
- [ ] Die Überschriftenhierarchie ist durchgängig, der Text enthält genau eine Überschrift der ersten Ebene.
- [ ] Linktexte sind eigenständig verständlich.
- [ ] Tabellen besitzen Kopfzeilen, Farbe ist kein alleiniger Informationsträger.
- [ ] Codeblöcke sind mit einer Sprache gekennzeichnet.
- [ ] Oberflächenelemente sind per Tastatur bedienbar, der Fokus ist sichtbar.
- [ ] Der Kontrast erfüllt die Mindestanforderungen, helle und dunkle Themen sind lesbar.
- [ ] Hilfetexte und Fehlermeldungen leiten zur nächsten Aktion an.

## 6. Verbotene Praktiken

1. Das Vermitteln zentraler Informationen ausschließlich über Bilder ohne Textalternative ist verboten.
2. Das Darstellen von Status oder Fehlern ausschließlich durch Farbe ist verboten.
3. Die Verwendung bedeutungsloser Linktexte ist verboten.
4. Das Entfernen von Fokusindikatoren ohne Ersatz ist verboten.

## Verwandte Dateien

- Dokumentationslayout: [README-Visual-Layout-Spezifikation](./readme-visual-layout-specification.md)
- Barrierefreiheitsanforderungen für Badges: [Badge-Spezifikation](./badge-specification.md)
- Schreibstandards: [Allgemeine Schreib-Spezifikation](./general-writing-specification.md)
- Dokumentationsqualität gehört zu Dimension D12, siehe [Prüfungsdimensionsmatrix](./review-dimension-matrix.md)
