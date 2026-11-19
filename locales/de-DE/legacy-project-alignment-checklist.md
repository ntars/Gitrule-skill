# Checkliste zur Angleichung bestehender Projekte

> Problem, das diese Datei löst: Wenn diese Spezifikationssammlung auf ein bestehendes Projekt angewendet wird, liefert sie eine Punkt für Punkt prüfbare Checkliste, Beurteilungsmethoden und Bestehenskriterien für sechs Bereiche: Metadaten, Dateibenennung, Abschnittsstruktur, Zweisprachigkeitssynchronisation, Links und Push.

## 1. Anwendungsbereich

Diese Checkliste dient zwei Szenarien:

1. ein vorhandenes Repository erstmals in die Verwaltung durch diese Spezifikationssammlung überführen;
2. nach einer Aktualisierung der Spezifikationssammlung eine Regressionsprüfung bereits angeglichener Repositorys durchführen.

Die Checkliste wird in der Reihenfolge „zuerst Metadaten, dann Struktur, zuletzt Push“ ausgeführt. Solange eine Gruppe nicht bestanden ist, wird die nächste nicht begonnen, um massenhafte Umschreibungen auf fehlerhafter Grundlage zu vermeiden.

## 2. Prüfpunkte

### 2.1 Metadaten (entsprechend [Projektbenennungs-Spezifikation](./project-naming-specification.md) Abschnitt 5)

| Nummer | Prüfpunkt | Beurteilungsmethode | Bestehenskriterium |
| --- | --- | --- | --- |
| A1 | Repository-Name regelkonform | Abgleich mit Benennungsformel und Zeichensatzregeln | Durchgehend klein geschrieben, kebab-case, 2–25 Zeichen, ohne Versionsnummer und Füllwörter |
| A2 | Beschreibung im zweisprachig zusammengeführten Format | Bereich „About“ des Repositorys lesen oder `gh repo view --json description` | `Landessprache \| Englisch`, je ein Leerzeichen beiderseits des senkrechten Strichs |
| A3 | Länge der Beschreibung | Zeichen zählen, chinesisch und englisch getrennt | Je höchstens 120 Zeichen, zusammen höchstens 350 Zeichen |
| A4 | Anzahl und Sprache der Topics | `gh repo view --json repositoryTopics` | Genau 20, ausschließlich Englisch, ausschließlich klein geschrieben, Wörter mit Bindestrichen getrennt |
| A5 | Abdeckung der Topics | Prüfung nach den fünf Kategorien Sprache, Domäne, Form, Ökosystem, Szenario | Alle fünf Kategorien abgedeckt, keine Topics im Widerspruch zum Technologie-Stack |

Vorgehen bei Überschreitung: zuerst die englische Fassung kürzen, dann die chinesische; beim Kürzen zunächst Schmückwörter und doppelte Einschränkungen entfernen, dann gleichbedeutende Formulierungen zusammenführen.

### 2.2 Dateibenennung (entsprechend [Mehrsprachigkeits-Spezifikation](./multilingual-specification.md))

| Nummer | Prüfpunkt | Beurteilungsmethode | Bestehenskriterium |
| --- | --- | --- | --- |
| B1 | Benennung der Haupt-README | Verzeichnis auflisten | Chinesisch `README.md`, Englisch `README_EN.md` |
| B2 | Benennung weiterer Sprachen | Verzeichnis auflisten | `README_<Sprachcode in Großbuchstaben>.md`, etwa `README_JA.md` |
| B3 | Einheitlichkeit der Benennung | Repository-weit nach alten Namen suchen | Keine Reste alter Benennungen wie `README.en.md`, `README.ja.md` |
| B4 | Synchronisation der Verweise | Nach alten Dateinamen suchen | Navigationslinks, Verzeichnisbaum-Beispiele und Whitelists in Skripten sind aktualisiert |
| B5 | Sprachwechsel-Links | Erste Zeile jeder Sprachfassung öffnen | Jede Sprachfassung kann in der ersten Zeile auf alle übrigen Sprachen wechseln |

Dateiumbenennungen müssen mit `git mv` erfolgen, um die Dateihistorie zu erhalten. Skripte im Repository (Vorabprüfung, Paketierung, Dokumentationsvalidierung) verwenden häufig Dateinamen als Whitelist; sie sind synchron anzupassen, andernfalls schlägt die Validierung nach dem Push fehl.

### 2.3 Abschnittsstruktur (entsprechend [README-Abschnitts-Spezifikation](./readme-sections-specification.md))

