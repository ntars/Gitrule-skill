# Especificação de retrospectiva de iteração

> Problema que este arquivo resolve: definir o modelo de retrospectiva ao fim da iteração, seus campos e o mecanismo de acompanhamento das ações de melhoria, garantindo que os problemas se consolidem em ações executáveis e verificáveis para o ciclo seguinte e evitando a repetição de erros.

## 1. Dispositivos normativos

1. Ao fim de cada iteração, a retrospectiva deve ser concluída em até cinco dias úteis; o atraso deve ser justificado.
2. A retrospectiva deve basear-se em dados factuais; é vedado substituir métricas por impressões; as fontes de dados estão na [especificação de métricas de qualidade](./quality-metrics-specification.md).
3. Cada problema deve explicitar causa raiz, ação de melhoria, responsável e forma de verificação; itens sem responsável ou sem forma de verificação não podem entrar na lista de ações.
4. O número de ações de melhoria tem limite de três, ordenadas por impacto; acima de três, devem ser agrupadas ou rebaixadas a sugestões.
5. As ações de melhoria do ciclo anterior devem ser verificadas item a item nesta retrospectiva; as não concluídas devem ter o motivo justificado e ser reprogramadas.
6. O documento de retrospectiva registra apenas melhorias de processo, não o conteúdo de alterações de versão, que consta na [especificação de registro de alterações](./changelog-specification.md).

## 2. Modelo de documento de retrospectiva

```markdown
# Retrospectiva de iteração: {{项目名称}} {{迭代标识}}

Período da iteração: {{YYYY-MM-DD ~ YYYY-MM-DD}} ｜ Facilitador: {{姓名}} ｜ Participantes: {{姓名列表}} ｜ Data da retrospectiva: {{YYYY-MM-DD}}

## 1. Revisão dos objetivos
| Objetivo da iteração | Origem | Situação de alcance | Base de julgamento |
| --- | --- | --- | --- |
| {{目标描述}} | {{路线图 / 立项书}} | {{达成 / 未达成 / 部分达成}} | {{数据或交付物}} |

## 2. Instantâneo de dados
| Métrica | Valor do ciclo anterior | Valor deste ciclo | Variação | Meta |
| --- | --- | --- | --- | --- |
| Requisitos entregues | | | | |
| Defeitos escapados | | | | |
| Duração média da CI | | | | |
| Cobertura de requisitos | | | | |
| Incidentes | | | | |

## 3. Lista de fatos
- Favorável: {{基于数据的事实，如「本轮 CI 全绿率 98%」}}
- Impeditivo: {{基于数据的障碍，如「集成环境等待平均 4 小时」}}
- Imprevisto: {{未预见的事件及其影响}}

## 4. Problemas e causas raiz
| Número | Problema | Evidência | Causa raiz | Impacto |
| --- | --- | --- | --- | --- |
| R-01 | {{问题描述}} | {{数据 / 事件}} | {{根因，非表象}} | {{造成的影响}} |

## 5. Ações de melhoria
| Número | Problema associado | Ação | Responsável | Prazo | Forma de verificação | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| A-01 | R-01 | {{具体动作}} | {{姓名}} | {{YYYY-MM-DD}} | {{如何验证生效}} | A iniciar |

## 6. Verificação das ações do ciclo anterior
| Número | Ação | Estado no ciclo anterior | Conclusão deste ciclo | Tratamento seguinte |
| --- | --- | --- | --- | --- |
| A-00 | {{动作}} | Em andamento | {{完成 / 未完成 / 放弃}} | {{继续 / 重排 / 关闭并说明}} |

## 7. Consensos e pendências
- Consenso deste ciclo: {{需要长期遵守的约定}}
- Pendências: {{不在本轮处理的问题及原因}}
```

## 3. Modelo de item de ação de melhoria

```markdown
### A-{{两位序号}}：{{动作标题}}

- Problema associado: {{R-NN}}
- Ação: {{一个可执行的动作，含具体对象}}
- Responsável: {{姓名，唯一}}
- Prazo: {{YYYY-MM-DD}}
- Forma de verificação: {{可判定的检查和阈值}}
- Efeito esperado: {{用指标描述}}
- Estado: A iniciar / Em andamento / Concluída / Abandonada
```

## 4. Definição de campos

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Identificador da iteração | Sim | Texto | Coerente com a numeração de fases da [especificação de roteiro](./roadmap-specification.md) | `Sprint-12` |
| Situação de alcance | Sim | Enumeração | Alcançado / Não alcançado / Parcialmente alcançado | `部分达成` |
| Base de julgamento | Sim | Texto | Dados ou link de entrega; não pode ficar em branco | `REQ-001 已发布` |
| Instantâneo de dados | Sim | Tabela | Pelo menos 3 métricas, com valores do ciclo anterior e deste ciclo | `缺陷逃逸 2 → 0` |
| Causa raiz | Sim | Texto | Distinguir sintoma de causa raiz; encadear com “porque” de forma verificável | `因为环境未纳入 CI` |
| Ação | Sim | Texto | Ação única, com objeto e comportamento | `将集成环境纳入 CI` |
| Responsável | Sim | Texto | Único; é vedado escrever “equipe” | `Wang Wu` |
| Forma de verificação | Sim | Texto | Julgável, com momento de checagem | `下轮 CI 时长 <10 分钟` |
| Estado | Sim | Enumeração | Um dos quatro estados | `已完成` |

