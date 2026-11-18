# Especificação de modelos de Issue e PR

> Problema que este arquivo resolve: definir o design de campos, o formato e os requisitos de redação dos formulários estruturados `.github/ISSUE_TEMPLATE/*.yml` e da lista de autoverificação `.github/PULL_REQUEST_TEMPLATE.md`, para que o relato de problemas e o envio de alterações tenham restrições de entrada executáveis.

## 1. Princípios de design

1. **Estrutura antes de texto livre**: os formulários de Issue são definidos em YAML e orientam o preenchimento por meio de listas suspensas, caixas de seleção e campos obrigatórios, reduzindo relatos inúteis.
2. **Minimização dos obrigatórios**: manter apenas os campos necessários para localizar o problema; campos opcionais não devem ser marcados como obrigatórios.
3. **Autoverificação explícita**: o modelo de PR lista em forma de checklist os itens de autoverificação marcáveis, evitando que quem contribui pule etapas essenciais.
4. **Responsabilidade única**: o formulário de Issue coleta informações e não veicula a apresentação do projeto; o modelo de PR serve à autoverificação e não repete a descrição funcional (corresponde à [matriz de documentação](./document-matrix.md)).

## 2. Estrutura do formulário de Issue

### 2.1 Arquivos e nomenclatura

- O caminho é fixo: `.github/ISSUE_TEMPLATE/*.yml`, um arquivo por modelo.
- O nome do arquivo usa minúsculas e hífen, como `bug-report.yml`, `feature-request.yml`, `question.yml`.
- Devem ser oferecidos ao menos dois tipos de modelo: “relato de defeito” e “solicitação de funcionalidade”.

### 2.2 Campos padrão

| Campo | Tipo | Obrigatório | Uso |
| --- | --- | --- | --- |
| `name` | Cadeia de caracteres | Sim | Nome exibido do modelo |
| `description` | Cadeia de caracteres | Sim | Descrição da finalidade do modelo |
| `title` | Prefixo de cadeia | Sim | Prefixo automático do título do problema |
| `labels` | Array | Não | Etiquetas anexadas automaticamente |
| `body` | Array | Sim | Lista de campos do formulário |

Tipos de campo comuns em `body`:

| Tipo | Cenário de aplicação | Exemplo |
| --- | --- | --- |
| `markdown` | Texto explicativo, sem entrada | Instruções de preenchimento |
| `textarea` | Descrição de texto longo | Passos de reprodução do problema |
| `input` | Texto curto de uma linha | Número da versão |
| `dropdown` | Opções limitadas | Sistema operacional, gravidade |
| `checkboxes` | Confirmações múltiplas | Se já foram pesquisados problemas duplicados |

### 2.3 Lista de campos do relato de defeito

1. Descrição do problema (`textarea`, obrigatório): o que aconteceu.
2. Comportamento esperado (`textarea`, obrigatório): o que deveria acontecer.
3. Passos de reprodução (`textarea`, obrigatório): numerados e reproduzíveis de forma independente.
4. Ambiente de execução (`input` ou `dropdown`): sistema operacional, ambiente de execução, versão do projeto.
5. Registros ou capturas de tela (`textarea`): fornecer a mensagem de erro; informações sensíveis devem ser anonimizadas.
6. Confirmação de verificação de duplicidade (`checkboxes`, obrigatório): já foram pesquisadas issues existentes.

### 2.4 Lista de campos da solicitação de funcionalidade

1. Exposição do problema (`textarea`, obrigatório): qual capacidade falta atualmente.
2. Cenário de uso (`textarea`, obrigatório): quem precisa e em que situação.
3. Solução esperada (`textarea`): como se espera que seja implementado.
4. Alternativas (`textarea`): outras abordagens já consideradas.
5. Impacto na compatibilidade (`dropdown`): se envolve alterações disruptivas.

## 3. Estrutura do modelo de PR

### 3.1 Blocos obrigatórios

`PULL_REQUEST_TEMPLATE.md` deve conter os seguintes blocos, em ordem fixa:

