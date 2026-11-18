# Prüfbericht-Format

> Problem, das diese Datei löst: Definiert das einzige Lieferformat für Prüfberichte, die Feldanforderungen und Ausfüllbeispiele, damit der Bericht von einem anderen Agent direkt ausgeführt werden kann.

Der Bericht ist das einzige Lieferergebnis des Prüfschritts. Jeder Befund muss gleichzeitig Beleg, Verantwortlichen und Maßnahme enthalten; nicht ausführbare Schlussfolgerungen dürfen nicht in den Bericht aufgenommen werden.

## 1. Berichtsgerüst

````markdown
# Push-Prüfbericht · {{仓库名}}

Ergebnis: {{结论}}
Modus: {{模式}}
Repository: {{仓库名}} · {{可见性}} · {{许可证}} · Standard-Branch {{默认分支}}

## I. Qualitätstor-Status
| Tor | Status | Offene Punkte |
| --- | --- | --- |
| A Sicherheit | {{门禁状态}} | {{未决项}} |
| B Qualität | {{门禁状态}} | {{未决项}} |
| C Startseite | {{门禁状态}} | {{未决项}} |

## II. Befundliste
| Stufe | Dimension | Befund | Beleg (Pfad:Zeile / Befehlsausgabe) | Verantwortlicher Agent | Maßnahme |
| --- | --- | --- | --- | --- | --- |
| {{等级}} | {{维度}} | {{问题}} | {{证据}} | {{责任agent}} | {{动作}} |

## III. Status der Dokumentationsmatrix
| Datei | Status | Fehlend/zu ändern |
| --- | --- | --- |
| {{文件路径}} | {{状态}} | {{待改项}} |

## IV. Ausführungscheckliste für den Push
- [ ] {{推送规则}}

## V. Freigabeerklärung
{{放行说明}}
````

## 2. Felddefinitionen

| Feld | Pflicht | Typ | Ausfüllhinweis | Beispiel |
| --- | --- | --- | --- | --- |
| Repository-Name | ja | Text | Zeichengleich mit dem GitHub-Repository-Namen | `markdown-lint-cli` |
| Ergebnis | ja | Enumeration | Nur `ALLOW PUSH` oder `BLOCK PUSH`; bei nicht auf null gebrachten P0 muss Letzteres stehen | `BLOCK PUSH` |
| Modus | ja | Enumeration | Bei privaten temporären Skript-Repositories „reduziertes Review“, sonst „vollständiges Review“ | `vollständiges Review` |
| Sichtbarkeit | ja | Enumeration | `private` / `public`; vor der Veröffentlichung ist die Lizenz erneut zu prüfen | `private` |
| Lizenz | ja | SPDX-Kennung | Ohne Lizenz `NONE` schreiben; das Ergebnis muss dann `BLOCK PUSH` lauten | `MIT` |
| Standard-Branch | ja | Text | Tatsächlichen Branch-Namen schreiben, nicht das angenommene `main` | `main` |
| Qualitätstor-Status | ja | Enumeration ×3 | Je eine Zeile für A/B/C; bei `SKIP` ist der Grund unter „Offene Punkte“ anzugeben | `FAIL` |
| Offene Punkte | bedingt Pflicht | Text | Pflicht bei Status `FAIL` oder `SKIP`; Blockade- oder Überspringgrund auflisten | `D1 hat .env erkannt` |
| Stufe | ja | Enumeration | `P0` blockierend / `P1` vor dem Push beheben oder registrieren / `P2` Empfehlung | `P0` |
| Dimension | ja | `D1`–`D14` | Nummerierung siehe [Prüfdimensionsmatrix](./review-dimension-matrix.md) | `D1` |
| Befund | ja | Text | Einen Sachverhalt in einem Satz festhalten, keine Vermutungen oder emotionalen Formulierungen | `Im Wurzelverzeichnis liegt .env` |
| Beleg | ja | Pfad:Zeile oder Befehlsausgabe | Muss nachprüfbar sein; ohne Beleg `SKIP + Grund` schreiben | `.env:3` |
| Verantwortlicher Agent | ja | Agent-Name | Konkrete Ausführungsrolle schreiben, nicht „betroffene Personen“ | `security-auditor` |
| Maßnahme | ja | Text | Direkt ausführbare Operation mit Zieldatei | `.env löschen, Schlüssel rotieren und Historie bereinigen` |
| Dateipfad | ja | Text | Punktweise gemäß der Liste in [Dokumentationsmatrix](./document-matrix.md) aufführen | `SECURITY.md` |
| Status der Dokumentationsmatrix | ja | Tabelle zeilenweise | Je Datei vorhanden, fehlend oder zu ändern kennzeichnen | `SECURITY.md fehlt` |
| Ausführungscheckliste für den Push | ja | Kontrollkästchenliste | Regelweise gemäß [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md) entfalten | `- [ ] Sicherstellen, dass .gitignore wirksam ist` |
| Freigabeerklärung | ja | Text | Bei Blockade Grund und Aufhebungsbedingungen schreiben; bei Freigabe die erfüllten harten Regeln | `Nach Nullen von P0 erneut prüfbar` |