## 5. Instruções de preenchimento

1. **Revisão dos objetivos**: tomar como referência os objetivos originais da iniciação do projeto ou do roteiro, sem reescrevê-los para coincidir com o resultado.
2. **Instantâneo de dados**: deve usar o mesmo critério do ciclo anterior; ao alterar o critério, indicar simultaneamente “critério alterado” e as definições nova e antiga.
3. **Lista de fatos**: registrar apenas fatos verificáveis; julgamentos subjetivos como “comunicação deficiente” devem ser convertidos em eventos e horários concretos.
4. **Causa raiz**: perguntar repetidamente até o nível em que se pode agir; “porque os testes são insuficientes” ainda é sintoma, enquanto “porque os requisitos não estão associados a casos de teste” é a causa raiz.
5. **Número de ações**: no máximo três; se houver mais de três problemas, ordenar por impacto e registrar os não incluídos em “Pendências”.
6. **Forma de verificação**: deve indicar o momento da checagem e o limiar de julgamento; “acompanhar posteriormente” é inaceitável.
7. **Verificação do ciclo anterior**: dar conclusão item a item; é vedado pular o bloco inteiro; abandonar exige justificativa.

Erros comuns:

| Redação incorreta | Problema | Forma de correção |
| --- | --- | --- |
| “Todos devem dar mais atenção à qualidade” | Sem ação, sem responsável | Converter em ação concreta e responsável |
| Causa raiz escrita como “descuido” | Não verificável, não aprimorável | Perguntar até o nível de processo ou ferramenta |
| 8 ações de melhoria | Impossível implementar | Ordenar por impacto e manter as três primeiras |
| Forma de verificação escrita como “ver o efeito” | Não julgável | Acrescentar limiar e momento de checagem |
| Ações do ciclo anterior não verificadas | Ciclo de melhoria interrompido | Preencher a conclusão deste ciclo item a item |

## 6. Exemplo completo

```markdown
# Retrospectiva de iteração: markdown-lint-cli Sprint-12

Período da iteração: 2026-11-10 ~ 2026-11-21 ｜ Facilitador: Li Si ｜ Participantes: Wang Wu, Zhao Liu ｜ Data da retrospectiva: 2026-11-23

## 1. Revisão dos objetivos
| Objetivo da iteração | Origem | Situação de alcance | Base de julgamento |
| --- | --- | --- | --- |
| Publicar as regras essenciais da v1.0.0 | Roteiro S12 | Alcançado | tag v1.0.0 publicada |
| Cobertura de requisitos em 100% | Iniciação G1 | Parcialmente alcançado | 13/14 requisitos obrigatórios fechados |

## 2. Instantâneo de dados
| Métrica | Valor do ciclo anterior | Valor deste ciclo | Variação | Meta |
| --- | --- | --- | --- | --- |
| Requisitos entregues | 6 | 14 | +8 | 14 |
| Defeitos escapados | 2 | 1 | -1 | 0 |
| Cobertura de requisitos | 85% | 92.9% | +7.9% | 100% |

## 4. Problemas e causas raiz
| Número | Problema | Evidência | Causa raiz | Impacto |
| --- | --- | --- | --- | --- |
| R-01 | REQ-003 sem caso de teste | Campo TC da matriz de rastreabilidade em “pendente” | Porque a completude da matriz de rastreabilidade não era validada obrigatoriamente na revisão de requisitos | Cobertura de requisitos abaixo da meta |

## 5. Ações de melhoria
| Número | Problema associado | Ação | Responsável | Prazo | Forma de verificação | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| A-01 | R-01 | Incluir o item de checagem “matriz de rastreabilidade preenchida” na lista de revisão de requisitos | Wang Wu | 2026-11-27 | Os 5 registros de revisão do próximo ciclo contêm o item marcado | A iniciar |
```

## Arquivos relacionados

- Dados de rastreamento do requisito à publicação: [especificação da matriz de rastreabilidade de requisitos](./requirements-traceability-matrix-specification.md)
- Critérios das métricas e forma de apuração: [especificação de métricas de qualidade](./quality-metrics-specification.md)
- Fases e origem dos objetivos: [especificação de roteiro](./roadmap-specification.md)
- Conteúdo das alterações de versão: [especificação de registro de alterações](./changelog-specification.md)
- Retrospectiva de incidentes e melhorias: [especificação de resposta a incidentes](./incident-response-specification.md)
- Fase de execução do rastreamento: [processo de execução](./execution-process.md)
