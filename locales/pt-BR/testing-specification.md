# Especificação de testes

> Problema que este arquivo resolve: definir a estratificação dos testes, o modelo e os campos do plano de testes e dos casos de teste, os critérios de cobertura e as normas de execução, garantindo que cada requisito seja verificável e cada alteração seja regressível.

## 1. Disposições normativas

1. Os testes dividem-se em três camadas: unidade, integração e ponta a ponta; cada camada deve indicar o objeto testado e o escopo não testado, evitando cobertura redundante.
2. Cada requisito de nível “obrigatório” deve ter ao menos um caso de teste correspondente; a relação de rastreamento está na [especificação de matriz de rastreabilidade de requisitos](./requirements-traceability-matrix-specification.md).
3. A correção de defeitos deve acrescentar primeiro o caso de regressão e depois alterar o código; o caso de regressão deve reproduzir o defeito original.
4. O limite de cobertura é definido por projeto e inserido na CI, não podendo ficar abaixo do limite estabelecido (corresponde à regra absoluta H9).
5. Os testes devem ser repetíveis e sem dependência de estado externo; dependências de serviços externos devem ser isoladas ou simuladas com mock.
6. A nomenclatura dos testes deve expressar o comportamento testado e o resultado esperado; testes, lint, format e verificação de tipos devem ser executados automaticamente na CI, e o merge só é permitido com tudo verde (ver [especificação de revisão de código](./code-review-specification.md)).

## 2. Estratificação dos testes

| Camada | Objeto testado | Deve cobrir | Não cobre | Ferramentas típicas |
| --- | --- | --- | --- | --- |
| Testes de unidade | Funções, módulos de lógica pura | Lógica central, condições de limite, ramos de exceção | Cooperação entre módulos, I/O externo | Runner nativo da linguagem |
| Testes de integração | Cooperação entre módulos | Cadeias de chamada críticas, adaptadores, interação com persistência | Fluxo completo do usuário | Contêiner de testes / mock server |
| Testes de ponta a ponta | Cenários completos do usuário | Caminhos principais de uso, ciclos de negócio críticos | Exaustão de ramos, teste de carga | Driver de navegador / CLI |

## 3. Modelo de plano de testes

```markdown
# Plano de testes: {{项目名称}} {{版本号}}

Versão: {{v1.0}} ｜ Escopo de requisitos correspondente: {{REQ-001 ~ REQ-020}} ｜ Responsável: {{姓名}}

## Escopo dos testes
- Incluído: {{模块 / 需求编号列表}}
- Excluído: {{不在本期验证的范围及原因}}
- Critérios de sucesso da iniciação relacionados: {{G1 / G2}}

## Estratégia por camada
| Camada | Objeto testado | Meta de cobertura | Ferramenta | Momento de execução |
| --- | --- | --- | --- | --- |
| Unidade | {{对象}} | {{覆盖率阈值}} | {{工具}} | A cada commit |
| Integração | {{对象}} | {{关键链路清单}} | {{工具}} | A cada merge |
| Ponta a ponta | {{场景}} | {{主要路径清单}} | {{工具}} | A cada publicação |

## Ambiente e dados
- Ambiente: {{操作系统 / 运行时版本 / 依赖服务版本}}
- Dados de teste: {{构造方式；禁止使用生产敏感数据}}
- Dependências externas: {{需 mock 的服务及隔离方式}}

## Entrada e saída
- Entrada: {{进入测试的前置条件，如开发自测通过}}
- Saída: {{通过率 100%、无 P0/P1 缺陷、覆盖率达标}}
- Condições de pausa: {{阻塞性问题清单}}

## Riscos e decisões de compromisso
- Escopo não testado e motivo: {{例如第三方付费接口以 mock 替代}}
- Risco conhecido: {{例如并发场景仅做 10 路验证}}
```

## 4. Modelo de caso de teste

```markdown
### TC-{{三位序号}}: {{用例标题}}

- Requisitos relacionados: {{REQ-001}}
- Camada: {{单元 / 集成 / 端到端}}
- Prioridade: {{P0 / P1 / P2}}
- Tipo: {{正常 / 边界 / 异常}}
- Pré-condições: {{环境与数据准备}}
- Passos e resultados esperados:
  | Passo | Operação | Resultado esperado |
  | --- | --- | --- |
  | 1 | {{操作}} | {{可判定的结果}} |
  | 2 | {{操作}} | {{可判定的结果}} |
- Limpeza: {{恢复环境的操作；无则写「无」}}
```

## 5. Definição de campos

### 5.1 Campos do plano de testes

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Escopo de requisitos correspondente | Sim | lista | Usar intervalo de números REQ | `REQ-001 ~ REQ-020` |
| Escopo excluído | Sim | texto | Indicar o motivo da não realização do teste | `API paga não testada: sem conta de teste` |
| Meta de cobertura | Sim | limite | A cobertura deve ser percentual numérica | `Cobertura de linhas ≥80%` |
| Momento de execução | Sim | enumeração | Commit / merge / publicação | `A cada merge` |
| Dados de teste | Sim | texto | Declarar a forma de construção; proibido usar dados sensíveis reais | `Gerado com fixture` |
| Condições de saída | Sim | texto | Verificável, incluindo limite de gravidade de defeitos | `Sem defeitos P0/P1 abertos` |

