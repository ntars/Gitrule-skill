# Especificación de la matriz de trazabilidad de requisitos

> Problema que resuelve este archivo: define la plantilla y los campos de la matriz de trazabilidad bidireccional de requisitos a diseño, implementación, pruebas y publicación, para garantizar que los productos de cada fase del ciclo de vida se referencien de forma coherente, que el impacto de los cambios pueda evaluarse y que las lagunas de cobertura puedan detectarse.

## 1. Articulado de la especificación

1. Cada requisito de nivel «obligatorio» debe ocupar una fila en la matriz de trazabilidad y registrar los productos de toda la cadena, desde el inicio del proyecto hasta la publicación.
2. La relación de trazabilidad debe poder consultarse en ambos sentidos: en sentido directo, del requisito a los productos posteriores; en sentido inverso, del producto a los requisitos anteriores.
3. Cuando un requisito se corresponde con varios productos, debe usarse una lista de identificadores separados por comas; los identificadores deben coincidir exactamente con los definidos en los documentos correspondientes.
4. Los cambios de requisitos deben dejar constancia en la matriz, registrando el motivo del cambio, el alcance del impacto y el responsable de la decisión; no deben sobrescribirse directamente los valores anteriores.
5. La matriz debe verificarse antes de cada publicación de versión; los requisitos «obligatorios» sin cerrar no deben publicarse.
6. Criterio del cálculo de cobertura: cobertura de requisitos = número de requisitos «obligatorios» publicados / número total de requisitos «obligatorios».

## 2. Plantilla de la matriz de trazabilidad

```markdown
# Matriz de trazabilidad de requisitos: {{项目名称}}

Versión: {{vX.Y.Z}} ｜ Actualizado por: {{姓名}} ｜ Última verificación: {{YYYY-MM-DD}}

| ID del requisito | Título del requisito | Prioridad | Objetivo del proyecto | Decisión de arquitectura | Documento de diseño | PR de implementación | Caso de prueba | Versión de publicación | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | {{标题}} | Obligatorio | G1 | ADR-0002 | docs/api.md#check | #12 | TC-001, TC-002 | v1.0.0 | Verificado |
| REQ-002 | {{标题}} | Recomendado | G2 | — | — | #15 | TC-005 | — | Implementado |
| REQ-003 | {{标题}} | Obligatorio | G1 | ADR-0003 | docs/architecture.md#flow | — | — | — | Pendiente de implementación |

Estados: por confirmar / confirmado / pendiente de implementación / implementado / verificado / publicado / obsoleto
```

## 3. Plantilla del índice inverso

```markdown
## Consulta inversa por producto

| Tipo de producto | Identificador del producto | ID de requisitos cubiertos |
| --- | --- | --- |
| Decisión de arquitectura | ADR-0002 | REQ-001, REQ-004 |
| Caso de prueba | TC-001 | REQ-001 |
| PR de implementación | #12 | REQ-001, REQ-007 |
| Versión de publicación | v1.0.0 | REQ-001, REQ-002 |
```

## 4. Plantilla del registro de cambios

```markdown
## Registro de cambios

| Fecha | ID del requisito | Contenido del cambio | Motivo | Alcance del impacto | Responsable de la decisión |
| --- | --- | --- | --- | --- | --- |
| {{YYYY-MM-DD}} | {{REQ-NNN}} | {{字段：原值 → 新值}} | {{依据}} | {{受影响的下游产物}} | {{姓名}} |
```

## 5. Definición de campos

| Campo | Obligatorio | Tipo | Puntos de cumplimentación | Ejemplo |
| --- | --- | --- | --- | --- |
| ID del requisito | Sí | `REQ-NNN` | Coherente con la numeración de la [especificación de inicio del proyecto y requisitos](./project-initiation-and-requirements-specification.md) | `REQ-001` |
| Prioridad | Sí | Enumeración | Obligatorio / recomendado / opcional | `Obligatorio` |
| Objetivo del proyecto | Sí | `G-N` | Número del objetivo correspondiente del documento de inicio del proyecto | `G1` |
| Decisión de arquitectura | No | `ADR-NNNN` | Si no hay decisión de arquitectura debe escribirse «—»; no debe dejarse vacío | `ADR-0002` |
| Documento de diseño | No | `ruta#ancla` | Con precisión hasta el ancla de la sección | `docs/api.md#check` |
| PR de implementación | No | `#número` | Número del PR, no el hash del commit | `#12` |
| Caso de prueba | Sí | Lista de `TC-NNN` | Al menos uno; si no hay casos, debe justificarse | `TC-001` |
| Versión de publicación | No | `vX.Y.Z` | Coherente con el tag | `v1.0.0` |
| Estado | Sí | Enumeración | Uno de los siete estados; solo avanza, salvo el paso a obsoleto | `Verificado` |
| Alcance del impacto del registro de cambios | Sí | Texto | Enumerar los ADR, PR y TC afectados | `ADR-0002, TC-001` |

