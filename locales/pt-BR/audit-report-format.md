# Formato do relatório de auditoria

> Problema que este arquivo resolve: definir o formato único de entrega do relatório de auditoria, os requisitos de campos e os exemplos de preenchimento, garantindo que o relatório possa ser executado diretamente por outro agent.

O relatório é o único produto da etapa de auditoria. Cada problema deve apresentar simultaneamente evidência, responsável e ação; conclusões não executáveis não devem ser registradas no relatório.

## 1. Estrutura do relatório

````markdown
# Relatório de auditoria de push · {{仓库名}}

Conclusão: {{结论}}
Modo: {{模式}}
Repositório: {{仓库名}} · {{可见性}} · {{许可证}} · branch padrão {{默认分支}}

## I. Status dos portões
| Portão | Status | Pendências |
| --- | --- | --- |
| A Segurança | {{门禁状态}} | {{未决项}} |
| B Qualidade | {{门禁状态}} | {{未决项}} |
| C Página inicial | {{门禁状态}} | {{未决项}} |

## II. Lista de problemas
| Nível | Dimensão | Problema | Evidência (caminho:linha / saída de comando) | Agent responsável | Ação |
| --- | --- | --- | --- | --- | --- |
| {{等级}} | {{维度}} | {{问题}} | {{证据}} | {{责任agent}} | {{动作}} |

## III. Status da matriz de documentação
| Arquivo | Status | Itens ausentes/a alterar |
| --- | --- | --- |
| {{文件路径}} | {{状态}} | {{待改项}} |

## IV. Lista de execução do push
- [ ] {{推送规则}}

## V. Nota de liberação
{{放行说明}}
````

## 2. Definição dos campos

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Nome do repositório | Sim | Texto | Idêntico, caractere a caractere, ao nome do repositório no GitHub | `markdown-lint-cli` |
| Conclusão | Sim | Enumeração | Apenas `ALLOW PUSH` ou `BLOCK PUSH`; com P0 pendente deve ser a segunda | `BLOCK PUSH` |
| Modo | Sim | Enumeração | Repositórios privados de scripts temporários podem usar “auditoria simplificada”; os demais, “auditoria completa” | `auditoria completa` |
| Visibilidade | Sim | Enumeração | `private` / `public`; antes de tornar público, revisar a licença | `private` |
| Licença | Sim | Identificador SPDX | Sem licença, escrever `NONE`, e nesse caso a conclusão deve ser `BLOCK PUSH` | `MIT` |
| Branch padrão | Sim | Texto | Escrever o nome real do branch, não presumir `main` | `main` |
| Status dos portões | Sim | Enumeração ×3 | Uma linha para A/B/C; `SKIP` deve indicar o motivo em “Pendências” | `FAIL` |
| Pendências | Condicionalmente obrigatório | Texto | Obrigatório quando o status for `FAIL` ou `SKIP`; listar o motivo do bloqueio ou da omissão | `D1 detectou .env` |
| Nível | Sim | Enumeração | `P0` bloqueia / `P1` corrigir ou registrar antes do push / `P2` sugestão | `P0` |
| Dimensão | Sim | `D1`–`D14` | Numeração conforme a [matriz de dimensões de revisão](./review-dimension-matrix.md) | `D1` |
| Problema | Sim | Texto | Uma frase que expõe o fato, sem suposições nem linguagem emocional | `Existe um .env na raiz` |
| Evidência | Sim | caminho:linha ou saída de comando | Deve ser verificável; quando não for possível obter evidência, escrever `SKIP + motivo` | `.env:3` |
| Agent responsável | Sim | Nome do agent | Escrever o papel executor concreto, não “pessoas envolvidas” | `security-auditor` |
| Ação | Sim | Texto | Operação diretamente executável, com o arquivo de destino | `Excluir .env, rotacionar a chave e limpar o histórico` |
| Caminho do arquivo | Sim | Texto | Listar item a item conforme a [matriz de documentação](./document-matrix.md) | `SECURITY.md` |
| Status da matriz de documentação | Sim | Tabela, linha a linha | Marcar por arquivo se existe, se falta ou se precisa de alteração | `SECURITY.md ausente` |
| Lista de execução do push | Sim | Lista de caixas de seleção | Detalhar regra a regra conforme a [especificação de push e publicação](./push-and-release-specification.md) | `- [ ] Confirmar que o .gitignore está em vigor` |
| Nota de liberação | Sim | Texto | Em caso de bloqueio, escrever o motivo e as condições de liberação; em caso de liberação, escrever as regras absolutas atendidas | `Pode ser revisado após zerar os P0` |

## 3. Instruções de preenchimento

1. **Conclusão primeiro**: avaliar primeiro a quantidade de P0 e depois escrever a conclusão. Com qualquer P0 pendente, não deve ser emitido `ALLOW PUSH`.
2. **Evidência obrigatória**: cada problema deve ter `caminho:linha` ou saída de comando copiável. Conclusões sem evidência devem ser marcadas como `SKIP` com o motivo indicado, nunca como `PASS`.
3. **Responsabilidade por papel**: o agent responsável deve usar os nomes de papel da [matriz de dimensões de revisão](./review-dimension-matrix.md), com um responsável por problema.
4. **Ação executável**: a ação deve indicar o arquivo de destino e o tipo de operação; “tratar depois” e “ajustar por conta própria” são considerados inválidos.
5. **Portões coerentes**: o status das três linhas A/B/C deve corresponder à lista de problemas; com qualquer portão em `FAIL`, a conclusão deve ser `BLOCK PUSH`.
6. **Matriz de documentação item a item**: listar arquivo por arquivo conforme a matriz, sem escrever apenas “a documentação está basicamente completa”.
7. **Lista detalhada**: a lista de execução do push deve detalhar as regras uma a uma, sem substituí-las por “executar conforme a especificação”.

