# Test-Spezifikation

> Problem, das diese Datei löst: Sie definiert Testebenen, Vorlagen und Felder für Testplan und Testfälle, die Grundlage der Abdeckungsmessung sowie Ausführungskriterien, damit jede Anforderung überprüfbar und jede Änderung regressionsfähig bleibt.

## 1. Spezifikationsregeln

1. Tests werden in die drei Ebenen Unit, Integration und End-to-End gegliedert; für jede Ebene sind Prüfobjekt und nicht geprüfter Bereich zu benennen, um Mehrfachabdeckung zu vermeiden.
2. Jede Anforderung der Stufe „Muss“ muss mindestens einem Testfall zugeordnet sein; die Verfolgungsbeziehung ist in der [Anforderungs-Verfolgungsmatrix-Spezifikation](./requirements-traceability-matrix-specification.md) beschrieben.
3. Bei der Behebung von Defekten ist zuerst ein Regressionstestfall zu ergänzen, danach der Code zu ändern; der Regressionstestfall muss den ursprünglichen Defekt reproduzieren können.
4. Die Abdeckungsschwelle wird projektbezogen festgelegt und in die CI übernommen; sie darf den festgelegten Wert nicht unterschreiten (entspricht der harten Regel H9).
5. Tests müssen wiederholbar sein und dürfen nicht von externem Zustand abhängen; bei Abhängigkeit von externen Diensten sind diese zu isolieren oder zu mocken.
6. Testnamen müssen das geprüfte Verhalten und das erwartete Ergebnis ausdrücken; Tests, Lint, Formatierung und Typprüfung sind in der CI automatisch auszuführen, erst bei vollständig grünem Ergebnis ist eine Zusammenführung zulässig (siehe [Code-Review-Spezifikation](./code-review-specification.md)).

## 2. Testebenen

| Ebene | Prüfobjekt | Muss abgedeckt werden | Nicht abgedeckt | Typische Werkzeuge |
| --- | --- | --- | --- | --- |
| Unit-Test | Funktionen, rein logische Module | Kernlogik, Grenzbedingungen, Ausnahmezweige | Modulübergreifende Zusammenarbeit, externe E/A | Sprachspezifischer Runner |
| Integrationstest | Zusammenarbeit zwischen Modulen | Zentrale Aufrufketten, Adapter, Persistenzinteraktion | Vollständige Nutzerabläufe | Testcontainer / Mock-Server |
| End-to-End-Test | Vollständige Nutzerszenarien | Hauptnutzungspfade, zentrale Geschäftszyklen | Vollständige Zweigabdeckung, Lasttests | Browser- / CLI-Treiber |

## 3. Vorlage des Testplans

```markdown
# Testplan: {{项目名称}} {{版本号}}

Version: {{v1.0}} ｜ Zugehöriger Anforderungsumfang: {{REQ-001 ~ REQ-020}} ｜ Verantwortlich: {{姓名}}

## Testumfang
- Enthalten: {{模块 / 需求编号列表}}
- Ausgeschlossen: {{不在本期验证的范围及原因}}
- Zugehörige Erfolgskriterien des Projektstarts: {{G1 / G2}}

## Ebenenstrategie
| Ebene | Prüfobjekt | Abdeckungsziel | Werkzeug | Ausführungszeitpunkt |
| --- | --- | --- | --- | --- |
| Unit | {{对象}} | {{覆盖率阈值}} | {{工具}} | Jeder Commit |
| Integration | {{对象}} | {{关键链路清单}} | {{工具}} | Jede Zusammenführung |
| End-to-End | {{场景}} | {{主要路径清单}} | {{工具}} | Jede Veröffentlichung |

## Umgebung und Daten
- Umgebung: {{操作系统 / 运行时版本 / 依赖服务版本}}
- Testdaten: {{构造方式；禁止使用生产敏感数据}}
- Externe Abhängigkeiten: {{需 mock 的服务及隔离方式}}

## Ein- und Austrittskriterien
- Eintritt: {{进入测试的前置条件，如开发自测通过}}
- Austritt: {{通过率 100%、无 P0/P1 缺陷、覆盖率达标}}
- Abbruchbedingungen: {{阻塞性问题清单}}

## Risiken und Abwägungen
- Nicht getesteter Umfang und Begründung: {{例如第三方付费接口以 mock 替代}}
- Bekannte Risiken: {{例如并发场景仅做 10 路验证}}
```

