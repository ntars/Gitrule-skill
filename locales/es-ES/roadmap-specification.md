# Especificación de la hoja de ruta

> Problema que resuelve este archivo: define la plantilla de la hoja de ruta, sus campos, el marcado de estados y el principio de no compromiso, para evitar presentar un plan como un compromiso y garantizar la coherencia con el registro de cambios y la retrospectiva de iteración.

## 1. Articulado de la especificación

1. La hoja de ruta debe indicar en un lugar destacado «esta hoja de ruta es un plan y no un compromiso de entrega».
2. No deben comprometerse fechas concretas de entrega; la versión objetivo se expresa mediante un intervalo de versiones o un trimestre.
3. Los cambios de estado deben dejar constancia, y los elementos cancelados deben explicar su motivo.
4. Los elementos completados deben remitir a la entrada correspondiente de la [especificación del registro de cambios](./changelog-specification.md), para evitar incoherencias entre ambas ubicaciones.
5. La hoja de ruta se orienta a planes futuros y admite ajustes y cancelaciones; el registro de cambios se orienta a hechos ya publicados y no puede reescribir entradas históricas.
6. Cada elemento planificado debe vincularse al menos a un requisito o a una acción de mejora de iteración; para la relación de trazabilidad, véase la [especificación de la matriz de trazabilidad de requisitos](./requirements-traceability-matrix-specification.md).

## 2. Plantilla de la hoja de ruta

```markdown
# Hoja de ruta: {{项目名称}}

> Esta hoja de ruta es un plan y no un compromiso de entrega. La versión objetivo y el trimestre son solo previsiones y pueden ajustarse según la prioridad.

Versión: {{v1.0}} ｜ Actualizado por: {{姓名}} ｜ Última verificación: {{YYYY-MM-DD}}

## Ahora / Siguiente / Más adelante

| Etapa | Elemento planificado | Estado | Versión objetivo | Requisito vinculado | Dependencias | Criterio de aceptación | Registro de cambios |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ahora | {{能力描述}} | En curso | {{v1.0}} | {{REQ-001}} | {{无}} | {{可验证条件}} | — |
| Siguiente | {{能力描述}} | Planificado | {{v1.1 ~ v1.2}} | {{REQ-008}} | {{计划项 A}} | {{可验证条件}} | — |
| Más adelante | {{能力描述}} | Planificado | {{待定}} | {{REQ-015}} | {{外部依赖}} | {{可验证条件}} | — |
| Cancelado | {{能力描述}} | Cancelado | — | {{REQ-020}} | — | — | — |

Estados: planificado / en curso / completado / cancelado

## Registro de cambios de estado
| Fecha | Elemento planificado | Estado anterior → Estado nuevo | Motivo | Responsable de la decisión |
| --- | --- | --- | --- | --- |
| {{YYYY-MM-DD}} | {{计划项}} | {{规划中 → 已取消}} | {{原因}} | {{姓名}} |

## Nota de cancelación
- {{计划项}}: {{取消原因，如需求变更、依赖 unavailable}}
```

## 3. Plantilla de elemento planificado

```markdown
### {{计划项名称}}

- Estado: {{规划中 / 进行中 / 已完成 / 已取消}}
- Versión objetivo: {{vX.Y / 季度 / 待定}}
- Requisito vinculado: {{REQ-NNN}}
- Origen: {{立项书 / 迭代回顾 A-NN / 用户反馈}}
- Dependencias: {{前置计划项或外部依赖；无则写「无」}}
- Criterio de aceptación: {{可验证的完成条件，须含阈值}}
- Motivo de no finalización: {{仅已取消项填写}}
```

## 4. Definición de campos

| Campo | Obligatorio | Tipo | Puntos de cumplimentación | Ejemplo |
| --- | --- | --- | --- | --- |
| Elemento planificado | Sí | Sintagma nominal | Describe la capacidad que se va a entregar, no la acción de una tarea | `Compatibilidad con configuración TOML` |
| Estado | Sí | Enumeración | Planificado / en curso / completado / cancelado | `En curso` |
| Versión objetivo | Sí | Versión / trimestre / pendiente | Se prohíben las fechas concretas | `v1.1 ~ v1.2` |
| Requisito vinculado | Sí | `REQ-NNN` | Coherente con la numeración del inicio del proyecto | `REQ-008` |
| Origen | Sí | Texto | Inicio del proyecto, retrospectiva de iteración o comentarios de usuarios | `Retrospectiva de iteración A-01` |
| Dependencias | Sí | Texto | Si no las hay debe escribirse «ninguna»; no debe dejarse vacío | `Depende del elemento planificado A` |
| Criterio de aceptación | Sí | Texto | Verificable y con umbral | `Análisis de 100 muestras sin fallos` |
| Registro de cambios | Obligatorio según el caso | Enlace | Obligatorio en los elementos completados | `[1.0.0]` |
| Motivo de cancelación | Obligatorio según el caso | Texto | Obligatorio en los elementos cancelados | `La API externa de la que dependía ya no está disponible` |

