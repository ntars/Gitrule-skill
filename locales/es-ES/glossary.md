# Glosario

> Problema que resuelve este archivo: define de forma centralizada los términos técnicos y las abreviaturas usados en todo el proyecto, garantizando la correspondencia uno a uno de los términos entre las versiones china e inglesa y la coherencia de la expresión en todo el texto.

## 1. Reglas de mantenimiento

1. La primera vez que aparece un término debe darse su definición, con el formato «término en chino (English Term, abreviatura)».
2. Un mismo concepto usa una sola expresión en todo el texto; los términos de las versiones china e inglesa se corresponden uno a uno y comparten esta tabla.
3. Todo término nuevo debe añadirse a esta tabla y sincronizarse en la posición correspondiente de la versión en inglés.
4. La primera vez que aparece una abreviatura debe desarrollarse su forma completa; después puede usarse directamente la abreviatura.

## 2. Tabla de correspondencia de términos

| Chino | English | Abreviatura | Descripción |
| --- | --- | --- | --- |
| 软件物料清单 | Software Bill of Materials | SBOM | Inventario completo de dependencias y componentes del proyecto |
| 语义化版本 | Semantic Versioning | SemVer | Formato del número de versión `MAJOR.MINOR.PATCH` |
| 架构决策记录 | Architecture Decision Record | ADR | Registra las decisiones arquitectónicas importantes, su contexto y sus consecuencias |
| 行为准则 | Code of Conduct | CoC | Normas de conducta de los participantes de la comunidad |
| 持续集成 / 持续交付 | Continuous Integration / Continuous Delivery | CI/CD | Proceso automatizado de compilación, pruebas y entrega |
| 软件许可证标识符 | Software Package Data Exchange | SPDX | Sistema de identificadores estándar de licencias |
| 最小可行产品 | Minimum Viable Product | MVP | Versión mínima capaz de validar la hipótesis central |
| 自然语言处理 | Natural Language Processing | NLP | Tecnologías relacionadas con el procesamiento de texto |
| 大模型 | Large Language Model | LLM | Modelo de lenguaje preentrenado a gran escala |
| 模型上下文协议 | Model Context Protocol | MCP | Protocolo que conecta modelos con herramientas externas |
| 待补充 | To Be Determined | TBD | Marca de posición para información aún no confirmada |

> Las entradas de la tabla son ejemplos genéricos; antes de usarlas deben añadirse o eliminarse según la terminología real del proyecto.

## 3. Matriz de términos multilingües

| Código | Idioma | SemVer | ADR | CoC | CI/CD | MCP | TBD |
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

- **Abreviaturas comunes**: Se usan tal cual en el cuerpo del texto de cada idioma y nunca se localizan: SBOM, SPDX, ADR, SemVer, CoC, CI/CD, MVP, NLP, LLM, MCP, TBD.

Esta tabla fija una traducción por término y por idioma, para citarla directamente al añadir un idioma o al hacer un reemplazo global. Los términos se dan en forma de cita (nominativo o infinitivo); el ruso y el alemán los flexionan en el cuerpo del texto, así que conviene buscar por raíz.

Criterio de inclusión: solo se listan los términos con apariciones reales en el cuerpo del texto, y cada celda de abajo se localiza en el directorio de ese idioma. SBOM, MVP, NLP y LLM no aparecen ninguna vez en el cuerpo del texto de los doce idiomas y solo existen como ejemplos en la tabla de correspondencia de la sección anterior, por lo que quedan excluidos de la matriz. SPDX se usa siempre como abreviatura escueta en todos los idiomas y su forma completa nunca aparece, así que figura en la línea de abreviaturas de arriba junto a las demás, sin columna de traducción.

Al añadir un idioma, complete primero las traducciones según esta tabla y después ejecute `python3 cli/gitrule.py xcheck --path . --reference zh-CN` para verificar la coherencia estructural.

## Archivos relacionados

- Para los requisitos de coherencia terminológica, véase la [especificación general de redacción](./general-writing-specification.md)
- Para las reglas de uso compartido de términos bilingües, véase la [especificación de multilenguaje](./multilingual-specification.md)
- La plantilla de la tabla de correspondencia se encuentra en [recopilación de información y plantillas](./information-collection-and-templates.md)
