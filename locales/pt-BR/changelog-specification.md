# Especificação de registro de alterações

> Problema que este arquivo resolve: definir o modelo, os campos e a forma de escrita do registro de alterações de versão voltado ao usuário, garantindo que cada alteração seja rastreável, que a versão possa ser correlacionada e que o caminho de atualização possa ser julgado.

## 1. Dispositivos normativos

1. O registro de alterações segue a estrutura Keep a Changelog e o número de versão segue o versionamento semântico da [especificação de gerenciamento de versões](./version-management-specification.md).
2. Cada versão deve ter data de publicação no formato `YYYY-MM-DD`; o conteúdo não publicado fica na seção `Unreleased`.
3. Os itens são agrupados em seis categorias: `Added` (novo) / `Changed` (alterado) / `Deprecated` (obsoleto) / `Removed` (removido) / `Fixed` (corrigido) / `Security` (segurança).
4. Cada alteração é voltada ao usuário e deve explicar o impacto e a forma de migração, sem detalhes internos de refatoração.
5. Alterações disruptivas devem ser marcadas com `BREAKING CHANGE:` e acompanhadas dos passos de migração (ver [especificação de guia de migração](./migration-guide-specification.md)).
6. O número de versão deve ser coerente com a tag e com as Release Notes; alterações disruptivas devem corresponder a `feat!:` ou `BREAKING CHANGE:` na mensagem de commit.

## 2. Modelo de registro de alterações

```markdown
# Registro de alterações

Este arquivo registra todas as alterações voltadas ao usuário. O formato segue o Keep a Changelog e as versões seguem o versionamento semântico.

## [Unreleased]

### Added
- {{新增能力，说明对使用者的价值}}

### Changed
- {{行为变更，说明影响范围}}

### Deprecated
- {{即将移除的能力，说明替代方案与移除版本}}

### Removed
- {{已移除的能力，说明迁移路径}}

### Fixed
- {{缺陷修复，说明触发条件}}

### Security
- {{安全修复，说明影响与升级建议}}

## [{{X.Y.Z}}] - {{YYYY-MM-DD}}

### {{类型}}
- {{变更条目}}
- {{BREAKING CHANGE: 原行为 → 新行为；迁移步骤见链接}}

[Unreleased]: https://github.com/{{owner}}/{{repo}}/compare/v{{X.Y.Z}}...HEAD
[{{X.Y.Z}}]: https://github.com/{{owner}}/{{repo}}/compare/v{{prev}}...v{{X.Y.Z}}
```

## 3. Modelo de item

```markdown
- {{动词开头的一句话变更描述}}（{{关联 REQ 编号}}）
  - Impacto: {{哪些使用者或场景受影响}}
  - Migração: {{需要执行的动作；无则省略此行}}
  - Referência: {{Issue / PR 链接}}
```

## 4. Definição dos campos

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Número de versão | Sim | `X.Y.Z` | Idêntico à tag; sem o prefixo `v` também é aceitável, mas deve ser uniforme em todo o documento | `1.2.0` |
| Data de publicação | Sim | `YYYY-MM-DD` | Prevalece a data de criação da tag | `2026-11-18` |
| Tipo de grupo | Sim | Enumeração | Uma das seis categorias; sem itens da categoria, a seção inteira é omitida | `Fixed` |
| Descrição da alteração | Sim | Texto | Iniciada por verbo, voltada ao usuário, explicando o valor | `Adicionada a verificação de tabelas GFM` |
| Impacto | Obrigatório condicionalmente | Texto | Obrigatório em alteração de comportamento, obsolescência, remoção e alteração disruptiva | `O arquivo de configuração antigo precisa ser renomeado` |
| Migração | Obrigatório condicionalmente | Texto | Obrigatório em alteração disruptiva, apontando para o guia de migração | `Ver guia de migração v1.0` |
| BREAKING CHANGE | Obrigatório condicionalmente | Marca | Obrigatório em alteração disruptiva, no início do item | `BREAKING CHANGE:` |
| Link de comparação | Sim | URL | Cada seção de versão deve fornecer link de comparação | `compare/v1.1.0...v1.2.0` |
| REQ relacionado | Não | Lista | Facilita a comparação com a matriz de rastreabilidade de requisitos | `REQ-007` |

