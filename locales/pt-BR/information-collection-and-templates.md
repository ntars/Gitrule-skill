# Coleta de informações e modelos

> Problema que este arquivo resolve: definir os campos de informação do projeto que devem ser coletados antes da redação da documentação, as regras de marcação de informações não confirmadas, e oferecer um índice de marcadores de posição, um modelo de correspondência terminológica, um modelo de inventário de dependências e um texto de coleta de informações do projeto pronto para ser copiado.

## 1. Campos obrigatórios (a ausência bloqueia)

| Campo | Descrição | Seções afetadas |
| --- | --- | --- |
| Nome do projeto | Nome do repositório e nome de exibição; quando divergirem, a divergência deve ser explicada | Documento inteiro |
| Posicionamento em uma frase | No máximo 60 caracteres, explicando o que é o projeto e qual problema resolve, para quem | Seção 1 |
| Descrição do repositório (idioma nacional e inglês) | Cada idioma com no máximo 120 caracteres, explicando respectivamente o tipo de projeto e a finalidade central | Seção 1 |
| Tags de tópico | Preencher 20 palavras em inglês minúsculas, unidas por `-`; uso misto de maiúsculas e minúsculas ou termos não ingleses são considerados ausência do item | Seção 1 |
| Contexto do projeto | Motivo da iniciação e deficiências das soluções existentes | Seção 2 |
| Lista de funcionalidades centrais | Agrupadas por módulo, incluindo comportamentos perceptíveis ao usuário | Seção 3 |
| Stack tecnológico | Linguagem, framework e restrições de versão do ambiente de execução | Seção 6 |
| Inventário de dependências | Nome, versão, licença, titular dos direitos e endereço de origem | Seção 6, NOTICE |
| Tipo de licença | Licença do próprio projeto, que deve ser um identificador SPDX | Seção 19 |
| Titular dos direitos autorais | Nome da pessoa física ou razão social da organização, e o ano | Seção 19, NOTICE |
| Forma de instalação e execução | Requisitos de ambiente, comandos e resultado esperado | Seções 7 e 8 |

## 2. Campos opcionais

Lista de itens de configuração, definição de API, estrutura de diretórios, dados de teste de desempenho, matriz de compatibilidade, problemas conhecidos, registro de atualizações, roteiro, fluxo de contribuição, política de segurança, capturas de tela e endereço de demonstração, origem de materiais externos.

## 3. Instruções de preenchimento dos campos e exemplos

| Campo | Instruções de preenchimento | Exemplo |
| --- | --- | --- |
| Nome do projeto | O nome do repositório usa letras minúsculas, números e `-`; o nome de exibição pode usar a grafia da marca; quando divergirem, indicar o motivo | Nome do repositório `markdown-lint-cli`, nome de exibição `Markdown Lint CLI` |
| Posicionamento em uma frase | Contém a palavra de categoria e um qualificador, sem acúmulo de adjetivos, com no máximo 60 caracteres | `Ferramenta de linha de comando para verificação de especificações Markdown destinada a equipes de documentação técnica` |
| Descrição do repositório (idioma nacional e inglês) | Idioma nacional e inglês formam frases independentes, ambas com no máximo 120 caracteres, sem substituir a descrição por um slogan | `Português: ferramenta de linha de comando para verificar a estrutura de documentos Markdown` / `English: A CLI tool for checking Markdown document structure` |
| Tags de tópico | Todas em inglês minúsculo, palavras unidas por `-`, total de 20, cobrindo linguagem, formato, finalidade, ecossistema e cenário | `go cli markdown linter developer-tools` |
| Stack tecnológico | Indicar a linguagem principal, o framework e as restrições de versão do ambiente de execução; não escrever “versão mais recente” | `Go >= 1.22；Cobra v1.8.x` |
| Inventário de dependências | Cada item contém versão, licença, titular dos direitos e endereço oficial; origem desconhecida deve ser marcada como item não confirmado | Ver o modelo de tabela de inventário de dependências do apêndice C |
| Tipo de licença | Usar identificador SPDX, sem expressões vagas como “código aberto” ou “uso livre” | `MIT` |
| Forma de instalação e execução | Informar o diretório de trabalho atual, o comando completo e a saída esperada verificável | No diretório raiz do repositório, executar `go install ./cmd/mdlint` e obter a versão como saída |
| Itens não confirmados | Usar a marcação fixa, indicando o conteúdo ausente e o responsável pelo complemento, sem substituir por “provisório” | `【Pendente: tipo de licença da dependência foo, responsável: Zhang San】` |

## 4. Regras de marcação de informações não confirmadas

