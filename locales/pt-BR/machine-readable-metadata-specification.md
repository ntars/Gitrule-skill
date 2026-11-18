# Especificação de metadados legíveis por máquina

> Problema que este arquivo resolve: definir a estrutura do manifesto de metadados consumido programaticamente por especialistas, Skills, MCP, linha de comando e outros, garantindo que a máquina o obtenha de forma estável e detectável.

## 1. Objetivos de design

1. Identificador estável: cada documento tem um identificador único e imutável, para referência por programas.
2. Independência de idioma: o identificador não varia com o idioma; o idioma aparece apenas no caminho.
3. Detectabilidade: o manifesto lista o tipo, o caminho, o idioma e o resumo de todos os documentos.

## 2. Estrutura do manifesto

O manifesto legível por máquina (manifest) deve conter:

| Campo | Requisito |
| --- | --- |
| id | Identificador único e estável, em kebab-case minúsculo, sem idioma nem versão |
| title | Título do documento |
| summary | Uma frase que explique qual problema resolve |
| domain | Domínio ao qual pertence (um dos sete domínios) |
| paths | Mapeamento de código de idioma para caminho relativo, como `zh-CN`: `./locales/zh-CN/角色与职责.md` |
| version | Versão do conjunto de especificações |

## 3. Regras obrigatórias

1. Um novo idioma apenas acrescenta um mapeamento em `paths`, sem alterar o `id` nem os caminhos de outros idiomas.
2. Ao renomear um documento, o `id` deve permanecer inalterado e apenas `paths` deve ser atualizado.
3. O identificador e o caminho devem ser coerentes com os arquivos reais; a CI valida a validade do manifesto.
4. Esta especificação fornece um exemplo de manifesto copiável; o projeto-alvo deve criar a instância real do manifesto conforme os campos da seção 2 e garantir que `paths` corresponda aos arquivos em disco.

## 4. Exemplo de manifesto (copiável)

O exemplo a seguir lista três entradas de documento. O manifesto real deve cobrir todas as especificações do diretório de idioma-alvo; o `id` não varia com o idioma e `paths` acumula mapeamentos por código de idioma.

```json
{
  "version": "1.0.0",
  "entries": [
    {
      "id": "role-and-responsibility",
      "title": "角色与职责",
      "summary": "定义执行者身份、职责边界、触发条件、适用范围与硬性约束",
      "domain": "总纲与治理",
      "paths": {
        "zh-CN": "./locales/zh-CN/角色与职责.md"
      },
      "version": "1.0.0"
    },
    {
      "id": "readme-standard-template",
      "title": "README标准模板",
      "summary": "提供可直接套用的通用 README 模板与占位符对照表",
      "domain": "命名与文档",
      "paths": {
        "zh-CN": "./locales/zh-CN/README标准模板.md"
      },
      "version": "1.0.0"
    },
    {
      "id": "machine-readable-metadata",
      "title": "机器可读元数据规范",
      "summary": "定义供专家、Skill、MCP、命令行消费的元数据清单结构",
      "domain": "AI 与机器适配",
      "paths": {
        "zh-CN": "./locales/zh-CN/机器可读元数据规范.md"
      },
      "version": "1.0.0"
    }
  ]
}
```

Ao adicionar um idioma, acrescenta-se apenas o mapeamento em `paths` da entrada correspondente, por exemplo `"en-US": "./locales/en-US/role-and-responsibility.md"`; o `id` não deve ser modificado.

## Arquivos relacionados

- A forma como as Skills consomem metadados está na [especificação de autoria de Skill](./skill-authoring-specification.md)
- A forma como as ferramentas MCP expõem documentação está na [especificação de ferramentas MCP](./mcp-tool-specification.md)
- As convenções de invocação de Agent estão na [especificação de invocação de Agent e prompts](./agent-invocation-and-prompt-specification.md)
