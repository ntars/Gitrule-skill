# Spezifikation für Projektstart und Anforderungen

> Problem, das diese Datei löst: Definiert Vorlagen und Felder für Zielformulierung, Anforderungserhebung und Scope-Abgrenzung in der Projektstartphase, damit ein Projekt von Beginn an über eine klare, überprüfbare und nachverfolgbare Grundlage verfügt.

## 1. Spezifikationsklauseln

1. Das Projektstartdokument muss sechs Fragen beantworten: Was ist es, warum wird es gemacht, in welchem Umfang wird es umgesetzt, für wen ist es nicht bestimmt, wer nutzt es, welchen Einschränkungen unterliegt es.
2. Anforderungen müssen die drei Stufen „muss / sollte / kann“ unterscheiden; die Sprachkonventionen siehe [Allgemeine Schreibspezifikation](./general-writing-specification.md).
3. Jede Anforderung muss überprüfbar sein: entweder Akzeptanzkriterien in Given/When/Then oder eine entscheidbare Messschwelle angeben.
4. Jede Anforderung muss eine stabile Nummer und eine Quelle besitzen; Anforderungseinträge ohne Nummer sind verboten.
5. Bei unzureichenden Informationen ist „【待确认：字段名】“ zu kennzeichnen; Raten ist unzulässig, Regeln siehe [Informationserhebung und Vorlagen](./information-collection-and-templates.md).
6. Der Scope muss sowohl einbezogene als auch ausgeschlossene Punkte nennen; leere Nicht-Ziele gelten als nicht abgegrenzter Scope.
7. Scope-Änderungen müssen Grund, Auswirkung und Entscheider festhalten und in die Änderungsaufzeichnung der [Spezifikation für die Anforderungs-Verfolgungsmatrix](./requirements-traceability-matrix-specification.md) eingehen.

## 2. Vorlage für das Projektstartdokument

```markdown
# Projektstartdokument：{{项目名称}}

Dokumentversion：{{v0.1}} ｜ Status：{{草稿 / 评审中 / 已批准}} ｜ Entscheider：{{姓名}} ｜ Datum：{{YYYY-MM-DD}}

## Positionierung in einem Satz
Bietet {{目标用户}} die {{核心能力}} und löst {{当前痛点}}.
(≤60 Zeichen; Eigenlob wie „leistungsstark“, „elegant“, „führend“ ist verboten)

## Hintergrund und Motivation
- Ausgangslage：{{当前如何运作}}
- Unzulänglichkeiten bestehender Lösungen：{{具体缺陷 1}}; {{具体缺陷 2}}
- Zeitfenster：{{时机、技术或市场变化}}
- Grundlage des Projektstarts：{{工单号 / 访谈记录 / 数据指标，须可溯源}}

## Ziele und Nicht-Ziele
| Typ | Eintrag | Überprüfbares Ergebnis |
| --- | --- | --- |
| Ziel G1 | {{要达成的结果}} | {{可量化指标 + 阈值}} |
| Ziel G2 | {{要达成的结果}} | {{可量化指标 + 阈值}} |
| Nicht-Ziel N1 | {{明确不做的事}} | {{判定边界，说明为何排除}} |

## Erfolgskriterien
| Kennzahl | Basiswert | Zielwert | Nachweisverfahren | Nachweiszeitpunkt |
| --- | --- | --- | --- | --- |
| {{指标名}} | {{当前值}} | {{目标值}} | {{如何测量}} | {{何时测量}} |

## Zielnutzer
| Nutzerrolle | Typisches Szenario | Kernbedarf | Aktuelle Ersatzlösung |
| --- | --- | --- | --- |
| {{角色}} | {{何时何地}} | {{要完成的任务}} | {{现用方案}} |

## Einschränkungen
- Technisch：{{语言、平台、兼容性等限制}}
- Zeitlich：{{截止日期或窗口}}
- Ressourcen：{{人力、预算、基础设施}}
- Compliance：{{许可证、隐私、行业规范}}

## Scope
- Einbezogen：{{本期交付项}}
- Ausgeschlossen：{{本期明确不交付项}}
- Zu bestätigen：{{【待确认：字段名】}}

## Entscheidungsaufzeichnung
| Datum | Entscheidung | Entscheider | Grundlage |
| --- | --- | --- | --- |
```

## 3. Vorlage für Anforderungseinträge

