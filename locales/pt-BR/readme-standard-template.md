# Modelo padrão de README

> Problema que este arquivo resolve: fornecer um modelo genérico de README pronto para cópia e aplicação direta mediante substituição dos marcadores de posição, cobrindo a apresentação da primeira tela ao longo de todo o ciclo de vida do projeto, acompanhado de tabela de correspondência de marcadores de posição, explicação das seções opcionais e lista de verificação de entrega, para que qualquer desenvolvedor possa customizá-lo rapidamente conforme seu próprio projeto.

## 1. Instruções de uso

1. Copiar todo o conteúdo da seção 3, “Corpo do modelo”, e criar o arquivo `README.md` no diretório raiz do projeto.
2. Substituir um a um os `{{...}}` conforme a tabela de correspondência de marcadores de posição da seção 4; itens não utilizados devem ser excluídos junto com a linha ou a seção inteira em que se encontram.
3. As subseções da seção 3 correspondem às 20 seções da [especificação de seções do README](./readme-sections-specification.md), ordenadas do núcleo para fora segundo o ciclo de vida; ao excluir uma seção, o link correspondente na navegação da primeira tela deve ser excluído em sincronia.
4. Padronizar estilo, cores e quantidade de selos conforme a [especificação de selos](./badge-specification.md); verificar o posicionamento de capturas de tela, tabelas e blocos de código conforme a [especificação de layout visual do README](./readme-visual-layout-specification.md).
5. Selecionar as seções conforme o tipo de projeto, segundo o [guia de adaptação do README por categoria](./readme-category-adaptation-guide.md).
6. Antes do commit, executar a lista de verificação da seção 6, confirmando que não restam marcadores de posição.

## 2. Princípios de customização

- **Itens obrigatórios**: nome do projeto, descrição do repositório, posicionamento em uma frase, instalação, início rápido, licença.
- **Ordem fixa**: a ordem das seções é a mesma da [especificação de seções do README](./readme-sections-specification.md), com correspondência seção a seção entre as versões em chinês e em inglês.
- **Evidência em primeiro lugar**: características centrais, desempenho e decisões de engenharia devem apresentar evidências reconferíveis; são proibidos elogios qualitativos.
- **Divulgação transparente**: cenários não aplicáveis, limitações, problemas conhecidos e funcionalidades não implementadas devem ser listados explicitamente, sem ocultação.
- **Não compromisso**: o roteiro deve ser marcado como “não é compromisso”, sem datas concretas de entrega.
- **Veracidade**: todos os comandos, exemplos, links e selos devem ser efetivamente utilizáveis; contatos e canais de notificação devem ser reais e acessíveis.

## 3. Corpo do modelo

Esta seção está organizada “do núcleo para fora” segundo o ciclo de vida do projeto, com 20 seções em correspondência um a um com as 20 seções da [especificação de seções do README](./readme-sections-specification.md). O texto dentro do bloco de código de cada seção é o corpo pronto para cópia.

O mapeamento entre as seções e as fases do ciclo de vida é o seguinte, para facilitar a localização conforme a necessidade:

| Fase do ciclo de vida | Subseções correspondentes | Foco da apresentação |
| --- | --- | --- |
| Iniciação do projeto | 3.1–3.2 | Posicionamento, contexto, cenários aplicáveis e limitações |
| Análise de requisitos | 3.2–3.3 | Limites funcionais, cenários aplicáveis, cenários não aplicáveis |
| Projeto de arquitetura | 3.5–3.6、3.11 | Decisões de engenharia, pilha tecnológica, estrutura de diretórios |
| Implementação | 3.3–3.4、3.9–3.10 | Funcionalidades, características, configuração, API |
| Verificação por testes | 3.8、3.12 | Exemplo de início rápido, evidências de desempenho |
| Implantação | 3.7、3.14 | Instalação e implantação, matriz de compatibilidade |
| Operação e monitoramento | 3.13、3.15 | Segurança e privacidade, problemas conhecidos e limitações |
| Manutenção iterativa | 3.15–3.17 | Funcionalidades não implementadas, registro de alterações, roteiro posterior |

