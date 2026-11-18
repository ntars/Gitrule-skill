# README-Standardvorlage

> Problem, das diese Datei löst: Sie stellt eine universelle README-Vorlage bereit, die direkt kopiert und durch Ersetzen der Platzhalter übernommen werden kann. Sie deckt die Darstellung der Startseite über den gesamten Projektlebenszyklus ab und enthält eine Platzhalter-Übersicht, Hinweise zu optionalen Abschnitten sowie eine Liefer-Checkliste, sodass jede Entwicklerin und jeder Entwickler die Vorlage schnell an das eigene Projekt anpassen kann.

## 1. Anleitung

1. Den gesamten Inhalt von Abschnitt 3 „Vorlagentext“ kopieren und als `README.md` im Projektstamm neu anlegen.
2. Anhand der Platzhalter-Übersicht in Abschnitt 4 die `{{...}}` einzeln ersetzen; nicht verwendete Einträge samt zugehöriger Zeile oder Abschnitt löschen.
3. Die Unterabschnitte in Abschnitt 3 entsprechen den 20 Kapiteln der [README-Abschnittsspezifikation](./readme-sections-specification.md) und sind in der Lebenszyklusreihenfolge von innen nach außen angeordnet; beim Löschen eines Kapitels muss der zugehörige Link in der Startbildschirm-Navigation synchron entfernt werden.
4. Anhand der [Badge-Spezifikation](./badge-specification.md) Stil, Farbe und Anzahl der Badges vereinheitlichen; anhand der [README-Spezifikation für visuelles Layout](./readme-visual-layout-specification.md) die Platzierung von Screenshots, Tabellen und Codeblöcken prüfen.
5. Anhand des [README-Leitfadens zur Kategorieanpassung](./readme-category-adaptation-guide.md) die Abschnitte nach Projekttyp auswählen.
6. Vor dem Commit die Checkliste in Abschnitt 6 ausführen und bestätigen, dass keine Platzhalter zurückbleiben.

## 2. Anpassungsprinzipien

- **Pflichtangaben**: Projektname, Repository-Beschreibung, Ein-Satz-Positionierung, Installation, Schnellstart, Lizenz.
- **Feste Reihenfolge**: Die Abschnittsreihenfolge entspricht der [README-Abschnittsspezifikation](./readme-sections-specification.md); die chinesische und die englische Fassung entsprechen sich Kapitel für Kapitel.
- **Evidenz zuerst**: Kernfunktionen, Leistungsverhalten und technische Abwägungen müssen nachprüfbare Belege enthalten; qualitative Lobpreisungen sind unzulässig.
- **Transparente Offenlegung**: Ungeeignete Szenarien, Einschränkungen, bekannte Probleme und nicht implementierte Funktionen müssen ausdrücklich aufgeführt und dürfen nicht verschwiegen werden.
- **Keine Zusage**: Die Roadmap wird mit „keine Zusage“ gekennzeichnet; konkrete Liefertermine werden nicht genannt.
- **Echtheit**: Alle Befehle, Beispiele, Links und Badges müssen tatsächlich funktionieren; Kontaktangaben und Meldewege müssen real erreichbar sein.

## 3. Vorlagentext

Dieser Abschnitt ist nach dem Projektlebenszyklus „von innen nach außen“ gegliedert und umfasst 20 Abschnitte, die den 20 Kapiteln der [README-Abschnittsspezifikation](./readme-sections-specification.md) eins zu eins entsprechen. Der Text in den Codeblöcken jedes Abschnitts ist der kopierbare Inhalt.

Die Zuordnung von Abschnitten zu Lebenszyklusphasen ist nachstehend aufgeführt, um das gezielte Auffinden zu erleichtern:

| Lebenszyklusphase | Zugehörige Unterabschnitte | Darstellungsschwerpunkt |
| --- | --- | --- |
| Projektstart | 3.1–3.2 | Positionierung, Hintergrund, geeignete Szenarien und Einschränkungen |
| Anforderungsanalyse | 3.2–3.3 | Funktionsgrenzen, geeignete Szenarien, ungeeignete Szenarien |
| Architekturentwurf | 3.5–3.6, 3.11 | Technische Abwägungen, Technologie-Stack, Verzeichnisstruktur |
| Entwicklungsrealisierung | 3.3–3.4, 3.9–3.10 | Funktionen, Merkmale, Konfiguration, API |
| Test und Verifikation | 3.8, 3.12 | Schnellstart-Beispiel, Nachweise zum Leistungsverhalten |
| Bereitstellung und Freigabe | 3.7, 3.14 | Installation und Bereitstellung, Kompatibilitätsmatrix |
| Betrieb und Monitoring | 3.13, 3.15 | Sicherheit und Datenschutz, bekannte Probleme und Einschränkungen |
| Iterative Wartung | 3.15–3.17 | Nicht implementierte Funktionen, Änderungsprotokoll, weitere Roadmap |

