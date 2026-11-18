# Modelo de guia de contribuição

> Problema que este arquivo resolve: fornecer um modelo de guia de contribuição pronto para cópia, a fim de que o projeto gere o CONTRIBUTING.md, cobrindo formas de participação, preparação do ambiente, modelo de branches, convenção de commits, requisitos de PR, requisitos de testes, código de conduta e declaração de licença; as instruções de preenchimento que o acompanham cobrem o recorte para cada tipo de projeto.

## 1. Instruções de uso

1. Copiar todo o conteúdo do modelo de texto (seção 3) e criar com ele o arquivo `CONTRIBUTING.md` no diretório raiz do projeto.
2. Substituir os marcadores de posição conforme a seção 4; todos os comandos devem ser comandos reais, executáveis diretamente.
3. Recortar conforme as variantes de cenário da seção 5: em projetos do tipo documentação, remover o parágrafo de comandos de teste e preservar o fluxo de Issue e de PR.
4. O fundamento das regras está na [especificação de guia de contribuição](./contribution-guide-specification.md); os detalhes de branch e de commit estão, respectivamente, na [especificação de fluxo de trabalho Git e branches](./git-workflow-and-branching-specification.md) e na [especificação de mensagens de commit](./commit-message-specification.md).

## 2. Princípios de customização

- **Executável**: os comandos devem indicar o diretório de trabalho e as premissas de dependências; é proibido escrever apenas “instalar dependências” sem o comando concreto.
- **Com condição de acionamento**: cada passo deve indicar quando é executado e qual é o resultado esperado.
- **Não genérico**: é proibido escrever apenas “PRs são bem-vindos” sem um fluxo substancial, em correspondência com a verificação de governança da comunidade do [portão de qualidade](./quality-gate.md).
- **Referenciar em vez de copiar**: as regras de commit e de teste devem referenciar as especificações correspondentes, sem repetir o texto integral neste arquivo.

## 3. Modelo de texto

````markdown
# Guia de contribuição

> Este arquivo explica como participar da contribuição do {{项目名称}} e destina-se a contribuidores externos e a participantes de primeira viagem.

## Formas de participação

| Forma | Cenário aplicável | Entrada |
| --- | --- | --- |
| Discussão em issue | Sugestão de funcionalidade, relato de problema | {{议题入口}} |
| Melhoria de documentação | Erros de digitação, complemento de exemplos, otimização de estrutura | Enviar PR diretamente |
| Contribuição de código | Correção de defeitos, implementação de funcionalidades | Ver o fluxo abaixo |
| Relato de problema | Bloqueio de uso, reprodução de anomalia | {{问题反馈入口}} |

## Preparação do ambiente de desenvolvimento

Premissa: {{环境前提}}

```bash
# Clonar o repositório
git clone {{仓库地址}}
cd {{项目目录名}}

# Instalar dependências
{{依赖安装命令}}

# Executar localmente
{{本地运行命令}}
```

Resultado esperado: {{验证本地环境可用的方式}}

## Modelo de branches

- Criar um branch pessoal a partir de {{基准分支}}, com o formato de nome `{{分支命名格式}}` (por exemplo, `feat/breve-descricao`).
- Cada PR deve tratar de um único assunto; quando o escopo da mudança for muito amplo, deve-se dividi-lo.
- É proibido fazer commit diretamente em {{受保护分支}}; a integração deve ocorrer por PR.

## Convenção de commits

