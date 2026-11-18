# Especificação de promoção de código aberto

> Problema que este arquivo resolve: definir os canais de promoção, o ritmo de publicação, os materiais da página inicial e as regras de operação da comunidade para projetos de código aberto antes e depois do lançamento, de modo que o projeto obtenha, com base em documentação utilizável, uma exposição compatível com o público-alvo.

A lista de canais e os princípios deste arquivo baseiam-se no capítulo sobre promoção do *Guia de exploração do GitHub*, de phodal; o projeto verificou a aplicabilidade dessas práticas na comunidade de código aberto em chinês com a escala de 11,362 stars.

## 1. Princípios básicos

1. **Qualidade antes da promoção**: a promoção apenas amplia a qualidade existente e não corrige ausências. Não se deve iniciar a promoção antes de README, exemplos, documentação e testes estarem prontos.
2. **O projeto em si não é tudo na promoção**: além do código e do README, deve-se preparar documentação detalhada, programas de exemplo e mecanismos de resposta a problemas.
3. **Motivação clara**: a promoção serve a objetivos concretos (obter usuários iniciais, recrutar contribuidores, coletar feedback) e não deve ser feita para perseguir número de stars.
4. **Canal compatível**: escolher canais conforme a stack tecnológica e o público-alvo do projeto, evitando divulgação indiscriminada.
5. **Apresentação honesta**: é proibido inventar números de stars, volume de downloads ou casos de uso; a comparação de características deve basear-se em fatos verificáveis.

## 2. Lista de preparação antes do lançamento

| Categoria | Requisito | Base de julgamento |
| --- | --- | --- |
| Página inicial | O README passa na verificação das quatro perguntas (o que faz / o que resolve / características / exemplo) | [especificação de seções do README](./readme-sections-specification.md) |
| Texto de uma frase | Categoria e qualificadores claros, capaz de ser repetido de forma autônoma | seção 1.1 do mesmo documento |
| Exemplo | Hello world executável em até dois passos | [modelo padrão de README](./readme-standard-template.md) |
| Documentação | Instalação, configuração e documentação de API completas | [matriz de documentação](./document-matrix.md) |
| Licença | LICENSE existe e é coerente com a identificação no README | [especificação de LICENSE](./license-specification.md) |
| Conformidade | O NOTICE cobre as dependências de terceiros | [especificação de NOTICE](./notice-specification.md) |
| Entradas da comunidade | Modelos de Issue, guia de contribuição e código de conduta prontos | [especificação do guia de contribuição](./contribution-guide-specification.md) |
| Mecanismo de resposta | Responsável e prazo de resposta a problemas definidos | [especificação de resposta a incidentes](./incident-response-specification.md) |

Promover sem concluir a lista acima é uma conduta proibida por esta especificação.

## 3. Classificação de canais

### 3.1 Comunidades técnicas internacionais

| Canal | Conteúdo adequado | Advertências |
| --- | --- | --- |
| Hacker News | Implementação técnica, engenharia de software com profundidade | O título deve ser sóbrio, evitando linguagem de marketing |
| Subreddits correspondentes do Reddit | Bibliotecas, ferramentas, frameworks | Respeitar as regras de autopromoção de cada subreddit |
| Lobsters | Programação de sistemas, práticas de engenharia | A comunidade é sensível a marketing |
| Boletins técnicos (JavaScript Weekly etc.) | Bibliotecas e ferramentas | Fornecer um resumo conciso do projeto |
| Blog oficial e site de documentação | Apresentações aprofundadas e notas de versão | Servem de destino para os demais canais |

### 3.2 Comunidades técnicas em chinês

| Canal | Conteúdo adequado |
| --- | --- |
| Juejin | Frontend, mobile, práticas de engenharia |
| Developer Headlines | Projetos técnicos em geral |
| V2EX | Ferramentas, software de produtividade, projetos de empreendedorismo |
| Zhihu | Análise técnica e decisões de design |
| Conta oficial no WeChat | Artigos longos aprofundados, séries de tutoriais |
| Geek Headlines | Notícias técnicas em geral |

### 3.3 Canais próprios do projeto

1. As entradas da comunidade no README do projeto (Discussions, Discord);
2. As contas sociais próprias do projeto, usadas para anunciar versões e atividades;
3. O site de documentação e o site de exemplos, como páginas de recepção do tráfego externo.

## 4. Ritmo de publicação

1. **Período de aquecimento**: concluir a lista da seção 2 e preparar materiais como o texto de uma frase, capturas de tela e GIF de demonstração.
2. **Período de lançamento**: publicar em 1 ou 2 canais mais compatíveis, evitando repetir o mesmo conteúdo em várias plataformas ao mesmo tempo.
3. **Período de resposta**: manter alta frequência de resposta nas 72 horas seguintes ao lançamento, tratando Issues e feedback.
4. **Período de iteração**: atualizar continuamente conforme o ritmo de publicação de versões, com nota de alterações em cada lançamento.
5. **Período de consolidação**: organizar as perguntas frequentes em um FAQ e realimentar a documentação.

## 5. Requisitos dos materiais da página inicial

| Material | Especificação | Uso |
| --- | --- | --- |
| Texto de uma frase | Até 60 caracteres em chinês / até 25 palavras em inglês; a description do repositório adota o formato combinado bilíngue “idioma nacional \| inglês”, ver a seção 5 da [especificação de nomes de projeto](./project-naming-specification.md) | Description do repositório, resumo em redes sociais |
| Captura de tela | Duas versões, tema claro e escuro, com largura controlada | Primeira tela do README |
| GIF de demonstração | Volume controlado após compressão, mostrando o fluxo principal | Seção de demonstração do README |
| Logo | Formato SVG, com versões clara e escura | Primeira tela e cartões sociais |
| Tabela comparativa de características | Baseada em fatos verificáveis, incluindo cenários não aplicáveis | README ou site de documentação |

Os materiais devem ser atualizados junto com as versões, evitando exibir interfaces antigas.

## 6. Operação da comunidade

1. Oferecer entradas claras para quem contribui pela primeira vez, como a etiqueta `good first issue`.
2. A resposta a problemas deve ter registro, evitando a repetição de questões já resolvidas.
3. O código de conduta se aplica a todos os canais da comunidade, ver a [especificação de código de conduta](./code-of-conduct-specification.md).
4. Os agradecimentos aos contribuidores devem ser concentrados em um local, evitando dispersão pelo texto.
5. Não deve ser obtida atenção falsa por meio de incentivo a stars, trocas de curtidas e práticas semelhantes.

## 7. Práticas proibidas

1. É proibido promover quando a lista de qualidade não estiver concluída.
2. É proibido inventar ou exagerar dados e casos de uso do projeto.
3. É proibido repetir o mesmo conteúdo em vários canais ao mesmo tempo.
4. É proibido depreciar projetos semelhantes para valorizar a própria imagem.
5. É proibido usar meios de indução para obter número de stars.

## Arquivos relacionados

- As quatro perguntas da página inicial e o texto de uma frase estão na [especificação de seções do README](./readme-sections-specification.md)
- As especificações dos materiais visuais estão na [especificação de layout visual do README](./readme-visual-layout-specification.md)
- As regras das entradas da comunidade estão na [especificação do guia de contribuição](./contribution-guide-specification.md)
- O mecanismo de resposta a problemas está na [especificação de resposta a incidentes](./incident-response-specification.md)
- As notas de versão estão na [especificação de push e publicação](./push-and-release-specification.md)
- A origem da pesquisa está no [relatório de pesquisa sobre modelos de README](./readme-template-research-report.md)
