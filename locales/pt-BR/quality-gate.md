# Portão de qualidade

> Problema que este arquivo resolve: definir as condições de liberação dos três níveis de portão, o modelo de lista de decisão e seus campos, garantindo que a decisão de liberação do push seja uniforme, executável e passível de reverificação.

## 1. Três níveis de portão

| Camada | Significado | Condição de liberação |
| --- | --- | --- |
| Gate A · portão de segurança | Chaves, privacidade, licença, arquivos grandes | Zero P0 |
| Gate B · portão de qualidade | Build, testes, lint, convenção de commits, proteção de branch | Zero P0 e P1 registrado como pendência |
| Gate C · portão da página inicial | README, metadados, matriz de documentação, selos, links | Zero P0 e P1 ≤ 3 já agendado |

Somente com A, B e C verdes deve ser emitido `✅ ALLOW PUSH`. Os itens não aprovados devem ser corrigidos ou ter o motivo indicado, e o resultado deve ser registrado no [formato do relatório de auditoria](./audit-report-format.md).

## 2. Decisão dos 14 itens antes da entrega

Antes da entrega da documentação, decidir item a item; os itens não aprovados devem ser corrigidos ou ter o motivo indicado.

| Número | Item de verificação | Critério de decisão |
| --- | --- | --- |
| G1 | Coloquialismo e ambiguidade | Pesquisa no texto integral por termos coloquiais e referências vagas, com contagem de ocorrências igual a 0 |
| G2 | Integridade das seções | As versões em chinês e em inglês têm 20 seções cada, na mesma ordem |
| G3 | Coerência entre funcionalidades e diretórios | Toda funcionalidade descrita no README tem módulo correspondente na estrutura de diretórios |
| G4 | Evidência das características | Cada característica tem evidência ou está marcada como pendente |
| G5 | Cobertura dos detalhes de design | Cada uma das 10 categorias da seção 8 tem item ou indicação de não aplicável |
| G6 | Integridade das dependências | A quantidade de dependências diretas e indiretas é coerente com a árvore de dependências |
| G7 | Exatidão da licença | O identificador SPDX de cada dependência é coerente com a declaração oficial |
| G8 | Texto integral da licença | Todas as licenças que exigem texto integral o têm, em inglês |
| G9 | Declaração de copyright | As declarações de copyright do próprio projeto e de terceiros estão completas |
| G10 | Sincronia bilíngue | Seções, tabelas, terminologia e blocos de código idênticos nos dois lados |
| G11 | Executabilidade dos comandos | Os comandos de instalação, início rápido e push são executáveis diretamente |
| G12 | Consolidação de pendências de confirmação | Todos os itens pendentes de confirmação estão consolidados e sua localização é identificável |
| G13 | Origem dos materiais | Todos os materiais têm origem e registro de licença |
| G14 | Informações sensíveis | Ausência de chaves, tokens, endereços de rede interna e informações pessoais privadas |

## 3. Modelo de lista de decisão do portão

