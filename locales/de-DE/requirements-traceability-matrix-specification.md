# Anforderungs-Verfolgungsmatrix-Spezifikation

> Problem, das diese Datei löst: Sie definiert Vorlage und Felder einer bidirektionalen Verfolgungsmatrix von Anforderungen zu Design, Umsetzung, Tests und Veröffentlichung, damit die Artefakte aller Lebenszyklusphasen konsistent aufeinander verweisen, Änderungsauswirkungen bewertbar sind und Abdeckungslücken auffindbar bleiben.

## 1. Spezifikationsregeln

1. Jede Anforderung der Stufe „Muss“ muss eine Zeile in der Verfolgungsmatrix belegen und die Artefakte der gesamten Kette vom Projektstart bis zur Veröffentlichung erfassen.
2. Verfolgungsbeziehungen müssen in beide Richtungen nachschlagbar sein: vorwärts von der Anforderung zu den nachgelagerten Artefakten, rückwärts vom Artefakt zur vorgelagerten Anforderung.
3. Entspricht eine Anforderung mehreren Artefakten, ist eine kommagetrennte Liste von Nummern zu verwenden; die Nummern müssen exakt mit den Definitionen in den jeweiligen Dokumenten übereinstimmen.
4. Anforderungsänderungen müssen in der Matrix nachvollziehbar dokumentiert werden, mit Änderungsgrund, Auswirkungsumfang und Entscheider; die ursprünglichen Werte dürfen nicht direkt überschrieben werden.
5. Die Matrix muss vor jeder Versionsveröffentlichung geprüft werden; nicht abgeschlossene Anforderungen der Stufe „Muss“ dürfen nicht veröffentlicht werden.
6. Berechnungsgrundlage der Abdeckung: Anforderungsabdeckung = Anzahl veröffentlichter Anforderungen der Stufe „Muss“ / Gesamtzahl der Anforderungen der Stufe „Muss“.

## 2. Vorlage der Verfolgungsmatrix

```markdown
# Anforderungs-Verfolgungsmatrix: {{项目名称}}

Version: {{vX.Y.Z}} ｜ Aktualisiert von: {{姓名}} ｜ Letzte Prüfung: {{YYYY-MM-DD}}

| Anforderungs-ID | Anforderungstitel | Priorität | Projektziel | Architekturentscheidung | Designdokument | Umsetzungs-PR | Testfall | Veröffentlichungsversion | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | {{标题}} | Muss | G1 | ADR-0002 | docs/api.md#check | #12 | TC-001, TC-002 | v1.0.0 | Verifiziert |
| REQ-002 | {{标题}} | Sollte | G2 | — | — | #15 | TC-005 | — | Umgesetzt |
| REQ-003 | {{标题}} | Muss | G1 | ADR-0003 | docs/architecture.md#flow | — | — | — | Ausstehend |

Status: Ausstehend / Bestätigt / Zu umsetzen / Umgesetzt / Verifiziert / Veröffentlicht / Verworfen
```

## 3. Vorlage des Rückwärtsindex

```markdown
## Rückwärtssuche nach Artefakt

| Artefakttyp | Artefaktnummer | Abgedeckte Anforderungs-IDs |
| --- | --- | --- |
| Architekturentscheidung | ADR-0002 | REQ-001, REQ-004 |
| Testfall | TC-001 | REQ-001 |
| Umsetzungs-PR | #12 | REQ-001, REQ-007 |
| Veröffentlichungsversion | v1.0.0 | REQ-001, REQ-002 |
```

## 4. Vorlage des Änderungsprotokolls

```markdown
## Änderungsprotokoll

| Datum | Anforderungs-ID | Änderungsinhalt | Grund | Auswirkungsumfang | Entscheider |
| --- | --- | --- | --- | --- | --- |
| {{YYYY-MM-DD}} | {{REQ-NNN}} | {{字段：原值 → 新值}} | {{依据}} | {{受影响的下游产物}} | {{姓名}} |
```

## 5. Felddefinitionen

| Feld | Pflichtfeld | Typ | Hinweise zum Ausfüllen | Beispiel |
| --- | --- | --- | --- | --- |
| Anforderungs-ID | Ja | `REQ-NNN` | Muss mit der Nummerierung der [Projektstart- und Anforderungs-Spezifikation](./project-initiation-and-requirements-specification.md) übereinstimmen | `REQ-001` |
| Priorität | Ja | Aufzählung | Muss / Sollte / Kann | `Muss` |
| Projektziel | Ja | `G-N` | Entspricht der Zielnummer im Projektstartdokument | `G1` |
| Architekturentscheidung | Nein | `ADR-NNNN` | Ohne Architekturentscheidung „—“ schreiben, nicht leer lassen | `ADR-0002` |
| Designdokument | Nein | `Pfad#Anker` | Genau bis zum Abschnittsanker | `docs/api.md#check` |
| Umsetzungs-PR | Nein | `#Nummer` | PR-Nummer, nicht der Commit-Hash | `#12` |
| Testfall | Ja | Liste von `TC-NNN` | Mindestens ein Eintrag; ohne Testfall ist der Grund anzugeben | `TC-001` |
| Veröffentlichungsversion | Nein | `vX.Y.Z` | Muss mit dem Tag übereinstimmen | `v1.0.0` |
| Status | Ja | Aufzählung | Einer von sieben Zuständen, nur vorwärts, außer Verwerfung | `Verifiziert` |
| Änderungsprotokoll.Auswirkungsumfang | Ja | Text | Betroffene ADR, PR und TC auflisten | `ADR-0002, TC-001` |

