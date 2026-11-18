# Especificação de guia de migração

> Problema que este arquivo resolve: definir a estrutura, os elementos de conteúdo e o momento de publicação do guia de migração em alterações disruptivas, permitindo que o usuário atualize da versão antiga para a nova de forma gradual e seguindo etapas.

## 1. Condições de disparo

O guia de migração deve ser fornecido em qualquer uma das situações a seguir:

1. A mensagem de commit contém `BREAKING CHANGE:` ou `feat!:` / `fix!:` (ver [especificação de mensagem de commit](./commit-message-specification.md)).
2. O nome de uma chave de configuração, o valor padrão ou a precedência sofre alteração.
3. A assinatura de API, a estrutura de retorno ou o código de erro sofre alteração.
4. A versão mínima de execução é elevada ou uma plataforma deixa de ser suportada.
5. A estrutura de diretórios ou a nomenclatura de arquivos sofre alteração, afetando os caminhos referenciados pelo usuário.

## 2. Localização e nomenclatura de arquivos

1. Orientações de migração de pequeno porte são inseridas na entrada da versão correspondente em `CHANGELOG.md`.
2. Quando a alteração é de maior porte e envolve operações de várias etapas, cria-se um arquivo próprio no diretório `docs/migration/`, nomeado por versão, como `docs/migration/v2.md`.
3. O caminho completo de migração entre versões principais é indexado em `docs/migration/README.md`.
4. O README contém apenas o aviso de migração e o link, sem detalhar as etapas (ver [matriz de documentação](./document-matrix.md)).

## 3. Estrutura do documento

O guia de migração deve ser organizado na seguinte ordem:

1. **Título e versão**: indicar a versão de origem e a versão de destino, como “Migração de v1.x para v2.0”.
2. **Visão geral do impacto**: listar as categorias de alteração e o escopo de impacto, indicando quais usuários devem migrar.
3. **Pré-requisitos**: preparações a concluir antes da migração, como backup e atualização da versão do ambiente.
4. **Lista de alterações**: enumerar item a item as alterações disruptivas, cada uma com “comportamento antigo”, “comportamento novo” e “motivo da alteração”.
5. **Etapas de migração**: enumerar as operações executáveis, com comandos ou exemplos de código.
6. **Forma de verificação**: como confirmar o sucesso após a migração, com comando de verificação ou saída esperada.
7. **Forma de reversão**: como restaurar a versão antiga em caso de falha na migração.
8. **Perguntas frequentes**: listar as dúvidas recorrentes e as respostas.
9. **Obtenção de ajuda**: apontar para issues, fórum de discussão ou site de documentação.

### 3.1 Modelo em branco para cópia

O modelo a seguir corresponde item a item à estrutura de nove itens da seção 3; basta copiar e substituir os marcadores de posição:

````markdown
# Migração de {{源版本}} para {{目标版本}}

> Este guia descreve todas as operações necessárias para atualizar de {{源版本}} para {{目标版本}} e aplica-se a {{适用使用者范围}}.

## 1. Visão geral do impacto

| Categoria de alteração | Conteúdo específico | Escopo de impacto | Migração obrigatória |
| --- | --- | --- | --- |
| {{变更类别}} | {{变更内容}} | {{受影响的使用者场景}} | {{是否必须迁移}} |

## 2. Pré-requisitos

- {{前置准备}}
- {{检查项与确认命令}}

## 3. Lista de alterações

### {{变更项名称}}

- Comportamento antigo: {{旧版本行为}}
- Comportamento novo: {{新版本行为}}
- Motivo da alteração: {{变更原因}}

Antes da migração:

```{{代码语言}}
{{旧配置或旧代码}}
```

Após a migração:

```{{代码语言}}
{{新配置或新代码}}
```

## 4. Etapas de migração

1. {{迁移步骤}}
2. {{迁移步骤}}
3. {{人工处理步骤}}

## 5. Forma de verificação

```bash
{{可独立运行的检查命令}}
```

Saída esperada: {{预期结果}}

## 6. Forma de reversão

1. {{恢复旧版本的操作}}
2. {{恢复旧配置的操作}}

## 7. Perguntas frequentes

### {{问题}}

Resposta: {{解答}}

## 8. Obtenção de ajuda

- Relato de problemas: {{issue 地址}}
- Fórum de discussão: {{讨论区地址}}
- Documentação relacionada: {{文档链接}}
````

Correspondência dos marcadores de posição:

