# Architekturdesign-Dokumentations-Spezifikation

> Problem, das diese Datei löst: Sie definiert Vorlage, Felder und Schreibweise der Architekturdokumentation und der Architekturentscheidungen (ADR), beschreibt Systemgrenzen, Modulverantwortlichkeiten, Qualitätsmerkmale und zentrale Abwägungen und stellt die Nachvollziehbarkeit von Entscheidungen sicher.

## 1. Spezifikationsregeln

1. Die Architekturdokumentation (`docs/architecture.md`) beschreibt ausschließlich Struktur und Grenzen und enthält keine Anwendungsbeispiele; die Abgrenzung der Zuständigkeiten ist in der [Dokumentmatrix](./document-matrix.md) festgelegt.
2. Jede wesentliche technische Entscheidung muss eine zugehörige ADR besitzen; Entscheidungen ohne ADR gelten als nicht dokumentiert.
3. ADR-Nummern sind fortlaufend und dauerhaft fest; einmal angenommen, wird die Historie nicht umgeschrieben, Statusänderungen werden durch eine neue ADR dokumentiert und mit „Ersetzt durch“ gekennzeichnet.
4. Die Architekturbeschreibung muss mit der Codeimplementierung übereinstimmen; bei Abweichungen gilt der Code, und die Dokumentation ist unverzüglich zu überarbeiten.
5. Jede Architekturentscheidung muss auf eine oder mehrere Anforderungen zurückführbar sein; die Verfolgungsbeziehung ist in der [Anforderungs-Verfolgungsmatrix-Spezifikation](./requirements-traceability-matrix-specification.md) beschrieben.
6. Für Qualitätsmerkmale sind überprüfbare Messziele anzugeben; Formulierungen wie „hohe Performance“ oder „hohe Verfügbarkeit“ allein sind unzulässig.

## 2. Vorlage der Architekturdokumentation

```markdown
# Architekturdesign: {{项目名称}}

Dokumentversion: {{v1.0}} ｜ Zugehörige Codeversion: {{tag}} ｜ Datum der letzten Prüfung: {{YYYY-MM-DD}}

## Systemkontext
- Systemverantwortung: {{一句话说明系统边界内的责任}}
- Externe Beteiligte: {{用户、上游系统、下游系统}}
- Ein- und Ausgaben: {{进入系统的请求与系统产出的结果}}
- Außerhalb der Grenze: {{明确不由本系统承担的职责}}

## Modulgliederung
| Modul | Einzige Verantwortlichkeit | Externe Schnittstelle | Abhängige Module | Nicht zuständig |
| --- | --- | --- | --- | --- |
| {{模块名}} | {{仅一件事}} | {{接口名}} | {{模块名}} | {{明确排除}} |

## Zentrale Datenflüsse
1. {{触发点}} → {{模块 A}}: {{传递的数据}}
2. {{模块 A}} → {{模块 B}}: {{转换与传递}}
3. {{模块 B}} → {{结果}}: {{最终产出}}

## Technologieauswahl
| Bereich | Auswahl | Alternativen | Entscheidungsgrundlage | ADR |
| --- | --- | --- | --- | --- |
| {{语言 / 框架 / 存储}} | {{采用项}} | {{未采用项}} | {{取舍理由}} | {{ADR-000N}} |

## Qualitätsmerkmale
| Merkmal | Zielwert | Nachweisverfahren | Zugehörige ADR |
| --- | --- | --- | --- |
| Performance | {{P95 延迟 < X ms}} | {{压测方式}} | {{ADR-000N}} |
| Verfügbarkeit | {{月度可用性 ≥ X%}} | {{监控统计}} | {{ADR-000N}} |
| Sicherheit | {{敏感数据零明文落盘}} | {{审计方式}} | {{ADR-000N}} |
| Skalierbarkeit | {{横向扩容至 N 节点无需改代码}} | {{扩容演练}} | {{ADR-000N}} |

## Randbedingungen und Abwägungen
- Technische Randbedingungen: {{语言版本、平台、兼容性}}
- Verworfene Ansätze und Gründe: {{方案 A：原因}}
- Bekannte technische Schulden: {{债务项与偿还条件}}
```

## 3. ADR-Vorlage