## 3. Ausfüllhinweise

1. **Ergebnis zuerst**: Zuerst die Anzahl der P0 bestimmen, dann das Ergebnis schreiben. Solange ein P0 nicht auf null gebracht ist, darf `ALLOW PUSH` nicht ausgegeben werden.
2. **Beleg verpflichtend**: Jeder Befund benötigt `Pfad:Zeilennummer` oder eine kopierbare Befehlsausgabe. Schlussfolgerungen ohne Beleg werden mit `SKIP` und Grundangabe gekennzeichnet, nicht mit `PASS`.
3. **Verantwortung auf Rollen**: Für den verantwortlichen Agent den Rollennamen aus der [Prüfdimensionsmatrix](./review-dimension-matrix.md) verwenden; ein Befund entspricht einem Verantwortlichen.
4. **Maßnahme ausführbar**: Die Maßnahme muss Zieldatei und Operationstyp benennen; „spätere Behandlung“ und „selbst anpassen“ gelten als ungültig.
5. **Qualitätstor konsistent**: Die drei Zeilen A/B/C müssen der Befundliste entsprechen; ist ein Tor `FAIL`, muss das Ergebnis `BLOCK PUSH` lauten.
6. **Dokumentationsmatrix punktweise**: Dateiweise gemäß Liste aufführen; „Dokumentation im Wesentlichen vollständig“ ist nicht zulässig.
7. **Checkliste entfalten**: Die Ausführungscheckliste für den Push muss die Regeln einzeln entfalten; „gemäß Spezifikation ausführen“ ist kein Ersatz.

Häufige Fehler:

| Fehlerhafte Schreibweise | Problem | Korrektur |
| --- | --- | --- |
| In der Belegspalte „vermutlich problematisch“ schreiben | Kein Pfad, keine Ausgabe, nicht nachprüfbar | `Dateipfad:Zeilennummer` oder Befehlsausgabe ergänzen |
| `ALLOW PUSH` schreiben, obwohl P0 nicht auf null gebracht ist | Verstoß gegen harte Regeln | In `BLOCK PUSH` ändern und Aufhebungsbedingungen auflisten |
| Bei nicht prüfbaren Punkten `PASS` schreiben | Ergebnis erfunden | `SKIP` schreiben und den Grund unter offene Punkte angeben |
| Als Verantwortlichen „betroffene Personen“ schreiben | Kein Verantwortungssubjekt | Konkreten Agent-Namen schreiben |
| Als Maßnahme „spätere Behandlung“ schreiben | Nicht ausführbar | Zieldatei und konkrete Operation angeben |
| Standard-Branch `main` schreiben, ohne ihn zu verifizieren | Weicht von der Realität ab | Ausgabe von `git branch` ist maßgeblich |

## 4. Vollständiges Beispiel

Nachfolgend ein vollständig ausgefülltes Beispiel für `BLOCK PUSH`:

````markdown
# Push-Prüfbericht · markdown-lint-cli

Ergebnis: BLOCK PUSH
Modus: vollständiges Review
Repository: markdown-lint-cli · private · NONE · Standard-Branch main

