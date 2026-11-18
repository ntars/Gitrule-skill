# Skill-Erstellungsspezifikation

> Problem, das diese Datei löst: Definiert Struktur, Auslösebedingungen und progressives Laden bei der Kapselung eines Spezifikationssatzes als Skill, damit Skills auffindbar, wartbar und frei von doppelten Inhalten bleiben.

## 1. Verzeichnisstruktur

Ein Skill verwendet die Struktur „Einstiegspunkt + bedarfsgesteuerte Ressourcen“:

```text
skill-name/
├── SKILL.md          必需：元数据 + 核心流程
├── references/       规范正文，按需加载
└── assets/           模板与素材（可选）
```

## 2. Anforderungen an SKILL.md

1. Die Metadaten enthalten `name` und `description`; die Beschreibung muss „was tun + wann verwenden“ benennen, um die Auslösung zu ermöglichen.
2. Der Haupttext enthält nur die dauerhaft geltenden Kernregeln und Abläufe; detaillierte Nachschlageinhalte gehören nach `references/`.
3. Imperativ- bzw. Infinitivform verwenden, die zweite Person vermeiden.
4. Bei der Referenzierung von Ressourcen eindeutige Pfade und die Bedingung „wann lesen“ angeben.

## 3. Harte Regeln

1. Der Spezifikationstext wird nur an einer Stelle gepflegt: Skills referenzieren die Dateien dieses Spezifikationssatzes und kopieren nicht den Volltext, um doppelte Drift zu vermeiden.
2. Ein Skill erledigt nur eine Sache; mehrere Zuständigkeiten in denselben Skill zu packen ist verboten.
3. Auslösebedingungen mit konkreten Phrasen angeben, um zu breite Auslösung zu vermeiden.
4. Die Version wird synchron mit der Version des Spezifikationssatzes aktualisiert.

## Verwandte Dateien

- Struktur der Metadatenliste siehe [Spezifikation für maschinenlesbare Metadaten](./machine-readable-metadata-specification.md)
- Einzige Zuständigkeit der Dokumentation siehe [Dokumentmatrix](./document-matrix.md)
- Konventionen für Agent-Aufrufe siehe [Spezifikation für Agent-Aufrufe und Prompts](./agent-invocation-and-prompt-specification.md)
