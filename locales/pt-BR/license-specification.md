# Especificação de LICENSE

> Problema que este arquivo resolve: definir a marcação SPDX da licença do projeto, os requisitos do texto completo de LICENSE, a posição da linha de copyright, o mecanismo de detecção do GitHub, a disposição de arquivos em caso de licenças em camadas e o processo de confirmação, bem como a regra de não escrever nada sem confirmação.

## 1. Regras básicas

1. A licença do projeto deve ser declarada explicitamente no README por meio de um identificador SPDX, com o arquivo LICENSE correspondente fornecido.
2. O arquivo LICENSE deve conter o texto oficial integral em inglês da licença, sem supressão ou alteração de cláusulas. Reformular, reordenar parágrafos ou recompor em Markdown faz falhar a detecção automática.
3. A linha de copyright é colocada no início do arquivo ou na seção 19 do README; para o formato, ver a [especificação de seções do README](./readme-sections-specification.md).

## 2. Mecanismo de detecção do GitHub

O GitHub determina a licença de um repositório com a ferramenta de código aberto licensee. O resultado condiciona o selo da página do repositório, o campo `license` da API e o fato de uma busca pela palavra-chave `license` encontrar ou não o repositório. As regras são:

1. Apenas dois locais são examinados: a raiz do projeto e um diretório `LICENSES/` de primeiro nível. Arquivos com o mesmo nome dentro de `locales/`, `docs/` ou outros subdiretórios não participam.
2. Na raiz, os arquivos são pontuados pelo nome, e a pontuação mais alta vence: `LICENSE` vale 1.00, `LICENSE.md` 0.95, `COPYING` 0.90, as formas com sufixo como `LICENSE-MIT` 0.70.
3. Dentro de um diretório `LICENSES/` de primeiro nível, um nome de arquivo no formato de identificador SPDX com extensão `.txt`, `.md`, `.markdown` ou `.html` vale 1.00; qualquer outro vale 0.00.
4. O conteúdo deve corresponder estreitamente ao texto oficial integral da licença. Um arquivo contendo apenas uma menção do tipo “este projeto usa a licença X” não será detectado, e o resultado que produziria seria um valor não padrão.
5. Quando várias licenças distintas são detectadas, o resultado no nível do projeto pode não retornar uma licença concreta, e a página do repositório exibe `View license` ou `Other`.
6. Declarações em linguagem natural no README não participam. Escrever “este projeto tem licença MIT” não faz com que seja detectado como MIT.

Portanto: **a declaração no README e o arquivo LICENSE são dois mecanismos independentes, e ambos são necessários.** Além disso, quando há vários arquivos de licença na raiz, qual será finalmente reportado depende tanto da pontuação do nome quanto da correspondência do conteúdo, e não é previsível; nas medições, os repositórios com licença dupla reportaram apenas uma das duas.

## 3. Disposição de arquivos em caso de licenças em camadas

Licenças em camadas significam que partes diferentes de um repositório seguem licenças diferentes, por exemplo código sob MIT e documentação sob CC BY 4.0. A disposição é decidida nesta ordem:

| Opção | O que vai na raiz | Resultado da detecção | Condição de uso |
| --- | --- | --- | --- |
| Camada única (padrão) | Um único `LICENSE` | Detecção estável dessa licença | Todas as camadas usam a mesma licença, ou a diferença não altera as obrigações dos usuários |
| Camadas com explicação | `LICENSE` traz a licença principal, mais um `LICENSING.md` | Detecção estável da licença do `LICENSE` da raiz | É preciso estratificar e o selo deve permanecer inequívoco |
| Camadas com REUSE | `LICENSES/` de primeiro nível contém cada texto integral | Pode degradar para um valor não padrão | Somente se a parte a jusante exigir explicitamente conformidade REUSE |

Trade-offs:

1. Não coloque vários arquivos de licença na raiz. Nas medições, cada repositório com licença dupla reportou apenas uma de suas duas licenças; a outra ficou invisível na página do repositório e na API, o que equivale a declarar publicamente apenas uma licença.
2. A disposição REUSE entra em conflito com a clareza do selo: várias licenças em `LICENSES/` são lidas como várias licenças, o que compra um `reuse lint` verde ao custo de um resultado de detecção ambíguo. Os dois não podem ser plenamente satisfeitos ao mesmo tempo; o projeto precisa escolher.
3. Com a opção “camadas com explicação”, o nome `LICENSING.md` não corresponde ao padrão `LICENSE` nem ao padrão `COPYING`, portanto não é confundido com um arquivo de licença e não afeta a detecção do `LICENSE` da raiz.
4. Qualquer que seja a disposição escolhida, a seção 19 do README deve informar a expressão SPDX (por exemplo `MIT AND CC-BY-4.0`) e o escopo de cada camada. É o único lugar onde a informação sobrevive no nível da leitura humana.

## 4. Decisão de estratificação e processo de confirmação

Licenças em camadas têm alcance jurídico. Antes de escrever ou otimizar, confirme rodada após rodada; não invente nada.

1. Não introduza estratificação por iniciativa própria. Quando o usuário não a tiver pedido explicitamente, trate o projeto como de camada única e registre no relatório: “Se a estratificação for necessária, as opções candidatas e suas diferenças são as seguintes”.
2. Toda proposta de estratificação deve expor seu fundamento: o que cada camada cobre de fato, as licenças candidatas e a diferença de suas obrigações, o efeito sobre os usuários a jusante e como o resultado da detecção mudaria.
3. Confirme ao menos duas vezes antes de escrever: primeiro a combinação (qual licença para qual camada), depois a disposição de arquivos (qual licença vai no arquivo da raiz e se `LICENSES/` será criado).
4. Confirme novamente antes do push. Depois de gerar os arquivos, informe explicitamente “Os arquivos foram gerados; revise e confirme você mesmo” e nunca faça commit ou push no lugar do usuário.
5. Opções não confirmadas vão apenas para um relatório ou arquivo temporário; não devem ser gravadas como `LICENSE`, `LICENSES/` ou `LICENSING.md`.
6. Quando uma parte não puder ser atribuída a nenhuma camada, marque “【pendente de confirmação: atribuição de camada】” e liste os arquivos duvidosos; não classifique por padrão.

## 5. Requisitos da isenção de responsabilidade

Textos de licença têm eficácia jurídica. Modelos e ferramentas fornecem apenas regras de decisão e disposição de arquivos, e não constituem aconselhamento jurídico.

1. A seção 19 do README ou o arquivo `LICENSING.md` deve conter uma isenção de responsabilidade informando que a escolha da licença é confirmada pelo titular do projeto.
2. A isenção de responsabilidade deve coincidir com a do NOTICE; não pode existir em um lugar e faltar no outro.
3. Não afirme que “a revisão de conformidade foi concluída”. Informe apenas que “a disposição de arquivos e a marcação SPDX foram verificadas conforme as regras quanto à completude”.
4. A eficácia jurídica das licenças em camadas segue o texto integral de cada licença. O texto descritivo dentro do repositório é apenas um índice e não altera as cláusulas.

## Arquivos relacionados

- A ausência de LICENSE bloqueia o push e constitui a regra absoluta H2; ver [regras absolutas](./hard-rules.md)
- Para a avaliação de compatibilidade de licenças de dependências, ver a [especificação de conformidade de código aberto](./open-source-compliance-specification.md)
- Para a declaração de terceiros em arquivo independente, ver a [especificação de NOTICE](./notice-specification.md)
- A exatidão da licença pertence aos portões G7/G8; ver [portão de qualidade](./quality-gate.md)