| Nummer | Prüfpunkt | Beurteilungsmethode | Bestehenskriterium |
| --- | --- | --- | --- |
| C1 | Abschnitte vollständig | Überschriften der zweiten Ebene extrahieren und mit der Liste der 20 Kapitel abgleichen | Alle 20 Kapitel vorhanden, keines fehlt |
| C2 | Benennung der Abschnitte | Überschriftentexte einzeln abgleichen | Identisch mit der Terminologie der Spezifikation; Varianten wie „Kernhighlights“ oder „Designdetails und kleine Kniffe“ sind unzulässig |
| C3 | Reihenfolge der Abschnitte | In Reihenfolge des Auftretens abgleichen | Identisch mit der Reihenfolge der Spezifikation |
| C4 | Zusätzliche Abschnitte | Prüfen, ob weitere Abschnitte existieren | Zusätzliche Inhalte als „Anhang“ nach den 20 Kapiteln, nicht in die Reihenfolge des Haupttextes eingefügt |
| C5 | Entsprechung der Sprachfassungen | Anzahl und Reihenfolge der Überschriften zweiter Ebene in beiden Sprachen abgleichen | Beide Sprachen entsprechen einander Punkt für Punkt |

Erscheinen im Haupttext Abschnittsnamen, die von der Spezifikation abweichen, ist die Terminologie der Spezifikation maßgeblich und zu vereinheitlichen; enthält ein Abschnitt umfangreiche vorhandene Inhalte, ist die Umbenennung gegenüber einer Neufassung des Textes zu bevorzugen.

### 2.4 Zweisprachigkeitssynchronisation (entsprechend [Mehrsprachigkeits-Spezifikation](./multilingual-specification.md))

| Nummer | Prüfpunkt | Beurteilungsmethode | Bestehenskriterium |
| --- | --- | --- | --- |
| D1 | Einheitliche Versionsnummer | Nach Versionszeichenketten suchen | Beide Sprachen nennen dieselbe Versionsnummer und denselben Status |
| D2 | Einheitliche Zahlen | Funktionsanzahl, Testanzahl, Plattformanzahl abgleichen | Derselbe Kennwert hat in beiden Fassungen denselben Wert |
| D3 | Einheitliche Links | Mengen relativer Links abgleichen | Beide Fassungen verweisen auf dieselben Dateien |
| D4 | Einheitliche Terminologie | Fachbegriffe stichprobenartig prüfen | Derselbe Begriff wird in beiden Fassungen mit derselben Übersetzung wiedergegeben |
| D5 | Einheitliche Struktur | Anzahl der Tabellen und Listen abgleichen | Tabellen und Listen je Abschnitt in gleicher Anzahl |

Wird in einer Fassung ein faktischer Inhalt geändert, ist die andere Fassung im selben Commit zu aktualisieren; eine Nachübersetzung in einem späteren Commit ist unzulässig.

### 2.5 Links und Inhalte (entsprechend [Allgemeine Schreib-Spezifikation](./general-writing-specification.md))

| Nummer | Prüfpunkt | Beurteilungsmethode | Bestehenskriterium |
| --- | --- | --- | --- |
| E1 | Relative Links erreichbar | Jeden Link auflösen und Dateiexistenz prüfen | Anzahl toter Links gleich 0 |
| E2 | Sprachkennung der Codeblöcke | Nach Code-Fences suchen | Alle mit Sprache gekennzeichnet, keine nackten Fences |
| E3 | Spaltenzahl der Tabellen | Trennzeile und Datenzeilen jeder Tabelle prüfen | Spaltenzahlen stimmen überein |
| E4 | Unzulässige Ausdrucksweisen | Nach umgangssprachlichen Wörtern, Ausrufezeichen, Auslassungspunkten, Emojis suchen | Keine Treffer; bei Zitaten sind diese in Anführungszeichen zu setzen und mit Quelle zu versehen |
| E5 | Unbelegte Daten | Nach Leistungszahlen suchen | Jede Zahl hat Testumgebung und Testmethode |
| E6 | Zusichernde Formulierungen | Nach Wörtern wie „garantiert“, „dauerhaft“, „vollständig“ suchen | Technische Einschränkungen dürfen bleiben; Zusicherungen nach außen sind zu entfernen |

### 2.6 Community-Dateien und Push (entsprechend [Dokumentationsmatrix](./document-matrix.md), [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md))

| Nummer | Prüfpunkt | Beurteilungsmethode | Bestehenskriterium |
| --- | --- | --- | --- |
| F1 | Pflichtdateien vollständig | Verzeichnis auflisten | `LICENSE`, `NOTICE`, `CONTRIBUTING.md`, `SECURITY.md` vorhanden |
| F2 | Lizenz und NOTICE konsistent | Geschichtete Routing-Tabelle abgleichen | Lizenz auf Verzeichnisebene und NOTICE-Erklärung stimmen überein |
| F3 | Ignorierregeln | `.gitignore` prüfen | Build-Artefakte, Abhängigkeitsverzeichnisse, `.DS_Store`, `.workbuddy/` sind ignoriert |
| F4 | Commit-Nachrichten | `git log` prüfen | Entsprechen `<type>(<scope>): <subject>` |
| F5 | Remote konsistent | Lokales `HEAD` mit `origin/main` abgleichen | Beide identisch, Arbeitsbereich sauber |

