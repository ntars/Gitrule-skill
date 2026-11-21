# Entwicklungshandbuch-Vorlagenspezifikation

> Problem, das diese Datei löst: Sie definiert das Skelett des zweiphasigen Entwicklungshandbuchs „in der Cloud verfassen, lokal ausführen“, das Format der Aufgabenkarten, das Übergabeprotokoll und die Abnahmeschranken, damit dieselbe Idee von einem Cloud-Modell in eindeutige Aufgabenkarten übertragen und von einem lokalen Codierungsmodell abschnittsweise nacheinander ausgeführt werden kann.

## 1. Positionierung und Verwendungsablauf

1. Diese Spezifikation richtet sich an das Szenario der Arbeitsteilung „ein Cloud-Inferenzmodell + ein lokales Codierungsmodell“: Die Cloud ist dafür zuständig, vage Ideen in klare Entwürfe zu übertragen, die lokale Seite führt den Entwurf deterministisch aus.
2. Der Verwendungsablauf ist fest auf vier Schritte eingestellt, die Reihenfolge darf nicht übersprungen werden:
   - Vorabprüfung: Prüfen, ob die Idee fehlerhafte Prämissen, logische Sprünge oder fehlende Informationen enthält; bei unzureichenden Informationen zuerst beim Benutzer nachfragen, Spekulationen sind verboten.
   - Verfassen in der Cloud: Gemäß der Spezifikation in Abschnitt 9 Open-Source-Lösungen sichten und das Handbuch ausfüllen.
   - Prüfung durch den Benutzer: Im Mittelpunkt stehen die Abnahmebefehle, die Übernahmeaufzeichnungen und die Verbotsbereiche.
   - Lokale Ausführung: Entsprechende Kapitel und Übergabeaufzeichnungen gemäß dem maschinenlesbaren Index injizieren und abschnittsweise ausführen.
3. Im Handbuchtext sind vage Wörter wie „usw.“, „im Zusammenhang mit“, „angemessen“, „möglichst“, „wenn nötig“ verboten; jede Stelle muss entweder einen exakten Wert oder eine Entscheidungsregel angeben.

## 2. Skelett des Handbuchs

Jedes Entwicklungshandbuch enthält fest die folgenden Teile, die Reihenfolge bleibt unverändert:

| Teil | Zuständigkeit |
| --- | --- |
| Maschinenlesbarer Index | Navigationstabelle aus Kapitelpfaden, zugehörigen Code-Verzeichnissen, Abnahmebefehlen und Phasenkennzeichnungen |
| Übernahmeaufzeichnung | Record-Tabelle der Open-Source-Lieferkette, einzige Quelle der Wahrheit des gesamten Projekts (siehe Abschnitt 11) |
| Projektverfassung | Invarianten des gesamten Projekts, in jeden Teil zu injizieren |
| Glossar | Gegenüberstellung von Fachbegriffen und verständlichen Erklärungen sowie des zugehörigen Codes |
| Modul-Kapitel | Ein Kapitel pro Modul, verfasst nach der Struktur aus Abschnitt 4 |
| Release-Kapitel | Build- und Distributionsspezifikation; Veröffentlichungsaktionen erfordern die Bestätigung des Benutzers |
| Website-Texte-Kapitel | Textspezifikation für normale Benutzer; wird nicht in das lokale Modell injiziert |
| Änderungsprotokoll | Datum, Kapitel, Änderung und Entscheidungsträger |

## 3. Projektverfassung

Die Projektverfassung umfasst die in jeden lokalen Ausführungsteil zu injizierenden Invarianten und enthält fest fünf Punkte:

1. Technologie-Stack und Versionen: exakt bis zur Versionsnummer.
2. Konvention zur Verzeichnisstruktur: Baumdiagramm plus eine Ein-Satz-Zuständigkeit je Verzeichnis.
3. Codierkonventionen: je nach Projekttyp zugeschnitten; die Baseline umfasst modulares bedarfsgesteuertes Laden, minimalen und unmittelbarsten Code, keine nicht angeforderten Funktionen sowie vollständige Kommentare, wobei Fachkonzepte in verständlicher Sprache kommentiert werden; Oberflächenprojekte folgen dem Apple HIG, Schriftgrößen verwenden ausnahmslos px oder rem, rpx ist verboten.
4. Globale Verbotsbereiche: absolut Unzulässiges, z. B. keine Abhängigkeiten einführen, die nicht in der Übernahmeaufzeichnung stehen, keine Vertragsdateien ändern.
5. Ausgabesprachen-Spezifikation: Erläuterungen, Protokolle, Fortschritt und Fehlermeldungen verwenden vereinfachtes Chinesisch; Code, Befehle, Dateipfade und Eigennamen dürfen im Original bleiben.

