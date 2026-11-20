# Especificação de conformidade de código aberto

> Problema que este arquivo resolve: definir o escopo de coleta da conformidade de código aberto, os campos da lista de dependências, os métodos de coleta, o julgamento de compatibilidade de licenças, a marcação de modificações e as regras de citação de materiais, garantindo declarações completas e verificáveis.

## 1. Escopo de coleta

Deve cobrir quatro tipos de origem: dependências diretas, dependências indiretas e transitivas, cadeia de ferramentas de compilação e desenvolvimento, e materiais e recursos (ícones, fontes, imagens, áudio, conjuntos de dados, origem de algoritmos).

## 2. Campos da lista de dependências

| Campo | Requisito |
| --- | --- |
| Nome do componente | Idêntico ao repositório oficial |
| Versão | Versão efetivamente travada, não expressão de intervalo |
| Forma de referência | Dependência direta ou dependência indireta |
| Titular dos direitos autorais | Nome completo do titular declarado oficialmente |
| Licença | Identificador SPDX; em caso de múltiplas licenças, indicar a forma de combinação |
| Endereço oficial | URL completa do repositório ou da página inicial |
| Uso neste projeto | Local concreto de chamada ou funcionalidade |
| Houve modificação | Sim ou não |
| Descrição da modificação | Arquivo modificado, conteúdo da modificação, motivo; se não houver modificação, preencher “nenhuma” |
| Local do texto original da licença | Caminho dentro do projeto ou link para o arquivo |

O modelo de tabela da lista de dependências está em [coleta de informações e modelos](./information-collection-and-templates.md).

## 3. Métodos de coleta

Conforme a stack tecnológica, usar o comando correspondente para gerar a árvore de dependências e depois completar item a item as informações de licença e direitos autorais: `npm ls --all`, `pip freeze`, `go mod graph`, `cargo tree`, `mvn dependency:tree`, `gradle dependencies`, `composer show --tree`. Para a varredura de licenças podem ser usadas ferramentas como `license-checker`, `pip-licenses` e `cargo-license`; o resultado da varredura deve ser revisado manualmente, e a saída da ferramenta não deve ser usada diretamente como conclusão final.

## 4. Compatibilidade de licenças

1. Deve-se julgar a compatibilidade entre a licença do projeto e a licença de cada dependência, verificando com atenção o alcance da contagiosidade de GPL, AGPL, LGPL e MPL.
2. Para dependências Apache-2.0, deve-se confirmar se os requisitos do arquivo NOTICE já foram atendidos.
3. Licenças de materiais (como fontes SIL OFL e a série CC) devem ter seus requisitos de atribuição e disseminação verificados separadamente.
4. Quando não for possível determinar a compatibilidade, marcar «pendente de confirmação: compatibilidade de licença» e explicar o motivo da dúvida.
5. Quando o projeto adotar licenças em camadas, o julgamento deve ser feito camada por camada: uma dependência usada em determinada camada é avaliada pela licença dessa camada, e a licença principal não deve representar todo o repositório. A disposição e o processo de confirmação constam na [especificação de LICENSE](./license-specification.md).
6. Quando uma mesma dependência atravessar várias camadas de licença, indicar seu escopo real de uso e decidir pela camada aplicável mais rigorosa.

## 5. Marcação de modificações em código de terceiros

1. Manter no cabeçalho do arquivo a declaração original de direitos autorais e a declaração de licença.
2. Listar no NOTICE o caminho do arquivo modificado, um resumo do conteúdo modificado e a data da modificação.
3. Explicar de forma sincronizada na seção correspondente do README.

## 6. Citação e materiais

1. Ao citar documentação ou trechos de código de terceiros, indicar o endereço de origem, o autor e a licença.
2. Imagens, ícones e fontes devem ter origem e licença registradas; quando faltarem, marcar como pendente de confirmação, sem uso direto.
3. Não devem ser usados materiais de origem desconhecida.

## Arquivos relacionados

- Conversão da lista de dependências em NOTICE, ver a [especificação de NOTICE](./notice-specification.md)
- Escolha da licença e requisitos do texto integral, ver a [especificação de LICENSE](./license-specification.md)
- A veracidade das dependências e dos direitos autorais pertence aos portões G6–G9 e G13, ver o [portão de qualidade](./quality-gate.md)
