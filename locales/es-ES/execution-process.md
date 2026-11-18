# Proceso de ejecución

> Problema que resuelve este archivo: define la secuencia completa de fases desde el inicio del proyecto hasta la entrega, las condiciones de entrada y los entregables de cada fase, así como la regla de preguntas bloqueantes cuando la información es insuficiente.

## 1. Proceso de push del control general (Phase 0–6)

### Phase 0 · Inicio del proyecto (Project Init)

Salida: 3 candidatos de nombre de proyecto + motivo de la elección + conclusión de la búsqueda de duplicados + tabla de metadatos del repositorio (description / topics / rama por defecto / visibilidad / license). Para las reglas de nomenclatura, véase la [especificación de nombres de proyecto](./project-naming-specification.md).

### Phase 1 · Inventario (Inventory)

Escanear el repositorio y producir un inventario estructurado:
- Pila tecnológica, archivos de entrada, gestor de paquetes, lockfile
- Documentación existente y documentación faltante
- Los 10 archivos de mayor tamaño del repositorio
- CI / plantillas / reglas de protección existentes
- Estado actual de git: archivos no rastreados, cambios sin commit, commits sospechosos en el historial

### Phase 2 · Auditoría en paralelo (Audit)

Según la [matriz de dimensiones de revisión](./review-dimension-matrix.md), asignar las dimensiones a los subagentes para su ejecución en paralelo; el modo de asignación se describe en el [contrato de asignación de subagentes](./sub-agent-dispatch-contract.md). Cada subagente devuelve únicamente conclusiones estructuradas, no prosa extensa.

### Phase 3 · Corrección (Fix)

Enumerar las tareas pendientes en el orden P0 → P1 → P2, indicando el agente responsable y la acción prevista. No debe pasarse a la Phase 5 mientras P0 no esté en cero.

### Phase 4 · Generación de documentación (Docs)

Asignar cada archivo, según la [matriz de documentación](./document-matrix.md), al agente de documentación. **Se escribe un solo archivo por vez y, tras validarlo, se pasa al siguiente.**

### Phase 5 · Push (Push)

Ejecutar conforme a la [especificación de push y publicación](./push-and-release-specification.md), mostrando el resultado de cada punto.

### Phase 6 · Posterior al push (Post-Push)

Crear el tag, redactar las Release Notes, verificar la disponibilidad de las insignias y los enlaces, confirmar que la CI está en verde y confirmar que la información del apartado About es correcta.

## 2. Proceso de generación de documentación (fases 0–5)

Avanzar en orden de fase; no debe pasarse a la siguiente fase mientras la anterior no esté completada.

| Fase | Nombre | Condición de entrada | Entregable |
| --- | --- | --- | --- |
| 0 | Verificación de información | Recepción de esta especificación y de los materiales del proyecto | Lista de información confirmada y lista de información faltante |
| 1 | Preguntas bloqueantes | Existencia de campos obligatorios faltantes (véanse [recopilación de información y plantillas](./information-collection-and-templates.md)) | Lista estructurada de preguntas, agrupada por campo |
| 2 | Confirmación del marco | Campos obligatorios completos | Índice de secciones del README y esquema de puntos clave de cada sección, para confirmación del usuario |
| 3 | Generación de documentación | El usuario confirma el marco o indica expresamente que no requiere confirmación | Todos los entregables |
| 4 | Puerta de calidad | Generación de documentación finalizada | Resultado de la evaluación punto por punto de la [puerta de calidad](./quality-gate.md) |
| 5 | Entrega | La puerta se supera en su totalidad o los elementos no superados ya están marcados | Salida en el orden del [formato del informe de auditoría](./audit-report-format.md), con la guía de push adjunta |

## 3. Reglas de preguntas de la fase 1

1. Agrupar las preguntas por campo, sin superar los 15 elementos por ronda.
2. Cada pregunta debe explicar su finalidad y las secciones afectadas, para facilitar al usuario la determinación de prioridades.
3. Cuando el usuario indique expresamente que un dato no puede proporcionarse, marcar en la posición correspondiente del documento «[Pendiente de confirmación: nombre del campo]» y resumirlo al final del texto.
4. Cuando el usuario responda «según tu criterio», pueden proponerse valores recomendados, pero debe marcarse «[Valor recomendado, pendiente de confirmación del usuario]».

## Archivos relacionados

- Para los roles y responsabilidades, véase [roles y responsabilidades](./roles-and-responsibilities.md)
- Para los campos obligatorios y las marcas de elementos faltantes, véanse [recopilación de información y plantillas](./information-collection-and-templates.md)
- Para la evaluación de la puerta, véase la [puerta de calidad](./quality-gate.md)
