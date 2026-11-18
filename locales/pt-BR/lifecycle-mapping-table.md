# Tabela de mapeamento do ciclo de vida

> Problema que este arquivo resolve: mapear todas as especificações para as oito fases do ciclo de vida do projeto, apresentando as condições de entrada, as entregas-chave, as especificações centrais e o portão de saída de cada fase, como ponto de navegação único para o uso das especificações “de dentro para fora e do início ao fim”.

Este arquivo responde apenas a “quais especificações uma fase exige e quando é possível avançar para a fase seguinte”. As cláusulas específicas de cada especificação dentro da fase continuam regidas pelo arquivo correspondente; para o fluxo operacional, ver o [processo de execução](./execution-process.md); para o recorte conforme o tipo de projeto, ver o [guia de seleção de especificações](./specification-selection-guide.md).

## 1. Visão geral das fases

| Fase | Nome | Questão central | Entregas-chave | Portão de saída |
| --- | --- | --- | --- | --- |
| 1 | Iniciação do projeto | O que fazer, qual nome, como configurar o repositório | Conclusão de nomenclatura, tabela de metadados do repositório, lista de informações | Nomenclatura conforme, informações obrigatórias completas ou sinalizadas |
| 2 | Análise de requisitos | Quais são os requisitos, como aceitá-los | Lista de requisitos, critérios de aceitação, matriz de rastreabilidade | Cada requisito com identificador único e critério de aceitação |
| 3 | Design de arquitetura | Como decompor, como acordar interfaces e dados | Documentação de arquitetura, contrato de API, modelo de dados | Rastreabilidade de requisitos para design sem lacunas, interfaces revisadas |
| 4 | Implementação de desenvolvimento | Como escrever código e fazer commit de forma consistente | Código, sequência de commits, fluxo de trabalho de CI, documentação de API | Revisão aprovada, CI verde, dependências sem vulnerabilidades de alto risco |
| 5 | Validação por testes | Se a qualidade exigida para publicação foi alcançada | Suíte de testes, relatório de cobertura, decisão de portão | Build e testes aprovados, P0 zerado |
| 6 | Implantação e lançamento | Como publicar, como apresentar na página inicial | tag, Release, documentação da página inicial, plano de reversão | Portões das três camadas verdes, plano de reversão validado |
| 7 | Operação e monitoramento | Como detectar problemas, como responder | Monitoramento e alertas, fluxo de resposta, documentação de incidentes | Indicadores críticos com alerta, canais de resposta disponíveis |
| 8 | Manutenção iterativa | Como fazer retrospectiva, como evoluir | Relatório de retrospectiva, roteiro atualizado, guia de migração | Itens de ação registrados, mudanças disruptivas com caminho de migração |

As fases 1–5 avançam de dentro para fora; as fases 6–8 passam da entrega para a operação e a evolução. As fases 7 e 8 podem ocorrer em paralelo, mas nenhuma delas pode ignorar o portão de saída da fase 5 do ciclo de vida.

## 2. Fase de iniciação do projeto

- **Objetivo da fase**: definir o posicionamento do projeto, a nomenclatura conforme e os metadados do repositório, estabelecendo a linha de base de informações compartilhada pelas fases seguintes.
- **Condição de entrada**: a concepção do projeto está formada e os usuários-alvo e o problema a resolver já podem ser enunciados.
- **Especificações centrais**: [papéis e responsabilidades](./roles-and-responsibilities.md), [especificação de iniciação e requisitos de projeto](./project-initiation-and-requirements-specification.md), [especificação de nomes de projeto](./project-naming-specification.md), [coleta de informações e modelos](./information-collection-and-templates.md), [processo de execução](./execution-process.md).
- **Entregas-chave**: três candidatos de nome e a conclusão da busca por duplicidade; tabela de metadados do repositório (descrição, tópicos, branch padrão, visibilidade, licença); lista de informações obrigatórias e lista de informações ausentes.
- **Portão de saída**: o nome do repositório atende a todas as regras absolutas da [especificação de nomes de projeto](./project-naming-specification.md); o tipo de licença está definido; os campos obrigatórios estão completos e os ausentes foram sinalizados conforme a [coleta de informações e modelos](./information-collection-and-templates.md).