```markdown
# ADR-{{四位序号}}: {{决策标题}}

- Status: {{提议 / 已采纳 / 已废弃 / 被 ADR-000N 替代}}
- Datum: {{YYYY-MM-DD}}
- Entscheider: {{姓名}}
- Zugeordnete Anforderung: {{REQ-001 / …}}

## Kontext
{{面临的客观问题与约束，须可验证，不写主观偏好}}

## Entscheidung
{{采用的方案，一句话陈述，须明确到可执行的程度}}

## Alternativen
| Ansatz | Vorteile | Nachteile | Grund der Ablehnung |
| --- | --- | --- | --- |
| {{方案 A}} | | | |
| {{方案 B（采用）}} | | | — |

## Konsequenzen
- Positiv: {{获得的能力}}
- Negativ: {{引入的成本或限制}}
- Folgeaufgaben: {{需要跟进的事项}}

## Verwandte Dateien
- {{架构文档中受影响的章节}}
- {{替代或被引用的 ADR}}
```

## 4. Felddefinitionen

### 4.1 Felder der Architekturdokumentation

| Feld | Pflichtfeld | Typ | Hinweise zum Ausfüllen | Beispiel |
| --- | --- | --- | --- | --- |
| Zugehörige Codeversion | Ja | Tag | Muss mit dem Tag der [Versionsverwaltungs-Spezifikation](./version-management-specification.md) übereinstimmen | `v1.2.0` |
| Datum der letzten Prüfung | Ja | Datum | Nach jeder Codeänderung zu aktualisieren | `2026-11-18` |
| Einzige Verantwortlichkeit des Moduls | Ja | Text | Pro Modul genau eine Aufgabe | `Analyse und Validierung von Markdown-Regeln` |
| Nicht zuständig | Ja | Text | Klare Grenze, um Verantwortungsdrift zu vermeiden | `Keine Textumschreibung` |
| Technologieauswahl.Entscheidungsgrundlage | Ja | Text | Muss die ADR-Nummer referenzieren | `Siehe ADR-0002` |
| Qualitätsmerkmale.Zielwert | Ja | Messgröße | Mit Einheit und Schwellenwert, überprüfbar | `P95 < 150ms` |
| Bekannte technische Schulden | Nein | Liste | Auslösebedingung für den Abbau angeben | `Ersatz des Parsers in v2` |

### 4.2 ADR-Felder

| Feld | Pflichtfeld | Typ | Hinweise zum Ausfüllen | Beispiel |
| --- | --- | --- | --- | --- |
| Nummer | Ja | `ADR-NNNN` | Vierstellige Nummer, fortlaufend und dauerhaft fest | `ADR-0002` |
| Status | Ja | Aufzählung | Vorschlag / Angenommen / Verworfen / Ersetzt | `Angenommen` |
| Zugeordnete Anforderung | Ja | Liste | REQ-Nummer aus dem Projektstartdokument | `REQ-001` |
| Kontext | Ja | Text | Objektive Randbedingungen darstellen, „ich denke“ ist unzulässig | `Kompatibilität mit Node 18 erforderlich` |
| Entscheidung | Ja | Text | Ein Satz, ausführbar | `remark als Parser verwenden` |
| Alternativen | Ja | Tabelle | Mindestens 1 nicht gewählter Ansatz | Siehe Vorlage |
| Ablehnungsbegründung | Ja | Text | Für jeden nicht gewählten Ansatz anzugeben | Siehe Vorlage |
| Konsequenzen | Ja | Liste | Positiv, negativ und Folgeaufgaben vollständig | Siehe Vorlage |

## 5. Hinweise zum Ausfüllen

