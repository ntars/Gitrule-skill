# Glossary

> What this file solves: Centrally defines the technical terms and abbreviations used throughout the project, ensuring one-to-one correspondence of terms between the Chinese and English versions and consistent expression throughout.

## 1. Maintenance Rules

1. A definition must be given when a term first appears, in the format "Chinese Term (English Term, Abbreviation)".
2. Use only one expression for the same concept throughout; the Chinese and English versions correspond one-to-one and share this table.
3. New terms must be added to this table and synchronized to the corresponding location in the English version.
4. When an abbreviation first appears, spell out the full name; afterward the abbreviation may be used directly.

## 2. Term Correspondence Table

| Chinese | English | Abbreviation | Description |
| --- | --- | --- | --- |
| 软件物料清单 | Software Bill of Materials | SBOM | Complete list of project dependencies and components |
| 语义化版本 | Semantic Versioning | SemVer | Version number format `MAJOR.MINOR.PATCH` |
| 架构决策记录 | Architecture Decision Record | ADR | Records important architecture decisions and their background and consequences |
| 行为准则 | Code of Conduct | CoC | Code of behavior for community participants |
| 持续集成 / 持续交付 | Continuous Integration / Continuous Delivery | CI/CD | Automated build, test, and delivery processes |
| 软件许可证标识符 | Software Package Data Exchange | SPDX | Standard identifier system for licenses |
| 最小可行产品 | Minimum Viable Product | MVP | The smallest version that can validate a core hypothesis |
| 自然语言处理 | Natural Language Processing | NLP | Technologies related to text processing |
| 大模型 | Large Language Model | LLM | Large-scale pretrained language model |
| 模型上下文协议 | Model Context Protocol | MCP | Protocol connecting models with external tools |
| 待补充 | To Be Determined | TBD | Placeholder marker for information not yet confirmed |

> The entries in this table are general examples; add or remove entries according to the project's actual terminology before use.

## 3. Multilingual Term Matrix

| Code | Language | SemVer | ADR | CoC | CI/CD | MCP | TBD |
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
| `hi-IN` | हिन्दी | SemVer | संरचना निर्णय अभिलेख | आचार संहिता | सतत एकीकरण | मॉडल संदर्भ प्रोटोकॉल | पूर्ति शेष |

- **Common abbreviations**: Used as-is in the body text of every language and never localized: SBOM, SPDX, ADR, SemVer, CoC, CI/CD, MVP, NLP, LLM, MCP, TBD.

This table fixes one rendering per term for each language, to be referenced directly when adding a language or performing a global replacement. Terms are given in citation form (nominative or infinitive); Russian and German running text inflects them, so search by stem.

Inclusion rule: only terms with real occurrences in the body text are listed, and every cell below is retrievable in that language directory. SBOM, MVP, NLP, and LLM occur zero times in the body text of all twelve languages and exist only as examples in the correspondence table of the previous section, so they are excluded from the matrix. SPDX is always used as the bare abbreviation in every language and its full form never occurs, so it appears in the abbreviation line above together with the others, with no rendering column.

When adding a language, fill in the renderings from this table first, then run `python3 cli/gitrule.py xcheck --path . --reference zh-CN` to verify structural consistency.

## Related Files

- For terminology consistency requirements, see [General Writing Specification](./general-writing-specification.md)
- For bilingual term-sharing rules, see [Multilingual Specification](./multilingual-specification.md)
- For the correspondence table template, see [Information Collection and Templates](./information-collection-and-templates.md)