## 5. Instrucciones de cumplimentación

1. **División por etapas**: tres niveles «ahora / siguiente / más adelante»; «ahora» no debe superar los 3 elementos y, si se excede, debe reordenarse la prioridad.
2. **No compromiso**: se prohíben compromisos de fecha como «publicación en el T3» o «finalización en diciembre»; la previsión se expresa con números de versión o intervalos trimestrales.
3. **Criterio de aceptación**: debe poder dictaminarse objetivamente; «mejorar la facilidad de uso» no es admisible, mientras que «reducir los elementos de configuración de 5 a 2» sí lo es.
4. **Cambios de estado**: cada cambio añade un registro y no sobrescribe el valor anterior; los elementos cancelados conservan su fila y se explica el motivo.
5. **Vinculación al completar**: al cambiar el estado a «completado» debe cumplimentarse al mismo tiempo el ancla del registro de cambios; sin el registro correspondiente no debe marcarse como completado.
6. **Vinculación con la retrospectiva**: cuando se incorpora a la hoja de ruta una acción de mejora procedente de la retrospectiva de iteración, debe indicarse A-NN en «origen» y registrarse de forma sincronizada en la [especificación de la retrospectiva de iteración](./iteration-retrospective-specification.md).
7. **Resumen en el README**: el README solo incluye el resumen de los tres niveles y el enlace; la tabla completa permanece en este archivo, según la [especificación de secciones del README](./readme-sections-specification.md).

Errores frecuentes:

| Redacción incorrecta | Problema | Modo de corrección |
| --- | --- | --- |
| «Publicación en diciembre de 2026» | Constituye un compromiso | Cambiar a `v1.2` o `Q4` |
| Elemento completado sin enlace al registro de cambios | Incoherencia entre ambas ubicaciones | Añadir el ancla del registro |
| Eliminar la fila de un elemento cancelado | El historial deja de ser trazable | Conservar la fila y explicar el motivo |
| Elemento planificado redactado como «optimizar el rendimiento» | Sin criterio de aceptación | Añadir un indicador con umbral |
| Hoja de ruta con 20 elementos | No permite juzgar la prioridad | Reducir a tres niveles con un número limitado de elementos por nivel |

## 6. Ejemplo completo

```markdown
# Hoja de ruta: markdown-lint-cli

> Esta hoja de ruta es un plan y no un compromiso de entrega.

Versión: v1.0 ｜ Actualizado por: Li Si ｜ Última verificación: 2026-11-20

| Etapa | Elemento planificado | Estado | Versión objetivo | Requisito vinculado | Dependencias | Criterio de aceptación | Registro de cambios |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ahora | Conjunto de reglas básicas | Completado | v1.0.0 | REQ-001~007 | Ninguna | Tasa de detección ≥95 % en 50 muestras | [1.0.0] |
| Siguiente | Integración con el plugin del editor | Planificado | v1.1 | REQ-003 | Conjunto de reglas básicas estable | Invocable desde los editores principales | — |
| Más adelante | DSL de reglas personalizadas | Planificado | Pendiente | REQ-018 | API de plugins estable | El usuario puede añadir reglas sin modificar el código fuente | — |
| Cancelado | Sincronización de reglas en la nube | Cancelado | — | REQ-020 | — | — | — |

## Registro de cambios de estado
| Fecha | Elemento planificado | Estado anterior → Estado nuevo | Motivo | Responsable de la decisión |
| --- | --- | --- | --- | --- |
| 2026-11-15 | Sincronización de reglas en la nube | Planificado → Cancelado | Sin recursos de mantenimiento del lado servidor | Li Si |
```

## Archivos relacionados

- Nomenclatura de versiones y versión objetivo: [especificación de gestión de versiones](./version-management-specification.md)
- Base del inicio del proyecto y numeración de requisitos: [especificación de inicio del proyecto y requisitos](./project-initiation-and-requirements-specification.md)
- Registro externo de los elementos completados: [especificación del registro de cambios](./changelog-specification.md)
- Origen de las acciones de mejora: [especificación de la retrospectiva de iteración](./iteration-retrospective-specification.md)
- Trazabilidad de requisitos a plan: [especificación de la matriz de trazabilidad de requisitos](./requirements-traceability-matrix-specification.md)
- Sección de hoja de ruta del README: [especificación de secciones del README](./readme-sections-specification.md)
