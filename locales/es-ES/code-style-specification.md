# Especificación de estilo de código

> Problema que resuelve este archivo: define la plantilla de configuración de estilo de código, la tabla de convenciones de nomenclatura, las reglas de comentarios y las instrucciones de cumplimentación, para reducir las discrepancias de estilo y mejorar la legibilidad y la eficiencia de la revisión.

## 1. Artículos de la especificación

1. Las reglas de estilo se rigen por herramientas automatizadas; la intervención manual se limita a lo que las herramientas no pueden cubrir.
2. La configuración de formato debe versionarse con el repositorio (por ejemplo, el archivo de configuración del formateador) para garantizar la coherencia entre entornos.
3. La CI debe integrar la comprobación de formato; si no pasa, no debe fusionarse (véase la [especificación de pruebas](./testing-specification.md)).
4. No deben usarse números mágicos ni constantes codificadas directamente; deben extraerse como constantes con nombre.
5. El fin de línea debe ser LF de forma uniforme y el archivo debe terminar con un salto de línea (corresponde a la dimensión D3, higiene del repositorio).

## 2. Plantilla de configuración de estilo

```markdown
# Convención de estilo de código: {{项目名称}}

Versión de la configuración: {{v1.0}} ｜ Lenguaje y versión aplicables: {{如 TypeScript 5.x}} ｜ Herramienta de formato: {{如 Prettier 3.x}}

## Reglas de formato (impuestas por la herramienta)
| Regla | Valor | Opción de configuración de la herramienta | ¿Negociable? |
| --- | --- | --- | --- |
| Indentación | {{2 空格 / 4 空格 / Tab}} | {{配置项名}} | No |
| Ancho de línea | {{100 字符}} | {{配置项名}} | No |
| Comillas | {{单引号 / 双引号}} | {{配置项名}} | No |
| Fin de línea | LF | `endOfLine: lf` | No |
| Salto de línea al final del archivo | Obligatorio | Valor predeterminado de la herramienta | No |
| Punto y coma | {{有 / 无}} | {{配置项名}} | No |

## Convenciones de nomenclatura (no imponibles por herramienta, revisión manual)
| Objeto | Regla | Ejemplo correcto | Ejemplo incorrecto |
| --- | --- | --- | --- |
| Variable | {{camelCase}} | `userName` | `UserName` |
| Constante | {{UPPER_SNAKE_CASE}} | `MAX_RETRY` | `maxRetry` |
| Función | {{动词开头 camelCase}} | `parseConfig` | `configParse` |
| Clase / Tipo | {{PascalCase}} | `ConfigLoader` | `config_loader` |
| Nombre de archivo | {{kebab-case}} | `config-loader.ts` | `ConfigLoader.ts` |
| Valor booleano | {{is/has/can 前缀}} | `isValid` | `valid` |
| Colección | {{复数名词}} | `items` | `itemList` |

## Reglas de comentarios
- Casos en los que el comentario es obligatorio: {{公开 API 的契约、非直观算法、绕开限制的临时方案}}
- Comentarios prohibidos: {{复述代码、无信息量、失效的旧注释、情绪化表述}}
- Idioma de los comentarios: {{与项目主语言一致}}
- Formato de TODO: `// TODO({{负责人}}): {{事项}} — {{计划版本}}`

## Organización de archivos
1. Orden de importaciones: {{标准库 → 第三方 → 本地模块，组内字典序}}
2. Orden de declaraciones: {{常量 → 类型 → 函数 → 导出}}
3. Límite de líneas por archivo: {{300 行，超出须拆分}}

