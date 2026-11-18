# Relatório de pesquisa sobre modelos de README

> Problema que este arquivo resolve: registrar o método de pesquisa, a escala da amostra e as descobertas quantitativas deste modelo padrão de README, fornecendo base de dados ao [modelo padrão de README](./readme-standard-template.md) e às especificações específicas, além de explicitar os limites e as limitações do método.

## 1. Objetivos e método da pesquisa

### 1.1 Objetivo

Pesquisar projetos open source de destaque com maior número de estrelas, identificando padrões recorrentes de estrutura, organização de seções, apresentação visual e uso de selos em seus READMEs e documentações associadas, a fim de consolidar especificações gerais e modelos reutilizáveis.

### 1.2 Fontes de dados

- Metadados dos repositórios: GitHub GraphQL Search API, em ordem decrescente de estrelas, com filtro `is:public archived:false fork:false`.
- Texto original dos READMEs: GitHub REST Contents API (endpoint `readme`), obtido em base64 ou formato raw e então analisado.
- Parâmetros de selos: documentação oficial do Shields.io (páginas Static Badge e Logos) e descrição do formato badge-maker.
- Práticas da comunidade chinesa: a documentação do projeto, as mensagens de commit e as seções de divulgação de phodal/github (*Guia de exploração do GitHub*, 11,362 estrelas), usados para complementar princípios de redação e experiência operacional não cobertos pelas estatísticas automatizadas.

### 1.3 Método de coleta

1. **Metadados**: uma única consulta à GitHub Search API retorna no máximo 1000 registros. Para ampliar a amostra, adotou-se o fatiamento por faixas de estrelas — localizando por bisseção o limiar de estrelas correspondente a cada 1000 posições e descendo em lotes sucessivos, totalizando 11 lotes, obtiveram-se ao final os metadados de 10,995 repositórios de destaque.
2. **Amostragem de READMEs**: dentro dos 1000 repositórios de destaque, realizou-se amostragem estratificada pela linguagem principal, cobrindo as principais linguagens, como Python, TypeScript, JavaScript, Rust, Go e C++, com 120 repositórios sorteados; em todos eles o texto original do README foi obtido com sucesso.
3. **Critério estatístico**: a taxa de ocorrência de seções e a taxa de uso de elementos foram calculadas por repositório; o estilo dos selos e os parâmetros de logo foram contados pelo número de ocorrências na URL.

### 1.4 Limitações do método (a explicitar)

- A GitHub Search API impõe limite de 1000 registros por consulta; este relatório ampliou a escala pelo acúmulo de fatias, mas as fronteiras das fatias são afetadas por empates no número de estrelas, de modo que a amostra é um conjunto aproximado de projetos de destaque, e não um ranking estritamente contínuo.
- A escala da amostragem de READMEs é de 120; as conclusões refletem tendências e características comuns, sem representar a distribuição estatisticamente significativa de todos os projetos de destaque.
- A identificação de seções baseia-se na correspondência de palavras-chave nos títulos, havendo viés estatístico decorrente de diferenças de redação.
- A estatística de parâmetros de selos considera os parâmetros explicitamente presentes na URL; os parâmetros padrão de selos dinâmicos não foram contabilizados.

## 2. Distribuição dos repositórios de destaque (metadados)

### 2.1 Escala da amostra

- Uma única consulta obtém de forma estável os 1000 repositórios de destaque, com faixa de estrelas entre aproximadamente 563,574 e 30,857.
- Com o acúmulo de 11 lotes fatiados, a escala foi ampliada para 10,995 repositórios de destaque, com limite inferior de 5,452 estrelas.

### 2.2 Distribuição por linguagem (com base nos 1000 de destaque)

| Linguagem | Quantidade | Proporção |
| --- | --- | --- |
| Python | 223 | 22.3% |
| TypeScript | 178 | 17.8% |
| JavaScript | 112 | 11.2% |
| Rust | 80 | 8.0% |
| Sem linguagem principal | 74 | 7.4% |
| Go | 68 | 6.8% |
| C++ | 55 | 5.5% |
| Java | 27 | 2.7% |

