# Especificação de roteiro

> Problema que este arquivo resolve: definir o modelo de roteiro, os campos, a marcação de estado e o princípio de não compromisso, evitando que o plano seja apresentado como promessa e garantindo coerência com o registro de alterações e a retrospectiva de iteração.

## 1. Dispositivos normativos

1. O roteiro deve indicar, em local destacado, “este roteiro é um plano, não um compromisso de entrega”.
2. É vedado prometer datas concretas de entrega; a versão-alvo deve ser expressa por intervalo de versões ou por trimestre.
3. As mudanças de estado devem deixar rastro, e os itens cancelados devem indicar o motivo.
4. Os itens concluídos devem apontar para a entrada correspondente da [especificação de registro de alterações](./changelog-specification.md), evitando divergência de informações entre dois locais.
5. O roteiro trata de planos futuros e admite ajustes e cancelamentos; o registro de alterações trata de fatos já publicados e não pode reescrever entradas históricas.
6. Cada item de plano deve estar associado a pelo menos um requisito ou a uma ação de melhoria de iteração; a relação de rastreamento está na [especificação da matriz de rastreabilidade de requisitos](./requirements-traceability-matrix-specification.md).

## 2. Modelo de roteiro

```markdown
# Roteiro: {{项目名称}}

> Este roteiro é um plano, não um compromisso de entrega. A versão-alvo e o trimestre são apenas expectativas e podem ser ajustados conforme a prioridade.

Versão: {{v1.0}} ｜ Responsável pela atualização: {{姓名}} ｜ Última verificação: {{YYYY-MM-DD}}

## Agora / Próximo / Depois

| Fase | Item de plano | Estado | Versão-alvo | Requisito associado | Dependência | Critério de aceite | Registro de alterações |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Agora | {{能力描述}} | Em andamento | {{v1.0}} | {{REQ-001}} | {{无}} | {{可验证条件}} | — |
| Próximo | {{能力描述}} | Em planejamento | {{v1.1 ~ v1.2}} | {{REQ-008}} | {{计划项 A}} | {{可验证条件}} | — |
| Depois | {{能力描述}} | Em planejamento | {{待定}} | {{REQ-015}} | {{外部依赖}} | {{可验证条件}} | — |
| Cancelado | {{能力描述}} | Cancelado | — | {{REQ-020}} | — | — | — |

Estado: Em planejamento / Em andamento / Concluído / Cancelado

## Registro de mudanças de estado
| Data | Item de plano | Estado anterior → novo estado | Motivo | Responsável pela decisão |
| --- | --- | --- | --- | --- |
| {{YYYY-MM-DD}} | {{计划项}} | {{规划中 → 已取消}} | {{原因}} | {{姓名}} |

## Justificativa de cancelamento
- {{计划项}}: {{取消原因，如需求变更、依赖 unavailable}}
```

## 3. Modelo de item de plano

```markdown
### {{计划项名称}}

- Estado: {{规划中 / 进行中 / 已完成 / 已取消}}
- Versão-alvo: {{vX.Y / 季度 / 待定}}
- Requisito associado: {{REQ-NNN}}
- Origem: {{立项书 / 迭代回顾 A-NN / 用户反馈}}
- Dependência: {{前置计划项或外部依赖；无则写「无」}}
- Critério de aceite: {{可验证的完成条件，须含阈值}}
- Motivo de não conclusão: {{仅已取消项填写}}
```

## 4. Definição de campos

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Item de plano | Sim | Sintagma nominal | Descreve a capacidade a entregar, não a ação da tarefa | `Suporte a configuração TOML` |
| Estado | Sim | Enumeração | Em planejamento / Em andamento / Concluído / Cancelado | `Em andamento` |
| Versão-alvo | Sim | Versão / Trimestre / A definir | Datas concretas são vedadas | `v1.1 ~ v1.2` |
| Requisito associado | Sim | `REQ-NNN` | Coerente com a numeração da iniciação do projeto | `REQ-008` |
| Origem | Sim | Texto | Iniciação, retrospectiva de iteração ou feedback de usuário | `Retrospectiva de iteração A-01` |
| Dependência | Sim | Texto | Sem dependência, escrever “nenhuma”; é vedado deixar em branco | `Depende do item de plano A` |
| Critério de aceite | Sim | Texto | Verificável, com limiar | `Análise de 100 amostras sem falhas` |
| Registro de alterações | Condicionalmente obrigatório | Link | Obrigatório para itens concluídos | `[1.0.0]` |
| Motivo de cancelamento | Condicionalmente obrigatório | Texto | Obrigatório para itens cancelados | `A API externa dependente foi descontinuada` |

