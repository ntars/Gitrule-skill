# Especificação de acessibilidade

> Problema que este arquivo resolve: definir os requisitos de acessibilidade da documentação do projeto, do README e da interface do usuário, tornando o conteúdo igualmente utilizável por leitores que usam leitores de tela, operação por teclado e diferentes condições visuais.

## 1. Escopo de aplicação

1. Acessibilidade da documentação: README, site de documentação, código de exemplo, tabelas e imagens.
2. Acessibilidade da interface: interface do usuário de aplicações e projetos Web.
3. Acessibilidade da linha de comando: texto de ajuda, mensagens de erro e formato de saída.

## 2. Acessibilidade da documentação

### 2.1 Imagens e mídia

1. Cada imagem deve fornecer texto `alt` descrevendo o conteúdo e a função da imagem; imagens decorativas usam `alt` vazio.
2. É proibido usar textos sem informação, como “imagem”, “captura de tela” ou “image”, como `alt`.
3. GIFs animados devem ter seu conteúdo explicado em texto próximo, evitando transmitir informação apenas pela animação.
4. Gráficos devem oferecer também descrição textual ou tabela de dados; é proibido distinguir séries de dados apenas por cor.

### 2.2 Títulos e estrutura

1. A hierarquia de títulos deve ser contínua, sem saltos de nível (ver [especificação de layout visual do README](./readme-visual-layout-specification.md)).
2. Todo o documento deve ter apenas um título de nível um.
3. As listas devem usar a sintaxe Markdown apropriada, garantindo que o leitor de tela as identifique como listas.
4. As tabelas devem ter linha de cabeçalho; é proibido usar tabelas sem cabeçalho para diagramar a página.

### 2.3 Links e texto

1. O texto do link deve explicar o destino por si só; é proibido usar “clique aqui” ou “mais”.
2. A cor não deve ser o único meio de transmitir informação; deve ser combinada com texto ou ícone.
3. Na mesclagem de chinês e idiomas estrangeiros, os espaços devem ser preservados, garantindo segmentação de palavras e leitura correta.
4. As abreviações devem ter sua forma completa apresentada na primeira ocorrência.

### 2.4 Código e tabelas

1. Os blocos de código devem indicar a linguagem, facilitando o reconhecimento por ferramentas assistivas (ver [especificação de layout visual do README](./readme-visual-layout-specification.md)).
2. O conteúdo das células de tabela deve ser conciso, evitando mesclagem entre linhas que dificulte a interpretação pelo leitor de tela.
3. Comandos longos devem ter forma de escrita em várias linhas, sem depender de rolagem horizontal.

## 3. Acessibilidade da interface

### 3.1 Operação por teclado

1. Todos os elementos interativos devem ser alcançáveis e operáveis por teclado.
2. A ordem de foco deve coincidir com a ordem visual e o estado de foco deve ser claramente visível.
3. Deve haver atalho para saltar conteúdo repetitivo (como ir ao conteúdo principal).

### 3.2 Semântica e rótulos

1. Usar marcações semânticas para expressar estrutura e papel, evitando simular controles com elementos sem semântica.
2. Os controles de formulário devem ter rótulos associados, com as mensagens de erro vinculadas ao campo correspondente.
3. Mudanças dinâmicas de estado devem ser comunicadas à tecnologia assistiva por meio de avisos de acessibilidade.

### 3.3 Condições visuais

1. O contraste entre texto e fundo deve atender aos requisitos de legibilidade; o contraste do corpo do texto não deve ser inferior a 4.5:1 e o de textos grandes, inferior a 3:1.
2. Deve haver suporte aos temas claro e escuro do sistema, e a troca de tema não deve alterar a estrutura da informação (ver [especificação de layout visual do README](./readme-visual-layout-specification.md)).
3. As animações devem oferecer opção de redução, evitando conteúdo de cintilação de alta frequência com reprodução automática.
4. Com o texto ampliado a 200%, o layout deve continuar utilizável, sem corte de conteúdo.

## 4. Acessibilidade da linha de comando

1. As mensagens de erro devem explicar a causa e a ação de correção viável; é proibido emitir apenas o código de erro.
2. A saída de `--help` deve ser claramente categorizada, listando parâmetros obrigatórios e valores padrão.
3. Deve haver suporte a variável de ambiente que desative a saída colorida, facilitando o uso de leitores de tela e o processamento de logs.
4. Os avisos interativos devem oferecer parâmetros equivalentes não interativos, com suporte a cenários de automação.

## 5. Lista de verificação

- [ ] Todas as imagens têm texto `alt` informativo e claro.
- [ ] A hierarquia de títulos é contínua e o documento tem um único título de nível um.
- [ ] O texto dos links é compreensível isoladamente.
- [ ] As tabelas têm cabeçalho e a cor não é o único veículo de informação.
- [ ] Os blocos de código indicam a linguagem.
- [ ] Os elementos de interface são operáveis por teclado e o foco é visível.
- [ ] O contraste atende ao mínimo exigido e os temas claro e escuro são legíveis.
- [ ] O texto de ajuda e as mensagens de erro orientam o próximo passo.

## 6. Práticas proibidas

1. É proibido transmitir informação crítica apenas por imagem, sem alternativa textual.
2. É proibido indicar estado ou erro apenas por cor.
3. É proibido usar texto de link sem significado.
4. É proibido remover o estilo de indicação de foco sem oferecer alternativa.

## Arquivos relacionados

- A diagramação da documentação está na [especificação de layout visual do README](./readme-visual-layout-specification.md)
- Os requisitos de acessibilidade dos selos estão na [especificação de selos](./badge-specification.md)
- Os padrões de escrita estão na [especificação de escrita geral](./general-writing-specification.md)
- A qualidade da documentação pertence à dimensão D12, ver [matriz de dimensões de auditoria](./review-dimension-matrix.md)
