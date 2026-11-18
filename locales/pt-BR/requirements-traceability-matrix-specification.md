# Especificação da matriz de rastreabilidade de requisitos

> Problema que este arquivo resolve: definir o modelo e os campos da matriz bidirecional de rastreabilidade entre requisito, design, implementação, testes e publicação, garantindo que os artefatos de cada fase do ciclo de vida se referenciem de forma coerente, que o impacto de alterações seja avaliável e que lacunas de cobertura sejam identificáveis.

## 1. Dispositivos normativos

1. Cada requisito de nível “obrigatório” deve ocupar uma linha na matriz de rastreabilidade e registrar os artefatos de toda a cadeia, da iniciação do projeto à publicação.
2. A relação de rastreamento deve ser consultável nas duas direções: do requisito para os artefatos downstream e do artefato para os requisitos upstream.
3. Quando um requisito corresponde a vários artefatos, usa-se uma lista de numerações separadas por vírgula; as numerações devem ser exatamente idênticas às definidas nos documentos correspondentes.
4. Alterações de requisito devem deixar rastro na matriz, registrando motivo da alteração, escopo de impacto e responsável pela decisão; é vedado substituir diretamente o valor original.
5. A matriz deve ser verificada antes de cada publicação de versão; requisitos de nível “obrigatório” não fechados não podem ser publicados.
6. Critério de apuração da cobertura: cobertura de requisitos = número de requisitos “obrigatórios” publicados / total de requisitos “obrigatórios”.

## 2. Modelo da matriz de rastreabilidade

```markdown
# Matriz de rastreabilidade de requisitos: {{项目名称}}

Versão: {{vX.Y.Z}} ｜ Responsável pela atualização: {{姓名}} ｜ Última verificação: {{YYYY-MM-DD}}

| ID do requisito | Título do requisito | Prioridade | Objetivo da iniciação | Decisão de arquitetura | Documento de design | PR de implementação | Caso de teste | Versão de publicação | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | {{标题}} | Obrigatório | G1 | ADR-0002 | docs/api.md#check | #12 | TC-001, TC-002 | v1.0.0 | Verificado |
| REQ-002 | {{标题}} | Recomendado | G2 | — | — | #15 | TC-005 | — | Implementado |
| REQ-003 | {{标题}} | Obrigatório | G1 | ADR-0003 | docs/architecture.md#flow | — | — | — | A implementar |

Estado: A confirmar / Confirmado / A implementar / Implementado / Verificado / Publicado / Obsoleto
```

## 3. Modelo de índice reverso

```markdown
## Consulta reversa por artefato

| Tipo de artefato | Número do artefato | IDs de requisitos cobertos |
| --- | --- | --- |
| Decisão de arquitetura | ADR-0002 | REQ-001, REQ-004 |
| Caso de teste | TC-001 | REQ-001 |
| PR de implementação | #12 | REQ-001, REQ-007 |
| Versão de publicação | v1.0.0 | REQ-001, REQ-002 |
```

## 4. Modelo de registro de alterações

```markdown
## Registro de alterações

| Data | ID do requisito | Conteúdo da alteração | Motivo | Escopo de impacto | Responsável pela decisão |
| --- | --- | --- | --- | --- | --- |
| {{YYYY-MM-DD}} | {{REQ-NNN}} | {{字段：原值 → 新值}} | {{依据}} | {{受影响的下游产物}} | {{姓名}} |
```

## 5. Definição de campos

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| ID do requisito | Sim | `REQ-NNN` | Coerente com a numeração da [especificação de iniciação do projeto e requisitos](./project-initiation-and-requirements-specification.md) | `REQ-001` |
| Prioridade | Sim | Enumeração | Obrigatório / Recomendado / Opcional | `必须` |
| Objetivo da iniciação | Sim | `G-N` | Número do objetivo correspondente no documento de iniciação | `G1` |
| Decisão de arquitetura | Não | `ADR-NNNN` | Sem decisão de arquitetura, escrever “—”; é vedado deixar em branco | `ADR-0002` |
| Documento de design | Não | `caminho#âncora` | Preciso até a âncora de seção | `docs/api.md#check` |
| PR de implementação | Não | `#número` | Número da PR, não o hash do commit | `#12` |
| Caso de teste | Sim | Lista `TC-NNN` | Pelo menos um; sem caso, justificar | `TC-001` |
| Versão de publicação | Não | `vX.Y.Z` | Coerente com a tag | `v1.0.0` |
| Estado | Sim | Enumeração | Um dos sete estados, apenas avançando, exceto obsolescência | `已验证` |
| Registro de alterações.Escopo de impacto | Sim | Texto | Listar os ADR, PR e TC afetados | `ADR-0002, TC-001` |

