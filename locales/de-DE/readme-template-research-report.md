# README-Vorlagen-Recherchebericht

> Problem, das diese Datei löst: Sie dokumentiert Erhebungsmethodik, Stichprobenumfang und quantitative Befunde der vorliegenden Untersuchung zur Standard-README-Vorlage, liefert die Datengrundlage für die [README-Standardvorlage](./readme-standard-template.md) und die einzelnen Fachspezifikationen und benennt ausdrücklich die Grenzen und Einschränkungen der Methodik.

## 1. Untersuchungsziel und Methodik

### 1.1 Ziel

Untersucht werden führende Open-Source-Projekte mit hoher Sternenzahl, um Struktur, Abschnittsgliederung, visuelle Darstellung und Badge-Nutzung ihrer READMEs und zugehörigen Dokumentation zu verallgemeinern und daraus wiederverwendbare allgemeine Spezifikationen und Vorlagen zu gewinnen.

### 1.2 Datenquellen

- Repository-Metadaten: GitHub GraphQL Search API, absteigend nach Sternen, gefiltert mit `is:public archived:false fork:false`.
- README-Rohtexte: GitHub REST Contents API (Endpunkt `readme`), bezogen als base64 oder raw und anschließend ausgewertet.
- Badge-Parameter: offizielle Shields.io-Dokumentation (Static Badge, Seite Logos) sowie die Formatspezifikation von badge-maker.
- Praxis der chinesischen Community: Projektdokumentation, Commit-Nachrichten und Abschnitte zur Verbreitung von phodal/github („GitHub-Rundgang-Leitfaden“, 11.362 Sterne), zur Ergänzung von Schreibprinzipien und Betriebserfahrungen, die maschinelle Statistiken nicht abdecken.

### 1.3 Erhebungsmethodik

1. **Metadaten**: Eine einzelne Abfrage der GitHub Search API liefert höchstens 1000 Einträge. Zur Erweiterung der Stichprobe wurden Sternintervalle gestückelt – der Sternschwellenwert für jeweils 1000 Einträge wurde per Binärsuche bestimmt und über 11 Stapel schrittweise nach unten verschoben; insgesamt wurden Metadaten von 10.995 führenden Repositories gewonnen.
2. **README-Stichprobe**: Innerhalb der führenden 1000 Repositories wurde geschichtet nach Hauptsprache gezogen; abgedeckt wurden führende Sprachen wie Python, TypeScript, JavaScript, Rust, Go und C++, insgesamt 120 Repositories; für alle konnte der README-Rohtext erfolgreich abgerufen werden.
3. **Zählweise**: Die Abschnitts- und Elementhäufigkeiten wurden je Repository gezählt; Badge-Stile und logo-Parameter wurden nach ihrem Vorkommen in den URLs gezählt.

### 1.4 Grenzen der Methodik (verbindlich anzugeben)

- Die GitHub Search API begrenzt eine einzelne Abfrage auf 1000 Einträge. Der vorliegende Bericht erweitert den Umfang durch gestückelte Kumulation, doch die Stückgrenzen werden durch Gleichstand bei den Sternen beeinflusst; die Stichprobe ist eine angenäherte Menge führender Projekte und keine streng fortlaufende Rangliste.
- Der Stichprobenumfang der READMEs beträgt 120; die Ergebnisse zeigen Trends und Gemeinsamkeiten, nicht eine statistisch signifikante Verteilung aller führenden Projekte.
- Die Abschnittserkennung beruht auf dem Abgleich von Überschriften-Schlüsselwörtern; abweichende Formulierungen führen zu statistischen Verzerrungen.
- Die Badge-Parameterstatistik erfasst nur explizit in URLs auftretende Parameter; Standardparameter dynamischer Badges wurden nicht gezählt.

## 2. Verteilung der führenden Repositories (Metadaten)

### 2.1 Stichprobenumfang

- Eine einzelne Abfrage liefert stabil die führenden 1000 Repositories mit einem Sternbereich von etwa 563.574 bis 30.857.
- Durch Kumulation über 11 Stapel wurde auf 10.995 führende Repositories erweitert, mit einer unteren Sterngrenze von 5.452.

### 2.2 Sprachverteilung (bezogen auf die führenden 1000)

| Sprache | Anzahl | Anteil |
| --- | --- | --- |
| Python | 223 | 22,3 % |
| TypeScript | 178 | 17,8 % |
| JavaScript | 112 | 11,2 % |
| Rust | 80 | 8,0 % |
| Keine Hauptsprache | 74 | 7,4 % |
| Go | 68 | 6,8 % |
| C++ | 55 | 5,5 % |
| Java | 27 | 2,7 % |

