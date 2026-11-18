# Especificación de registro de cambios

> Problema que resuelve este archivo: define la plantilla de registro de cambios de versión orientada al usuario, sus campos y su redacción, para garantizar que cada cambio sea trazable, que las versiones se correspondan y que la ruta de actualización pueda determinarse.

## 1. Artículos de la especificación

1. El registro de cambios sigue la estructura de Keep a Changelog y el número de versión sigue el versionado semántico de la [especificación de gestión de versiones](./version-management-specification.md).
2. Cada versión debe tener fecha de publicación, con el formato `YYYY-MM-DD`; el contenido no publicado se coloca en la sección `Unreleased`.
3. Las entradas se agrupan en seis categorías: `Added` (nuevo) / `Changed` (cambio) / `Deprecated` (obsoleto) / `Removed` (eliminado) / `Fixed` (corregido) / `Security` (seguridad).
4. Cada cambio está orientado al usuario y debe explicar el impacto y la forma de migración; no se escriben detalles de refactorización interna.
5. Los cambios disruptivos deben marcarse con `BREAKING CHANGE:` e incluir los pasos de migración (véase la [especificación de guía de migración](./migration-guide-specification.md)).
6. El número de versión debe coincidir con la etiqueta y las Release Notes; los cambios disruptivos deben corresponderse con `feat!:` o `BREAKING CHANGE:` en el mensaje de commit.

## 2. Plantilla de registro de cambios

```markdown
# Registro de cambios

Este archivo registra todos los cambios orientados al usuario. El formato se basa en Keep a Changelog y las versiones siguen el versionado semántico.

## [Unreleased]

### Added
- {{新增能力，说明对使用者的价值}}

### Changed
- {{行为变更，说明影响范围}}

### Deprecated
- {{即将移除的能力，说明替代方案与移除版本}}

### Removed
- {{已移除的能力，说明迁移路径}}

### Fixed
- {{缺陷修复，说明触发条件}}

### Security
- {{安全修复，说明影响与升级建议}}

## [{{X.Y.Z}}] - {{YYYY-MM-DD}}

### {{类型}}
- {{变更条目}}
- {{BREAKING CHANGE: 原行为 → 新行为；迁移步骤见链接}}

[Unreleased]: https://github.com/{{owner}}/{{repo}}/compare/v{{X.Y.Z}}...HEAD
[{{X.Y.Z}}]: https://github.com/{{owner}}/{{repo}}/compare/v{{prev}}...v{{X.Y.Z}}
```

## 3. Plantilla de entrada

```markdown
- {{动词开头的一句话变更描述}}（{{关联 REQ 编号}}）
  - Impacto: {{哪些使用者或场景受影响}}
  - Migración: {{需要执行的动作；无则省略此行}}
  - Referencia: {{Issue / PR 链接}}
```

## 4. Definición de campos

| Campo | Obligatorio | Tipo | Puntos clave de cumplimentación | Ejemplo |
| --- | --- | --- | --- | --- |
| Número de versión | Sí | `X.Y.Z` | Idéntico a la etiqueta; puede omitirse el prefijo `v`, pero debe ser uniforme en todo el documento | `1.2.0` |
| Fecha de publicación | Sí | `YYYY-MM-DD` | Se toma la fecha en que se creó la etiqueta | `2026-11-18` |
| Tipo de grupo | Sí | Enumeración | Una de las seis categorías; si no hay entradas de una categoría, se omite la sección completa | `Fixed` |
| Descripción del cambio | Sí | Texto | Comienza con un verbo, orientada al usuario, explica el valor | `新增对 GFM 表格的检查` |
| Impacto | Obligatorio condicional | Texto | Obligatorio en cambios de comportamiento, obsolescencias, eliminaciones y cambios disruptivos | `旧配置文件需重命名` |
| Migración | Obligatorio condicional | Texto | Obligatorio en cambios disruptivos; apunta a la guía de migración | `见迁移指南 v1.0` |
| BREAKING CHANGE | Obligatorio condicional | Marca | Obligatorio en cambios disruptivos; se coloca al inicio de la entrada | `BREAKING CHANGE:` |
| Enlace de comparación | Sí | URL | Cada sección de versión debe ofrecer un enlace compare | `compare/v1.1.0...v1.2.0` |
| REQ asociado | No | Lista | Facilita el cotejo con la matriz de trazabilidad de requisitos | `REQ-007` |

