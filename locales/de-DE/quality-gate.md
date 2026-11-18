# Qualitätstor

> Problem, das diese Datei löst: Sie definiert die Freigabebedingungen der dreistufigen Tore, die Vorlage der Bewertungscheckliste und deren Felder, damit die Push-Freigabe einheitlich, ausführbar und nachprüfbar erfolgt.

## 1. Dreistufige Tore

| Stufe | Bedeutung | Freigabebedingung |
| --- | --- | --- |
| Gate A · Sicherheitstor | Geheimnisse, Privatsphäre, Lizenzen, große Dateien | null P0 |
| Gate B · Qualitätstor | Build, Tests, Lint, Commit-Konventionen, Branch-Schutz | null P0, P1 als Aufgabe erfasst |
| Gate C · Startseitentor | README, Metadaten, Dokumentationsmatrix, Badges, Links | null P0, P1 ≤ 3 und terminiert |

Nur wenn A, B und C vollständig grün sind, wird `✅ ALLOW PUSH` ausgegeben. Nicht bestandene Punkte sind zu korrigieren oder mit Begründung zu kennzeichnen; das Ergebnis wird im [Prüfberichtsformat](./audit-report-format.md) festgehalten.

## 2. 14 Bewertungspunkte vor der Lieferung

Vor der Lieferung der Dokumentation ist jeder Punkt zu bewerten; nicht bestandene Punkte sind zu korrigieren oder mit Begründung zu kennzeichnen.

| Nummer | Prüfpunkt | Bewertungsmaßstab |
| --- | --- | --- |
| G1 | Umgangssprache und Mehrdeutigkeit | Volltextsuche nach umgangssprachlichen Wörtern und unklaren Verweisen, Trefferzahl 0 |
| G2 | Abschnittsvollständigkeit | Deutsche und englische Fassung umfassen jeweils 20 Kapitel in gleicher Reihenfolge |
| G3 | Übereinstimmung von Funktionen und Verzeichnis | Jede in der README beschriebene Funktion hat ein entsprechendes Modul in der Verzeichnisstruktur |
| G4 | Belege für Features | Jedes Feature besitzt einen Beleg oder ist als ausstehend gekennzeichnet |
| G5 | Abdeckung der Designdetails | Alle 10 Kategorien in Abschnitt 8 enthalten Einträge oder sind als nicht zutreffend gekennzeichnet |
| G6 | Vollständigkeit der Abhängigkeiten | Anzahl direkter und indirekter Abhängigkeiten stimmt mit dem Abhängigkeitsbaum überein |
| G7 | Genauigkeit der Lizenzen | Der SPDX-Identifier jeder Abhängigkeit stimmt mit der offiziellen Angabe überein |
| G8 | Lizenzvolltext | Für alle Lizenzen, die den Volltext verlangen, ist der englische Originaltext beigefügt |
| G9 | Urheberrechtshinweise | Urheberrechtshinweise des Projekts und Dritter sind vollständig |
| G10 | Zweisprachige Synchronität | Abschnitte, Tabellen, Terminologie und Codeblöcke stimmen in beiden Fassungen überein |
| G11 | Ausführbarkeit der Befehle | Installations-, Schnellstart- und Push-Befehle sind direkt ausführbar |
| G12 | Zusammenfassung offener Punkte | Alle offenen Punkte sind zusammengefasst und lokalisierbar |
| G13 | Herkunft der Materialien | Für alle Materialien sind Quelle und Lizenz dokumentiert |
| G14 | Sensible Informationen | Keine Geheimnisse, Tokens, internen Adressen oder personenbezogenen Daten |

## 3. Vorlage der Tor-Bewertungscheckliste

