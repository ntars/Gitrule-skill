# Especificação de observabilidade

> Problema que este arquivo resolve: definir os campos de log, as metas SLI/SLO, as regras de alerta e o modelo de cartão de resposta a alertas, garantindo visibilidade do estado do sistema, localização de falhas e alertas acionáveis.

## 1. Dispositivos normativos

1. A observabilidade é composta por três pilares: logs, métricas e rastreamento distribuído; os três devem estar correlacionados por um identificador de requisição unificado.
2. Os logs devem ser estruturados e conter carimbo de data/hora, nível e identificador de requisição; é proibido registrar informações sensíveis, e as regras de anonimização estão na [especificação de segurança e privacidade](./security-and-privacy-specification.md).
3. Cada serviço crítico deve definir SLI e SLO, com critério de cálculo e janela estatística.
4. As regras de alerta devem ter limite explícito, duração e responsável; alertas sem orientação de tratamento não devem entrar em produção.
5. Após o disparo, o alerta deve poder ser correlacionado à classificação e ao fluxo de tratamento da [especificação de resposta a incidentes](./incident-response-specification.md).
6. Os critérios das métricas devem ser unificados com a [especificação de métricas de qualidade](./quality-metrics-specification.md); é proibido usar o mesmo nome com significados diferentes.

## 2. Os três pilares e seus campos

| Pilar | Campos obrigatórios | Requisito | Chave de correlação |
| --- | --- | --- | --- |
| Logs | Carimbo de data/hora, nível, identificador de requisição, mensagem, contexto | Saída estruturada, com níveis apenas DEBUG/INFO/WARN/ERROR | `trace_id` |
| Métricas | Nome da métrica, rótulos, valor, momento de coleta | Critério e valor-alvo explícitos | `service` |
| Rastreamento distribuído | Identificador de rastreamento, identificador de span, span pai, duração, estado | Chamadas entre serviços encadeáveis | `trace_id` |

## 3. Modelo de campos de log

```markdown
| Campo | Tipo | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- | --- |
| timestamp | ISO 8601 | Sim | Hora UTC, com fuso horário | 2026-11-18T10:00:00Z |
| level | Enumeração | Sim | DEBUG / INFO / WARN / ERROR | ERROR |
| trace_id | String | Sim | Identificador único de toda a cadeia | 4bf92f3577b34da6 |
| service | String | Sim | Nome do serviço | lint-api |
| message | String | Sim | Descrição breve sem informações sensíveis | rule load failed |
| context | Objeto | Não | Campos de contexto que permitem localização | {"rule":"spacing"} |
```

## 4. Modelo de definição de SLI/SLO

```markdown
# Definição de SLO: {{服务名}}

Versão: {{v1.0}} ｜ Responsável: {{姓名}} ｜ Ciclo de revisão: {{每季度}}

## Fronteira do serviço
- Responsabilidade do serviço: {{一句话}}
- Serviços dependentes: {{上游 / 下游}}
- Operações críticas do usuário: {{列出 2–5 项}}

## Definição de SLI
| SLI | Definição | Critério de cálculo | Fonte de dados |
| --- | --- | --- | --- |
| Disponibilidade | Requisições bem-sucedidas / total de requisições | Código HTTP <500 é sucesso | {{监控面板}} |
| Latência | Distribuição do tempo de requisição | Valor do percentil P95 | {{监控面板}} |
| Taxa de erro | Requisições com falha / total de requisições | Contagem de 5xx | {{监控面板}} |

## Metas de SLO
| SLI | Valor-alvo | Janela estatística | Valor atual | Estado |
| --- | --- | --- | --- | --- |
| Disponibilidade | ≥99.9% | 30 dias móveis | {{值}} | {{达标 / 未达标}} |
| Latência P95 | <300ms | 7 dias móveis | {{值}} | {{达标 / 未达标}} |
| Taxa de erro | <0.1% | 24 horas móveis | {{值}} | {{达标 / 未达标}} |

## Orçamento de erro
- Forma de cálculo: {{1 - SLO 目标值，按统计窗口换算}}
- Alerta de consumo: {{消耗达 50% / 75% / 90% 时分别通知}}
- Estratégia de esgotamento: {{冻结非关键发布，优先修复稳定性}}
```

## 5. Modelo de regra de alerta

```markdown
### ALERT-{{三位序号}}: {{告警名称}}

- SLI relacionado: {{可用性 / 延迟 / 错误率}}
- Expressão: {{可执行的查询表达式}}
- Limite: {{数值 + 单位}}
- Duração: {{N 分钟}}
- Nível de severidade: {{P0 / P1 / P2}}
- Responsável: {{姓名 / 值班组}}
- Exemplo de disparo: {{给出一个会触发的样例数据}}
- Condição de silenciamento: {{何时允许静默，须有到期时间}}

Orientação de tratamento:
1. {{第一步：确认现象的数据源与命令}}
2. {{第二步：常见原因与对应处理}}
3. {{第三步：升级条件与升级对象}}
- Nível de incidente relacionado: {{见事故响应规范的分级表}}
```

