# Especificação de selos

> Problema que este arquivo resolve: definir a sintaxe de URL, os parâmetros de estilo, a codificação de cores, a seleção de informações, a ordem de disposição e o controle de quantidade dos selos (Badge) no README, tendo o Shields.io como implementação principal, e apresentar exemplos de formato prontos para copiar e configurações de parâmetros recomendadas.

Os parâmetros descritos neste arquivo foram verificados na documentação oficial do Shields.io (páginas Static Badge e Logos, e a descrição do formato badge-maker); os dados de frequência de uso provêm de uma amostragem de READMEs de projetos líderes de código aberto realizada por este projeto, identificada como “medição própria”.

## 1. Sintaxe básica

### 1.1 Estrutura de URL de selo estático

Os selos estáticos recebem parâmetros pelo caminho da URL, com a seguinte estrutura padrão:

```text
https://img.shields.io/badge/<rótulo>-<mensagem>-<cor>?style=<estilo>&<outros parâmetros de consulta>
```

Os três segmentos do caminho são separados por hífen `-`:

| Segmento | Nome | Obrigatório | Descrição |
| --- | --- | --- | --- |
| 1º segmento | Rótulo (label) | Não | Texto da esquerda, que indica o nome do indicador |
| 2º segmento | Mensagem (message) | Sim | Texto da direita, que exibe o valor do indicador |
| 3º segmento | Cor (color) | Sim | Cor de fundo do lado direito |

A forma de dois segmentos (omitindo o rótulo, com apenas mensagem e cor) também é válida:

```text
https://img.shields.io/badge/<mensagem>-<cor>
```

### 1.2 Regras de escape de caracteres

Espaços e caracteres especiais no caminho da URL devem ser escapados, conforme as regras abaixo:

| Caractere de entrada | Forma na URL | Exemplo |
| --- | --- | --- |
| Espaço | `_` ou `%20` | `v0.1 prototype` → `v0.1%20prototype` |
| Sublinhado `_` | `__` (sublinhado duplo) | `my_label` → `my__label` |
| Hífen `-` | `--` (hífen duplo) | `dev-build` → `dev--build` |

O exemplo de protótipo fornecido pelo usuário está em conformidade com essa sintaxe e pode ser usado diretamente:

```markdown
![Status](https://img.shields.io/badge/status-v0.1%20prototype-8957e5?style=flat-square)
```

Seu significado é: rótulo `status`, mensagem `v0.1 prototype` (espaço como `%20`), cor `8957e5` (roxo em hexadecimal) e estilo `flat-square`.

### 1.3 Formato de incorporação em Markdown

```markdown
![versão](https://img.shields.io/badge/version-1.2.0-blue?style=flat-square)
```

Quando for necessário permitir o clique, envolver a imagem em um link:

```markdown
[![licença](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
```

## 2. Parâmetro de estilo (style)

O `style` determina o design visual geral do selo, aceita cinco valores e tem `flat` como padrão.

| Valor | Característica visual | Cenário adequado | Ocorrências medidas (N=120) |
| --- | --- | --- | --- |
| `flat` | Cantos retos, plano, padrão do Shields.io | Escolha geral, compatível com a maioria dos temas | 32 |
| `flat-square` | Cantos retos, sem arredondamento, um pouco mais compacto | Páginas iniciais que buscam regularidade e sobriedade | 60 |
| `for-the-badge` | Grande, em negrito, alto contraste | Destaque visual no topo, selos de ênfase | 65 |
| `social` | Cantos arredondados, dois tons, plano | Páginas iniciais com estilo social | 12 |
| `plastic` | Brilho em gradiente, efeito skeuomórfico | Estilo retrô, hoje pouco usado | 1 |

**Configuração recomendada**:

- Todos os selos de um mesmo README devem usar o mesmo `style`; a mistura é proibida. Este é o requisito primordial de consistência visual.
- Projetos em geral devem preferir `flat` ou `flat-square`; quando for necessário reforçar a identidade na página inicial, usar `for-the-badge` de forma uniforme.
- Na medição própria, `for-the-badge` (65 ocorrências) e `flat-square` (60 ocorrências) foram os mais populares, e ambos podem ser a escolha padrão.

Exemplo de formato:

```markdown
![build](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)
![build](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)
```

## 3. Parâmetros de cor (color / labelColor)

### 3.1 Três formas de representação de cor

Conforme a descrição do badge-maker, `color` (lado direito) e `labelColor` (fundo do lado esquerdo) aceitam as três formas abaixo:

**Forma um: cores nomeadas do Shields.io**

| Semântica | Cores nomeadas |
| --- | --- |
| Sucesso | `brightgreen`, `green`, `success` |
| Informação | `yellow`, `yellowgreen`, `orange`, `important` |
| Alerta | `red`, `critical` |
| Informativo | `blue`, `informational` |
| Neutro | `grey` / `gray`, `lightgrey` / `lightgray`, `inactive` |

