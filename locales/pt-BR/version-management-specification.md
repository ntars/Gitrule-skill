# Especificação de gestão de versões

> Problema que este arquivo resolve: definir as regras de versionamento semântico, o registro de decisão de versão, a base de incremento e as relações de dependência, garantindo que o número de versão expresse a natureza da alteração, seja analisável por ferramentas e coerente com os artefatos de publicação.

## 1. Disposições normativas

1. O número de versão segue o versionamento semântico: `MAJOR.MINOR.PATCH`.
2. O número de versão não usa ano, data ou número de build como corpo semântico; versões já publicadas não devem ter o número reutilizado.
3. Alterações disruptivas devem ser tratadas de forma concentrada na elevação da versão principal, com indicação da forma de migração.
4. O número de versão deve ser coerente com a tag, no formato `vMAJOR.MINOR.PATCH` (ver [especificação de push e publicação](./push-and-release-specification.md)).
5. Versões de pré-lançamento usam os sufixos `-alpha`, `-beta` e `-rc`, e devem ser validadas antes da publicação da versão estável.

## 2. Formato do número de versão e base de incremento

| Posição | Condição de incremento | Tipo de commit que dispara | Exemplo |
| --- | --- | --- | --- |
| MAJOR | Alteração disruptiva incompatível | `feat!:` / `fix!:` / `BREAKING CHANGE:` | `1.9.2 → 2.0.0` |
| MINOR | Nova funcionalidade compatível com versões anteriores | `feat` | `1.2.3 → 1.3.0` |
| PATCH | Correção de defeito compatível com versões anteriores | `fix` | `1.2.3 → 1.2.4` |

Formato de pré-lançamento: `vMAJOR.MINOR.PATCH-alpha.N` / `-beta.N` / `-rc.N`, com número crescente a partir de 1; o sufixo é removido na publicação da versão estável.

## 3. Modelo de registro de decisão de versão

```markdown
## Decisão de versão: {{X.Y.Z}}

- Data da decisão: {{YYYY-MM-DD}}
- Responsável pela decisão: {{姓名}}
- Versão atual: {{X.Y.Z}}
- Versão-alvo: {{X.Y.Z}}
- Posição incrementada: {{MAJOR / MINOR / PATCH}}
- Base: {{列举触发的提交类型与变更内容}}

| Alteração | Tipo de commit | Requisitos relacionados | Quebra compatibilidade |
| --- | --- | --- | --- |
| {{变更描述}} | {{feat / fix / BREAKING CHANGE}} | {{REQ-NNN}} | {{是 / 否}} |

- Tratamento de alteração disruptiva: {{迁移指南链接 / 不适用}}
- Entrada no registro de alterações: {{链接}}
- tag: {{vX.Y.Z}}
- Verificação de publicação: {{已通过 / 待通过}}
```

## 4. Modelo de livro de registro de versões

```markdown
# Livro de registro de versões: {{项目名称}}

| Versão | Data de publicação | Tipo | Alterações principais | tag | Registro de alterações | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| {{X.Y.Z}} | {{YYYY-MM-DD}} | {{主版本 / 次版本 / 修订}} | {{一句话}} | {{vX.Y.Z}} | {{链接}} | {{当前 / 历史 / 已废弃}} |
| {{X.Y.Z-rc.1}} | {{YYYY-MM-DD}} | Pré-lançamento | {{一句话}} | {{vX.Y.Z-rc.1}} | {{链接}} | Substituída |

Estado: atual / histórico / descartado / substituído
```

