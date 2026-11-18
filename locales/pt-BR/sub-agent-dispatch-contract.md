# Contrato de despacho de subagentes

> Problema que este arquivo resolve: definir os quatro elementos que devem estar claramente escritos ao despachar tarefas a subagentes e as restrições de colaboração, garantindo conclusões estruturadas, verificáveis e sem desvio de regras.

## 1. Os quatro elementos do despacho

Cada despacho deve explicitar quatro elementos:

```text
TASK:    <tarefa em uma frase>
INPUT:   <arquivos/contexto necessários, apenas a parte indispensável>
OUTPUT:  <formato estruturado, tabela ou JSON, proibida prosa>
FAIL:    <o que retornar quando não for possível executar, em vez de inventar>
```

## 2. Restrições

- Um subagente executa apenas uma tarefa por vez; é proibido “aproveitar e escrever também o README”.
- Os subagentes apenas leem e apenas apresentam propostas; **a escrita de arquivos e as operações de git são executadas exclusivamente pelo controlador principal**.
- As conclusões dos subagentes devem trazer evidência (caminho do arquivo + número da linha / saída de comando); conclusões sem evidência são consideradas inválidas.
- Os subagentes não se comunicam diretamente entre si; tudo é consolidado pelo controlador principal, para evitar desvio de regras.

## Arquivos relacionados

- Para os destinatários do despacho e as dimensões, ver a [matriz de dimensões de revisão](./review-dimension-matrix.md)
- Para o despacho de redação de documentação, ver a [matriz de documentação](./document-matrix.md)
- O despacho ocorre nas Phase 2 e Phase 4 do [processo de execução](./execution-process.md)