```markdown
### REQ-{{三位序号}}：{{需求标题}}

- Quelle：{{工单号 / 访谈 / 竞品 / 推测}}
- Priorität：{{必须 / 应当 / 可以}}
- Zugehöriges Ziel：{{G1 / G2 / …}}
- User Story：Als {{角色}} möchte ich {{行为}}, damit {{价值}}
- Akzeptanzkriterien：
  1. Given {{前置条件}}
     When {{操作}}
     Then {{预期结果}}
  2. Given {{边界或异常前置条件}}
     When {{操作}}
     Then {{预期结果}}
- Status：{{待确认 / 已确认 / 已实现 / 已验证 / 已废弃}}
- Zugehörige Verfolgung：{{见需求追踪矩阵中的需求 ID}}
```

## 4. Felddefinitionen

### 4.1 Felder des Projektstartdokuments

| Feld | Pflicht | Typ | Ausfüllhinweise | Beispiel |
| --- | --- | --- | --- | --- |
| Dokumentversion | ja | Text | Semantische Version oder Datumsversion | `v0.1` |
| Status | ja | Enumeration | Entwurf / in Prüfung / genehmigt | `评审中` |
| Entscheider | ja | Text | Person mit letzter Entscheidungsbefugnis über Scope und Prioritäten | `张三` |
| Positionierung in einem Satz | ja | Text | Zielnutzer + Kernfähigkeit + Problem, ≤60 Zeichen | Für Frontend-Entwickler bieten … |
| Grundlage des Projektstarts | ja | Text | mindestens eine nachverfolgbare Aufzeichnung, „Teamentscheidung“ ist verboten | `ISSUE-142` |
| Ziele / Nicht-Ziele | ja | Tabelle | jedem Ziel ein überprüfbares Ergebnis zuordnen; mindestens ein Nicht-Ziel | `G1：冷启动 <2s` |
| Erfolgskriterien | ja | Tabelle | Kennzahl muss Basiswert, Schwelle, Messverfahren und Zeitpunkt haben | `错误率 <0.1%` |
| Einschränkungen | ja | Liste | alle vier Kategorien ausfüllen, sonst „keine“ schreiben | `须兼容 Node 18+` |
| Zu bestätigen | nein | Liste | nur im Format 【待确认：字段名】 | `【待确认：预算上限】` |

### 4.2 Felder von Anforderungseinträgen

| Feld | Pflicht | Typ | Ausfüllhinweise | Beispiel |
| --- | --- | --- | --- | --- |
| Nummer | ja | `REQ-NNN` | dreistellige laufende Nummer, fortlaufend, nicht wiederverwendet, nicht umsortiert | `REQ-007` |
| Quelle | ja | Text | auf eine konkrete Aufzeichnung zurückführbar | `用户访谈 #3` |
| Priorität | ja | Enumeration | muss / sollte / kann | `必须` |
| Zugehöriges Ziel | ja | Liste | entsprechende G-Nummer des Projektstartdokuments | `G1` |
| User Story | ja | Text | alle drei Elemente Rolle + Verhalten + Nutzen | Als … möchte ich … damit … |
| Akzeptanzkriterien | ja | Liste | mindestens 1 Given/When/Then-Gruppe, muss Randfall oder Ausnahme enthalten | siehe Vorlage |
| Status | ja | Enumeration | einer von fünf Zuständen, nur vorwärts, kein Rückschritt | `已确认` |

## 5. Ausfüllhinweise

1. **Positionierung in einem Satz**: nach dem dreiteiligen Schema „für wen + was bieten + was lösen“ schreiben; ergibt der Satz nach Streichung der Ausschmückungen keinen Sinn, fehlen wesentliche Informationen.
2. **Erfolgskriterien**: jeder Punkt muss Basiswert und Schwelle zugleich aufweisen. „Leistung steigern“ und „bessere Erfahrung“ gelten als unzureichend und sind in „P95-Startzeit von 3 s auf <1,5 s senken“ zu ändern.
3. **Nicht-Ziele**: ausdrücklich ausgeschlossenen Scope und Abgrenzungskriterien benennen, nicht „später“; ohne nicht-leeres Nicht-Ziel gilt der Scope als nicht abgegrenzt.
4. **Anforderungsnummer**: nach Zuweisung dauerhaft fest; bei Verwerfung einer Anforderung wird der Status auf „verworfen“ geändert, die Nummer darf nicht zurückgezogen oder wiederverwendet werden.
5. **Akzeptanzkriterien**: müssen den Normalfall und mindestens einen Rand- oder Ausnahmefall abdecken; nicht objektiv entscheidbare Kriterien (etwa „schöne Oberfläche“) sind in überprüfbare Messgrößen oder Prüfpunkte zu überführen.
6. **Zu bestätigende Punkte**: im Projektstart sind zu bestätigende Punkte zulässig, müssen aber vollständig aufgelistet und mit bestätigender Person versehen sein; vor Entwicklungsbeginn müssen sie auf null stehen.

Häufige Fehler:

