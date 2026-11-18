# MCP-Werkzeugspezifikation

> Problem, das diese Datei löst: Definiert Schnittstellendesign und Beschreibungsregeln, wenn ein Spezifikationssatz über das Model Context Protocol (MCP) als Werkzeug bereitgestellt wird, damit Werkzeuge vom Modell korrekt gefunden und aufgerufen werden können.

## 1. Prinzipien des Werkzeugdesigns

1. Einzige Zuständigkeit: Ein Werkzeug erledigt eine Sache; umfassende All-in-one-Schnittstellen vermeiden.
2. Klare Beschreibung: Die Werkzeugbeschreibung nennt Zweck und Einsatzszenarien, damit das Modell entscheiden kann, wann es aufruft.
3. Eindeutige Parameter: Jeder Parameter hat Typ, Pflichtangabe, Wertebereich und Beschreibung.
4. Strukturierte Ausgabe: Strukturierte Daten zurückgeben, lange Fließtexte vermeiden.

## 2. Pflichtfelder

| Feld | Anforderung |
| --- | --- |
| name | eindeutige Kennung, kleingeschriebenes kebab-case |
| description | Zweck und Auslösebedingungen, konkret beurteilbar |
| inputSchema | Parametertypen, Pflichtfelder, Einschränkungen |
| Rückgabewert | strukturiertes Format und Feldbeschreibung |
| Fehler | Rückgabeformat bei Fehlschlag, Ergebnisse dürfen nicht erfunden werden |

## 3. Werkzeuge zum Spezifikationssatz

1. Dokumentabruf: Liefert Spezifikationsinhalte anhand von Sprachcode + Kennung (Kennungen siehe [Spezifikation für maschinenlesbare Metadaten](./machine-readable-metadata-specification.md)).
2. Listen: Liefert die verfügbaren Dokumente samt Sprachzuordnung.
3. Validierung: Prüft die Vollständigkeit der Dokumentmatrix (siehe [Dokumentmatrix](./document-matrix.md)) und den Status der Qualitätstore (siehe [Qualitätstor](./quality-gate.md)).

## 4. Harte Regeln

1. Werkzeuge dürfen nicht prüfbare Ergebnisse nicht als PASS zurückgeben; SKIP und Grund sind zu kennzeichnen (siehe [Verbotene Praktiken](./prohibited-practices.md)).
2. Die Ausgabe muss programmatisch parsebar sein und keine internen Denkprozesse enthalten.
3. Sicherheitsrelevante Inhalte dürfen nicht über Werkzeuge offengelegt werden (siehe [Sicherheits- und Datenschutzspezifikation](./security-and-privacy-specification.md)).

## Verwandte Dateien

- Metadatenstruktur siehe [Spezifikation für maschinenlesbare Metadaten](./machine-readable-metadata-specification.md)
- Skill-Kapselung siehe [Skill-Erstellungsspezifikation](./skill-authoring-specification.md)
- Konventionen für Agent-Aufrufe siehe [Spezifikation für Agent-Aufrufe und Prompts](./agent-invocation-and-prompt-specification.md)
