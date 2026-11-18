# Especificação de estilo de código

> Problema que este arquivo resolve: definir o modelo de configuração de estilo de código, a tabela de convenções de nomenclatura, as regras de comentários e as instruções de preenchimento, reduzindo divergências de estilo e elevando a legibilidade e a eficiência da revisão.

## 1. Dispositivos normativos

1. As regras de estilo têm como referência as ferramentas automatizadas; o trabalho manual cobre apenas o que as ferramentas não alcançam.
2. A configuração de formatação deve ser commitada junto com o repositório (por exemplo, o arquivo de configuração do formatador), garantindo consistência entre ambientes.
3. A CI deve integrar a verificação de formatação; sem aprovação, o merge não deve ocorrer (ver [especificação de testes](./testing-specification.md)).
4. Não se deve usar números mágicos nem constantes codificadas diretamente; elas devem ser extraídas como constantes nomeadas.
5. O fim de linha deve ser uniformemente LF e o arquivo deve terminar com quebra de linha (correspondente à dimensão D3, higiene do repositório).

## 2. Modelo de configuração de estilo

```markdown
# Convenção de estilo de código: {{项目名称}}

Versão da configuração: {{v1.0}} ｜ Linguagem e versão aplicáveis: {{如 TypeScript 5.x}} ｜ Ferramenta de formatação: {{如 Prettier 3.x}}

## Regras de formatação (impostas por ferramenta)
| Regra | Valor | Item de configuração da ferramenta | Negociável |
| --- | --- | --- | --- |
| Indentação | {{2 空格 / 4 空格 / Tab}} | {{配置项名}} | Não |
| Largura de linha | {{100 字符}} | {{配置项名}} | Não |
| Aspas | {{单引号 / 双引号}} | {{配置项名}} | Não |
| Fim de linha | LF | `endOfLine: lf` | Não |
| Quebra de linha no fim do arquivo | Obrigatória | Padrão da ferramenta | Não |
| Ponto e vírgula | {{有 / 无}} | {{配置项名}} | Não |

## Convenções de nomenclatura (não impostas por ferramenta, revisão manual)
| Objeto | Regra | Exemplo correto | Exemplo incorreto |
| --- | --- | --- | --- |
| Variável | {{camelCase}} | `userName` | `UserName` |
| Constante | {{UPPER_SNAKE_CASE}} | `MAX_RETRY` | `maxRetry` |
| Função | {{动词开头 camelCase}} | `parseConfig` | `configParse` |
| Classe / tipo | {{PascalCase}} | `ConfigLoader` | `config_loader` |
| Nome de arquivo | {{kebab-case}} | `config-loader.ts` | `ConfigLoader.ts` |
| Booleano | {{is/has/can 前缀}} | `isValid` | `valid` |
| Coleção | {{复数名词}} | `items` | `itemList` |

## Regras de comentários
- Cenários em que comentários são obrigatórios: {{公开 API 的契约、非直观算法、绕开限制的临时方案}}
- Comentários proibidos: {{复述代码、无信息量、失效的旧注释、情绪化表述}}
- Idioma dos comentários: {{与项目主语言一致}}
- Formato de TODO: `// TODO({{负责人}}): {{事项}} — {{计划版本}}`

## Organização de arquivos
1. Ordem de importação: {{标准库 → 第三方 → 本地模块，组内字典序}}
2. Ordem de declaração: {{常量 → 类型 → 函数 → 导出}}
3. Limite de linhas por arquivo: {{300 行，超出须拆分}}