## 5. Instrucciones de cumplimentación

1. **Granularidad de las entradas**: una entrada describe un resultado perceptible por el usuario; si hay varios resultados, se dividen en varias entradas.
2. **Comenzar con un verbo**: se emplean «añadir», «admitir», «corregir», «eliminar», «marcar como obsoleto», «ajustar»; no se emplean «se ha actualizado» ni «se han hecho algunos cambios».
3. **Contenido prohibido**: entradas sin fecha, refactorizaciones internas, planes de desarrollo, contenido de la hoja de ruta y formulaciones vagas («mejorar la experiencia», «corregir varios problemas»).
4. **Cambios disruptivos**: deben reunir simultáneamente la marca `BREAKING CHANGE:`, la descripción del impacto, los pasos de migración y el enlace a la guía de migración; no puede faltar ninguno de los cuatro.
5. **Elementos obsoletos**: debe indicarse la alternativa y el número de versión en que se prevé la eliminación, por ejemplo «se eliminará en la v2.0».
6. **Unreleased**: se registra inmediatamente después de la fusión; no se acumula para redactarlo el día de la publicación.
7. **Coherencia**: el número de versión y la fecha de publicación deben coincidir en la etiqueta, las Release Notes y el registro de despliegue; si no coinciden, prevalece la etiqueta y se corrigen los otros tres puntos.

Errores frecuentes:

| Redacción errónea | Problema | Corrección |
| --- | --- | --- |
| «Reestructurar los módulos internos» | Es un detalle interno, imperceptible para el usuario | Eliminarlo o reescribirlo como un efecto perceptible |
| «Corregir varios problemas» | No es verificable | Enumerar uno por uno los contenidos corregidos |
| Un cambio disruptivo que solo dice «hay cambios» | Sin ruta de migración | Añadir impacto, pasos de migración y enlace a la guía |
| Número de versión distinto de la etiqueta | Se rompe la correspondencia entre versiones | Unificar tomando la etiqueta como referencia |
| Sin enlace compare | No es posible consultar las diferencias | Añadir la URL compare de GitHub |

## 6. Ejemplo completo

```markdown
## [1.0.0] - 2026-11-20

### Added
- Se añade la regla de comprobación de espacios en la mezcla de chino e inglés (REQ-001), invocable directamente desde la línea de comandos.
- Se añade la salida de informes JSON, para facilitar la integración en las estadísticas de CI.

### Changed
- BREAKING CHANGE: el nombre del archivo de configuración pasa de `.mdlint.json` a `.mdlintrc.json`. El archivo antiguo deja de leerse; los pasos de migración figuran en la [guía de migración](./migration-guide-specification.md).

### Deprecated
- El parámetro `--format=table` se eliminará en la v2.0; utilice `--reporter=table` en su lugar.

### Fixed
- Se corrige el falso positivo producido cuando la puntuación china queda junto a una palabra inglesa.

### Security
- Se corrige el problema por el que la ruta de carga de los plugins de reglas podía ser sobrescrita por entradas externas; se recomienda a todos los usuarios actualizar a la v1.0.0.

[1.0.0]: https://github.com/example/markdown-lint-cli/compare/v0.9.3...v1.0.0
```

## Archivos relacionados

- Reglas de incremento de versión: [especificación de gestión de versiones](./version-management-specification.md)
- Documentación de migración para cambios disruptivos: [especificación de guía de migración](./migration-guide-specification.md)
- Límites de responsabilidad documental: [matriz de documentación](./document-matrix.md)
- Marca de cambio disruptivo en el mensaje de commit: [especificación de mensajes de commit](./commit-message-specification.md)
- Sección de historial de cambios del README: [especificación de secciones del README](./readme-sections-specification.md)
- Etiquetas y Release Notes: [especificación de push y publicación](./push-and-release-specification.md)