1. **Modulgliederung**: Enthält die „einzige Verantwortlichkeit“ einer Zeile zwei durch „und“ oder „sowie“ verbundene Aufgaben, ist sie in zwei Module aufzuteilen.
2. **Datenflüsse**: Chronologisch nummerieren, die übergebenen Daten benennen; reine Pfeile zwischen Modulnamen sind unzulässig.
3. **Qualitätsmerkmale**: Jedes Merkmal benötigt Zielwert, Nachweisverfahren und ADR-Referenz; fehlt eines davon, gilt der Eintrag als unvollständig.
4. **ADR-Kontext**: Problem und Randbedingungen beschreiben, nicht die Entscheidung selbst; die Entscheidung erscheint nur einmal im Abschnitt „Entscheidung“.
5. **Alternativen**: Auch bei nur einem Ansatz ist zu vermerken: „Eine Eigenimplementierung wurde geprüft und wegen zu hohem Wartungsaufwand verworfen“; ohne Alternative gilt die Begründung als unzureichend.
6. **Statusänderungen**: Der Text der ursprünglichen ADR wird nicht geändert; es wird eine neue ADR angelegt und der Status des Originals auf „Ersetzt durch ADR-000N“ gesetzt.
7. **Technische Schulden**: Die Auslösebedingung für den Abbau ist anzugeben; das bloße Auflisten von Symptomen ist unzulässig.

Häufige Fehler:

| Fehlerhafte Formulierung | Problem | Korrektur |
| --- | --- | --- |
| Architekturdokumentation enthält API-Aufrufbeispiele | Überschneidung mit der [API-Dokumentations-Spezifikation](./api-documentation-specification.md) | In die API-Dokumentation verschieben, in der Architektur nur Schnittstellennamen belassen |
| „Das System muss hohe Performance bieten“ | Kein Schwellenwert, nicht überprüfbar | Zielwert für P95-Latenz und Lasttestverfahren angeben |
| ADR enthält nur die Entscheidung, keine Alternativen | Nicht begründet | Mindestens 1 verworfene Alternative mit Grund ergänzen |
| Der Text einer angenommenen ADR wird geändert | Historie wird umgeschrieben | Neue ADR anlegen und Ersetzungsbeziehung kennzeichnen |
| Entscheidung lässt sich keiner Anforderung zuordnen | Verfolgungskette bricht | Zugeordnete REQ-Nummer ergänzen |

## 6. Vollständiges Beispiel

```markdown
# ADR-0002: remark als Markdown-Parsing-Schicht verwenden

- Status: Angenommen
- Datum: 2026-11-18
- Entscheider: Li Si
- Zugeordnete Anforderung: REQ-001, REQ-004

## Kontext
GFM und die Lokalisierung chinesischer Textknoten müssen unterstützt werden, die Laufzeitabhängigkeiten müssen mit Node 18 kompatibel sein; der Personalaufwand des Teams für die Pflege eines eigenen Parsers ist auf 0,5 Personenmonate pro Quartal begrenzt.

## Entscheidung
Das remark-Ökosystem wird als einzige Markdown-Parsing-Schicht verwendet, Regeln werden als Plugins implementiert.

## Alternativen
| Ansatz | Vorteile | Nachteile | Grund der Ablehnung |
| --- | --- | --- | --- |
| Eigenentwickelter Parser | Vollständig kontrollierbar | Langfristige Pflege von Randfällen erforderlich | Überschreitet den Personalrahmen |
| marked | Geringes Gewicht | Schwache Lokalisierung chinesischer Knoten | Erfüllt REQ-004 nicht |

## Konsequenzen
- Positiv: GFM-Kompatibilität wird upstream gepflegt, die Knotenlokalisierung erfüllt die Abnahmebedingungen.
- Negativ: Änderungen der Plugin-API erfordern die Nachführung von Upstream-Versionen.
- Folgeaufgaben: Hauptversion von remark in der CI fixieren und Release-Benachrichtigungen abonnieren.
```

## Verwandte Dateien

- Abgrenzung der Zuständigkeiten und unzulässige Inhalte: [Dokumentmatrix](./document-matrix.md)
- Rückverfolgung von Entscheidungen zu Anforderungen: [Anforderungs-Verfolgungsmatrix-Spezifikation](./requirements-traceability-matrix-specification.md)
- Externe Darstellung technischer Abwägungen: [Leitfaden zu Merkmalen und technischen Abwägungen](./features-and-engineering-tradeoffs-guide.md)
- Konventionen für das Schnittstellendesign: [API-Design-Spezifikation](./api-design-specification.md)
- Datenmodell und Migration: [Datenbankdesign-Spezifikation](./database-design-specification.md)
- Einheitliche Terminologie: [Glossar](./glossary.md)
