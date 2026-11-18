# Inicio del proyecto y especificación de requisitos

> Problema que resuelve este archivo: define las plantillas y los campos de la declaración de objetivos, la recopilación de requisitos y la delimitación del alcance en la fase de inicio del proyecto, con el fin de garantizar que el proyecto cuente desde el principio con una base clara, verificable y trazable.

## 1. Disposiciones de la especificación

1. El documento de inicio del proyecto debe responder a seis preguntas: qué es, por qué se hace, hasta qué punto se llevará, a quién no está destinado, quién lo usa y qué restricciones tiene.
2. Los requisitos deben distinguir tres niveles: «debe / debería / puede»; las convenciones de redacción figuran en la [Especificación general de redacción](./general-writing-specification.md).
3. Cada requisito debe ser verificable: aportar condiciones de aceptación en forma Given/When/Then o un umbral medible evaluable.
4. Cada requisito debe tener un número estable y una fuente; se prohíben las entradas de requisitos sin número.
5. Cuando la información sea insuficiente, marcar «【pendiente de confirmación: nombre del campo】»; no debe completarse por conjetura, las reglas figuran en [Recopilación de información y plantillas](./information-collection-and-templates.md).
6. El alcance debe indicar simultáneamente los elementos incluidos y los excluidos; unos no objetivos vacíos se consideran un alcance no delimitado.
7. Todo cambio de alcance debe registrar el motivo, el impacto y el responsable de la decisión, e incorporarse al registro de cambios de la [Especificación de la matriz de trazabilidad de requisitos](./requirements-traceability-matrix-specification.md).

## 2. Plantilla del documento de inicio del proyecto

```markdown
# Documento de inicio del proyecto: {{项目名称}}

Versión del documento: {{v0.1}} ｜ Estado: {{草稿 / 评审中 / 已批准}} ｜ Responsable de la decisión: {{姓名}} ｜ Fecha: {{YYYY-MM-DD}}

## Posicionamiento en una frase
Proporcionar a {{目标用户}} {{核心能力}}, resolviendo {{当前痛点}}.
(≤ 60 caracteres; se prohíben calificativos autoelogiosos como «potente», «elegante» o «líder»)

## Contexto y motivación
- Situación actual: {{当前如何运作}}
- Carencias de las soluciones existentes: {{具体缺陷 1}}; {{具体缺陷 2}}
- Ventana de oportunidad: {{时机、技术或市场变化}}
- Fundamento del inicio del proyecto: {{工单号 / 访谈记录 / 数据指标，须可溯源}}

## Objetivos y no objetivos
| Tipo | Elemento | Resultado verificable |
| --- | --- | --- |
| Objetivo G1 | {{要达成的结果}} | {{可量化指标 + 阈值}} |
| Objetivo G2 | {{要达成的结果}} | {{可量化指标 + 阈值}} |
| No objetivo N1 | {{明确不做的事}} | {{判定边界，说明为何排除}} |

## Criterios de éxito
| Indicador | Línea base | Valor objetivo | Forma de verificación | Momento de verificación |
| --- | --- | --- | --- | --- |
| {{指标名}} | {{当前值}} | {{目标值}} | {{如何测量}} | {{何时测量}} |

## Usuarios objetivo
| Rol de usuario | Escenario típico | Necesidad principal | Solución alternativa actual |
| --- | --- | --- | --- |
| {{角色}} | {{何时何地}} | {{要完成的任务}} | {{现用方案}} |

## Restricciones
- Técnicas: {{语言、平台、兼容性等限制}}
- Temporales: {{截止日期或窗口}}
- De recursos: {{人力、预算、基础设施}}
- De cumplimiento: {{许可证、隐私、行业规范}}

## Alcance
- Incluido: {{本期交付项}}
- Excluido: {{本期明确不交付项}}
- Pendiente de confirmación: {{【待确认：字段名】}}

## Registro de decisiones
| Fecha | Decisión | Responsable de la decisión | Fundamento |
| --- | --- | --- | --- |
```

## 3. Plantilla de entrada de requisito

