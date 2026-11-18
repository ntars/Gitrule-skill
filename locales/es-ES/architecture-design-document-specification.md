# Especificación del documento de diseño de arquitectura

> Problema que resuelve este archivo: define la plantilla, los campos y la forma de redacción del documento de arquitectura y de los registros de decisión de arquitectura (ADR), describe los límites del sistema, las responsabilidades de los módulos, los atributos de calidad y las concesiones clave, y garantiza la trazabilidad de las decisiones.

## 1. Cláusulas de la especificación

1. El documento de arquitectura (`docs/architecture.md`) describe solo la estructura y los límites, sin ejemplos de uso; los límites de responsabilidad se detallan en la [Matriz de documentación](./document-matrix.md).
2. Toda decisión técnica relevante debe tener un ADR correspondiente; una decisión sin ADR se considera una decisión no registrada.
3. La numeración de los ADR es continua y permanentemente fija; una vez adoptado un ADR no se reescribe el historial, y los cambios de estado se registran creando un nuevo ADR que se marca como «sustituido».
4. La descripción de la arquitectura debe mantenerse coherente con la implementación del código; si el código y la documentación no coinciden, prevalece el código y la documentación se corrige de inmediato.
5. Cada decisión de arquitectura debe poder rastrearse hasta uno o varios requisitos; la relación de trazabilidad se detalla en la [Especificación de la matriz de trazabilidad de requisitos](./requirements-traceability-matrix-specification.md).
6. Los atributos de calidad deben indicar objetivos medibles y verificables; se prohíbe limitarse a escribir «alto rendimiento» o «alta disponibilidad».

## 2. Plantilla del documento de arquitectura

```markdown
# Diseño de arquitectura: {{项目名称}}

Versión del documento: {{v1.0}} ｜ Versión de código correspondiente: {{tag}} ｜ Fecha de la última verificación: {{YYYY-MM-DD}}

## Contexto del sistema
- Responsabilidad del sistema: {{一句话说明系统边界内的责任}}
- Actores externos: {{用户、上游系统、下游系统}}
- Entradas y salidas: {{进入系统的请求与系统产出的结果}}
- Fuera de los límites: {{明确不由本系统承担的职责}}

## División de módulos
| Módulo | Responsabilidad única | Interfaz externa | Módulos de los que depende | De lo que no se encarga |
| --- | --- | --- | --- | --- |
| {{模块名}} | {{仅一件事}} | {{接口名}} | {{模块名}} | {{明确排除}} |

## Flujos de datos clave
1. {{触发点}} → {{模块 A}}: {{传递的数据}}
2. {{模块 A}} → {{模块 B}}: {{转换与传递}}
3. {{模块 B}} → {{结果}}: {{最终产出}}

## Selección tecnológica
| Ámbito | Selección | Alternativas | Base de la decisión | ADR |
| --- | --- | --- | --- | --- |
| {{语言 / 框架 / 存储}} | {{采用项}} | {{未采用项}} | {{取舍理由}} | {{ADR-000N}} |

## Atributos de calidad
| Atributo | Valor objetivo | Forma de verificación | ADR asociado |
| --- | --- | --- | --- |
| Rendimiento | {{P95 延迟 < X ms}} | {{压测方式}} | {{ADR-000N}} |
| Disponibilidad | {{月度可用性 ≥ X%}} | {{监控统计}} | {{ADR-000N}} |
| Seguridad | {{敏感数据零明文落盘}} | {{审计方式}} | {{ADR-000N}} |
| Escalabilidad | {{横向扩容至 N 节点无需改代码}} | {{扩容演练}} | {{ADR-000N}} |

## Restricciones y concesiones
- Restricciones técnicas: {{语言版本、平台、兼容性}}
- Opciones descartadas y sus motivos: {{方案 A：原因}}
- Deuda técnica conocida: {{债务项与偿还条件}}
```

## 3. Plantilla de ADR

```markdown
# ADR-{{四位序号}}: {{决策标题}}

- Estado: {{提议 / 已采纳 / 已废弃 / 被 ADR-000N 替代}}
- Fecha: {{YYYY-MM-DD}}
- Responsable de la decisión: {{姓名}}
- Requisitos asociados: {{REQ-001 / …}}

## Contexto
{{面临的客观问题与约束，须可验证，不写主观偏好}}

## Decisión
{{采用的方案，一句话陈述，须明确到可执行的程度}}

## Alternativas
| Opción | Ventajas | Inconvenientes | Motivo por el que no se adoptó |
| --- | --- | --- | --- |
| {{方案 A}} | | | |
| {{方案 B（采用）}} | | | — |

## Consecuencias
- Positivas: {{获得的能力}}
- Negativas: {{引入的成本或限制}}
- Tareas posteriores: {{需要跟进的事项}}

## Archivos relacionados
- {{架构文档中受影响的章节}}
- {{替代或被引用的 ADR}}
```

## 4. Definición de campos

### 4.1 Campos del documento de arquitectura

| Campo | Obligatorio | Tipo | Puntos clave | Ejemplo |
| --- | --- | --- | --- | --- |
| Versión de código correspondiente | Sí | tag | Coincide con el tag de la [Especificación de gestión de versiones](./version-management-specification.md) | `v1.2.0` |
| Fecha de la última verificación | Sí | Fecha | Debe actualizarse tras cada cambio de código | `2026-11-18` |
| Responsabilidad única del módulo | Sí | Texto | Un módulo escribe solo una cosa | `analizar y validar reglas Markdown` |
| De lo que no se encarga | Sí | Texto | Delimitar el alcance para evitar la deriva de responsabilidades | `no se encarga de la reescritura de texto` |
| Selección tecnológica. Base de la decisión | Sí | Texto | Debe citar el número de ADR | `véase ADR-0002` |
| Atributos de calidad. Valor objetivo | Sí | Métrica | Con unidad y umbral, verificable | `P95 < 150ms` |
| Deuda técnica conocida | No | Lista | Indicar la condición que activa el pago de la deuda | `sustituir el analizador en v2` |