## 6. Definição dos campos

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Definição de SLI | Sim | Texto | Deve ser uma proporção ou percentil calculável | Requisições bem-sucedidas / total de requisições |
| Critério de cálculo | Sim | Texto | Explicitar condições de inclusão e exclusão | Excluir requisições de verificação de saúde |
| Valor-alvo de SLO | Sim | Limite | Valor + unidade + percentual | `≥99.9%` |
| Janela estatística | Sim | Duração | Janela móvel; proibido usar “mês civil” de forma vaga | `30 dias móveis` |
| Orçamento de erro | Sim | Número | Deduzido do valor-alvo de SLO | `43 minutos de indisponibilidade permitidos por mês` |
| Expressão de alerta | Sim | Consulta | Colável e executável diretamente | `rate(http_5xx[5m]) > 0.01` |
| Duração | Sim | Duração | Evitar falsos positivos por oscilação momentânea | `5 minutos` |
| Orientação de tratamento | Sim | Lista | Ao menos 3 passos, incluindo condição de escalonamento | Ver modelo |
| Condição de silenciamento | Sim | Texto | Deve ter prazo de expiração | `Dentro da janela de publicação, no máximo 30 minutos` |

## 7. Instruções de preenchimento

1. **Escolha de SLI**: selecionar de 2 a 5 itens entre as dimensões perceptíveis ao usuário, sem substituir o SLI do usuário por métricas internas de recursos como CPU e memória.
2. **Unificação de critérios**: uma métrica com o mesmo nome deve usar o mesmo critério de cálculo em logs, painéis de monitoramento e expressões de alerta.
3. **Definição de metas**: a meta de SLO deve se basear nos valores medidos atuais e na tolerância do negócio; é proibido aplicar “quatro noves” sem justificativa.
4. **Orçamento de erro**: devem ser explicitados o resultado da conversão e as ações de consumo por faixa; ao esgotar o orçamento, congelar publicações não críticas.
5. **Alerta acionável**: cada alerta deve responder às três perguntas “o que observar, como investigar, quando escalonar”; faltando uma, não deve entrar em produção.
6. **Combate à fadiga de alertas**: alertas que não geraram tratamento efetivo por 30 dias consecutivos devem ter o nível reduzido ou ser excluídos, com justificativa registrada.
7. **Anonimização**: se os campos de contexto do log puderem conter chaves, tokens ou dados pessoais, a anonimização deve ocorrer antes da saída.

Erros comuns:

| Escrita incorreta | Problema | Forma de correção |
| --- | --- | --- |
| Usar uso de CPU como SLI | Não é perceptível ao usuário | Usar disponibilidade, latência e taxa de erro |
| Alerta dizendo apenas “anomalia no serviço” | Sem limite e sem orientação | Acrescentar expressão, limite e passos de tratamento |
| Log imprimindo o cabeçalho completo da requisição | Risco de vazamento de privacidade e chaves | Saída por lista de permissão dos campos necessários |
| Alerta sem prazo de silenciamento | Silenciamento longo causa omissão de alertas | Definir duração máxima de silenciamento |
| SLO sem janela estatística | Meta não verificável | Acrescentar janela móvel |

## 8. Exemplo completo

```markdown
# Definição de SLO: lint-api

Versão: v1.0 ｜ Responsável: Wang Wu ｜ Ciclo de revisão: trimestral

## Definição de SLI
| SLI | Definição | Critério de cálculo | Fonte de dados |
| --- | --- | --- | --- |
| Disponibilidade | Requisições bem-sucedidas / total de requisições | Código de status <500, excluindo verificação de saúde | Grafana lint-overview |
| Latência | Tempo de requisição de verificação P95 | Considera apenas o caminho /check | Grafana lint-overview |

## Metas de SLO
| SLI | Valor-alvo | Janela estatística | Valor atual | Estado |
| --- | --- | --- | --- | --- |
| Disponibilidade | ≥99.9% | 30 dias móveis | 99.94% | Atingida |
| Latência P95 | <300ms | 7 dias móveis | 268ms | Atingida |

## Orçamento de erro
- Forma de cálculo: 0.1% × 30 dias = 43 minutos/mês
- Alerta de consumo: 50% notifica o responsável, 75% notifica a equipe de plantão, 90% congela publicações não críticas
- Estratégia de esgotamento: suspender publicações de funcionalidades, permitindo apenas correções de estabilidade

### ALERT-001: taxa de erro 5xx acima do limite
- SLI relacionado: disponibilidade
- Expressão: `rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])`
- Limite: >0.01
- Duração: 5 minutos
- Nível de severidade: P1
- Responsável: Wang Wu
- Orientação de tratamento:
  1. Abrir o Grafana lint-overview e confirmar o serviço de origem do erro
  2. Consultar os logs ERROR e encadear a cadeia de chamadas por trace_id; a causa comum é falha no carregamento do plugin de regras
  3. Se não houver localização em 10 minutos, escalonar para Li Si e entrar no fluxo de incidente P1
```

## Arquivos relacionados

- Critérios e definições de métricas: [especificação de métricas de qualidade](./quality-metrics-specification.md)
- Fluxo de tratamento após o alerta: [especificação de resposta a incidentes](./incident-response-specification.md)
- Verificação de saúde na implantação: [especificação de implantação e reversão](./deployment-and-rollback-specification.md)
- Anonimização de logs e proteção de privacidade: [especificação de segurança e privacidade](./security-and-privacy-specification.md)
- Itens comuns de solução de problemas: [especificação de solução de problemas](./troubleshooting-specification.md)