## 4. Vorlage für Testfälle

```markdown
### TC-{{三位序号}}: {{用例标题}}

- Zugeordnete Anforderung: {{REQ-001}}
- Ebene: {{单元 / 集成 / 端到端}}
- Priorität: {{P0 / P1 / P2}}
- Typ: {{正常 / 边界 / 异常}}
- Vorbedingungen: {{环境与数据准备}}
- Schritte und Erwartungen:
  | Schritt | Aktion | Erwartetes Ergebnis |
  | --- | --- | --- |
  | 1 | {{操作}} | {{可判定的结果}} |
  | 2 | {{操作}} | {{可判定的结果}} |
- Bereinigung: {{恢复环境的操作；无则写「无」}}
```

## 5. Felddefinitionen

### 5.1 Felder des Testplans

| Feld | Pflichtfeld | Typ | Hinweise zum Ausfüllen | Beispiel |
| --- | --- | --- | --- | --- |
| Zugehöriger Anforderungsumfang | Ja | Liste | REQ-Nummernbereich verwenden | `REQ-001 ~ REQ-020` |
| Ausgeschlossener Umfang | Ja | Text | Grund für den Ausschluss angeben | `Kein Test der kostenpflichtigen Schnittstelle: kein Testkonto` |
| Abdeckungsziel | Ja | Schwellenwert | Abdeckung als Zahlenprozent | `Zeilenabdeckung ≥80%` |
| Ausführungszeitpunkt | Ja | Aufzählung | Commit / Zusammenführung / Veröffentlichung | `Jede Zusammenführung` |
| Testdaten | Ja | Text | Konstruktionsweise angeben, echte sensible Daten unzulässig | `Erzeugung über Fixture` |
| Austrittskriterien | Ja | Text | Beurteilbar, mit Schwellenwert für Defektstufen | `Keine offenen Defekte der Stufe P0/P1` |

### 5.2 Felder von Testfällen

| Feld | Pflichtfeld | Typ | Hinweise zum Ausfüllen | Beispiel |
| --- | --- | --- | --- | --- |
| Nummer | Ja | `TC-NNN` | Fortlaufend, keine Wiederverwendung | `TC-007` |
| Zugeordnete Anforderung | Ja | Liste | Mindestens eine REQ-Nummer | `REQ-001` |
| Priorität | Ja | Aufzählung | P0 / P1 / P2 | `P0` |
| Typ | Ja | Aufzählung | Normal / Grenzfall / Ausnahme | `Grenzfall` |
| Schritte und Erwartungen | Ja | Tabelle | Jeder Schritt braucht eine beurteilbare Erwartung | Siehe Vorlage |
| Bereinigung | Ja | Text | Ohne Bereinigung „Keine“ schreiben, nicht leer lassen | `Keine` |

### 5.3 Grundlage der Abdeckungsmessung

| Grundlage | Definition | Geltende Ebene | Empfohlene Schwelle |
| --- | --- | --- | --- |
| Zeilenabdeckung | Ausgeführte Anweisungen / Gesamtanweisungen | Unit | ≥80% |
| Zweigabdeckung | Ausgeführte Zweige / Gesamtzweige | Unit | ≥70% |
| Anforderungsabdeckung | Anforderungen der Stufe „Muss“ mit Testfall / Gesamtzahl der Anforderungen der Stufe „Muss“ | Alle Ebenen | 100% |
| Pfadabdeckung | Verifizierte Hauptpfade / Identifizierte Hauptpfade | End-to-End | 100% |

Hinweis zur Messgrundlage: Abdeckung ist ein Mittel zum Auffinden ungetesteter Bereiche, kein Qualitätsziel an sich; hohe Abdeckung ersetzt keine Assertion-Qualität, Assertions müssen Verhalten prüfen und nicht nur Code ausführen.

## 6. Hinweise zum Ausfüllen

