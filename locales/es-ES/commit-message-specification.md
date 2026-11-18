# Especificación de mensajes de commit

> Problema que resuelve este archivo: define los campos, el formato, las instrucciones de cumplimentación y los ejemplos de Conventional Commits, garantizando un historial legible y la generación automática del registro de cambios y del número de versión.

## 1. Formato

```text
<类型>[可选作用域][可选 !]: <描述>

[可选正文]

[可选脚注]
```

## 2. Tipos

Los diez tipos completos son los siguientes y cubren los escenarios de commit habituales en proyectos open source:

| Tipo | Significado |
| --- | --- |
| `feat` | Nueva funcionalidad |
| `fix` | Corrección de defectos |
| `docs` | Cambios en la documentación |
| `style` | Ajustes de formato que no alteran la lógica (espacios en blanco, formateo, punto y coma ausente, etc.) |
| `refactor` | Refactorización que no añade funcionalidad ni corrige defectos |
| `perf` | Cambio de código para optimizar el rendimiento |
| `test` | Añadir pruebas que faltaban o corregir pruebas existentes |
| `build` | Cambios que afectan al sistema de compilación o a dependencias externas (por ejemplo npm, gulp) |
| `ci` | Cambios en la configuración y los scripts de integración continua (por ejemplo GitHub Actions, CircleCI) |
| `chore` | Tareas misceláneas de compilación, dependencias, cadena de herramientas, etc. |

### 2.1 Comparación y elección de las convenciones de equipo

En distintos modos de colaboración existen tres convenciones habituales; el proyecto debe elegir una en el inicio del proyecto y unificarla en todo el equipo:

| Convención | Formato | Adecuada para | Limitaciones |
| --- | --- | --- | --- |
| Convención de trabajo | `[n.º de tarjeta] autor: contenido de la modificación` | Equipos que usan tablero kanban y programación en pareja | Depende de un sistema de números de tarjeta de tarea; no aplica si no hay tarjeta |
| Convención habitual | `[categoría] componente (opcional): contenido de la modificación` | Equipos que necesitan filtrar el historial por módulo de negocio | Requiere una tabla de clasificación acordada por el equipo, con coste adicional |
| Convención open source | `<type>(<scope>): <subject>` | Bibliotecas y aplicaciones open source que necesitan generar CHANGELOG automáticamente | Muchos tipos y ámbitos, mayor coste de aprendizaje |

Este proyecto adopta de forma uniforme la convención open source (es decir, Conventional Commits) porque es legible por máquinas y permite generar automáticamente el registro de cambios y el número de versión. La convención de trabajo y la convención habitual solo se usan por acuerdo en equipos de código cerrado y no deben mezclarse en repositorios públicos.

## 3. Definición de campos

| Campo | Obligatorio | Tipo | Puntos clave | Ejemplo |
| --- | --- | --- | --- | --- |
| Tipo | Sí | Enumeración | Uno de los diez; no se puede inventar | `feat` |
| Ámbito | No | Texto | Nombre del módulo, palabra corta en minúsculas, sin espacios | `parser` |
| Marca de ruptura | No | `!` | Se coloca tras el tipo o el ámbito y antes de los dos puntos | `feat!:` |
| Descripción | Sí | Texto | Modo imperativo, inicio en minúsculas, ≤72 caracteres, sin punto final | `add TOML config support` |
| Cuerpo | No | Texto | Explica el motivo y la implementación; separado de la descripción por una línea en blanco | `Allow the parser to read TOML...` |
| Pie | No | Texto | `BREAKING CHANGE:` o `Refs: #N` | `BREAKING CHANGE: ...` |
| Requisito asociado | No | `REQ-NNN` | Se escribe en el cuerpo o en el pie para facilitar la trazabilidad | `Refs: REQ-001` |

## 4. Instrucciones de cumplimentación

1. **Descripción**: usar el modo imperativo (add, fix, remove) y escribir «qué se hizo» en lugar de «se realizaron modificaciones»; los proyectos en chino pueden escribir la descripción en chino, pero debe ser uniforme en todo el repositorio.
2. **Ámbito**: tomar el nombre del módulo, no el del archivo; en cambios que cruzan módulos se omite el ámbito y no se escribe `all` ni `global`.
3. **Cuerpo**: se escribe solo cuando la descripción no basta para explicar el motivo; no se repite la descripción ni se relata el proceso paso a paso.
4. **Cambios que rompen la compatibilidad**: `feat!:` / `fix!:` y el pie `BREAKING CHANGE:` se eligen entre sí o se combinan; cuando aparecen, deben registrarse sincrónicamente en la [Especificación del registro de cambios](./changelog-specification.md) y en la [Especificación de la guía de migración](./migration-guide-specification.md).
5. **Atomicidad**: un commit hace solo una cosa; el formateo y el cambio lógico se confirman en dos commits distintos.
6. **Seguridad**: no debe contener secretos, tokens, datos personales ni direcciones internas; antes de confirmar se verifica con un escaneo de secretos (véase [Especificación de seguridad y privacidad](./security-and-privacy-specification.md)).
7. **Vinculación con la versión**: `feat` provoca el incremento de la versión menor, `fix` el de la versión de revisión y `BREAKING CHANGE` el de la versión mayor; véase en detalle la [Especificación de gestión de versiones](./version-management-specification.md).

Errores frecuentes:

| Escritura errónea | Problema | Corrección |
| --- | --- | --- |
| `wip`, `update`, `fix bug` | Sin información útil, infringe H10 | Indicar el objeto y la acción |
| `feat: Added new feature.` | No es imperativo, empieza en mayúscula, lleva punto final | `feat: add config loader` |
| `feat(todos): optimizar` | Ámbito no válido, descripción vaga | Usar el nombre concreto del módulo y precisar el cambio |
| Un commit que mezcla formateo y cambio funcional | Rompe la atomicidad | Dividir en dos commits, `style:` y `feat:` |
| Mensaje de commit con direcciones de la intranet | Filtración de información | Eliminarlo y pasar el escaneo de secretos |

## 5. Ejemplos completos

```text
feat(parser): add support for TOML config

Allow the parser to read TOML configuration files in addition to YAML.
Refs: REQ-001

BREAKING CHANGE: the `config` option now accepts a file path instead of an object.
```

Significado de cada campo: `feat` es el tipo, `parser` el ámbito y lo que sigue a los dos puntos es la descripción breve; el cuerpo explica el motivo y la implementación y el pie asocia el requisito; el pie final declara el cambio que rompe la compatibilidad e indica la dirección de migración.

Ejemplo de corrección:

```text
fix(spacing): avoid false positives before Chinese punctuation

The spacing rule previously flagged strings such as 「使用Node.js，」 because
the punctuation check ran after whitespace normalization.

Refs: REQ-004, #142
```

## Archivos relacionados

- La revisión del historial de commits corresponde a la dimensión D7: [Matriz de dimensiones de revisión](./review-dimension-matrix.md)
- Generación del registro de cambios: [Especificación del registro de cambios](./changelog-specification.md)
- Base del incremento de versión: [Especificación de gestión de versiones](./version-management-specification.md)
- Puntos de comprobación de la revisión de código: [Especificación de revisión de código](./code-review-specification.md)
- Trazabilidad de requisitos: [Especificación de la matriz de trazabilidad de requisitos](./requirements-traceability-matrix-specification.md)