Atenção: o valor padrão de `labelColor` é `grey` e o de `color` é `lightgrey` (a documentação observa ainda que `inactive` também é uma das cores padrão); alguns valores de cores nomeadas diferem ligeiramente das cores de mesmo nome em CSS, prevalecendo o resultado renderizado pelo Shields.io.

**Forma dois: cor hexadecimal**

Aceita hexadecimal de três ou seis dígitos, podendo omitir ou manter o prefixo `#`:

```text
?color=8957e5
?color=007fff
?color=%23007fff    ← 保留 # 时需编码为 %23
```

**Forma três: valor de cor CSS**

Aceita `rgb(...)`, `rgba(...)`, `hsl(...)`, `hsla(...)` e cores nomeadas em CSS (como `aqua`, `fuchsia`, `lightslategray`); o uso exige codificação de URL.

### 3.2 Mapeamento semântico de cores (configuração recomendada)

| Tipo de informação | Cor recomendada | Mensagem de exemplo |
| --- | --- | --- |
| Compilação aprovada, testes aprovados | `brightgreen` / `success` | `passing` |
| Compilação com falha | `red` / `critical` | `failing` |
| Versão estável | `blue` | `v1.2.0` |
| Pré-lançamento, protótipo | Roxo personalizado `8957e5` / `orange` | `v0.1 prototype` |
| Licença | `blue` / `green` | `MIT` |
| Estado da documentação | `yellowgreen` | `docs` |
| Descontinuado, sem manutenção | `red` / `inactive` | `deprecated` |

**Configuração recomendada**: definir um único conjunto de cores de marca e de estado por projeto, sem trocas casuais; a mesma semântica deve usar a mesma codificação de cor em todo o repositório.

Exemplo de formato:

```markdown
![cobertura](https://img.shields.io/badge/coverage-95%25-orange?style=flat-square)
![status](https://img.shields.io/badge/status-v0.1%20prototype-8957e5?style=flat-square)
![licença](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
```

## 4. Parâmetros de ícone (logo / logoColor / logoSize)

### 4.1 Uso de Simple Icons

O parâmetro `logo` recebe o slug do ícone em Simple Icons, no formato `?logo=<slug>`. Os slugs mais usados são:

| Uso | slug | Ocorrências medidas (N=120) |
| --- | --- | --- |
| Repositório GitHub | `github` | 35 |
| Comunidade Discord | `discord` | 20 |
| Pacote npm | `npm` | 4 |
| Plataformas Apple | `apple` | 3 |
| Docker | `docker` | 3 |
| Plataforma social X | `x` | 3 |
| Pacote Python | `pypi` | 2 |

A lista completa de slugs tem como referência o site Simple Icons ou o arquivo `slugs.md` do repositório simple-icons.

### 4.2 Cores e tamanho dos ícones

- `logoColor`: define a cor do ícone de Simple Icons e aceita hexadecimal, rgb, hsl e cores nomeadas em CSS; tem efeito apenas sobre ícones de Simple Icons, não sobre ícones personalizados.
- `logoSize`: quando definido como `auto`, o ícone é redimensionado conforme o conteúdo, o que é adequado para ícones mais largos; também tem efeito apenas sobre Simple Icons.

Exemplo de formato:

```markdown
![repo](https://img.shields.io/badge/github-repo-blue?logo=github)
![cor do logo](https://img.shields.io/badge/logo-javascript-blue?logo=javascript&logoColor=f5f5f5)
```

Ícones personalizados podem ser passados por `logo=data:image/svg+xml;base64,...`, mas a URL fica extremamente longa e de difícil manutenção, não sendo recomendado salvo em casos especiais.

## 5. Outros parâmetros de consulta

| Parâmetro | Função | Exemplo |
| --- | --- | --- |
| `label` | Substitui o texto padrão da esquerda (espaços devem ser codificados) | `?label=healthiness` |
| `labelColor` | Cor de fundo do lado esquerdo | `?labelColor=abcdef` |
| `color` | Cor de fundo do lado direito | `?color=fedcba` |
| `cacheSeconds` | Tempo de cache HTTP em segundos; valores abaixo do padrão são ignorados | `?cacheSeconds=3600` |
| `link` | Define o endereço de destino do clique nas metades esquerda e direita | Só tem efeito dentro da tag `<object>`; não funciona em imagens Markdown |

## 6. Selos dinâmicos

Os selos dinâmicos têm os dados obtidos em tempo real pelo Shields.io a partir de serviços externos, sem necessidade de atualização manual do valor. Tipos mais usados:

