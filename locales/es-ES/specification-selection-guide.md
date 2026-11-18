# Guía de selección de especificaciones

> Problema que resuelve este archivo: ofrece criterios de recorte de las especificaciones según el tipo de proyecto, el tamaño del equipo y la fase de publicación, y propone una combinación mínima viable y una combinación de conformidad completa, de modo que el «uso a la carta» cuente con criterios de decisión explícitos en lugar de depender del criterio personal.

El objeto de recorte de este archivo es el conjunto completo de especificaciones; las diferencias por tipo en el nivel de las secciones del README figuran en la [guía de adaptación del README por categoría](./readme-category-adaptation-guide.md), y la correspondencia completa de fases se recoge en la [tabla de correspondencia del ciclo de vida](./lifecycle-mapping-table.md).

## 1. Principios de selección

1. **Las restricciones obligatorias no admiten recorte**: las [reglas absolutas](./hard-rules.md) y las [prácticas prohibidas](./prohibited-practices.md) se aplican íntegramente en cualquier proyecto y en cualquier fase.
2. **La puerta de fase determina el mínimo**: antes de entrar en una fase debe superarse la puerta de salida que dicha fase tiene marcada en la [tabla de correspondencia del ciclo de vida](./lifecycle-mapping-table.md), y las especificaciones centrales correspondientes no deben omitirse.
3. **Las diferencias por tipo solo afectan a la profundidad**: el tipo de proyecto determina qué especificaciones se refuerzan y qué detalles se simplifican, y no constituye motivo para omitir la puerta de calidad.
4. **La degradación debe declararse explícitamente**: un repositorio privado de scripts temporales puede ejecutar solo las puertas P0, pero debe marcar el «modo degradado» en los entregables y enumerar los elementos no ejecutados.

## 2. Dimensiones de recorte

| Dimensión | Valores | Influencia principal |
| --- | --- | --- |
| Tipo de proyecto | Biblioteca / SDK, aplicación, herramienta de línea de comandos, framework, colección de recursos | Determina las especificaciones que se refuerzan y los detalles que pueden simplificarse |
| Tamaño del equipo | Persona individual, equipo pequeño, organización | Determina la necesidad de las especificaciones de gobernanza y colaboración |
| Fase de publicación | Validación de prototipo, primera publicación, mantenimiento estable | Determina el momento de introducción de las especificaciones de cumplimiento y operación |

Cuando se superponen las tres dimensiones, el valor se decide con la prioridad «restricción obligatoria → puerta de fase → fase de publicación → tipo de proyecto → tamaño del equipo»; el recorte en una dimensión de menor prioridad no debe debilitar las exigencias de una dimensión de mayor prioridad.

## 3. Recorte por tipo de proyecto

| Tipo de proyecto | Debe reforzarse | Puede simplificarse | Entregables necesarios |
| --- | --- | --- | --- |
| Biblioteca / SDK | [Especificación de diseño de API](./api-design-specification.md), [especificación de documentación de API](./api-documentation-specification.md), [especificación de gestión de versiones](./version-management-specification.md), [especificación del registro de cambios](./changelog-specification.md) | Despliegue y reversión, observabilidad (solo al distribuir artefactos), especificaciones visuales de capturas de pantalla | README, documentación de API, LICENSE, CHANGELOG |
| Aplicación | [Especificación de maquetación visual del README](./readme-visual-layout-specification.md), [especificación de accesibilidad](./accessibility-specification.md), [especificación de despliegue y reversión](./deployment-and-rollback-specification.md), [especificación de observabilidad](./observability-specification.md), [especificación de resolución de problemas](./troubleshooting-specification.md) | Documentación de API, diseño de bases de datos (cuando se usa un servicio gestionado) | README, capturas de pantalla, instrucciones de despliegue, SECURITY |
| Herramienta de línea de comandos | [Especificación de mensajes de commit](./commit-message-specification.md), [guía de redacción de características y compensaciones de ingeniería](./features-and-engineering-tradeoffs-guide.md), [guía de adaptación del README por categoría](./readme-category-adaptation-guide.md), [especificación de accesibilidad](./accessibility-specification.md) (salida de terminal) | Diseño de bases de datos, despliegue y reversión (cuando predomina la distribución por paquetes) | README, ejemplos de uso, GIF de demostración, LICENSE |
| Framework | [Matriz de documentación](./document-matrix.md), [especificación de documentación de API](./api-documentation-specification.md), [especificación de la guía de contribución](./contribution-guide-specification.md), [especificación del código de conducta](./code-of-conduct-specification.md), [especificación de observabilidad](./observability-specification.md) | Diseño de bases de datos (cuando no se incorpora almacenamiento) | README, punto de entrada de la documentación, guía de contribución, código de conducta |
| Colección de recursos | [Matriz de documentación](./document-matrix.md), [plantilla de guía de contribución](./contribution-guide-template.md), [especificación multilingüe](./multilingual-specification.md), [especificación general de redacción](./general-writing-specification.md) | Pruebas, despliegue, API, bases de datos, observabilidad | README, índice de categorías, guía de contribución, LICENSE |

