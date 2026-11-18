# Guia de adaptação do README por categoria

> Problema que este arquivo resolve: apresentar, para tipos distintos de projeto — biblioteca, aplicação, ferramenta de linha de comando, framework e coleção de recursos —, recomendações diferenciadas sobre seleção de seções do README, ênfase visual e configuração de selos, além de explicar como cada tipo de elemento eleva a estética e o poder de atração.

O modelo genérico serve a todos os projetos, mas leitores de tipos diferentes têm pontos de interesse distintos. Este arquivo apresenta ajustes orientados ao tipo, sobre a base das especificações gerais. O leitor deve tomar o [modelo padrão de README](./readme-standard-template.md) como base e recortá-lo conforme o tipo correspondente neste arquivo.

## 1. Visão geral dos tipos

| Tipo | Primeira pergunta do leitor | Foco da primeira tela | Seções obrigatórias | Seções dispensáveis |
| --- | --- | --- | --- | --- |
| Biblioteca / SDK | Forma de instalação e uso da API | Versão e licença | Instalação, início rápido, API, compatibilidade | Implantação, capturas de tela |
| Aplicação | Aparência da aplicação e funcionalidades centrais | Capturas de tela e funcionalidades | Funcionalidades, capturas de tela, instalação, início rápido | Referência de API |
| Ferramenta de linha de comando | Uso dos comandos e desempenho | Exemplos de comando e demonstração | Instalação, uso, tabela comparativa de comandos, demonstração | Arquitetura, configuração (quando escassa) |
| Framework | Ecossistema e custo de aprendizado | Entrada da documentação e exemplos | Posicionamento, início rápido, documentação, comunidade | Detalhes de desempenho (podem ser externalizados) |
| Coleção de recursos | O que é reunido e como pesquisar | Categorias do sumário e navegação | Sumário, categorias, guia de contribuição | Instalação, API |

## 2. Biblioteca / SDK

Representantes típicos: clientes HTTP como o axios, bibliotecas de funções utilitárias, SDKs de cliente.

### 2.1 Seleção de seções

- Antepor “posicionamento em uma frase + versão + licença”, para que o leitor avalie a compatibilidade com base nisso.
- Colocar “Instalação” no início, com o comando do gerenciador de pacotes (npm, pip, cargo etc.).
- “Início rápido” deve ser um exemplo completo e executável de forma independente.
- Detalhar a “Referência de API” no README principal ou vincular a `docs/api.md`; quando houver muitos itens de API, o README deve conter apenas um resumo + link.
- “Compatibilidade” deve indicar as versões de linguagem, os ambientes de execução e as plataformas suportados.

### 2.2 Ênfase visual

- Foco dos selos: versão, estado da build, licença, número de downloads, tamanho do pacote.
- Uso comedido de imagens; em geral não são necessárias capturas de tela; um logotipo pequeno pode estabelecer identificação.
- Apresentar os parâmetros da API em tabela, para melhorar a legibilidade.

### 2.3 Pontos para elevar a estética

1. Posicionar os selos de versão e licença no topo, estabelecendo credibilidade imediatamente.
2. Colocar o bloco de código do início rápido próximo da primeira tela, reduzindo a barreira de experimentação.
3. Padronizar a largura das colunas e a coluna de valor padrão nas tabelas de API, reduzindo a carga cognitiva.

## 3. Aplicação

Representantes típicos: editores, ferramentas de desktop, produtos voltados ao usuário final.

### 3.1 Seleção de seções

- A primeira tela deve conter captura de tela do produto ou imagem de execução, mostrando o valor antes de explicar a implementação.
- “Funcionalidades principais” deve ser organizada por cenário de uso do usuário, e não por módulo técnico.
- “Instalação” deve cobrir os pacotes de instalação ou os pontos de download de cada plataforma.
- “Início rápido” deve apresentar o caminho mais curto de entrada.
- As instruções de compilação a partir do código-fonte podem ser externalizadas para `CONTRIBUTING.md`.

### 3.2 Ênfase visual

- Foco dos selos: versão, estado da build, licença, número de downloads.
- A captura de tela, posicionada após o posicionamento, é o elemento central da primeira tela.
- A lista de funcionalidades deve ser acompanhada de ícones ou capturas curtas, melhorando a eficiência de leitura por varredura.

### 3.3 Pontos para elevar a estética

1. Apresentar capturas de tela de alta qualidade centralizadas, com adaptação automática a temas claros e escuros.
2. Usar frases curtas + ícones nos itens de funcionalidade, evitando descrições longas.
3. Tornar o ponto de download bem visível, com links em formato de botão.

## 4. Ferramenta de linha de comando

Representantes típicos: ferramentas de terminal como fd e ripgrep.

### 4.1 Seleção de seções