1. Descrição da alteração: o que foi modificado e o número da issue correspondente.
2. Tipo de alteração: marcado com caixas de seleção (funcionalidade, correção, documentação, refatoração, testes etc.; para os tipos, ver a [especificação de mensagens de commit](./commit-message-specification.md)).
3. Lista de autoverificação: itens de autoverificação marcáveis.
4. Alterações disruptivas: se não houver, escrever “nenhuma”; se houver, indicar a forma de migração (ver a [especificação de guia de migração](./migration-guide-specification.md)).
5. Documentação relacionada: se o README, o CHANGELOG e a documentação de API foram atualizados de forma sincronizada.

### 3.2 Exemplo de lista de autoverificação

```markdown
## Lista de autoverificação

- [ ] A compilação local passa
- [ ] Os testes relacionados passam e a nova funcionalidade inclui testes
- [ ] A mensagem de commit foi redigida conforme a [especificação de mensagens de commit](./commit-message-specification.md)
- [ ] A documentação foi atualizada de forma sincronizada ou foi confirmado que não requer atualização
- [ ] Não foram introduzidas chaves, dados privados ou arquivos grandes
```

## 4. Modelos copiáveis

### 4.1 Formulário de relato de defeito

Salvar como `.github/ISSUE_TEMPLATE/bug-report.yml`:

```yaml
name: Relato de defeito
description: Relata uma anomalia funcional reproduzível
title: "[Bug]: "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        Antes de enviar, pesquise primeiro as issues existentes para evitar duplicidade.
        Não cole chaves, tokens ou dados pessoais.
  - type: checkboxes
    id: duplicate-check
    attributes:
      label: Verificação de duplicidade
      options:
        - label: Pesquisei as issues existentes e confirmo que este relato não é duplicado
          required: true
  - type: textarea
    id: description
    attributes:
      label: Descrição do problema
      description: O que aconteceu de fato
      placeholder: Após executar o comando install, o programa termina com código de saída 1
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Comportamento esperado
      description: O que deveria acontecer
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: Passos de reprodução
      description: Numere os passos para que outra pessoa possa reproduzir de forma independente
      placeholder: |
        1. Executar o comando
        2. Observar a saída
        3. Ocorre a anomalia
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: Versão do projeto
      placeholder: v1.0.0
    validations:
      required: true
  - type: dropdown
    id: os
    attributes:
      label: Sistema operacional
      options:
        - macOS
        - Linux
        - Windows
        - Outro
    validations:
      required: true
  - type: textarea
    id: logs
    attributes:
      label: Registros ou capturas de tela
      description: Forneça a mensagem de erro; informações sensíveis devem ser anonimizadas
      render: shell
  - type: checkboxes
    id: security
    attributes:
      label: Confirmação de segurança da informação
      options:
        - label: Confirmo que não há chaves, tokens ou dados pessoais
          required: true
```

### 4.2 Formulário de solicitação de funcionalidade

Salvar como `.github/ISSUE_TEMPLATE/feature-request.yml`:

```yaml
name: Solicitação de funcionalidade
description: Propõe uma nova capacidade ou uma melhoria
title: "[Feature]: "
labels: ["enhancement"]
body:
  - type: textarea
    id: problem
    attributes:
      label: Exposição do problema
      description: Qual capacidade falta atualmente
    validations:
      required: true
  - type: textarea
    id: scenario
    attributes:
      label: Cenário de uso
      description: Quem precisa dessa capacidade e em que situação
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: Solução esperada
      description: Como se espera que seja implementado
  - type: textarea
    id: alternatives
    attributes:
      label: Alternativas
      description: Outras abordagens já consideradas
  - type: dropdown
    id: breaking
    attributes:
      label: Envolve alteração disruptiva
      options:
        - Não
        - Sim
        - Não sei
    validations:
      required: true
```

### 4.3 Modelo de PR

Salvar como `.github/PULL_REQUEST_TEMPLATE.md`:

````markdown
## Descrição da alteração

{{变更说明}}

## Tipo de alteração

