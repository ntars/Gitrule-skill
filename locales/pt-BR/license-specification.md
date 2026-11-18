# Especificação de LICENSE

> Problema que este arquivo resolve: definir a marcação SPDX da licença do projeto, os requisitos do texto completo de LICENSE, a posição da linha de copyright e a explicação de múltiplas licenças, bem como a regra de não escrever nada sem confirmação.

## Regras de LICENSE

1. A licença do projeto deve ser declarada explicitamente no README por meio de um identificador SPDX, com o arquivo LICENSE correspondente fornecido.
2. O arquivo LICENSE deve conter o texto oficial integral em inglês da licença, sem supressão ou alteração de cláusulas.
3. A linha de copyright é colocada no início do arquivo ou na seção 19 do README; para o formato, ver a [especificação de seções do README](./readme-sections-specification.md).
4. Ao adotar licenciamento duplo ou múltiplas licenças, devem ser explicadas as condições de aplicação e a forma de escolha.
5. Quando a escolha da licença não tiver sido confirmada pelo usuário, ela não deve ser gravada diretamente na documentação; devem ser oferecidas apenas as opções candidatas e a explicação das diferenças.

## Arquivos relacionados

- A ausência de LICENSE bloqueia o push e constitui a regra absoluta H2; ver [regras absolutas](./hard-rules.md)
- Para a avaliação de compatibilidade de licenças de dependências, ver a [especificação de conformidade de código aberto](./open-source-compliance-specification.md)
- Para a declaração de terceiros em arquivo independente, ver a [especificação de NOTICE](./notice-specification.md)
- A exatidão da licença pertence aos portões G7/G8; ver [portão de qualidade](./quality-gate.md)