## 4. Struktur der Modul-Kapitel

Jedes Modul-Kapitel enthält fest neun Abschnitte, die Reihenfolge bleibt unverändert:

| Abschnitt | Zuständigkeit |
| --- | --- |
| Zuständigkeit des Moduls | 1–3 Sätze, klar formuliert, was geleistet und was nicht geleistet wird |
| Genutzte Open-Source-Lösungen | Name, Zweck, Nummer in der Übernahmeaufzeichnung |
| Dateiliste | Pfade, Aktionen (neu anlegen/ändern/nur lesen), Zuständigkeit; insgesamt nicht mehr als 10, bei Überschreitung Kapitel teilen |
| Schnittstellenverträge | Signaturen, Routen, Protokollfelder exakt bis zum Typ, mit vollständigen Ein- und Ausgabebeispielen |
| Daten und Zustand | Was gespeichert wird, wo, in welchem Format; Fachkonzepte werden in verständlicher Sprache kommentiert |
| Abhängigkeitsbeziehungen | Drei Dateilisten: zuerst zu lesen, wird aufgerufen, niemals zu ändern |
| Aufgabenkarte | Die aus diesem Modul geteilten Teile, jede Karte wird unabhängig ausgeführt |
| Verbotsbereich dieses Kapitels | Was in diesem Modul besonders nicht erlaubt ist |
| Entwurfsanmerkungen | Auswahlgründe, verworfene Entwürfe, Unterscheidung von Fakten und Vermutungen; wird nicht in das lokale Modell injiziert |

## 5. Format der Aufgabenkarte

Eine Aufgabenkarte entspricht einer lokalen Sitzung entspricht einem Abnahmebefehl; die Pflichtfelder lauten:

| Feld | Anforderung |
| --- | --- |
| Ziel | Ein Satz, maschinenverifizierbar |
| Voraussetzungen | Der abhängige vorherige Teil und die Dateien existieren bereits |
| Schritte | Nummeriert aufgeführt, jeder Schritt eine deterministische Aktion, in einem Zug erledigt, ohne Unterbrechung und ohne Rückfragen |
| Abnahmebefehl | Direkt kopier- und ausführbar; wenn noch kein Abnahmesystem existiert, muss die erste Karte zuerst den Abnahmebefehl aufbauen |
| Erwartetes Ergebnis | Exakte Ausgabe, Exit-Code oder Anzahl der Assertions |
| Fehlerbehandlung | Je typischem Fehler die Maßnahme einzeln angeben; bei drei aufeinanderfolgenden Fehlern anhalten und in die Übergabeaufzeichnung schreiben |
| Übergabeanforderungen | Die Felder deklarieren, die in die Übergabeaufzeichnung zu schreiben sind |

Harte Vorgaben:

1. Berührt eine Karte mehr als 10 Dateien, ist die Karte zu teilen; umfasst ein Kapitel mehr als 6 Karten, ist das Kapitel zu teilen.
2. Karten, die eine Liefer-Selbstprüfung betreffen, müssen die Bereinigung redundanter Codes sowie die Synchronisationspunkte mit README, NOTICE und LICENSE explizit auflisten.
3. Aktionen, die Dateien löschen oder überschreiben, sind ausnahmslos anzuhalten, im block-Feld der Übergabeaufzeichnung zu vermerken und auf die Bestätigung des Benutzers zu warten.
4. Aufgaben, die zu vage sind, um einen Abnahmebefehl zu formulieren, dürfen nicht in eine Karte eingetragen werden und sind gesondert mit „Benutzerentscheidung erforderlich“ zu kennzeichnen.

## 6. PROGRESS-Übergabeprotokoll

Die Übergabeaufzeichnungsdatei PROGRESS.md ist die einzige Quelle der Wahrheit zwischen den Teilen; das Format ist fest:

| Feld | Anforderung |
| --- | --- |
| done | Ob das Ziel dieser Karte erreicht wurde |
| files | Liste der tatsächlich geänderten Dateien |
| decisions | Entscheidungen im Verlauf, im Format „A gewählt, weil B“ |
| next | Nummer und Einstieg der nächsten Karte; Dateipfad und Einstiegsfunktion müssen angegeben werden, „weiter ausbauen“ ist nicht zulässig |
| block | Ungelöste Probleme, sonst leer lassen |