| Categoria | Padrão de URL | Uso |
| --- | --- | --- |
| Status de compilação | `https://img.shields.io/github/actions/workflow/status/<owner>/<repo>/<workflow>` | Status da CI |
| Versão | `https://img.shields.io/npm/v/<package>` | Última versão no npm |
| Licença | `https://img.shields.io/npm/l/<package>` | Licença do pacote |
| Número de stars | `https://img.shields.io/github/stars/<owner>/<repo>` | Popularidade |
| Número de issues | `https://img.shields.io/github/issues/<owner>/<repo>` | Questões em aberto |
| Downloads | `https://img.shields.io/npm/dt/<package>` | Total de downloads |

Aos selos dinâmicos podem ser acrescentados parâmetros como `?style=` e `?logo=`, com as mesmas regras dos selos estáticos. Projetos de referência costumam adotar a combinação “selos dinâmicos para indicadores reais + selos estáticos para estados personalizados”.

## 7. Seleção de informações e ordem de disposição

### 7.1 Seleção de informações

O selo deve transmitir informações de estado “verificáveis e úteis ao leitor”. Recomenda-se manter apenas as categorias abaixo:

1. estado de compilação / testes;
2. versão ou último lançamento;
3. licença;
4. estado da documentação;
5. canais da comunidade (Discord, fórum de discussão);
6. estado personalizado do projeto (protótipo, em manutenção, descontinuado).

Não devem ser incluídos: volume de downloads sem fonte, etiquetas de marketing sem relação com o projeto, pontuações não verificáveis e blocos de cor puramente decorativos.

### 7.2 Ordem de disposição

Recomenda-se a ordem “estado → versão → licença → plataforma/comunidade → estado personalizado”, com a importância decrescente da esquerda para a direita. Justificativa: o estado de compilação determina se o leitor vai adotar o projeto, a versão determina o julgamento de compatibilidade e a licença determina se pode ser usado; ambos são informações prévias à decisão.

### 7.3 Controle de quantidade

- Projetos comuns: 4–6 selos.
- Coletâneas de recursos ou projetos de ecossistema: pode-se ampliar para 8–10 selos.
- Todos os selos devem ficar após o nome do projeto e o posicionamento em uma frase e antes do corpo do texto, em uma linha própria ou em um contêiner centralizado, sem dispersão pelo texto.

### 7.4 Selo estático de estado de entrega

A implementação padrão do item 6 da seção 7.1 (“estado personalizado do projeto”) é o selo estático de estado de entrega, com valores atualizados manualmente pelo autor do projeto, adequado ao progresso de entrega e ao estado de manutenção sem fonte de dados externa:

```text
![Status](https://img.shields.io/badge/status-4%20of%204%20delivered-brightgreen?style=flat-square)
```

1. A estrutura padrão é `badge/<rótulo>-<mensagem>-<cor>`, com estilo uniforme `?style=flat-square`; o significado do exemplo é “4 de 4 entregáveis entregues”.
2. No texto da mensagem, espaços são escritos como `%20`, hífens como `--` e sublinhados como `__`; não deve haver quebras de linha nem outros caracteres especiais não escapados.
3. Convenção semântica de cores: `brightgreen` indica concluído, `yellow` indica em andamento, `red` indica bloqueado e `lightgrey` indica não iniciado.
4. Quando o valor mudar, o selo e o texto devem ser atualizados em conjunto; o selo não deve ficar por muito tempo defasado em relação ao estado real; quando não for possível garantir a sincronização, usar um selo dinâmico.
5. O texto `alt` deve explicitar o significado real, como `![estado de entrega]`; pode-se vincular à lista de entregáveis ou à seção de índice correspondente.

## 8. Acessibilidade e adaptação a temas

- O texto `alt` de cada selo deve explicitar o significado real, por exemplo `![estado da compilação]` em vez de `![badge]`.
- Em temas escuro e claro, pode-se alternar a origem da imagem do selo com `<picture>`; o uso de `for-the-badge` com `labelColor=000` mantém contraste estável nos dois temas.
- O selo deve permitir clique para a fonte de dados correspondente (estado de compilação leva à CI, versão leva à página do gerenciador de pacotes, licença leva ao arquivo LICENSE).

## Arquivos relacionados

- A que seção pertencem e a ordem, ver a [especificação de seções do README](./readme-sections-specification.md)
- Hierarquia visual e posicionamento, ver a [especificação de layout visual do README](./readme-visual-layout-specification.md)
- Recomendações diferenciadas de selos por tipo de projeto, ver o [guia de adaptação do README por categoria](./readme-category-adaptation-guide.md)
- Linhas completas de selos prontas para uso, ver o [modelo padrão de README](./readme-standard-template.md)
- Método de pesquisa e amostra medida, ver o [relatório de pesquisa sobre modelos de README](./readme-template-research-report.md)