1. Formato uniforme: `【Pendente: o que falta especificamente】`; é proibido substituir por expressões vagas como “provisório”, “aproximadamente” ou “possivelmente”.
2. Local da marcação: uma ocorrência no ponto correspondente do texto e outra no “Resumo de itens pendentes” ao final do documento.
3. Itens não confirmados relacionados a licença, direitos autorais ou origem de dependências devem ser marcados explicitamente no NOTICE, sem omitir o item inteiro.
4. O resumo de itens pendentes deve conter número, campo, conteúdo ausente, responsável pelo complemento e prazo previsto para conclusão; itens sem responsável ou sem prazo não devem entrar na fase 0 (ver [fluxo de execução](./execution-process.md)).

## 5. Apêndice A · Índice de marcadores de posição

`{{项目名称}}`, `{{一句话定位}}`, `{{当前版本}}`, `{{维护状态}}`, `{{许可证 SPDX}}`, `{{著作权人}}`, `{{年份}}`, `{{分支名}}`, `{{仓库地址}}`, `{{最低运行时版本}}`

Regras de uso:

1. Este índice lista apenas os campos básicos da fase de coleta; a totalidade dos marcadores do README e suas descrições seguem a tabela de correspondência de marcadores do [modelo padrão de README](./readme-standard-template.md).
2. Os marcadores formais devem ser escritos uniformemente como `{{纯名}}`, sem aninhar texto explicativo, acentos graves ou um segundo marcador dentro das chaves; o conteúdo em chaves em linguagem natural nos exemplos da especificação não é considerado marcador formal.
3. Os campos em linguagem natural da tabela de coleta não usam marcadores diretamente; ao gerar o README, eles são mapeados para os marcadores correspondentes conforme a tabela de correspondência, e o documento final não deve conter nenhum conteúdo explicativo entre chaves.

## 6. Apêndice B · Modelo de tabela de correspondência terminológica chinês-inglês

| Chinês | English | Abreviação | Descrição |
| --- | --- | --- | --- |
| pendente | TBD | — | — |

## 7. Apêndice C · Modelo de tabela de inventário de dependências

| Nº | Nome do componente | Versão | Forma de referência | Titular dos direitos | Licença | Endereço oficial | Finalidade neste projeto | Modificado | Descrição da modificação | Local do texto original |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pendente | pendente | Direta | pendente | pendente | pendente | pendente | Não | Nenhuma | pendente |

Os requisitos dos campos estão na [especificação de conformidade de código aberto](./open-source-compliance-specification.md).

## 8. Área de preenchimento das informações do projeto

Após complementar as informações do projeto abaixo, iniciar a fase 0 (ver [fluxo de execução](./execution-process.md)).

- Nome do projeto:
- Posicionamento em uma frase:
- Descrição do repositório (idioma nacional e inglês):
- Tags de tópico:
- Contexto do projeto:
- Funcionalidades centrais:
- Stack tecnológico e versão:
- Inventário de dependências (ou caminho do arquivo de inventário):
- Tipo de licença:
- Titular dos direitos autorais e ano:
- Forma de instalação e execução:
- Endereço do repositório e branch de destino:
- Outros materiais complementares:

## 9. Apêndice D · Texto copiável de coleta de informações do projeto

Copiar o conteúdo abaixo para `项目信息采集表.md` no projeto de destino, substituindo item a item o conteúdo após “Preencher:”. Os campos que não puderem ser confirmados devem ser marcados conforme as regras da seção 4 e resumidos na seção 8.

````markdown
# Formulário de coleta de informações do projeto

> Este arquivo serve para coletar, de uma só vez, as informações necessárias à geração da documentação. Após o preenchimento, gerar o README, o NOTICE e os demais documentos entregáveis com base no resultado da coleta.

## 1. Informações básicas

| Campo | Conteúdo preenchido |
| --- | --- |
| Nome do repositório | Preencher: nome do repositório composto por letras minúsculas, números e hífens |
| Nome de exibição | Preencher: nome do projeto para exibição externa; se idêntico ao nome do repositório, escrever “igual ao nome do repositório” |
| Endereço do repositório | Preencher: endereço HTTPS completo |
| Branch de destino | Preencher: nome do branch padrão |
| Código de idioma | Preencher: código do idioma principal, como zh-CN |
| Versão atual | Preencher: número de versão semântica ou “não publicado” |
| Estado de manutenção | Preencher: manutenção ativa / manutenção de baixa frequência / arquivado |

## 2. Posicionamento e escopo de aplicação

| Campo | Conteúdo preenchido |
| --- | --- |
| Posicionamento em uma frase | Preencher: no máximo 60 caracteres, com palavra de categoria e qualificador |
| Descrição do repositório (idioma nacional) | Preencher: no máximo 120 caracteres |
| Descrição do repositório (English) | Preencher: no máximo 120 caracteres |
| Tags de tópico | Preencher: 20 palavras em inglês minúsculas, unidas por hífens |
| Contexto do projeto | Preencher: motivo da iniciação e deficiências das soluções existentes |
| Cenários aplicáveis | Preencher: listar item a item, cada um com condição de disparo |
| Cenários não aplicáveis | Preencher: listar item a item, cada um com o motivo |
| Vantagens | Preencher: cada item com base verificável |
| Limitações | Preencher: cada item com alcance de impacto e forma de contorno |

