# Especificação de revisão de código

> Problema que este arquivo resolve: definir o modelo de descrição de pull request, o modelo de parecer de revisão, o registro de revisão, os campos e o fluxo, garantindo qualidade de merge e compartilhamento de conhecimento.

## 1. Dispositivos normativos

1. O autor deve explicar na descrição do PR a finalidade da alteração, o alcance do impacto e os resultados dos testes próprios; o modelo está na [especificação de fluxo de trabalho Git e branches](./git-workflow-and-branching-specification.md).
2. O revisor deve apresentar pareceres concretos e acionáveis, distinguindo “deve ser alterado” de “sugestão”.
3. Antes do merge, deve haver aprovação de pelo menos 1 revisor e a CI deve estar totalmente verde (correspondente à regra absoluta H9); é proibido que o autor aprove o próprio PR.
4. Havendo divergência nos pareceres de revisão, o caso deve ser escalado para decisão dos mantenedores (ver [especificação de código de conduta](./code-of-conduct-specification.md)).
5. Após o merge, o branch de origem deve ser excluído, mantendo a lista de branches organizada.

## 2. Lista de verificação de revisão

O revisor deve confirmar item por item:

| # | Dimensão | Pontos de verificação | Julgamento |
| --- | --- | --- | --- |
| 1 | Correção | Lógica correta, casos-limite e exceções tratados | Aprovado / Requer alteração |
| 2 | Testes | A alteração tem testes correspondentes e os testes passam | Aprovado / Requer alteração |
| 3 | Estilo | Em conformidade com a [especificação de estilo de código](./code-style-specification.md) | Aprovado / Requer alteração |
| 4 | Segurança | Sem informações sensíveis, sem risco de injeção, validação de permissões correta | Aprovado / Requer alteração |
| 5 | Documentação | Alterações de interface ou comportamento refletidas na documentação | Aprovado / Requer alteração |
| 6 | Escopo | Alteração focada, sem mudanças irrelevantes | Aprovado / Requer alteração |
| 7 | Mensagem de commit | Em conformidade com a [especificação de mensagens de commit](./commit-message-specification.md) | Aprovado / Requer alteração |
| 8 | Rastreabilidade | Matriz de rastreabilidade de requisitos atualizada | Aprovado / Requer alteração |

## 3. Modelo de parecer de revisão

```markdown
### Parecer {{序号}}: {{一句话标题}}

- Nível: {{必须修改 / 建议 / 提问}}
- Local: {{文件路径:行号}}
- Problema: {{描述可观察的问题，不评价人}}
- Fundamentação: {{规范条款 / 需求编号 / 风险说明}}
- Sugestão: {{具体的修改方式或替代方案}}

Exemplo:
### Parecer 1: ramo de exceção não coberto
- Nível: deve ser alterado
- Local: `src/rules/spacing.ts:42`
- Problema: quando a entrada contém Markdown incompleto, uma exceção é lançada e o resultado de acerto da regra não é retornado.
- Fundamentação: REQ-001, critério de aceitação 2 (caminho de fronteira).
- Sugestão: capturar a exceção de análise neste ponto e retornar um acerto como “falha de análise”, além de acrescentar um caso de teste de fronteira.
```

## 4. Modelo de registro de revisão

```markdown
## Registro de revisão: {{PR 编号}}

Revisor: {{姓名}} ｜ Data da revisão: {{YYYY-MM-DD}} ｜ Rodada: {{第 N 轮}}

| Número do parecer | Nível | Conclusão do tratamento | Responsável pelo tratamento | Forma de verificação |
| --- | --- | --- | --- | --- |
| 1 | deve ser alterado | Alterado | autor | ver commit abc1234 |
| 2 | sugestão | Não acatado | autor | motivo: {{说明}} |

Conclusão: {{批准 / 需修改后再审 / 拒绝}}
- Condição de aprovação: todos os itens “deve ser alterado” tratados e CI totalmente verde.
- Itens pendentes: {{无 / 列出}}
```