Die führenden Projekte werden von Python, TypeScript und JavaScript dominiert; diese drei zusammen überschreiten 50 %; Systemsprachen wie Rust und Go haben einen merklichen Anteil. Daraus folgt, dass die Vorlage Installationsbefehle für Paketverwaltungen mehrerer Sprachen und Badges für mehrere Laufzeiten abdecken muss.

### 2.3 Lizenzverteilung (bezogen auf die führenden 1000)

| Lizenz | Anzahl | Anteil |
| --- | --- | --- |
| MIT | 399 | 39,9 % |
| Apache-2.0 | 197 | 19,7 % |
| Nicht erkannt (NOASSERTION) | 148 | 14,8 % |
| Keine Lizenz (NONE) | 65 | 6,5 % |
| GPL-3.0 | 51 | 5,1 % |
| AGPL-3.0 | 50 | 5,0 % |
| BSD-3-Clause | 17 | 1,7 % |

MIT dominiert und ist die Standardempfehlung der universellen Vorlage; zugleich müssen SPDX-Platzhalter für Optionen wie Apache-2.0 und GPL erhalten bleiben.

## 3. Befunde zur README-Struktur (N=120)

### 3.1 Häufigkeit der Abschnitte

| Abschnittsschlüsselwort | Anzahl der Repositories | Häufigkeit |
| --- | --- | --- |
| Contributing / Beitrag | 66 | 55,0 % |
| License / Lizenz | 52 | 43,3 % |
| Install / Installation | 49 | 40,8 % |
| Quick Start / Schnellstart | 28 | 23,3 % |
| Documentation / Dokumentation | 25 | 20,8 % |
| Development / Entwicklung | 22 | 18,3 % |
| Configuration / Konfiguration | 19 | 15,8 % |
| Features / Funktionen | 19 | 15,8 % |
| Security / Sicherheit | 15 | 12,5 % |
| Usage / Nutzung | 12 | 10,0 % |
| Requirements / Abhängige Umgebung | 11 | 9,2 % |
| API | 10 | 8,3 % |
| Examples / Beispiele | 10 | 8,3 % |

Befund: Beitragsleitfaden und Lizenz sind bei führenden Projekten Standard und spiegeln die Priorität von Community-Governance und Konformität wider; Installation und Schnellstart folgen unmittelbar danach. Die Vorlage führt beide daher als Pflichtangaben.

### 3.2 Nutzungsrate visueller Elemente

| Element | Anzahl der Repositories | Häufigkeit | Median (je Repository) |
| --- | --- | --- | --- |
| Codeblöcke | 80 | 66,7 % | 2 |
| Bilder | 76 | 63,3 % | 2 |
| Badges (Shields.io) | 61 | 50,8 % | 1 |
| Tabellen | 44 | 36,7 % | 0 |

Median der Überschriftenhierarchie: 7 Überschriften der zweiten Ebene; Median der Dateilänge: 171 Zeilen. Dies zeigt, dass führende READMEs durchgängig eine mittlere Länge beibehalten und mit 6–12 Überschriften der zweiten Ebene gegliedert sind.

### 3.3 Anpassung an Farbschemata (erste 40 Stichproben)

| Merkmal | Anzahl der Repositories |
| --- | --- |
| Zentrierter Container (`align="center"`) | 27 |
| `<picture>`-Element | 12 |
| Umschaltung helles und dunkles Schema (`prefers-color-scheme`) | 12 |
| `for-the-badge` kombiniert mit `labelColor` | 2 |

Der zentrierte Container ist die vorherrschende Methode für Startbildschirme; etwa ein Drittel der Projekte bietet Bilder in heller und dunkler Variante.

## 4. Befunde zu Badges

### 4.1 Stilparameter (nach Vorkommen in URLs, N=120)

| style | Anzahl |
| --- | --- |
| `for-the-badge` | 65 |
| `flat-square` | 60 |
| `flat` | 32 |
| `social` | 12 |
| `plastic` | 1 |

`for-the-badge` und `flat-square` sind am verbreitetsten; `plastic` ist weitgehend außer Gebrauch. Details siehe [Badge-Spezifikation](./badge-specification.md).

### 4.2 logo-Parameter (nach Vorkommen, N=120)