```markdown
# Decisão do portão: {{项目名称}} {{版本号}}

Data da decisão: {{YYYY-MM-DD}} ｜ Responsável pela decisão: {{姓名}} ｜ Repositório: {{owner/repo}}

## Gate A · portão de segurança
| Número | Item de verificação | Conclusão | Evidência | Nível | Tratamento |
| --- | --- | --- | --- | --- | --- |
| A1 | Chaves na área de trabalho | PASS / FAIL / SKIP | {{命令输出}} | {{P0}} | {{动作}} |
| A2 | Chaves no histórico | PASS / FAIL / SKIP | {{命令输出}} | {{P0}} | {{动作}} |
| A3 | Limpeza de informações sensíveis | PASS / FAIL / SKIP | {{证据}} | {{P0}} | {{动作}} |
| A4 | Existência e tipo de LICENSE | PASS / FAIL / SKIP | {{路径}} | {{P0}} | {{动作}} |
| A5 | Arquivos grandes e LFS | PASS / FAIL / SKIP | {{命令输出}} | {{P0}} | {{动作}} |

Conclusão: {{PASS / FAIL}}, itens pendentes: {{列出 / 无}}

## Gate B · portão de qualidade
| Número | Item de verificação | Conclusão | Evidência | Nível | Tratamento |
| --- | --- | --- | --- | --- | --- |
| B1 | Build aprovado | PASS / FAIL / SKIP | {{CI URL}} | {{P0}} | {{动作}} |
| B2 | Testes aprovados | PASS / FAIL / SKIP | {{CI URL}} | {{P0}} | {{动作}} |
| B3 | lint / format | PASS / FAIL / SKIP | {{CI URL}} | {{P1}} | {{动作}} |
| B4 | Convenção de mensagens de commit | PASS / FAIL / SKIP | {{git log}} | {{P1}} | {{动作}} |
| B5 | Proteção de branch | PASS / FAIL / SKIP | {{平台设置截图说明}} | {{P0}} | {{动作}} |

Conclusão: {{PASS / FAIL}}, itens pendentes: {{列出 / 无}}

## Gate C · portão da página inicial
| Número | Item de verificação | Conclusão | Evidência | Nível | Tratamento |
| --- | --- | --- | --- | --- | --- |
| C1 | Quatro elementos do README | PASS / FAIL / SKIP | {{路径:行号}} | {{P1}} | {{动作}} |
| C2 | Matriz de documentação completa | PASS / FAIL / SKIP | {{清单}} | {{P1}} | {{动作}} |
| C3 | Metadados completos | PASS / FAIL / SKIP | {{平台设置}} | {{P1}} | {{动作}} |
| C4 | Selos funcionais | PASS / FAIL / SKIP | {{HTTP 检查}} | {{P2}} | {{动作}} |
| C5 | Links válidos | PASS / FAIL / SKIP | {{校验输出}} | {{P1}} | {{动作}} |

Conclusão: {{PASS / FAIL}}, itens pendentes: {{列出 / 无}}

## Decisão dos 14 itens antes da entrega
| Número | Conclusão | Evidência | Tratamento |
| --- | --- | --- | --- |
| G1 ~ G14 | {{PASS / FAIL / SKIP}} | {{证据}} | {{动作}} |

## Decisão geral
- A: {{PASS / FAIL}} ｜ B: {{PASS / FAIL}} ｜ C: {{PASS / FAIL}}
- Conclusão de liberação: {{✅ ALLOW PUSH / ⛔ BLOCK PUSH}}
- Motivo do bloqueio: {{无 / 列出 P0}}
```

## 4. Definição de campos

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Responsável pela decisão | Sim | Texto | Único; é proibido usar “equipe” | `Wang Wu` |
| Conclusão | Sim | Enumerado | PASS / FAIL / SKIP | `PASS` |
| Evidência | Sim | Texto | Caminho + número de linha ou saída de comando; é proibida decisão sem evidência | `gitleaks: 0 findings` |
| Nível | Obrigatório sob condição | Enumerado | Obrigatório em caso de FAIL: P0 / P1 / P2 | `P0` |
| Tratamento | Obrigatório sob condição | Texto | Obrigatório em caso de FAIL: ação concreta e responsável | `Rotacionar a chave e limpar o histórico` |
| Motivo do SKIP | Obrigatório sob condição | Texto | Obrigatório em caso de SKIP; é proibido pular sem justificativa | `Sem script de build` |
| Conclusão de liberação | Sim | Enumerado | ALLOW PUSH / BLOCK PUSH | `BLOCK PUSH` |
| Motivo do bloqueio | Obrigatório sob condição | Texto | Obrigatório em caso de BLOCK, com a lista de P0 | `A2 com chave encontrada no histórico` |

## 5. Instruções de preenchimento