Hinweis: Die README ist die Startseite des Projekts. Die Prozessdokumentation der einzelnen Phasen (vollständige Aufzeichnungen zu Anforderungen, Entwurf, Tests, Bereitstellung und Betrieb) wird durch die jeweiligen Spezifikationen getragen, siehe [Dokumentationsmatrix](./document-matrix.md); dieses Kapitel stellt ausschließlich die für Nutzende sichtbaren Ergebnisse dar.

### 3.1 Projektname und Positionierung (entspricht Kapitel 1)

````markdown
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="{{LOGO_DARK_URL}}">
    <img alt="{{项目名称}} Logo" src="{{LOGO_LIGHT_URL}}" width="{{LOGO_WIDTH}}">
  </picture>

  <h1>{{项目名称}}</h1>

  [![build](https://img.shields.io/github/actions/workflow/status/{{OWNER}}/{{REPO}}/{{WORKFLOW}}?style=flat-square&logo=github)](https://github.com/{{OWNER}}/{{REPO}}/actions)
  [![version](https://img.shields.io/badge/version-{{VERSION}}-blue?style=flat-square)]({{RELEASE_URL}})
  [![license](https://img.shields.io/badge/license-{{LICENSE_SPDX}}-blue?style=flat-square)](./LICENSE)

  **Repository-Beschreibung**: 【{{仓库描述中文}} | {{REPO_DESCRIPTION_EN}}】

  **Themen-Tags**: {{TOPICS}}

  {{一句话定位}}

  {{语言切换链接}}

  [Installation](#installation) · [Schnellstart](#schnellstart) · [Kernfunktionen](#kernfunktionen) · [Bekannte Probleme und Einschränkungen](#bekannte-probleme-und-einschränkungen) · [Weitere Roadmap](#weitere-roadmap) · [Dokumentation](#dokumentation) · [Beitragen](#beitragen)
</div>
````

### 3.2 Projektkurzvorstellung (entspricht Kapitel 2)

````markdown
## Projektkurzvorstellung

{{背景}}

{{核心思路}}

**Geeignete Szenarien**

- {{适用场景一}}
- {{适用场景二}}

**Ungeeignete Szenarien**

- {{不适用场景一}}
- {{不适用场景二}}

### Stärken und Einschränkungen

**Stärken**

| Stärke | Beschreibung | Nachweis |
| --- | --- | --- |
| {{优势名称}} | {{优势说明}} | {{证据}} |
| {{优势名称}} | {{优势说明}} | {{证据}} |

**Einschränkungen**

| Einschränkung | Auswirkungsbereich | Vorläufige Umgehung |
| --- | --- | --- |
| {{局限描述}} | {{影响范围}} | {{规避方式}} |
| {{局限描述}} | {{影响范围}} | {{规避方式}} |
````

### 3.3 Kernfunktionen (entspricht Kapitel 3)

````markdown
## Kernfunktionen

- {{功能一}}：{{触发条件与结果}}
- {{功能二}}：{{触发条件与结果}}
- {{功能三}}：{{触发条件与结果}}
````

### 3.4 Kernmerkmale (entspricht Kapitel 4)

Jedes Merkmal muss die vollständige Fünf-Abschnitt-Struktur enthalten; fehlt ein Abschnitt, darf das Merkmal nicht aufgeführt werden. Zur Schreibweise siehe [Leitfaden für Merkmale und technische Abwägungen](./features-and-engineering-tradeoffs-guide.md).

````markdown
## Kernmerkmale

### {{特性名称}}

- **Wert**: {{价值}}
- **Realisierung**: {{实现方式}}
- **Abgrenzung**: {{差异化}}
- **Nachweis**: {{证据}}
````

### 3.5 Entwurfsdetails und technische Abwägungen (entspricht Kapitel 5)

In drei Abschnitten „Szenario → Vorgehen → Begründung“ verfassen; abgedeckte Kategorien siehe Abschnitt 2 des [Leitfadens für Merkmale und technische Abwägungen](./features-and-engineering-tradeoffs-guide.md).

````markdown
## Entwurfsdetails und technische Abwägungen

### {{取舍主题}}

- **Szenario**: {{场景}}
- **Vorgehen**: {{处理方式}}
- **Begründung**: {{原因}}
````

### 3.6 Technologie-Stack und Abhängigkeitsliste (entspricht Kapitel 6)

````markdown
## Technologie-Stack und Abhängigkeitsliste

| Kategorie | Technologie oder Komponente | Versionsvorgabe | Zweck |
| --- | --- | --- | --- |
| Laufzeit | {{运行时与版本}} | {{运行时版本约束}} | {{运行时用途}} |
| Build | {{构建工具与版本}} | {{构建版本约束}} | {{构建用途}} |
| Tests | {{测试工具与版本}} | {{测试版本约束}} | {{测试用途}} |

Details zu Abhängigkeiten Dritter und Lizenzen siehe [NOTICE](./NOTICE).
````

### 3.7 Installation und Bereitstellung (entspricht Kapitel 7)

````markdown
## Installation

Umgebungsanforderungen: {{运行时 / 操作系统 / 版本}}

```bash
{{包管理器安装命令}}
```

Installation prüfen:

```bash
{{验证命令}}
```

Ausgabe:

```text
{{预期输出}}
```

Aktualisieren: `{{升级命令}}`. Deinstallieren: `{{卸载命令}}`.

Containerisierte Bereitstellung: {{容器化说明}}
````

### 3.8 Schnellstart (entspricht Kapitel 8)

````markdown
## Schnellstart

{{一句话说明本示例完成什么}}

```{{语言标识}}
{{最小可运行示例}}
```

Erwartete Ausgabe:

```text
{{输出}}
```
````

### 3.9 Konfiguration (entspricht Kapitel 9)

````markdown
## Konfiguration

| Schlüssel | Typ | Standardwert | Erforderlich | Wertebereich | Wirkung | Beispiel |
| --- | --- | --- | --- | --- | --- | --- |
| {{键名}} | {{类型}} | {{默认值}} | {{是否必填}} | {{取值范围}} | {{作用}} | {{示例值}} |

Konfigurationspriorität: {{配置优先级}}.

Hot-Reload: {{热更新支持说明}}
````

### 3.10 API- oder Modulbeschreibung (entspricht Kapitel 10)

````markdown
## API

{{模块概述}}

```{{语言标识}}
{{接口签名}}
```

Parameter:

| Parameter | Typ | Erforderlich | Beschreibung |
| --- | --- | --- | --- |
| {{参数名}} | {{参数类型}} | {{参数是否必填}} | {{参数说明}} |

Rückgabewert: {{返回值说明}}

Fehlercodes:

| Fehlercode | Bedeutung | Behandlung |
| --- | --- | --- |
| {{错误码}} | {{错误含义}} | {{错误处理方式}} |

Aufrufbeispiel:

```{{语言标识}}
{{调用示例}}
```

Ratenbegrenzung und Kontingente: {{限流与配额说明}}

Siehe [API-Dokumentation]({{API_DOC_PATH}}).
````

### 3.11 Verzeichnisstruktur (entspricht Kapitel 11)

````markdown
## Verzeichnisstruktur

```text
{{项目名}}/
├── {{目录条目}}   # {{职责}}
├── {{目录条目}}   # {{职责}}
└── {{目录条目}}   # {{职责}}
```
````

### 3.12 Leistungsverhalten (entspricht Kapitel 12)

````markdown
## Leistungsverhalten

Testumgebung: {{测试环境}}

Testmethode: {{测试方法}}

| Kennzahl | Wert | Vergleichsbasis |
| --- | --- | --- |
| {{性能指标}} | {{指标数值}} | {{对比基线}} |

Engpassanalyse: {{瓶颈分析}}

Optimierungsempfehlungen: {{调优建议}}
````

### 3.13 Sicherheit und Datenschutz (entspricht Kapitel 13)

````markdown
## Sicherheit und Datenschutz

Datenerhebung und -speicherung: {{数据收集与存储说明}}

Transportverschlüsselung: {{传输加密说明}}

Berechtigungsmodell: {{权限模型说明}}

Bekannte Risiken: {{已知风险}}

Meldeweg für Schwachstellen: {{漏洞上报渠道}}

Sicherheitsrichtlinie siehe [SECURITY.md](./SECURITY.md).
````

### 3.14 Kompatibilität (entspricht Kapitel 14)

````markdown
## Kompatibilität

| Dimension | Unterstützter Bereich | Verifikationsstatus |
| --- | --- | --- |
| Betriebssystem | {{操作系统}} | {{操作系统验证状态}} |
| Laufzeit | {{运行时兼容版本}} | {{运行时验证状态}} |
| Browser | {{浏览器}} | {{浏览器验证状态}} |
| Datenbank | {{数据库版本}} | {{数据库验证状态}} |

Ausdrücklich nicht unterstützt: {{明确不支持项}}
````

### 3.15 Bekannte Probleme, Einschränkungen und nicht implementierte Funktionen (entspricht Kapitel 15)

````markdown
## Bekannte Probleme und Einschränkungen

**Bekannte Probleme**

| Problembeschreibung | Auswirkungsbereich | Vorläufige Umgehung | Tracking-Link |
| --- | --- | --- | --- |
| {{问题描述}} | {{影响范围}} | {{临时规避方案}} | {{跟踪链接}} |

**Aktuelle Einschränkungen**

{{当前限制说明}}

**Nicht implementierte Funktionen**

| Funktion | Grund der Nichtumsetzung | Planungsstatus |
| --- | --- | --- |
| {{未实现功能}} | {{未实现原因}} | {{计划状态}} |
````

### 3.16 Änderungsprotokoll (entspricht Kapitel 16)

````markdown
## Änderungsprotokoll

Versionsänderungen folgen der Semantischen Versionierung und der Struktur von Keep a Changelog; die vollständige Aufzeichnung siehe [CHANGELOG.md](./CHANGELOG.md).
````

### 3.17 Weitere Roadmap (entspricht Kapitel 17)

Schreibweise für Status und Zielversion von Planungspunkten siehe [Roadmap-Spezifikation](./roadmap-specification.md); die Kennzeichnung „keine Zusage“ ist verpflichtend.

````markdown
## Weitere Roadmap

> Die folgenden Inhalte sind Planungspunkte und keine Lieferzusage; tatsächlicher Umfang und Zeitpunkt richten sich nach den Veröffentlichungsaufzeichnungen.

| Planungspunkt | Status | Zielversion |
| --- | --- | --- |
| {{计划项}} | {{计划状态}} | {{目标版本}} |
| {{计划项}} | {{计划状态}} | {{目标版本}} |
````

### 3.18 Beitragen (entspricht Kapitel 18)

````markdown
## Beitragen

- Einrichtung der Entwicklungsumgebung: {{搭建步骤}}
- Branch-Modell: {{说明}}
- Commit-Konvention: {{Conventional Commits 等}}
- PR-Anforderungen: {{要求}}
- Verhaltenskodex: siehe [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
- Issue-Vorlagen: siehe [.github/ISSUE_TEMPLATE/](./.github/ISSUE_TEMPLATE/)
````

### 3.19 Urheberrecht und Lizenz (entspricht Kapitel 19)

````markdown
## Lizenz

Copyright © {{年份}} {{著作权人}}. Licensed under {{SPDX 标识符}}.

Dieses Projekt steht unter der Lizenz {{许可证名称}}; der vollständige Text siehe [LICENSE](./LICENSE).
````

### 3.20 NOTICE-Konformitätserklärung (entspricht Kapitel 20)

````markdown
## NOTICE-Konformitätserklärung

Dieses Projekt verwendet Komponenten und Materialien Dritter; eine Zusammenfassung der Lizenzen und Urheberrechtsinformationen siehe [NOTICE](./NOTICE). Dieses Kapitel ersetzt nicht die NOTICE-Datei.
````

## 4. Platzhalter-Übersicht

Die Tabelle führt alle im Vorlagentext vorkommenden Platzhalter auf. Die Reihenfolge folgt den Abschnitten; nicht verwendete Einträge werden samt zugehöriger Zeile gelöscht.

| Platzhalter | Bedeutung | Beispiel | Erforderlich |
| --- | --- | --- | --- |
| `{{项目名称}}` | Anzeigename des Projekts | `Awesome Tool` | Ja |
| `{{LOGO_DARK_URL}}` | Adresse des Logos für das dunkle Farbschema | `media/logo-dark.svg` | Nein |
| `{{LOGO_LIGHT_URL}}` | Adresse des Logos für das helle Farbschema | `media/logo-light.svg` | Nein |
| `{{LOGO_WIDTH}}` | Anzeigebreite des Logos (px) | `200` | Nein |
| `{{OWNER}}` | Repository-Eigentümer | `octocat` | Nein |
| `{{REPO}}` | Repository-Name | `awesome-tool` | Nein |
| `{{WORKFLOW}}` | Dateiname des CI-Workflows | `ci.yml` | Nein |
| `{{VERSION}}` | Aktuelle Versionsnummer | `1.2.0` | Nein |
| `{{LICENSE_SPDX}}` | SPDX-Kennung der Lizenz | `MIT` | Ja |
| `{{RELEASE_URL}}` | URL der Veröffentlichungsseite | GitHub-Releases-Link | Nein |
| `{{仓库描述中文}}` | Chinesischer Teil der Repository-Beschreibung, ≤ 120 Zeichen | `Leichtgewichtiges Go-CLI-Tool für JSON-Verarbeitung` | Ja |
| `{{REPO_DESCRIPTION_EN}}` | Englischer Teil der Repository-Beschreibung, ≤ 120 Zeichen | `A lightweight Go CLI for JSON processing` | Ja |
| `{{TOPICS}}` | Themen-Tags, bis zu 20 englische Kleinschreibungswörter, mit `-` verbunden | `go cli json command-line developer-tools` | Nein |
| `{{一句话定位}}` | Ein Satz dazu, was das Projekt ist, für wen es gedacht ist und welches Problem es löst | `Ein leichtgewichtiges Go-CLI-Tool zur JSON-Verarbeitung` | Ja |
| `{{语言切换链接}}` | Link zur Umschaltung zwischen Sprachfassungen | Linktext `English`, Zielpfad gemäß tatsächlichem Sprachverzeichnis, z. B. `../en-US/README.md` | Nein |
| `{{背景}}` | Entstehungsgrund des Projekts und zu lösendes Problem | Projektabhängig | Ja |
| `{{核心思路}}` | Angewandte Kernmethode oder Entwurfsentscheidung | Projektabhängig | Ja |
| `{{适用场景一}}` / `{{适用场景二}}` | Fälle, für die das Projekt geeignet ist | `Kleine JSON-Dateien müssen schnell verarbeitet werden` | Ja |
| `{{不适用场景一}}` / `{{不适用场景二}}` | Ausdrücklich nicht empfohlene Fälle samt Gründen | `GB-große Dateien müssen gestreamt verarbeitet werden` | Ja |
| `{{优势名称}}` | Substantivische Bezeichnung der Stärke | `Keine Abhängigkeiten` | Nein |
| `{{优势说明}}` | Konkrete Erläuterung der Stärke | `Keine Laufzeitabhängigkeiten Dritter` | Nein |
| `{{证据}}` | Nachprüfbarer Beleg oder reproduzierbare Schritte für die Stärke | `ldd-Ausgabe ist leer` | Nein |
| `{{局限描述}}` | Konkrete Beschreibung der Einschränkung | `Kein gleichzeitiges Schreiben` | Nein |
| `{{影响范围}}` | Von der Einschränkung betroffene Funktionen oder Szenarien | `Bei gleichzeitigem Schreiben mehrerer Prozesse` | Nein |
| `{{规避方式}}` | Vorläufige Umgehung der Einschränkung | `Externe Sperre` | Nein |
| `{{功能一}}` / `{{功能二}}` / `{{功能三}}` | Funktionsname | `Filtern` | Ja |
| `{{触发条件与结果}}` | Auslösebedingung und Ergebnis der Funktion | `Nach Übergabe von --filter wird bedingt ausgegeben` | Ja |
| `{{特性名称}}` | Merkmalsname, höchstens 15 Zeichen | `Einzeldatei-Verteilung` | Nein |
| `{{价值}}` | Konkretes Problem, das das Merkmal löst, und Folgen bei Nichtlösung | Projektabhängig | Nein |
| `{{实现方式}}` | Eingesetzte Technik, Mechanismus oder Algorithmus, einschließlich Schlüsseldateien oder -funktionen | Projektabhängig | Nein |
| `{{差异化}}` | Objektiv beurteilbare Vergleichsdimension gegenüber benannten Lösungen | Projektabhängig | Nein |
| `{{证据}}` | Reproduzierbare Tests, Benchmarks, Codestellen oder Schritte | Projektabhängig | Nein |
| `{{取舍主题}}` | Thema der technischen Abwägung | `Gleichzeitiges Schreiben` | Nein |
| `{{场景}}` | Konkrete Situation, die dieses Design auslöst | Projektabhängig | Nein |
| `{{处理方式}}` | Gewähltes Vorgehen | Projektabhängig | Nein |
| `{{原因}}` | Begründung, warum andere Vorgehen nicht gewählt wurden | Projektabhängig | Nein |
| `{{运行时与版本}}` / `{{构建工具与版本}}` / `{{测试工具与版本}}` | Name und Version der Stack-Komponente | `Go 1.22` | Nein |
| `{{运行时版本约束}}` / `{{构建版本约束}}` / `{{测试版本约束}}` | Bereich der Versionsvorgabe | `>=1.22` | Nein |
| `{{运行时用途}}` / `{{构建用途}}` / `{{测试用途}}` | Zweck der Komponente | `Kompilieren und Ausführen` | Nein |
| `{{运行时 / 操作系统 / 版本}}` | Anforderungen an die Installationsumgebung | `Go 1.22+、Linux/macOS` | Ja |
| `{{包管理器安装命令}}` | Tatsächlicher Installationsbefehl | `go install example.com/tool@latest` | Ja |
| `{{验证命令}}` | Befehl zur Prüfung der Installation | `tool --version` | Nein |
| `{{预期输出}}` | Erwartetes Ergebnis des Prüfbefehls | `tool 1.2.0` | Nein |
| `{{升级命令}}` / `{{卸载命令}}` | Befehle zum Aktualisieren und Deinstallieren | `go install example.com/tool@latest` | Nein |
| `{{容器化说明}}` | Hinweis zur Containerisierung oder Image-Adresse | `docker run ...` | Nein |
| `{{一句话说明本示例完成什么}}` | Ziel des Schnellstart-Beispiels | `JSON nach Feld filtern und ausgeben` | Ja |
| `{{语言标识}}` | Sprachkennung des Codeblocks | `bash` | Ja |
| `{{最小可运行示例}}` | Minimales lauffähiges Beispiel | Projektabhängig | Ja |
| `{{输出}}` | Erwartete Ausgabe des Beispiels | Projektabhängig | Ja |
| `{{键名}}` | Name des Konfigurationsschlüssels | `output.format` | Nein |
| `{{类型}}` | Typ des Konfigurationswerts | `string` | Nein |
| `{{默认值}}` | Standardwert der Konfiguration | `json` | Nein |
| `{{是否必填}}` | Angabe, ob erforderlich | `Nein` | Nein |
| `{{取值范围}}` | Zulässiger Wertebereich | `json / yaml` | Nein |
| `{{作用}}` | Wirkung der Konfiguration | `Ausgabeformat festlegen` | Nein |
| `{{示例值}}` | Konfigurationsbeispiel | `yaml` | Nein |
| `{{配置优先级}}` | Rangfolge bei Konfiguration aus mehreren Quellen | `Kommandozeilenargument > Umgebungsvariable > Konfigurationsdatei` | Nein |
| `{{热更新支持说明}}` | Ob Hot-Reload unterstützt wird und auf welche Weise | `Nicht unterstützt, Neustart erforderlich` | Nein |
| `{{模块概述}}` | Überblick über den Zweck des Moduls | Projektabhängig | Nein |
| `{{接口签名}}` | Signatur von Funktion oder Schnittstelle | `func Filter(in io.Reader, key string) error` | Nein |
| `{{参数名}}` / `{{参数类型}}` / `{{参数是否必填}}` / `{{参数说明}}` | Felder der Schnittstellenparameter | `in / io.Reader / Ja / Eingabestrom` | Nein |
| `{{返回值说明}}` | Bedeutung des Rückgabewerts | `Bei Erfolg wird nil zurückgegeben` | Nein |
| `{{错误码}}` / `{{错误含义}}` / `{{错误处理方式}}` | Felder des Fehlercodes | `E001 / Eingabe leer / Eingabe prüfen` | Nein |
| `{{调用示例}}` | Codebeispiel für den Aufruf der Schnittstelle | Projektabhängig | Nein |
| `{{限流与配额说明}}` | Regeln für Ratenbegrenzung und Kontingente | `Keine Ratenbegrenzung` | Nein |
| `{{API_DOC_PATH}}` | Relativer Pfad zur API-Dokumentation | `./docs/api.md` | Nein |
| `{{项目名}}` | Name des Wurzelknotens im Verzeichnisbaum | `awesome-tool` | Ja |
| `{{目录条目}}` / `{{职责}}` | Einträge und Zuständigkeiten im Verzeichnisbaum | `cmd/ / Befehlseinstieg` | Ja |
| `{{测试环境}}` | Hardware, System, Laufzeitversion | `Intel i7 / Ubuntu 22.04 / Go 1.22` | Nein |
| `{{测试方法}}` | Methode des Leistungstests | `go test -bench` | Nein |
| `{{性能指标}}` / `{{指标数值}}` / `{{对比基线}}` | Felder der Leistungskennzahl | `Durchsatz / 120 MB/s / 80 MB/s` | Nein |
| `{{瓶颈分析}}` | Erläuterung des Leistungsengpasses | Projektabhängig | Nein |
| `{{调优建议}}` | Empfehlungen zur Leistungsoptimierung | Projektabhängig | Nein |
| `{{数据收集与存储说明}}` | Umfang der Datenerhebung und Art der Speicherung | `Es werden keine Nutzerdaten erhoben` | Nein |
| `{{传输加密说明}}` | Art der Transportverschlüsselung | `HTTPS` | Nein |
| `{{权限模型说明}}` | Erläuterung des Berechtigungsmodells | `Token-basiert` | Nein |
| `{{已知风险}}` | Bekannte Sicherheitsrisiken | Projektabhängig | Nein |
| `{{漏洞上报渠道}}` | Real erreichbarer Meldeweg für Schwachstellen | `security@example.com` | Nein |
| `{{操作系统}}` / `{{操作系统验证状态}}` | Unterstützte Betriebssysteme und Verifikationsstatus | `Linux, macOS / Verifiziert` | Nein |
| `{{运行时兼容版本}}` / `{{运行时验证状态}}` | Kompatibler Laufzeitbereich und Verifikationsstatus | `Go 1.20+ / Verifiziert` | Nein |
| `{{浏览器}}` / `{{浏览器验证状态}}` | Unterstützte Browser und Verifikationsstatus | `Chrome 100+ / Verifiziert` | Nein |
| `{{数据库版本}}` / `{{数据库验证状态}}` | Datenbankversion und Verifikationsstatus | `PostgreSQL 14+ / Verifiziert` | Nein |
| `{{明确不支持项}}` | Ausdrücklich nicht unterstützte Umgebungen | `Windows 32 Bit` | Nein |
| `{{问题描述}}` | Beschreibung des bekannten Problems | `Hoher Speicherverbrauch bei sehr langen Eingaben` | Nein |
| `{{影响范围}}` | Von dem Problem betroffene Funktionen oder Szenarien | `Bei Eingaben über 100 MB` | Nein |
| `{{临时规避方案}}` | Vorläufige Umgehung | `Stapelweise Verarbeitung` | Nein |
| `{{跟踪链接}}` | Adresse zur Verfolgung des Problems | GitHub-Issue-Link | Nein |
| `{{当前限制说明}}` | Aktuelle funktionale Einschränkung | `Gleichzeitiges Schreiben wird noch nicht unterstützt` | Nein |
| `{{未实现功能}}` | Bislang nicht implementierte Funktion | `Hot-Reload der Konfiguration` | Nein |
| `{{未实现原因}}` | Grund der Nichtumsetzung | `Geringe Priorität` | Nein |
| `{{计划状态}}` | Planungsstatus (für nicht implementierte Funktionen und Roadmap) | `Eingeplant` | Nein |
| `{{计划项}}` | Planungspunkt der Roadmap | `Hot-Reload der Konfigurationsdatei unterstützen` | Nein |
| `{{目标版本}}` | Zielversion des Planungspunkts | `v1.3.0` | Nein |
| `{{搭建步骤}}` | Schritte oder Link zur Einrichtung der Entwicklungsumgebung | `Siehe CONTRIBUTING.md` | Nein |
| `{{说明}}` | Erläuterung des Branch-Modells | `Feat-Branches von main abzweigen` | Nein |
| `{{Conventional Commits 等}}` | Erläuterung der Commit-Konvention | `Conventional Commits` | Nein |
| `{{要求}}` | Anforderungen an Pull Requests | `Einzelne Änderung, Tests bestanden` | Nein |
| `{{年份}}` | Urheberrechtsjahr | `2026` | Ja |
| `{{著作权人}}` | Urheberrechtsinhaber | `Ntarstudio` | Ja |
| `{{SPDX 标识符}}` | SPDX-Kennung in der Copyright-Zeile | `MIT` | Ja |
| `{{许可证名称}}` | Vollständiger Lizenzname | `MIT` | Ja |

## 5. Hinweise zu optionalen Abschnitten

Abschnitt 3 enthält den kopierbaren Text der 20 Kapitel. Nachstehend folgen ergänzende Hinweise zum Hinzufügen und Entfernen je nach Projekttyp; beim Löschen eines Kapitels muss der zugehörige Link in der Startbildschirm-Navigation synchron entfernt werden.

| Abschnitt | Empfohlene Projekttypen | Bedingung für Entfernung |
| --- | --- | --- |
| Kernmerkmale | Alle | Ohne nachprüfbare Belege entfernbar, sofern keine qualitative Beschreibung als Ersatz dient |
| Entwurfsdetails und technische Abwägungen | Frameworks, Anwendungen, Dienste | Ohne wesentliche Abwägungen entfernbar |
| Technologie-Stack und Abhängigkeitsliste | Bibliotheken, Frameworks | Ohne externe Abhängigkeiten entfernbar |
| Leistungsverhalten | CLI, Bibliotheken, Dienste | Ohne Testdaten entfernbar, geschätzte Zahlen sind unzulässig |
| Sicherheit und Datenschutz | Dienste, Anwendungen, Projekte mit personenbezogenen Daten | Bei reinen lokalen Werkzeugen reduzierbar |
| Kompatibilität | Bibliotheken, SDKs, plattformübergreifende Anwendungen | Bei einer einzigen Laufzeitumgebung reduzierbar |
| Änderungsprotokoll | Alle | Nur wenn kein CHANGELOG existiert, durch eine eingebettete Änderungszusammenfassung ersetzen |
| Weitere Roadmap | Alle | Ohne öffentlichen Plan entfernbar |
| NOTICE-Konformitätserklärung | Mit Abhängigkeiten Dritter | Ohne Abhängigkeiten Dritter entfernbar |

## 6. Checkliste vor der Lieferung

- [ ] Keine zurückbleibenden `{{...}}`-Platzhalter.
- [ ] Der Startbildschirm enthält die Repository-Beschreibung 【Chinesisch | Englisch】 und Themen-Tags; beide stimmen mit den Repository-Metadaten überein.
- [ ] Die chinesische und die englische Repository-Beschreibung umfassen jeweils höchstens 120 Zeichen.
- [ ] Die Themen-Tags sind mit 20 Einträgen vollständig, durchgehend englische Kleinschreibung und mit `-` verbunden.
- [ ] Die Ein-Satz-Positionierung enthält ein Kategoriewort; im Chinesischen höchstens 60 Zeichen, im Englischen höchstens 25 Wörter.
- [ ] Jedes Kernmerkmal enthält die Fünf-Abschnitt-Struktur und nachprüfbare Belege.
- [ ] Stärken und Einschränkungen sind getrennt aufgeführt; Einschränkungen enthalten Auswirkungsbereich und Umgehung.
- [ ] Bekannte Probleme enthalten einen Tracking-Link; nicht implementierte Funktionen enthalten Grund und Planungsstatus.
- [ ] Die Roadmap ist mit „keine Zusage“ gekennzeichnet und enthält keine konkreten Liefertermine.
- [ ] Ungeeignete Szenarien und ausdrücklich nicht unterstützte Punkte sind aufgeführt.
- [ ] Die Hauptüberschrift ist eindeutig, die Ebenen der Unterüberschriften sind fortlaufend, und die Abschnittsreihenfolge entspricht den 20 Kapiteln der Spezifikation.
- [ ] Der Badge-Stil ist einheitlich, die Links sind gültig, und die alt-Texte sind eindeutig.
- [ ] Installationsbefehl und Schnellstart-Beispiel wurden getestet und sind lauffähig.
- [ ] Alle Codeblöcke sind mit einer Sprache gekennzeichnet, alle Bilder haben alt-Texte.
- [ ] Relative Pfade funktionieren in Forks und im Offline-Zustand.
- [ ] Die LICENSE ist vorhanden, die SPDX-Kennung stimmt mit der README überein.
- [ ] Die Kapitelreihenfolge der chinesischen und der englischen Fassung entspricht sich eins zu eins.

## Verwandte Dateien

- Vollständige Abschnittsdefinitionen siehe [README-Abschnittsspezifikation](./readme-sections-specification.md)
- Badge-Konfiguration siehe [Badge-Spezifikation](./badge-specification.md)
- Visuelle Vorgaben siehe [README-Spezifikation für visuelles Layout](./readme-visual-layout-specification.md)
- Typbezogene Auswahl siehe [README-Leitfaden zur Kategorieanpassung](./readme-category-adaptation-guide.md)
- Recherchegrundlage siehe [README-Vorlagen-Recherchebericht](./readme-template-research-report.md)
- Schreibweise für Merkmale und Abwägungen siehe [Leitfaden für Merkmale und technische Abwägungen](./features-and-engineering-tradeoffs-guide.md)
- Metadatenregeln siehe [Projekt-Namensspezifikation](./project-naming-specification.md)
- Roadmap-Regeln siehe [Roadmap-Spezifikation](./roadmap-specification.md)