As mensagens de commit seguem o Conventional Commits, com o formato `type(scope): subject`. Tipos usuais: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`. Exemplo:

```text
feat(cli): add config file support
```

As regras completas estão na [especificação de mensagens de commit]({{提交规范链接}}).

## Requisitos de PR

Antes de enviar o PR, concluir a seguinte autoverificação:

- [ ] O escopo da mudança é único e há uma issue ou explicação correspondente.
- [ ] A mensagem de commit segue o formato acima.
- [ ] A execução local de `{{测试命令}}` foi integralmente aprovada.
- [ ] A documentação foi atualizada em conjunto com o código.
- [ ] Não foram introduzidas chaves, chaves privadas nem informações sensíveis.
- [ ] A descrição indica o conteúdo da mudança, o motivo e a forma de verificação.

## Requisitos de testes

| Item de verificação | Comando | Critério de aprovação |
| --- | --- | --- |
| Testes unitários | `{{单元测试命令}}` | Aprovação integral |
| Análise estática | `{{lint 命令}}` | Sem erros |
| Validação de build | `{{构建命令}}` | Build bem-sucedido |

Limite de cobertura: {{覆盖率要求}}.

## Código de conduta

Ao participar deste projeto, a pessoa concorda em observar o [código de conduta](./CODE_OF_CONDUCT.md).

## Convenção de Issue

- Antes de perguntar, pesquisar as issues existentes para evitar duplicidade.
- O relato de defeito deve conter: informações do ambiente, passos de reprodução, resultado esperado, resultado efetivo e log de erro.
- A sugestão de funcionalidade deve explicar o cenário de uso e a alternativa caso não seja adotada.

## Declaração de licença

O conteúdo contribuído segue, por padrão, a licença do projeto {{许可证名称及 SPDX 标识符}}, cujo texto integral está em [LICENSE](./LICENSE). Ao enviar, a pessoa declara ter o direito de licenciar sua contribuição sob essa licença.
````

## 4. Tabela de correspondência de marcadores de posição e definição de campos

| Marcador de posição | Obrigatório | Definição do campo | Exemplo de preenchimento |
| --- | --- | --- | --- |
| `{{项目名称}}` | Sim | Nome externo do projeto | `FooBar` |
| `{{议题入口}}` | Sim | Endereço real e acessível das issues | `https://github.com/owner/repo/issues` |
| `{{问题反馈入口}}` | Não | Canal dedicado quando distinto da entrada de issues | `https://github.com/owner/repo/issues/new` |
| `{{环境前提}}` | Sim | Versão da linguagem, gerenciador de pacotes e dependências de sistema | `Node.js 20+, pnpm 8+` |
| `{{仓库地址}}` | Sim | Endereço clonável do repositório | `https://github.com/owner/repo.git` |
| `{{项目目录名}}` | Sim | Nome do diretório após a clonagem | `repo` |
| `{{依赖安装命令}}` | Sim | Comando real de instalação | `pnpm install` |
| `{{本地运行命令}}` | Sim | Comando real de inicialização | `pnpm dev` |
| `{{验证本地环境可用的方式}}` | Sim | Sinal observável de sucesso | `Acessar localhost:3000 e ver a página inicial` |
| `{{基准分支}}` | Sim | Branch de origem a partir do qual o branch é criado | `main` |
| `{{分支命名格式}}` | Sim | Regra de nomenclatura de branches | `feat/breve-descricao` |
| `{{受保护分支}}` | Sim | Branch em que é proibido fazer commit direto | `main` |
| `{{提交规范链接}}` | Não | Endereço da convenção de commits interna ou externa ao projeto | `./docs/COMMIT_CONVENTION.md` |
| `{{测试命令}}` | Sim | Comando real de testes | `pnpm test` |
| `{{lint 命令}}` | Sim | Comando real de análise estática | `pnpm lint` |
| `{{构建命令}}` | Sim | Comando real de build | `pnpm build` |
| `{{覆盖率要求}}` | Não | Limite de cobertura para código novo | `Código novo não inferior a 80%` |
| `{{许可证名称及 SPDX 标识符}}` | Sim | Nome completo da licença do projeto e identificador SPDX | `Licença MIT (MIT)` |

## 5. Instruções de preenchimento e variantes de cenário

| Cenário | Seções obrigatórias | Seções recortáveis | Pontos de ajuste |
| --- | --- | --- | --- |
| Projeto de código | Todas | Nenhuma | Os comandos devem ser realmente executados e validados |
| Projeto de documentação | Formas de participação, requisitos de PR, código de conduta, licença | Requisitos de testes, preparação do ambiente de desenvolvimento | Remover a tabela de testes e manter a autoverificação de PR |
| Projeto individual | Formas de participação, requisitos de PR, código de conduta, licença | A preparação do ambiente pode ser enxuta | Definir expressamente se contribuições externas são aceitas |
| Projeto corporativo | Todas | Nenhuma | Acrescentar link do acordo de licença de contribuidor (CLA) e requisitos jurídicos |

Comparação de erros frequentes:

| Redação incorreta | Consequência | Redação correta |
| --- | --- | --- |
| “Toda forma de contribuição é bem-vinda” | Sem caminho concreto, o contribuidor não sabe por onde começar | Listar a tabela de formas de participação e as entradas |
| “Basta executar os testes” | Sem indicação do comando e do critério de aprovação | Indicar comando, critério de aprovação e limite de cobertura |
| Comando escrito como `npm install` em um projeto que usa pnpm | Comando não executável | Coerência com o lockfile real |

## 6. Exemplo completo

A seguir, um exemplo preenchido do trecho de comandos, apenas como referência de formato.

```bash
# Clonar o repositório
git clone https://github.com/owner/repo.git
cd repo

# Instalar dependências
pnpm install

# Executar localmente
pnpm dev
```

Resultado esperado: acessar localhost:3000 e ver a página inicial.

## Arquivos relacionados

- Especificação correspondente: [especificação de guia de contribuição](./contribution-guide-specification.md)
- Modelos complementares: [modelo de código de conduta](./code-of-conduct-template.md), [modelo de SECURITY](./security-template.md)
- Detalhes de teste: [especificação de testes](./testing-specification.md)
- Dimensão de governança da comunidade: [matriz de dimensões de revisão](./review-dimension-matrix.md)
- Voltar ao índice em chinês simplificado: [README](./README.md)
