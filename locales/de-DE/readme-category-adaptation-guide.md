# README-Leitfaden zur Kategorieanpassung

> Problem, das diese Datei löst: Sie gibt für unterschiedliche Projekttypen – Bibliotheken, Anwendungen, Kommandozeilenwerkzeuge, Frameworks und Ressourcensammlungen – differenzierte Empfehlungen zur Auswahl der README-Abschnitte, zu visuellen Schwerpunkten und zur Badge-Konfiguration und erläutert, wie die Elemente jedes Typs Ästhetik und Attraktivität steigern.

Die universelle Vorlage eignet sich für alle Projekte, doch die Leserschaft unterschiedlicher Projekttypen hat unterschiedliche Schwerpunkte. Dieser Leitfaden gibt aufbauend auf der allgemeinen Spezifikation typbezogene Anpassungsempfehlungen. Als Grundlage dient die [README-Standardvorlage](./readme-standard-template.md); die Anpassung erfolgt nach dem jeweiligen Typ gemäß diesem Dokument.

## 1. Typenübersicht

| Typ | Zentrale Leserfrage | Schwerpunkt des Startbildschirms | Erforderliche Abschnitte | Entbehrliche Abschnitte |
| --- | --- | --- | --- | --- |
| Bibliothek / SDK | Installationsweg und API-Nutzung | Version und Lizenz | Installation, Schnellstart, API, Kompatibilität | Bereitstellung, Screenshots |
| Anwendung | Aussehen der Anwendung und Kernfunktionen | Screenshots und Funktionen | Funktionen, Screenshots, Installation, Schnellstart | API-Referenz |
| Kommandozeilenwerkzeug | Befehlsnutzung und Leistung | Befehlsbeispiele und Demo | Installation, Nutzung, Befehlsübersicht, Demo | Architektur, Konfiguration (bei geringem Umfang) |
| Framework | Ökosystem und Lernaufwand | Einstieg in die Dokumentation und Beispiele | Positionierung, Schnellstart, Dokumentation, Community | Leistungsdetails (extern verlinkbar) |
| Ressourcensammlung | Was wird aufgenommen, wie wird gesucht | Kategorisierung und Navigation | Verzeichnis, Kategorien, Beitragsleitfaden | Installation, API |

## 2. Bibliothek / SDK

Typische Vertreter: HTTP-Clients wie axios, Hilfsfunktionsbibliotheken, Client-SDKs.

### 2.1 Auswahl der Abschnitte

- Vorangestellt „Ein-Satz-Positionierung + Version + Lizenz“, damit Lesende die Kompatibilität beurteilen können.
- „Installation“ steht ganz vorn und enthält den Paketverwaltungsbefehl (npm, pip, cargo usw.).
- „Schnellstart“ muss ein vollständiges, eigenständig lauffähiges Beispiel sein.
- „API-Referenz“ wird ausführlich in der Haupt-README oder unter `docs/api.md` geführt; bei sehr vielen API-Einträgen enthält die README nur eine Zusammenfassung mit Link.
- „Kompatibilität“ erläutert unterstützte Sprachversionen, Laufzeiten und Plattformen.

### 2.2 Visuelle Schwerpunkte

- Badge-Schwerpunkte: Version, Build-Status, Lizenz, Downloadzahl, Paketgröße.
- Bilder sparsam einsetzen; Screenshots sind in der Regel nicht erforderlich; ein kleines Logo kann der Wiedererkennung dienen.
- API-Parameter in Tabellenform darstellen, um die Lesbarkeit zu erhöhen.

### 2.3 Ansatzpunkte zur Steigerung der Ästhetik

1. Version und Lizenz als Badges oben platzieren, um unmittelbar Vertrauen aufzubauen.
2. Den Schnellstart-Codeblock nahe am Startbildschirm platzieren, um die Einstiegshürde zu senken.
3. In API-Tabellen Spaltenbreite und Standardwertspalte vereinheitlichen, um die kognitive Belastung zu verringern.

## 3. Anwendungen

Typische Vertreter: Editoren, Desktop-Werkzeuge, Produkte für Endanwendende.

### 3.1 Auswahl der Abschnitte

- Der Startbildschirm muss einen Produktscreenshot oder ein Laufzeitbild enthalten: erst den Wert zeigen, dann die Umsetzung erläutern.
- „Kernfunktionen“ werden nach Nutzungsszenarien gegliedert, nicht nach technischen Modulen.
- „Installation“ deckt Installationspakete oder Download-Einstiege für alle Plattformen ab.
- „Schnellstart“ nennt den kürzesten Einstiegsweg.
- Hinweise zum Build aus dem Quellcode können auf `CONTRIBUTING.md` verlinken.

### 3.2 Visuelle Schwerpunkte

- Badge-Schwerpunkte: Version, Build-Status, Lizenz, Downloadzahl.
- Der Screenshot steht nach der Positionierung und ist das Kernelement des Startbildschirms.
- Funktionslisten werden mit Symbolen oder kurzen Screenshots kombiniert, um das Überfliegen zu erleichtern.

### 3.3 Ansatzpunkte zur Steigerung der Ästhetik

1. Hochwertige Produktscreenshots zentriert darstellen und an helles und dunkles Farbschema anpassen.
2. Funktionspunkte als kurze Sätze mit Symbolen statt langer Beschreibungen.
3. Download-Einstiege auffällig gestalten und als schaltflächenartige Links umsetzen.

## 4. Kommandozeilenwerkzeuge

Typische Vertreter: Terminalwerkzeuge wie fd und ripgrep.

### 4.1 Auswahl der Abschnitte