## 3. Fase de análise de requisitos

- **Objetivo da fase**: desdobrar a concepção em itens de requisito aceitáveis e rastreáveis e, a partir deles, formar o roteiro.
- **Condição de entrada**: as conclusões de nomenclatura e metadados da fase de iniciação do projeto estão confirmadas.
- **Especificações centrais**: [especificação de iniciação e requisitos de projeto](./project-initiation-and-requirements-specification.md), [especificação da matriz de rastreabilidade de requisitos](./requirements-traceability-matrix-specification.md), [especificação de roteiro](./roadmap-specification.md), [coleta de informações e modelos](./information-collection-and-templates.md).
- **Entregas-chave**: lista de requisitos com identificador único; critério de aceitação de cada requisito; versão inicial da matriz de rastreabilidade de requisitos; roteiro organizado por prioridade.
- **Portão de saída**: cada requisito possui identificador único e critério de aceitação verificável; a matriz de rastreabilidade já contém os campos do lado de requisitos; os itens planejados do roteiro estão marcados como não compromisso de entrega.

## 4. Fase de design de arquitetura

- **Objetivo da fase**: definir fronteiras de módulos, contratos de interface e modelo de dados, de modo que os requisitos possam ser atribuídos a unidades de design concretas.
- **Condição de entrada**: a lista de requisitos e os critérios de aceitação estão confirmados.
- **Especificações centrais**: [especificação de documentação de design de arquitetura](./architecture-design-document-specification.md), [especificação de design de API](./api-design-specification.md), [especificação de design de banco de dados](./database-design-specification.md), [matriz de documentação](./document-matrix.md), [especificação geral de redação](./general-writing-specification.md).
- **Entregas-chave**: documentação de design de arquitetura; contrato de API; modelo de dados e estratégia de migração; lista da matriz de documentação.
- **Portão de saída**: cada requisito aponta, na matriz de rastreabilidade, para ao menos uma unidade de design; interfaces e modelo de dados revisados; as responsabilidades dos arquivos na matriz de documentação não se sobrepõem.

## 5. Fase de implementação de desenvolvimento

- **Objetivo da fase**: implementar o design com estilo de código, formato de commit e fluxo de revisão consistentes, mantendo dependências e automação sob controle.
- **Condição de entrada**: a arquitetura e os contratos de interface foram aprovados em revisão.
- **Especificações centrais**: [especificação de estilo de código](./code-style-specification.md), [especificação de fluxo de trabalho Git e branches](./git-workflow-and-branching-specification.md), [especificação de mensagens de commit](./commit-message-specification.md), [especificação de revisão de código](./code-review-specification.md), [especificação de gestão de dependências](./dependency-management-specification.md), [especificação de propriedade de código](./code-ownership-specification.md), [especificação de documentação de API](./api-documentation-specification.md), [especificação de fluxo de trabalho de CI](./ci-workflow-specification.md).
- **Entregas-chave**: código em conformidade com a especificação de estilo; sequência de commits em conformidade com o Conventional Commits; fluxo de trabalho de CI; documentação de API sincronizada com a implementação.
- **Portão de saída**: mensagens de commit e nomes de branch conformes à especificação; código revisado e roteamento de propriedade correto; fluxo de trabalho de CI aprovado; dependências sem vulnerabilidades de alto risco não tratadas.

## 6. Fase de validação por testes