| Marcador de posição | Obrigatório | Pontos de preenchimento |
| --- | --- | --- |
| `{{源版本}}` / `{{目标版本}}` | Sim | Coerente com a tag de destino, no formato `vX.Y.Z` |
| `{{适用使用者范围}}` | Sim | Indicar quais usuários devem migrar, evitando formulações vagas |
| `{{变更类别}}` | Sim | Pelo menos uma entre as quatro categorias: configuração, API, execução, diretórios |
| `{{是否必须迁移}}` | Sim | Indicar se a alteração exige que o usuário execute a migração |
| `{{旧行为}}` / `{{新行为}}` | Sim | Comparação item a item; é vedado registrar apenas um dos lados |
| `{{代码语言}}` | Sim | Identificador de linguagem do bloco de código, como `yaml`, `json`, `js` |
| `{{前置准备}}` | Sim | Backup e verificação de ambiente a concluir antes da migração |
| `{{迁移步骤}}` | Sim | Cada etapa deve ser diretamente executável, com comando ou código |
| `{{人工处理步骤}}` | Sim | Etapas não automatizáveis devem ser marcadas explicitamente aqui |
| `{{检查命令}}` / `{{预期结果}}` | Sim | O comando deve ser executável de forma independente e o resultado, julgável |
| `{{回滚方式}}` | Sim | Não pode ser omitido; ver práticas proibidas na seção 7 |

## 4. Requisitos de conteúdo

### 4.1 Exemplo de comparação de alterações

```markdown
### Item de configuração `timeout` renomeado para `timeoutMs`

- Comportamento antigo: uso de `timeout: 5000` no arquivo de configuração, em segundos.
- Comportamento novo: uso de `timeoutMs: 5000`, em milissegundos.
- Motivo da alteração: unificar a unidade de tempo e evitar inconsistência com o parâmetro de API.

Antes da migração:

```yaml
timeout: 5
```

Após a migração:

```yaml
timeoutMs: 5000
```

### 4.2 Requisitos de redação

1. Cada etapa deve trazer um comando ou código diretamente executável; é vedado apenas descrever “alterar a configuração”.
2. Apresentar a comparação entre antes e depois da migração, para facilitar a verificação item a item.
3. Marcar explicitamente as etapas não automatizáveis que exigem tratamento manual.
4. O escopo de impacto deve ser concreto, evitando formulações vagas como “pode afetar parte dos usuários”.
5. O comando de verificação deve ser executável de forma independente e incluir a saída esperada.

## 5. Momento de publicação e vinculações

1. O guia de migração deve ser publicado em sincronia com a versão que contém a alteração disruptiva, sem atraso.
2. A entrada correspondente em `CHANGELOG.md` deve apontar para o guia de migração (ver [especificação de registro de alterações](./changelog-specification.md)).
3. O bloco de alterações disruptivas do modelo de PR deve solicitar o preenchimento da forma de migração (ver [especificação de modelos de Issue e PR](./issue-and-pr-template-specification.md)).
4. O número de versão segue o versionamento semântico; alterações disruptivas devem elevar a versão principal (ver [especificação de gerenciamento de versões](./version-management-specification.md)).
5. O README deve avisar, em local destacado, que os usuários de versões antigas leiam o guia de migração.

## 6. Política de descontinuação e retenção

1. O guia de migração deve ser mantido por longo prazo e não pode ser excluído após a publicação de uma nova versão.
2. A documentação de versões antigas pode ser marcada como “sem manutenção”, mas o acesso deve ser preservado.
3. Atualizações que atravessam várias versões principais devem oferecer um caminho em etapas; é vedado exigir a transposição de todas as alterações de uma só vez.

## 7. Práticas proibidas

1. É vedado escrever apenas “há alterações disruptivas, ajuste por conta própria”.
2. É vedado omitir a forma de reversão.
3. É vedado usar pseudocódigo inexequível nas etapas de migração.
4. É vedado excluir guias de migração de versões históricas.

## Arquivos relacionados

- A estrutura do registro de alterações está na [especificação de registro de alterações](./changelog-specification.md)
- As regras de incremento de versão estão na [especificação de gerenciamento de versões](./version-management-specification.md)
- A declaração de alteração disruptiva na mensagem de commit está na [especificação de mensagem de commit](./commit-message-specification.md)
- As fronteiras de responsabilidade documental estão na [matriz de documentação](./document-matrix.md)
- O processo de publicação está na [especificação de push e publicação](./push-and-release-specification.md)