Los proyectos de tipo colección de recursos no suelen contener código ejecutable, por lo que la [especificación de pruebas](./testing-specification.md) y la [especificación del flujo de trabajo de CI](./ci-workflow-specification.md) pueden marcarse como no aplicables; no obstante, deben seguir cumpliéndose la [especificación general de redacción](./general-writing-specification.md) y la [especificación de accesibilidad](./accessibility-specification.md) para garantizar la utilidad del texto de los enlaces y de la estructura de las listas.

## 4. Recorte por tamaño del equipo

| Tamaño del equipo | Especificaciones que deben añadirse | Especificaciones que pueden omitirse |
| --- | --- | --- |
| Persona individual | [Reglas absolutas](./hard-rules.md), [especificación de nombres de proyecto](./project-naming-specification.md), [plantilla estándar de README](./readme-standard-template.md), [especificación de LICENSE](./license-specification.md) | Código de conducta, propiedad del código, retrospectiva de iteración, métricas de calidad (pueden completarse antes de la primera publicación) |
| Equipo pequeño | Sobre la base individual se añaden [especificación de propiedad del código](./code-ownership-specification.md), [especificación de la guía de contribución](./contribution-guide-specification.md), [especificación del flujo de trabajo de CI](./ci-workflow-specification.md), [puerta de calidad](./quality-gate.md) | Respuesta a incidentes, observabilidad (pueden completarse tras la puesta en servicio) |
| Organización | Aplicación íntegra; además deben implantarse la [especificación de NOTICE](./notice-specification.md), la [plantilla de SECURITY](./security-template.md), la [exención de responsabilidad](./disclaimer.md), la [especificación de respuesta a incidentes](./incident-response-specification.md), la [especificación de métricas de calidad](./quality-metrics-specification.md) y la [especificación de la matriz de trazabilidad de requisitos](./requirements-traceability-matrix-specification.md) | Ninguna |

Cuando crece el tamaño del equipo, las especificaciones de gobernanza deben completarse antes de que el repositorio sea visible al exterior, sin esperar a añadirlas después de la primera publicación.

## 5. Recorte por fase de publicación

| Fase de publicación | Debe introducirse | Puede aplazarse | Requisitos de declaración |
| --- | --- | --- | --- |
| Validación de prototipo | [Reglas absolutas](./hard-rules.md), [especificación de nombres de proyecto](./project-naming-specification.md), [plantilla estándar de README](./readme-standard-template.md), [especificación general de redacción](./general-writing-specification.md) | Puerta de calidad, observabilidad, respuesta a incidentes, documentos legales | Debe marcarse el «modo degradado» y enumerarse los elementos aplazados |
| Primera publicación | Sobre la base del prototipo se añaden la [puerta de calidad](./quality-gate.md), la [especificación de conformidad de código abierto](./open-source-compliance-specification.md), la [especificación de LICENSE](./license-specification.md), la [plantilla de exención de responsabilidad](./disclaimer-template.md), la [plantilla de guía de contribución](./contribution-guide-template.md), la [plantilla de código de conducta](./code-of-conduct-template.md), la [plantilla de SECURITY](./security-template.md), la [especificación de insignias](./badge-specification.md) | Guía de migración, retrospectiva de iteración (pueden completarse tras la primera iteración de versión) | No deben omitirse los elementos P0 de la puerta |
| Mantenimiento estable | Sobre la base de la primera publicación se añaden la [especificación del registro de cambios](./changelog-specification.md), la [especificación de gestión de versiones](./version-management-specification.md), la [especificación de la guía de migración](./migration-guide-specification.md), la [especificación de observabilidad](./observability-specification.md), la [especificación de respuesta a incidentes](./incident-response-specification.md), la [especificación de resolución de problemas](./troubleshooting-specification.md), la [especificación de la retrospectiva de iteración](./iteration-retrospective-specification.md), la [especificación de la matriz de trazabilidad de requisitos](./requirements-traceability-matrix-specification.md) | Ninguna | Los cambios disruptivos deben contar con ruta de migración y anuncio |

