# Spezifikation für maschinenlesbare Metadaten

> Problem, das diese Datei löst: Definiert die Struktur einer Metadatenliste, die von Experten, Skills, MCP, Kommandozeile und anderen Programmen konsumiert wird, damit die maschinelle Nutzung stabil und auffindbar ist.

## 1. Designziele

1. Stabile Kennung: Jedes Dokument besitzt eine eindeutige, unveränderliche Kennung für die programmatische Referenzierung.
2. Sprachunabhängigkeit: Die Kennung ändert sich nicht mit der Sprache; die Sprache zeigt sich nur im Pfad.
3. Auffindbarkeit: Die Liste führt Typ, Pfad, Sprache und Kurzfassung aller Dokumente auf.

## 2. Struktur der Liste

Die Maschinenliste (Manifest) muss enthalten:

| Feld | Anforderung |
| --- | --- |
| id | stabile eindeutige Kennung, kleingeschriebenes kebab-case, ohne Sprache und Version |
| title | Titel des Dokuments |
| summary | ein Satz zur Beschreibung des gelösten Problems |
| domain | zugehörige Domäne (eine der sieben Domänen) |
| paths | Zuordnung von Sprachcode zu relativem Pfad, z. B. `zh-CN`: `./locales/zh-CN/角色与职责.md` |
| version | Version des Spezifikationssatzes |

## 3. Harte Regeln

1. Neue Sprachen werden nur als zusätzliche Zuordnung in `paths` ergänzt; `id` und die Pfade anderer Sprachen bleiben unverändert.
2. Bei Umbenennung eines Dokuments bleibt `id` unverändert; nur `paths` wird aktualisiert.
3. Kennung und Pfad müssen mit der tatsächlichen Datei übereinstimmen; die kontinuierliche Integration prüft die Gültigkeit der Liste.
4. Diese Spezifikation stellt ein kopierbares Listenbeispiel bereit; das Zielprojekt muss gemäß den Feldern aus Abschnitt 2 eine konkrete Listeninstanz anlegen und sicherstellen, dass `paths` mit den Dateien auf dem Datenträger übereinstimmen.

## 4. Listenbeispiel (kopierbar)

Das folgende Beispiel führt drei Dokumenteinträge auf. Die tatsächliche Liste muss alle Spezifikationen des Zielsprachverzeichnisses abdecken; `id` ändert sich nicht mit der Sprache, `paths` wird nach Sprachcode um Zuordnungen ergänzt.

```json
{
  "version": "1.0.0",
  "entries": [
    {
      "id": "role-and-responsibility",
      "title": "角色与职责",
      "summary": "定义执行者身份、职责边界、触发条件、适用范围与硬性约束",
      "domain": "总纲与治理",
      "paths": {
        "zh-CN": "./locales/zh-CN/角色与职责.md"
      },
      "version": "1.0.0"
    },
    {
      "id": "readme-standard-template",
      "title": "README标准模板",
      "summary": "提供可直接套用的通用 README 模板与占位符对照表",
      "domain": "命名与文档",
      "paths": {
        "zh-CN": "./locales/zh-CN/README标准模板.md"
      },
      "version": "1.0.0"
    },
    {
      "id": "machine-readable-metadata",
      "title": "机器可读元数据规范",
      "summary": "定义供专家、Skill、MCP、命令行消费的元数据清单结构",
      "domain": "AI 与机器适配",
      "paths": {
        "zh-CN": "./locales/zh-CN/机器可读元数据规范.md"
      },
      "version": "1.0.0"
    }
  ]
}
```

Bei einer neuen Sprache wird nur in `paths` des betreffenden Eintrags eine Zuordnung ergänzt, beispielsweise `"en-US": "./locales/en-US/role-and-responsibility.md"`; `id` darf nicht geändert werden.

## Verwandte Dateien

- Schreibweise für die Metadatenkonsumierung durch Skills siehe [Skill-Erstellungsspezifikation](./skill-authoring-specification.md)
- Art der Dokumentbereitstellung durch MCP-Werkzeuge siehe [MCP-Werkzeugspezifikation](./mcp-tool-specification.md)
- Konventionen für Agent-Aufrufe siehe [Spezifikation für Agent-Aufrufe und Prompts](./agent-invocation-and-prompt-specification.md)