## 5. Definição de campos

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Nível | Sim | Enumeração | deve ser alterado / sugestão / questionamento | `deve ser alterado` |
| Local | Sim | `caminho:linha` | Preciso até a linha; proibido indicar apenas o nome do arquivo | `src/parser.ts:42` |
| Problema | Sim | Texto | Descrever o fenômeno, sem avaliar o autor | `exceção de análise não capturada` |
| Fundamentação | Sim | Texto | Dispositivo da especificação ou número de REQ | `REQ-001 critério de aceitação 2` |
| Sugestão | Sim | Texto | Acionável; não basta dizer “otimize” | `capturar a exceção e retornar o acerto` |
| Conclusão do tratamento | Sim | Enumeração | Alterado / Não acatado / Adiado | `Alterado` |
| Forma de verificação | Sim | Texto | Hash do commit ou forma de reconferência | `ver commit abc1234` |
| Conclusão | Sim | Enumeração | aprovado / requer alteração e nova revisão / rejeitado | `aprovado` |

## 6. Instruções de preenchimento

1. **Distinção de níveis**: “deve ser alterado” designa problemas que bloqueiam o merge (correção, segurança, ausência de testes); “sugestão” não afeta o merge; “questionamento” exige esclarecimento do autor, mas não requer alteração.
2. **Formulação do parecer**: descrever problemas observáveis; são proibidas linguagens avaliativas como “isto está muito mal escrito”.
3. **Local**: preciso até o número da linha; problemas que abrangem vários arquivos devem ser anotados separadamente em cada parecer.
4. **Fundamentação**: rastrear sempre que possível; na ausência de base normativa, explicitar o risco ou o impacto; é proibido “eu acho”.
5. **Conclusão do tratamento**: “não acatado” exige justificativa; “adiado” exige indicar o local de acompanhamento posterior.
6. **Aprovação**: confirmar que todos os itens “deve ser alterado” foram encerrados e que a CI está totalmente verde; o autor não deve aprovar o próprio PR.
7. **Divergência**: havendo discordância entre revisor e autor, escalar aos mantenedores, registrando a decisão no registro de revisão.

Erros comuns:

| Redação incorreta | Problema | Forma de correção |
| --- | --- | --- |
| “Isto não serve” | Sem problema, sem fundamentação, sem sugestão | Acrescentar os três elementos |
| “Sugiro otimizar o desempenho” | Não acionável | Apresentar a forma concreta e o indicador de julgamento |
| Indicar apenas o nome do arquivo, sem a linha | Dificulta a localização | Precisar até a linha |
| Aprovação pelo próprio autor | Violação das regras | Revisão por outra pessoa |
| Usar “deve ser alterado” para preferência pessoal | Uso indevido do nível | Rebaixar para “sugestão” |

## 7. Exemplo completo

```markdown
## Registro de revisão: #12

Revisor: Li Si ｜ Data da revisão: 2026-11-18 ｜ Rodada: 1ª rodada

| Número do parecer | Nível | Conclusão do tratamento | Responsável pelo tratamento | Forma de verificação |
| --- | --- | --- | --- | --- |
| 1 | deve ser alterado | Alterado | Wang Wu | ver commit a1b2c3d |
| 2 | sugestão | Não acatado | Wang Wu | motivo: o QPS atual ainda não atingiu o gargalo, evitando projeto excessivo |
| 3 | questionamento | Esclarecido | Wang Wu | explicação complementada no corpo do PR |

Conclusão: aprovado
- Condição de aprovação: todos os itens “deve ser alterado” tratados e CI totalmente verde (run #128).
- Itens pendentes: nenhum
```

## Arquivos relacionados

- Descrição de PR e modelo de branches: [especificação de fluxo de trabalho Git e branches](./git-workflow-and-branching-specification.md)
- Base da verificação de estilo: [especificação de estilo de código](./code-style-specification.md)
- Critério de aprovação de testes: [especificação de testes](./testing-specification.md)
- Atualização do estado de rastreabilidade: [especificação de matriz de rastreabilidade de requisitos](./requirements-traceability-matrix-specification.md)
- Portão de qualidade: [portão de qualidade](./quality-gate.md)
- Base para decisão de divergências: [especificação de código de conduta](./code-of-conduct-specification.md)
- A verificação automatizada pertence à dimensão D9: [matriz de dimensões de revisão](./review-dimension-matrix.md)