- Após o “posicionamento em uma frase”, incluir imediatamente a navegação de seções, para facilitar o salto.
- “Instalação” deve listar os principais gerenciadores de pacotes e os binários por plataforma.
- “Uso” deve ser orientado a tarefas, com exemplos dos comandos mais frequentes.
- A “tabela comparativa de comandos” ou a “comparação com ferramentas semelhantes” atende a uma demanda recorrente.
- A “Demonstração” deve usar GIF ou gravação de terminal para mostrar o efeito real.
- Os dados de desempenho devem indicar o ambiente e o método de teste.

### 4.2 Ênfase visual

- Foco dos selos: versão, estado da build, plataformas suportadas, licença.
- O GIF de demonstração é o ativo visual central, mostrando velocidade e experiência de uso.
- Usar blocos de código com marcação de linguagem para os comandos e blocos `text` para as saídas.

### 4.3 Pontos para elevar a estética

1. Posicionar os exemplos de comando no topo, para que o leitor possa copiá-los sem rolar a página.
2. O GIF de demonstração mostra o efeito real do terminal, reforçando a impressão de “rapidez”.
3. Colocar os links de idioma de vários níveis (como versões em chinês e em coreano) próximos da linha de selos.

## 5. Framework

Representantes típicos: frameworks full stack como o next.js.

### 5.1 Seleção de seções

- A primeira tela deve enfatizar o posicionamento, a escala do ecossistema e a porta de entrada para o aprendizado.
- A entrada de “Documentação” deve ser bem visível, geralmente apontando para um site de documentação independente.
- “Comunidade” deve indicar a área de discussão, os canais de mensagem instantânea e o código de conduta.
- “Início rápido” deve apresentar o comando mínimo de criação do projeto.
- Conteúdos aprofundados (arquitetura, API) devem ser externalizados, sem desenvolvimento no README.

### 5.2 Ênfase visual

- Foco dos selos: versão, estado da build, licença, canais da comunidade.
- Combinar o logotipo da marca com selos no estilo `for-the-badge`, reforçando a primeira tela.
- Capturas de tela de Showcase podem ser usadas para apresentar casos do ecossistema.

### 5.3 Pontos para elevar a estética

1. Logotipo centralizado + selos grandes de estilo uniforme, formando uma primeira tela com identidade de marca.
2. Apresentar as entradas de documentação e comunidade como blocos de navegação bem visíveis.
3. Entradas para iniciantes, como as Good First Issues, reduzem a barreira de contribuição.

## 6. Coleção de recursos

Representantes típicos: listas da série awesome.

### 6.1 Seleção de seções

- Abrir a primeira tela com logotipo e informações de patrocínio é uma prática comum.
- Organizar o sumário por categorias temáticas, oferecendo navegação clara.
- O “guia de contribuição” deve indicar os critérios de inclusão e o formato de envio.
- As seções de instalação, API e implantação não são necessárias.

### 6.2 Ênfase visual

- A quantidade de selos pode ser flexibilizada, mas o estilo deve ser uniforme.
- A categorização do sumário deve usar títulos de segundo nível + listas, com uma breve descrição em cada item.
- Os logotipos dos patrocinadores devem ser organizados em tabela ou grade, mantendo o alinhamento.

### 6.3 Pontos para elevar a estética

1. Estrutura de sumário clara, com níveis de título de categoria consistentes.
2. Cada item deve ter uma descrição em uma frase, evitando apenas links.
3. As áreas de patrocínio e agradecimento devem ser alinhadas e organizadas, sem prejudicar a leitura do corpo.

## 7. Princípios gerais entre tipos

1. **Leitor em primeiro lugar**: a primeira tela deve responder às perguntas mais relevantes para o leitor; a diferença de tipo afeta apenas a ordem, não a integralidade da informação.
2. **Estilo uniforme**: selos, títulos e blocos de código do mesmo projeto devem ter estilo consistente.
3. **Exemplos copiáveis**: todo tipo deve oferecer ao menos um exemplo diretamente executável.
4. **Links externos**: conteúdos aprofundados que excedem a responsabilidade da primeira tela devem ser externalizados para documentação independente.
5. **Sincronização contínua**: capturas de tela, selos de versão e listas de funcionalidades devem ser atualizados com a versão, evitando que informações desatualizadas prejudiquem a credibilidade.

## Arquivos relacionados

- A lista geral de seções está na [especificação de seções do README](./readme-sections-specification.md)
- A especificação de elementos visuais está na [especificação de layout visual do README](./readme-visual-layout-specification.md)
- A configuração de selos está na [especificação de selos](./badge-specification.md)
- O modelo genérico está no [modelo padrão de README](./readme-standard-template.md)
- A evidência da distribuição por tipo está no [relatório de pesquisa sobre modelos de README](./readme-template-research-report.md)