## 5. Instruções de preenchimento

1. **Granularidade dos itens**: uma alteração descreve um resultado perceptível ao usuário; múltiplos resultados devem ser separados em vários itens.
2. **Início por verbo**: usar “adicionar”, “suportar”, “corrigir”, “remover”, “tornar obsoleto”, “ajustar”; não usar “atualizei”, “fiz algumas coisas”.
3. **Conteúdo proibido**: itens sem data, refatoração interna, planos de desenvolvimento, conteúdo de roteiro, expressões vagas (“melhorar a experiência”, “corrigir vários problemas”).
4. **Alteração disruptiva**: deve reunir simultaneamente a marca `BREAKING CHANGE:`, a descrição de impacto, os passos de migração e o link do guia de migração; nenhum dos quatro pode faltar.
5. **Itens obsoletos**: devem indicar a alternativa e o número da versão em que a remoção está prevista, por exemplo “será removido na v2.0”.
6. **Unreleased**: registrar imediatamente após o merge, sem acumular para preencher no dia da publicação.
7. **Coerência**: número de versão e data de publicação devem ser coerentes com a tag, as Release Notes e o registro de implantação nos três pontos; havendo divergência, prevalece a tag e os outros três devem ser corrigidos.

Erros comuns:

| Escrita incorreta | Problema | Forma de correção |
| --- | --- | --- |
| “Refatorar a estrutura interna dos módulos” | Detalhe interno, imperceptível ao usuário | Remover ou reescrever como efeito perceptível |
| “Corrigir vários problemas” | Não é verificável | Listar cada correção item por item |
| Alteração disruptiva dizendo apenas “houve mudança” | Sem caminho de migração | Acrescentar impacto, passos de migração e link do guia |
| Número de versão divergente da tag | Correlação de versões rompida | Unificar com base na tag |
| Sem link de comparação | Impossível ver as diferenças | Acrescentar a URL de comparação do GitHub |

## 6. Exemplo completo

```markdown
## [1.0.0] - 2026-11-20

### Added
- Adicionada regra de verificação de espaçamento entre texto em chinês e inglês (REQ-001), com suporte a chamada direta pela linha de comando.
- Adicionada saída de relatório em JSON, facilitando a integração com estatísticas da CI.

### Changed
- BREAKING CHANGE: o nome do arquivo de configuração passou de `.mdlint.json` para `.mdlintrc.json`. O arquivo antigo deixa de ser lido; os passos de migração estão no [guia de migração](./migration-guide-specification.md).

### Deprecated
- O parâmetro `--format=table` será removido na v2.0; usar `--reporter=table`.

### Fixed
- Corrigido o falso positivo quando pontuação chinesa fica adjacente a palavras em inglês.

### Security
- Corrigido o problema em que o caminho de carregamento de plugins de regras podia ser sobrescrito por entrada externa; recomenda-se que todos os usuários atualizem para a v1.0.0.

[1.0.0]: https://github.com/example/markdown-lint-cli/compare/v0.9.3...v1.0.0
```

## Arquivos relacionados

- Regras de incremento de versão: [especificação de gerenciamento de versões](./version-management-specification.md)
- Documentação de migração para alterações disruptivas: [especificação de guia de migração](./migration-guide-specification.md)
- Fronteiras de responsabilidade da documentação: [matriz de documentação](./document-matrix.md)
- Marca de ruptura na mensagem de commit: [especificação de mensagens de commit](./commit-message-specification.md)
- Seção de registro de alterações no README: [especificação de seções do README](./readme-sections-specification.md)
- Tag e Release Notes: [especificação de push e publicação](./push-and-release-specification.md)
