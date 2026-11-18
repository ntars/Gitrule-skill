# Especificación de metadatos legibles por máquina

> Problema que resuelve este archivo: define la estructura del listado de metadatos que consumen de forma programática expertos, Skills, MCP, la línea de comandos y otros, con el fin de garantizar un acceso automático estable y descubrible.

## 1. Objetivos de diseño

1. Identificadores estables: cada documento dispone de un identificador único e invariable para su referencia programática.
2. Independencia del idioma: el identificador no cambia con el idioma; el idioma solo se refleja en la ruta.
3. Descubribilidad: el listado enumera el tipo, la ruta, el idioma y el resumen de todos los documentos.

## 2. Estructura del listado

El listado automático (manifest) debe contener:

| Campo | Requisito |
| --- | --- |
| id | Identificador único y estable, kebab-case en minúsculas, sin idioma ni versión |
| title | Título del documento |
| summary | Una frase que explique qué problema resuelve |
| domain | Dominio al que pertenece (uno de los siete dominios) |
| paths | Correspondencia de código de idioma a ruta relativa, por ejemplo `zh-CN`: `./locales/zh-CN/角色与职责.md` |
| version | Versión del conjunto de especificaciones |

## 3. Reglas obligatorias

1. Al añadir un idioma solo se añade la correspondencia en `paths`; no se modifica `id` ni las rutas de otros idiomas.
2. Al renombrar un documento debe mantenerse `id` sin cambios y actualizar solo `paths`.
3. El identificador y la ruta deben coincidir con los archivos reales; la integración continua valida la validez del listado.
4. Esta especificación proporciona un ejemplo de listado copiable; el proyecto de destino debe crear una instancia real del listado conforme a los campos de la sección 2 y asegurar que `paths` coincida con los archivos en disco.

## 4. Ejemplo de listado (copiable)

El ejemplo siguiente enumera tres entradas de documentos. El listado real debe cubrir todas las especificaciones del directorio de idioma de destino; `id` no varía con el idioma y `paths` añade correspondencias por código de idioma.

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

Al añadir un idioma, solo se añade la correspondencia en el `paths` de la entrada correspondiente, por ejemplo `"en-US": "./locales/en-US/role-and-responsibility.md"`; no debe modificarse `id`.

## Archivos relacionados

- Forma en que el Skill consume los metadatos: [Especificación de redacción de Skill](./skill-authoring-specification.md)
- Forma en que las herramientas MCP exponen la documentación: [Especificación de herramientas MCP](./mcp-tool-specification.md)
- Convenciones de invocación de Agent: [Especificación de invocación de Agent y de prompts](./agent-invocation-and-prompt-specification.md)
