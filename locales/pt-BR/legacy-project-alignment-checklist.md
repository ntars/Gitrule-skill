# Lista de verificação de alinhamento de projeto existente

> Problema que este arquivo resolve: ao aplicar este conjunto de especificações a um projeto já existente, oferecer uma lista de verificação item a item, o método de julgamento e o critério de aprovação, cobrindo seis etapas: metadados, nomenclatura de arquivos, estrutura de seções, sincronização bilíngue, links e push.

## 1. Escopo de aplicação

Esta lista atende a duas situações:

1. incluir pela primeira vez um repositório já existente na gestão deste conjunto de especificações;
2. após a atualização do conjunto de especificações, realizar verificação de regressão nos repositórios já alinhados.

A lista é executada na ordem “primeiro metadados, depois estrutura e por fim push”. Quando o grupo anterior não é aprovado, não se passa ao seguinte, para evitar reescritas em massa sobre uma base incorreta.

## 2. Itens de verificação

### 2.1 Metadados (correspondem à seção 5 da [especificação de nomes de projeto](./project-naming-specification.md))

| Nº | Item de verificação | Método de julgamento | Critério de aprovação |
| --- | --- | --- | --- |
| A1 | Nome do repositório conforme | Comparar com a fórmula de nomenclatura e as regras de conjunto de caracteres | Tudo em minúsculas, kebab-case, 2–25 caracteres, sem número de versão nem palavras informativas |
| A2 | Descrição no formato bilíngue combinado | Ler a área About do repositório ou `gh repo view --json description` | `idioma nacional \| inglês`, com um espaço de cada lado da barra vertical |
| A3 | Comprimento da descrição | Contar caracteres, separadamente em chinês e em inglês | No máximo 120 caracteres cada, total não superior a 350 caracteres |
| A4 | Quantidade e idioma dos tópicos | `gh repo view --json repositoryTopics` | Exatamente 20, todos em inglês, todos em minúsculas, termos separados por hífen |
| A5 | Cobertura dos tópicos | Conferir as cinco categorias: linguagem, domínio, formato, ecossistema e cenário | As cinco categorias estão cobertas, sem tópicos incompatíveis com a stack tecnológica |

Ordem de tratamento em caso de excesso: primeiro comprimir a versão em inglês, depois a versão em chinês; na compressão, remover primeiro os modificadores e as qualificações repetidas, e em seguida fundir expressões sinônimas.

### 2.2 Nomenclatura de arquivos (corresponde à [especificação multilíngue](./multilingual-specification.md))

| Nº | Item de verificação | Método de julgamento | Critério de aprovação |
| --- | --- | --- | --- |
| B1 | Nomenclatura do README principal | Listar o diretório | Em chinês, `README.md`; em inglês, `README_EN.md` |
| B2 | Nomenclatura dos demais idiomas | Listar o diretório | `README_<código do idioma em maiúsculas>.md`, como `README_JA.md` |
| B3 | Consistência de nomenclatura | Pesquisar nomes antigos em todo o repositório | Não restam nomenclaturas antigas como `README.en.md` e `README.ja.md` |
| B4 | Sincronização das referências | Pesquisar os nomes de arquivo antigos | Links de navegação, exemplos de árvore de diretórios e listas de permissão em scripts já foram atualizados |
| B5 | Links de troca de idioma | Abrir a primeira linha de cada versão de idioma | Cada versão de idioma permite, na primeira linha, alternar para todas as demais |

A renomeação de arquivos deve usar `git mv`, preservando o histórico do arquivo. Scripts do repositório (pré-verificação, empacotamento, validação de documentação) costumam usar strings de nome de arquivo como lista de permissão, e devem ser alterados em conjunto; caso contrário, a validação falha após o push.

### 2.3 Estrutura de seções (corresponde à [especificação de seções do README](./readme-sections-specification.md))

