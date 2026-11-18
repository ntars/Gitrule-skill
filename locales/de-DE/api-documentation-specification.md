# API-Dokumentations-Spezifikation

> Problem, das diese Datei löst: Sie definiert Struktur und Felder einer vollständigen API-Referenzdokumentation als Grundlage für die Erstellung von docs/api.md und trennt diese strikt von tutorialartigen Inhalten.

## 1. Pflichtstruktur

Jeder API-Eintrag muss enthalten:

| Feld | Anforderung |
| --- | --- |
| Schnittstellensignatur | Methode, Pfad oder Funktionsprototyp, vollständig und kopierbar |
| Parameter | Name, Typ, Pflichtangabe, Standardwert, Wertebereich, Beschreibung |
| Rückgabewert | Beschreibung von Typ und Struktur |
| Fehlercodes | Fehlercode, Auslösebedingung, Behandlungsweise |
| Aufrufbeispiel | Lauffähiges Minimalbeispiel mit Sprachkennzeichnung |
| Ratenbegrenzung und Kontingente | Aufruffrequenzbegrenzung, Kontingent, Behandlung bei Überschreitung |

## 2. Verbindliche Regeln

1. Parameter und Rückgabewerte müssen Typ und Einschränkungen angeben; Standardwerte dürfen nicht weggelassen werden.
2. Fehlercodes sind vollständig aufzuführen; die Angabe „kann Fehler verursachen“ ist unzulässig.
3. Codeblöcke müssen mit einer Sprachkennung versehen sein, Beispiele müssen eigenständig lauffähig sein.
4. Diese Datei enthält ausschließlich Referenzinformationen, keine Tutorials, Hintergründe oder Designausführungen (Tutorials und Hintergründe siehe [README-Abschnitts-Spezifikation](./readme-sections-specification.md)).

## 3. Konsistenzanforderungen

Die Schnittstellensignaturen in der API-Dokumentation müssen mit der tatsächlichen Code-Implementierung übereinstimmen; die Parameternamen müssen den Präzisionsanforderungen der [Allgemeinen Schreib-Spezifikation](./general-writing-specification.md) entsprechen; Terminologie siehe [Glossar](./glossary.md).

## Verwandte Dateien

- Abgrenzung der Dokumentationszuständigkeiten: [Dokumentationsmatrix](./document-matrix.md)
- API-Design-Spezifikation (wie Schnittstellen zu entwerfen sind): [API-Design-Spezifikation](./api-design-specification.md)
- Dokumentationsqualität gehört zu Dimension D12, siehe [Prüfungsdimensionsmatrix](./review-dimension-matrix.md)
