# Ausführungsprozess

> Problem, das diese Datei löst: Definiert die vollständige Phasenfolge vom Projektstart bis zur Auslieferung, die Eintrittsbedingungen und Ergebnisse jeder Phase sowie die blockierenden Rückfrageregeln bei unzureichenden Informationen.

## 1. Gesamtsteuerungs-Push-Prozess (Phase 0–6)

### Phase 0 · Projektstart (Project Init)

Ergebnis: 3 Namenskandidaten für das Projekt + Begründung der Auswahl + Ergebnis der Namensdublettenprüfung + Repository-Metadatentabelle (description / topics / Standard-Branch / Sichtbarkeit / license). Namensregeln siehe [Projektnamens-Spezifikation](./project-naming-specification.md).

### Phase 1 · Bestandsaufnahme (Inventory)

Repository scannen und eine strukturierte Liste erzeugen:
- Technologie-Stack, Einstiegsdateien, Paketmanager, Lockfile
- Vorhandene Dokumentation, fehlende Dokumentation
- Top 10 der größten Dateien im Repository
- Vorhandene CI / Vorlagen / Schutzregeln
- Aktueller Git-Status: nicht verfolgte Dateien, nicht committete Änderungen, verdächtige Commits in der Historie

### Phase 2 · Paralleles Review (Audit)

Gemäß [Review-Dimensionsmatrix](./review-dimension-matrix.md) die Dimensionen an Sub-Agenten zur parallelen Ausführung zuweisen; die Zuweisung siehe [Sub-Agent-Dispatch-Vertrag](./sub-agent-dispatch-contract.md). Jeder Sub-Agent liefert nur strukturierte Ergebnisse, keine langen Fließtexte.

### Phase 3 · Behebung (Fix)

Die Aufgaben in der Reihenfolge P0 → P1 → P2 auflisten, mit verantwortlichem Agenten und geplanter Maßnahme. Solange P0 nicht auf null steht, darf Phase 5 nicht begonnen werden.

### Phase 4 · Dokumenterstellung (Docs)

Gemäß [Dokumentmatrix](./document-matrix.md) Datei für Datei an Dokument-Agenten zuweisen. **Es wird immer nur eine Datei geschrieben; erst nach Prüfung folgt die nächste.**

### Phase 5 · Push (Push)

Gemäß [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md) ausführen und das Ergebnis Punkt für Punkt zurückmelden.

### Phase 6 · Nach dem Push (Post-Push)

Tag setzen, Release Notes schreiben, Verfügbarkeit von Badges und Links prüfen, grünen CI bestätigen, Richtigkeit der Informationen im About-Bereich bestätigen.

## 2. Dokumenterstellungsprozess (Phase 0–5)

Die Phasen werden der Reihe nach durchlaufen; solange eine Phase nicht abgeschlossen ist, darf die nächste nicht begonnen werden.

| Phase | Name | Eintrittsbedingung | Ergebnis |
| --- | --- | --- | --- |
| 0 | Informationsprüfung | Spezifikation und Projektmaterialien liegen vor | Liste bestätigter Informationen, Liste fehlender Informationen |
| 1 | Blockierende Rückfragen | Pflichtfelder fehlen (siehe [Informationserfassung und Vorlagen](./information-collection-and-templates.md)) | Strukturierte Rückfrageliste, nach Feldern gruppiert |
| 2 | Strukturbestätigung | Pflichtfelder vollständig | Kapitelverzeichnis der README und Stichpunktgliederung je Kapitel zur Bestätigung durch den Nutzer |
| 3 | Dokumenterstellung | Der Nutzer bestätigt die Struktur oder erklärt ausdrücklich, dass keine Bestätigung erforderlich ist | Alle Ergebnisse |
| 4 | Qualitätstor | Dokumenterstellung abgeschlossen | Punktweise Beurteilungsergebnisse des [Qualitätstors](./quality-gate.md) |
| 5 | Auslieferung | Alle Tore bestanden oder nicht bestandene Punkte gekennzeichnet | Ausgabe in der Reihenfolge des [Prüfberichtsformats](./audit-report-format.md), mit Push-Anleitung |

## 3. Rückfrageregeln in Phase 1

1. Fragen nach Feldern gruppiert stellen, höchstens 15 Punkte pro Runde.
2. Jede Frage muss Zweck und betroffene Kapitel nennen, damit der Nutzer die Priorität einschätzen kann.
3. Erklärt der Nutzer ausdrücklich, dass eine Angabe nicht möglich ist, ist an der entsprechenden Stelle im Dokument „【Zu bestätigen: Feldname】“ zu vermerken und am Dateiende zusammenzufassen.
4. Antwortet der Nutzer „nach Ihrer Einschätzung“, dürfen Vorschlagswerte genannt werden, die jedoch mit „【Vorschlagswert, vom Nutzer zu bestätigen】“ zu kennzeichnen sind.

## Verwandte Dateien

- Rollen und Verantwortlichkeiten siehe [Rollen und Verantwortlichkeiten](./roles-and-responsibilities.md)
- Pflichtfelder und Kennzeichnung fehlender Angaben siehe [Informationserfassung und Vorlagen](./information-collection-and-templates.md)
- Beurteilung des Qualitätstors siehe [Qualitätstor](./quality-gate.md)
