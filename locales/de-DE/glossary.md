# Glossar

> Problem, das diese Datei löst: Definiert zentral die im gesamten Projekt verwendeten Fachbegriffe und Abkürzungen, damit die chinesische und die englische Fassung eineindeutig einander zugeordnet und durchgängig einheitlich formuliert sind.

## 1. Pflegeregeln

1. Bei der ersten Nennung eines Begriffs ist eine Definition anzugeben, im Format „chinesischer Begriff (English Term, Abkürzung)“.
2. Für dasselbe Konzept wird im gesamten Text nur eine Formulierung verwendet; die chinesische und die englische Fassung sind eineindeutig einander zugeordnet und nutzen diese Tabelle gemeinsam.
3. Neue Begriffe sind gleichzeitig in diese Tabelle und an die entsprechende Stelle der englischen Fassung zu schreiben.
4. Eine Abkürzung ist bei der ersten Nennung auszuschreiben, danach darf die Abkürzung direkt verwendet werden.

## 2. Terminologietabelle

| Chinesisch | English | Abkürzung | Erläuterung |
| --- | --- | --- | --- |
| 软件物料清单 | Software Bill of Materials | SBOM | Vollständige Liste der Projektabhängigkeiten und -komponenten |
| 语义化版本 | Semantic Versioning | SemVer | Versionsnummernformat `MAJOR.MINOR.PATCH` |
| 架构决策记录 | Architecture Decision Record | ADR | Dokumentiert wichtige Architekturentscheidungen samt Kontext und Folgen |
| 行为准则 | Code of Conduct | CoC | Verhaltensregeln für Teilnehmende der Community |
| 持续集成 / 持续交付 | Continuous Integration / Continuous Delivery | CI/CD | Automatisierte Build-, Test- und Auslieferungsprozesse |
| 软件许可证标识符 | Software Package Data Exchange | SPDX | Standardisiertes Kennzeichnungssystem für Lizenzen |
| 最小可行产品 | Minimum Viable Product | MVP | Kleinste Version zur Validierung der Kernannahme |
| 自然语言处理 | Natural Language Processing | NLP | Technologien zur Textverarbeitung |
| 大模型 | Large Language Model | LLM | Großes vortrainiertes Sprachmodell |
| 模型上下文协议 | Model Context Protocol | MCP | Protokoll zur Verbindung von Modellen mit externen Werkzeugen |
| 待补充 | To Be Determined | TBD | Platzhalterkennzeichnung für noch nicht bestätigte Informationen |

> Die Einträge in der Tabelle sind allgemeine Beispiele und vor der Verwendung gemäß der tatsächlichen Projektterminologie zu ergänzen oder zu streichen.

## 3. Mehrsprachige Terminologiematrix

| Code | Sprache | SemVer | ADR | CoC | CI/CD | MCP | TBD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `zh-CN` | 简体中文 | 语义化版本 | 架构决策记录 | 行为准则 | 持续集成 | 模型上下文协议 | 待补充 |
| `zh-TW` | 繁體中文 | 語義化版本 | 架構決策記錄 | 行為準則 | 持續整合 | 模型上下文協議 | 待補充 |
| `en-US` | English | Semantic Versioning | Architecture Decision Record | Code of Conduct | Continuous Integration | Model Context Protocol | TBD |
| `ja-JP` | 日本語 | セマンティックバージョニング | アーキテクチャ決定記録 | 行動規範 | 継続的インテグレーション | モデルコンテキストプロトコル | 未定 |
| `ko-KR` | 한국어 | 시맨틱 버저닝 | 아키텍처 결정 기록 | 행동 강령 | 지속적 통합 | 모델 컨텍스트 프로토콜 | 미정 |
| `fr-FR` | Français | versionnage sémantique | décision d'architecture | code de conduite | intégration continue | protocole de contexte de modèle | À compléter |
| `de-DE` | Deutsch | semantische Versionierung | Architekturentscheidung | Verhaltenskodex | kontinuierliche Integration | Model Context Protocol | Zu ergänzen |
| `es-ES` | Español | versionado semántico | registros de decisión de arquitectura | código de conducta | integración continua | protocolo de contexto de modelo | pendiente |
| `pt-BR` | Português | versionamento semântico | registro de decisão de arquitetura | código de conduta | integração contínua | protocolo de contexto de modelo | pendente |
| `ru-RU` | Русский | семантическое версионирование | запись архитектурных решений | Кодекс поведения | непрерывная интеграция | протокол контекста модели | будет дополнено |
| `ar-SA` | العربية | الإصدار الدلالي | القرارات المعمارية | مدونة السلوك | التكامل المستمر | بروتوكول سياق النموذج | قيد الاستكمال |
| `hi-IN` | हिन्दी | सेमांटिक वर्ज़निंग | संरचना निर्णय | आचार संहिता | सतत एकीकरण | मॉडल संदर्भ प्रोटोकॉल | पूर्ति शेष |

- **Gängige Abkürzungen**: Werden im Text jeder Sprache unverändert verwendet und nie lokalisiert: SBOM, SPDX, ADR, SemVer, CoC, CI/CD, MVP, NLP, LLM, MCP, TBD.

Diese Tabelle legt je Begriff eine feste Übersetzung pro Sprache fest, die beim Hinzufügen einer Sprache oder bei einer globalen Ersetzung direkt herangezogen wird. Begriffe stehen in der Zitierform (Nominativ oder Infinitiv); im russischen und deutschen Fließtext werden sie flektiert, daher nach dem Stamm suchen.

Aufnahmekriterium: Nur Begriffe mit tatsächlichen Vorkommen im Fließtext werden aufgeführt, und jede Zelle unten ist im jeweiligen Sprachverzeichnis auffindbar. SBOM, MVP, NLP und LLM kommen im Fließtext aller zwölf Sprachen null Mal vor und existieren nur als Beispiele in der Zuordnungstabelle des vorigen Abschnitts; sie sind daher nicht in der Matrix enthalten. SPDX wird in jeder Sprache stets nur als Abkürzung verwendet, die Langform kommt nie vor, daher steht es oben in der Abkürzungszeile bei den übrigen Abkürzungen und erhält keine Übersetzungsspalte.

Beim Hinzufügen einer Sprache zuerst die Übersetzungen nach dieser Tabelle ergänzen und danach `python3 cli/gitrule.py xcheck --path . --reference zh-CN` ausführen, um die strukturelle Konsistenz zu prüfen.

## Verwandte Dateien

- Anforderungen an die Terminologiekonsistenz siehe [Allgemeine Schreibspezifikation](./general-writing-specification.md)
- Regeln zur gemeinsamen Nutzung zweisprachiger Termini siehe [Mehrsprachigkeits-Spezifikation](./multilingual-specification.md)
- Vorlage der Vergleichstabelle siehe [Informationserfassung und Vorlagen](./information-collection-and-templates.md)