Os projetos de destaque concentram-se em Python, TypeScript e JavaScript, que juntos somam mais de 50%; linguagens de sistema como Rust e Go têm participação significativa. Isso determina que o modelo deve cobrir comandos de instalação por gerenciadores de pacotes de várias linguagens e selos de múltiplos ambientes de execução.

### 2.3 Distribuição por licença (com base nos 1000 de destaque)

| Licença | Quantidade | Proporção |
| --- | --- | --- |
| MIT | 399 | 39.9% |
| Apache-2.0 | 197 | 19.7% |
| Não identificada (NOASSERTION) | 148 | 14.8% |
| Sem licença (NONE) | 65 | 6.5% |
| GPL-3.0 | 51 | 5.1% |
| AGPL-3.0 | 50 | 5.0% |
| BSD-3-Clause | 17 | 1.7% |

A MIT ocupa posição dominante, sendo a recomendação padrão do modelo genérico; ao mesmo tempo, devem ser preservados os marcadores de posição de identificadores SPDX de opções como Apache-2.0 e GPL.

## 3. Descobertas sobre a estrutura do README (N=120)

### 3.1 Taxa de ocorrência de seções

| Palavra-chave da seção | Repositórios com ocorrência | Taxa de ocorrência |
| --- | --- | --- |
| Contributing / contribuição | 66 | 55.0% |
| License / licença | 52 | 43.3% |
| Install / instalação | 49 | 40.8% |
| Quick Start / início rápido | 28 | 23.3% |
| Documentation / documentação | 25 | 20.8% |
| Development / desenvolvimento | 22 | 18.3% |
| Configuration / configuração | 19 | 15.8% |
| Features / funcionalidades | 19 | 15.8% |
| Security / segurança | 15 | 12.5% |
| Usage / uso | 12 | 10.0% |
| Requirements / ambiente de dependências | 11 | 9.2% |
| API | 10 | 8.3% |
| Examples / exemplos | 10 | 8.3% |

Descoberta: o guia de contribuição e a licença são itens padrão dos projetos de destaque, refletindo a prioridade da governança comunitária e da conformidade; instalação e início rápido vêm logo em seguida. Por isso, o modelo classifica ambos como obrigatórios.

### 3.2 Taxa de uso de elementos visuais

| Elemento | Repositórios com ocorrência | Taxa de ocorrência | Mediana (por repositório) |
| --- | --- | --- | --- |
| Blocos de código | 80 | 66.7% | 2 |
| Imagens | 76 | 63.3% | 2 |
| Selos (Shields.io) | 61 | 50.8% | 1 |
| Tabelas | 44 | 36.7% | 0 |

Mediana da hierarquia de títulos: 7 títulos de segundo nível; mediana do comprimento dos arquivos: 171 linhas. Isso indica que os READMEs de destaque são em geral mantidos em comprimento médio, organizados com 6 a 12 títulos de segundo nível.

### 3.3 Adaptação a temas (primeiras 40 amostras)

| Característica | Repositórios com ocorrência |
| --- | --- |
| Contêiner centralizado (`align="center"`) | 27 |
| Elemento `<picture>` | 12 |
| Alternância de tema claro e escuro (`prefers-color-scheme`) | 12 |
| `for-the-badge` com `labelColor` | 2 |

O contêiner centralizado é a técnica dominante na primeira tela; cerca de um terço dos projetos oferece imagens em versões para temas claro e escuro.

## 4. Descobertas sobre selos

### 4.1 Parâmetros de estilo (por número de ocorrências na URL, N=120)

| style | Ocorrências |
| --- | --- |
| `for-the-badge` | 65 |
| `flat-square` | 60 |
| `flat` | 32 |
| `social` | 12 |
| `plastic` | 1 |

`for-the-badge` e `flat-square` são os mais populares; `plastic` está praticamente em desuso. Detalhes na [especificação de selos](./badge-specification.md).

### 4.2 Parâmetros de logo (por número de ocorrências, N=120)

