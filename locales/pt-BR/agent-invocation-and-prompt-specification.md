# Especificação de invocação de Agent e de prompts

> Problema que este arquivo resolve: definir o contrato de despacho e a forma de redação de prompts quando um Agent invoca o conjunto de especificações, garantindo que a invocação seja verificável, não exceda suas atribuições e não sofra desvio.

## 1. Princípios de invocação

1. Responsabilidade única: uma invocação conclui apenas uma tarefa; é proibido executar outras tarefas “de passagem”.
2. Separação entre leitura e escrita: o subagente apenas lê e analisa; a escrita de arquivos e as operações de git são executadas de forma centralizada pelo controlador (ver [contrato de despacho de subagentes](./sub-agent-dispatch-contract.md)).
3. Exigência de evidência: as conclusões devem trazer evidência (caminho + número da linha / saída de comando); conclusões sem evidência são consideradas inválidas.
4. Sem comunicação direta: os subagentes não se comunicam entre si; tudo é agregado pelo controlador.

## 2. Estrutura do prompt

O prompt de invocação deve conter quatro elementos:

```text
TASK:    <一句话任务>
INPUT:   <必要上下文，只给所需部分>
OUTPUT:  <结构化输出格式，表格或 JSON，禁止散文>
FAIL:    <无法完成时的返回约定，不得瞎编>
```

## 3. Redação do prompt

1. Empregar linguagem escrita e orações imperativas, com informação completa e sem depender de inferência a partir do contexto (ver [especificação geral de redação](./general-writing-specification.md)).
2. Especificar o formato de saída e o retorno em caso de falha, evitando improvisos do modelo.
3. Ao citar especificações, indicar o caminho do arquivo (ver [especificação de metadados legíveis por máquina](./machine-readable-metadata-specification.md)).
4. Usar formato unificado para modelos e marcadores de posição (ver [coleta de informações e modelos](./information-collection-and-templates.md)).

## 4. Regras obrigatórias

1. Não deve ser exigido que o Agent invente resultados de verificação; os itens não verificáveis são marcados como SKIP + motivo.
2. O processo de raciocínio interno não deve ser incluído nos entregáveis (ver [práticas proibidas](./prohibited-practices.md)).
3. O conteúdo relacionado à segurança deve ser tratado conforme a [especificação de segurança e privacidade](./security-and-privacy-specification.md).

## Arquivos relacionados

- Para o contrato de despacho, ver [contrato de despacho de subagentes](./sub-agent-dispatch-contract.md)
- Para os metadados de máquina, ver a [especificação de metadados legíveis por máquina](./machine-readable-metadata-specification.md)
- Para o encapsulamento de Skill, ver a [especificação de redação de Skill](./skill-authoring-specification.md)
- Para as ferramentas MCP, ver a [especificação de ferramentas MCP](./mcp-tool-specification.md)