## 5. Instruções de preenchimento

1. **Divisão de fases**: três faixas, “Agora / Próximo / Depois”; “Agora” não deve exceder 3 itens e, se exceder, as prioridades devem ser reorganizadas.
2. **Não compromisso**: é vedado escrever compromissos de data como “publicação no Q3” ou “conclusão no mês 12”; a expectativa deve ser expressa por número de versão ou por intervalo de trimestre.
3. **Critério de aceite**: deve permitir julgamento objetivo; “melhorar a usabilidade” é inaceitável, enquanto “reduzir os itens de configuração de 5 para 2” é aceitável.
4. **Mudança de estado**: cada mudança acrescenta um registro e não substitui o valor original; os itens cancelados mantêm a linha e indicam o motivo.
5. **Vinculação na conclusão**: ao alterar o estado para “Concluído”, deve-se preencher simultaneamente a âncora no registro de alterações; sem o registro correspondente, o item não pode ser marcado como concluído.
6. **Vinculação com a retrospectiva**: ao incorporar ao roteiro uma ação de melhoria proveniente da retrospectiva de iteração, deve-se indicar A-NN em “Origem” e registrar em sincronia na [especificação de retrospectiva de iteração](./iteration-retrospective-specification.md).
7. **Resumo no README**: o README apresenta apenas o resumo das três faixas e o link, mantendo a tabela completa neste arquivo, conforme a [especificação de seções do README](./readme-sections-specification.md).

Erros comuns:

| Redação incorreta | Problema | Forma de correção |
| --- | --- | --- |
| “Publicação em 12/2026” | Configura compromisso | Alterar para `v1.2` ou `Q4` |
| Item concluído sem link para o registro de alterações | Divergência de informações entre dois locais | Acrescentar a âncora do registro |
| Excluir a linha do item cancelado | Histórico não rastreável | Manter a linha e indicar o motivo |
| Item de plano escrito como “otimizar o desempenho” | Sem critério de aceite | Acrescentar métrica com limiar |
| Roteiro com 20 itens acumulados | Impossível julgar prioridades | Reduzir a três faixas, com limite de itens por faixa |

## 6. Exemplo completo

```markdown
# Roteiro: markdown-lint-cli

> Este roteiro é um plano, não um compromisso de entrega.

Versão: v1.0 ｜ Responsável pela atualização: Li Si ｜ Última verificação: 2026-11-20

| Fase | Item de plano | Estado | Versão-alvo | Requisito associado | Dependência | Critério de aceite | Registro de alterações |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Agora | Conjunto de regras essenciais | Concluído | v1.0.0 | REQ-001~007 | Nenhuma | Taxa de detecção ≥95% em 50 amostras | [1.0.0] |
| Próximo | Integração com plug-in de editor | Em planejamento | v1.1 | REQ-003 | Conjunto de regras essenciais estável | Chamável nos editores principais | — |
| Depois | DSL de regras personalizadas | Em planejamento | A definir | REQ-018 | API de plug-in estável | Usuário adiciona regras sem alterar o código-fonte | — |
| Cancelado | Sincronização de regras na nuvem | Cancelado | — | REQ-020 | — | — | — |

## Registro de mudanças de estado
| Data | Item de plano | Estado anterior → novo estado | Motivo | Responsável pela decisão |
| --- | --- | --- | --- | --- |
| 2026-11-15 | Sincronização de regras na nuvem | Em planejamento → Cancelado | Falta de recursos de manutenção no servidor | Li Si |
```

## Arquivos relacionados

- Nomenclatura de versões e versão-alvo: [especificação de gerenciamento de versões](./version-management-specification.md)
- Base da iniciação e numeração de requisitos: [especificação de iniciação do projeto e requisitos](./project-initiation-and-requirements-specification.md)
- Registro externo dos itens concluídos: [especificação de registro de alterações](./changelog-specification.md)
- Origem das ações de melhoria: [especificação de retrospectiva de iteração](./iteration-retrospective-specification.md)
- Rastreamento do requisito ao plano: [especificação da matriz de rastreabilidade de requisitos](./requirements-traceability-matrix-specification.md)
- Seção de roteiro no README: [especificação de seções do README](./readme-sections-specification.md)