| logo-Slug | Anzahl |
| --- | --- |
| `github` | 35 |
| `discord` | 20 |
| `npm` | 4 |
| `apple` / `docker` / `linkedin` / `x` | je 2–3 |

GitHub und Discord sind die häufigsten Symbole und entsprechen den beiden Informationskategorien „Quellcode-Repository“ und „Community-Kanal“.

## 5. Belege zu Startbildschirmen von Referenzprojekten

| Projekt | Typ | Merkmale der Startseite |
| --- | --- | --- |
| `sindresorhus/awesome` | Ressourcensammlung | Zentriertes Logo, Sponsoringbereich, thematisch gegliedertes Verzeichnis |
| `axios/axios` | Bibliothek | Wichtiger Hinweis, Sponsoring-Tabelle, Mehrsprachigkeit |
| `sharkdp/fd` | CLI | Badges + mehrsprachige Links, Abschnittsnavigation, Demo-Animation |
| `BurntSushi/ripgrep` | CLI | Badges, Schnelllinks, Suchscreenshot, Leistungsvergleich |
| `vercel/next.js` | Framework | Zentriertes Logo, `for-the-badge`-Badges, Einstiege zu Dokumentation und Community |
| `microsoft/vscode` | Anwendung | Badges, Repository-Erläuterung, Produktscreenshot, Einstiege zu Beiträgen und Feedback |
| `rust-lang/rust` | Sprache | Zentriertes Banner, Navigationszeile, Wertpunkte „Why Rust“ |
| `phodal/github` | Chinesisches E-Book | Vier Fragen des Startbildschirms, Beispiele für Ein-Satz-Texte, Prinzip der Installationsvereinfachung, Liste der Verbreitungskanäle |

Gemeinsamkeiten: Der Startbildschirm beantwortet „Was ist es, wie wird es verwendet, wo stehen Details“; Badges stehen direkt bei der Überschrift; Screenshot oder Demo folgen unmittelbar der Positionierung; Einstiege zu Beiträgen und Community stehen weiter unten, sind aber Pflicht.

## 6. Zusammenfassende Schlussfolgerungen

1. Die universelle Vorlage muss als Hauptstrang „Positionierung → Installation → Schnellstart → Dokumentation → Beitragen → Lizenz“ verwenden.
2. Badges standardmäßig im Stil `flat-square` oder `for-the-badge`, im gesamten Dokument einheitlich, in einer Anzahl von 4–6.
3. Bilder und Codeblöcke sind der Kern eines attraktiven Startbildschirms; sie müssen mit `alt`-Texten und Sprachkennungen versehen werden.
4. Der Projekttyp bestimmt die Auswahl der Abschnitte, siehe [README-Leitfaden zur Kategorieanpassung](./readme-category-adaptation-guide.md).
5. Konformität und Community-Governance (Lizenz, Beitragsleitfaden) sind bei führenden Projekten Konsens und werden als Pflichtangaben geführt.

## 7. Hinweise zum Datenumfang

Kumuliertes Ergebnis der Metadaten-Stückelung führender Repositories: 10.995 Repositories, Sternbereich von 563.575 bis 5.452. Die Lizenz- und Sprachverteilung dieser Stichprobe im Zehntausenderbereich entspricht den Schlussfolgerungen der Stichprobe der führenden 1000:

| Dimension | Verteilung |
| --- | --- |
| Sprache | Python 1.995, TypeScript 1.529, JavaScript 1.279, keine Hauptsprache 888, Go 847, C++ 531, Java 528, Rust 507 |
| Lizenz | MIT 4.160 (37,8 %), Apache-2.0 2.073 (18,9 %), nicht erkannt 1.463, keine Lizenz 1.106, GPL-3.0 747 |

Die Tiefenstatistik der READMEs umfasst 120 Stichproben; alle Abrufe waren erfolgreich. Die Stückelung verwendet angenäherte Sternschwellenwerte; der Umfang entspricht einer angenäherten Menge führender Projekte und keiner streng fortlaufenden Rangliste.

## Verwandte Dateien

- Direkt übernehmbare Vorlage siehe [README-Standardvorlage](./readme-standard-template.md)
- Badge-Spezifikation siehe [Badge-Spezifikation](./badge-specification.md)
- Visuelle Vorgaben siehe [README-Spezifikation für visuelles Layout](./readme-visual-layout-specification.md)
- Kategorieanpassung siehe [README-Leitfaden zur Kategorieanpassung](./readme-category-adaptation-guide.md)
- Abschnittsdefinitionen siehe [README-Abschnittsspezifikation](./readme-sections-specification.md)
