# Spezifikation für Agent-Aufrufe und Prompts

> Problem, das diese Datei löst: Definiert den Dispatch-Vertrag und die Prompt-Schreibweise beim Aufruf von Agent-Spezifikationssätzen, damit Aufrufe überprüfbar bleiben, keine Befugnisse überschreiten und nicht abdriften.

## 1. Aufrufprinzipien

1. Einzige Zuständigkeit: Ein Aufruf erledigt genau eine Sache; „nebenbei“ andere Aufgaben zu erledigen ist verboten.
2. Trennung von Lesen und Schreiben: Sub-Agenten lesen und analysieren nur; Dateischreiben und Git-Operationen führt ausschließlich die Hauptsteuerung aus (siehe [Sub-Agent-Dispatch-Vertrag](./sub-agent-dispatch-contract.md)).
3. Belegpflicht: Schlussfolgerungen müssen Belege enthalten (Pfad + Zeilennummer / Befehlsausgabe); ohne Beleg gelten sie als ungültig.
4. Keine Kommunikation: Sub-Agenten kommunizieren nicht direkt miteinander, alles wird über die Hauptsteuerung zusammengeführt.

## 2. Prompt-Struktur

Der Aufruf-Prompt muss vier Elemente enthalten:

```text
TASK:    <一句话任务>
INPUT:   <必要上下文，只给所需部分>
OUTPUT:  <结构化输出格式，表格或 JSON，禁止散文>
FAIL:    <无法完成时的返回约定，不得瞎编>
```

## 3. Prompt-Schreibweise

1. Schriftsprache und Imperativ verwenden, Informationen vollständig, nicht auf Kontextschlüsse angewiesen (siehe [Allgemeine Schreibspezifikation](./general-writing-specification.md)).
2. Ausgabeformat und Fehlerrückgabe eindeutig festlegen, um freie Entfaltung des Modells zu vermeiden.
3. Bei Bezug auf Spezifikationen den Dateipfad angeben (siehe [Spezifikation für maschinenlesbare Metadaten](./machine-readable-metadata-specification.md)).
4. Einheitliches Format für Vorlagen und Platzhalter (siehe [Informationserhebung und Vorlagen](./information-collection-and-templates.md)).

## 4. Harte Regeln

1. Agenten dürfen nicht dazu aufgefordert werden, Prüfergebnisse zu erfinden; nicht prüfbare Punkte sind mit SKIP + Grund zu kennzeichnen.
2. Interne Denkprozesse dürfen nicht in Liefergegenstände geschrieben werden (siehe [Verbotene Praktiken](./prohibited-practices.md)).
3. Sicherheitsrelevante Inhalte werden gemäß [Sicherheits- und Datenschutzspezifikation](./security-and-privacy-specification.md) behandelt.

## Verwandte Dateien

- Dispatch-Vertrag siehe [Sub-Agent-Dispatch-Vertrag](./sub-agent-dispatch-contract.md)
- Maschinen-Metadaten siehe [Spezifikation für maschinenlesbare Metadaten](./machine-readable-metadata-specification.md)
- Skill-Kapselung siehe [Skill-Erstellungsspezifikation](./skill-authoring-specification.md)
- MCP-Werkzeuge siehe [MCP-Werkzeugspezifikation](./mcp-tool-specification.md)
