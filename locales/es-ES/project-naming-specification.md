# Especificación de nombres de proyecto

> Problema que resuelve este archivo: define las reglas obligatorias de caracteres, uso de mayúsculas y minúsculas, segmentación, longitud y semántica del nombre del repositorio, así como la fórmula de nomenclatura, los sufijos convencionales, el proceso de búsqueda y los requisitos de metadatos asociados.

## 1. Reglas obligatorias

| Regla | Requisito | Contraejemplo |
|---|---|---|
| Conjunto de caracteres | Solo `a-z`, `0-9`, `-` | `My_Proj`, `我的项目` |
| Mayúsculas y minúsculas | Todo en minúsculas | `MyProject` |
| Segmentación | kebab-case, unido con `-` | `myproject`, `my_project` |
| Longitud | 2–25 caracteres | Nombres concatenados demasiado largos |
| Terminación | Sustantivo o cierre con sufijo de forma | Terminar en `-project` o `-test` |
| Versión | Sin número de versión, año ni fecha | `tool-v2`, `app2024` |
| Palabras sin información | Se prohíben `my`/`demo`/`test`/`new`/`tmp` | `my-new-demo` |
| Unicidad | Una búsqueda en GitHub / npm / PyPI respectivamente | Coincidir con una biblioteca conocida |
| Semántica | El nombre por sí mismo permite leer «qué hace» | `xyz`, `abc123` |

## 2. Fórmula de nomenclatura (elegir una de cuatro)

```text
<技术>-<对象>          vue-virtual-table      go-ratelimit
<对象>-<形态>          note-cli   image-api   config-loader
<动词>-<对象>          parse-markdown   sync-dotfiles
<领域>-<子领域>        web-ui-kit   data-pipeline
```

## 3. Sufijos convencionales

`-cli` línea de comandos / `-sdk` biblioteca de cliente / `-api` `-server` lado servidor / `-template` `-boilerplate` andamiaje / `-loader` `-parser` middleware / `-kit` conjunto de componentes / `-notes` `-guide` documentación / `dotfiles` repositorio de configuración / `awesome-xxx` colección de recursos.

## 4. Proceso de nomenclatura

1. Escribir en una frase «a quién resuelve qué problema el proyecto».
2. Extraer de esa frase el sustantivo central + la forma y aplicar cualquiera de las fórmulas de la sección 2.
3. Generar 3 candidatos y realizar la búsqueda de duplicados para cada uno.
4. Elegir el que pueda entenderse mejor sin leer el README.
5. El nombre en chino no se escribe en el nombre del repositorio, sino tras el título de la primera línea del README.

## 5. Metadatos asociados

### 5.1 Descripción del repositorio (description)

- Tiene el mismo origen que el nombre del repositorio; estructura: `<qué hace> for <para quién>`.
- Formato combinado bilingüe: `idioma nacional | inglés`, escribiendo primero la versión en el idioma nacional, seguida de una barra vertical de ancho medio (con un espacio a cada lado) y luego la versión en inglés. Ejemplo de un proyecto en chino:

```text
轻量级 Go 命令行 JSON 处理工具 | A lightweight Go CLI for JSON processing
```

- Longitud: el idioma nacional y el inglés no deben superar los 120 caracteres cada uno, y el total bilingüe no debe superar los 350 caracteres (límite de GitHub).
- Criterio de selección cuando el total bilingüe excede el límite: se comprime prioritariamente la versión en inglés y no la versión en el idioma nacional, ya que el chino tiene mayor densidad de información y comprimir el chino supone una mayor pérdida de información; al comprimir, se eliminan primero los modificadores y las limitaciones repetidas, se combinan después las expresiones sinónimas y se conserva finalmente la estructura completa de sujeto y predicado de cada versión lingüística.
- Sin saltos de línea, sintaxis Markdown ni Emoji; el estilo de puntuación final de ambos idiomas debe mantenerse coherente (con punto final en ambos o sin punto final en ambos).

### 5.2 Temas (topics)

- Completar los 20 (límite de GitHub), con cobertura completa y sin dejar espacios vacíos.
- Todos en inglés; no deben usarse el chino ni otros idiomas; todo en minúsculas, unido con `-`, sin espacios ni caracteres especiales.
- Cubrir de forma completa las cinco categorías: lenguaje, dominio, forma, ecosistema y escenario; además pueden añadirse términos genéricos como documentation u open-source.
- Establecerlos en el momento de crear el repositorio, sin dejarlos vacíos; revisarlos una vez tras el cambio de nombre o el reposicionamiento del repositorio.

## Archivos relacionados

- El cumplimiento de nomenclatura pertenece a la regla absoluta H1; véanse las [reglas absolutas](./hard-rules.md)
- La revisión de metadatos pertenece a la dimensión D10; véase la [matriz de dimensiones de revisión](./review-dimension-matrix.md)
- El documento que lo desarrolla es `docs/naming.md`; véase la [matriz de documentación](./document-matrix.md)
