# Matriz de documentação

> Problema que este arquivo resolve: definir a responsabilidade exclusiva de cada documento entregue, o conteúdo terminantemente proibido e as restrições de divisão, assegurando um arquivo por responsabilidade e vedando a fusão.

## 1. Arquivos e responsabilidades

| Arquivo | Responsabilidade exclusiva | Terminantemente proibido |
|---|---|---|
| `README.md` | Página inicial: o que é, como instalar, como executar, onde consultar detalhes | API completa, fluxo de contribuição, registro de atualizações |
| `LICENSE` | Texto integral da licença | Qualquer texto explicativo |
| `CHANGELOG.md` | Alterações de versão voltadas ao usuário | Detalhes internos de refatoração, planos de desenvolvimento |
| `CONTRIBUTING.md` | Processo e normas para contribuidores externos | Descrição das funcionalidades do projeto |
| `CODE_OF_CONDUCT.md` | Código de conduta | Conteúdo técnico |
| `SECURITY.md` | Canais de reporte de vulnerabilidades e política de resposta | Lista de vulnerabilidades conhecidas |
| `docs/api.md` | Referência completa de API | Tutoriais |
| `docs/architecture.md` | Arquitetura e fronteiras de módulos | Exemplos de uso |
| `docs/naming.md` | Convenções de nomenclatura | Outras especificações |
| `docs/release.md` | Processo de publicação e política de versões | Registro de alterações |
| `.github/PULL_REQUEST_TEMPLATE.md` | Lista de autoverificação da PR | Apresentação do projeto |
| `.github/ISSUE_TEMPLATE/*.yml` | Formulário estruturado de issue | Texto livre |
| `.github/workflows/*.yml` | CI/CD | Documentação explicativa |

> Observação: o texto normativo de `docs/naming.md` está na [especificação de nomenclatura de projetos](./project-naming-specification.md); o texto normativo de `docs/release.md` está na [especificação de push e publicação](./push-and-release-specification.md).

## 2. Restrições

- Arquivos com mais de 300 linhas devem ser divididos em `docs/`, mantendo no README apenas o resumo + link.
- Os nomes de arquivo são fixos em maiúsculas e os caminhos são fixos; é vedado criar níveis de diretório próprios.
- Todo documento deve começar com uma frase que explique “qual problema este arquivo resolve” e terminar com links cruzados para arquivos relacionados.

## Arquivos relacionados

- A estrutura de 20 capítulos do README está na [especificação de seções do README](./readme-sections-specification.md)
- A especificação autônoma do NOTICE está na [especificação de NOTICE](./notice-specification.md)
- A especificação autônoma da LICENSE está na [especificação de LICENSE](./license-specification.md)
- A completude e a qualidade da documentação pertencem às dimensões D11/D12; ver [matriz de dimensões de revisão](./review-dimension-matrix.md)