## 6. Hinweise zum Ausfüllen

1. **Nummernkonsistenz**: Anforderungs-IDs, ADR-Nummern und TC-Nummern in der Matrix müssen zeichengenau mit den Quelldokumenten übereinstimmen; Abkürzungen und Aliasnamen sind unzulässig.
2. **Leerwertregel**: Nicht zutreffende Angaben werden als „—“ geschrieben, noch nicht erzeugte als „Ausstehend“; beide Bedeutungen sind verschieden und dürfen nicht vermischt werden.
3. **Rückwärtsindex**: Nach jeder Aktualisierung der Vorwärtsmatrix ist der Rückwärtsindex synchron zu aktualisieren; bei Abweichungen gilt die Vorwärtsmatrix, die unverzüglich zu korrigieren ist.
4. **Änderungsnachweis**: Vor dem Ändern eines Feldes ist im Änderungsprotokoll eine Zeile mit altem und neuem Wert zu ergänzen; direktes Überschreiben ist unzulässig.
5. **Prüfung vor der Veröffentlichung**: Vor der Veröffentlichung ist für jede Anforderung der Stufe „Muss“ zu prüfen, ob Testfall und Veröffentlichungsversion vorliegen; fehlt eine Angabe, ist die Veröffentlichung zu blockieren.
6. **Verworfene Anforderungen**: Die Zeile bleibt erhalten und wird nicht gelöscht, der Status wird auf „Verworfen“ gesetzt und im Änderungsprotokoll der Grund der Verwerfung dokumentiert.

Häufige Fehler:

| Fehlerhafte Formulierung | Problem | Korrektur |
| --- | --- | --- |
| Feld für Testfälle bleibt leer | Abdeckungslücke nicht sichtbar | „Ausstehend“ eintragen und vor der Veröffentlichung auf null bringen |
| Feld für PR enthält den Commit-Hash | Review-Nachweis nicht auffindbar | PR-Nummer verwenden |
| Wert wird bei Änderung direkt geändert | Auswirkung nicht nachvollziehbar | Zuerst Änderungsprotokoll ergänzen |
| Status springt von „Verifiziert“ zurück auf „Umgesetzt“ | Verstoß gegen das Vorwärtsprinzip | Neuen Defekt anlegen und eigene Verfolgungszeile beginnen |
| Vorwärts- und Rückwärtsindex weichen voneinander ab | Referenzen stimmen nicht überein | Vor der Veröffentlichung anhand der Vorwärtsmatrix synchronisieren |

## 7. Vollständiges Beispiel

```markdown
# Anforderungs-Verfolgungsmatrix: markdown-lint-cli

Version: v1.0.0 ｜ Aktualisiert von: Wang Wu ｜ Letzte Prüfung: 2026-11-20

| Anforderungs-ID | Anforderungstitel | Priorität | Projektziel | Architekturentscheidung | Designdokument | Umsetzungs-PR | Testfall | Veröffentlichungsversion | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | Prüfung von Leerzeichen zwischen chinesischem und englischem Text | Muss | G1 | ADR-0002 | docs/api.md#rules-spacing | #12 | TC-001, TC-002 | v1.0.0 | Veröffentlicht |
| REQ-002 | Ausgabe von JSON-Berichten | Sollte | G1 | — | docs/api.md#reporter | #15 | TC-011 | v1.0.0 | Veröffentlicht |
| REQ-003 | Integration in Editor-Plugins | Kann | G2 | Ausstehend | Ausstehend | — | Ausstehend | — | Ausstehend |

## Änderungsprotokoll

| Datum | Anforderungs-ID | Änderungsinhalt | Grund | Auswirkungsumfang | Entscheider |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | REQ-003 | Priorität: Sollte → Kann | Zeitrahmen für v1.0 nicht ausreichend | ADR-0005, TC-020 | Li Si |
```

## Verwandte Dateien

- Anforderungsnummern und Abnahmebedingungen: [Projektstart- und Anforderungs-Spezifikation](./project-initiation-and-requirements-specification.md)
- Nummerierung von Architekturentscheidungen: [Architekturdesign-Dokumentations-Spezifikation](./architecture-design-document-specification.md)
- Nummerierung von Testfällen: [Test-Spezifikation](./testing-specification.md)
- Veröffentlichungsversionen und Tags: [Versionsverwaltungs-Spezifikation](./version-management-specification.md)
- Externe Änderungsbeschreibung einer Version: [Änderungsprotokoll-Spezifikation](./changelog-specification.md)
- Prozessrückblick nach einer Iteration: [Iterationsretrospektiven-Spezifikation](./iteration-retrospective-specification.md)
