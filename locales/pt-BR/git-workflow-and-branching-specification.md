# Especificação de fluxo de trabalho de Git e de branches

> Problema que este arquivo resolve: definir o modelo de branches, as regras de nomenclatura, o modelo de descrição de pull requests e a estratégia de merge, garantindo linha principal estável, colaboração ordenada e alterações rastreáveis.

## 1. Cláusulas da especificação

1. O branch padrão (`main` ou `master`) deve ser protegido; é proibido o push direto (corresponde à regra absoluta H7).
2. Todas as alterações são integradas à linha principal por meio de branch pessoal + pull request.
3. Branches de longa duração e de curta duração devem ser claramente delimitados, evitando branches que permanecem longo tempo sem merge.
4. É proibido `git push --force` em branches públicos; para reescrever branches pessoais usa-se `--force-with-lease` (corresponde a H8).
5. É proibido fazer rebase/amend em branches públicos já enviados por push; antes do merge, a CI e a revisão de código devem ser aprovadas.

## 2. Modelo de branches

| Tipo de branch | Ciclo de vida | Criado a partir de | Merge em | Formato de nome | Exemplo |
| --- | --- | --- | --- | --- | --- |
| Branch padrão | Longo | — | — | `main` | `main` |
| Branch de funcionalidade | Curto, ≤2 semanas | `main` | `main` | `feat/<descrição breve>` | `feat/user-login` |
| Branch de correção | Curto, ≤1 semana | `main` | `main` | `fix/<descrição breve>` | `fix/token-expiry` |
| Branch de documentação | Curto | `main` | `main` | `docs/<descrição breve>` | `docs/api-guide` |
| Branch de publicação | Médio | `main` | `main` + tag | `release/<versão>` | `release/1.2.0` |
| Correção emergencial | Curto, ≤24 horas | tag de publicação | `main` + tag | `hotfix/<descrição breve>` | `hotfix/payment-error` |

Regras de nomenclatura: kebab-case em minúsculas; a descrição breve deve expressar a intenção; são proibidos `test`, `temp`, `wip`, `my-xxx`; ao vincular a um requisito, acrescenta-se o número do requisito, por exemplo `feat/spacing-rule-req001`.

## 3. Modelo de descrição de pull request

```markdown
## Propósito da alteração
{{一句话说明为什么需要此变更，关联需求编号}}

## Conteúdo da alteração
- {{具体改动 1}}
- {{具体改动 2}}

## Escopo de impacto
- Módulos afetados: {{模块名}}
- Rompe a compatibilidade: {{是 / 否；是则给出迁移说明}}
- Envolve configuração ou migração de dados: {{是 / 否；是则说明}}

## Forma de verificação
- Comando de autoteste: {{命令}}
- Testes adicionados ou alterados: {{TC 编号}}
- Endereço de execução da CI: {{URL}}

## Vinculações
- Requisito: {{REQ-NNN}}
- Matriz de rastreabilidade: {{已更新 / 待更新}}
- Documentação: {{docs/api.md#章节 / 无}}
- Issue: {{#编号 / 无}}

## Autoverificação
- [ ] A mensagem de commit está em conformidade com a especificação
- [ ] Não contém informações sensíveis
- [ ] A matriz de rastreabilidade de requisitos foi atualizada
- [ ] Alterações disruptivas foram registradas no registro de alterações
```

## 4. Definição dos campos

| Campo | Obrigatório | Tipo | Pontos principais de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Descrição breve do branch | Sim | kebab-case | Deve expressar a intenção de forma autônoma; proibidas palavras sem informação | `spacing-rule` |
| Requisito vinculado | Sim | `REQ-NNN` | Consistente com o número da iniciação do projeto | `REQ-001` |
| Propósito da alteração | Sim | Texto | Explicar “por quê”, não “o que foi alterado” | `Corrige falso positivo de pontuação chinesa` |
| Escopo de impacto | Sim | Texto | Deve explicitar se rompe a compatibilidade | `Não` |
| Comando de autoteste | Sim | Comando | Copiável e executável | `npm test -- -t spacing` |
| Número do teste | Sim | `TC-NNN` | Consistente com a numeração da especificação de testes | `TC-001` |
| Endereço da CI | Sim | URL | Facilita a verificação pelo revisor | `https://github.com/.../runs/123` |
| Lista de autoverificação | Sim | Marcação | Marcar item a item; proibido marcar tudo de uma vez | — |