Observação: o README é a página inicial do projeto; a documentação de processo de cada fase (registros completos de requisitos, projeto, testes, implantação e operação) é sustentada pelas especificações correspondentes, conforme a [matriz de documentação](./document-matrix.md); esta seção apresenta apenas as conclusões visíveis ao usuário.

### 3.1 Nome e posicionamento do projeto (correspondente à seção 1)

````markdown
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="{{LOGO_DARK_URL}}">
    <img alt="{{项目名称}} Logo" src="{{LOGO_LIGHT_URL}}" width="{{LOGO_WIDTH}}">
  </picture>

  <h1>{{项目名称}}</h1>

  [![build](https://img.shields.io/github/actions/workflow/status/{{OWNER}}/{{REPO}}/{{WORKFLOW}}?style=flat-square&logo=github)](https://github.com/{{OWNER}}/{{REPO}}/actions)
  [![version](https://img.shields.io/badge/version-{{VERSION}}-blue?style=flat-square)]({{RELEASE_URL}})
  [![license](https://img.shields.io/badge/license-{{LICENSE_SPDX}}-blue?style=flat-square)](./LICENSE)

  **Descrição do repositório**: 【{{仓库描述中文}} | {{REPO_DESCRIPTION_EN}}】

  **Etiquetas de tópico**: {{TOPICS}}

  {{一句话定位}}

  {{语言切换链接}}

  [Instalação](#instalação) · [Início rápido](#início-rápido) · [Características principais](#características-principais) · [Problemas conhecidos e limitações](#problemas-conhecidos-e-limitações) · [Roteiro posterior](#roteiro-posterior) · [Documentação](#documentação) · [Participação e contribuição](#participação-e-contribuição)
</div>
````

### 3.2 Apresentação do projeto (correspondente à seção 2)

````markdown
## Apresentação do projeto

{{背景}}

{{核心思路}}

**Cenários aplicáveis**

- {{适用场景一}}
- {{适用场景二}}

**Cenários não aplicáveis**

- {{不适用场景一}}
- {{不适用场景二}}

### Vantagens e limitações

**Vantagens**

| Vantagem | Descrição | Forma de verificação |
| --- | --- | --- |
| {{优势名称}} | {{优势说明}} | {{证据}} |
| {{优势名称}} | {{优势说明}} | {{证据}} |

**Limitações**

| Limitação | Alcance do impacto | Forma de contorno temporária |
| --- | --- | --- |
| {{局限描述}} | {{影响范围}} | {{规避方式}} |
| {{局限描述}} | {{影响范围}} | {{规避方式}} |
````

### 3.3 Funcionalidades principais (correspondente à seção 3)

````markdown
## Funcionalidades principais

- {{功能一}}：{{触发条件与结果}}
- {{功能二}}：{{触发条件与结果}}
- {{功能三}}：{{触发条件与结果}}
````

### 3.4 Características principais (correspondente à seção 4)

Cada característica deve conter integralmente a estrutura de cinco partes; a ausência de qualquer uma delas impede sua listagem. A base de redação está em [redação de características e decisões de engenharia](./features-and-engineering-tradeoffs-guide.md).

````markdown
## Características principais

### {{特性名称}}

- **Valor**: {{价值}}
- **Forma de implementação**: {{实现方式}}
- **Diferenciação**: {{差异化}}
- **Evidência**: {{证据}}
````

### 3.5 Detalhes de projeto e decisões de engenharia (correspondente à seção 5)

Redigir em três partes — “cenário → forma de tratamento → motivo” —, cobrindo as categorias da seção 2 de [redação de características e decisões de engenharia](./features-and-engineering-tradeoffs-guide.md).

````markdown
## Detalhes de projeto e decisões de engenharia

### {{取舍主题}}

- **Cenário**: {{场景}}
- **Forma de tratamento**: {{处理方式}}
- **Motivo**: {{原因}}
````

### 3.6 Pilha tecnológica e lista de dependências (correspondente à seção 6)

````markdown
## Pilha tecnológica e lista de dependências

| Categoria | Tecnologia ou componente | Restrição de versão | Finalidade |
| --- | --- | --- | --- |
| Ambiente de execução | {{运行时与版本}} | {{运行时版本约束}} | {{运行时用途}} |
| Compilação | {{构建工具与版本}} | {{构建版本约束}} | {{构建用途}} |
| Testes | {{测试工具与版本}} | {{测试版本约束}} | {{测试用途}} |

O detalhamento das dependências de terceiros e as licenças estão no [NOTICE](./NOTICE).
````

### 3.7 Instalação e implantação (correspondente à seção 7)

````markdown
## Instalação

Requisitos de ambiente: {{运行时 / 操作系统 / 版本}}

```bash
{{包管理器安装命令}}
```

Verificação da instalação:

```bash
{{验证命令}}
```

Saída:

```text
{{预期输出}}
```

Atualização: `{{升级命令}}`. Desinstalação: `{{卸载命令}}`.

Implantação em contêiner: {{容器化说明}}
````

### 3.8 Início rápido (correspondente à seção 8)

````markdown
## Início rápido

{{一句话说明本示例完成什么}}

```{{语言标识}}
{{最小可运行示例}}
```

Saída esperada:

```text
{{输出}}
```
````

### 3.9 Explicação de configuração (correspondente à seção 9)

````markdown
## Explicação de configuração

| Nome da chave | Tipo | Valor padrão | Obrigatório | Faixa de valores | Função | Exemplo |
| --- | --- | --- | --- | --- | --- | --- |
| {{键名}} | {{类型}} | {{默认值}} | {{是否必填}} | {{取值范围}} | {{作用}} | {{示例值}} |

Prioridade de configuração: {{配置优先级}}.

Atualização a quente: {{热更新支持说明}}
````

### 3.10 API ou explicação de módulos (correspondente à seção 10)

````markdown
## API

{{模块概述}}

```{{语言标识}}
{{接口签名}}
```

Parâmetros:

| Parâmetro | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| {{参数名}} | {{参数类型}} | {{参数是否必填}} | {{参数说明}} |

Valor de retorno: {{返回值说明}}

Códigos de erro:

| Código de erro | Significado | Forma de tratamento |
| --- | --- | --- |
| {{错误码}} | {{错误含义}} | {{错误处理方式}} |

Exemplo de chamada:

```{{语言标识}}
{{调用示例}}
```

Limitação de taxa e cota: {{限流与配额说明}}

Detalhes na [documentação da API]({{API_DOC_PATH}}).
````

### 3.11 Estrutura de diretórios (correspondente à seção 11)

````markdown
## Estrutura de diretórios

```text
{{项目名}}/
├── {{目录条目}}   # {{职责}}
├── {{目录条目}}   # {{职责}}
└── {{目录条目}}   # {{职责}}
```
````

### 3.12 Desempenho (correspondente à seção 12)

````markdown
## Desempenho

Ambiente de teste: {{测试环境}}

Método de teste: {{测试方法}}

| Métrica | Valor | Linha de base comparativa |
| --- | --- | --- |
| {{性能指标}} | {{指标数值}} | {{对比基线}} |

Análise de gargalos: {{瓶颈分析}}

Recomendações de ajuste: {{调优建议}}
````

### 3.13 Segurança e privacidade (correspondente à seção 13)

````markdown
## Segurança e privacidade

Coleta e armazenamento de dados: {{数据收集与存储说明}}

Criptografia em trânsito: {{传输加密说明}}

Modelo de permissões: {{权限模型说明}}

Riscos conhecidos: {{已知风险}}

Canal de notificação de vulnerabilidades: {{漏洞上报渠道}}

A política de segurança está no [SECURITY.md](./SECURITY.md).
````

### 3.14 Explicação de compatibilidade (correspondente à seção 14)

````markdown
## Explicação de compatibilidade

| Dimensão | Faixa suportada | Estado de verificação |
| --- | --- | --- |
| Sistema operacional | {{操作系统}} | {{操作系统验证状态}} |
| Ambiente de execução | {{运行时兼容版本}} | {{运行时验证状态}} |
| Navegador | {{浏览器}} | {{浏览器验证状态}} |
| Banco de dados | {{数据库版本}} | {{数据库验证状态}} |

Não suportado explicitamente: {{明确不支持项}}
````

### 3.15 Problemas conhecidos, limitações e funcionalidades não implementadas (correspondente à seção 15)

````markdown
## Problemas conhecidos e limitações

**Problemas conhecidos**

| Descrição do problema | Alcance do impacto | Solução temporária de contorno | Link de acompanhamento |
| --- | --- | --- | --- |
| {{问题描述}} | {{影响范围}} | {{临时规避方案}} | {{跟踪链接}} |

**Limitações atuais**

{{当前限制说明}}

**Funcionalidades não implementadas**

| Funcionalidade | Motivo da não implementação | Estado do planejamento |
| --- | --- | --- |
| {{未实现功能}} | {{未实现原因}} | {{计划状态}} |
````

### 3.16 Registro de alterações (correspondente à seção 16)

````markdown
## Registro de alterações

As alterações de versão seguem o versionamento semântico e a estrutura do Keep a Changelog; o registro completo está em [CHANGELOG.md](./CHANGELOG.md).
````

### 3.17 Roteiro posterior (correspondente à seção 17)

A redação do estado dos itens planejados e da versão-alvo está na [especificação de roteiro](./roadmap-specification.md); deve ser marcado como “não é compromisso”.

````markdown
## Roteiro posterior

> O conteúdo a seguir consiste em itens planejados, não em compromisso de entrega; o escopo e os prazos efetivos prevalecem conforme os registros de publicação.

| Item planejado | Estado | Versão-alvo |
| --- | --- | --- |
| {{计划项}} | {{计划状态}} | {{目标版本}} |
| {{计划项}} | {{计划状态}} | {{目标版本}} |
````

### 3.18 Participação e contribuição (correspondente à seção 18)

````markdown
## Participação e contribuição

- Preparação do ambiente de desenvolvimento: {{搭建步骤}}
- Modelo de branches: {{说明}}
- Especificação de commits: {{Conventional Commits 等}}
- Requisitos de PR: {{要求}}
- Código de conduta: ver [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
- Modelo de Issue: ver [.github/ISSUE_TEMPLATE/](./.github/ISSUE_TEMPLATE/)
````

### 3.19 Direitos autorais e licença (correspondente à seção 19)

````markdown
## Licença

Copyright © {{年份}} {{著作权人}}. Licensed under {{SPDX 标识符}}.

Este projeto é distribuído sob a licença {{许可证名称}}; o texto integral está em [LICENSE](./LICENSE).
````

### 3.20 Declaração de conformidade NOTICE (correspondente à seção 20)

````markdown
## Declaração de conformidade NOTICE

Este projeto utiliza componentes e materiais de terceiros, cujo resumo de licenças e informações de direitos autorais está no [NOTICE](./NOTICE). Esta seção não substitui o arquivo NOTICE.
````

## 4. Tabela de correspondência de marcadores de posição

A tabela lista todos os marcadores de posição presentes no corpo do modelo, em ordem de seção; itens não utilizados devem ser excluídos junto com a linha em que se encontram.

| Marcador de posição | Significado | Exemplo | Obrigatório |
| --- | --- | --- | --- |
| `{{项目名称}}` | Nome de exibição do projeto | `Awesome Tool` | Sim |
| `{{LOGO_DARK_URL}}` | Endereço do logotipo para tema escuro | `media/logo-dark.svg` | Não |
| `{{LOGO_LIGHT_URL}}` | Endereço do logotipo para tema claro | `media/logo-light.svg` | Não |
| `{{LOGO_WIDTH}}` | Largura de exibição do logotipo (px) | `200` | Não |
| `{{OWNER}}` | Proprietário do repositório | `octocat` | Não |
| `{{REPO}}` | Nome do repositório | `awesome-tool` | Não |
| `{{WORKFLOW}}` | Nome do arquivo do fluxo de trabalho de CI | `ci.yml` | Não |
| `{{VERSION}}` | Número da versão atual | `1.2.0` | Não |
| `{{LICENSE_SPDX}}` | Identificador SPDX da licença | `MIT` | Sim |
| `{{RELEASE_URL}}` | URL da página de publicação | link do GitHub Releases | Não |
| `{{仓库描述中文}}` | Parte em chinês da descrição do repositório, ≤120 caracteres | `ferramenta leve de CLI em Go para processar JSON` | Sim |
| `{{REPO_DESCRIPTION_EN}}` | Parte em inglês da descrição do repositório, ≤120 caracteres | `A lightweight Go CLI for JSON processing` | Sim |
| `{{TOPICS}}` | Etiquetas de tópico, completar 20 palavras em inglês minúsculas, unidas por `-` | `go cli json command-line developer-tools` | Não |
| `{{一句话定位}}` | Explicação em uma frase do que é o projeto, para quem se destina e qual problema resolve | `ferramenta leve de CLI em Go para processar JSON` | Sim |
| `{{语言切换链接}}` | Link de troca entre versões de idioma | texto do link `English`, caminho de destino conforme o diretório de idioma real, como `../en-US/README.md` | Não |
| `{{背景}}` | Motivo de criação do projeto e problema a resolver | conforme o projeto | Sim |
| `{{核心思路}}` | Método-chave ou decisão de projeto adotada | conforme o projeto | Sim |
| `{{适用场景一}}` / `{{适用场景二}}` | Situações adequadas ao uso | `necessidade de processar rapidamente arquivos JSON pequenos` | Sim |
| `{{不适用场景一}}` / `{{不适用场景二}}` | Situações explicitamente não recomendadas e seus motivos | `necessidade de processar em fluxo arquivos de nível GB` | Sim |
| `{{优势名称}}` | Nome substantivo da vantagem | `zero dependências` | Não |
| `{{优势说明}}` | Descrição concreta da vantagem | `não introduz dependências de terceiros em tempo de execução` | Não |
| `{{证据}}` | Evidência reconferível ou passos reproduzíveis da vantagem | `a saída de ldd está vazia` | Não |
| `{{局限描述}}` | Descrição concreta da limitação | `não admite escrita concorrente` | Não |
| `{{影响范围}}` | Funcionalidade ou cenário afetado pela limitação | `quando vários processos escrevem ao mesmo tempo` | Não |
| `{{规避方式}}` | Solução temporária de contorno da limitação | `bloqueio externo` | Não |
| `{{功能一}}` / `{{功能二}}` / `{{功能三}}` | Nome da funcionalidade | `filtragem` | Sim |
| `{{触发条件与结果}}` | Condição de acionamento e resultado da funcionalidade | `após passar --filter, gera a saída conforme a condição` | Sim |
| `{{特性名称}}` | Nome da característica, no máximo 15 caracteres | `distribuição em arquivo único` | Não |
| `{{价值}}` | Problema concreto resolvido pela característica e consequência de não resolvê-lo | conforme o projeto | Não |
| `{{实现方式}}` | Tecnologia, mecanismo ou algoritmo adotado, com arquivos ou funções-chave | conforme o projeto | Não |
| `{{差异化}}` | Dimensão de comparação objetivamente julgável em relação a soluções nomeadas | conforme o projeto | Não |
| `{{证据}}` | Testes, benchmarks, localização de código ou passos reproduzíveis | conforme o projeto | Não |
| `{{取舍主题}}` | Tema da decisão de engenharia | `escrita concorrente` | Não |
| `{{场景}}` | Situação concreta que aciona o projeto | conforme o projeto | Não |
| `{{处理方式}}` | Solução adotada | conforme o projeto | Não |
| `{{原因}}` | Motivo de não adotar outras soluções | conforme o projeto | Não |
| `{{运行时与版本}}` / `{{构建工具与版本}}` / `{{测试工具与版本}}` | Nome e versão dos componentes da pilha tecnológica | `Go 1.22` | Não |
| `{{运行时版本约束}}` / `{{构建版本约束}}` / `{{测试版本约束}}` | Faixa de restrição de versão | `>=1.22` | Não |
| `{{运行时用途}}` / `{{构建用途}}` / `{{测试用途}}` | Finalidade do componente | `compilação e execução` | Não |
| `{{运行时 / 操作系统 / 版本}}` | Requisitos de ambiente de instalação | `Go 1.22+、Linux/macOS` | Sim |
| `{{包管理器安装命令}}` | Comando de instalação efetivo | `go install example.com/tool@latest` | Sim |
| `{{验证命令}}` | Comando de verificação da instalação | `tool --version` | Não |
| `{{预期输出}}` | Resultado esperado do comando de verificação | `tool 1.2.0` | Não |
| `{{升级命令}}` / `{{卸载命令}}` | Comandos de atualização e desinstalação | `go install example.com/tool@latest` | Não |
| `{{容器化说明}}` | Explicação sobre conteinerização ou endereço da imagem | `docker run ...` | Não |
| `{{一句话说明本示例完成什么}}` | Objetivo do exemplo de início rápido | `gerar a saída do JSON filtrado por campo` | Sim |
| `{{语言标识}}` | Identificador de linguagem do bloco de código | `bash` | Sim |
| `{{最小可运行示例}}` | Exemplo mínimo executável | conforme o projeto | Sim |
| `{{输出}}` | Saída esperada do exemplo | conforme o projeto | Sim |
| `{{键名}}` | Nome da chave de configuração | `output.format` | Não |
| `{{类型}}` | Tipo do valor de configuração | `string` | Não |
| `{{默认值}}` | Valor padrão da configuração | `json` | Não |
| `{{是否必填}}` | Se o preenchimento é obrigatório | `Não` | Não |
| `{{取值范围}}` | Faixa de valores permitida | `json / yaml` | Não |
| `{{作用}}` | Função da configuração | `especificar o formato de saída` | Não |
| `{{示例值}}` | Exemplo de configuração | `yaml` | Não |
| `{{配置优先级}}` | Ordem de prioridade entre configurações de várias origens | `argumentos de linha de comando > variáveis de ambiente > arquivo de configuração` | Não |
| `{{热更新支持说明}}` | Se há suporte a atualização a quente e de que forma | `não suportado; exige reinício` | Não |
| `{{模块概述}}` | Visão geral da finalidade do módulo | conforme o projeto | Não |
| `{{接口签名}}` | Assinatura de função ou interface | `func Filter(in io.Reader, key string) error` | Não |
| `{{参数名}}` / `{{参数类型}}` / `{{参数是否必填}}` / `{{参数说明}}` | Campos de parâmetros da interface | `in / io.Reader / Sim / fluxo de entrada` | Não |
| `{{返回值说明}}` | Significado do valor de retorno | `retorna nil em caso de sucesso` | Não |
| `{{错误码}}` / `{{错误含义}}` / `{{错误处理方式}}` | Campos de código de erro | `E001 / entrada vazia / verificar a entrada` | Não |
| `{{调用示例}}` | Código de chamada da interface | conforme o projeto | Não |
| `{{限流与配额说明}}` | Regras de limitação de taxa e cota | `sem limitação de taxa` | Não |
| `{{API_DOC_PATH}}` | Caminho relativo da documentação da API | `./docs/api.md` | Não |
| `{{项目名}}` | Nome do nó raiz da árvore de diretórios | `awesome-tool` | Sim |
| `{{目录条目}}` / `{{职责}}` | Item da árvore de diretórios e sua responsabilidade | `cmd/ / ponto de entrada dos comandos` | Sim |
| `{{测试环境}}` | Hardware, sistema e versão do ambiente de execução | `Intel i7 / Ubuntu 22.04 / Go 1.22` | Não |
| `{{测试方法}}` | Método de teste de desempenho | `go test -bench` | Não |
| `{{性能指标}}` / `{{指标数值}}` / `{{对比基线}}` | Campos de métricas de desempenho | `vazão / 120 MB/s / 80 MB/s` | Não |
| `{{瓶颈分析}}` | Explicação do gargalo de desempenho | conforme o projeto | Não |
| `{{调优建议}}` | Recomendação de ajuste de desempenho | conforme o projeto | Não |
| `{{数据收集与存储说明}}` | Alcance da coleta e forma de armazenamento dos dados | `não coleta dados de usuário` | Não |
| `{{传输加密说明}}` | Forma de criptografia em trânsito | `HTTPS` | Não |
| `{{权限模型说明}}` | Explicação do modelo de permissões | `baseado em Token` | Não |
| `{{已知风险}}` | Risco de segurança conhecido | conforme o projeto | Não |
| `{{漏洞上报渠道}}` | Canal real e acessível para notificação de vulnerabilidades | `security@example.com` | Não |
| `{{操作系统}}` / `{{操作系统验证状态}}` | Faixa de suporte e estado de verificação do sistema operacional | `Linux, macOS / verificado` | Não |
| `{{运行时兼容版本}}` / `{{运行时验证状态}}` | Faixa de compatibilidade e estado de verificação do ambiente de execução | `Go 1.20+ / verificado` | Não |
| `{{浏览器}}` / `{{浏览器验证状态}}` | Faixa de suporte e estado de verificação do navegador | `Chrome 100+ / verificado` | Não |
| `{{数据库版本}}` / `{{数据库验证状态}}` | Versão do banco de dados e estado de verificação | `PostgreSQL 14+ / verificado` | Não |
| `{{明确不支持项}}` | Ambiente explicitamente não suportado | `Windows de 32 bits` | Não |
| `{{问题描述}}` | Descrição do problema conhecido | `alto consumo de memória com entradas muito longas` | Não |
| `{{影响范围}}` | Funcionalidade ou cenário afetado pelo problema | `quando a entrada ultrapassa 100 MB` | Não |
| `{{临时规避方案}}` | Forma de contorno temporária | `processamento em lotes` | Não |
| `{{跟踪链接}}` | Endereço de acompanhamento do problema | link de Issue do GitHub | Não |
| `{{当前限制说明}}` | Limitação funcional atual | `atualmente não há suporte a escrita concorrente` | Não |
| `{{未实现功能}}` | Funcionalidade ainda não implementada | `atualização a quente da configuração` | Não |
| `{{未实现原因}}` | Motivo da não implementação | `baixa prioridade` | Não |
| `{{计划状态}}` | Estado do planejamento (para funcionalidades não implementadas e roteiro) | `planejado` | Não |
| `{{计划项}}` | Item planejado do roteiro | `suportar atualização a quente do arquivo de configuração` | Não |
| `{{目标版本}}` | Versão-alvo do item planejado | `v1.3.0` | Não |
| `{{搭建步骤}}` | Passos ou link para preparação do ambiente de desenvolvimento | `ver CONTRIBUTING.md` | Não |
| `{{说明}}` | Explicação do modelo de branches | `criar branch feat a partir de main` | Não |
| `{{Conventional Commits 等}}` | Explicação da especificação de commits | `Conventional Commits` | Não |
| `{{要求}}` | Requisitos de PR | `alteração única, testes aprovados` | Não |
| `{{年份}}` | Ano dos direitos autorais | `2026` | Sim |
| `{{著作权人}}` | Titular dos direitos autorais | `Ntarstudio` | Sim |
| `{{SPDX 标识符}}` | Identificador SPDX na linha de direitos autorais | `MIT` | Sim |
| `{{许可证名称}}` | Nome completo da licença | `MIT` | Sim |

## 5. Explicação das seções opcionais

A seção 3 já apresenta o corpo copiável das 20 seções. A seguir, orientações complementares sobre inclusão e exclusão conforme o tipo de projeto; ao excluir uma seção, o link correspondente na navegação da primeira tela deve ser excluído em sincronia.

| Seção | Tipos em que se recomenda manter | Condição de exclusão |
| --- | --- | --- |
| Características principais | Todos | Pode ser excluída quando não houver evidência reconferível, sem substituí-la por descrição qualitativa |
| Detalhes de projeto e decisões de engenharia | Frameworks, aplicações, serviços | Pode ser excluída quando não houver decisão relevante |
| Pilha tecnológica e lista de dependências | Bibliotecas, frameworks | Pode ser excluída quando não houver dependências externas |
| Desempenho | CLI, bibliotecas, serviços | Pode ser excluída quando não houver dados de teste; é proibido estimar números |
| Segurança e privacidade | Serviços, aplicações, projetos que tratam dados pessoais | Pode ser simplificada em ferramentas puramente locais |
| Explicação de compatibilidade | Bibliotecas, SDKs, aplicações multiplataforma | Pode ser simplificada quando houver um único ambiente de execução |
| Registro de alterações | Todos | Apenas quando o CHANGELOG não existir, substituir por um resumo de alterações embutido |
| Roteiro posterior | Todos | Pode ser excluída quando não houver plano público |
| Declaração de conformidade NOTICE | Projetos com dependências de terceiros | Pode ser excluída quando não houver dependências de terceiros |

## 6. Lista de verificação antes da entrega

- [ ] Não há marcadores de posição `{{...}}` remanescentes.
- [ ] A primeira tela contém a descrição do repositório 【chinês | inglês】 e as etiquetas de tópico, ambas consistentes com os metadados do repositório.
- [ ] A descrição do repositório, em chinês e em inglês, não ultrapassa 120 caracteres cada.
- [ ] As etiquetas de tópico completam 20, todas em inglês minúsculo, unidas por `-`.
- [ ] O posicionamento em uma frase contém a palavra de categoria; o texto em chinês não ultrapassa 60 caracteres e o em inglês, 25 palavras.
- [ ] Cada característica principal contém a estrutura de cinco partes e evidência reconferível.
- [ ] Vantagens e limitações estão listadas separadamente, com alcance do impacto e forma de contorno nas limitações.
- [ ] Os problemas conhecidos incluem link de acompanhamento; as funcionalidades não implementadas incluem motivo e estado do planejamento.
- [ ] O roteiro está marcado como “não é compromisso”, sem datas concretas de entrega.
- [ ] Cenários não aplicáveis e itens explicitamente não suportados estão listados.
- [ ] Há um único título de primeiro nível, níveis de título de segundo nível contínuos e ordem das seções igual às 20 seções da especificação.
- [ ] O estilo dos selos é uniforme, os links são válidos e os textos `alt` são explícitos.
- [ ] Os comandos de instalação e o exemplo de início rápido foram testados e são executáveis.
- [ ] Todos os blocos de código têm marcação de linguagem e todas as imagens têm texto `alt`.
- [ ] Os caminhos relativos funcionam em forks e no modo offline.
- [ ] O LICENSE existe e o identificador SPDX é consistente com o README.
- [ ] A ordem das seções das versões em chinês e em inglês corresponde uma a uma.

## Arquivos relacionados

- A definição completa das seções está na [especificação de seções do README](./readme-sections-specification.md)
- A configuração de selos está na [especificação de selos](./badge-specification.md)
- A especificação visual está na [especificação de layout visual do README](./readme-visual-layout-specification.md)
- O recorte por tipo está no [guia de adaptação do README por categoria](./readme-category-adaptation-guide.md)
- A base da pesquisa está no [relatório de pesquisa sobre modelos de README](./readme-template-research-report.md)
- A redação de características e decisões está em [redação de características e decisões de engenharia](./features-and-engineering-tradeoffs-guide.md)
- As regras de metadados estão na [especificação de nomes de projeto](./project-naming-specification.md)
- As regras de roteiro estão na [especificação de roteiro](./roadmap-specification.md)