1. Am Ende jeder Karte ist ein Eintrag anzuhängen; das Format darf nicht geändert werden.
2. Bei der lokalen Ausführung wird nur der neueste Eintrag injiziert; historische Einträge werden nicht injiziert.
3. Wiederaufsetzen an der Unterbrechungsstelle: Beim Empfang der Anweisung „weiter“ zuerst den neuesten Eintrag lesen, um die Unterbrechungsstelle zu bestätigen, und am von next angegebenen Einstieg fortfahren; das Wiederholen bereits abgeschlossener Schritte aus Gedächtnis oder Vermutung ist verboten.

## 7. Lokales Injektionsbudget

Das harness setzt den Kontext jedes Teils gemäß der folgenden Tabelle zusammen; das Gesamtbudget übersteigt nicht 24K (75 % des 32K-Arbeitsfensters):

| Injizierter Posten | Budget |
| --- | --- |
| Projektverfassung | 2–3K |
| Kapitel der aktuellen Aufgabenkarte | 2–5K |
| Neuester Eintrag der Übergabeaufzeichnung | rund 0,5K |
| Skelett des Übergabe-Prompts | rund 0,3K |
| Code- und Werkzeugausgaben | verbleibendes Kontingent |

Nicht injiziert: die Gesamttabelle der Übernahmeaufzeichnung (es werden nur die von dieser Karte betroffenen Einträge injiziert), Entwurfsanmerkungen, das Website-Texte-Kapitel.

## 8. Eiserne Regeln des Übergabe-Prompts

Zu Beginn jedes Teils wird eine feste Eröffnung injiziert; die eisernen Regeln umfassen fest sechs Punkte:

1. Durchgehend vereinfachtes Chinesisch ausgeben; Code, Befehle, Pfade und Eigennamen dürfen im Original bleiben.
2. Nur das tun, was in der Aufgabenkarte steht; keine nicht angeforderten Funktionen, Konfigurationen oder Erweiterungsfähigkeiten hinzufügen.
3. Nichts erfinden oder fabulieren; bei unsicheren API-Signaturen direkt die Unsicherheit erklären; Fakten und Vermutungen explizit unterscheiden.
4. Schlägt der Abnahmebefehl fehl, ist gemäß der Fehlerbehandlung der Aufgabenkarte zu verfahren; das eigenmächtige Ändern der Abnahmekriterien ist nicht zulässig.
5. Aktionen, die Dateien löschen oder überschreiben, sind ausnahmslos anzuhalten und auf die Bestätigung des Benutzers zu warten.
6. Nach Abschluss die Übergabeaufzeichnung strikt gemäß den Übergabeanforderungen schreiben und dann enden.

## 9. Spezifikation für das Ausfüllen durch die Cloud

Bevor das Cloud-Modell das Handbuch ausfüllt, sind zunächst zwei Vorarbeiten abzuschließen, dann wird Kapitel für Kapitel ausgefüllt:

1. Prämissenprüfung: fehlerhafte Prämissen, logische Sprünge und fehlende Informationen prüfen; bei Unvollständigkeit zuerst den Benutzer fragen.
2. Open-Source-Sondierung: verfügbare fertige Lösungen im Open-Source-Ökosystem recherchieren; erst sichten, dann ausfüllen; wo eine ausgereifte Lösung verfügbar ist, kein Rad neu erfinden; die Ergebnisse in der Übernahmeaufzeichnung registrieren.

Beim Ausfüllen gilt:

1. Alle vagen Wörter tilgen; jede Stelle erhält einen exakten Wert oder eine Entscheidungsregel.
2. Entwurfsentscheidungen gehören in die Entwurfsanmerkungen, einschließlich Auswahlgründen und verworfenen Entwürfen, zur Prüfung durch den Benutzer; sie werden nicht in das lokale Modell injiziert.
3. Anweisungen an das lokale Modell sind so zu verfassen, als wisse es nichts über den Projekthintergrund; alle Prämissen sind explizit auszuschreiben.
4. Konformitätsuntergrenze: unklare Lizenz als „zu bestätigen“ kennzeichnen; starke-Copyleft-Lösungen mit Hinweis auf abgeleitete Pflichten kennzeichnen; modifizierten Open-Source-Code mit Original-Copyright und Änderungsbeschreibung versehen; Übernahmen müssen README, README_EN, NOTICE und LICENSE synchronisieren, die Synchronisation ist als expliziter Schritt und Abnahmeinhalt der jeweiligen Aufgabenkarte zu erfassen.
5. Für Dokumentformatspezifikationen auf die entsprechenden Spezifikationen dieses Repositorys verweisen; den Spezifikationstext nicht ins Handbuch kopieren.