## 6. Instruções de preenchimento

1. **Coerência de numeração**: os IDs de requisito, as numerações ADR e as numerações TC da matriz devem ser idênticos, palavra por palavra, aos documentos de origem; é vedado usar abreviações ou aliases.
2. **Padrão de valor vazio**: quando não se aplica, escrever “—”; quando ainda não produzido, escrever “pendente”; os dois significados são distintos e não podem ser confundidos.
3. **Índice reverso**: após cada atualização da matriz direta, atualizar em sincronia o índice reverso; em caso de divergência, prevalece a matriz direta e a correção deve ser imediata.
4. **Rastro de alterações**: antes de modificar qualquer campo, acrescentar uma linha no registro de alterações com o valor original e o novo valor; é vedado substituir diretamente.
5. **Verificação de publicação**: antes da publicação, verificar item a item se os requisitos de nível “obrigatório” possuem caso de teste e versão de publicação; a ausência de qualquer um bloqueia a publicação.
6. **Requisitos obsoletos**: manter a linha sem excluí-la, alterar o estado para “Obsoleto” e registrar o motivo da obsolescência no registro de alterações.

Erros comuns:

| Redação incorreta | Problema | Forma de correção |
| --- | --- | --- |
| Campo de caso de teste em branco | Lacuna de cobertura invisível | Preencher “pendente” e zerar antes da publicação |
| Campo de PR preenchido com hash de commit | Impossível localizar o registro de revisão | Usar o número da PR |
| Alterar o valor diretamente na mudança | Impacto não rastreável | Acrescentar primeiro o registro de alterações |
| Estado regredindo de “Verificado” para “Implementado” | Viola o princípio de avanço apenas | Abrir um novo defeito e criar outra linha de rastreamento |
| Índice direto e reverso divergentes | Referências descasadas | Sincronizar com base na matriz direta antes da publicação |

## 7. Exemplo completo

```markdown
# Matriz de rastreabilidade de requisitos: markdown-lint-cli

Versão: v1.0.0 ｜ Responsável pela atualização: Wang Wu ｜ Última verificação: 2026-11-20

| ID do requisito | Título do requisito | Prioridade | Objetivo da iniciação | Decisão de arquitetura | Documento de design | PR de implementação | Caso de teste | Versão de publicação | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | Verificação de espaçamento entre chinês e inglês | Obrigatório | G1 | ADR-0002 | docs/api.md#rules-spacing | #12 | TC-001, TC-002 | v1.0.0 | Publicado |
| REQ-002 | Saída de relatório JSON | Recomendado | G1 | — | docs/api.md#reporter | #15 | TC-011 | v1.0.0 | Publicado |
| REQ-003 | Integração com plug-in de editor | Opcional | G2 | Pendente | Pendente | — | Pendente | — | A confirmar |

## Registro de alterações

| Data | ID do requisito | Conteúdo da alteração | Motivo | Escopo de impacto | Responsável pela decisão |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | REQ-003 | Prioridade: Recomendado → Opcional | Prazo insuficiente para a v1.0 | ADR-0005, TC-020 | Li Si |
```

## Arquivos relacionados

- Numeração de requisitos e critérios de aceite: [especificação de iniciação do projeto e requisitos](./project-initiation-and-requirements-specification.md)
- Numeração de decisões de arquitetura: [especificação de documento de design de arquitetura](./architecture-design-document-specification.md)
- Numeração de casos de teste: [especificação de testes](./testing-specification.md)
- Versão de publicação e tag: [especificação de gerenciamento de versões](./version-management-specification.md)
- Descrição externa das alterações de versão: [especificação de registro de alterações](./changelog-specification.md)
- Retrospectiva de processo ao fim da iteração: [especificação de retrospectiva de iteração](./iteration-retrospective-specification.md)