## 6. Instrucciones de cumplimentación

1. **Coherencia de identificadores**: los ID de requisito, los números ADR y los números TC de la matriz deben coincidir literalmente con los documentos de origen; se prohíben abreviaturas o alias.
2. **Criterio de valores vacíos**: lo no aplicable se escribe «—» y lo no generado se escribe «pendiente»; ambos significados son distintos y no deben confundirse.
3. **Índice inverso**: cada actualización de la matriz directa debe ir acompañada de la actualización del índice inverso; si ambos no coinciden, prevalece la matriz directa y debe corregirse de inmediato.
4. **Constancia de los cambios**: antes de modificar cualquier campo debe añadirse una fila al registro de cambios con el valor anterior y el nuevo; se prohíbe sobrescribir directamente.
5. **Verificación previa a la publicación**: antes de publicar debe comprobarse uno por uno si los requisitos «obligatorios» disponen de caso de prueba y de versión de publicación; la falta de cualquiera de ellos bloquea la publicación.
6. **Requisitos obsoletos**: se conserva la fila y no se elimina; el estado pasa a «obsoleto» y en el registro de cambios se indica el motivo de la obsolescencia.

Errores frecuentes:

| Redacción incorrecta | Problema | Modo de corrección |
| --- | --- | --- |
| Dejar vacío el campo del caso de prueba | La laguna de cobertura queda invisible | Escribir «pendiente» y vaciarlo antes de la publicación |
| Poner el hash del commit en el campo del PR | No puede localizarse el registro de revisión | Usar el número del PR |
| Cambiar el valor directamente al modificarlo | El impacto deja de ser trazable | Añadir primero el registro de cambios |
| Retrasar el estado de «verificado» a «implementado» | Infringe el principio de avance único | Abrir un defecto nuevo y una nueva fila de trazabilidad |
| Incoherencia entre la matriz directa y el índice inverso | Referencias desalineadas | Sincronizar con la matriz directa antes de publicar |

## 7. Ejemplo completo

```markdown
# Matriz de trazabilidad de requisitos: markdown-lint-cli

Versión: v1.0.0 ｜ Actualizado por: Wang Wu ｜ Última verificación: 2026-11-20

| ID del requisito | Título del requisito | Prioridad | Objetivo del proyecto | Decisión de arquitectura | Documento de diseño | PR de implementación | Caso de prueba | Versión de publicación | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | Comprobación de espacios entre chino e inglés | Obligatorio | G1 | ADR-0002 | docs/api.md#rules-spacing | #12 | TC-001, TC-002 | v1.0.0 | Publicado |
| REQ-002 | Salida de informe JSON | Recomendado | G1 | — | docs/api.md#reporter | #15 | TC-011 | v1.0.0 | Publicado |
| REQ-003 | Integración con el plugin del editor | Opcional | G2 | Pendiente | Pendiente | — | Pendiente | — | Por confirmar |

## Registro de cambios

| Fecha | ID del requisito | Contenido del cambio | Motivo | Alcance del impacto | Responsable de la decisión |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | REQ-003 | Prioridad: recomendado → opcional | Plazo insuficiente en v1.0 | ADR-0005, TC-020 | Li Si |
```

## Archivos relacionados

- Numeración de requisitos y condiciones de aceptación: [especificación de inicio del proyecto y requisitos](./project-initiation-and-requirements-specification.md)
- Numeración de decisiones de arquitectura: [especificación del documento de diseño de arquitectura](./architecture-design-document-specification.md)
- Numeración de casos de prueba: [especificación de pruebas](./testing-specification.md)
- Versiones de publicación y tag: [especificación de gestión de versiones](./version-management-specification.md)
- Descripción externa de los cambios de versión: [especificación del registro de cambios](./changelog-specification.md)
- Retrospectiva del proceso al final de la iteración: [especificación de la retrospectiva de iteración](./iteration-retrospective-specification.md)
