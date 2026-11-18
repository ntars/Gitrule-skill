# Sub-Agent-Dispatch-Vertrag

> Problem, das diese Datei löst: Definiert die vier Elemente, die bei der Aufgabenzuweisung an einen Sub-Agenten zwingend anzugeben sind, sowie die Kooperationsvorgaben, damit Ergebnisse strukturiert, überprüfbar und frei von Regelabweichungen bleiben.

## 1. Vier Dispatch-Elemente

Bei jeder Zuweisung müssen vier Elemente angegeben werden:

```text
TASK:    <一句话任务>
INPUT:   <需要的文件/上下文，只给必要部分>
OUTPUT:  <结构化格式，表格或 JSON，禁止散文>
FAIL:    <做不了时返回什么，而不是瞎编>
```

## 2. Vorgaben

- Ein Sub-Agent erledigt pro Auftrag nur eine Sache; „schreibe nebenbei auch die README“ ist verboten.
- Sub-Agenten dürfen nur lesen und nur Lösungen liefern; **Dateischreiben und Git-Operationen werden ausschließlich von der Hauptsteuerung ausgeführt**.
- Ergebnisse von Sub-Agenten müssen Belege enthalten (Dateipfad + Zeilennummer / Befehlsausgabe); Ergebnisse ohne Belege gelten als ungültig.
- Sub-Agenten kommunizieren nicht direkt miteinander, alles wird über die Hauptsteuerung zusammengeführt, um Regelabweichungen zu vermeiden.

## Verwandte Dateien

- Zuweisungsziele und Dimensionen siehe [Review-Dimensionsmatrix](./review-dimension-matrix.md)
- Zuweisung der Dokumenterstellung siehe [Dokumentmatrix](./document-matrix.md)
- Die Zuweisung erfolgt in Phase 2 und Phase 4 des [Ausführungsprozesses](./execution-process.md)
