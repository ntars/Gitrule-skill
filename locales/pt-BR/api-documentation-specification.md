# Especificação de documentação de API

> Problema que este arquivo resolve: definir a estrutura e os campos de uma documentação de referência de API completa, como base para a redação de docs/api.md, mantendo-a estritamente separada do conteúdo do tipo tutorial.

## 1. Estrutura obrigatória

Cada item de API deve conter:

| Campo | Requisito |
| --- | --- |
| Assinatura da interface | Método, caminho ou protótipo de função, completo e copiável |
| Parâmetros | Nome, tipo, obrigatoriedade, valor padrão, faixa de valores, descrição |
| Valor de retorno | Tipo e descrição da estrutura |
| Códigos de erro | Código de erro, condição de disparo, forma de tratamento |
| Exemplo de chamada | Exemplo mínimo executável, com indicação da linguagem |
| Limitação de taxa e cota | Limite de frequência de chamadas, cota, tratamento de excesso |

## 2. Regras obrigatórias

1. Parâmetros e valores de retorno devem indicar tipo e restrições; os valores padrão não devem ser omitidos.
2. Os códigos de erro devem ser listados integralmente; não deve ser escrito apenas “pode gerar erro”.
3. Os blocos de código devem indicar a linguagem e os exemplos devem ser executáveis de forma independente.
4. Este arquivo contém apenas informações de referência; não são escritos tutoriais, contextos ou explicações de design (para tutoriais e contexto, ver [especificação de seções do README](./readme-sections-specification.md)).

## 3. Requisitos de consistência

As assinaturas de interface na documentação de API devem ser consistentes com a implementação real do código; a nomenclatura dos parâmetros deve atender aos requisitos de precisão da [especificação geral de redação](./general-writing-specification.md); para os termos, ver o [glossário](./glossary.md).

## Arquivos relacionados

- Para os limites de responsabilidade da documentação, ver a [matriz de documentação](./document-matrix.md)
- Para a especificação de design de API (como projetar interfaces), ver a [especificação de design de API](./api-design-specification.md)
- A qualidade da documentação pertence à dimensão D12; ver a [matriz de dimensões de revisão](./review-dimension-matrix.md)