```markdown
# Tor-Bewertung: {{项目名称}} {{版本号}}

Bewertungsdatum: {{YYYY-MM-DD}} ｜ Bewertende Person: {{姓名}} ｜ Repository: {{owner/repo}}

## Gate A · Sicherheitstor
| Nummer | Prüfpunkt | Ergebnis | Nachweis | Stufe | Maßnahme |
| --- | --- | --- | --- | --- | --- |
| A1 | Geheimnisse im Arbeitsbereich | PASS / FAIL / SKIP | {{命令输出}} | {{P0}} | {{动作}} |
| A2 | Geheimnisse in der Historie | PASS / FAIL / SKIP | {{命令输出}} | {{P0}} | {{动作}} |
| A3 | Bereinigung sensibler Informationen | PASS / FAIL / SKIP | {{证据}} | {{P0}} | {{动作}} |
| A4 | Vorhandensein und Typ der LICENSE | PASS / FAIL / SKIP | {{路径}} | {{P0}} | {{动作}} |
| A5 | Große Dateien und LFS | PASS / FAIL / SKIP | {{命令输出}} | {{P0}} | {{动作}} |

Ergebnis: {{PASS / FAIL}}, offene Punkte: {{列出 / 无}}

## Gate B · Qualitätstor
| Nummer | Prüfpunkt | Ergebnis | Nachweis | Stufe | Maßnahme |
| --- | --- | --- | --- | --- | --- |
| B1 | Build bestanden | PASS / FAIL / SKIP | {{CI URL}} | {{P0}} | {{动作}} |
| B2 | Tests bestanden | PASS / FAIL / SKIP | {{CI URL}} | {{P0}} | {{动作}} |
| B3 | Lint / Formatierung | PASS / FAIL / SKIP | {{CI URL}} | {{P1}} | {{动作}} |
| B4 | Commit-Nachrichtenkonvention | PASS / FAIL / SKIP | {{git log}} | {{P1}} | {{动作}} |
| B5 | Branch-Schutz | PASS / FAIL / SKIP | {{平台设置截图说明}} | {{P0}} | {{动作}} |

Ergebnis: {{PASS / FAIL}}, offene Punkte: {{列出 / 无}}

## Gate C · Startseitentor
| Nummer | Prüfpunkt | Ergebnis | Nachweis | Stufe | Maßnahme |
| --- | --- | --- | --- | --- | --- |
| C1 | Vier Kernelemente der README | PASS / FAIL / SKIP | {{路径:行号}} | {{P1}} | {{动作}} |
| C2 | Dokumentationsmatrix vollständig | PASS / FAIL / SKIP | {{清单}} | {{P1}} | {{动作}} |
| C3 | Metadaten vollständig | PASS / FAIL / SKIP | {{平台设置}} | {{P1}} | {{动作}} |
| C4 | Badges funktionsfähig | PASS / FAIL / SKIP | {{HTTP 检查}} | {{P2}} | {{动作}} |
| C5 | Links gültig | PASS / FAIL / SKIP | {{校验输出}} | {{P1}} | {{动作}} |

Ergebnis: {{PASS / FAIL}}, offene Punkte: {{列出 / 无}}

## 14 Bewertungspunkte vor der Lieferung
| Nummer | Ergebnis | Nachweis | Maßnahme |
| --- | --- | --- | --- |
| G1 ~ G14 | {{PASS / FAIL / SKIP}} | {{证据}} | {{动作}} |

## Gesamtbewertung
- A: {{PASS / FAIL}} ｜ B: {{PASS / FAIL}} ｜ C: {{PASS / FAIL}}
- Freigabeergebnis: {{✅ ALLOW PUSH / ⛔ BLOCK PUSH}}
- Blockierungsgrund: {{无 / 列出 P0}}
```

## 4. Felddefinitionen

| Feld | Pflichtfeld | Typ | Hinweise zum Ausfüllen | Beispiel |
| --- | --- | --- | --- | --- |
| Bewertende Person | Ja | Text | Eindeutig, „Team“ ist unzulässig | `Wang Wu` |
| Ergebnis | Ja | Aufzählung | PASS / FAIL / SKIP | `PASS` |
| Nachweis | Ja | Text | Pfad + Zeilennummer oder Befehlsausgabe, Bewertung ohne Nachweis unzulässig | `gitleaks: 0 findings` |
| Stufe | Bedingt erforderlich | Aufzählung | Bei FAIL zwingend P0 / P1 / P2 | `P0` |
| Maßnahme | Bedingt erforderlich | Text | Bei FAIL zwingend konkrete Aktion und Verantwortliche | `Schlüssel rotieren und Historie bereinigen` |
| SKIP-Grund | Bedingt erforderlich | Text | Bei SKIP zwingend, grundloses Überspringen unzulässig | `Kein Build-Skript` |
| Freigabeergebnis | Ja | Aufzählung | ALLOW PUSH / BLOCK PUSH | `BLOCK PUSH` |
| Blockierungsgrund | Bedingt erforderlich | Text | Bei BLOCK zwingend, P0-Punkte auflisten | `A2 Treffer für Geheimnis in der Historie` |

## 5. Ausfüllhinweise

