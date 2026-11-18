# Especificação de nomes de projeto

> Problema que este arquivo resolve: definir as regras obrigatórias de caracteres, maiúsculas e minúsculas, segmentação, comprimento e semântica do nome do repositório, bem como a fórmula de nomenclatura, os sufixos convencionais, o processo de busca e os requisitos de metadados associados.

## 1. Regras obrigatórias

| Regra | Requisito | Contraexemplo |
|---|---|---|
| Conjunto de caracteres | Apenas `a-z`, `0-9`, `-` | `My_Proj`, `我的项目` |
| Maiúsculas e minúsculas | Tudo em minúsculas | `MyProject` |
| Segmentação | kebab-case, unido com `-` | `myproject`, `my_project` |
| Comprimento | 2–25 caracteres | Nomes concatenados demasiado longos |
| Terminação | Substantivo ou fechamento com sufixo de forma | Terminar em `-project` ou `-test` |
| Versão | Sem número de versão, ano nem data | `tool-v2`, `app2024` |
| Palavras sem informação | Proíbem-se `my`/`demo`/`test`/`new`/`tmp` | `my-new-demo` |
| Unicidade | Uma busca em GitHub / npm / PyPI, respectivamente | Coincidir com uma biblioteca conhecida |
| Semântica | O próprio nome permite ler “o que faz” | `xyz`, `abc123` |

## 2. Fórmula de nomenclatura (escolher uma entre quatro)

```text
<技术>-<对象>          vue-virtual-table      go-ratelimit
<对象>-<形态>          note-cli   image-api   config-loader
<动词>-<对象>          parse-markdown   sync-dotfiles
<领域>-<子领域>        web-ui-kit   data-pipeline
```

## 3. Sufixos convencionais

`-cli` linha de comando / `-sdk` biblioteca de cliente / `-api` `-server` lado servidor / `-template` `-boilerplate` andaime / `-loader` `-parser` middleware / `-kit` conjunto de componentes / `-notes` `-guide` documentação / `dotfiles` repositório de configuração / `awesome-xxx` coleção de recursos.

## 4. Processo de nomenclatura

1. Escrever em uma frase “a quem o projeto resolve qual problema”.
2. Extrair dessa frase o substantivo central + a forma e aplicar qualquer fórmula da seção 2.
3. Gerar 3 candidatos e realizar a busca de duplicados para cada um.
4. Escolher o que possa ser melhor compreendido sem ler o README.
5. O nome em chinês não é escrito no nome do repositório, mas após o título da primeira linha do README.

## 5. Metadados associados

### 5.1 Descrição do repositório (description)

- Tem a mesma origem do nome do repositório; estrutura: `<o que faz> for <para quem>`.
- Formato combinado bilíngue: `idioma nacional | inglês`, escrevendo primeiro a versão no idioma nacional, seguida de uma barra vertical de largura normal (com um espaço de cada lado) e depois a versão em inglês. Exemplo de um projeto em chinês:

```text
轻量级 Go 命令行 JSON 处理工具 | A lightweight Go CLI for JSON processing
```

- Comprimento: o idioma nacional e o inglês não devem exceder 120 caracteres cada um, e o total bilíngue não deve exceder 350 caracteres (limite do GitHub).
- Critério de escolha quando o total bilíngue excede o limite: comprime-se prioritariamente a versão em inglês, e não a versão no idioma nacional — o chinês tem maior densidade de informação, e comprimir o chinês perde mais informação; ao comprimir, eliminam-se primeiro os modificadores e as qualificações repetidas, combinam-se depois as expressões sinônimas e conserva-se por último a estrutura completa de sujeito e predicado de cada versão linguística.
- Sem quebras de linha, sintaxe Markdown nem Emoji; o estilo de pontuação final dos dois idiomas deve ser mantido coerente (com ponto final em ambos ou sem ponto final em ambos).

### 5.2 Tópicos (topics)

- Preencher os 20 (limite do GitHub), com cobertura completa e sem deixar posições vazias.
- Todos em inglês; não devem ser usados o chinês nem outros idiomas; tudo em minúsculas, unido com `-`, sem espaços nem caracteres especiais.
- Cobrir integralmente as cinco categorias: linguagem, domínio, forma, ecossistema e cenário; além disso, podem ser acrescentados termos genéricos como documentation e open-source.
- Definir no momento da criação do repositório, sem deixar vazios; revisar uma vez após a mudança de nome ou o reposicionamento do repositório.

## Arquivos relacionados

- A conformidade de nomenclatura pertence à regra absoluta H1; ver as [regras absolutas](./hard-rules.md)
- A revisão de metadados pertence à dimensão D10; ver a [matriz de dimensões de revisão](./review-dimension-matrix.md)
- O documento que a desenvolve é `docs/naming.md`; ver a [matriz de documentação](./document-matrix.md)