## 6. Combinaciones

### 6.1 Combinación mínima viable

Aplicable a prototipos personales o repositorios privados de validación; consta de 10 documentos:

| Uso | Especificación |
| --- | --- |
| Restricción | [Reglas absolutas](./hard-rules.md), [prácticas prohibidas](./prohibited-practices.md) |
| Inicio del proyecto | [Especificación de inicio del proyecto y requisitos](./project-initiation-and-requirements-specification.md), [especificación de nombres de proyecto](./project-naming-specification.md) |
| Página principal | [Plantilla estándar de README](./readme-standard-template.md), [especificación general de redacción](./general-writing-specification.md) |
| Ingeniería | [Especificación de estilo de código](./code-style-specification.md), [especificación de mensajes de commit](./commit-message-specification.md), [especificación de pruebas](./testing-specification.md) |
| Publicación | [Especificación de push y publicación](./push-and-release-specification.md), [especificación de LICENSE](./license-specification.md) |

Al utilizar esta combinación debe declararse el modo degradado en los entregables y completarse la combinación íntegra de la sección 6.3 antes de la primera publicación.

### 6.2 Combinación estándar de publicación

Sobre la combinación mínima viable se completan los elementos básicos de calidad, cumplimiento, gobernanza y operación: se añaden la [puerta de calidad](./quality-gate.md), la [especificación de secciones del README](./readme-sections-specification.md), la [especificación de maquetación visual del README](./readme-visual-layout-specification.md), la [especificación de insignias](./badge-specification.md), la [matriz de documentación](./document-matrix.md), la [especificación de conformidad de código abierto](./open-source-compliance-specification.md), la [plantilla de exención de responsabilidad](./disclaimer-template.md), la [plantilla de SECURITY](./security-template.md), la [plantilla de guía de contribución](./contribution-guide-template.md), la [plantilla de código de conducta](./code-of-conduct-template.md), la [especificación del registro de cambios](./changelog-specification.md), la [especificación de gestión de versiones](./version-management-specification.md), la [especificación de accesibilidad](./accessibility-specification.md), la [especificación del flujo de trabajo de CI](./ci-workflow-specification.md), la [especificación de plantillas de Issue y PR](./issue-and-pr-template-specification.md) y la [especificación de seguridad y privacidad](./security-and-privacy-specification.md).

Esta combinación satisface todas las condiciones de liberación de las puertas A, B y C de un repositorio público y es el punto de partida recomendado para la mayoría de los proyectos.

### 6.3 Combinación de conformidad completa

Aplica la totalidad de las especificaciones y se destina a proyectos de nivel organizativo, a proyectos distribuidos en entornos regulados o a proyectos que requieren integración programática mediante expert, Skill, MCP o programas de línea de comandos. El número de documentos se rige por el [índice en chino simplificado](./README.md); al activarla deben verificarse una por una las puertas de fase de la [tabla de correspondencia del ciclo de vida](./lifecycle-mapping-table.md).

## 7. Tratamiento de conflictos

1. Cuando surja un conflicto dentro de una misma dimensión, prevalece la exigencia de la fase de publicación más avanzada; la simplificación propia de la fase de prototipo no debe prolongarse hasta la fase pública.
2. Cuando surja un conflicto entre dimensiones distintas, se aplica la prioridad de la sección 2; las restricciones obligatorias y las puertas de fase no pueden ser anuladas por ninguna dimensión.
3. Si un proyecto presenta circunstancias especiales que justifican apartarse de esta guía, deben registrarse en los entregables las especificaciones afectadas, los motivos y las medidas compensatorias, y someterse a revisión.
4. El modo degradado no debe aplicarse a repositorios públicos ni servir de base para omitir la licencia o las puertas de seguridad.

## Archivos relacionados

- Para la correspondencia completa entre fases y especificaciones, véase la [tabla de correspondencia del ciclo de vida](./lifecycle-mapping-table.md)
- Para el recorte por tipo en las secciones del README, véase la [guía de adaptación del README por categoría](./readme-category-adaptation-guide.md)
- Para las restricciones que no admiten recorte, véanse las [reglas absolutas](./hard-rules.md) y las [prácticas prohibidas](./prohibited-practices.md)
- Para las condiciones de liberación de la puerta, véase la [puerta de calidad](./quality-gate.md)