| Nº | Item de verificação | Método de julgamento | Critério de aprovação |
| --- | --- | --- | --- |
| C1 | Seções completas | Extrair os títulos de nível 2 e comparar com a lista de 20 capítulos | Os 20 capítulos existem, sem capítulo ausente |
| C2 | Nomenclatura das seções | Comparar o texto dos títulos item a item | Coerente com o vocabulário da especificação, sem variantes como “pontos principais” ou “detalhes de design e pequenos truques” |
| C3 | Ordem das seções | Comparar pela ordem de aparição | Coerente com a ordem da especificação |
| C4 | Seções adicionais | Verificar a existência de seções extras | Conteúdo extra é colocado como “apêndice” após os 20 capítulos, sem inserção na ordem do texto principal |
| C5 | Correspondência entre versões de idioma | Comparar a quantidade e a ordem dos títulos de nível 2 em chinês e em inglês | Correspondência um a um entre os dois idiomas |

Quando o texto principal apresentar nomes de seção divergentes da especificação, unificar conforme o vocabulário da especificação; se a seção contiver muito conteúdo já existente, priorizar a renomeação em vez de reescrever o texto.

### 2.4 Sincronização bilíngue (corresponde à [especificação multilíngue](./multilingual-specification.md))

| Nº | Item de verificação | Método de julgamento | Critério de aprovação |
| --- | --- | --- | --- |
| D1 | Versão idêntica | Pesquisar a string de versão | Os dois idiomas indicam a mesma versão e o mesmo estado |
| D2 | Números idênticos | Comparar número de funcionalidades, de testes e de plataformas | O mesmo indicador tem o mesmo valor nas duas versões |
| D3 | Links idênticos | Comparar o conjunto de links relativos | As duas versões apontam para o mesmo conjunto de arquivos |
| D4 | Terminologia idêntica | Verificar por amostragem os termos técnicos | O mesmo conceito usa a mesma tradução nas duas versões |
| D5 | Estrutura idêntica | Comparar a quantidade de tabelas e de listas | A seção tem a mesma quantidade de tabelas e de listas |

Após qualquer versão alterar conteúdo factual, a outra versão deve ser atualizada no mesmo commit; não se admite tradução complementar em commit separado.

### 2.5 Links e conteúdo (correspondem à [especificação geral de redação](./general-writing-specification.md))

| Nº | Item de verificação | Método de julgamento | Critério de aprovação |
| --- | --- | --- | --- |
| E1 | Links relativos acessíveis | Resolver um a um e verificar a existência do arquivo | Número de links quebrados igual a 0 |
| E2 | Identificador de linguagem dos blocos de código | Pesquisar as cercas | Todos identificados com linguagem, sem cerca nua |
| E3 | Número de colunas das tabelas | Conferir linha a linha a linha separadora e as linhas de dados | Número de colunas consistente |
| E4 | Expressões proibidas | Pesquisar coloquialismos, pontos de exclamação, reticências e emojis | Nenhuma ocorrência; citações de texto original devem vir entre aspas com indicação da fonte |
| E5 | Dados não verificados | Pesquisar números de desempenho | Todo número tem ambiente e método de teste |
| E6 | Afirmações promocionais | Pesquisar termos como “garantir”, “permanente” e “definitivo” | Qualificadores técnicos podem permanecer; afirmações promocionais externas devem ser removidas |

### 2.6 Arquivos da comunidade e push (correspondem à [matriz de documentação](./document-matrix.md) e à [especificação de push e publicação](./push-and-release-specification.md))

| Nº | Item de verificação | Método de julgamento | Critério de aprovação |
| --- | --- | --- | --- |
| F1 | Arquivos obrigatórios presentes | Listar o diretório | `LICENSE`, `NOTICE`, `CONTRIBUTING.md` e `SECURITY.md` presentes |
| F2 | Licença coerente com o NOTICE | Comparar a tabela de roteamento por camadas | A licença por diretório é coerente com a declaração do NOTICE |
| F3 | Regras de ignorar | Pesquisar o `.gitignore` | Artefatos de compilação, diretórios de dependências, `.DS_Store` e `.workbuddy/` estão ignorados |
| F4 | Mensagem de commit | Consultar `git log` | Em conformidade com `<type>(<scope>): <subject>` |
| F5 | Remoto coerente | Comparar o `HEAD` local com `origin/main` | Ambos idênticos e área de trabalho limpa |

## 3. Verificações adicionais para repositórios multilíngues

