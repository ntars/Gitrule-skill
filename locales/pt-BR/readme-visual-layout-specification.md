# Especificação de layout visual do README

> Problema que este arquivo resolve: definir a hierarquia de layout do README, a organização de parágrafos, as tabelas, os cenários de uso e a posição de capturas de tela e GIFs, de modo que a documentação alcance equilíbrio entre densidade informacional e atratividade visual.

Os dados “medidos” deste arquivo provêm da amostragem estatística realizada por este projeto sobre READMEs de projetos open source de destaque (amostra N=120); as práticas de referência derivam da análise da estrutura da primeira tela de diversos projetos com muitas estrelas.

## 1. Hierarquia de layout

### 1.1 Níveis de título

O README deve estabelecer uma hierarquia clara de títulos, observando as seguintes restrições:

1. Manter no texto apenas um título de primeiro nível (`#`), correspondente ao nome do projeto, na primeira linha do arquivo.
2. Os títulos de segundo nível (`##`) são as seções principais, em número preferencial de 6 a 12; a mediana medida é de 7.
3. Os títulos de terceiro nível (`###`) servem à subdivisão dentro de uma seção, usados apenas quando o conteúdo do título de segundo nível for longo.
4. Não deve haver salto de nível de título (por exemplo, de `#` diretamente para `###`).
5. O texto dos títulos deve ser conciso, empregando substantivos ou locuções substantivas, sem ponto final.

### 1.2 Ordem da estrutura da primeira tela

A primeira tela designa o conteúdo visível sem necessidade de rolagem, organizado na seguinte ordem:

1. logotipo ou banner do projeto centralizado (opcional);
2. título de primeiro nível (nome do projeto);
3. linha de selos (ver [especificação de selos](./badge-specification.md));
4. posicionamento em uma frase (indicando o que é o projeto, para quem se destina e qual problema resolve);
5. linha de links de navegação de seções (opcional, aplicável a READMEs longos);
6. resumo das funcionalidades ou características centrais.

Evidência de referência: `fd` e `ripgrep` apresentam a navegação de seções logo após o posicionamento; `next.js` e `rust-lang/rust` abrem com logotipo e banner centralizados; `vscode` insere a captura de tela do produto logo após o posicionamento.

### 1.3 Parágrafos e espaçamento

- Limitar cada parágrafo a 1–4 linhas, evitando blocos densos de texto.
- Deixar uma linha em branco entre parágrafos, garantindo respiro após a renderização.
- Antepor as conclusões principais e pospor as explicações.
- Manter um espaço entre caracteres chineses e caracteres latinos ou números; usar a pontuação de cada idioma conforme seu próprio contexto.

## 2. Especificação de uso de tabelas

### 2.1 Cenários de uso

As tabelas são adequadas a informações multidimensionais e comparáveis. Na medição, 36.7% da amostra usa tabelas, sendo o formato recomendado para explicação de configuração, matriz de compatibilidade e comparação de comandos. Os cenários aplicáveis incluem:

- explicação de itens de configuração (nome da chave, tipo, valor padrão, função);
- matriz de compatibilidade de plataforma / versão;
- comparação de comandos ou parâmetros;
- comparação de funcionalidades (este projeto e outras soluções);
- roteiro e estado.

### 2.2 Posição

A tabela deve vir imediatamente após o título de segundo nível a que pertence, precedida de uma frase introdutória que explique sua finalidade; havendo exceções após a tabela, complementar em novo parágrafo.

### 2.3 Requisitos de redação

| Requisito | Descrição |
| --- | --- |
| Controle de colunas | 3–6 colunas; acima de 6, considerar a divisão |
| Cabeçalho claro | Cada coluna deve ter um cabeçalho substantivo curto, evitando cabeçalhos vazios |
| Alinhamento consistente | O modo de alinhamento das tabelas deve ser uniforme no texto |
| Conteúdo conciso | Não escrever parágrafos longos nas células; quando necessário, expandir com notas de rodapé ou links |
| Sem células vazias | Onde não houver conteúdo, escrever “não se aplica” ou “nenhum” |

## 3. Especificação de uso de blocos de código

### 3.1 Cenários de uso

Os blocos de código servem a comandos, configurações, chamadas de API e saídas de exemplo. Na medição, 66.7% da amostra contém blocos de código, elemento indispensável na seção “Início rápido”, com mediana de 2.

### 3.2 Requisitos de redação

1. Todo bloco de código deve indicar a linguagem, por exemplo `bash`, `json`, `python`, `javascript`, para permitir destaque de sintaxe.
2. Os exemplos de comando devem apresentar o comando completo e executável, sem omitir etapas prévias.
3. Quando for necessário mostrar o resultado, criar outro bloco de código marcado como `text` e explicar a saída esperada no texto.
4. Deixar uma linha em branco antes e depois de cada bloco de código.
5. Limitar o conteúdo de cada bloco a 20 linhas; exemplos mais longos devem ser divididos em vários blocos ou movidos para o diretório `examples/`, com o respectivo link.
6. Quando se usar o prompt `$` em comandos interativos, ele deve ser uniforme em todo o texto.