- **Objetivo da fase**: confirmar, por meio de testes reproduzíveis e da decisão de portão, que as entregas atingem a linha de base de qualidade exigida para publicação.
- **Condição de entrada**: a implementação funcional está concluída e o fluxo de trabalho de CI pode ser executado.
- **Especificações centrais**: [especificação de testes](./testing-specification.md), [portão de qualidade](./quality-gate.md), [especificação de métricas de qualidade](./quality-metrics-specification.md), [especificação de acessibilidade](./accessibility-specification.md), [especificação de segurança e privacidade](./security-and-privacy-specification.md).
- **Entregas-chave**: suíte de testes e relatório de cobertura; resultado da decisão item a item do portão; registro de verificações de segurança e acessibilidade.
- **Portão de saída**: build, testes e análise estática aprovados; todos os itens P0 dos Gate A, B e C zerados; itens P1 registrados como pendência ou concluídos.

## 7. Fase de implantação e lançamento

- **Objetivo da fase**: publicar a versão por um processo controlado e concluir a documentação da página inicial e as entregas visíveis ao usuário.
- **Condição de entrada**: o portão de saída da fase de validação por testes está aprovado, sem itens P0 não zerados.
- **Especificações centrais**: [especificação de push e publicação](./push-and-release-specification.md), [especificação de gestão de versões](./version-management-specification.md), [especificação de registro de alterações](./changelog-specification.md), [especificação de implantação e reversão](./deployment-and-rollback-specification.md), [especificação de guia de migração](./migration-guide-specification.md), [especificação de fluxo de trabalho de CI](./ci-workflow-specification.md), [especificação de modelos de Issue e PR](./issue-and-pr-template-specification.md); para a documentação da página inicial, ver [modelo padrão de README](./readme-standard-template.md), [especificação de seções do README](./readme-sections-specification.md), [especificação de layout visual do README](./readme-visual-layout-specification.md), [especificação de selos](./badge-specification.md), [guia de adaptação de README por categoria](./readme-category-adaptation-guide.md).
- **Entregas-chave**: versão semântica e tag anotada; Release Notes e registro de alterações; README da página inicial e modelos da comunidade; registro de implantação e plano de reversão.
- **Portão de saída**: portões das três camadas verdes; tag do tipo annotated e em conformidade com o SemVer; plano de reversão validado; documentação da página inicial sem caminhos absolutos locais e sem marcadores de posição remanescentes.

## 8. Fase de operação e monitoramento

- **Objetivo da fase**: estabelecer capacidade de observabilidade e mecanismos de resposta, para que problemas em produção possam ser descobertos, localizados e tratados.
- **Condição de entrada**: a versão foi publicada e o serviço ou artefato está disponível.
- **Especificações centrais**: [especificação de observabilidade](./observability-specification.md), [especificação de resposta a incidentes](./incident-response-specification.md), [especificação de solução de problemas](./troubleshooting-specification.md), [especificação de segurança e privacidade](./security-and-privacy-specification.md), [modelo de SECURITY](./security-template.md), [isenção de responsabilidade](./disclaimer.md), [modelo de isenção de responsabilidade](./disclaimer-template.md).
- **Entregas-chave**: indicadores críticos e regras de alerta; classificação de incidentes e fluxo de resposta; documentação de perguntas frequentes e solução de problemas; canal de recebimento de vulnerabilidades.
- **Portão de saída**: todos os indicadores críticos com alerta configurado; canal de relato de vulnerabilidades disponível e validado; fluxo de resposta a incidentes com ao menos um simulado ou exercício de mesa concluído.

## 9. Fase de manutenção iterativa

- **Objetivo da fase**: revisar as iterações entregues, gerir o caminho de evolução e manter o alinhamento contínuo entre requisitos, design e testes.
- **Condição de entrada**: ao menos uma publicação ou ciclo de iteração concluído.
- **Especificações centrais**: [especificação de retrospectiva de iteração](./iteration-retrospective-specification.md), [especificação de roteiro](./roadmap-specification.md), [especificação da matriz de rastreabilidade de requisitos](./requirements-traceability-matrix-specification.md), [especificação de registro de alterações](./changelog-specification.md), [especificação de guia de migração](./migration-guide-specification.md), [especificação de gestão de versões](./version-management-specification.md), [especificação de promoção open source](./open-source-promotion-specification.md).
- **Entregas-chave**: relatório de retrospectiva de iteração com itens de ação; roteiro e matriz de rastreabilidade atualizados; guia de migração para mudanças disruptivas; registro de alterações de versão.
- **Portão de saída**: itens de ação da rodada anterior com responsável e prazo registrados; mudanças disruptivas com caminho de migração e anúncio; matriz de rastreabilidade sem elos quebrados.