| slug do logo | Ocorrências |
| --- | --- |
| `github` | 35 |
| `discord` | 20 |
| `npm` | 4 |
| `apple` / `docker` / `linkedin` / `x` | 2 a 3 cada |

GitHub e Discord são os ícones mais frequentes, correspondendo a duas categorias de informação: “repositório de código-fonte” e “canal da comunidade”.

## 5. Evidência da primeira tela de projetos de referência

| Projeto | Tipo | Características da primeira tela |
| --- | --- | --- |
| `sindresorhus/awesome` | Coleção de recursos | Logotipo centralizado, área de patrocínio, sumário por categoria temática |
| `axios/axios` | Biblioteca | Avisos importantes, tabela de patrocínio, multilíngue |
| `sharkdp/fd` | CLI | Selos + links de idioma, navegação de seções, GIF de demonstração |
| `BurntSushi/ripgrep` | CLI | Selos, links rápidos, captura de tela de busca, comparação de desempenho |
| `vercel/next.js` | Framework | Logotipo centralizado, selos `for-the-badge`, entradas de documentação e comunidade |
| `microsoft/vscode` | Aplicação | Selos, descrição do repositório, captura de tela do produto, entradas de contribuição e feedback |
| `rust-lang/rust` | Linguagem | Banner centralizado, linha de navegação, pontos de valor do Why Rust |
| `phodal/github` | E-book em chinês | Quatro perguntas da primeira tela, exemplos de texto em uma frase, princípio de simplificação da instalação, lista de canais de divulgação |

Característica comum: a primeira tela responde “o que é, como usar e onde estão os detalhes”; os selos ficam junto ao título; a captura de tela ou demonstração vem logo após o posicionamento; as entradas de contribuição e comunidade ficam mais abaixo, mas são indispensáveis.

## 6. Conclusões consolidadas

1. O modelo genérico deve ter como eixo “posicionamento → instalação → início rápido → documentação → contribuição → licença”.
2. Os selos devem usar por padrão `flat-square` ou `for-the-badge`, de forma uniforme em todo o texto, em quantidade de 4 a 6.
3. Imagens e blocos de código são o núcleo de uma primeira tela atrativa, devendo ser acompanhados de `alt` e de marcação de linguagem.
4. O tipo de projeto determina a seleção de seções, conforme o [guia de adaptação do README por categoria](./readme-category-adaptation-guide.md).
5. Conformidade e governança comunitária (licença, guia de contribuição) são consenso entre os projetos de destaque, sendo classificadas como obrigatórias.

## 7. Explicação da escala de dados

Resultado acumulado do fatiamento dos metadados dos repositórios de destaque: 10,995 repositórios, com faixa de estrelas de 563,575 a 5,452. A distribuição de licenças e de linguagens dessa amostra de escala de dez mil é a seguinte, consistente com as conclusões da amostra dos 1000 de destaque:

| Dimensão | Distribuição |
| --- | --- |
| Linguagem | Python 1,995, TypeScript 1,529, JavaScript 1,279, sem linguagem principal 888, Go 847, C++ 531, Java 528, Rust 507 |
| Licença | MIT 4,160 (37.8%), Apache-2.0 2,073 (18.9%), não identificada 1,463, sem licença 1,106, GPL-3.0 747 |

A amostra da estatística aprofundada de READMEs é de 120 arquivos, todos obtidos com sucesso. O fatiamento adota limiares aproximados de estrelas, constituindo um conjunto aproximado de projetos de destaque, e não um ranking estritamente contínuo.

## Arquivos relacionados

- O modelo de aplicação direta está no [modelo padrão de README](./readme-standard-template.md)
- A especificação de selos está na [especificação de selos](./badge-specification.md)
- A especificação visual está na [especificação de layout visual do README](./readme-visual-layout-specification.md)
- A adaptação por categoria está no [guia de adaptação do README por categoria](./readme-category-adaptation-guide.md)
- A definição de seções está na [especificação de seções do README](./readme-sections-specification.md)