| Fehlerhafte Schreibweise | Problem | Korrektur |
| --- | --- | --- |
| „Ein gut nutzbares Werkzeug bauen“ | kein Zielnutzer, kein überprüfbares Ergebnis | Nutzerrolle und Schwellenwert ergänzen |
| Nicht-Ziel mit „keine“ | Scope nicht abgegrenzt, neigt zur Ausweitung | ausdrücklich ausgeschlossene Punkte der Periode aufführen |
| Anforderung ohne Nummer, direkt im Text beschrieben | nicht verfolgbar und referenzierbar | `REQ-NNN` zuweisen und bereichsweit referenzieren |
| Akzeptanzkriterium „Funktion normal“ | nicht entscheidbar | in Given/When/Then aufteilen |
| Vermutungen als feststehende Anforderung | Quelle nicht nachvollziehbar | Quelle als „Vermutung“ kennzeichnen und in zu bestätigen überführen |

## 6. Vollständiges Beispiel

```markdown
# Projektstartdokument：markdown-lint-cli

Dokumentversion：v0.1 ｜ Status：in Prüfung ｜ Entscheider：李四 ｜ Datum：2026-11-18

## Positionierung in einem Satz
Bietet chinesischsprachigen technischen Autorinnen und Autoren ein Kommandozeilenwerkzeug zur Prüfung von Markdown-Konventionen und löst das Problem uneinheitlicher Dokumentationsstile über mehrere Repositories ohne automatische Prüfung.

## Hintergrund und Motivation
- Ausgangslage：Die READMEs von 12 Repositories werden von den jeweiligen Maintainern handschriftlich verfasst, der Stil ist uneinheitlich.
- Unzulänglichkeiten bestehender Lösungen：gängige englische Lint-Werkzeuge unterstützen die Regel für Leerzeichen zwischen chinesischen und englischen Zeichen nicht; manuelle Reviews dauern im Schnitt 25 Minuten pro Dokument.
- Zeitfenster：Das Team vereinheitlicht derzeit die Open-Source-Startseite und muss die Konventionen einmalig umsetzen.
- Grundlage des Projektstarts：ISSUE-142, Protokoll des Dokumentenreviews vom 2026-11-10.

## Ziele und Nicht-Ziele
| Typ | Eintrag | Überprüfbares Ergebnis |
| --- | --- | --- |
| Ziel G1 | 8 Arten von Formatproblemen automatisch prüfen | Trefferquote ≥95 % bei 50 Beispieldokumenten |
| Ziel G2 | Laufzeit einer einzelnen Prüfung beherrschbar | Prüfung eines Dokuments mit 1000 Zeilen <2 s |
| Nicht-Ziel N1 | keine inhaltliche Textüberarbeitung | nur Ausgabe der Fundstellen der Regeln, keine Textänderung |

## Erfolgskriterien
| Kennzahl | Basiswert | Zielwert | Nachweisverfahren | Nachweiszeitpunkt |
| --- | --- | --- | --- | --- |
| Dauer des manuellen Reviews | 25 Minuten/Dokument | <5 Minuten/Dokument | kontrolliertes Experiment mit 5 Maintainern | vor Veröffentlichung von v1.0 |

### REQ-001：Leerzeichen bei gemischt chinesisch-englischem Satz prüfen
- Quelle：ISSUE-142
- Priorität：muss
- Zugehöriges Ziel：G1
- User Story：Als Dokumentations-Maintainer möchte ich fehlende Leerzeichen zwischen chinesischen und englischen Zeichen automatisch markiert bekommen, damit das Layout einheitlich ist.
- Akzeptanzkriterien：
  1. Given Das Dokument enthält „使用Node.js开发“
     When die Prüfung ausgeführt wird
     Then Zeilennummer und Hinweis „中英文间缺少空格“ ausgeben
  2. Given An dieser Stelle enthält das Dokument bereits ein Leerzeichen
     When die Prüfung ausgeführt wird
     Then keinen Treffer dieser Regel ausgeben
- Status：bestätigt
```

## Verwandte Dateien

- Verfolgung von Anforderungen zu Design, Tests und Veröffentlichung: [Spezifikation für die Anforderungs-Verfolgungsmatrix](./requirements-traceability-matrix-specification.md)
- Informationsfelder und Kennzeichnung fehlender Angaben: [Informationserhebung und Vorlagen](./information-collection-and-templates.md)
- Phasengliederung und Eintrittsbedingungen: [Ausführungsprozess](./execution-process.md)
- Benennung erfolgt nach Festlegung des Projektstartergebnisses: [Projektbenennungsspezifikation](./project-naming-specification.md)
- Externe Erläuterung von Scope-Änderungen: [Änderungsprotokoll-Spezifikation](./changelog-specification.md)
