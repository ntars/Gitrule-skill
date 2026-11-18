# Especificação de ferramentas MCP

> Problema que este arquivo resolve: definir as regras de design de interface e de descrição ao expor o conjunto de especificações como ferramentas por meio do protocolo de contexto de modelo (MCP), garantindo que as ferramentas possam ser corretamente descobertas e invocadas pelo modelo.

## 1. Princípios de design de ferramentas

1. Responsabilidade única: uma ferramenta faz uma coisa, evitando interfaces que tentem abranger tudo.
2. Descrição clara: a descrição da ferramenta explica a finalidade e os cenários de aplicação, para que o modelo possa decidir quando invocá-la.
3. Parâmetros explícitos: cada parâmetro tem tipo, obrigatoriedade, faixa de valores e descrição.
4. Saída estruturada: retornar dados estruturados, evitando textos longos em prosa.

## 2. Campos obrigatórios

| Campo | Requisito |
| --- | --- |
| name | Identificador único, kebab-case em minúsculas |
| description | Finalidade e condições de disparo, específicas o suficiente para permitir decisão |
| inputSchema | Tipos de parâmetro, campos obrigatórios, restrições |
| Valor de retorno | Formato estruturado e descrição dos campos |
| Erro | Formato de retorno em caso de falha; não deve inventar resultados |

## 3. Ferramentas relacionadas ao conjunto de especificações

1. Tipo de recuperação de documentação: retorna o conteúdo da especificação por código de idioma + identificador (para os identificadores, ver a [especificação de metadados legíveis por máquina](./machine-readable-metadata-specification.md)).
2. Tipo de inventário: retorna a lista de documentos disponíveis e seu mapeamento de idiomas.
3. Tipo de validação: verifica a integridade da matriz de documentação (ver [matriz de documentação](./document-matrix.md)) e o estado dos portões (ver [portão de qualidade](./quality-gate.md)).

## 4. Regras obrigatórias

1. A ferramenta não deve retornar como PASS um resultado que não possa ser verificado; deve marcar SKIP com o motivo (ver [práticas proibidas](./prohibited-practices.md)).
2. A saída deve ser analisável por programa e não deve conter o processo de raciocínio interno.
3. O conteúdo relacionado à segurança não deve ser exposto por meio das ferramentas (ver [especificação de segurança e privacidade](./security-and-privacy-specification.md)).

## Arquivos relacionados

- Para a estrutura dos metadados, ver a [especificação de metadados legíveis por máquina](./machine-readable-metadata-specification.md)
- Para o encapsulamento de Skill, ver a [especificação de redação de Skill](./skill-authoring-specification.md)
- Para as convenções de invocação de Agent, ver a [especificação de invocação de Agent e de prompts](./agent-invocation-and-prompt-specification.md)