1. **Evidência obrigatória**: toda decisão deve ter evidência; um PASS sem evidência é considerado inválido e deve ser alterado para SKIP com indicação do motivo.
2. **Correspondência de níveis**: um FAIL deve ter nível indicado; P0 bloqueia diretamente a liberação, P1 deve ser registrado como pendência e P2 entra como sugestão.
3. **Limite do Gate C**: somente P1 ≤ 3 e já agendado permite PASS; acima disso, deve-se tratar como degradação ou bloquear.
4. **Uso do SKIP**: quando não for possível verificar, marcar SKIP + motivo, nunca PASS; reavaliar quando as condições estiverem atendidas.
5. **Consistência**: a decisão do portão deve ser coerente com os níveis P0/P1/P2 da [matriz de dimensões de revisão](./review-dimension-matrix.md) e com as regras de bloqueio das [regras absolutas](./hard-rules.md).
6. **Liberação**: somente com os três itens verdes deve ser emitido `✅ ALLOW PUSH`; qualquer FAIL emite `⛔ BLOCK PUSH`, com a lista dos motivos de bloqueio.
7. **Formato de entrega**: o resultado da decisão deve ser emitido conforme o [formato do relatório de auditoria](./audit-report-format.md); após a aprovação, executar a [especificação de push e publicação](./push-and-release-specification.md).

Erros frequentes:

| Redação incorreta | Problema | Forma de correção |
| --- | --- | --- |
| Conclusão PASS com evidência vazia | Decisão inválida | Acrescentar evidência ou alterar para SKIP |
| P0 não zerado com ALLOW PUSH | Violação das regras absolutas | Alterar para BLOCK PUSH |
| SKIP sem motivo | Suspeita de omissão na verificação | Acrescentar o motivo |
| Gate C com 5 itens P1 e PASS | Acima do limite | Degradar ou bloquear |
| Resultado da decisão apenas em texto, sem lista | Não reverificável | Preencher item a item no modelo |

## 6. Exemplo completo

```markdown
# Decisão do portão: markdown-lint-cli v1.0.0

Data da decisão: 2026-11-20 ｜ Responsável pela decisão: Wang Wu ｜ Repositório: example/markdown-lint-cli

## Gate A · portão de segurança
| Número | Item de verificação | Conclusão | Evidência | Nível | Tratamento |
| --- | --- | --- | --- | --- | --- |
| A1 | Chaves na área de trabalho | PASS | gitleaks detect: 0 findings | — | — |
| A2 | Chaves no histórico | PASS | gitleaks --log-opts=--all: 0 findings | — | — |
| A4 | Existência e tipo de LICENSE | PASS | LICENSE linha 1 MIT | — | — |
| A5 | Arquivos grandes e LFS | PASS | find -size +50M: nenhum | — | — |

Conclusão: PASS, itens pendentes: nenhum

## Gate B · portão de qualidade
| Número | Item de verificação | Conclusão | Evidência | Nível | Tratamento |
| --- | --- | --- | --- | --- | --- |
| B1 | Build aprovado | PASS | run #128 | — | — |
| B2 | Testes aprovados | PASS | 132/132 passed | — | — |
| B4 | Convenção de mensagens de commit | PASS | git log --oneline integralmente conforme | — | — |

Conclusão: PASS, itens pendentes: nenhum

## Decisão geral
- A: PASS ｜ B: PASS ｜ C: PASS
- Conclusão de liberação: ✅ ALLOW PUSH
- Motivo do bloqueio: nenhum
```

## Arquivos relacionados

- Base da decisão e níveis de falha: [matriz de dimensões de revisão](./review-dimension-matrix.md)
- Regras cuja violação bloqueia: [regras absolutas](./hard-rules.md)
- Formato de saída do resultado da decisão: [formato do relatório de auditoria](./audit-report-format.md)
- Execução após a aprovação do portão: [especificação de push e publicação](./push-and-release-specification.md)
- Origem das evidências do portão de segurança: [especificação de segurança e privacidade](./security-and-privacy-specification.md)
- Origem das evidências do portão de qualidade: [especificação de testes](./testing-specification.md), [especificação de fluxo de trabalho de CI](./ci-workflow-specification.md)
- Base de decisão do portão da página inicial: [modelo padrão de README](./readme-standard-template.md), [matriz de documentação](./document-matrix.md)
