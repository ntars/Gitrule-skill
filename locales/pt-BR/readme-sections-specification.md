# Especificação de seções do README

> Problema que este arquivo resolve: definir as 20 seções que o README de cada diretório de idioma deve conter, o conteúdo que cada seção deve conter e não deve apresentar, bem como o formato padrão da linha de direitos autorais.

## 1. Requisitos gerais das seções

As 20 seções a seguir devem existir integralmente, em ordem fixa, com correspondência um a um entre as versões de cada idioma.

| Número | Seção | Deve conter | Não deve apresentar |
| --- | --- | --- | --- |
| 1 | Nome e posicionamento do projeto | Nome do projeto, descrição do repositório (formato bilíngue combinado `idioma nacional \| inglês`), etiquetas de tópico (completar as 20, apenas em inglês), posicionamento em uma frase, links de troca de idioma, versão atual, estado de manutenção | Adjetivos vagos; descrição do repositório com mais de 120 caracteres; etiquetas de tópico com maiúsculas e minúsculas misturadas ou contendo palavras que não sejam em inglês |
| 2 | Apresentação do projeto | Contexto, problema a resolver, ideia central, cenários aplicáveis, cenários não aplicáveis, e vantagens e limitações apresentadas separadamente (as limitações devem incluir o alcance do impacto e a forma de contorno) | Resumir em uma única frase; listar apenas vantagens sem limitações |
| 3 | Funcionalidades principais | Itens de funcionalidade agrupados por módulo, cada um com condição de acionamento e resultado | Listar apenas nomes de funcionalidades |
| 4 | Características principais | Desenvolvidas conforme a estrutura de [redação de características e decisões de engenharia](./features-and-engineering-tradeoffs-guide.md) | Elogios sem evidência |
| 5 | Detalhes de projeto e decisões de engenharia | Desenvolvidos conforme a estrutura de [redação de características e decisões de engenharia](./features-and-engineering-tradeoffs-guide.md) | Descrições duplicadas em relação às funcionalidades |
| 6 | Pilha tecnológica e lista de dependências | Ambiente de execução, compilação, cadeia de ferramentas de testes e restrições de versão; o detalhamento das dependências aponta para o NOTICE | Ausência de número de versão |
| 7 | Instalação e implantação | Requisitos de ambiente, passos de instalação, comandos de verificação, formas de atualização e desinstalação, explicação sobre conteinerização | Pular etapas ou omitir a verificação |
| 8 | Início rápido | Exemplo mínimo executável, com comandos completos e saída esperada | Pseudocódigo não executável |
| 9 | Explicação de configuração | Tabela de itens de configuração (nome da chave, tipo, valor padrão, obrigatoriedade, faixa de valores, função, exemplo), prioridade de configuração, suporte a atualização a quente | Ausência de valor padrão |
| 10 | API ou explicação de módulos | Assinatura da interface, parâmetros, valor de retorno, códigos de erro, exemplo de chamada, limitação de taxa e cota | Ausência de códigos de erro |
| 11 | Estrutura de diretórios | Estrutura em árvore e responsabilidade de cada nível | Enumeração arquivo por arquivo sem explicação |
| 12 | Desempenho | Ambiente de teste, método de teste, dados de métricas, análise de gargalos, recomendações de ajuste | Números sem condições de teste |
| 13 | Segurança e privacidade | Coleta e armazenamento de dados, criptografia em trânsito, modelo de permissões, canal de notificação de vulnerabilidades, riscos conhecidos | Prometer segurança absoluta |
| 14 | Explicação de compatibilidade | Matriz de versões de sistema operacional, ambiente de execução, navegador e banco de dados, com indicação explícita dos itens não suportados | Formulações ambíguas |
| 15 | Problemas conhecidos e limitações | Problemas conhecidos (descrição, alcance do impacto, solução temporária de contorno, link de acompanhamento), limitações atuais, lista de funcionalidades não implementadas (funcionalidade, motivo da não implementação, estado do planejamento) | Ocultar defeitos graves; apresentar funcionalidades não implementadas como implementadas |
| 16 | Registro de alterações | Seguir a estrutura do Keep a Changelog, com números de versão conforme o versionamento semântico | Itens sem data |
| 17 | Roteiro posterior | Itens planejados, estado, versão-alvo, com a marcação “não é compromisso” | Prometer prazos de entrega |
| 18 | Participação e contribuição | Preparação do ambiente de desenvolvimento, modelo de branches, especificação de commits, requisitos de PR, código de conduta, modelo de Issue | Escrever apenas “PRs são bem-vindos” |
| 19 | Direitos autorais e licença | Linha de direitos autorais, nome da licença, identificador SPDX, local do texto integral da licença | Ausência do titular dos direitos |
| 20 | Declaração de conformidade NOTICE | Resumo das dependências de terceiros, link relativo para o arquivo NOTICE | Substituir o NOTICE por esta seção |

## 1.1 As quatro perguntas da primeira tela e o texto em uma frase

A primeira tela do README deve responder a quatro perguntas, em ordem fixa:

1. o que o projeto faz;
2. qual problema o projeto resolve;
3. quais características o projeto tem;
4. o exemplo mínimo de hello world.

A pergunta 1 corresponde ao “posicionamento em uma frase”, que deve atender simultaneamente a três pontos: indicar o tipo de projeto, apresentar qualificadores precisos e poder ser repetido diretamente. Textos públicos de projetos maduros podem servir de referência:

| Projeto | Texto em uma frase | Análise da estrutura |
| --- | --- | --- |
| Angular | One framework. Mobile & desktop. | categoria + abrangência |
| React | A declarative, efficient, and flexible JavaScript library for building user interfaces. | três qualificadores + categoria + finalidade |
| Vue | A progressive, incrementally-adoptable JavaScript framework for building UI on the web. | duas características + categoria + finalidade |

Restrições de redação:

- não devem ser usados adjetivos sem informação, como “poderoso”, “excelente” ou “revolucionário”;
- deve ser indicada a palavra de categoria (biblioteca, framework, ferramenta, aplicação), para que o leitor classifique o projeto de imediato;
- os qualificadores de característica não devem ultrapassar três, evitando acúmulo;
- a versão em chinês deve ser limitada a 60 caracteres, e a versão em inglês, a 25 palavras.

A pergunta 3, “quais características”, deve divulgar também os cenários não aplicáveis. Exemplo de redação eficaz: indicar que determinado middleware de mensagens “suporta apenas QoS nível 0, não sendo aplicável a cenários que exigem nível 1”; a redação ineficaz consiste em listar apenas vantagens. A comparação de características deve basear-se em fatos verificáveis e não deve depreciar projetos semelhantes.

O exemplo de hello world da pergunta 4 deve permitir concluir a instalação e a execução em dois passos; projetos com etapas de instalação complexas deveriam oferecer imagem de contêiner ou ambiente de demonstração on-line, evitando que o leitor desista após ler o README.

## 2. Formato padrão da linha de direitos autorais

```text
Copyright © {{年份}} {{著作权人}}. Licensed under {{SPDX 标识符}}.
```

## Arquivos relacionados

- Os limites de conteúdo das seções estão em [matriz de documentação](./document-matrix.md)
- As regras de descrição do repositório e etiquetas de tópico estão na seção 5 da [especificação de nomes de projeto](./project-naming-specification.md)
- A consistência entre as versões em chinês e em inglês está na [especificação de multilinguismo](./multilingual-specification.md)
- O NOTICE referenciado pelo detalhamento de dependências está na [especificação de NOTICE](./notice-specification.md)
- O padrão de redação está na [especificação geral de redação](./general-writing-specification.md)
