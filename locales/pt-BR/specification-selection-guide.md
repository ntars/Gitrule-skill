# Guia de seleção de especificações

> Problema que este arquivo resolve: apresentar os critérios de recorte das especificações segundo o tipo de projeto, o tamanho da equipe e a fase de publicação, oferecendo o conjunto mínimo viável e o conjunto completo em conformidade, para que o “uso conforme a necessidade” tenha critérios de decisão claros, sem depender de julgamento individual.

O objeto de recorte deste arquivo é o conjunto completo das especificações; as diferenças por tipo no nível das seções do README estão no [guia de adaptação de README por categoria](./readme-category-adaptation-guide.md), e o mapeamento completo das fases está na [tabela de mapeamento do ciclo de vida](./lifecycle-mapping-table.md).

## 1. Princípios de seleção

1. **Restrições obrigatórias não podem ser recortadas**: as [regras absolutas](./hard-rules.md) e as [práticas proibidas](./prohibited-practices.md) aplicam-se integralmente em qualquer projeto e em qualquer fase.
2. **O portão da fase determina o limite inferior**: antes de entrar em uma fase, o portão de saída dessa fase indicado na [tabela de mapeamento do ciclo de vida](./lifecycle-mapping-table.md) deve ser aprovado, e as especificações centrais correspondentes não podem ser omitidas.
3. **A diferença de tipo afeta apenas a profundidade**: o tipo de projeto determina quais especificações são enfatizadas e quais detalhes são simplificados, o que não constitui motivo para ignorar o portão de qualidade.
4. **A degradação deve ser declarada de forma explícita**: um repositório privado de scripts temporários pode executar apenas o portão P0 e deve indicar “modo degradado” nas entregas e listar os itens não executados.

## 2. Dimensões de recorte

| Dimensão | Valores | Efeito principal |
| --- | --- | --- |
| Tipo de projeto | Biblioteca / SDK, aplicação, ferramenta de linha de comando, framework, coleção de recursos | Determina as especificações reforçadas e os detalhes simplificáveis |
| Tamanho da equipe | Individual, equipe pequena, organização | Determina a necessidade das especificações de governança e colaboração |
| Fase de publicação | Validação de protótipo, primeira publicação, manutenção estável | Determina o momento de introdução das especificações de conformidade e operação |

Quando as três dimensões se sobrepõem, adotar a prioridade “restrições obrigatórias → portão da fase → fase de publicação → tipo de projeto → tamanho da equipe”; o recorte em uma dimensão de prioridade menor não deve enfraquecer as exigências de uma dimensão de prioridade maior.

## 3. Recorte por tipo de projeto

| Tipo de projeto | A reforçar | Simplificável | Entregas obrigatórias |
| --- | --- | --- | --- |
| Biblioteca / SDK | [Especificação de design de API](./api-design-specification.md), [especificação de documentação de API](./api-documentation-specification.md), [especificação de gestão de versões](./version-management-specification.md), [especificação de registro de alterações](./changelog-specification.md) | Implantação e reversão, observabilidade (apenas na distribuição de artefatos), especificações visuais de capturas de tela | README, documentação de API, LICENSE, CHANGELOG |
| Aplicação | [Especificação de layout visual do README](./readme-visual-layout-specification.md), [especificação de acessibilidade](./accessibility-specification.md), [especificação de implantação e reversão](./deployment-and-rollback-specification.md), [especificação de observabilidade](./observability-specification.md), [especificação de solução de problemas](./troubleshooting-specification.md) | Documentação de API, design de banco de dados (ao usar serviços gerenciados) | README, capturas de tela, instruções de implantação, SECURITY |
| Ferramenta de linha de comando | [Especificação de mensagens de commit](./commit-message-specification.md), [guia de redação de características e trade-offs de engenharia](./features-and-engineering-tradeoffs-guide.md), [guia de adaptação de README por categoria](./readme-category-adaptation-guide.md), [especificação de acessibilidade](./accessibility-specification.md) (saída de terminal) | Design de banco de dados, implantação e reversão (quando a distribuição se dá principalmente por pacote) | README, exemplos de uso, gif de demonstração, LICENSE |
| Framework | [Matriz de documentação](./document-matrix.md), [especificação de documentação de API](./api-documentation-specification.md), [especificação de guia de contribuição](./contribution-guide-specification.md), [especificação de código de conduta](./code-of-conduct-specification.md), [especificação de observabilidade](./observability-specification.md) | Design de banco de dados (quando não há armazenamento embutido) | README, entrada da documentação, guia de contribuição, código de conduta |
| Coleção de recursos | [Matriz de documentação](./document-matrix.md), [modelo de guia de contribuição](./contribution-guide-template.md), [especificação de multilinguismo](./multilingual-specification.md), [especificação geral de redação](./general-writing-specification.md) | Testes, implantação, API, banco de dados, observabilidade | README, diretório de categorias, guia de contribuição, LICENSE |

