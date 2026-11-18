# Especificação de resposta a incidentes

> Problema que este arquivo resolve: definir o modelo de relatório de incidentes, o registro de linha do tempo, os modelos de comunicação e os campos de retrospectiva, garantindo falhas controláveis, informações sincronizadas e experiência acumulável.

## 1. Dispositivos normativos

1. Classificação de incidentes: P0, funcionalidade central indisponível ou dados corrompidos; P1, funcionalidade grave prejudicada afetando a maioria dos usuários; P2, problema localizado com impacto limitado.
2. Fluxo de resposta: detecção → classificação → contenção → localização → correção → comunicação; a contenção tem prioridade sobre a localização.
3. Todo incidente P0/P1 deve passar por retrospectiva, registrando linha do tempo, causa raiz, impacto, tratamento e itens de melhoria.
4. Os itens de melhoria devem ser incorporados à [especificação de roteiro](./roadmap-specification.md) para acompanhamento até o fechamento.
5. A retrospectiva deve focar na melhoria do sistema, sem imputar responsabilidade individual.
6. Vazamento de chaves: rotação imediata → limpeza do histórico → comunicação; não deve ser feito apenas um commit de exclusão (ver [especificação de segurança e privacidade](./security-and-privacy-specification.md)).
7. Push acidental de arquivos grandes: migração para LFS ou reescrita de histórico (ver [especificação de push e publicação](./push-and-release-specification.md)).

## 2. Modelo de relatório de incidentes

```markdown
# Relatório de incidente: {{INC-YYYYMMDD-NN}}

- Nível do incidente: {{P0 / P1 / P2}}
- Horário de detecção: {{YYYY-MM-DD HH:MM}}
- Horário de recuperação: {{YYYY-MM-DD HH:MM}}
- Duração: {{N 分钟}}
- Comandante: {{姓名}}
- Estado atual: {{处理中 / 已恢复 / 已复盘}}

## Alcance do impacto
| Dimensão | Descrição |
| --- | --- |
| Funcionalidade afetada | {{具体功能}} |
| Proporção de usuários afetados | {{估算值与依据}} |
| Impacto nos dados | {{无 / 描述}} |
| Impacto no negócio | {{可量化的损失或阻塞}} |

## Linha do tempo
| Horário | Evento | Origem | Responsável pela ação |
| --- | --- | --- | --- |
| {{HH:MM}} | Acionamento do alerta | {{监控面板}} | {{姓名}} |
| {{HH:MM}} | Classificação como P1 | {{判断依据}} | {{姓名}} |
| {{HH:MM}} | Execução da reversão | {{命令 / 平台}} | {{姓名}} |
| {{HH:MM}} | Recuperação do serviço | {{验证方式}} | {{姓名}} |

## Causa raiz
- Causa direta: {{触发故障的具体事件}}
- Causa fundamental: {{为何未被预防或及时检测}}
-  Fatores de amplificação: {{扩大影响的因素}}

## Tratamento e verificação
1. {{止血措施}}
2. {{修复措施}}
3. {{验证方式与结果}}

## Itens de melhoria
| Número | Ação | Responsável | Prazo | Forma de verificação | Estado |
| --- | --- | --- | --- | --- | --- |
| {{A-NN}} | {{具体动作}} | {{姓名}} | {{YYYY-MM-DD}} | {{可判定阈值}} | {{待开始}} |
```

## 3. Modelos de comunicação

```markdown
## Comunicado de incidente (inicial)

- Horário: {{YYYY-MM-DD HH:MM}}
- Nível: {{P0 / P1 / P2}}
- Sintoma: {{用户可感知的现象，不写内部细节}}
- Impacto: {{受影响范围}}
- Medidas em curso: {{正在做什么}}
- Próxima atualização: {{HH:MM}}

## Comunicado de incidente (recuperação)

- Horário de recuperação: {{HH:MM}}
- Confirmação da recuperação: {{验证方式与结果}}
- Impacto remanescente: {{无 / 描述}}
- Próximos passos: {{复盘安排}}
```

## 4. Definição de campos

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Número do incidente | Sim | `INC-YYYYMMDD-NN` | Número sequencial do dia, contínuo e sem reutilização | `INC-20261118-01` |
| Nível do incidente | Sim | Enumeração | P0 / P1 / P2 | `P1` |
| Duração | Sim | Duração | Minutos entre a detecção e a recuperação | `42 minutos` |
| Comandante | Sim | Texto | Único, responsável pela decisão e pela sincronização | `Li Si` |
| Proporção de usuários afetados | Sim | Texto | Deve apresentar a base da estimativa | `cerca de 8%, com base na contagem de logs de erro` |
| Linha do tempo | Sim | Tabela | Cada nó deve conter horário e origem | ver modelo |
| Causa fundamental | Sim | Texto | Distinguir causa direta de causa fundamental | `ausência de simulação de reversão` |
| Item de melhoria.forma de verificação | Sim | Texto | Verificável, com limite | `reversão em <5 minutos na próxima simulação` |
| Próxima atualização | Sim | Horário | Obrigatório em tratamento; proibido “atualização a qualquer momento” | `18:30` |