Exemplo de formato:

```bash
npm install <package-name>
```

```text
✓ Installation complete
```

## 4. Especificação de uso de capturas de tela e GIFs

### 4.1 Cenários de uso e critérios de escolha

| Elemento | Cenário aplicável | Observações |
| --- | --- | --- |
| Captura de tela estática | Interface da aplicação, resultado de execução, gráficos | Uso medido de 63.3%, o mais frequente |
| GIF / imagem animada | Demonstração em linha de comando, fluxo interativo, comparação antes e depois | Arquivo volumoso, requer compressão e controle de duração |
| Logotipo / banner | Identificação de marca, primeira tela | Fornecer versões para tema claro e escuro |
| Diagrama esquemático | Arquitetura, fluxo, fluxo de dados | Deve ser atualizado em sincronia com a versão da documentação |

Na medição, 63.3% da amostra contém imagens. Evidência de referência: `fd` usa `doc/screencast.svg` como demonstração, `ripgrep` usa captura de tela dos resultados de busca, `vscode` usa captura de tela da execução do produto, e `rust` e `next.js` usam banner de logotipo com adaptação a temas claro e escuro.

### 4.2 Posição

1. Logotipo / banner: no topo do arquivo, centralizado.
2. Captura de tela do produto: após o posicionamento em uma frase e antes do “Início rápido”, para estabelecer percepção intuitiva.
3. GIF de demonstração: em seção própria de “Demonstração”, imediatamente após “Funcionalidades principais”.
4. Diagrama de arquitetura: na seção “Arquitetura” ou “Projeto”, ou movido para `docs/architecture.md` com link no README.

### 4.3 Requisitos de redação

- Toda imagem deve ter texto `alt` descrevendo o conteúdo da cena; não devem ser usados textos sem significado, como `image` ou `captura de tela`.
- As imagens devem usar caminhos relativos para recursos do repositório ou URLs absolutas estáveis; evitar links temporários com prazo de validade.
- Imagens que exigem adaptação ao tema devem usar HTML `<picture>` com `prefers-color-scheme`, fornecendo versões para tema claro e escuro.
- Controlar o volume das imagens: preferir WebP ou PNG otimizado para capturas de tela, e converter GIFs em vídeos curtos ou imagens animadas comprimidas.
- Adequação da largura da imagem: usar o atributo `width` ou um contêiner externo para limitar, evitando quebrar o layout da página.

## 5. Links e navegação

### 5.1 Navegação de seções

Quando o README ultrapassar 200 linhas, incluir na primeira tela uma linha de links de navegação apontando para as seções principais:

```markdown
[Instalação](#instalação) · [Início rápido](#início-rápido) · [Documentação](#documentação) · [Contribuição](#participação-e-contribuição)
```

### 5.2 Preferência por links relativos

Documentos, imagens e licença dentro do repositório devem usar sempre caminhos relativos, garantindo o funcionamento em forks e na leitura offline. Os links externos devem ser fontes autorizadas (documentação oficial, página do gerenciador de pacotes, página de CI).

## 6. Lista de verificação para estética e atratividade

1. A primeira tela deve ter logotipo ou título claro, comunicando o posicionamento do projeto em 3 segundos.
2. Os selos devem ter estilo uniforme, cores semânticas e quantidade moderada.
3. Deve haver um único título de primeiro nível, de 6 a 12 títulos de segundo nível e nenhum salto de nível.
4. Deve existir ao menos um exemplo de código copiável e executável.
5. Deve existir ao menos uma captura de tela ou demonstração que evidencie o valor do produto.
6. As tabelas devem ser usadas para informações comparativas, com número de colunas controlado e cabeçalhos claros.
7. Todas as imagens devem ter `alt` e todos os blocos de código, marcação de linguagem.
8. Documentos longos devem ter navegação de seções.
9. Imagens e selos devem ser legíveis em temas claro e escuro.

## Arquivos relacionados

- O estilo e a paleta dos selos estão na [especificação de selos](./badge-specification.md)
- A lista completa de seções está na [especificação de seções do README](./readme-sections-specification.md)
- A ênfase visual por tipo de projeto está no [guia de adaptação do README por categoria](./readme-category-adaptation-guide.md)
- O esqueleto de layout de aplicação direta está no [modelo padrão de README](./readme-standard-template.md)
- A amostra medida e o método estão no [relatório de pesquisa sobre modelos de README](./readme-template-research-report.md)
