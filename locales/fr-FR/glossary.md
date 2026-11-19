# Glossaire

> Problème que ce fichier résout : définir de manière centralisée les termes techniques et abréviations employés dans l'ensemble du projet, afin de garantir une correspondance biunivoque des termes entre les versions chinoise et anglaise et une formulation homogène dans tout le document.

## 1. Règles de maintenance

1. Un terme doit être défini lors de sa première apparition, au format « terme chinois (English Term, abréviation) ».
2. Un même concept n'utilise qu'une seule formulation dans tout le document ; les termes des versions chinoise et anglaise se correspondent un à un et partagent ce tableau.
3. Tout nouveau terme doit être ajouté à ce tableau et reporté à l'emplacement correspondant de la version anglaise.
4. Une abréviation doit être développée en toutes lettres lors de sa première apparition ; l'abréviation seule peut ensuite être utilisée.

## 2. Tableau de correspondance terminologique

| 中文 | English | 缩写 | 说明 |
| --- | --- | --- | --- |
| 软件物料清单 | Software Bill of Materials | SBOM | Liste complète des dépendances et composants du projet |
| 语义化版本 | Semantic Versioning | SemVer | Format de numéro de version `MAJOR.MINOR.PATCH` |
| 架构决策记录 | Architecture Decision Record | ADR | Consigne une décision d'architecture importante, son contexte et ses conséquences |
| 行为准则 | Code of Conduct | CoC | Règles de comportement des participants à la communauté |
| 持续集成 / 持续交付 | Continuous Integration / Continuous Delivery | CI/CD | Processus automatisés de build, de test et de livraison |
| 软件许可证标识符 | Software Package Data Exchange | SPDX | Système d'identifiants normalisés pour les licences |
| 最小可行产品 | Minimum Viable Product | MVP | Version minimale permettant de valider les hypothèses centrales |
| 自然语言处理 | Natural Language Processing | NLP | Technologies liées au traitement de texte |
| 大模型 | Large Language Model | LLM | Grand modèle de langage préentraîné |
| 模型上下文协议 | Model Context Protocol | MCP | Protocole reliant les modèles aux outils externes |
| 待补充 | To Be Determined | TBD | Marqueur d'espace réservé pour une information non encore confirmée |

> Les entrées de ce tableau sont des exemples génériques ; elles doivent être complétées ou réduites selon la terminologie réelle du projet avant utilisation.

## 3. Matrice des termes multilingues

| Code | Langue | SemVer | ADR | CoC | CI/CD | MCP | TBD |
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

- **Abréviations courantes**: Employées telles quelles dans le texte de chaque langue et jamais localisées : SBOM, SPDX, ADR, SemVer, CoC, CI/CD, MVP, NLP, LLM, MCP, TBD.

Ce tableau fixe une traduction par terme et par langue, à référencer directement lors de l'ajout d'une langue ou d'un remplacement global. Les termes sont donnés sous leur forme de citation (nominatif ou infinitif) ; le russe et l'allemand les fléchissent dans le corps du texte, il faut donc chercher par radical.

Critère d'inclusion : seuls les termes réellement présents dans le corps du texte sont listés, et chaque cellule ci-dessous est retrouvable dans le répertoire de la langue concernée. SBOM, MVP, NLP et LLM n'y apparaissent aucune fois dans les douze langues et n'existent que comme exemples dans le tableau de correspondance de la section précédente ; ils sont donc exclus de la matrice. SPDX s'emploie toujours sous sa seule abréviation dans chaque langue et sa forme développée n'apparaît jamais : il figure donc dans la ligne d’abréviations ci-dessus avec les autres, sans colonne de traduction.

Lors de l'ajout d'une langue, complétez d'abord les traductions d'après ce tableau, puis exécutez `python3 cli/gitrule.py xcheck --path . --reference zh-CN` pour vérifier la cohérence structurelle.

## Fichiers associés

- Exigences de cohérence terminologique : voir la [spécification générale de rédaction](./general-writing-specification.md)
- Règles de partage des termes bilingues : voir la [spécification multilingue](./multilingual-specification.md)
- Gabarit du tableau de correspondance : voir la [collecte d'informations et gabarits](./information-collection-and-templates.md)