1. **Nachweispflicht**: Jede Bewertung benötigt einen Nachweis; ein PASS ohne Nachweis gilt als ungültig und ist in SKIP mit Begründung zu ändern.
2. **Stufenzuordnung**: FAIL erfordert eine Stufe; P0 blockiert die Freigabe unmittelbar, P1 ist als Aufgabe zu erfassen, P2 wird als Empfehlung vermerkt.
3. **Schwelle von Gate C**: PASS erst bei P1 ≤ 3 und erfolgter Terminierung; bei Überschreitung ist herabzustufen oder zu blockieren.
4. **Verwendung von SKIP**: Ist eine Prüfung nicht möglich, ist SKIP + Grund zu vermerken; PASS darf nicht geschrieben werden. Sobald die Bedingungen vorliegen, ist die Prüfung nachzuholen.
5. **Konsistenz**: Die Tor-Bewertung muss mit den Stufen P0/P1/P2 der [Prüfungsdimensionsmatrix](./review-dimension-matrix.md) und den Blockierungsregeln der [Harten Regeln](./hard-rules.md) übereinstimmen.
6. **Freigabe**: Erst wenn alle drei Punkte grün sind, wird `✅ ALLOW PUSH` ausgegeben; bei einem FAIL wird `⛔ BLOCK PUSH` ausgegeben und der Blockierungsgrund aufgeführt.
7. **Lieferformat**: Die Bewertungsergebnisse werden gemäß [Prüfberichtsformat](./audit-report-format.md) ausgegeben; nach Bestehen erfolgt die Ausführung gemäß [Push- und Veröffentlichungs-Spezifikation](./push-and-release-specification.md).

Häufige Fehler:

| Fehlerhafte Schreibweise | Problem | Korrektur |
| --- | --- | --- |
| Ergebnis PASS, aber Nachweis leer | Bewertung ungültig | Nachweis ergänzen oder auf SKIP ändern |
| ALLOW PUSH trotz nicht genullter P0 | Verstoß gegen harte Regeln | Auf BLOCK PUSH ändern |
| SKIP ohne Grund | Vermutete übersehene Prüfung | Grund ergänzen |
| Gate C mit fünf P1-Punkten dennoch PASS | Schwelle überschritten | Herabstufen oder blockieren |
| Bewertungsergebnis nur als Text ohne Checkliste | Nicht nachprüfbar | Vorlage Punkt für Punkt ausfüllen |

## 6. Vollständiges Beispiel

```markdown
# Tor-Bewertung: markdown-lint-cli v1.0.0

Bewertungsdatum: 2026-11-20 ｜ Bewertende Person: Wang Wu ｜ Repository: example/markdown-lint-cli

## Gate A · Sicherheitstor
| Nummer | Prüfpunkt | Ergebnis | Nachweis | Stufe | Maßnahme |
| --- | --- | --- | --- | --- | --- |
| A1 | Geheimnisse im Arbeitsbereich | PASS | gitleaks detect: 0 findings | — | — |
| A2 | Geheimnisse in der Historie | PASS | gitleaks --log-opts=--all: 0 findings | — | — |
| A4 | Vorhandensein und Typ der LICENSE | PASS | LICENSE Zeile 1 MIT | — | — |
| A5 | Große Dateien und LFS | PASS | find -size +50M: keine | — | — |

Ergebnis: PASS, offene Punkte: keine

## Gate B · Qualitätstor
| Nummer | Prüfpunkt | Ergebnis | Nachweis | Stufe | Maßnahme |
| --- | --- | --- | --- | --- | --- |
| B1 | Build bestanden | PASS | run #128 | — | — |
| B2 | Tests bestanden | PASS | 132/132 passed | — | — |
| B4 | Commit-Nachrichtenkonvention | PASS | git log --oneline durchgehend konform | — | — |

Ergebnis: PASS, offene Punkte: keine

## Gesamtbewertung
- A: PASS ｜ B: PASS ｜ C: PASS
- Freigabeergebnis: ✅ ALLOW PUSH
- Blockierungsgrund: keine
```

## Verwandte Dateien

- Bewertungsgrundlagen und Fehlerstufen: [Prüfungsdimensionsmatrix](./review-dimension-matrix.md)
- Regeln, deren Verletzung blockiert: [Harte Regeln](./hard-rules.md)
- Ausgabeformat der Bewertungsergebnisse: [Prüfberichtsformat](./audit-report-format.md)
- Ausführung nach bestandenem Tor: [Push- und Veröffentlichungs-Spezifikation](./push-and-release-specification.md)
- Nachweisquelle des Sicherheitstors: [Sicherheits- und Datenschutz-Spezifikation](./security-and-privacy-specification.md)
- Nachweisquelle des Qualitätstors: [Test-Spezifikation](./testing-specification.md), [CI-Workflow-Spezifikation](./ci-workflow-specification.md)
- Bewertungsgrundlage des Startseitentors: [README-Standardvorlage](./readme-standard-template.md), [Dokumentationsmatrix](./document-matrix.md)
