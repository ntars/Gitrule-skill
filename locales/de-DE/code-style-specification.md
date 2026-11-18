# Code-Stil-Spezifikation

> Problem, das diese Datei löst: Sie definiert Vorlage der Code-Stilkonfiguration, Namenskonventionstabelle, Kommentarregeln und Hinweise zum Ausfüllen, um Stilabweichungen zu verringern und Lesbarkeit sowie Review-Effizienz zu steigern.

## 1. Spezifikationsregeln

1. Stilregeln richten sich nach automatisierten Werkzeugen; manuell werden nur Bereiche behandelt, die Werkzeuge nicht abdecken können.
2. Die Formatierungskonfiguration muss mit dem Repository eingecheckt werden (etwa eine Konfigurationsdatei für die Formatierung), um Konsistenz über Umgebungen hinweg zu gewährleisten.
3. Die CI muss eine Formatprüfung integrieren; bei Nichtbestehen ist eine Zusammenführung unzulässig (siehe [Test-Spezifikation](./testing-specification.md)).
4. Magische Zahlen und hartcodierte Konstanten sind unzulässig; sie müssen als benannte Konstanten extrahiert werden.
5. Zeilenenden sind einheitlich LF, Dateien enden mit einem Zeilenumbruch (entspricht Dimension D3 Repository-Hygiene).

## 2. Vorlage der Stilkonfiguration

```markdown
# Code-Stilkonvention: {{项目名称}}

Konfigurationsversion: {{v1.0}} ｜ Anwendbare Sprache und Version: {{如 TypeScript 5.x}} ｜ Formatierungswerkzeug: {{如 Prettier 3.x}}

## Formatregeln (werkzeugerzwungen)
| Regel | Wert | Werkzeugoption | Verhandelbar |
| --- | --- | --- | --- |
| Einrückung | {{2 空格 / 4 空格 / Tab}} | {{配置项名}} | Nein |
| Zeilenbreite | {{100 字符}} | {{配置项名}} | Nein |
| Anführungszeichen | {{单引号 / 双引号}} | {{配置项名}} | Nein |
| Zeilenende | LF | `endOfLine: lf` | Nein |
| Zeilenumbruch am Dateiende | Erforderlich | Werkzeugstandard | Nein |
| Semikolon | {{有 / 无}} | {{配置项名}} | Nein |

## Namenskonventionen (nicht werkzeugerzwingbar, manuelle Prüfung)
| Objekt | Regel | Positivbeispiel | Gegenbeispiel |
| --- | --- | --- | --- |
| Variable | {{camelCase}} | `userName` | `UserName` |
| Konstante | {{UPPER_SNAKE_CASE}} | `MAX_RETRY` | `maxRetry` |
| Funktion | {{动词开头 camelCase}} | `parseConfig` | `configParse` |
| Klasse / Typ | {{PascalCase}} | `ConfigLoader` | `config_loader` |
| Dateiname | {{kebab-case}} | `config-loader.ts` | `ConfigLoader.ts` |
| Boolescher Wert | {{is/has/can 前缀}} | `isValid` | `valid` |
| Sammlung | {{复数名词}} | `items` | `itemList` |

## Kommentarregeln
- Situationen mit Kommentarpflicht: {{公开 API 的契约、非直观算法、绕开限制的临时方案}}
- Verbotene Kommentare: {{复述代码、无信息量、失效的旧注释、情绪化表述}}
- Kommentarsprache: {{与项目主语言一致}}
- TODO-Format: `// TODO({{负责人}}): {{事项}} — {{计划版本}}`

## Dateiorganisation
1. Importreihenfolge: {{标准库 → 第三方 → 本地模块，组内字典序}}
2. Deklarationsreihenfolge: {{常量 → 类型 → 函数 → 导出}}
3. Maximale Zeilenzahl pro Datei: {{300 行，超出须拆分}}

