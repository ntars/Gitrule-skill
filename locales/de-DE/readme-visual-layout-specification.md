# README-Spezifikation für visuelles Layout

> Problem, das diese Datei löst: Sie definiert die typografische Hierarchie, die Absatzgliederung, die Einsatzszenarien für Tabellen, Screenshots und GIFs sowie deren Platzierung, damit die Dokumentation ein ausgewogenes Verhältnis zwischen Informationsdichte und visueller Attraktivität erreicht.

Die „Messwerte“ in diesem Dokument stammen aus einer Stichprobenerhebung dieses Projekts zu READMEs führender Open-Source-Projekte (Stichprobe N=120); die Referenzpraktiken wurden durch die Auswertung der Startbildschirm-Struktur mehrerer Projekte mit hoher Sternenzahl belegt.

## 1. Typografische Hierarchie

### 1.1 Überschriftenebenen

Die README muss eine klare Überschriftenhierarchie aufbauen und folgende Vorgaben einhalten:

1. Im gesamten Dokument bleibt genau eine Hauptüberschrift (`#`) erhalten, nämlich der Projektname, in der ersten Zeile der Datei.
2. Überschriften der zweiten Ebene (`##`) sind die Hauptabschnitte; ihre Anzahl sollte bei 6–12 liegen; der gemessene Median beträgt 7.
3. Überschriften der dritten Ebene (`###`) dienen der Untergliederung innerhalb eines Abschnitts und werden nur verwendet, wenn der Inhalt eines Abschnitts der zweiten Ebene lang ist.
4. Sprünge in der Überschriftenhierarchie (etwa von `#` direkt zu `###`) sind unzulässig.
5. Der Überschriftentext ist knapp, verwendet Substantive oder Nominalphrasen und endet ohne Schlusspunkt.

### 1.2 Reihenfolge der Startbildschirm-Struktur

Als Startbildschirm gilt der ohne Scrollen sichtbare Inhalt; er wird in folgender Reihenfolge gegliedert:

1. Zentriertes Logo oder Projektbanner (optional);
2. Hauptüberschrift (Projektname);
3. Badge-Zeile (Details siehe [Badge-Spezifikation](./badge-specification.md));
4. Ein-Satz-Positionierung (was das Projekt ist, für wen es gedacht ist, welches Problem es löst);
5. Zeile mit Navigationslinks zu den Abschnitten (optional, für lange READMEs);
6. Zusammenfassung der Kernfunktionen oder Kernmerkmale.

Referenzbelege: `fd` und `ripgrep` setzen direkt nach der Positionierung die Abschnittsnavigation; `next.js` und `rust-lang/rust` eröffnen mit zentriertem Logo und Banner; `vscode` fügt direkt nach der Positionierung einen Produktscreenshot ein.

### 1.3 Absätze und Weißraum

- Jeder Absatz sollte auf 1–4 Zeilen begrenzt werden, um dichte Textblöcke zu vermeiden.
- Zwischen Absätzen wird eine Leerzeile eingefügt, um nach dem Rendern für Auflockerung zu sorgen.
- Zentrale Aussagen stehen vorn, Erläuterungen folgen.
- Zwischen chinesischen und englischen Zeichen sowie Zahlen wird ein Leerzeichen eingefügt; Satzzeichen werden je nach Kontext verwendet.

## 2. Regeln zur Verwendung von Tabellen

### 2.1 Einsatzszenarien

Tabellen eignen sich für mehrdimensionale, vergleichbare Informationen. Gemessen verwenden 36,7 % der Stichproben Tabellen; sie sind die empfohlene Form für Konfigurationshinweise, Kompatibilitätsmatrizen und Befehlsübersichten. Geeignete Szenarien sind:

- Beschreibung von Konfigurationsoptionen (Schlüssel, Typ, Standardwert, Wirkung);
- Kompatibilitätsmatrix für Plattformen und Versionen;
- Gegenüberstellung von Befehlen oder Parametern;
- Funktionsvergleich (dieses Projekt gegenüber anderen Lösungen);
- Roadmap und Status.

