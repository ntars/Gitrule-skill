# Especificação de mensagens de commit

> Problema que este arquivo resolve: definir os campos, o formato, as instruções de preenchimento e os exemplos do Conventional Commits, garantindo um histórico legível e a geração automática do registro de alterações e do número de versão.

## 1. Formato

```text
<类型>[可选作用域][可选 !]: <描述>

[可选正文]

[可选脚注]
```

## 2. Tipos

As dez categorias completas são as seguintes e cobrem os cenários de commit de projetos de código aberto comuns:

| Tipo | Significado |
| --- | --- |
| `feat` | Nova funcionalidade |
| `fix` | Correção de defeito |
| `docs` | Alteração na documentação |
| `style` | Ajuste de formatação que não altera a lógica (espaços em branco, formatação, ponto e vírgula ausente etc.) |
| `refactor` | Refatoração que não adiciona funcionalidade nem corrige defeito |
| `perf` | Alteração de código para otimização de desempenho |
| `test` | Adição de testes ausentes ou correção de testes existentes |
| `build` | Alteração que afeta o sistema de compilação ou dependências externas (como npm, gulp) |
| `ci` | Alteração na configuração e nos scripts de integração contínua (como GitHub Actions, CircleCI) |
| `chore` | Tarefas diversas de compilação, dependências, cadeia de ferramentas etc. |

### 2.1 Comparação e escolha entre estilos de equipe

Em diferentes modos de colaboração existem três estilos comuns; o projeto deve escolher um na iniciação e unificar em toda a equipe:

| Estilo | Formato | Aplicação | Limitação |
| --- | --- | --- | --- |
| Estilo de trabalho | `[任务卡号] 作者: 修改内容` | Equipes que usam kanban e programação em par | Depende do sistema de números de tarefa; não se aplica quando não há número de tarefa |
| Estilo convencional | `[分类] 组件（可选）: 修改内容` | Equipes que precisam filtrar o histórico por módulo de negócio | Exige uma tabela de categorias acordada pela equipe, com custo adicional |
| Estilo de código aberto | `<type>(<scope>): <subject>` | Bibliotecas e aplicações de código aberto que precisam gerar CHANGELOG automaticamente | Muitos tipos e escopos, com custo de aprendizado mais alto |

Este projeto adota de forma unificada o estilo de código aberto (ou seja, o Conventional Commits), pelo fato de ser legível por máquina e permitir a geração automática do registro de alterações e do número de versão. Os estilos de trabalho e convencional são usados apenas em equipes de código fechado, conforme acordado, e não devem ser misturados em repositórios externos.

## 3. Definição dos campos

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Tipo | Sim | Enumeração | Um dos dez tipos, sem criação própria | `feat` |
| Escopo | Não | Texto | Nome do módulo, palavra curta em minúsculas, sem espaços | `parser` |
| Marca de ruptura | Não | `!` | Colocada após o tipo ou o escopo e antes dos dois-pontos | `feat!:` |
| Descrição | Sim | Texto | Frase no imperativo, início em minúscula, ≤72 caracteres, sem ponto final | `add TOML config support` |
| Corpo | Não | Texto | Explica o motivo e a implementação, separado da descrição por uma linha em branco | `Allow the parser to read TOML...` |
| Rodapé | Não | Texto | `BREAKING CHANGE:` ou `Refs: #N` | `BREAKING CHANGE: ...` |
| Requisito associado | Não | `REQ-NNN` | Escrito no corpo ou no rodapé, para facilitar o rastreamento | `Refs: REQ-001` |

## 4. Instruções de preenchimento

1. **Descrição**: usar o imperativo (add, fix, remove) e escrever “o que foi feito”, não “foi feita uma alteração”; em projetos em chinês, pode-se escrever a descrição em chinês, mas isso deve ser unificado em todo o repositório.
2. **Escopo**: usar o nome do módulo, não o nome do arquivo; em alterações que atravessam módulos, omitir o escopo, não escrevendo `all` nem `global`.
3. **Corpo**: escrever apenas quando a descrição não for suficiente para explicar o motivo; não repetir a descrição nem registrar o passo a passo do processo.
4. **Alteração incompatível**: usar `feat!:` / `fix!:` ou o rodapé `BREAKING CHANGE:`, escolhendo uma das formas ou combinando as duas; quando ocorrerem, devem ser registradas em conjunto na [especificação de registro de alterações](./changelog-specification.md) e na [especificação de guia de migração](./migration-guide-specification.md).
5. **Atomicidade**: um commit faz apenas uma coisa; formatação e alteração de lógica devem ser feitas em dois commits.
6. **Segurança**: não deve conter chaves, tokens, dados pessoais nem endereços internos; antes do commit, verificar com a varredura de chaves (ver a [especificação de segurança e privacidade](./security-and-privacy-specification.md)).
7. **Vinculação de versão**: `feat` dispara o incremento de versão secundária, `fix` dispara o incremento de versão de correção e `BREAKING CHANGE` dispara o incremento de versão principal; detalhes na [especificação de gestão de versões](./version-management-specification.md).

Erros comuns:

| Redação incorreta | Problema | Forma de correção |
| --- | --- | --- |
| `wip`, `update`, `fix bug` | Sem informação útil, viola H10 | Indicar o objeto e a ação |
| `feat: Added new feature.` | Não está no imperativo, inicia em maiúscula e tem ponto final | `feat: add config loader` |
| `feat(全部): 优化` | Escopo inválido e descrição vaga | Usar o nome concreto do módulo e descrever a alteração |
| Um commit com formatação e alteração funcional | Rompe a atomicidade | Separar em dois commits, `style:` e `feat:` |
| Mensagem de commit com endereço de rede interna | Vazamento de informação | Remover e passar pela varredura de chaves |

## 5. Exemplo completo

```text
feat(parser): add support for TOML config

Allow the parser to read TOML configuration files in addition to YAML.
Refs: REQ-001

BREAKING CHANGE: the `config` option now accepts a file path instead of an object.
```

Significado de cada campo: `feat` é o tipo, `parser` é o escopo e o texto após os dois-pontos é a descrição curta; o corpo explica o motivo e a implementação, e o rodapé associa o requisito; o rodapé final declara a alteração incompatível e indica a direção de migração.

Exemplo de correção:

```text
fix(spacing): avoid false positives before Chinese punctuation

The spacing rule previously flagged strings such as 「使用Node.js，」 because
the punctuation check ran after whitespace normalization.

Refs: REQ-004, #142
```

## Arquivos relacionados

- A revisão do histórico de commits pertence à dimensão D7: [matriz de dimensões de revisão](./review-dimension-matrix.md)
- Geração do registro de alterações: [especificação de registro de alterações](./changelog-specification.md)
- Base do incremento de versão: [especificação de gestão de versões](./version-management-specification.md)
- Itens de verificação da revisão de código: [especificação de revisão de código](./code-review-specification.md)
- Rastreamento de requisitos: [especificação da matriz de rastreabilidade de requisitos](./requirements-traceability-matrix-specification.md)