## I. Qualitätstor-Status
| Tor | Status | Offene Punkte |
| --- | --- | --- |
| A Sicherheit | FAIL | D1 hat .env erkannt, D2 ohne LICENSE |
| B Qualität | SKIP | Abhängigkeiten im Repository nicht installiert, Build und Tests nicht ausführbar |
| C Startseite | FAIL | README ohne Installationsabschnitt und Minimalbeispiel |

## II. Befundliste
| Stufe | Dimension | Befund | Beleg (Pfad:Zeile / Befehlsausgabe) | Verantwortlicher Agent | Maßnahme |
| --- | --- | --- | --- | --- | --- |
| P0 | D1 | Im Wurzelverzeichnis liegt .env | `.env:3` enthält DATABASE_URL | security-auditor | .env löschen, Datenbank-Anmeldedaten rotieren und Historie bereinigen |
| P0 | D2 | Keine Lizenzdatei | `ls LICENSE` gibt `No such file or directory` aus | license-checker | Nach Bestätigung der Lizenz durch den Repository-Eigentümer LICENSE erzeugen |
| P1 | D13 | README ohne Installationsabschnitt | `README.md:1-28` ohne Überschrift „Installation“ | readme-writer | Gemäß README-Standardvorlage Installation und Minimalbeispiel ergänzen |

## III. Status der Dokumentationsmatrix
| Datei | Status | Fehlend/zu ändern |
| --- | --- | --- |
| README.md | zu ändern | Installationsabschnitt und Minimalbeispiel fehlen |
| LICENSE | fehlt | Lizenztyp durch Eigentümer zu bestätigen |
| SECURITY.md | fehlt | Noch nicht erstellt |

## IV. Ausführungscheckliste für den Push
- [ ] Sicherstellen, dass git status sauber ist
- [ ] Vollständigen Schlüssel-Scan ausführen (einschließlich historischer Commits)
- [ ] build, test und lint lokal bestehen
- [ ] Dokumentationsmatrix vollständig

## V. Freigabeerklärung
Blockadegrund: Es bestehen 2 P0 (Anmeldedatenleck, keine Lizenz), und das Qualitätstor ist wegen nicht installierter Abhängigkeiten nicht bewertbar. Aufhebungsbedingungen: Schlüsselrotation und Historienbereinigung abschließen, Lizenz festlegen, Tests in einer baubaren Umgebung erneut ausführen und P0 auf null bringen, danach erneut prüfen.
````

Bei `ALLOW PUSH` kann im fünften Abschnitt stehen: „Alle harten Regeln sind erfüllt, alle drei Qualitätstore sind PASS, der Push kann ausgeführt werden.“ Die übrigen Abschnitte sind nach tatsächlicher Lage auszufüllen; Belege und Checkliste dürfen nicht entfallen.

## 5. Lieferreihenfolge

1. Vollständiger Inhalt der Sprach-Navigation der Root-README.
2. Vollständiger Inhalt der README jedes fertiggestellten Sprachverzeichnisses, mit Sprachcode und Dateipfad einzeln aufgeführt.
3. Inhalt der NOTICE-Datei.
4. Erläuterung des LICENSE-Konzepts (ist keine Lizenz vom Nutzer vorgegeben, nur Kandidaten und Unterschiede nennen, nicht direkt erzeugen).
5. Zusammenfassung der zu bestätigenden Punkte.
6. Prüfbericht (dieser Bericht).
7. Anleitung zum GitHub-Push.

## Verwandte Dateien

- Zur Bewertung des Qualitätstor-Status siehe [Qualitätstor](./quality-gate.md)
- Zur Dimensionsnummerierung der Befundliste siehe [Prüfdimensionsmatrix](./review-dimension-matrix.md)
- Zum Status der Dokumentationsmatrix siehe [Dokumentationsmatrix](./document-matrix.md)
- Die Ausführungscheckliste für den Push stammt aus der [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md)
- Zur Art der Auftragsvergabe siehe [Sub-Agent-Dispatch-Vertrag](./sub-agent-dispatch-contract.md)