- [ ] Funcionalidade (feat)
- [ ] Correção (fix)
- [ ] Documentação (docs)
- [ ] Formatação (style)
- [ ] Refatoração (refactor)
- [ ] Testes (test)
- [ ] Compilação ou cadeia de ferramentas (build / ci)

## Lista de autoverificação

- [ ] A compilação local passa
- [ ] Os testes relacionados passam e a nova funcionalidade inclui testes
- [ ] A mensagem de commit foi redigida conforme a especificação de mensagens de commit
- [ ] A documentação foi atualizada de forma sincronizada ou foi confirmado que não requer atualização
- [ ] Não foram introduzidas chaves, dados privados ou arquivos grandes

## Alterações disruptivas

{{破坏性变更说明}}

## Documentação relacionada

- [ ] O README foi sincronizado ou não requer atualização
- [ ] O CHANGELOG foi registrado
- [ ] A documentação de API foi sincronizada ou não requer atualização
````

### 4.4 Tabela de correspondência de marcadores de posição

| Marcador de posição | Obrigatório | Pontos principais de preenchimento |
| --- | --- | --- |
| `{{变更说明}}` | Sim | Uma frase declarando o conteúdo da alteração, com o número da issue no formato `#número` |
| `{{破坏性变更说明}}` | Sim | Se não houver alteração disruptiva, escrever “nenhuma”; se houver, descrever os passos de migração e vincular o guia de migração |

Os campos `name`, `description`, `title` e `labels` do formulário YAML são metadados do modelo e devem ser substituídos conforme a situação real do projeto; os tipos de campo e os valores de `required` em `body` devem ser ajustados conforme as listas de campos das seções 2 e 3, sem reduzir os campos obrigatórios.

### 4.5 Exemplo completo de preenchimento

Exemplo de preenchimento de um relato de defeito:

````markdown
## Descrição do problema

Após executar `npm run build`, o processo termina com código de saída 1.

## Comportamento esperado

A compilação é concluída com sucesso e gera o diretório `dist/`.

## Passos de reprodução

1. Fazer checkout da tag v1.0.0
2. Executar `npm ci`
3. Executar `npm run build` e observar o código de saída 1

## Versão do projeto

v1.0.0

## Sistema operacional

macOS

## Registros ou capturas de tela

```
Error: Cannot find module 'mdlint-core'
```

## Confirmação de segurança da informação

- [x] Confirmo que não há chaves, tokens ou dados pessoais
````

## 5. Requisitos de redação

1. As descrições de campo usam orações imperativas ou declarativas e não devem ser coloquiais.
2. Cada campo obrigatório deve trazer um exemplo de preenchimento ou um requisito de formato.
3. O texto de ajuda deve explicar “por que esta informação é necessária”, evitando exigências vagas.
4. Campos que envolvem privacidade devem alertar sobre a anonimização (ver a [especificação de segurança e privacidade](./security-and-privacy-specification.md)).
5. Os modelos são atualizados conforme a evolução do projeto; campos obsoletos devem ser removidos e não devem se acumular por longo prazo.

## 6. Práticas proibidas

1. É proibido unificar todos os tipos de problema em um único modelo de texto livre.
2. É proibido definir campos obrigatórios sem relação com a localização do problema.
3. É proibido incluir apresentação do projeto ou conteúdo de marketing nos modelos.
4. É proibido que o modelo de PR omita a lista de autoverificação e a declaração de alterações disruptivas.

## Arquivos relacionados

- Para os limites de responsabilidade dos arquivos, ver a [matriz de documentação](./document-matrix.md)
- Para o processo de contribuição, ver a [especificação de guia de contribuição](./contribution-guide-specification.md)
- Para os critérios de revisão, ver a [especificação de revisão de código](./code-review-specification.md)
- Para a migração de alterações disruptivas, ver a [especificação de guia de migração](./migration-guide-specification.md)
- As verificações de governança comunitária pertencem à dimensão D14; ver a [matriz de dimensões de revisão](./review-dimension-matrix.md)
