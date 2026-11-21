# Especificação do modelo de manual de desenvolvimento

> Problema que este arquivo resolve: definir o esqueleto do manual de desenvolvimento de duas fases “redigir na nuvem, executar localmente”, o formato dos cartões de tarefa, o protocolo de transição e os portões de verificação, para que uma mesma ideia possa ser transcrita pela nuvem em cartões de tarefa sem ambiguidade e executada em regime de revezamento, parte a parte, pelo modelo de codificação local.

## 1. Posicionamento e fluxo de uso

1. Esta especificação destina-se ao cenário de divisão de trabalho “um modelo de raciocínio na nuvem + um modelo de codificação local”: a nuvem é responsável por transcrever ideias vagas em soluções explícitas, e o local, por executar a solução de forma determinística.
2. O fluxo de uso é fixo em quatro etapas, e a ordem não pode ser pulada:
   - Verificação prévia: examinar se a ideia contém premissas erradas, saltos lógicos ou informações faltantes; se as informações forem insuficientes, perguntar primeiro ao usuário; é proibido preencher lacunas por conjectura.
   - Redação na nuvem: varrer soluções de código aberto conforme a seção 9 e preencher o manual.
   - Revisão pelo usuário: foco na revisão dos comandos de aceitação, do registro de adoção e das zonas proibidas.
   - Execução local: injetar as seções e os registros de transição correspondentes por meio do índice legível por máquina e executar parte a parte.
3. No corpo do manual é proibido aparecerem palavras vagas como “etc.”, “relacionado”, “apropriado”, “na medida do possível” e “quando necessário”; cada ocorrência deve fornecer um valor preciso ou uma regra de decisão.

## 2. Esqueleto do manual

Cada manual de desenvolvimento contém fixamente as partes abaixo, sem alteração de ordem:

| Parte | Responsabilidade |
| --- | --- |
| Índice legível por máquina | Tabela de navegação de caminhos de seção, diretórios de código correspondentes, comandos de aceitação e marcações de fase |
| Registro de adoção | Tabela de registro da cadeia de suprimentos de código aberto, fonte única de verdade de todo o projeto (ver seção 11) |
| Constituição do projeto | Invariantes de todo o projeto, injetada em cada parte |
| Glossário | Termos com explicação em linguagem simples e correspondência com o código |
| Seções de módulo | Um capítulo por módulo, redigido conforme a estrutura da seção 4 |
| Seção de distribuição | Normas de build e de distribuição; as ações de publicação exigem confirmação do usuário |
| Seção de texto do site | Normas de texto voltadas ao usuário comum, não injetadas no modelo local |
| Registro de alterações | Data, seção, alteração e decisor |

## 3. Constituição do projeto

A constituição do projeto é o conjunto de invariantes injetado em cada parte executada localmente, com cinco itens fixos:

1. Stack tecnológico e versões: precisão até o número de versão.
2. Convenção de estrutura de diretórios: árvore de diretórios com uma frase de responsabilidade por diretório.
3. Norma de codificação: ajustada ao tipo de projeto, com a linha de base de carregamento modular sob demanda, código mínimo e mais direto, nenhuma funcionalidade não solicitada, comentários completos e conceitos técnicos explicados em linguagem simples; projetos de interface seguem as Apple HIG, a unidade de fonte é sempre px ou rem, e rpx é proibido.
4. Zonas proibidas globais: o que nunca pode ser feito, por exemplo não introduzir dependências fora do registro de adoção e não alterar arquivos de contrato.
5. Norma de idioma de saída: explicações, logs, progresso e mensagens de erro em chinês simplificado; código, comandos, caminhos de arquivo e termos próprios podem permanecer no original.

## 4. Estrutura da seção de módulo

Cada seção de módulo contém fixamente nove subseções, sem alteração de ordem:

| Subseção | Responsabilidade |
| --- | --- |
| Responsabilidade do módulo | 1 a 3 frases deixando claro o que faz e o que não faz |
| Soluções de código aberto das quais depende | Nome, finalidade e número no registro de adoção |
| Lista de arquivos | Caminho, ação (criar/modificar/somente leitura) e responsabilidade; total de no máximo 10 arquivos, acima disso dividir o capítulo |
| Contrato de interface | Assinaturas, rotas e campos de protocolo com precisão de tipo, com exemplos completos de entrada e saída |
| Dados e estado | O que armazenar, onde armazenar e em qual formato; conceitos técnicos explicados em linguagem simples |
| Relações de dependência | Três listas de arquivos: os que devem ser lidos antes, os que serão chamados e os que jamais serão alterados |
| Cartões de tarefa | As partes em que o módulo foi dividido, cada cartão executado de forma independente |
| Zona proibida do capítulo | O que é especialmente proibido neste módulo |
| Notas de design | Razões da escolha, soluções descartadas e distinção entre fato e conjectura; não injetadas no modelo local |