Projetos do tipo coleção de recursos normalmente não contêm código executável, e a [especificação de testes](./testing-specification.md) e a [especificação de fluxo de trabalho de CI](./ci-workflow-specification.md) podem ser marcadas como não aplicáveis; a [especificação geral de redação](./general-writing-specification.md) e a [especificação de acessibilidade](./accessibility-specification.md), porém, continuam obrigatórias, para garantir a usabilidade dos textos de link e da estrutura de listas.

## 4. Recorte por tamanho da equipe

| Tamanho da equipe | Especificações a acrescentar | Especificações dispensáveis |
| --- | --- | --- |
| Individual | [Regras absolutas](./hard-rules.md), [especificação de nomes de projeto](./project-naming-specification.md), [modelo padrão de README](./readme-standard-template.md), [especificação de LICENSE](./license-specification.md) | Código de conduta, propriedade de código, retrospectiva de iteração, métricas de qualidade (podem ser completadas até a primeira publicação) |
| Equipe pequena | Além das do caso individual, acrescentar [especificação de propriedade de código](./code-ownership-specification.md), [especificação de guia de contribuição](./contribution-guide-specification.md), [especificação de fluxo de trabalho de CI](./ci-workflow-specification.md), [portão de qualidade](./quality-gate.md) | Resposta a incidentes, observabilidade (podem ser completadas após o serviço entrar no ar) |
| Organização | Aplicação integral; além disso, devem ser implementadas a [especificação de NOTICE](./notice-specification.md), o [modelo de SECURITY](./security-template.md), a [isenção de responsabilidade](./disclaimer.md), a [especificação de resposta a incidentes](./incident-response-specification.md), a [especificação de métricas de qualidade](./quality-metrics-specification.md) e a [especificação da matriz de rastreabilidade de requisitos](./requirements-traceability-matrix-specification.md) | Nenhuma |

Quando o tamanho da equipe aumenta, as especificações de governança devem ser completadas antes de o repositório se tornar visível ao público, e não se deve aguardar a primeira publicação para acrescentá-las.

## 5. Recorte por fase de publicação

| Fase de publicação | A introduzir | Adiável | Requisito de declaração |
| --- | --- | --- | --- |
| Validação de protótipo | [Regras absolutas](./hard-rules.md), [especificação de nomes de projeto](./project-naming-specification.md), [modelo padrão de README](./readme-standard-template.md), [especificação geral de redação](./general-writing-specification.md) | Portão de qualidade, observabilidade, resposta a incidentes, documentos jurídicos | Deve indicar “modo degradado” e listar os itens adiados |
| Primeira publicação | Além dos do protótipo, acrescentar [portão de qualidade](./quality-gate.md), [especificação de conformidade open source](./open-source-compliance-specification.md), [especificação de LICENSE](./license-specification.md), [modelo de isenção de responsabilidade](./disclaimer-template.md), [modelo de guia de contribuição](./contribution-guide-template.md), [modelo de código de conduta](./code-of-conduct-template.md), [modelo de SECURITY](./security-template.md), [especificação de selos](./badge-specification.md) | Guia de migração, retrospectiva de iteração (podem ser completados após a primeira iteração de versão) | Não se deve omitir itens do portão P0 |
| Manutenção estável | Além dos da primeira publicação, acrescentar [especificação de registro de alterações](./changelog-specification.md), [especificação de gestão de versões](./version-management-specification.md), [especificação de guia de migração](./migration-guide-specification.md), [especificação de observabilidade](./observability-specification.md), [especificação de resposta a incidentes](./incident-response-specification.md), [especificação de solução de problemas](./troubleshooting-specification.md), [especificação de retrospectiva de iteração](./iteration-retrospective-specification.md), [especificação da matriz de rastreabilidade de requisitos](./requirements-traceability-matrix-specification.md) | Nenhum | Mudanças disruptivas devem ter caminho de migração e anúncio |