1. **Zugeordnete Anforderung**: Eine REQ-Nummer ist anzugeben; nicht zuordenbare Fälle sind in die Aufzeichnung explorativer Tests zu überführen und nicht in den offiziellen Testsatz aufzunehmen.
2. **Erwartetes Ergebnis**: Muss beurteilbar sein. „Gibt das korrekte Ergebnis zurück“ ist unzureichend; „Gibt Statuscode 200 zurück und das Feld `name` ist nicht leer“ ist zulässig.
3. **Verteilung der Typen**: Zu jeder Anforderung der Stufe „Muss“ gehören mindestens ein Normalfall und ein Grenzfall oder Ausnahmefall.
4. **Bereinigung**: Testfälle mit Bezug auf Dateien, Datenbanken oder globalen Zustand müssen Bereinigungsschritte enthalten; ohne Bereinigung gilt der Fall als unvollständig.
5. **Regressionstests**: Bei der Defektbehebung ist der Defektnummer als Präfix zu verwenden, zum Beispiel `TC-007-regression-142`.
6. **Isolation**: Testfälle dürfen nicht von der Ausführungsreihenfolge abhängen; gemeinsam genutzter Zustand ist in den Vorbedingungen neu aufzubauen.

Häufige Fehler:

| Fehlerhafte Formulierung | Problem | Korrektur |
| --- | --- | --- |
| Erwartung lautet „Funktion normal“ | Nicht beurteilbar | Konkreten Rückgabewert oder Status angeben |
| Testfall ohne zugeordnete Anforderung | Verfolgungskette bricht | REQ-Nummer ergänzen |
| Nur der Normalfall wird getestet | Grenzfalldefekte bleiben unentdeckt | Ausnahme- und Grenzfälle ergänzen |
| Testfall hängt vom Ergebnis des vorherigen ab | Nicht wiederholbar | Zustand in den Vorbedingungen neu aufbauen |
| Tests mit Produktivdaten | Datenschutz- und Compliance-Risiko | Auf Fixtures umstellen |

## 7. Vollständiges Beispiel

```markdown
# Testplan: markdown-lint-cli v1.0

Version: v1.0 ｜ Zugehöriger Anforderungsumfang: REQ-001 ~ REQ-014 ｜ Verantwortlich: Wang Wu

## Testumfang
- Enthalten: Regel-Engine, CLI-Parameteranalyse, Berichtsausgabe (REQ-001 ~ REQ-014)
- Ausgeschlossen: Integration in Editor-Plugins (auf v1.1 verschoben, keine zugehörige Anforderung)
- Zugehörige Erfolgskriterien des Projektstarts: G1, G2

## Ebenenstrategie
| Ebene | Prüfobjekt | Abdeckungsziel | Werkzeug | Ausführungszeitpunkt |
| --- | --- | --- | --- | --- |
| Unit | Regelfunktionen | Zeilenabdeckung ≥85% | Sprachspezifischer Runner | Jeder Commit |
| Integration | CLI → Regel-Engine → Bericht | 3 zentrale Ketten | Testcontainer | Jede Zusammenführung |
| End-to-End | Stapelprüfung echter Repositories | 2 Hauptpfade | Shell-Treiber | Jede Veröffentlichung |

### TC-001: Fehlendes Leerzeichen zwischen chinesischem und englischem Text wird erkannt
- Zugeordnete Anforderung: REQ-001
- Ebene: Unit
- Priorität: P0
- Typ: Grenzfall
- Vorbedingungen: Regel `spacing` geladen
- Schritte und Erwartungen:
  | Schritt | Aktion | Erwartetes Ergebnis |
  | --- | --- | --- |
  | 1 | Eingabe „使用Node.js开发“ | 1 Treffer, Zeile 1 |
  | 2 | Eingabe „使用 Node.js 开发“ | 0 Treffer |
- Bereinigung: Keine
```

## Verwandte Dateien

- Bidirektionale Verfolgung von Anforderungen zu Testfällen: [Anforderungs-Verfolgungsmatrix-Spezifikation](./requirements-traceability-matrix-specification.md)
- Ebenengrundlagen und Kennzahlendefinitionen: [Qualitätskennzahlen-Spezifikation](./quality-metrics-specification.md)
- Eintritts-Qualitätstor: [Qualitätstor](./quality-gate.md)
- Prüfungsdimension D6: [Prüfungsdimensionsmatrix](./review-dimension-matrix.md)
- Automatische Ausführung in der CI: [CI-Workflow-Spezifikation](./ci-workflow-specification.md)
- Lokale Ausführung vor dem Commit: [Push- und Veröffentlichungs-Spezifikation](./push-and-release-specification.md)
