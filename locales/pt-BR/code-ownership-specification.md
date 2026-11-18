# Especificação de propriedade de código

> Problema que este arquivo resolve: definir a sintaxe do arquivo `.github/CODEOWNERS`, a atribuição de propriedade e as regras de roteamento de revisão, de modo que cada alteração seja automaticamente atribuída a revisores responsáveis.

## 1. Princípios de projeto

1. **Mapeamento explícito de caminho para pessoa**: cada regra indica quem é responsável por determinado caminho, evitando revisão ausente ou revisão duplicada.
2. **Mínimo necessário de owners**: o número de proprietários de um caminho deve ficar entre 1 e 3; em excesso, a responsabilidade se dispersa.
3. **Herança padrão**: deve ser definido um proprietário padrão global, que cobre os caminhos não correspondidos por regras explícitas.
4. **Sincronia com a estrutura da equipe**: a atualização deve ocorrer sempre que houver mudança de membros, evitando que contas inativas bloqueiem a revisão.

## 2. Localização e sintaxe do arquivo

### 2.1 Caminho

O arquivo `CODEOWNERS` pode ser colocado em qualquer um dos locais abaixo, adotando-se o primeiro encontrado por ordem de prioridade:

1. `CODEOWNERS` na raiz do repositório;
2. `docs/CODEOWNERS`;
3. `.github/CODEOWNERS` (recomendado).

### 2.2 Regras de sintaxe

```text
# Comentários começam com #
<padrão de caminho>  <proprietário>  [<proprietário>...]
```

- Uma regra por linha, com o padrão de caminho seguido de um ou mais proprietários.
- O formato do proprietário é `@nome-de-usuário` ou `@organização/equipe`.
- O uso de e-mail como proprietário exige associação com uma conta do GitHub.
- Os caminhos diferenciam maiúsculas de minúsculas e aceitam os curingas `*` e `**`.

### 2.3 Exemplo

```text
# Proprietário padrão
*                       @org/maintainers

# Atribuição por diretório
/src/core/              @org/core-team
/src/api/               @org/api-team @alice
/docs/                  @org/docs-team

# Atribuição por tipo de arquivo
*.md                    @org/docs-team
/.github/workflows/      @org/devops-team
```

## 3. Regras de correspondência

1. Apenas a última regra correspondente tem efeito, sem acumulação; por isso as regras genéricas devem vir primeiro e as regras específicas depois.
2. Uma regra de diretório corresponde ao diretório e aos seus subdiretórios, salvo quando iniciada por `/`, o que restringe o caminho à raiz.
3. A ordem das regras determina a prioridade e deve ir do mais amplo ao mais restrito.
4. Caminhos sem correspondência têm a revisão atribuída ao proprietário padrão.

## 4. Estratégia de atribuição de propriedade

| Dimensão | Base de atribuição |
| --- | --- |
| Diretório | Atribuição pelas fronteiras de módulo ou subsistema |
| Tipo de arquivo | Documentação, configuração e testes podem ser atribuídos por tipo |
| Caminhos críticos | Segurança, publicação e configuração de CI ficam exclusivamente com os mantenedores centrais |
| Novos membros | Participam primeiro como revisores não obrigatórios e passam a proprietários formais após se familiarizarem |

## 5. Integração com o fluxo de revisão

1. Na criação do PR, o GitHub solicita automaticamente a revisão dos proprietários dos caminhos correspondentes.
2. A exigência de revisão obrigatória é configurada nas regras de proteção de branch, conforme a [especificação de fluxo de trabalho Git e branches](./git-workflow-and-branching-specification.md).
3. Os proprietários devem responder dentro do prazo acordado; em caso de atraso, a responsabilidade passa ao proprietário padrão.
4. Mudanças de proprietário exigem atualização simultânea do arquivo, evitando que contas inativas bloqueiem o fluxo (ver [especificação de revisão de código](./code-review-specification.md)).

## 6. Requisitos de manutenção

1. A revisão deve ocorrer após cada mudança de estrutura organizacional ou de responsabilidades da equipe.
2. Transferências de repositório e saídas de membros exigem remoção imediata do proprietário correspondente.
3. Alterações no arquivo exigem revisão de pelo menos um proprietário atual, impedindo a expansão autônoma de permissões.
4. Os proprietários não devem apontar para contas inativas ou contas de bot (exceto as dedicadas à automação).

## 7. Práticas proibidas

1. É proibido usar regras curinga excessivamente amplas que tornem todos proprietários.
2. É proibido atribuir caminhos sensíveis (publicação, configuração de segredos) a membros sem capacidade de revisão.
3. É proibido gravar dados de contato pessoais no arquivo.
4. É proibido manter indefinidamente a propriedade de membros que já deixaram a equipe.

## Arquivos relacionados

- As fronteiras de responsabilidade dos arquivos estão na [matriz de documentação](./document-matrix.md)
- Critérios e responsabilidades de revisão estão na [especificação de revisão de código](./code-review-specification.md)
- Proteção de branch está na [especificação de fluxo de trabalho Git e branches](./git-workflow-and-branching-specification.md)
- As verificações automatizadas pertencem à dimensão D9, ver [matriz de dimensões de auditoria](./review-dimension-matrix.md)