### 5.2 Campos do caso de teste

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Número | Sim | `TC-NNN` | Contínuo, sem reutilização | `TC-007` |
| Requisitos relacionados | Sim | lista | Ao menos um número REQ | `REQ-001` |
| Prioridade | Sim | enumeração | P0 / P1 / P2 | `P0` |
| Tipo | Sim | enumeração | Normal / limite / exceção | `Limite` |
| Passos e resultados esperados | Sim | tabela | Cada passo deve ter resultado verificável | Ver modelo |
| Limpeza | Sim | texto | Sem limpeza, escrever “nenhuma”; não deixar em branco | `Nenhuma` |

### 5.3 Critérios de cobertura

| Critério | Definição | Camada aplicável | Limite recomendado |
| --- | --- | --- | --- |
| Cobertura de linhas | Número de instruções executadas / total de instruções | Unidade | ≥80% |
| Cobertura de ramos | Número de ramos executados / total de ramos | Unidade | ≥70% |
| Cobertura de requisitos | Requisitos “obrigatórios” com caso de teste / total de requisitos “obrigatórios” | Todas as camadas | 100% |
| Cobertura de caminhos | Caminhos principais verificados / total de caminhos principais identificados | Ponta a ponta | 100% |

Observação sobre os critérios: a cobertura é um meio de descobrir áreas não testadas, não um objetivo de qualidade em si; cobertura alta não substitui a qualidade das asserções, que devem verificar comportamento e não apenas executar código.

## 6. Instruções de preenchimento

1. **Requisitos relacionados**: deve-se preencher o número REQ; casos sem vínculo devem ser migrados para o registro de testes exploratórios e não integram o conjunto formal de casos.
2. **Resultado esperado**: deve ser verificável. “Retorna o resultado correto” é inadequado; “retorna o status 200 e o campo `name` não vazio” é adequado.
3. **Distribuição de tipos**: cada requisito de nível “obrigatório” deve ter ao menos um caso normal e um caso de limite ou de exceção.
4. **Limpeza**: casos que envolvam arquivos, banco de dados ou estado global devem indicar os passos de limpeza; a ausência de limpeza torna o caso incompleto.
5. **Casos de regressão**: a correção de defeitos deve ser nomeada com o número do defeito como prefixo, por exemplo `TC-007-regression-142`.
6. **Isolamento**: os casos não devem depender da ordem de execução; os que compartilham estado devem reconstruí-lo nas pré-condições.

Erros comuns:

| Redação incorreta | Problema | Forma de correção |
| --- | --- | --- |
| Resultado esperado “funciona normalmente” | Não verificável | Indicar o valor de retorno ou o estado concreto |
| Caso sem requisito relacionado | Cadeia de rastreamento rompida | Acrescentar o número REQ |
| Testar apenas o caminho normal | Defeitos de limite não detectados | Acrescentar casos de exceção e de limite |
| Caso dependente do resultado do caso anterior | Execução não repetível | Reconstruir o estado nas pré-condições |
| Usar dados de produção nos testes | Risco de privacidade e de conformidade | Usar fixture |

## 7. Exemplo completo

```markdown
# Plano de testes: markdown-lint-cli v1.0

Versão: v1.0 ｜ Escopo de requisitos correspondente: REQ-001 ~ REQ-014 ｜ Responsável: Wang Wu

## Escopo dos testes
- Incluído: mecanismo de regras, análise de parâmetros da CLI, saída de relatórios (REQ-001 ~ REQ-014)
- Excluído: integração com plugin de editor (adiada para v1.1; sem requisito correspondente)
- Critérios de sucesso da iniciação relacionados: G1 e G2

## Estratégia por camada
| Camada | Objeto testado | Meta de cobertura | Ferramenta | Momento de execução |
| --- | --- | --- | --- | --- |
| Unidade | Funções de regra | Cobertura de linhas ≥85% | Runner nativo da linguagem | A cada commit |
| Integração | CLI → mecanismo de regras → relatório | 3 cadeias críticas | Contêiner de testes | A cada merge |
| Ponta a ponta | Verificação em lote em repositório real | 2 caminhos principais | Driver shell | A cada publicação |

### TC-001: detectar espaço ausente entre chinês e inglês
- Requisitos relacionados: REQ-001
- Camada: unidade
- Prioridade: P0
- Tipo: limite
- Pré-condições: carregar a regra `spacing`
- Passos e resultados esperados:
  | Passo | Operação | Resultado esperado |
  | --- | --- | --- |
  | 1 | Inserir 「使用Node.js开发」 | Retornar 1 ocorrência, linha 1 |
  | 2 | Inserir 「使用 Node.js 开发」 | Retornar 0 ocorrências |
- Limpeza: nenhuma
```

## Arquivos relacionados

- Rastreamento bidirecional entre requisito e caso de teste: [especificação de matriz de rastreabilidade de requisitos](./requirements-traceability-matrix-specification.md)
- Critérios por camada e definição de métricas: [especificação de métricas de qualidade](./quality-metrics-specification.md)
- Portão de entrada: [portão de qualidade](./quality-gate.md)
- Dimensão de revisão D6: [matriz de dimensões de revisão](./review-dimension-matrix.md)
- Configuração de execução automática na CI: [especificação de fluxo de trabalho de CI](./ci-workflow-specification.md)
- Execução local antes do commit: [especificação de push e publicação](./push-and-release-specification.md)
