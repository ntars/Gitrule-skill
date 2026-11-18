# Especificação de fluxos de trabalho de CI

> Problema que este arquivo resolve: definir as condições de disparo, a divisão de tarefas, a estratégia de cache e a configuração de segurança dos fluxos de trabalho de integração contínua em `.github/workflows/*.yml`, tornando a compilação, os testes e as verificações reproduzíveis e auditáveis.

## 1. Princípios de design

1. **Responsabilidade única**: cada fluxo de trabalho responde por apenas uma classe de objetivo (compilação, testes, publicação, implantação de documentação); publicação e testes não devem ser misturados em um mesmo fluxo de trabalho.
2. **Feedback rápido**: verificações leves (lint, formatação) primeiro; tarefas demoradas (matriz completa de testes) depois.
3. **Reprodutibilidade**: fixar as versões das dependências, usar Actions com versão fixa; o cache serve apenas para acelerar e não altera o resultado.
4. **Privilégio mínimo**: o fluxo de trabalho concede permissões conforme a tarefa, com padrão somente leitura; tarefas de publicação elevam privilégios separadamente (ver [especificação de segurança e privacidade](./security-and-privacy-specification.md)).

## 2. Estrutura de arquivos

### 2.1 Nomenclatura e caminho

- O caminho é fixo: `.github/workflows/*.yml`.
- O nome do arquivo usa minúsculas e hífen, nomeado conforme a responsabilidade, como `ci.yml`, `release.yml`, `docs.yml`.
- O campo `name` do fluxo de trabalho deve ser semanticamente consistente com o nome do arquivo.

### 2.2 Blocos obrigatórios

| Bloco | Função | Requisito |
| --- | --- | --- |
| `name` | Nome exibido do fluxo de trabalho | Conciso e capaz de expressar a responsabilidade |
| `on` | Condições de disparo | Branch, caminho ou evento explícitos |
| `permissions` | Declaração de permissões | Declaração explícita, mínimo por padrão |
| `jobs` | Conjunto de tarefas | Dividido por responsabilidade |

### 2.3 Design das condições de disparo

| Evento de disparo | Aplicação | Atenção |
| --- | --- | --- |
| `push` | Branch principal e branches de publicação | Restringir o escopo de branches, evitando disparo em todos os branches |
| `pull_request` | Todos os PRs | Garantir a verificação antes do merge |
| `workflow_dispatch` | Disparo manual | Para operações controladas, como publicação e reversão |
| `schedule` | Tarefas agendadas | Para verificação de atualização de dependências e builds noturnos |
| `release` | Ações após a publicação | Para upload de artefatos e anúncios |

## 3. Divisão de tarefas

Ordem de fases recomendada:

1. **Análise estática**: formatação, lint, verificação de tipos.
2. **Compilação**: gerar os artefatos de compilação para reutilização pelas tarefas seguintes.
3. **Testes**: testes unitários e de integração, que podem ser executados em paralelo por matriz.
4. **Validação de artefatos**: verificar tamanho, assinatura ou integridade dos artefatos de compilação.
5. **Publicação**: executada somente quando a CI estiver totalmente verde e as condições atendidas (ver [especificação de push e publicação](./push-and-release-specification.md)).

As dependências entre tarefas são declaradas por meio de `needs`, garantindo interrupção imediata em caso de falha; tarefas seguintes não devem prosseguir em estado de falha.

## 4. Compilação em matriz

Usar `strategy.matrix` para cobrir múltiplas versões e múltiplas plataformas:

```yaml
strategy:
  fail-fast: false
  matrix:
    os: [ubuntu-latest, macos-latest, windows-latest]
    node-version: [18, 20, 22]
```

Requisitos:

- A cobertura de versões deve abranger a versão mínima e a mais recente declaradas como suportadas pelo projeto (ver [explicação de compatibilidade](./readme-sections-specification.md), seção 14).
- `fail-fast` deve ser definido como `false`, para que cada combinação seja executada integralmente, facilitando a localização de problemas de compatibilidade.
- A matriz não deve ter mais de três dimensões, evitando a explosão de combinações.

## 5. Estratégia de cache

| Objeto de cache | Sugestão de chave | Atenção |
| --- | --- | --- |
| Diretório de dependências | Hash do arquivo de lock do gerenciador de pacotes | Invalidado assim que o arquivo de lock mudar |
| Artefatos de compilação | Hash do código-fonte e da configuração | Consistente com as entradas de compilação |
| Cadeia de ferramentas | Número da versão | Invalidado assim que a versão for atualizada |

O cache apenas acelera e não altera o resultado da compilação; mesmo com acerto de cache, os testes completos devem ser executados.

## 6. Configuração de segurança

1. As chaves são injetadas via Secrets do repositório; é proibido gravá-las nos arquivos de fluxo de trabalho ou nos registros.
2. Cada fluxo de trabalho declara `permissions` explicitamente, com `contents: read` por padrão.
3. As referências a Actions de terceiros devem usar versão fixa ou hash de commit, evitando etiquetas flutuantes.
4. Quando o PR vem de um Fork, é proibido injetar Secrets, prevenindo ataques de elevação de privilégio.
5. As tarefas de publicação devem ser separadas das verificações principais e disparadas apenas em branches protegidos ou tags.

## 7. Selo de status

O fluxo de trabalho deve fornecer ao README um selo de status, no formato:

```markdown
[![CI](https://github.com/{owner}/{repo}/actions/workflows/ci.yml/badge.svg)](https://github.com/{owner}/{repo}/actions/workflows/ci.yml)
```

Para os parâmetros e a disposição dos selos, ver a [especificação de selos](./badge-specification.md).

## 8. Práticas proibidas

1. É proibido codificar de forma fixa chaves ou endereços internos no fluxo de trabalho.
2. É proibido usar `continue-on-error` para mascarar falhas de teste.
3. É proibido configurar múltiplas regras de disparo conflitantes para a mesma condição.
4. É proibido publicar quando a verificação do branch principal não tiver sido aprovada.

## Arquivos relacionados

- Para os limites de responsabilidade dos arquivos, ver a [matriz de documentação](./document-matrix.md)
- Para compilação e testes locais, ver a [especificação de testes](./testing-specification.md)
- Para o encadeamento com a publicação, ver a [especificação de push e publicação](./push-and-release-specification.md)
- As verificações automatizadas pertencem à dimensão D9; ver a [matriz de dimensões de revisão](./review-dimension-matrix.md)
- Para a linha vermelha de chaves, ver H3 em [regras absolutas](./hard-rules.md)