### 4.2 Campos del ADR

| Campo | Obligatorio | Tipo | Puntos clave | Ejemplo |
| --- | --- | --- | --- | --- |
| Número | Sí | `ADR-NNNN` | Número de cuatro dígitos, continuo y permanentemente fijo | `ADR-0002` |
| Estado | Sí | Enumeración | Propuesto / Aceptado / Obsoleto / Sustituido | `aceptado` |
| Requisitos asociados | Sí | Lista | Números REQ del documento de inicio del proyecto | `REQ-001` |
| Contexto | Sí | Texto | Exponer restricciones objetivas; se prohíbe «creo que» | `requiere compatibilidad con Node 18` |
| Decisión | Sí | Texto | Una frase, ejecutable | `adoptar remark como analizador` |
| Alternativas | Sí | Tabla | Al menos una opción no adoptada | Véase la plantilla |
| Motivo del rechazo | Sí | Texto | Debe indicarse para cada opción no adoptada | Véase la plantilla |
| Consecuencias | Sí | Lista | Deben figurar las tres: positivas, negativas y tareas posteriores | Véase la plantilla |

## 5. Instrucciones de cumplimentación

1. **División de módulos**: si la «responsabilidad única» de una fila contiene dos cosas unidas por «y» o «así como», debe dividirse en dos módulos.
2. **Flujos de datos**: se numeran en orden temporal e indican el contenido de los datos transmitidos; se prohíbe escribir solo el nombre del módulo y una flecha.
3. **Atributos de calidad**: cada uno debe tener valor objetivo, forma de verificación y referencia de ADR; si falta cualquiera de los tres, se considera incompleto.
4. **Contexto del ADR**: se escriben el problema y las restricciones, no la decisión en sí; la decisión aparece una sola vez, en el apartado «Decisión».
5. **Alternativas**: aunque solo exista una opción, debe escribirse «se consideró implementarlo internamente, pero se descartó por su elevado coste de mantenimiento»; la ausencia de alternativas se considera falta de argumentación.
6. **Cambio de estado**: no se modifica el cuerpo del ADR original; se crea un nuevo ADR y se cambia el estado del original a «sustituido por ADR-000N».
7. **Deuda técnica**: debe indicarse la condición que activa su pago; se prohíbe enumerar solo los síntomas.

Errores frecuentes:

| Escritura errónea | Problema | Corrección |
| --- | --- | --- |
| Incluir ejemplos de llamadas a la API en el documento de arquitectura | Solapa responsabilidades con la [Especificación de documentación de API](./api-documentation-specification.md) | Trasladarlo a la documentación de API y dejar en la arquitectura solo los nombres de las interfaces |
| «El sistema necesita alto rendimiento» | Sin umbral, no verificable | Dar un objetivo de latencia P95 y el método de prueba de carga |
| Un ADR con decisión pero sin alternativas | Sin argumentación | Añadir al menos una opción no adoptada y su motivo |
| Modificar el cuerpo de un ADR ya aceptado | Se reescribe el historial | Crear un nuevo ADR e indicar la relación de sustitución |
| Una decisión que no puede asociarse a un requisito | Se rompe la cadena de trazabilidad | Añadir el número REQ asociado |

## 6. Ejemplo completo

```markdown
# ADR-0002: adoptar remark como capa de análisis de Markdown

- Estado: aceptado
- Fecha: 2026-11-18
- Responsable de la decisión: 李四
- Requisitos asociados: REQ-001, REQ-004

## Contexto
Debe admitirse GFM y la localización de nodos de texto en chino, y las dependencias de ejecución deben ser compatibles con Node 18; el límite de esfuerzo del equipo para mantener el analizador es de 0,5 personas-mes por trimestre.

## Decisión
Adoptar el ecosistema remark como única capa de análisis de Markdown, con las reglas implementadas en forma de plugins.

## Alternativas
| Opción | Ventajas | Inconvenientes | Motivo por el que no se adoptó |
| --- | --- | --- | --- |
| Analizador propio | Control total | Requiere mantener a largo plazo los casos límite | Supera el límite de esfuerzo |
| marked | Ligero | Escasa capacidad de localización de nodos en chino | No satisface REQ-004 |

## Consecuencias
- Positivas: la compatibilidad con GFM la mantiene el proyecto upstream y la localización de nodos cumple las condiciones de aceptación.
- Negativas: los cambios en la API de plugins obligan a seguir las versiones upstream.
- Tareas posteriores: fijar la versión mayor de remark en la CI y suscribirse a sus avisos de publicación.
```

## Archivos relacionados

- Límites de responsabilidad y contenido prohibido: [Matriz de documentación](./document-matrix.md)
- Trazabilidad inversa de la decisión al requisito: [Especificación de la matriz de trazabilidad de requisitos](./requirements-traceability-matrix-specification.md)
- Redacción externa de las concesiones de ingeniería: [Guía de redacción de características y concesiones de ingeniería](./features-and-engineering-tradeoffs-guide.md)
- Convenciones de diseño de interfaces: [Especificación de diseño de API](./api-design-specification.md)
- Modelo de datos y migraciones: [Especificación de diseño de bases de datos](./database-design-specification.md)
- Unificación de terminología: [Glosario](./glossary.md)
