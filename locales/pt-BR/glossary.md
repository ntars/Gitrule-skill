# Glossário

> Problema que este arquivo resolve: definir de forma centralizada os termos técnicos e as abreviações usadas em todo o projeto, garantindo correspondência um a um entre as versões em chinês e em inglês e uniformidade de expressão em todo o texto.

## 1. Regras de manutenção

1. Na primeira ocorrência de um termo, deve ser apresentada sua definição, no formato “termo em chinês (English Term, abreviação)”.
2. Um mesmo conceito usa apenas uma expressão em todo o texto; os termos das versões em chinês e em inglês correspondem um a um e compartilham esta tabela.
3. Termos novos devem ser acrescentados a esta tabela e sincronizados na posição correspondente da versão em inglês.
4. Na primeira ocorrência de uma abreviação, deve ser apresentada a forma completa; depois disso, a abreviação pode ser usada diretamente.

## 2. Tabela de correspondência de termos

| Chinês | English | Abreviação | Descrição |
| --- | --- | --- | --- |
| 软件物料清单 | Software Bill of Materials | SBOM | Lista completa das dependências e componentes do projeto |
| 语义化版本 | Semantic Versioning | SemVer | Formato do número de versão `MAJOR.MINOR.PATCH` |
| 架构决策记录 | Architecture Decision Record | ADR | Registra decisões arquiteturais importantes, seu contexto e suas consequências |
| 行为准则 | Code of Conduct | CoC | Código de conduta dos participantes da comunidade |
| 持续集成 / 持续交付 | Continuous Integration / Continuous Delivery | CI/CD | Fluxo automatizado de build, testes e entrega |
| 软件许可证标识符 | Software Package Data Exchange | SPDX | Sistema de identificadores padrão de licenças |
| 最小可行产品 | Minimum Viable Product | MVP | Versão mínima capaz de validar a hipótese central |
| 自然语言处理 | Natural Language Processing | NLP | Tecnologias relacionadas ao processamento de texto |
| 大模型 | Large Language Model | LLM | Modelo de linguagem de grande porte pré-treinado |
| 模型上下文协议 | Model Context Protocol | MCP | Protocolo que conecta modelos a ferramentas externas |
| 待补充 | To Be Determined | TBD | Marca de posição para informação ainda não confirmada |

> Os itens da tabela são exemplos genéricos e devem ser acrescentados ou removidos conforme a terminologia real do projeto antes do uso.

## 3. Matriz de termos multilíngues

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
| `hi-IN` | हिन्दी | सेमांटिक वर्ज़निंग | संरचना निर्णय | आचार संहिता | सतत एकीकरण | मॉडल संदर्भ प्रोटोकॉल | पूर्ति शेष |

- **Abreviações comuns**: Usadas como estão no corpo do texto de cada idioma e nunca localizadas: SBOM, SPDX, ADR, SemVer, CoC, CI/CD, MVP, NLP, LLM, MCP, TBD.

Esta tabela fixa uma tradução por termo e por idioma, para ser citada diretamente ao adicionar um idioma ou ao fazer uma substituição global. Os termos aparecem na forma de citação (nominativo ou infinitivo); o russo e o alemão os flexionam no corpo do texto, então convém buscar pelo radical.

Critério de inclusão: só entram os termos com ocorrências reais no corpo do texto, e cada célula abaixo é localizável no diretório daquele idioma. SBOM, MVP, NLP e LLM não aparecem nenhuma vez no corpo do texto dos doze idiomas e existem apenas como exemplos na tabela de correspondência da seção anterior, por isso ficam fora da matriz. O SPDX é sempre usado como abreviação pura em todos os idiomas e sua forma completa nunca ocorre, portanto aparece na linha de abreviações acima junto às demais, sem coluna de tradução.

Ao adicionar um idioma, preencha primeiro as traduções conforme esta tabela e depois execute `python3 cli/gitrule.py xcheck --path . --reference zh-CN` para verificar a consistência estrutural.

## Arquivos relacionados

- Para os requisitos de consistência terminológica, ver a [especificação geral de redação](./general-writing-specification.md)
- Para as regras de compartilhamento de termos bilíngues, ver a [especificação multilíngue](./multilingual-specification.md)
- Para o modelo da tabela de correspondência, ver [coleta de informações e modelos](./information-collection-and-templates.md)
