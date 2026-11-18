# Matriz de dimensões de revisão

> Problema que este arquivo resolve: definir as 14 dimensões da auditoria paralela da Phase 2, seus pontos de verificação, o agent sugerido e o nível de falha, como base para o despacho e o julgamento.

## Matriz de dimensões de revisão

| # | Dimensão | Pontos de verificação (palavras-chave; os detalhes são desdobrados pelo subagente) | Agent sugerido | Nível de falha |
|---|---|---|---|---|
| D1 | Segurança e privacidade | Varredura de chaves, `.env`, chaves privadas, domínios/IP internos, dados pessoais, resíduos em registros | security-auditor | P0 |
| D2 | Licença e aspectos legais | Existência e tipo de LICENSE, compatibilidade da licença das dependências, NOTICE, declarações de terceiros | license-checker | P0 |
| D3 | Higiene do repositório | Cobertura do .gitignore, artefatos e diretórios de dependências, .gitattributes, fim de linha LF, bits de execução, conflitos de maiúsculas e minúsculas em nomes de arquivo | repo-hygienist | P0/P1 |
| D4 | Tamanho e binários | Arquivos >50MB, compressão de imagens, configuração de LFS, crescimento do histórico | repo-hygienist | P1 |
| D5 | Compilação reproduzível | Commit do lockfile, declaração da versão do motor, scripts de compilação, compilação bem-sucedida em ambiente limpo | build-verifier | P0 |
| D6 | Testes e análise estática | Testes unitários aprovados, cobertura, lint, format, verificação de tipos | ci-runner | P0/P1 |
| D7 | Histórico de commits | Conventional Commits, atomicidade, ausência de WIP, informações do autor, ausência de mensagens de commit sensíveis | commit-reviewer | P1 |
| D8 | Branches e publicação | Proteção da main, nomenclatura de branches, tag SemVer, annotated tag, Release Notes | release-manager | P1 |
| D9 | Automação | Workflow de CI executável, selos de status, dependabot, CODEOWNERS, modelos de issue/PR | ci-runner | P1 |
| D10 | Metadados do repositório | description (formato combinado bilíngue `idioma nacional \| inglês`, ≤120 caracteres em cada idioma), topics (20 no total, apenas em inglês, tudo em minúsculas), branch padrão, links da área About, social preview | metadata-agent | P1 |
| D11 | Integridade da documentação | Verificação da existência de cada item da matriz de documentação | docs-orchestrator | P0/P1 |
| D12 | Qualidade da documentação | Hierarquia de títulos, identificação de linguagem nos blocos de código, validade dos links, alt das imagens, espaçamento entre chinês e inglês, ausência de marcadores de posição | docs-orchestrator | P1/P2 |
| D13 | Página inicial do README | Posicionamento em uma frase, instalação, início rápido, selos ≤4, capturas de tela, ausência de caminhos absolutos locais | readme-writer | P1 |
| D14 | Governança da comunidade | CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, modelos de Issue, canais de suporte | docs-orchestrator | P2 |

## Significado dos níveis

- **P0**: bloqueia o push.
- **P1**: deve ser corrigido antes do push ou obrigatoriamente registrado como pendência.
- **P2**: melhoria recomendada.

## Despacho e consolidação

- A forma de despacho de cada dimensão está no [contrato de despacho de subagentes](./sub-agent-dispatch-contract.md).
- Os resultados do julgamento são consolidados na lista de problemas do [formato do relatório de auditoria](./audit-report-format.md), e cada item deve trazer evidência.
- A base de verificação de D11/D12 está na [matriz de documentação](./document-matrix.md) e no [portão de qualidade](./quality-gate.md).

## Arquivos relacionados

- O momento de execução está na Phase 2 do [processo de execução](./execution-process.md)
- As condições de liberação dos portões estão no [portão de qualidade](./quality-gate.md)