## 10. Especificações transversais

As especificações a seguir não pertencem a uma única fase e devem vigorar continuamente em todas as fases:

| Categoria | Especificação | Forma de vigência |
| --- | --- | --- |
| Restrições obrigatórias | [Regras absolutas](./hard-rules.md), [Práticas proibidas](./prohibited-practices.md) | A violação em qualquer fase bloqueia; não se admite isenção por motivo de cronograma |
| Processo e terminologia | [Papéis e responsabilidades](./roles-and-responsibilities.md), [Processo de execução](./execution-process.md), [Glossário](./glossary.md) | Unificar a divisão de papéis, a terminologia das fases e a ordem das entregas |
| Comunidade e governança | [Especificação de guia de contribuição](./contribution-guide-specification.md), [Modelo de guia de contribuição](./contribution-guide-template.md), [Especificação de código de conduta](./code-of-conduct-specification.md), [Modelo de código de conduta](./code-of-conduct-template.md) | Concluir antes de o repositório se tornar visível ao público e ajustar depois conforme a escala da comunidade |
| Jurídico e conformidade | [Especificação de conformidade open source](./open-source-compliance-specification.md), [Especificação de LICENSE](./license-specification.md), [Especificação de NOTICE](./notice-specification.md), [Isenção de responsabilidade](./disclaimer.md), [Modelo de isenção de responsabilidade](./disclaimer-template.md) | Definir a licença na fase de iniciação e concluir todos os documentos jurídicos antes da fase de implantação |
| Redação e multilinguismo | [Especificação geral de redação](./general-writing-specification.md), [Especificação de multilinguismo](./multilingual-specification.md), [Guia de redação de características e trade-offs de engenharia](./features-and-engineering-tradeoffs-guide.md), [Matriz de documentação](./document-matrix.md) | Aplicar-se a toda a produção documental, garantindo consistência de expressão |
| Integração programática | [Especificação de metadados legíveis por máquina](./machine-readable-metadata-specification.md), [Especificação de autoria de Skill](./skill-authoring-specification.md), [Especificação de ferramentas MCP](./mcp-tool-specification.md), [Especificação de invocação de Agent e prompts](./agent-invocation-and-prompt-specification.md) | Sobrepor quando houver necessidade de expert, Skill, MCP ou invocação por linha de comando |

## 11. Degradação e retorno

1. Um repositório privado de scripts temporários pode ser degradado para executar apenas o portão P0 e deve declarar “modo degradado” nas entregas e indicar os itens não executados.
2. Quando o portão de saída de qualquer fase não for aprovado, não se deve avançar para a fase seguinte; os problemas, responsáveis e ações devem ser registrados conforme o [formato do relatório de auditoria](./audit-report-format.md).
3. Quando um problema P0 for descoberto após a fase de implantação, deve-se retornar à fase de validação por testes para nova decisão e, se necessário, executar o fluxo de tratamento de incidentes da [especificação de push e publicação](./push-and-release-specification.md).

## Arquivos relacionados

- Para o fluxo operacional dentro das fases, ver o [processo de execução](./execution-process.md)
- Para o recorte das especificações conforme o tipo de projeto, ver o [guia de seleção de especificações](./specification-selection-guide.md)
- Para os critérios de decisão do portão, ver o [portão de qualidade](./quality-gate.md)
- Para o formato de registro de problemas de auditoria, ver o [formato do relatório de auditoria](./audit-report-format.md)
