# Especificación de herramientas MCP

> Problema que resuelve este archivo: define las reglas de diseño de interfaz y de descripción al exponer el conjunto de especificaciones como herramientas mediante el protocolo de contexto de modelo (MCP), con el fin de garantizar que el modelo pueda descubrir e invocar correctamente las herramientas.

## 1. Principios de diseño de herramientas

1. Responsabilidad única: una herramienta hace una sola cosa; evitar interfaces genéricas y sobredimensionadas.
2. Descripción clara: la descripción de la herramienta indica su finalidad y sus escenarios de aplicación, para que el modelo pueda determinar cuándo invocarla.
3. Parámetros explícitos: cada parámetro tiene tipo, obligatoriedad, rango de valores y descripción.
4. Salida estructurada: devolver datos estructurados, evitando prosa extensa.

## 2. Campos obligatorios

| Campo | Requisito |
| --- | --- |
| name | Identificador único, kebab-case en minúsculas |
| description | Finalidad y condiciones de activación, concretas y evaluables |
| inputSchema | Tipos de parámetro, campos obligatorios y restricciones |
| valor de retorno | Formato estructurado y descripción de campos |
| error | Formato de retorno en caso de fallo; no debe inventar resultados |

## 3. Herramientas relacionadas con el conjunto de especificaciones

1. De consulta documental: devuelven el contenido de la especificación según el código de idioma + identificador (identificadores en [Especificación de metadatos legibles por máquina](./machine-readable-metadata-specification.md)).
2. De listado: devuelven la lista de documentos disponibles y su correspondencia de idiomas.
3. De validación: comprueban la integridad de la matriz de documentación (véase [Matriz de documentación](./document-matrix.md)) y el estado de las puertas de calidad (véase [Puertas de calidad](./quality-gate.md)).

## 4. Reglas obligatorias

1. La herramienta no debe devolver como PASS un resultado que no puede verificarse; debe marcar SKIP y el motivo (véase [Prácticas prohibidas](./prohibited-practices.md)).
2. La salida debe poder ser analizada por un programa y no debe contener el proceso de razonamiento interno.
3. El contenido relacionado con seguridad no debe filtrarse a través de las herramientas (véase [Especificación de seguridad y privacidad](./security-and-privacy-specification.md)).

## Archivos relacionados

- Estructura de metadatos: [Especificación de metadatos legibles por máquina](./machine-readable-metadata-specification.md)
- Encapsulado de Skill: [Especificación de redacción de Skill](./skill-authoring-specification.md)
- Convenciones de invocación de Agent: [Especificación de invocación de Agent y de prompts](./agent-invocation-and-prompt-specification.md)
