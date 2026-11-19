# Especificação geral de redação

> Problema que este arquivo resolve: definir o registro, a exatidão, a consistência terminológica, as regras de formato e o conteúdo proibido de toda a documentação entregue, garantindo expressão precisa, sem ambiguidade e reproduzível.

## 1. Registro

1. Usar linguagem escrita, com frases declarativas e imperativas.
2. Não devem ser usadas expressões coloquiais, como “咱们”, “超简单”, “搞定”, “贼快”, “一键起飞”.
3. Não devem ser usados pontos de exclamação, reticências, abreviações de internet nem emoticons.
4. Não devem ser usadas perguntas retóricas nem perguntas hipotéticas como abertura de seção.

## 2. Exatidão

1. Cada frase deve expressar um sentido completo, sem depender de inferência pelo contexto.
2. Não devem ser usados referentes vagos como “ele”, “isto”, “relacionado”, “alguns”, “vários”; quando a referência for realmente necessária, usar o substantivo completo.
3. Datas, números de versão, caminhos, comandos, nomes de funções e nomes de chaves de configuração devem ser precisos e coerentes com a situação real do projeto.
4. Os comandos devem ser diretamente executáveis, incluindo a indicação necessária do diretório de trabalho atual.
5. Quando houver número de versão, deve ser escrita a semântica da restrição de versão, por exemplo `>=1.2.0 <2.0.0`.

## 3. Consistência terminológica

1. Na primeira ocorrência de um termo, apresentar sua definição, no formato “termo em chinês (English Term, abreviação)”.
2. Um mesmo conceito usa apenas uma expressão em todo o texto, e os termos das versões em chinês e em inglês correspondem um a um.
3. Deve ser mantida uma tabela de correspondência de termos chinês-inglês, no apêndice do README ou em arquivo independente, e as versões bilíngues devem compartilhar a mesma tabela (modelo em [coleta de informações e modelos](./information-collection-and-templates.md)).

## 4. Regras de formato

1. A hierarquia de títulos começa em `##` (`#` é reservado ao nome do projeto) e não deve haver salto de nível.
2. Cada título de segundo nível corresponde a uma seção definida pela [especificação de seções do README](./readme-sections-specification.md), e a ordem não deve ser alterada.
3. As tabelas devem ter cabeçalho e número de colunas uniforme; comandos, caminhos, código e nomes de chaves de configuração usam marcação de código em linha.
4. Os blocos de código devem indicar o identificador de linguagem, e comandos de várias linhas devem poder ser copiados e executados como um todo.
5. Links externos usam URL completa, sem encurtadores; links internos usam âncoras de caminho relativo.
6. Inserir espaço entre o chinês e o inglês e entre o chinês e os números; não misturar pontuação chinesa e inglesa.

## 5. Convenção de marcadores de posição

1. Os marcadores de posição formais nos modelos copiáveis são escritos uniformemente como `{{纯名}}`, por exemplo `{{仓库地址}}`; o nome não deve conter conectivos de escolha múltipla como “或” e “，”, nem ser escrito como uma frase explicativa.
2. Os marcadores de posição formais devem ser registrados na tabela de correspondência de marcadores de posição do modelo a que pertencem, e o registro inclui significado, exemplo e se é obrigatório.
3. O conteúdo entre chaves em linguagem natural, presente em exemplos de especificação ou dicas de preenchimento, serve apenas de exemplo, não é marcador de posição formal e não entra na tabela de correspondência; na geração da documentação final, deve ser integralmente substituído pelo conteúdo real.
4. Não devem ser usadas chaves aninhadas, crases nem um segundo marcador de posição como nome de marcador de posição.
5. Na tradução, o nome dos marcadores de posição deve coincidir literalmente com o idioma de origem; não deve ser localizado, transliterado nem parafraseado. Apenas o texto explicativo fora dos marcadores pode ser traduzido. Um marcador é a âncora da substituição de modelo: se seu nome for traduzido, a correspondência entre idiomas e a substituição em lote deixam de funcionar.

## 6. Lista de proibições

Não devem constar: números de desempenho não verificados, conclusões comparativas sem fonte, afirmações promissórias (como “garantia de compatibilidade com todos os ambientes” e “gratuito para sempre”), descrições depreciativas de projetos de terceiros nem conteúdo promocional alheio ao projeto.

## Arquivos relacionados

- Para a estrutura de seções, ver a [especificação de seções do README](./readme-sections-specification.md)
- Para a correspondência de termos bilíngues, ver a [especificação multilíngue](./multilingual-specification.md)
- A avaliação de qualidade G1 (coloquialismo e ambiguidade) está no [portão de qualidade](./quality-gate.md)
