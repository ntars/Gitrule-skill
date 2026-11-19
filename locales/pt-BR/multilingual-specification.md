# Especificação multilíngue

> Problema que este arquivo resolve: definir o layout de arquivos por diretório de código de idioma, a alternância de idioma, a consistência de tradução, a consistência de código e as regras de sincronização de alterações unilaterais.

## 1. Layout de diretórios

1. O `README.md` do diretório raiz do repositório assume apenas a página inicial do projeto e a navegação de idiomas, não contendo o corpo de especificações específicas.
2. As especificações específicas ficam dispostas de forma plana no diretório `locales/<language-code>/`, por exemplo `locales/zh-CN/角色与职责.md`.
3. Os códigos de idioma seguem o estilo BCP 47, por exemplo `zh-CN`, `en-US`, `ja-JP`, `ko-KR`; o código de idioma aparece apenas no nome do diretório e não é escrito no nome do arquivo.
4. **Os nomes de arquivo devem usar o próprio idioma**: diretórios em chinês usam nomes de arquivo em chinês (`角色与职责.md`), diretórios em inglês usam nomes de arquivo em inglês com letras minúsculas e hífens (`roles-and-responsibilities.md`), e o mesmo vale para os demais idiomas; é proibido manter nomes de arquivo em chinês em diretórios de outros idiomas.
5. Não se exige que os nomes de arquivo dos diretórios de cada idioma correspondam literalmente, mas deve haver mapeamento um a um: a mesma especificação deve ter o mesmo papel de conteúdo em todos os diretórios de idioma, e a relação de mapeamento deve ser registrada no campo `paths` do arquivo de inventário (ver [especificação de metadados legíveis por máquina](./machine-readable-metadata-specification.md)).
6. O chinês simplificado e o inglês são as versões concluídas inicialmente; os demais idiomas devem ser marcados como “pendente” ou “concluído” na tabela de idiomas do `README.md` raiz, e idiomas sem diretório criado não devem ter links vazios.
7. Para adicionar um idioma, basta criar o diretório correspondente e traduzir documento por documento, sem alterar os arquivos de idiomas existentes; os demais idiomas concluídos devem ser atualizados somente quando a revisão do idioma de origem exigir sincronização.

## 2. Alternância de idioma

1. O `README.md` de cada diretório de idioma deve oferecer, no topo, links de alternância de idioma.
2. Os links usam caminhos relativos ao diretório de idioma atual, por exemplo a forma escrita no diretório de chinês simplificado:
   `[English](../en-US/README.md) | [简体中文](./README.md)`.
3. O texto do link usa a autodenominação do idioma de destino, por exemplo `English`, `简体中文`, `日本語`; não devem ser usadas abreviações como `CN` ou `EN`.
4. Os links de alternância apontam apenas para diretórios de idioma já criados; diretórios de idioma não criados são indicados uniformemente pela tabela de idiomas do `README.md` raiz, sem deixar links quebrados no corpo do texto.

## 3. Consistência de tradução

1. A tradução deve ser integral: o número de seções, a ordem das seções, o número de colunas das tabelas e o número de blocos de código devem ser idênticos aos do idioma de origem; não devem ser entregues produtos resumidos nem traduções automáticas não revisadas.
2. Comandos, caminhos, nomes de chaves de configuração, nomes de marcadores de posição e valores de parâmetros dentro de blocos de código permanecem inalterados; apenas comentários e textos explicativos são traduzidos. Por exemplo, em um bloco de árvore de diretórios como `├── SKILL.md   obrigatório: metadados + fluxo principal`, os símbolos de ramificação e os caminhos permanecem iguais, enquanto a descrição seguinte deve ser traduzida.
3. **Os campos de modelo voltados ao usuário devem ser localizados**: na configuração `yaml` dos formulários de Issue, `name`, `label`, `description`, `placeholder` e as opções de lista suspensa são exibidos diretamente na página web do GitHub e devem ser traduzidos para o idioma de destino; campos estruturais como `type`, `id`, `labels`, `required` e `render` permanecem em inglês. O critério de distinção é “se o item será exibido a uma pessoa”, e não “se ele está dentro de um bloco de código”. Da mesma forma, o corpo de modelos copiáveis dentro de blocos `markdown` deve ser integralmente traduzido.
4. Os termos devem seguir uniformemente a tabela de correspondência chinês-inglês de [coleta de informações e modelos](./information-collection-and-templates.md); um mesmo conceito deve usar o mesmo conjunto de correspondências em todos os idiomas.
5. Qualquer alteração unilateral deve ser sincronizada com todos os idiomas concluídos, registrando no registro de alterações os códigos de idioma e as versões sincronizadas; a revisão não deve ser considerada concluída sem a sincronização.
6. A verificação de consistência pertence ao portão G10, ver [portão de qualidade](./quality-gate.md).

## 4. Textos legais

1. O NOTICE fornece por padrão a versão em chinês; os textos legais que envolvem o texto original da licença, a declaração de direitos autorais e a isenção de responsabilidade mantêm o texto original em inglês, sem tradução e sem reescrita.
2. Textos legais que exigem versão bilíngue chinês-inglês devem apresentar o original e a tradução lado a lado, indicando “a tradução é apenas para referência; prevalece o original”.
3. Para o tratamento do idioma dos textos legais, ver a [especificação de NOTICE](./notice-specification.md) e a [isenção de responsabilidade](./disclaimer.md).

## Arquivos relacionados

- Navegação de idiomas da raiz: [página inicial do repositório](../../README.md)
- Inventário de idiomas e identificadores estáveis: [especificação de metadados legíveis por máquina](./machine-readable-metadata-specification.md)
- Base do número e da ordem das seções: as 20 seções da [especificação de seções do README](./readme-sections-specification.md)
- Modelo da tabela de correspondência de termos: [coleta de informações e modelos](./information-collection-and-templates.md)
- Padrão de redação: [especificação geral de redação](./general-writing-specification.md)
- A sincronização bilíngue pertence ao portão G10, ver [portão de qualidade](./quality-gate.md)