## 5. Instruções de preenchimento

1. **Ciclo de vida do branch**: branches de funcionalidade não integrados após 2 semanas devem ter o motivo explicado na retrospectiva de iteração e ser divididos ou encerrados.
2. **Nomenclatura da descrição breve**: extrair o substantivo central + ação do propósito da alteração; proibidos nomes vagos como `fix2`, `new-feature`.
3. **Propósito da alteração**: escrever o problema e o valor; “atualizar código” e “otimizar lógica” são inaceitáveis.
4. **Escopo de impacto**: ao marcar rompimento de compatibilidade, deve-se também indicar `BREAKING CHANGE:` no registro de alterações.
5. **Comando de autoteste**: o revisor deve poder copiá-lo e executá-lo diretamente, obtendo a mesma conclusão; para etapas complexas, indicar o caminho do script.
6. **Matriz de rastreabilidade**: antes do merge do PR, os campos de PR de implementação e de status na [especificação da matriz de rastreabilidade de requisitos](./requirements-traceability-matrix-specification.md) devem ser atualizados.
7. **force push**: usar `--force-with-lease` apenas em branches próprios ainda não revisados por terceiros, e explicar o motivo no PR.

Erros comuns:

| Forma incorreta | Problema | Forma de correção |
| --- | --- | --- |
| Nomes de branch `test`, `temp` | Sem informação de intenção | Alterar para `feat/<capacidade específica>` |
| Descrição do PR apenas com “corrige bug” | Impossível revisar o impacto | Acrescentar propósito, impacto e forma de verificação |
| Push direto para `main` | Viola H7 | Integrar via PR |
| Forçar push após reescrever branch já revisado | A conclusão da revisão deixa de ser válida | Adicionar novos commits respondendo aos comentários |
| Não excluir o branch de origem após o merge | Inchaço da lista de branches | Excluir imediatamente após o merge |

## 6. Exemplo completo

```markdown
## Propósito da alteração
Corrige o falso positivo da regra de espaçamento quando a pontuação chinesa está adjacente a palavras em inglês (REQ-004).

## Conteúdo da alteração
- O mecanismo de regras passa a considerar os limites de pontuação
- Foram adicionados os casos de regressão correspondentes

## Escopo de impacto
- Módulos afetados: regra spacing
- Rompe a compatibilidade: não
- Envolve configuração ou migração de dados: não

## Forma de verificação
- Comando de autoteste: `npm test -- -t "中文标点"`
- Testes adicionados ou alterados: TC-007-regression-142
- Endereço de execução da CI: https://github.com/example/markdown-lint-cli/actions/runs/128

## Vinculações
- Requisito: REQ-004
- Matriz de rastreabilidade: atualizada
- Documentação: nenhuma
- Issue: #142

## Autoverificação
- [x] A mensagem de commit está em conformidade com a especificação
- [x] Não contém informações sensíveis
- [x] A matriz de rastreabilidade de requisitos foi atualizada
- [x] Alterações disruptivas foram registradas no registro de alterações (esta alteração não é disruptiva)
```

## Arquivos relacionados

- Critérios de revisão e classificação de comentários: [especificação de revisão de código](./code-review-specification.md)
- Formato de commit: [especificação de mensagens de commit](./commit-message-specification.md)
- Atualização do status de rastreabilidade: [especificação da matriz de rastreabilidade de requisitos](./requirements-traceability-matrix-specification.md)
- Branches e publicação pertencem à dimensão D8: [matriz de dimensões de revisão](./review-dimension-matrix.md)
- Regras obrigatórias H7/H8: [regras absolutas](./hard-rules.md)
- Operação de push: [especificação de push e publicação](./push-and-release-specification.md)