## 5. Instruções de preenchimento

1. **Classificação**: classificar segundo o alcance e a gravidade do impacto; em caso de dúvida, classificar pelo nível mais alto e ajustar depois, registrando o motivo.
2. **Contenção prioritária**: primeiro restaurar o serviço (reversão, degradação, limitação de taxa) e depois localizar a causa raiz; a localização não deve atrasar a contenção.
3. **Linha do tempo**: registrar em ordem cronológica de ocorrência, com origem verificável (ID de alerta, comando, trecho de log); é proibido complementar de memória após o fato.
4. **Causa raiz**: a causa direta é o evento desencadeador e a causa fundamental é a deficiência sistêmica; ambas devem ser preenchidas.
5. **Comunicação**: o comunicado inicial deve indicar a próxima atualização; o comunicado de recuperação deve explicar a forma de verificação e o impacto remanescente.
6. **Itens de melhoria**: no máximo três, incorporados ao roteiro para acompanhamento; itens sem responsável não devem constar do relatório.
7. **Retrospectiva**: focar na melhoria do sistema e dos processos, sem avaliar pessoas; não imputar responsabilidade nem escrever expressões como “fulano agiu com descuido”.
8. **Incidentes especiais**: o vazamento de chaves é tratado conforme H12; o push acidental de arquivos grandes é tratado com migração para LFS; ambos devem ter registro próprio.

Erros comuns:

| Redação incorreta | Problema | Forma de correção |
| --- | --- | --- |
| Localizar a causa raiz antes de conter | Prolonga a duração da falha | Reverter e restaurar primeiro |
| Complementar a linha do tempo depois | Fatos não confiáveis | Registrar imediatamente durante o tratamento |
| Escrever na causa raiz “alguém foi descuidado” | Imputa culpa individual e não gera melhoria | Investigar até o nível do processo ou da ferramenta |
| Escrever no comunicado “correção o quanto antes” | Sem próxima atualização definida | Informar um horário concreto |
| Item de melhoria sem forma de verificação | Fechamento não verificável | Acrescentar limite e momento de checagem |

## 6. Exemplo completo

```markdown
# Relatório de incidente: INC-20261118-01

- Nível do incidente: P1
- Horário de detecção: 2026-11-18 10:12
- Horário de recuperação: 2026-11-18 10:54
- Duração: 42 minutos
- Comandante: Li Si
- Estado atual: com retrospectiva concluída

## Alcance do impacto
| Dimensão | Descrição |
| --- | --- |
| Funcionalidade afetada | A interface de verificação de regras retorna 5xx |
| Proporção de usuários afetados | cerca de 8%, com base na contagem de logs 5xx |
| Impacto nos dados | nenhum |
| Impacto no negócio | impossibilidade de enviar tarefas de verificação por 42 minutos |

## Causa raiz
- Causa direta: o caminho de carregamento do plug-in de regras foi sobrescrito pela nova configuração, causando falha na inicialização.
- Causa fundamental: a alteração de configuração não foi incorporada à verificação de pré-lançamento.

## Itens de melhoria
| Número | Ação | Responsável | Prazo | Forma de verificação | Estado |
| --- | --- | --- | --- | --- | --- |
| A-01 | Incorporar alterações de configuração à lista de verificação de pré-lançamento | Wang Wu | 2026-11-25 | as próximas 5 alterações devem conter registro de verificação | a iniciar |
```

## Arquivos relacionados

- Origem dos alertas e orientação de tratamento: [especificação de observabilidade](./observability-specification.md)
- Operação de reversão: [especificação de implantação e reversão](./deployment-and-rollback-specification.md)
- Tratamento de chaves e informações sensíveis: [especificação de segurança e privacidade](./security-and-privacy-specification.md)
- Arquivos grandes e reescrita de histórico: [especificação de push e publicação](./push-and-release-specification.md)
- Acompanhamento de itens de melhoria: [especificação de roteiro](./roadmap-specification.md)
- Retrospectiva de melhoria de processo: [especificação de retrospectiva de iteração](./iteration-retrospective-specification.md)
- Critérios de julgamento de alertas: [especificação de métricas de qualidade](./quality-metrics-specification.md)