## 5. Definição de campos

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Versão atual | Sim | `X.Y.Z` | Coerente com a tag mais recente | `1.2.3` |
| Versão-alvo | Sim | `X.Y.Z` | Incrementar apenas uma posição | `1.3.0` |
| Posição incrementada | Sim | enumeração | MAJOR / MINOR / PATCH | `MINOR` |
| Base | Sim | lista | Listar as alterações que dispararam; proibido “atualização de rotina” | `Novo suporte a TOML` |
| Tratamento de alteração disruptiva | Condicionalmente obrigatório | link | Obrigatório no incremento de MAJOR | `[Guia de migração]` |
| Entrada no registro de alterações | Sim | link | Apontar para a seção da versão correspondente | `[1.3.0]` |
| tag | Sim | `vX.Y.Z` | Correspondência um a um com o número de versão | `v1.3.0` |
| Data de publicação | Sim | `YYYY-MM-DD` | Prevalece a data de criação da tag | `2026-11-20` |
| Estado | Sim | enumeração | Atual / histórico / descartado / substituído | `Atual` |

## 6. Instruções de preenchimento

1. **Incremento de uma posição**: cada publicação incrementa apenas uma posição; havendo simultaneamente feat e BREAKING CHANGE, adota-se a posição mais alta (MAJOR) e as demais alterações são incorporadas a essa versão.
2. **Concentração de alterações disruptivas**: várias alterações disruptivas devem ser agrupadas na mesma versão principal, evitando incrementos consecutivos de MAJOR.
3. **Proibição de reutilização**: números de versão publicados ficam permanentemente ocupados; em caso de retirada da publicação, incrementa-se PATCH e publica-se uma versão corrigida, sem reutilizar o número original.
4. **Pré-lançamento**: `alpha` serve à validação interna, `beta` ao teste público e `rc` ao candidato à publicação; todos os níveis devem passar pela CI.
5. **Verificação de consistência**: o número de versão deve ser consistente em cinco locais — tag, registro de alterações, Release Notes, registro de implantação e livro de registro de versões; em caso de divergência, prevalece a tag e os demais são corrigidos.
6. **Dependências**: a base de incremento vem do tipo da [especificação de mensagem de commit](./commit-message-specification.md); a explicação externa está na [especificação de registro de alterações](./changelog-specification.md); o caminho de atualização está na [especificação de guia de migração](./migration-guide-specification.md).

Erros comuns:

| Redação incorreta | Problema | Forma de correção |
| --- | --- | --- |
| `v2026.11` | Data como corpo semântico | Alterar para `v2.1.0` |
| Incrementar duas posições na mesma versão | Semântica confusa | Incrementar apenas a posição mais alta |
| Reutilizar um número de versão retirado | Impossível distinguir artefatos | Incrementar PATCH e publicar versão corrigida |
| Incremento de MAJOR sem guia de migração | Usuário não consegue atualizar | Acrescentar e vincular o guia de migração |
| Número de versão existente apenas na tag | Livro de registro e changelog inconsistentes | Sincronizar os cinco locais |

## 7. Exemplo completo

```markdown
## Decisão de versão: 2.0.0

- Data da decisão: 2026-12-01
- Responsável pela decisão: Li Si
- Versão atual: 1.9.2
- Versão-alvo: 2.0.0
- Posição incrementada: MAJOR
- Base: o formato do arquivo de configuração passa de objeto para caminho de arquivo, o que constitui alteração incompatível.

| Alteração | Tipo de commit | Requisitos relacionados | Quebra compatibilidade |
| --- | --- | --- | --- |
| Configuração por caminho de arquivo | BREAKING CHANGE | REQ-021 | Sim |
| Novo suporte a análise de TOML | feat | REQ-001 | Não |

- Tratamento de alteração disruptiva: [Guia de migração v2.0]
- Entrada no registro de alterações: [2.0.0]
- tag: v2.0.0
- Verificação de publicação: aprovada
```

## Arquivos relacionados

- Tipos de commit e marcação de alteração disruptiva: [especificação de mensagem de commit](./commit-message-specification.md)
- tag e Release Notes: [especificação de push e publicação](./push-and-release-specification.md)
- Entrada no registro de alterações: [especificação de registro de alterações](./changelog-specification.md)
- Caminho de atualização: [especificação de guia de migração](./migration-guide-specification.md)
- Origem da versão-alvo: [especificação de roteiro](./roadmap-specification.md)
- Consistência de versão no registro de implantação: [especificação de implantação e reversão](./deployment-and-rollback-specification.md)