Quando o repositório tem três ou mais versões de idioma, acrescentar três itens às verificações acima:

1. **Conferência dos títulos de seção idioma a idioma**: os títulos dos 20 capítulos de cada idioma devem ser coerentes com o significado da referência em chinês ou em inglês, sem capítulo ausente em qualquer idioma;
2. **Número de linhas das tabelas consistente**: listas de projetos, tabelas de status e tabelas de parâmetros têm o mesmo número de linhas em todas as versões de idioma;
3. **Sincronização do glossário**: a tabela de correspondência de termos fica em um arquivo independente compartilhado pelos dois idiomas, e todas as versões de idioma referenciam o mesmo arquivo.

## 4. Erros comuns e tratamento

| Erro | Sintoma | Tratamento |
| --- | --- | --- |
| Julgar mal os numerais chineses ao renumerar capítulos em lote | “十、” é reconhecido como “二十、” e o capítulo 10 é sobrescrito com o título do capítulo 20 | Substituir por pares explícitos “string antiga → string nova”, verificando cada ocorrência antes de gravar |
| Alterar apenas o caminho do link sem alterar o texto exibido | O link funciona, mas o texto ainda mostra o nome antigo da seção | Pesquisar o nome antigo da seção em todo o texto e atualizar caminho e texto exibido ao mesmo tempo |
| Renomear arquivos sem sincronizar os scripts | A documentação local está correta, mas o script de validação falha após o push | Pesquisar todas as strings de nome de arquivo no repositório, incluindo scripts, configurações e exemplos de documentação |
| Alterar apenas um lado do conteúdo bilíngue | As duas versões divergem em fatos | Tomar o estado real do repositório como referência, alterar primeiro a versão principal e depois a outra no mesmo commit |
| Página de índice não sincronizada | O novo arquivo não está no índice e é considerado órfão | Após criar um arquivo, atualizar imediatamente a contagem e a entrada do índice e revisar a soma das contagens por domínio |
| Descrição do repositório divergente do texto principal | A área About menciona sete projetos e o texto menciona nove | Atualizar a descrição conforme a lista do texto principal e registrar isso na mensagem de commit |

## 5. Modelo de registro de aceitação

```text
仓库：{{仓库名}}
检查日期：{{日期}}
规范版本：{{版本或提交号}}

元数据：A1 {{通过/不通过}} A2 {{通过/不通过}} A3 {{通过/不通过}} A4 {{通过/不通过}} A5 {{通过/不通过}}
文件命名：B1 {{ }} B2 {{ }} B3 {{ }} B4 {{ }} B5 {{ }}
章节结构：C1 {{ }} C2 {{ }} C3 {{ }} C4 {{ }} C5 {{ }}
双语同步：D1 {{ }} D2 {{ }} D3 {{ }} D4 {{ }} D5 {{ }}
链接与内容：E1 {{ }} E2 {{ }} E3 {{ }} E4 {{ }} E5 {{ }} E6 {{ }}
社区与推送：F1 {{ }} F2 {{ }} F3 {{ }} F4 {{ }} F5 {{ }}

未通过项与处置：{{逐条列出}}
放行结论：{{通过 / 有条件通过 / 阻断}}
```

## 6. Definição dos campos

| Campo | Significado | Valores |
| --- | --- | --- |
| Nome do repositório | Nome completo do repositório verificado | `proprietário/repositório` |
| Versão da especificação | Estado do conjunto de especificações em que se baseia esta verificação | Número do commit ou da versão |
| Aprovado | O item atende ao critério de aprovação | Booleano |
| Conclusão de liberação | Tratamento do resultado da verificação | Aprovado / Aprovado com condições / Bloqueado |

## Arquivos relacionados

- Nomenclatura e metadados do repositório, ver a [especificação de nomes de projeto](./project-naming-specification.md)
- Lista de capítulos, ver a [especificação de seções do README](./readme-sections-specification.md)
- Regras bilíngues, ver a [especificação multilíngue](./multilingual-specification.md)
- Redação e expressões proibidas, ver a [especificação geral de redação](./general-writing-specification.md)
- Ações de push, ver a [especificação de push e publicação](./push-and-release-specification.md)