## Lista de exceções
| Cenário | Regra de exceção | Aprovador | Validade |
| --- | --- | --- | --- |
| {{如生成代码}} | {{不参与格式化}} | {{姓名}} | {{至 v2.0}} |
```

## 3. Definição dos campos de configuração

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Versão da configuração | Sim | Texto | Incrementada a cada mudança nas regras de estilo | `v1.0` |
| Linguagem e versão aplicáveis | Sim | Texto | Explicitar a versão principal, evitando deriva de regras | `TypeScript 5.x` |
| Ferramenta de formatação | Sim | Texto | Coerente com a versão do lockfile | `Prettier 3.2` |
| Regra.valor | Sim | Enumeração / número | Deve ser único; proibido “depende” | `2 espaços` |
| Negociável | Sim | Enumeração | Não / Sim; marcado “Sim” exige condições de negociação | `Não` |
| Exemplo correto de nomenclatura | Sim | Código | Extraído do código existente do projeto | `parseConfig` |
| Exemplo incorreto de nomenclatura | Sim | Código | Deve ser um erro real e frequente | `configParse` |
| Responsável pelo TODO | Sim | Texto | Proibido escrever “equipe” | `Zhang San` |
| Validade da exceção | Sim | Versão / data | Revisão obrigatória ao vencer | `Até v2.0` |

## 4. Instruções de preenchimento

1. **Ferramenta em primeiro lugar**: toda regra que a ferramenta possa impor deve ser gravada na configuração de formatação, sem depender da memória humana; o trabalho manual cobre apenas nomenclatura, comentários e organização de arquivos.
2. **Valor da largura de linha**: deve ser definido em função da largura da interface de revisão, sendo 100 ou 120 os valores usuais; uma vez definido, não deve ser sobrescrito em arquivos isolados.
3. **Exemplo correto de nomenclatura**: deve ser extraído de nomes realmente existentes no código do projeto; é proibido usar marcadores de posição didáticos.
4. **Nomenclatura booleana**: os prefixos `is`/`has`/`can` devem ser coerentes com a semântica; `isReady` não deve expressar uma ação.
5. **TODO**: deve conter responsável, item e versão planejada; TODOs sem plano não devem entrar no tronco principal.
6. **Lista de exceções**: cada exceção deve ter aprovador e validade; sem revisão ao vencer, a exceção expira automaticamente.

Erros comuns:

| Escrita incorreta | Problema | Forma de correção |
| --- | --- | --- |
| “O código deve ser o mais conciso possível” | Não é verificável | Converter em regra verificável, como limite de tamanho de função |
| Tabela de nomenclatura só com regras, sem contraexemplos | Impossível comparar na revisão | Acrescentar contraexemplos reais e frequentes |
| Comentário “aqui havia um bug” | Sem informação e sujeito a obsolescência | Reescrever explicando o comportamento atual e o motivo |
| TODO sem responsável | Ninguém acompanha | Acrescentar responsável e versão planejada |
| Exceção sem validade | Isenção permanente | Acrescentar validade e revisor |

## 5. Exemplo completo

```markdown
# Convenção de estilo de código: markdown-lint-cli

Versão da configuração: v1.0 ｜ Linguagem e versão aplicáveis: TypeScript 5.x ｜ Ferramenta de formatação: Prettier 3.2

## Regras de formatação (impostas por ferramenta)
| Regra | Valor | Item de configuração da ferramenta | Negociável |
| --- | --- | --- | --- |
| Indentação | 2 espaços | `tabWidth: 2` | Não |
| Largura de linha | 100 caracteres | `printWidth: 100` | Não |
| Aspas | Aspas simples | `singleQuote: true` | Não |
| Fim de linha | LF | `endOfLine: lf` | Não |
| Ponto e vírgula | Sim | `semi: true` | Não |

## Convenções de nomenclatura (revisão manual)
| Objeto | Regra | Exemplo correto | Exemplo incorreto |
| --- | --- | --- | --- |
| Função | camelCase iniciado por verbo | `parseRules` | `rulesParser` |
| Constante | UPPER_SNAKE_CASE | `DEFAULT_RULES` | `defaultRules` |
| Nome de arquivo | kebab-case | `rule-loader.ts` | `RuleLoader.ts` |

## Regras de comentários
- Cenários em que comentários são obrigatórios: a semântica de correspondência das regras e o contorno de comportamentos da API upstream.
- Comentários proibidos: repetir o código, “corrigi um bug”, TODO sem responsável.
- Formato de TODO: `// TODO(Wang Wu): substituir o analisador temporário — v2.0`

## Lista de exceções
| Cenário | Regra de exceção | Aprovador | Validade |
| --- | --- | --- | --- |
| Diretório fixtures | Não participa da formatação | Li Si | Até v2.0 |
```

## Arquivos relacionados

- Base de verificação da revisão de código: [especificação de revisão de código](./code-review-specification.md)
- A verificação de formatação é executada na CI: [especificação de testes](./testing-specification.md), [especificação de fluxo de trabalho de CI](./ci-workflow-specification.md)
- A higiene do repositório pertence à dimensão D3: [matriz de dimensões de auditoria](./review-dimension-matrix.md)
- Verificação antes do commit: [especificação de push e publicação](./push-and-release-specification.md)
- Rastreamento de requisitos para implementação: [especificação da matriz de rastreabilidade de requisitos](./requirements-traceability-matrix-specification.md)