## 10. Phasenstatus und Arbeitsfenster

Jedes Kapitel im maschinenlesbaren Index trägt eine Phasenkennzeichnung, nach der das lokale Arbeitsfenster angepasst wird:

| Phase | Merkmale | Arbeitsfenster |
| --- | --- | --- |
| Greenfield | Implementierung nach eingefrorenem Vertrag ausfüllen | 16–24K |
| Wachstum | modulübergreifende Funktionen, Standardstufe | 32K |
| Wartung | Refaktorierung und modulübergreifende Fehlersuche | 48–64K, Parallelität entsprechend reduziert |

Kapitel in der Wartungsphase müssen zusätzlich eine Fehlersuchanleitung anhängen: eine Dreispalten-Tabelle aus Symptom, möglichen Positionen und Verifikationsbefehl.

## 11. Übernahmeaufzeichnung, Release und Website-Texte

1. Die Felder der Übernahmeaufzeichnungstabelle sind fest: Name, Kategorie, Version, Zweck, Lizenz, Copyright-Inhaber, offizielle Adresse, ob modifiziert, Änderungsbeschreibung, Art der Kennzeichnung, Übernahmestatus; der Übernahmestatus ist in die drei Stufen „sofort übernehmbar“, „zu bewerten“, „noch nicht verfügbar“ unterteilt.
2. Das Release-Kapitel deckt Build-Skripte, CI-Matrix, Checksummen und die Vorlage der Signatur-Umgebungsvariablen ab; der Abnahmebefehl der Release-Karte ist die Prüfung der Build-Artefakte; externe Veröffentlichungsaktionen gelangen nicht in das lokale Modell und werden nach Bestätigung durch den Benutzer ausgeführt.
3. Das Website-Texte-Kapitel richtet sich an normale Benutzer: Code, Kommandozeile, Fachbegriffe und Leerwörter sind verboten; die Struktur umfasst Erstbild-Positionierung, Schmerzpunkte, Highlights, Vertrauen, Download, Szenengeschichten und häufige Fragen; der Ton ist ruhig und zurückhaltend.

## 12. Projektübergreifende Verweise und Prüfung

1. Referenziert das Zielprojekt diese Spezifikation, wird der Volltext über `gitrule spec` gelesen und das Handbuchskelett als Anfangsskelett des projektinternen Handbuchs kopiert; diese Spezifikation wird nicht mit dem Projekt überarbeitet, die Evolution des projektinternen Handbuchs schließt sich im Projekt-Repository.
2. Für Aufgabenkarten mit Dokumentlieferungen wird der Abnahmebefehl um `gitrule check` ergänzt; bei mehrsprachigen Projekten um `gitrule xcheck`; nach Änderungen am Glossar ist `gitrule termcheck` auszuführen.
3. Dokumentverletzungen von `gitrule check` gehören zur Klasse der automatisch reparierbaren Fälle; zunächst `gitrule optimize` ausführen und erneut prüfen; ist immer noch nicht bestanden, in das block-Feld der Übergabeaufzeichnung schreiben.
4. Gitrule-Spezifikationen regeln nur Dokumente und Repository-Konventionen; die Codequalität obliegt den Tests und Verifikationsskripten der jeweiligen Projekte; beide ersetzen einander nicht.

## Verwandte Dateien

- [Maschinenlesbarer Index](./README.md): der Registrierungseinstieg dieser Spezifikation
- [Harte Regeln](./hard-rules.md): die übergeordnete Beschränkung der Abnahmeschranken dieser Spezifikation
- [Dokumentationsmatrix](./document-matrix.md): die eindeutige Zuständigkeitsdefinition des Lieferdokuments, zu dem das Handbuch gehört
- [Allgemeine Schreibspezifikation](./general-writing-specification.md): der Schreibstandard für den Handbuchtext
- [Mehrsprachigkeitsspezifikation](./multilingual-specification.md): die Regeln zur mehrsprachigen Synchronisierung dieser Spezifikation
- [Spezifikation für maschinenlesbare Metadaten](./machine-readable-metadata-specification.md): die stabile Kennung und Pfadzuordnung dieser Spezifikation
- [Informationserhebung und Vorlagen](./information-collection-and-templates.md): die Terminologie-Gegenüberstellung und die Feldkonventionen der Vorlagen