## Ausnahmenliste
| Situation | Ausnahmeregel | Genehmigt von | Gültig bis |
| --- | --- | --- | --- |
| {{如生成代码}} | {{不参与格式化}} | {{姓名}} | {{至 v2.0}} |
```

## 3. Felddefinitionen der Konfiguration

| Feld | Pflichtfeld | Typ | Hinweise zum Ausfüllen | Beispiel |
| --- | --- | --- | --- | --- |
| Konfigurationsversion | Ja | Text | Bei Änderung der Stilregeln erhöhen | `v1.0` |
| Anwendbare Sprache und Version | Ja | Text | Hauptversion angeben, um Regelabweichungen zu vermeiden | `TypeScript 5.x` |
| Formatierungswerkzeug | Ja | Text | Muss mit der Version in der Lockfile übereinstimmen | `Prettier 3.2` |
| Regel.Wert | Ja | Aufzählung / Zahl | Muss eindeutig sein, „je nach Fall“ ist unzulässig | `2 Leerzeichen` |
| Verhandelbar | Ja | Aufzählung | Nein / Ja; bei „Ja“ sind die Bedingungen anzugeben | `Nein` |
| Positivbeispiel der Benennung | Ja | Code | Aus dem vorhandenen Projektcode entnehmen | `parseConfig` |
| Gegenbeispiel der Benennung | Ja | Code | Muss eine real häufig gemachte Schreibweise sein | `configParse` |
| TODO-Verantwortlicher | Ja | Text | „Team“ ist unzulässig | `Zhang San` |
| Gültigkeit der Ausnahme | Ja | Version / Datum | Nach Ablauf ist eine erneute Prüfung erforderlich | `Bis v2.0` |

## 4. Hinweise zum Ausfüllen

1. **Werkzeugvorrang**: Alle Regeln, die ein Werkzeug erzwingen kann, gehören in die Formatierungskonfiguration und nicht in das Gedächtnis der Mitwirkenden; manuell werden nur Benennung, Kommentare und Dateiorganisation behandelt.
2. **Wert der Zeilenbreite**: Dieser ist an der Breite der Review-Oberfläche auszurichten, üblich sind 100 oder 120; nach der Festlegung darf er nicht in einzelnen Dateien überschrieben werden.
3. **Positivbeispiele der Benennung**: Aus dem vorhandenen Projektcode tatsächlich existierende Namen entnehmen; lehrbuchartige Platzhalter sind unzulässig.
4. **Boolesche Benennung**: Die Präfixe `is`/`has`/`can` müssen der Semantik entsprechen; `isReady` darf keine Aktion bezeichnen.
5. **TODO**: Verantwortlichen, Vorgang und geplante Version sind zwingend anzugeben; TODOs ohne Planung dürfen nicht in den Hauptzweig gelangen.
6. **Ausnahmenliste**: Jede Ausnahme benötigt Genehmiger und Gültigkeitsdauer; ohne erneute Prüfung nach Ablauf verfällt sie automatisch.

Häufige Fehler:

| Fehlerhafte Formulierung | Problem | Korrektur |
| --- | --- | --- |
| „Code möglichst prägnant halten“ | Nicht beurteilbar | In prüfbare Regel ändern, etwa Obergrenze der Funktionslänge |
| Namenskonventionstabelle enthält nur Regeln, keine Gegenbeispiele | Kein Vergleich bei der Prüfung möglich | Reale, häufig gemachte Gegenbeispiele ergänzen |
| Kommentar lautet „Hier war früher ein Bug“ | Informationslos und schnell veraltet | Stattdessen aktuelles Verhalten und Grund beschreiben |
| TODO ohne Verantwortlichen | Niemand folgt nach | Verantwortlichen und geplante Version ergänzen |
| Ausnahme ohne Gültigkeitsdauer | Dauerhafte Ausnahme | Gültigkeitsdauer und Prüfperson ergänzen |

## 5. Vollständiges Beispiel

```markdown
# Code-Stilkonvention: markdown-lint-cli

Konfigurationsversion: v1.0 ｜ Anwendbare Sprache und Version: TypeScript 5.x ｜ Formatierungswerkzeug: Prettier 3.2

## Formatregeln (werkzeugerzwungen)
| Regel | Wert | Werkzeugoption | Verhandelbar |
| --- | --- | --- | --- |
| Einrückung | 2 Leerzeichen | `tabWidth: 2` | Nein |
| Zeilenbreite | 100 Zeichen | `printWidth: 100` | Nein |
| Anführungszeichen | Einfache Anführungszeichen | `singleQuote: true` | Nein |
| Zeilenende | LF | `endOfLine: lf` | Nein |
| Semikolon | Ja | `semi: true` | Nein |

## Namenskonventionen (manuelle Prüfung)
| Objekt | Regel | Positivbeispiel | Gegenbeispiel |
| --- | --- | --- | --- |
| Funktion | camelCase mit Verb am Anfang | `parseRules` | `rulesParser` |
| Konstante | UPPER_SNAKE_CASE | `DEFAULT_RULES` | `defaultRules` |
| Dateiname | kebab-case | `rule-loader.ts` | `RuleLoader.ts` |

## Kommentarregeln
- Situationen mit Kommentarpflicht: die Treffersemantik von Regeln, Umgehungen des Verhaltens vorgelagerter APIs.
- Verbotene Kommentare: Wiedergabe des Codes, „einen Bug behoben“, TODO ohne Verantwortlichen.
- TODO-Format: `// TODO(Wang Wu): temporären Parser ersetzen — v2.0`

## Ausnahmenliste
| Situation | Ausnahmeregel | Genehmigt von | Gültig bis |
| --- | --- | --- | --- |
| Verzeichnis fixtures | Nimmt nicht an der Formatierung teil | Li Si | Bis v2.0 |
```

## Verwandte Dateien

- Grundlage der Code-Review-Prüfung: [Code-Review-Spezifikation](./code-review-specification.md)
- Formatprüfung in der CI: [Test-Spezifikation](./testing-specification.md), [CI-Workflow-Spezifikation](./ci-workflow-specification.md)
- Repository-Hygiene als Dimension D3: [Prüfungsdimensionsmatrix](./review-dimension-matrix.md)
- Prüfung vor dem Commit: [Push- und Veröffentlichungs-Spezifikation](./push-and-release-specification.md)
- Verfolgung von Anforderungen zur Umsetzung: [Anforderungs-Verfolgungsmatrix-Spezifikation](./requirements-traceability-matrix-specification.md)