## Lista de excepciones
| Escenario | Regla de excepción | Aprobador | Validez |
| --- | --- | --- | --- |
| {{如生成代码}} | {{不参与格式化}} | {{姓名}} | {{至 v2.0}} |
```

## 3. Definición de campos de configuración

| Campo | Obligatorio | Tipo | Puntos de cumplimentación | Ejemplo |
| --- | --- | --- | --- | --- |
| Versión de la configuración | Sí | Texto | Se incrementa cuando cambian las reglas de estilo | `v1.0` |
| Lenguaje y versión aplicables | Sí | Texto | Indicar la versión principal para evitar la deriva de reglas | `TypeScript 5.x` |
| Herramienta de formato | Sí | Texto | Coherente con la versión del lockfile | `Prettier 3.2` |
| Regla. Valor | Sí | Enumeración / Numérico | Debe ser único; se prohíbe «depende» | `2 espacios` |
| ¿Negociable? | Sí | Enumeración | No / Sí; si se marca «Sí» deben indicarse las condiciones de negociación | `No` |
| Ejemplo correcto de nomenclatura | Sí | Código | Tomado del código existente del proyecto | `parseConfig` |
| Ejemplo incorrecto de nomenclatura | Sí | Código | Debe ser una forma realmente propensa al error | `configParse` |
| Responsable del TODO | Sí | Texto | Se prohíbe escribir «equipo» | `Zhang San` |
| Validez de la excepción | Sí | Versión / Fecha | Debe revisarse al vencer | `Hasta v2.0` |

## 4. Instrucciones de cumplimentación

1. **Prioridad de la herramienta**: toda regla que una herramienta pueda imponer debe escribirse en la configuración de formato y no confiarse a la memoria humana; la intervención manual se limita a nomenclatura, comentarios y organización de archivos.
2. **Valor del ancho de línea**: debe fijarse teniendo en cuenta la anchura de la interfaz de revisión, habitualmente 100 o 120; una vez determinado, no debe sobrescribirse en archivos concretos.
3. **Ejemplo correcto de nomenclatura**: debe tomarse un nombre realmente existente en el código del proyecto; se prohíben marcadores de posición de manual.
4. **Nomenclatura booleana**: los prefijos `is`/`has`/`can` deben ser coherentes con la semántica; `isReady` no debe expresar una acción.
5. **TODO**: debe incluir responsable, asunto y versión planificada; ningún TODO sin plan debe llegar a la rama principal.
6. **Lista de excepciones**: cada excepción debe tener aprobador y periodo de validez; si vence sin revisión, queda automáticamente sin efecto.

Errores frecuentes:

| Redacción incorrecta | Problema | Forma de corrección |
| --- | --- | --- |
| «Que el código sea lo más conciso posible» | No verificable | Convertir en una regla comprobable, como un límite de longitud de función |
| Tabla de nomenclatura con reglas pero sin ejemplos incorrectos | Imposible contrastar en la revisión | Añadir ejemplos incorrectos reales y frecuentes |
| Comentario «aquí había un bug» | Sin información y propenso a quedar obsoleto | Explicar el comportamiento actual y su motivo |
| TODO sin responsable | Nadie lo da seguimiento | Añadir responsable y versión planificada |
| Excepción sin periodo de validez | Exención permanente | Añadir periodo de validez y revisor |

## 5. Ejemplo completo

```markdown
# Convención de estilo de código: markdown-lint-cli

Versión de la configuración: v1.0 ｜ Lenguaje y versión aplicables: TypeScript 5.x ｜ Herramienta de formato: Prettier 3.2

## Reglas de formato (impuestas por la herramienta)
| Regla | Valor | Opción de configuración de la herramienta | ¿Negociable? |
| --- | --- | --- | --- |
| Indentación | 2 espacios | `tabWidth: 2` | No |
| Ancho de línea | 100 caracteres | `printWidth: 100` | No |
| Comillas | Simples | `singleQuote: true` | No |
| Fin de línea | LF | `endOfLine: lf` | No |
| Punto y coma | Sí | `semi: true` | No |

## Convenciones de nomenclatura (revisión manual)
| Objeto | Regla | Ejemplo correcto | Ejemplo incorrecto |
| --- | --- | --- | --- |
| Función | camelCase con verbo inicial | `parseRules` | `rulesParser` |
| Constante | UPPER_SNAKE_CASE | `DEFAULT_RULES` | `defaultRules` |
| Nombre de archivo | kebab-case | `rule-loader.ts` | `RuleLoader.ts` |

## Reglas de comentarios
- Casos en los que el comentario es obligatorio: la semántica de coincidencia de las reglas y el tratamiento alternativo del comportamiento de la API upstream.
- Comentarios prohibidos: repetir el código, «se corrigió un bug», TODO sin responsable.
- Formato de TODO: `// TODO(Wang Wu): sustituir el analizador temporal — v2.0`

## Lista de excepciones
| Escenario | Regla de excepción | Aprobador | Validez |
| --- | --- | --- | --- |
| Directorio fixtures | No participa en el formato | Li Si | Hasta v2.0 |
```

## Archivos relacionados

- Base de las comprobaciones de revisión de código: [especificación de revisión de código](./code-review-specification.md)
- La comprobación de formato se ejecuta en la CI: [especificación de pruebas](./testing-specification.md), [especificación de flujo de trabajo de CI](./ci-workflow-specification.md)
- La higiene del repositorio pertenece a la dimensión D3: [matriz de dimensiones de revisión](./review-dimension-matrix.md)
- Comprobaciones previas al push: [especificación de push y publicación](./push-and-release-specification.md)
- Trazabilidad de requisitos a implementación: [especificación de la matriz de trazabilidad de requisitos](./requirements-traceability-matrix-specification.md)