Erros comuns:

| Redação incorreta | Problema | Forma de correção |
| --- | --- | --- |
| Escrever “possivelmente há problema” na coluna de evidência | Sem caminho e sem saída de comando, não é verificável | Incluir `caminho:linha` ou saída de comando |
| Escrever `ALLOW PUSH` com P0 pendente | Viola as regras absolutas | Alterar para `BLOCK PUSH` e indicar as condições de liberação |
| Escrever `PASS` em item que não pôde ser verificado | Resultado inventado | Escrever `SKIP` e indicar o motivo em Pendências |
| Responsável escrito como “pessoas envolvidas” | Sem sujeito responsável | Escrever o nome concreto do agent |
| Ação escrita como “tratar depois” | Não executável | Indicar o arquivo de destino e a operação concreta |
| Branch padrão escrito como `main` sem verificação | Divergente do real | Usar a saída de `git branch` como referência |

## 4. Exemplo completo

A seguir, um exemplo completo de preenchimento com `BLOCK PUSH`:

````markdown
# Relatório de auditoria de push · markdown-lint-cli

Conclusão: BLOCK PUSH
Modo: auditoria completa
Repositório: markdown-lint-cli · private · NONE · branch padrão main

## I. Status dos portões
| Portão | Status | Pendências |
| --- | --- | --- |
| A Segurança | FAIL | D1 detectou .env; D2 sem LICENSE |
| B Qualidade | SKIP | O repositório não tem dependências instaladas; build e testes não puderam ser executados |
| C Página inicial | FAIL | O README não tem seção de instalação nem exemplo mínimo |

## II. Lista de problemas
| Nível | Dimensão | Problema | Evidência (caminho:linha / saída de comando) | Agent responsável | Ação |
| --- | --- | --- | --- | --- | --- |
| P0 | D1 | Existe um .env na raiz | `.env:3` contém DATABASE_URL | security-auditor | Excluir .env, rotacionar as credenciais do banco e limpar o histórico |
| P0 | D2 | Não há arquivo de licença | `ls LICENSE` retorna `No such file or directory` | license-checker | Após o proprietário do repositório confirmar a licença, gerar o LICENSE |
| P1 | D13 | O README não tem seção de instalação | `README.md:1-28` não tem título “instalação” | readme-writer | Acrescentar instalação e exemplo mínimo conforme o modelo padrão de README |

## III. Status da matriz de documentação
| Arquivo | Status | Itens ausentes/a alterar |
| --- | --- | --- |
| README.md | A alterar | Falta a seção de instalação e o exemplo mínimo |
| LICENSE | Ausente | Aguarda confirmação do tipo de licença pelo proprietário |
| SECURITY.md | Ausente | Ainda não criado |

## IV. Lista de execução do push
- [ ] Confirmar que o git status está limpo
- [ ] Executar a varredura completa de chaves (incluindo commits históricos)
- [ ] Passar localmente em build, test e lint
- [ ] Matriz de documentação completa

## V. Nota de liberação
Motivo do bloqueio: existem 2 itens P0 (vazamento de credenciais e ausência de licença), e o portão de qualidade não pôde ser avaliado porque as dependências não estão instaladas. Condições de liberação: concluir a rotação de chaves e a limpeza do histórico, definir a licença, repetir os testes em um ambiente que permita compilar e revisar após zerar os P0.
````

Em caso de `ALLOW PUSH`, a quinta seção pode dizer: “Todas as regras absolutas foram atendidas e os três portões estão em PASS; o push pode ser executado.” As demais seções devem ser preenchidas conforme a situação real, sem omitir evidências e listas.

## 5. Ordem de entrega

1. Conteúdo completo da navegação de idiomas do README raiz.
2. Conteúdo completo do README de cada diretório de idioma já concluído, listando um a um o código de idioma e o caminho do arquivo.
3. Conteúdo do arquivo NOTICE.
4. Explicação da proposta de LICENSE (se o usuário não indicou uma licença, apresentar apenas candidatas e diferenças, sem gerar o arquivo diretamente).
5. Resumo dos itens pendentes de confirmação.
6. Relatório de auditoria (este relatório).
7. Orientações de push no GitHub.

## Arquivos relacionados

- Determinação do status dos portões, ver o [portão de qualidade](./quality-gate.md)
- Numeração das dimensões na lista de problemas, ver a [matriz de dimensões de revisão](./review-dimension-matrix.md)
- Status da matriz de documentação, ver a [matriz de documentação](./document-matrix.md)
- A lista de execução do push vem da [especificação de push e publicação](./push-and-release-specification.md)
- Forma de despacho, ver o [contrato de despacho de subagentes](./sub-agent-dispatch-contract.md)
