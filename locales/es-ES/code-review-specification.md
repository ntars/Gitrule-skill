# Especificación de revisión de código

> Problema que resuelve este archivo: define la plantilla de descripción de la pull request, la plantilla de comentarios de revisión, el registro de revisión, los campos y el flujo, para garantizar la calidad de la fusión y el intercambio de conocimiento.

## 1. Artículos de la especificación

1. El autor debe explicar en la descripción del PR el propósito del cambio, el alcance del impacto y los resultados de las pruebas propias; la plantilla se encuentra en la [especificación de flujo de trabajo de Git y ramas](./git-workflow-and-branching-specification.md).
2. Quien revisa debe formular comentarios concretos y ejecutables, distinguiendo entre «cambio obligatorio» y «sugerencia».
3. Antes de la fusión debe haber al menos la aprobación de 1 revisor y la CI completamente en verde (corresponde a la regla absoluta H9); se prohíbe que el autor apruebe su propio PR.
4. Cuando haya desacuerdo en los comentarios de revisión, debe escalarse al mantenedor para su decisión (véase la [especificación de código de conducta](./code-of-conduct-specification.md)).
5. Tras la fusión debe eliminarse la rama de origen para mantener limpia la lista de ramas.

## 2. Lista de verificación de la revisión

Quien revisa debe confirmar punto por punto:

| # | Dimensión | Puntos de comprobación | Resultado |
| --- | --- | --- | --- |
| 1 | Corrección | Lógica correcta, límites y excepciones tratados | Aprobado / Requiere cambios |
| 2 | Pruebas | El cambio cuenta con pruebas correspondientes y estas pasan | Aprobado / Requiere cambios |
| 3 | Estilo | Conforme a la [especificación de estilo de código](./code-style-specification.md) | Aprobado / Requiere cambios |
| 4 | Seguridad | Sin información sensible, sin riesgo de inyección, validación de permisos correcta | Aprobado / Requiere cambios |
| 5 | Documentación | Los cambios de interfaz o de comportamiento se han reflejado en la documentación | Aprobado / Requiere cambios |
| 6 | Alcance | Cambio focalizado, sin modificaciones ajenas | Aprobado / Requiere cambios |
| 7 | Mensaje de commit | Conforme a la [especificación de mensajes de commit](./commit-message-specification.md) | Aprobado / Requiere cambios |
| 8 | Trazabilidad | La matriz de trazabilidad de requisitos está actualizada | Aprobado / Requiere cambios |

## 3. Plantilla de comentarios de revisión

```markdown
### Comentario {{序号}}：{{一句话标题}}

- Nivel: {{必须修改 / 建议 / 提问}}
- Ubicación: {{文件路径:行号}}
- Problema: {{描述可观察的问题，不评价人}}
- Fundamento: {{规范条款 / 需求编号 / 风险说明}}
- Sugerencia: {{具体的修改方式或替代方案}}

Ejemplo:
### Comentario 1: Rama de excepción no cubierta
- Nivel: Cambio obligatorio
- Ubicación: `src/rules/spacing.ts:42`
- Problema: Cuando la entrada contiene Markdown incompleto se lanza una excepción y no se devuelve el resultado de coincidencia de la regla.
- Fundamento: REQ-001, criterio de aceptación 2 (ruta límite).
- Sugerencia: Capturar aquí la excepción de análisis y devolver la coincidencia como «fallo de análisis», añadiendo un caso de prueba de límite.
```

## 4. Plantilla de registro de revisión

```markdown
## Registro de revisión: {{PR 编号}}

Revisor: {{姓名}} ｜ Fecha de revisión: {{YYYY-MM-DD}} ｜ Ronda: {{第 N 轮}}

| N.º de comentario | Nivel | Conclusión de tratamiento | Responsable del tratamiento | Método de verificación |
| --- | --- | --- | --- | --- |
| 1 | Cambio obligatorio | Modificado | Autor | Véase el commit abc1234 |
| 2 | Sugerencia | No adoptada | Autor | Motivo: {{说明}} |

Conclusión: {{批准 / 需修改后再审 / 拒绝}}
- Condiciones de aprobación: todos los puntos de «cambio obligatorio» están resueltos y la CI está completamente en verde.
- Puntos pendientes: {{无 / 列出}}
```

## 5. Definición de campos