## 5. Formato do cartão de tarefa

Um cartão de tarefa equivale a uma sessão local e a um comando de aceitação, com os campos fixos abaixo:

| Campo | Requisito |
| --- | --- |
| Objetivo | Uma frase, verificável por máquina |
| Pré-condições | A parte anterior da qual depende e os arquivos já existem |
| Passos | Numerados, cada passo uma ação determinística, concluída de uma vez, sem interrupção nem perguntas adicionais |
| Comando de aceitação | Copiável e executável diretamente; ainda sem sistema de aceitação, o primeiro cartão deve construí-lo antes |
| Resultado esperado | Saída precisa, código de saída ou número de asserções |
| Tratamento de falha | Disposição item a item por erro típico; após 3 falhas consecutivas, parar obrigatoriamente e registrar no registro de transição |
| Requisitos de transição | Campos que devem obrigatoriamente ser escritos no registro de transição |

Restrições obrigatórias:

1. Um cartão que toque mais de 10 arquivos deve ser dividido; um capítulo com mais de 6 cartões deve ser dividido.
2. Todo cartão que envolva autoverificação de entrega deve listar explicitamente a limpeza de código redundante e os pontos de sincronização de README, NOTICE e LICENSE.
3. Ações que envolvam excluir ou sobrescrever arquivos param sempre e são registradas no campo block do registro de transição, aguardando confirmação do usuário.
4. Tarefa vaga demais para ter um comando de aceitação não pode ser registrada em cartão e deve ser marcada à parte como “requer decisão do usuário”.

## 6. Protocolo de transição PROGRESS

O arquivo de registro de transição PROGRESS.md é a única fonte de verdade entre uma parte e outra, com formato fixo:

| Campo | Requisito |
| --- | --- |
| done | Se o objetivo do cartão foi alcançado |
| files | Lista dos arquivos efetivamente alterados |
| decisions | Decisões do processo, no formato “escolheu A, porque B” |
| next | Número do próximo cartão e ponto de entrada, escritos até o caminho do arquivo e a função de entrada; é proibido escrever “continuar aprimorando” |
| block | Problemas não resolvidos; se não houver, deixar em branco |

1. Ao encerrar cada cartão, deve-se acrescentar uma entrada, sem alterar o formato.
2. Na execução local, apenas a entrada mais recente é injetada; as entradas históricas não são injetadas.
3. Retomada de ponto de interrupção: ao receber o comando “continuar”, ler primeiro a entrada mais recente para confirmar o ponto de interrupção e prosseguir a partir do ponto de entrada indicado em next; é proibido refazer passos concluídos de memória ou por conjectura.

## 7. Orçamento de injeção local

O harness monta o contexto de cada parte conforme a tabela abaixo, com orçamento total de no máximo 24K (75% da janela de trabalho de 32K):

| Item injetado | Orçamento |
| --- | --- |
| Constituição do projeto | 2 a 3K |
| Capítulo ao qual pertence o cartão de tarefa atual | 2 a 5K |
| Entrada mais recente do registro de transição | cerca de 0,5K |
| Esqueleto do prompt de transição | cerca de 0,3K |
| Código e saídas de ferramentas | saldo restante |

Não são injetados: a tabela completa do registro de adoção (apenas os itens envolvidos no cartão são injetados), as notas de design e a seção de texto do site.

## 8. Regras absolutas do prompt de transição

Ao iniciar cada parte, um início fixo é injetado, com seis regras absolutas:

1. Usar chinês simplificado em toda a saída; código, comandos, caminhos e termos próprios podem permanecer no original.
2. Fazer apenas o que está no cartão de tarefa, sem adicionar funcionalidades, configurações ou capacidades de extensão não solicitadas.
3. Não inventar nem fabricar; diante de uma assinatura de API incerta, declarar diretamente a incerteza; distinguir explicitamente fato de conjectura.
4. Em caso de falha do comando de aceitação, executar o tratamento de falha do cartão de tarefa; é proibido alterar os critérios de aceitação por conta própria.
5. Ações que envolvam excluir ou sobrescrever arquivos param sempre, aguardando confirmação do usuário.
6. Ao concluir, escrever o registro de transição estritamente conforme os requisitos de transição e, em seguida, encerrar.

## 9. Normas de preenchimento na nuvem

Antes de preencher o manual, o modelo da nuvem conclui duas verificações prévias e então preenche capítulo a capítulo:

1. Verificação de premissas: examinar premissas erradas, saltos lógicos e informações faltantes; se insuficientes, perguntar primeiro ao usuário.
2. Varredura de soluções de código aberto: pesquisar soluções prontas disponíveis no ecossistema de código aberto, varrer antes de preencher, usar soluções maduras em vez de reinventar a roda e registrar os resultados no registro de adoção.

Ao preencher, observar:

1. Eliminar toda palavra vaga, fornecendo em cada ocorrência um valor preciso ou uma regra de decisão.
2. Registrar as decisões de design nas notas de design, com razões da escolha e soluções descartadas, para revisão do usuário; não injetadas no modelo local.
3. Redigir as instruções ao modelo local partindo do princípio de que “ele não conhece o contexto do projeto”, escrevendo todas as premissas explicitamente.
4. Linha de base de conformidade: licença desconhecida marcada como “a confirmar”; soluções com copyleft forte recebem aviso das obrigações de obra derivada; código aberto modificado conserva os direitos autorais originais e a descrição das modificações; cada item adotado deve sincronizar README, README_EN, NOTICE e LICENSE, e a sincronização entra como passo explícito e conteúdo de aceitação do cartão de tarefa correspondente.
5. As referências às normas de formato de documento apontam para as especificações correspondentes deste repositório, sem copiar o texto normativo dentro do manual.

## 10. Estados de fase e janela de trabalho

Cada capítulo do índice legível por máquina traz uma marcação de fase, pela qual se ajusta a janela de trabalho local:

| Fase | Característica | Janela de trabalho |
| --- | --- | --- |
| Greenfield | Implementar conforme o contrato congelado | 16 a 24K |
| Crescimento | Funcionalidades entre módulos, faixa padrão | 32K |
| Manutenção | Refatoração e diagnóstico entre módulos | 48 a 64K, com paralelismo correspondentemente reduzido |

Capítulos em manutenção devem acrescentar um guia de diagnóstico com três colunas: sintoma, posições possíveis e comando de verificação.

## 11. Registro de adoção, distribuição e texto do site

1. Os campos da tabela do registro de adoção são fixos: nome, categoria, versão, finalidade, licença, titular dos direitos, endereço oficial, modificado, descrição da modificação, forma de declaração e estado de adoção; o estado de adoção tem três faixas: “adotável imediatamente”, “requer avaliação” e “indisponível por ora”.
2. A seção de distribuição cobre scripts de build, matriz de CI, checksum e modelo de variáveis de ambiente de assinatura; o comando de aceitação do cartão de distribuição é a verificação dos artefatos de build; as ações de publicação externa não passam pelo modelo local e são executadas após confirmação do usuário.
3. A seção de texto do site é voltada ao usuário comum: é proibido conter código, linha de comando, termos técnicos e palavras vazias; a estrutura é posicionamento da primeira dobra, dores, destaques, confiança, download, histórias de cenário e perguntas frequentes; o tom é sereno e contido.

## 12. Referência entre projetos e verificação

1. Quando o projeto-alvo referencia esta especificação, lê-se o texto integral por meio de `gitrule spec` e copia-se o esqueleto do manual como esqueleto inicial do manual dentro do projeto; esta especificação não é revisada junto com o projeto, e a evolução do manual interno se fecha no repositório do projeto.
2. Cartões de tarefa que produzam documentos acrescentam `gitrule check` ao comando de aceitação; projetos multilíngues acrescentam `gitrule xcheck`; após alteração do glossário, executar `gitrule termcheck`.
3. Violações documentais detectadas por `gitrule check` são de correção automática possível: pode-se primeiro executar `gitrule optimize` e reverificar; persistindo a falha, registrar no campo block do registro de transição.
4. As especificações do Gitrule tratam apenas de documentos e normas de repositório; a qualidade do código pertence aos testes e aos scripts de verificação de cada projeto, e um não substitui o outro.

## Arquivos relacionados

- Entrada de registro desta especificação: [índice geral](./README.md)
- Restrições de nível superior dos portões de aceitação desta especificação: [regras absolutas](./hard-rules.md)
- Definição de responsabilidade exclusiva do manual como documento entregável: [matriz de documentação](./document-matrix.md)
- Padrão de redação do corpo do manual: [especificação geral de redação](./general-writing-specification.md)
- Regras de sincronização multilíngue desta especificação: [especificação de multilinguismo](./multilingual-specification.md)
- Identificador estável e mapeamento de caminhos desta especificação: [especificação de metadados legíveis por máquina](./machine-readable-metadata-specification.md)
- Correspondência terminológica e convenções dos campos de modelo: [coleta de informações e modelos](./information-collection-and-templates.md)