## 3. Funcionalidades e características

| Módulo | Comportamento perceptível ao usuário | Condição de disparo | Resultado | Evidência ou link |
| --- | --- | --- | --- | --- |
| Preencher: nome do módulo | Preencher: descrição do comportamento | Preencher: forma de disparo | Preencher: saída ou mudança de estado | Preencher: link de teste, captura de tela ou documentação |

## 4. Tecnologia e dependências

| Campo | Conteúdo preenchido |
| --- | --- |
| Linguagem principal e restrições de versão | Preencher: por exemplo `Go >= 1.22` |
| Framework e ferramenta de build | Preencher: nome e restrições de versão |
| Ambiente de execução e requisitos de sistema | Preencher: versão de sistema operacional, ambiente de execução, navegador ou banco de dados |
| Inventário de dependências | Preencher: caminho do arquivo de inventário de dependências ou inserir a tabela do apêndice C nesta seção |
| Materiais externos | Preencher: origem e licença de fontes, imagens, ícones e conjuntos de dados |

## 5. Entrega e uso

| Campo | Conteúdo preenchido |
| --- | --- |
| Requisitos de ambiente | Preencher: condições indispensáveis antes da instalação |
| Comando de instalação | Preencher: comando completo, incluindo a indicação do diretório de trabalho atual |
| Comando de verificação e saída esperada | Preencher: comando diretamente executável e resultado verificável |
| Forma de atualização e desinstalação | Preencher: comandos ou passos da operação |
| Lista de itens de configuração | Preencher: nome da chave, tipo, valor padrão, obrigatoriedade, faixa de valores e efeito |
| Descrição de API ou módulo | Preencher: assinatura da interface, parâmetros, valor de retorno, códigos de erro e exemplo de chamada |
| Matriz de compatibilidade | Preencher: combinações de versão explicitamente suportadas e não suportadas |
| Dados de desempenho | Preencher: ambiente de teste, método, métricas e gargalos; sem dados, escrever “não fornecido, não deve ser inferido” |

## 6. Riscos e fronteiras

| Campo | Conteúdo preenchido |
| --- | --- |
| Problemas conhecidos | Preencher: descrição, alcance de impacto, solução temporária de contorno e link de acompanhamento |
| Limitações atuais | Preencher: o que a versão atual explicitamente não faz |
| Funcionalidades não implementadas | Preencher: funcionalidade, motivo da não implementação e estado do planejamento |
| Segurança e privacidade | Preencher: coleta, armazenamento e transmissão de dados, modelo de permissões e riscos conhecidos |
| Canal de relato de vulnerabilidades | Preencher: e-mail, modelo de Issue ou endereço dedicado |

## 7. Conformidade e responsabilidade

| Campo | Conteúdo preenchido |
| --- | --- |
| Tipo de licença | Preencher: identificador SPDX, por exemplo `MIT` |
| Titular dos direitos autorais | Preencher: nome da pessoa física ou razão social da organização |
| Ano dos direitos autorais | Preencher: ano ou intervalo de anos |
| Local do texto integral da licença | Preencher: caminho do arquivo LICENSE |
| Caminho do arquivo NOTICE | Preencher: caminho do arquivo NOTICE; sem dependências de terceiros, escrever “não aplicável, motivo: ...” |
| Isenção de responsabilidade | Preencher: adoção das fronteiras de responsabilidade ou das cláusulas de ausência de garantias |

## 8. Resumo de itens pendentes

| Nº | Campo | Conteúdo ausente | Responsável pelo complemento | Prazo previsto | Alcance de impacto |
| --- | --- | --- | --- | --- | --- |
| T-001 | Preencher: nome do campo | Preencher: o que falta especificamente | Preencher: nome ou papel | Preencher: YYYY-MM-DD | Preencher: seções ou portões de qualidade afetados |

## 9. Especificações relacionadas

- Estrutura de seções: [especificação de seções do README](./readme-sections-specification.md)
- Modelo copiável: [modelo padrão de README](./readme-standard-template.md)
- Detalhamento dos campos de dependência: [especificação de conformidade de código aberto](./open-source-compliance-specification.md)
- Julgamento de portão: [portão de qualidade](./quality-gate.md)
````

## Arquivos relacionados

- As regras de perguntas e as condições de entrada na fase 0 estão no [fluxo de execução](./execution-process.md)
- A correspondência de impacto por seção está na [especificação de seções do README](./readme-sections-specification.md)
- A correspondência completa dos marcadores do README está no [modelo padrão de README](./readme-standard-template.md)
- O detalhamento dos campos de dependência está na [especificação de conformidade de código aberto](./open-source-compliance-specification.md)
- O resumo de pendências pertence ao portão G12, ver [portão de qualidade](./quality-gate.md)