## 6. Combinações

### 6.1 Combinação mínima viável

Aplicável a protótipos individuais ou repositórios privados de validação, com 10 documentos no total:

| Finalidade | Especificação |
| --- | --- |
| Restrição | [Regras absolutas](./hard-rules.md), [práticas proibidas](./prohibited-practices.md) |
| Iniciação | [Especificação de iniciação e requisitos de projeto](./project-initiation-and-requirements-specification.md), [especificação de nomes de projeto](./project-naming-specification.md) |
| Página inicial | [Modelo padrão de README](./readme-standard-template.md), [especificação geral de redação](./general-writing-specification.md) |
| Engenharia | [Especificação de estilo de código](./code-style-specification.md), [especificação de mensagens de commit](./commit-message-specification.md), [especificação de testes](./testing-specification.md) |
| Publicação | [Especificação de push e publicação](./push-and-release-specification.md), [especificação de LICENSE](./license-specification.md) |

Ao usar esta combinação, é obrigatório declarar o modo degradado nas entregas e completar, antes da primeira publicação, a combinação completa da seção 6.3 do guia.

### 6.2 Combinação padrão de publicação

Sobre a combinação mínima viável, completar os itens básicos de qualidade, conformidade, governança e operação: acrescentar [portão de qualidade](./quality-gate.md), [especificação de seções do README](./readme-sections-specification.md), [especificação de layout visual do README](./readme-visual-layout-specification.md), [especificação de selos](./badge-specification.md), [matriz de documentação](./document-matrix.md), [especificação de conformidade open source](./open-source-compliance-specification.md), [modelo de isenção de responsabilidade](./disclaimer-template.md), [modelo de SECURITY](./security-template.md), [modelo de guia de contribuição](./contribution-guide-template.md), [modelo de código de conduta](./code-of-conduct-template.md), [especificação de registro de alterações](./changelog-specification.md), [especificação de gestão de versões](./version-management-specification.md), [especificação de acessibilidade](./accessibility-specification.md), [especificação de fluxo de trabalho de CI](./ci-workflow-specification.md), [especificação de modelos de Issue e PR](./issue-and-pr-template-specification.md), [especificação de segurança e privacidade](./security-and-privacy-specification.md).

Esta combinação atende a todas as condições de liberação dos Gate A, B e C de um repositório público e é o ponto de partida recomendado para a maioria dos projetos.

### 6.3 Combinação completa em conformidade

Aplica todas as especificações e destina-se a projetos de nível organizacional, a projetos distribuídos para cenários regulados ou a projetos que exijam integração programática por expert / Skill / MCP / linha de comando. A quantidade de documentos tem como referência o [índice em chinês simplificado](./README.md); na ativação, deve-se verificar item a item o portão de cada fase na [tabela de mapeamento do ciclo de vida](./lifecycle-mapping-table.md).

## 7. Tratamento de conflitos

1. Quando houver conflito dentro de uma mesma dimensão, prevalecem as exigências do estágio de publicação mais avançado; a simplificação do estágio de protótipo não deve se estender ao estágio público.
2. Quando houver conflito entre dimensões distintas, aplicar a prioridade da seção 2; as restrições obrigatórias e os portões de fase não devem ser sobrepostos por nenhuma dimensão.
3. Quando o projeto tiver uma situação especial que exija desvio deste guia, deve-se registrar nas entregas as especificações desviadas, os motivos e as medidas compensatórias, e submetê-las à revisão.
4. O modo degradado não deve ser usado em repositórios públicos nem servir de base para ignorar a licença ou o portão de segurança.

## Arquivos relacionados

- Para o mapeamento completo entre fases e especificações, ver a [tabela de mapeamento do ciclo de vida](./lifecycle-mapping-table.md)
- Para o recorte por tipo no nível das seções do README, ver o [guia de adaptação de README por categoria](./readme-category-adaptation-guide.md)
- Para as restrições não recortáveis, ver as [regras absolutas](./hard-rules.md) e as [práticas proibidas](./prohibited-practices.md)
- Para as condições de liberação do portão, ver o [portão de qualidade](./quality-gate.md)