### 2.2 Platzierung

Die Tabelle folgt unmittelbar der zugehörigen Überschrift der zweiten Ebene; ein einleitender Satz davor erläutert den Zweck der Tabelle. Gibt es nach der Tabelle Ausnahmen, werden diese in einem eigenen Absatz ergänzt.

### 2.3 Vorgaben zur Schreibweise

| Anforderung | Erläuterung |
| --- | --- |
| Spaltenanzahl begrenzen | 3–6 Spalten; bei mehr als 6 Spalten ist eine Aufteilung zu erwägen |
| Eindeutige Tabellenköpfe | Jede Spalte erhält einen kurzen substantivischen Kopf; leere Köpfe sind zu vermeiden |
| Einheitliche Ausrichtung | Die Ausrichtung der Tabellen ist im gesamten Dokument einheitlich |
| Kurze Inhalte | In Zellen keine langen Absätze; bei Bedarf über Fußnoten oder Links ausführen |
| Keine leeren Zellen | Wo kein Inhalt vorhanden ist, „keine“ oder „nicht zutreffend“ angeben |

## 3. Regeln zur Verwendung von Codeblöcken

### 3.1 Einsatzszenarien

Codeblöcke dienen Befehlen, Konfigurationen, API-Aufrufen und Beispielausgaben. Gemessen enthalten 66,7 % der Stichproben Codeblöcke; sie sind Pflichtbestandteil des Abschnitts „Schnellstart“, der Median beträgt 2.

### 3.2 Vorgaben zur Schreibweise

1. Jeder Codeblock muss eine Sprachkennung tragen, etwa `bash`, `json`, `python`, `javascript`, um die Syntaxhervorhebung zu ermöglichen.
2. Befehlsbeispiele enthalten vollständige ausführbare Befehle; vorangehende Schritte dürfen nicht ausgelassen werden.
3. Soll ein Ergebnis gezeigt werden, wird ein separater Codeblock mit der Kennung `text` angelegt und die erwartete Ausgabe im Text erläutert.
4. Vor und nach jedem Codeblock steht je eine Leerzeile.
5. Der Inhalt eines einzelnen Blocks ist auf höchstens 20 Zeilen begrenzt; längere Beispiele werden in mehrere Blöcke aufgeteilt oder in das Verzeichnis `examples/` verschoben und verlinkt.
6. Wird bei interaktiven Befehlen die Eingabeaufforderung `$` verwendet, muss dies im gesamten Dokument einheitlich geschehen.

Formatbeispiel:

```bash
npm install <package-name>
```

```text
✓ Installation complete
```

## 4. Regeln zur Verwendung von Screenshots und GIFs

### 4.1 Einsatzszenarien und Abwägung

| Element | Geeignete Szenarien | Hinweise |
| --- | --- | --- |
| Statischer Screenshot | Anwendungsoberfläche, Ausführungsergebnis, Diagramme | Gemessene Nutzungsrate 63,3 %, am häufigsten verwendet |
| GIF / Animation | Kommandozeilen-Demo, Interaktionsablauf, Vorher-Nachher-Vergleich | Große Dateigröße, Komprimierung erforderlich, Laufzeit begrenzen |
| Logo / Banner | Markenwiedererkennung, Startbildschirm | Dunkle und helle Variante bereitstellen |
| Schemagrafik | Architektur, Abläufe, Datenfluss | Muss mit der Dokumentationsversion synchron aktualisiert werden |

Gemessen enthalten 63,3 % der Stichproben Bilder. Referenzbelege: `fd` verwendet `doc/screencast.svg` als Demo, `ripgrep` verwendet einen Screenshot der Suchergebnisse, `vscode` verwendet einen Screenshot der laufenden Anwendung, `rust` und `next.js` verwenden ein an helles und dunkles Farbschema angepasstes Logo-Banner.

### 4.2 Platzierung