| Campo | Obligatorio | Tipo | Puntos de cumplimentación | Ejemplo |
| --- | --- | --- | --- | --- |
| Nivel | Sí | Enumeración | Cambio obligatorio / Sugerencia / Pregunta | `Cambio obligatorio` |
| Ubicación | Sí | `ruta:línea` | Preciso hasta la línea; se prohíbe indicar solo el nombre del archivo | `src/parser.ts:42` |
| Problema | Sí | Texto | Describe el fenómeno, no evalúa al autor | `Excepción de análisis no capturada` |
| Fundamento | Sí | Texto | Cláusula de la especificación o código REQ | `REQ-001, criterio de aceptación 2` |
| Sugerencia | Sí | Texto | Ejecutable; no basta con «por favor, optimizar» | `Capturar la excepción y devolver la coincidencia` |
| Conclusión de tratamiento | Sí | Enumeración | Modificado / No adoptada / Aplazada | `Modificado` |
| Método de verificación | Sí | Texto | Hash del commit o forma de reexamen | `Véase el commit abc1234` |
| Conclusión | Sí | Enumeración | Aprobado / Requiere cambios y nueva revisión / Rechazado | `Aprobado` |

## 6. Instrucciones de cumplimentación

1. **Distinción de niveles**: «cambio obligatorio» se refiere a problemas que bloquean la fusión (corrección, seguridad, falta de pruebas); «sugerencia» no afecta a la fusión; «pregunta» requiere aclaración del autor pero no exige modificaciones.
2. **Formulación del comentario**: debe describirse el problema observable; se prohíben expresiones valorativas como «esto está muy mal escrito».
3. **Ubicación**: precisa hasta el número de línea; los problemas que afectan a varios archivos deben indicarse por separado en cada comentario.
4. **Fundamento**: cuando sea trazable, debe trazarse; si no existe fundamento normativo, deben indicarse el riesgo o el impacto; se prohíbe «me parece».
5. **Conclusión de tratamiento**: en «no adoptada» debe indicarse el motivo; en «aplazada» debe indicarse dónde se hará el seguimiento posterior.
6. **Aprobación**: debe confirmarse que todos los puntos de «cambio obligatorio» están cerrados y que la CI está completamente en verde; el autor no debe aprobar su propio PR.
7. **Desacuerdo**: cuando el revisor y el autor discrepen, debe escalarse al mantenedor, y la decisión debe registrarse en el registro de revisión.

Errores frecuentes:

| Redacción incorrecta | Problema | Forma de corrección |
| --- | --- | --- |
| «Esto no vale» | Sin problema, sin fundamento, sin sugerencia | Aportar los tres elementos |
| «Sugiero optimizar el rendimiento» | No ejecutable | Dar una forma concreta e indicadores de decisión |
| Indicar solo el nombre del archivo sin la línea | Localización difícil | Precisar hasta la línea |
| El autor se aprueba a sí mismo | Infracción de la norma | Revisión por otra persona |
| Usar «cambio obligatorio» para preferencias personales | Uso abusivo del nivel | Rebajar a «sugerencia» |

## 7. Ejemplo completo

```markdown
## Registro de revisión: #12

Revisor: Li Si ｜ Fecha de revisión: 2026-11-18 ｜ Ronda: 1

| N.º de comentario | Nivel | Conclusión de tratamiento | Responsable del tratamiento | Método de verificación |
| --- | --- | --- | --- | --- |
| 1 | Cambio obligatorio | Modificado | Wang Wu | Véase el commit a1b2c3d |
| 2 | Sugerencia | No adoptada | Wang Wu | Motivo: el QPS actual no alcanza el cuello de botella; se evita el sobrediseño |
| 3 | Pregunta | Aclarada | Wang Wu | Aclaración añadida en el cuerpo del PR |

Conclusión: Aprobado
- Condiciones de aprobación: todos los puntos de «cambio obligatorio» están resueltos y la CI está completamente en verde (run #128).
- Puntos pendientes: ninguno
```

## Archivos relacionados

- Descripción del PR y modelo de ramas: [especificación de flujo de trabajo de Git y ramas](./git-workflow-and-branching-specification.md)
- Base de la comprobación de estilo: [especificación de estilo de código](./code-style-specification.md)
- Criterios de aprobación de pruebas: [especificación de pruebas](./testing-specification.md)
- Actualización del estado de trazabilidad: [especificación de la matriz de trazabilidad de requisitos](./requirements-traceability-matrix-specification.md)
- Puerta de calidad: [puerta de calidad](./quality-gate.md)
- Base para la decisión de desacuerdos: [especificación de código de conducta](./code-of-conduct-specification.md)
- Las comprobaciones automatizadas pertenecen a la dimensión D9: [matriz de dimensiones de revisión](./review-dimension-matrix.md)
