# Especificação de NOTICE

> Problema que este arquivo resolve: definir as sete partes que o arquivo NOTICE deve conter e os requisitos de consistência com o README, garantindo que a declaração de terceiros seja um arquivo independente e que as informações sejam exatas.

## 1. Arquivo independente

O NOTICE constitui um arquivo independente; não deve ser mesclado ao README nem substituído por uma lista no README. Deve conter as seguintes partes:

1. **Declaração do próprio projeto**: nome do projeto, titular dos direitos autorais, ano, licença, identificador SPDX.
2. **Lista de componentes de terceiros**: listar item a item conforme os campos da lista de dependências da [especificação de conformidade de código aberto](./open-source-compliance-specification.md).
3. **Apêndice do texto original das licenças**: quando a licença exigir o texto integral, anexar uma cópia do texto original para cada licença; o texto original permanece em inglês, sem tradução.
4. **Declaração de modificações**: locais e conteúdo das modificações em código de terceiros.
5. **Declaração de origem de materiais e dados**.
6. **Isenção de responsabilidade**: manter o texto original em inglês, podendo ser acompanhado de tradução para o chinês para fins de comparação.
7. **Itens pendentes de confirmação**: itens cuja licença ou titularidade de direitos autorais não possa ser verificada devem ser explicitamente marcados como “pendente de confirmação”.

## 2. Requisitos de consistência

As informações de componentes e licenças do NOTICE devem ser totalmente consistentes com as da seção 6 do README (stack tecnológica e lista de dependências), da seção 19 (copyright e licenciamento) e da seção 20 (declaração de conformidade de NOTICE); não deve haver divergência de versão, identificador de licença ou titular dos direitos autorais.

## Arquivos relacionados

- Para os campos da lista de dependências e o método de coleta, ver a [especificação de conformidade de código aberto](./open-source-compliance-specification.md)
- Para os requisitos do texto integral da licença, ver a [especificação de LICENSE](./license-specification.md)
- Para as seções relacionadas do README, ver a [especificação de seções do README](./readme-sections-specification.md)
- A consistência pertence aos portões G7–G9; ver [portão de qualidade](./quality-gate.md)