1. Logo / Banner: ganz oben in der Datei, zentriert.
2. Produktscreenshot: nach der Ein-Satz-Positionierung und vor „Schnellstart“, um eine unmittelbare Vorstellung zu vermitteln.
3. GIF-Demo: eigener Abschnitt „Demo / Vorführung“ unmittelbar nach „Kernfunktionen“.
4. Architekturgrafik: in den Abschnitt „Architektur“ oder „Entwurf“ aufnehmen oder nach `docs/architecture.md` verschieben und in der README verlinken.

### 4.3 Vorgaben zur Schreibweise

- Für jedes Bild muss ein `alt`-Text angegeben werden, der den Bildinhalt beschreibt; nichtssagende Texte wie `image` oder `Screenshot` sind unzulässig.
- Bilder werden über relative Pfade auf Ressourcen im Repository verwiesen oder über stabile absolute URLs eingebunden; zeitlich befristete temporäre Links sind zu vermeiden.
- Für Bilder, die sich an das Farbschema anpassen müssen, wird HTML `<picture>` zusammen mit `prefers-color-scheme` verwendet, um helle und dunkle Varianten bereitzustellen.
- Dateigröße begrenzen: Für Screenshots bevorzugt WebP oder optimiertes PNG verwenden, GIFs bevorzugt in kurze Videos oder komprimierte Animationen umwandeln.
- Bildbreite anpassen: über das Attribut `width` oder einen äußeren Container begrenzen, damit das Seitenlayout nicht gesprengt wird.

## 5. Links und Navigation

### 5.1 Abschnittsnavigation

Überschreitet die README 200 Zeilen, wird im Startbildschirm eine Zeile mit Navigationslinks zu den Hauptabschnitten eingefügt:

```markdown
[Installation](#installation) · [Schnellstart](#schnellstart) · [Dokumentation](#dokumentation) · [Beitragen](#beitragen)
```

### 5.2 Relative Links bevorzugen

Dokumente, Bilder und Lizenzen innerhalb des Repositorys werden durchgängig über relative Pfade referenziert, damit sie auch in Forks und beim Offline-Lesen funktionieren. Externe Links müssen auf autoritative Quellen verweisen (offizielle Dokumentation, Paketverwaltungsseite, CI-Seite).

## 6. Checkliste für Ästhetik und Attraktivität

1. Der Startbildschirm enthält ein Logo oder eine klare Überschrift und vermittelt die Positionierung des Projekts innerhalb von 3 Sekunden.
2. Badges haben einen einheitlichen Stil, eine semantische Farbgebung und eine angemessene Anzahl.
3. Es gibt genau eine Hauptüberschrift und 6–12 Überschriften der zweiten Ebene, ohne Sprünge in der Hierarchie.
4. Mindestens ein kopierbares und lauffähiges Codebeispiel ist vorhanden.
5. Mindestens ein Screenshot oder eine Demo, der bzw. die den Produktwert zeigt, ist vorhanden.
6. Tabellen werden für Vergleichsinformationen verwendet, mit begrenzter Spaltenzahl und klaren Köpfen.
7. Alle Bilder haben `alt`-Texte, alle Codeblöcke eine Sprachkennung.
8. Lange Dokumente verfügen über eine Abschnittsnavigation.
9. Bilder und Badges sind in hellem und dunklem Farbschema lesbar.

## Verwandte Dateien

- Badge-Stil und Farbgebung siehe [Badge-Spezifikation](./badge-specification.md)
- Vollständige Abschnittsliste siehe [README-Abschnittsspezifikation](./readme-sections-specification.md)
- Visuelle Schwerpunkte je Projekttyp siehe [README-Leitfaden zur Kategorieanpassung](./readme-category-adaptation-guide.md)
- Direkt übernehmbares Layout-Gerüst siehe [README-Standardvorlage](./readme-standard-template.md)
- Messstichproben und Methodik siehe [README-Vorlagen-Recherchebericht](./readme-template-research-report.md)
