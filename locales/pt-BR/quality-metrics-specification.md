# Especificação de métricas de qualidade

> Problema que este arquivo resolve: definir métricas de qualidade rastreáveis e seus critérios de apuração, evitando avaliar a qualidade do projeto com números sem fundamento.

## 1. Princípios das métricas

1. As métricas devem ser mensuráveis e reproduzíveis, com indicação da forma de coleta e do critério de apuração.
2. As métricas servem para melhoria, não para ranking simplista nem para gerar pressão.
3. Cada métrica deve indicar o valor-alvo e o valor atual e ser revista periodicamente.

## 2. Métricas sugeridas

| Categoria | Métrica | Descrição do critério |
| --- | --- | --- |
| Testes | Cobertura de testes | Proporção de linhas de código cobertas, com indicação da ferramenta de medição |
| Testes | Taxa de aprovação em testes | Casos aprovados / total de casos |
| Build | Taxa de sucesso de build | Builds bem-sucedidos / total de builds |
| Defeitos | Densidade de defeitos | Número de defeitos encontrados por unidade de tamanho de código |
| Defeitos | Tempo médio de correção | Tempo médio entre a descoberta e a conclusão da correção |
| Desempenho | Tempo de resposta | Indicar o cenário e o percentil (por exemplo, P95) |
| Dependências | Número de vulnerabilidades de alto risco | Quantidade de vulnerabilidades de alto risco não corrigidas em dependências |

## 3. Regras obrigatórias

1. As métricas de desempenho devem indicar o ambiente e o método de teste; números sem condição declarada são proibidos (em correspondência com a [especificação geral de redação](./general-writing-specification.md)).
2. A coleta de dados das métricas deve ser automatizada, reduzindo o viés da apuração manual.
3. Métricas anômalas devem ter registro de acompanhamento, incorporado à [especificação de roteiro](./roadmap-specification.md) ou ao rastreamento de problemas.

## Arquivos relacionados

- Para o portão de qualidade, ver o [portão de qualidade](./quality-gate.md)
- Para os requisitos de testes, ver a [especificação de testes](./testing-specification.md)
- Para a redação da seção de desempenho, ver a [especificação de seções do README](./readme-sections-specification.md)