```markdown
### REQ-{{三位序号}}: {{需求标题}}

- Fuente: {{工单号 / 访谈 / 竞品 / 推测}}
- Prioridad: {{必须 / 应当 / 可以}}
- Objetivo asociado: {{G1 / G2 / …}}
- Historia de usuario: como {{角色}}, deseo {{行为}}, para {{价值}}
- Condiciones de aceptación:
  1. Given {{前置条件}}
     When {{操作}}
     Then {{预期结果}}
  2. Given {{边界或异常前置条件}}
     When {{操作}}
     Then {{预期结果}}
- Estado: {{待确认 / 已确认 / 已实现 / 已验证 / 已废弃}}
- Trazabilidad asociada: {{见需求追踪矩阵中的需求 ID}}
```

## 4. Definición de campos

### 4.1 Campos del documento de inicio del proyecto

| Campo | Obligatorio | Tipo | Puntos de cumplimentación | Ejemplo |
| --- | --- | --- | --- | --- |
| Versión del documento | Sí | Texto | Versión semántica o versión por fecha | `v0.1` |
| Estado | Sí | Enumeración | Borrador / en revisión / aprobado | `en revisión` |
| Responsable de la decisión | Sí | Texto | Persona con poder de decisión final sobre alcance y prioridades | `Zhang San` |
| Posicionamiento en una frase | Sí | Texto | Usuario objetivo + capacidad principal + problema, ≤ 60 caracteres | Proporcionar a los desarrolladores front-end de… |
| Fundamento del inicio del proyecto | Sí | Texto | Al menos un registro trazable; se prohíbe «decisión del equipo» | `ISSUE-142` |
| Objetivos / no objetivos | Sí | Tabla | Cada objetivo se empareja con un resultado verificable; al menos un no objetivo | `G1: arranque en frío < 2 s` |
| Criterios de éxito | Sí | Tabla | El indicador debe tener línea base, umbral, método de medición y momento | `tasa de error < 0,1 %` |
| Restricciones | Sí | Lista | Deben cumplimentarse las cuatro categorías; si no existe, escribir «ninguna» | `debe ser compatible con Node 18+` |
| Pendiente de confirmación | No | Lista | Usar solo el formato 【pendiente de confirmación: nombre del campo】 | `【pendiente de confirmación: límite presupuestario】` |

### 4.2 Campos de la entrada de requisito

| Campo | Obligatorio | Tipo | Puntos de cumplimentación | Ejemplo |
| --- | --- | --- | --- | --- |
| Número | Sí | `REQ-NNN` | Número de tres dígitos, continuo, no reutilizado y no reordenado | `REQ-007` |
| Fuente | Sí | Texto | Trazable hasta un registro concreto | `entrevista de usuario n.º 3` |
| Prioridad | Sí | Enumeración | Debe / debería / puede | `debe` |
| Objetivo asociado | Sí | Lista | Número G correspondiente del documento de inicio del proyecto | `G1` |
| Historia de usuario | Sí | Texto | Los tres elementos rol + comportamiento + valor deben estar completos | Como… deseo… para… |
| Condiciones de aceptación | Sí | Lista | Al menos 1 conjunto Given/When/Then, que debe incluir un caso límite o excepcional | Véase la plantilla |
| Estado | Sí | Enumeración | Uno de los cinco estados; solo avanza, no retrocede | `confirmado` |

## 5. Instrucciones de cumplimentación

1. **Posicionamiento en una frase**: redactar según la estructura en tres segmentos «para quién + qué aporta + qué resuelve»; si la frase deja de ser válida al eliminar los calificativos, significa que falta información sustantiva.
2. **Criterios de éxito**: cada entrada debe presentar a la vez una línea base y un umbral. «Mejorar el rendimiento» o «mejor experiencia» se consideran no conformes y deben reformularse como «tiempo de arranque P95 reducido de 3 s a < 1,5 s».
3. **No objetivos**: indicar el alcance explícitamente excluido y la frontera de decisión, y no «ya se verá más adelante»; si no hay no objetivos no vacíos, el alcance se considera no delimitado.
4. **Número de requisito**: una vez asignado queda fijado de forma permanente; cuando un requisito se abandona, su estado pasa a «abandonado» y el número no debe reciclarse ni reutilizarse.
5. **Condiciones de aceptación**: deben cubrir el camino nominal y al menos un camino límite o excepcional; las condiciones no evaluables objetivamente (como «interfaz estética») deben convertirse en medidas o puntos de control verificables.
6. **Puntos pendientes de confirmación**: el inicio del proyecto admite puntos pendientes de confirmación, pero deben enumerarse íntegramente y designarse los responsables de confirmarlos; deben quedar resueltos antes de pasar al desarrollo.