## 3. Zusätzliche Prüfungen für mehrsprachige Repositorys

Existieren mehr als drei Sprachfassungen, sind über die obigen Prüfungen hinaus drei weitere Punkte zu ergänzen:

1. **Abschnittsüberschriften je Sprache prüfen**: Die Überschriften der 20 Kapitel müssen in jeder Sprache in ihrer Bedeutung mit der chinesischen oder englischen Referenz übereinstimmen; ein fehlendes Kapitel in einer Sprache ist unzulässig;
2. **Einheitliche Zeilenzahl der Tabellen**: Projektlisten, Statustabellen und Parametertabellen haben in allen Sprachfassungen dieselbe Zeilenzahl;
3. **Synchronisation des Glossars**: Die Terminologie-Übersichtstabelle liegt in einer von beiden Sprachen gemeinsam genutzten eigenständigen Datei, auf die alle Sprachfassungen verweisen.

## 4. Häufige Fehler und Behandlung

| Fehler | Symptom | Behandlung |
| --- | --- | --- |
| Fehlbeurteilung chinesischer Zahlzeichen beim massenhaften Ändern von Kapitelnummern | „十、“ wird als „二十、“ erkannt, Kapitel 10 wird mit der Überschrift von Kapitel 20 überschrieben | Auf explizite Eins-zu-eins-Ersetzung „alte Zeichenkette → neue Zeichenkette“ umstellen und jeden Treffer vor dem Schreiben prüfen |
| Nur Linkpfad geändert, Anzeigetext nicht | Link ist anklickbar, im Text steht jedoch noch der alte Abschnittsname | Volltext nach alten Abschnittsnamen durchsuchen, Pfad und Anzeigetext gemeinsam aktualisieren |
| Datei umbenannt, Skripte nicht angepasst | Lokale Dokumentation in Ordnung, Validierungsskript schlägt nach dem Push fehl | Alle Dateinamen-Zeichenketten im Repository durchsuchen, einschließlich Skripte, Konfigurationen und Dokumentationsbeispiele |
| Zweisprachig nur eine Seite geändert | Fakten beider Fassungen weichen voneinander ab | Maßgeblich ist der tatsächliche Stand des Repositorys; zuerst die Hauptfassung ändern, dann im selben Commit die andere Fassung |
| Indexseite nicht aktualisiert | Neue Datei fehlt im Index und gilt als verwaist | Nach dem Hinzufügen einer Datei sofort Zählung und Eintrag im Index aktualisieren und die Summe der Bereichszählungen gegenprüfen |
| Repository-Beschreibung und Haupttext weichen voneinander ab | Im Bereich „About“ stehen sieben Projekte, im Haupttext neun | Beschreibung anhand der Liste im Haupttext aktualisieren und dies in der Commit-Nachricht vermerken |

## 5. Vorlage für das Abnahmeprotokoll

```text
仓库：{{仓库名}}
检查日期：{{日期}}
规范版本：{{版本或提交号}}

元数据：A1 {{通过/不通过}} A2 {{通过/不通过}} A3 {{通过/不通过}} A4 {{通过/不通过}} A5 {{通过/不通过}}
文件命名：B1 {{ }} B2 {{ }} B3 {{ }} B4 {{ }} B5 {{ }}
章节结构：C1 {{ }} C2 {{ }} C3 {{ }} C4 {{ }} C5 {{ }}
双语同步：D1 {{ }} D2 {{ }} D3 {{ }} D4 {{ }} D5 {{ }}
链接与内容：E1 {{ }} E2 {{ }} E3 {{ }} E4 {{ }} E5 {{ }} E6 {{ }}
社区与推送：F1 {{ }} F2 {{ }} F3 {{ }} F4 {{ }} F5 {{ }}

未通过项与处置：{{逐条列出}}
放行结论：{{通过 / 有条件通过 / 阻断}}
```

## 6. Felddefinitionen

| Feld | Bedeutung | Werte |
| --- | --- | --- |
| Repository-Name | Vollständiger Name des geprüften Repositorys | `Besitzer/Repository` |
| Spezifikationsversion | Stand der Spezifikationssammlung, auf dem diese Prüfung beruht | Commit-Nummer oder Versionsnummer |
| Bestanden | Der Punkt erfüllt das Bestehenskriterium | Boolesch |
| Freigabeergebnis | Behandlung des Prüfergebnisses | Bestanden / Bedingt bestanden / Blockiert |

## Verwandte Dateien

- Repository-Benennung und Metadaten siehe [Projektbenennungs-Spezifikation](./project-naming-specification.md)
- Kapitelliste siehe [README-Abschnitts-Spezifikation](./readme-sections-specification.md)
- Zweisprachigkeitsregeln siehe [Mehrsprachigkeits-Spezifikation](./multilingual-specification.md)
- Schreibweise und unzulässige Ausdrucksweisen siehe [Allgemeine Schreib-Spezifikation](./general-writing-specification.md)
- Push-Vorgänge siehe [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md)