- Direkt nach der „Ein-Satz-Positionierung“ folgt die Abschnittsnavigation, um das Springen zu erleichtern.
- „Installation“ listet gängige Paketverwaltungen und Plattform-Binärdateien auf.
- „Nutzung“ ist aufgabenorientiert und enthält Beispiele häufig verwendeter Befehle.
- „Befehlsübersicht“ oder „Vergleich mit ähnlichen Werkzeugen“ ist ein häufig nachgefragtes Bedürfnis.
- „Demo“ zeigt mit GIF oder Terminalaufzeichnung die tatsächliche Wirkung.
- Leistungsdaten müssen Testumgebung und -methode nennen.

### 4.2 Visuelle Schwerpunkte

- Badge-Schwerpunkte: Version, Build-Status, Plattformunterstützung, Lizenz.
- Das Demo-GIF ist das zentrale visuelle Asset und zeigt Geschwindigkeit und Nutzungserlebnis.
- Befehle in Codeblöcken mit Sprachkennung, Ausgaben in `text`-Blöcken.

### 4.3 Ansatzpunkte zur Steigerung der Ästhetik

1. Befehlsbeispiele oben platzieren, sodass Lesende sie ohne Scrollen kopieren können.
2. Das Demo-GIF zeigt die echte Terminalwirkung und verstärkt den Eindruck von Schnelligkeit.
3. Mehrsprachige Links (etwa chinesische oder koreanische Übersetzungen) nahe der Badge-Zeile platzieren.

## 5. Frameworks

Typische Vertreter: Full-Stack-Frameworks wie next.js.

### 5.1 Auswahl der Abschnitte

- Der Startbildschirm betont Positionierung, Größe des Ökosystems und Lerneinstieg.
- Der Einstieg in die „Dokumentation“ muss auffällig sein und verweist üblicherweise auf eine eigenständige Dokumentationsseite.
- „Community“ erläutert Diskussionsbereiche, Instant-Messaging-Kanäle und Verhaltenskodex.
- „Schnellstart“ nennt den minimalen Befehl zur Projekterstellung.
- Tiefgehende Inhalte (Architektur, API) werden extern verlinkt und nicht in der README entfaltet.

### 5.2 Visuelle Schwerpunkte

- Badge-Schwerpunkte: Version, Build-Status, Lizenz, Community-Kanäle.
- Markenlogo kombiniert mit Badges im Stil `for-the-badge` stärkt den Startbildschirm.
- Showcase-Screenshots können Ökosystembeispiele präsentieren.

### 5.3 Ansatzpunkte zur Steigerung der Ästhetik

1. Zentriertes Logo plus große Badges im einheitlichen Stil ergeben einen markenorientierten Startbildschirm.
2. Einstiege zu Dokumentation und Community als auffällige Navigationsblöcke darstellen.
3. Einstiege für Neueinsteigende wie „Good First Issues“ senken die Beitragshürde.

## 6. Ressourcensammlungen

Typische Vertreter: Listen der Awesome-Reihe.

### 6.1 Auswahl der Abschnitte

- Der Startbildschirm beginnt üblicherweise mit Logo und Sponsoreninformationen.
- Der Hauptteil gliedert das Verzeichnis nach Themenkategorien und bietet eine klare Navigation.
- Der „Beitragsleitfaden“ erläutert Aufnahmekriterien und Einreichungsformat.
- Abschnitte zu Installation, API und Bereitstellung sind nicht erforderlich.

### 6.2 Visuelle Schwerpunkte

- Die Anzahl der Badges darf großzügiger sein, muss jedoch stilistisch einheitlich bleiben.
- Verzeichniskategorien als Überschrift der zweiten Ebene mit Liste, Einträge mit kurzer Erläuterung.
- Sponsorenlogos in Tabellen- oder Rasterform anordnen und die Ausrichtung beibehalten.

### 6.3 Ansatzpunkte zur Steigerung der Ästhetik

1. Klare Verzeichnisstruktur mit einheitlicher Hierarchie der Kategorieüberschriften.
2. Jeder Eintrag erhält eine Ein-Satz-Erläuterung; reine Links sind zu vermeiden.
3. Sponsoring- und Danksagungsbereich sauber ausrichten, ohne die Lesbarkeit des Haupttexts zu beeinträchtigen.

## 7. Typübergreifende Grundprinzipien

1. **Leserschaft zuerst**: Der Startbildschirm beantwortet die wichtigsten Fragen der Lesenden; Typunterschiede beeinflussen nur die Reihenfolge, nicht die Vollständigkeit der Informationen.
2. **Einheitlicher Stil**: Badges, Überschriften und Codeblöcke desselben Projekts müssen einheitlich gestaltet sein.
3. **Kopierbare Beispiele**: Jeder Typ bietet mindestens ein direkt ausführbares Beispiel.
4. **Externe Verlinkung**: Tiefgehende Inhalte, die über die Aufgabe des Startbildschirms hinausgehen, werden auf eigenständige Dokumente verlinkt.
5. **Fortlaufende Aktualisierung**: Screenshots, Versions-Badges und Funktionslisten müssen mit der Version aktualisiert werden, damit veraltete Informationen die Glaubwürdigkeit nicht beeinträchtigen.

## Verwandte Dateien

- Allgemeine Abschnittsliste siehe [README-Abschnittsspezifikation](./readme-sections-specification.md)
- Vorgaben zu visuellen Elementen siehe [README-Spezifikation für visuelles Layout](./readme-visual-layout-specification.md)
- Badge-Konfiguration siehe [Badge-Spezifikation](./badge-specification.md)
- Universelle Vorlage siehe [README-Standardvorlage](./readme-standard-template.md)
- Belege zur Typverteilung siehe [README-Vorlagen-Recherchebericht](./readme-template-research-report.md)