Errores frecuentes:

| Redacción errónea | Problema | Forma de corrección |
| --- | --- | --- |
| «Hacer una herramienta fácil de usar» | Sin usuario objetivo ni resultado verificable | Añadir el rol de usuario y los indicadores con umbral |
| Escribir «ninguno» como no objetivo | Alcance no delimitado, propenso a desbordarse | Enumerar los elementos explícitamente excluidos en esta fase |
| Requisito sin número, descrito directamente en el cuerpo del texto | Imposible de trazar y referenciar | Asignar `REQ-NNN` y referenciarlo en todo el ámbito |
| Escribir «funciona correctamente» como condición de aceptación | No evaluable | Descomponer en Given/When/Then |
| Tratar una conjetura como requisito establecido | Fuente no trazable | Marcar la fuente como «conjetura» y convertirla en pendiente de confirmación |

## 6. Ejemplo completo

```markdown
# Documento de inicio del proyecto: markdown-lint-cli

Versión del documento: v0.1 ｜ Estado: en revisión ｜ Responsable de la decisión: Li Si ｜ Fecha: 2026-11-18

## Posicionamiento en una frase
Proporcionar a los redactores técnicos chinos una herramienta de línea de comandos para la verificación de normas Markdown, resolviendo la inconsistencia de estilo documental entre múltiples repositorios y la ausencia de validación automática.

## Contexto y motivación
- Situación actual: los README de 12 repositorios son escritos a mano por sus respectivos mantenedores, con estilos heterogéneos.
- Carencias de las soluciones existentes: las herramientas genéricas de lint en inglés no admiten las reglas de espaciado entre chino e inglés; la revisión manual consume en promedio 25 minutos por documento.
- Ventana de oportunidad: el equipo está unificando actualmente su página de inicio de código abierto y necesita aplicar las normas de una sola vez.
- Fundamento del inicio del proyecto: ISSUE-142, acta de revisión documental del 2026-11-10.

## Objetivos y no objetivos
| Tipo | Elemento | Resultado verificable |
| --- | --- | --- |
| Objetivo G1 | Verificar automáticamente 8 categorías de problemas de formato | Tasa de detección ≥ 95 % en 50 documentos de muestra |
| Objetivo G2 | Mantener controlado el tiempo de una verificación | Verificación de un documento de 1000 líneas < 2 s |
| No objetivo N1 | No ofrecer pulido del contenido documental | Mostrar únicamente la ubicación de las reglas detectadas, sin reescribir el texto |

## Criterios de éxito
| Indicador | Línea base | Valor objetivo | Forma de verificación | Momento de verificación |
| --- | --- | --- | --- | --- |
| Tiempo de revisión manual | 25 minutos por documento | < 5 minutos por documento | Experimento comparativo con 5 mantenedores | Antes de la publicación de v1.0 |

### REQ-001: Verificar los espacios en el texto mixto chino-inglés
- Fuente: ISSUE-142
- Prioridad: debe
- Objetivo asociado: G1
- Historia de usuario: como mantenedor de documentación, deseo que se señalen automáticamente los espacios ausentes entre chino e inglés, para uniformar la maquetación.
- Condiciones de aceptación:
  1. Given el documento contiene «使用Node.js开发»
     When se ejecuta la verificación
     Then se muestra el número de línea y el aviso «falta un espacio entre chino e inglés»
  2. Given el documento ya tiene un espacio en ese punto
     When se ejecuta la verificación
     Then no se notifica la detección de esa regla
- Estado: confirmado
```

## Archivos relacionados

- Trazabilidad de los requisitos hacia el diseño, las pruebas y la publicación: [Especificación de la matriz de trazabilidad de requisitos](./requirements-traceability-matrix-specification.md)
- Campos de información y marcado de carencias: [Recopilación de información y plantillas](./information-collection-and-templates.md)
- División de fases y condiciones de entrada: [Flujo de ejecución](./execution-process.md)
- La denominación se realiza tras concluir el inicio del proyecto: [Especificación de denominación de proyectos](./project-naming-specification.md)
- Comunicación externa de los cambios de alcance: [Especificación del registro de cambios](./changelog-specification.md)
