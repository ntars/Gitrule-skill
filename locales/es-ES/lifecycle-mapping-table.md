# Tabla de correspondencia del ciclo de vida

> Problema que resuelve este archivo: asigna todas las especificaciones a las ocho fases del ciclo de vida del proyecto y precisa, para cada fase, sus condiciones de entrada, sus entregables clave, sus especificaciones centrales y su puerta de salida, de modo que constituya un único punto de navegación para tomar las especificaciones «de dentro hacia fuera y de principio a fin».

Este archivo solo responde a «qué especificaciones necesita una fase y cuándo puede pasarse a la siguiente». El articulado concreto de cada especificación dentro de una fase sigue rigiéndose por su archivo correspondiente; para el flujo operativo, véase el [proceso de ejecución](./execution-process.md), y para el recorte según el tipo de proyecto, véase la [guía de selección de especificaciones](./specification-selection-guide.md).

## 1. Visión general de las fases

| Fase | Nombre | Pregunta central | Entregables clave | Puerta de salida |
| --- | --- | --- | --- | --- |
| 1 | Inicio del proyecto | Qué se hace, cómo se llama y cómo se configura el repositorio | Conclusión de nomenclatura, tabla de metadatos del repositorio, lista de información | Nomenclatura conforme, información obligatoria completa o marcada |
| 2 | Análisis de requisitos | Qué son los requisitos y cómo se aceptan | Lista de requisitos, criterios de aceptación, matriz de trazabilidad | Cada requisito cuenta con identificador único y criterio de aceptación |
| 3 | Diseño de arquitectura | Cómo se descompone y cómo se acuerdan interfaces y datos | Documento de arquitectura, contrato de API, modelo de datos | Trazabilidad de requisitos a diseño sin omisiones, interfaces revisadas |
| 4 | Desarrollo e implementación | Cómo escribir código y hacer commits de forma coherente | Código, secuencia de commits, flujo de trabajo de CI, documentación de API | Revisión superada, CI en verde, dependencias sin vulnerabilidades graves |
| 5 | Verificación mediante pruebas | Si se alcanza la calidad necesaria para publicar | Conjunto de pruebas, informe de cobertura, dictamen de la puerta | Compilación y pruebas superadas, P0 a cero |
| 6 | Despliegue y publicación | Cómo se publica y cómo se presenta la página principal | tag, Release, documentación de la página principal, plan de reversión | Las tres puertas en verde, plan de reversión verificado |
| 7 | Operación y monitorización | Cómo se detectan los problemas y cómo se responde | Monitorización y alertas, flujo de respuesta, documentación de fallos | Indicadores clave con alerta, canales de respuesta disponibles |
| 8 | Mantenimiento iterativo | Cómo se hace la retrospectiva y cómo se evoluciona | Informe de retrospectiva, hoja de ruta actualizada, guía de migración | Acciones registradas, cambios disruptivos con ruta de migración |

Las fases 1 a 5 avanzan de dentro hacia fuera; las fases 6 a 8 pasan de la entrega a la operación y la evolución. Las fases 7 y 8 pueden ocurrir en paralelo, pero ninguna de ellas debe omitir la puerta de la fase 5.

## 2. Fase uno: inicio del proyecto

- **Objetivo de la fase**: determinar el posicionamiento del proyecto, la nomenclatura conforme y los metadatos del repositorio, y establecer la línea base de información compartida por las fases posteriores.
- **Condiciones de entrada**: la idea del proyecto está formada y ya pueden enunciarse los usuarios objetivo y el problema que se resuelve.
- **Especificaciones centrales**: [roles y responsabilidades](./roles-and-responsibilities.md), [especificación de inicio del proyecto y requisitos](./project-initiation-and-requirements-specification.md), [especificación de nombres de proyecto](./project-naming-specification.md), [recopilación de información y plantillas](./information-collection-and-templates.md), [proceso de ejecución](./execution-process.md).
- **Entregables clave**: tres candidatos de nombre y la conclusión de la búsqueda de nombres duplicados; tabla de metadatos del repositorio (descripción, etiquetas de tema, rama por defecto, visibilidad, licencia); lista de información obligatoria y lista de información faltante.
- **Puerta de salida**: el nombre del repositorio cumple todas las reglas absolutas de la [especificación de nombres de proyecto](./project-naming-specification.md); el tipo de licencia está determinado; los campos obligatorios están completos y los faltantes se han marcado conforme a [recopilación de información y plantillas](./information-collection-and-templates.md).

## 3. Fase dos: análisis de requisitos

- **Objetivo de la fase**: descomponer la idea en elementos de requisito verificables y trazables, y elaborar con ellos la hoja de ruta.
- **Condiciones de entrada**: se han confirmado las conclusiones de nomenclatura y metadatos de la fase uno.
- **Especificaciones centrales**: [especificación de inicio del proyecto y requisitos](./project-initiation-and-requirements-specification.md), [especificación de la matriz de trazabilidad de requisitos](./requirements-traceability-matrix-specification.md), [especificación de la hoja de ruta](./roadmap-specification.md), [recopilación de información y plantillas](./information-collection-and-templates.md).
- **Entregables clave**: lista de requisitos con identificadores únicos; criterios de aceptación de cada requisito; versión inicial de la matriz de trazabilidad de requisitos; hoja de ruta ordenada por prioridad.
- **Puerta de salida**: cada requisito dispone de identificador único y de un criterio de aceptación verificable; la matriz de trazabilidad ya incluye los campos del lado de requisitos; los elementos planificados de la hoja de ruta están marcados como no constitutivos de compromiso de entrega.

## 4. Fase tres: diseño de arquitectura

- **Objetivo de la fase**: determinar los límites de los módulos, los contratos de interfaz y el modelo de datos, de modo que los requisitos puedan asignarse a unidades de diseño concretas.
- **Condiciones de entrada**: se han confirmado la lista de requisitos y los criterios de aceptación.
- **Especificaciones centrales**: [especificación del documento de diseño de arquitectura](./architecture-design-document-specification.md), [especificación de diseño de API](./api-design-specification.md), [especificación de diseño de bases de datos](./database-design-specification.md), [matriz de documentación](./document-matrix.md), [especificación general de redacción](./general-writing-specification.md).
- **Entregables clave**: documento de diseño de arquitectura; contrato de API; modelo de datos y estrategia de migración; inventario de la matriz de documentación.
- **Puerta de salida**: cada requisito apunta en la matriz de trazabilidad al menos a una unidad de diseño; las interfaces y el modelo de datos han sido revisados; las responsabilidades de cada archivo de la matriz de documentación no se solapan.

## 5. Fase cuatro: desarrollo e implementación

- **Objetivo de la fase**: implementar el diseño con un estilo de código, un formato de commit y un proceso de revisión coherentes, manteniendo controlables las dependencias y la automatización.
- **Condiciones de entrada**: la arquitectura y los contratos de interfaz han superado la revisión.
- **Especificaciones centrales**: [especificación de estilo de código](./code-style-specification.md), [especificación de flujo de trabajo de Git y ramas](./git-workflow-and-branching-specification.md), [especificación de mensajes de commit](./commit-message-specification.md), [especificación de revisión de código](./code-review-specification.md), [especificación de gestión de dependencias](./dependency-management-specification.md), [especificación de propiedad del código](./code-ownership-specification.md), [especificación de documentación de API](./api-documentation-specification.md), [especificación del flujo de trabajo de CI](./ci-workflow-specification.md).
- **Entregables clave**: código conforme a la especificación de estilo; secuencia de commits conforme a Conventional Commits; flujo de trabajo de CI; documentación de API sincronizada con la implementación.
- **Puerta de salida**: los mensajes de commit y la nomenclatura de ramas cumplen la especificación; el código ha sido revisado y el enrutamiento de propiedad es correcto; el flujo de trabajo de CI pasa; las dependencias no presentan vulnerabilidades graves sin tratar.

## 6. Fase cinco: verificación mediante pruebas

- **Objetivo de la fase**: confirmar, mediante pruebas reproducibles y el dictamen de la puerta, que los entregables alcanzan la línea base de calidad necesaria para publicar.
- **Condiciones de entrada**: la funcionalidad está implementada y el flujo de trabajo de CI puede ejecutarse.
- **Especificaciones centrales**: [especificación de pruebas](./testing-specification.md), [puerta de calidad](./quality-gate.md), [especificación de métricas de calidad](./quality-metrics-specification.md), [especificación de accesibilidad](./accessibility-specification.md), [especificación de seguridad y privacidad](./security-and-privacy-specification.md).
- **Entregables clave**: conjunto de pruebas e informe de cobertura; resultado del dictamen de la puerta punto por punto; registro de comprobaciones de seguridad y accesibilidad.
- **Puerta de salida**: la compilación, las pruebas y el análisis estático pasan; los elementos P0 de las puertas A, B y C están todos a cero; los elementos P1 están registrados como pendientes o completados.

## 7. Fase seis: despliegue y publicación

- **Objetivo de la fase**: publicar la versión mediante un proceso controlado y completar la documentación de la página principal y los entregables visibles para el usuario.
- **Condiciones de entrada**: la puerta de la fase cinco ha pasado y no quedan elementos P0 sin cerrar.
- **Especificaciones centrales**: [especificación de push y publicación](./push-and-release-specification.md), [especificación de gestión de versiones](./version-management-specification.md), [especificación del registro de cambios](./changelog-specification.md), [especificación de despliegue y reversión](./deployment-and-rollback-specification.md), [especificación de la guía de migración](./migration-guide-specification.md), [especificación del flujo de trabajo de CI](./ci-workflow-specification.md), [especificación de plantillas de Issue y PR](./issue-and-pr-template-specification.md); para la documentación de la página principal, véanse la [plantilla estándar de README](./readme-standard-template.md), la [especificación de secciones del README](./readme-sections-specification.md), la [especificación de maquetación visual del README](./readme-visual-layout-specification.md), la [especificación de insignias](./badge-specification.md) y la [guía de adaptación del README por categoría](./readme-category-adaptation-guide.md).
- **Entregables clave**: versión semántica y etiqueta anotada; Release Notes y registro de cambios; README de la página principal y plantillas de comunidad; registro de despliegue y plan de reversión.
- **Puerta de salida**: las tres puertas están en verde; la etiqueta es annotated y cumple SemVer; el plan de reversión ha sido verificado; la documentación de la página principal no contiene rutas absolutas locales ni marcadores de posición residuales.

## 8. Fase siete: operación y monitorización

- **Objetivo de la fase**: establecer la capacidad de observabilidad y el mecanismo de respuesta, de modo que los problemas en producción puedan detectarse, localizarse y atenderse.
- **Condiciones de entrada**: la versión se ha publicado y el servicio o artefacto está disponible.
- **Especificaciones centrales**: [especificación de observabilidad](./observability-specification.md), [especificación de respuesta a incidentes](./incident-response-specification.md), [especificación de resolución de problemas](./troubleshooting-specification.md), [especificación de seguridad y privacidad](./security-and-privacy-specification.md), [plantilla de SECURITY](./security-template.md), [exención de responsabilidad](./disclaimer.md), [plantilla de exención de responsabilidad](./disclaimer-template.md).
- **Entregables clave**: indicadores clave y reglas de alerta; clasificación de incidentes y flujo de respuesta; documentación de preguntas frecuentes y resolución de problemas; canal de recepción de vulnerabilidades.
- **Puerta de salida**: todos los indicadores clave tienen alerta configurada; el canal de reporte de vulnerabilidades está disponible y verificado; el flujo de respuesta a incidentes ha completado al menos un simulacro o una simulación de mesa.

## 9. Fase ocho: mantenimiento iterativo

- **Objetivo de la fase**: hacer la retrospectiva de la iteración entregada, gestionar la ruta de evolución y mantener la alineación continua entre requisitos, diseño y pruebas.
- **Condiciones de entrada**: se ha completado al menos una publicación o un ciclo de iteración.
- **Especificaciones centrales**: [especificación de la retrospectiva de iteración](./iteration-retrospective-specification.md), [especificación de la hoja de ruta](./roadmap-specification.md), [especificación de la matriz de trazabilidad de requisitos](./requirements-traceability-matrix-specification.md), [especificación del registro de cambios](./changelog-specification.md), [especificación de la guía de migración](./migration-guide-specification.md), [especificación de gestión de versiones](./version-management-specification.md), [especificación de promoción de código abierto](./open-source-promotion-specification.md).
- **Entregables clave**: informe de retrospectiva de la iteración y acciones; hoja de ruta y matriz de trazabilidad actualizadas; guía de migración para cambios disruptivos; registro de cambios de versión.
- **Puerta de salida**: las acciones de la ronda anterior tienen responsable y plazo registrados; los cambios disruptivos cuentan con ruta de migración y anuncio; la matriz de trazabilidad no presenta enlaces rotos.

## 10. Especificaciones transversales

Las siguientes especificaciones no pertenecen a una sola fase y deben mantenerse vigentes en todas ellas:

| Categoría | Especificación | Forma de vigencia |
| --- | --- | --- |
| Restricción obligatoria | [Reglas absolutas](./hard-rules.md), [prácticas prohibidas](./prohibited-practices.md) | Su infracción en cualquier fase bloquea y no admite exención por motivos de plazo |
| Proceso y terminología | [Roles y responsabilidades](./roles-and-responsibilities.md), [proceso de ejecución](./execution-process.md), [glosario](./glossary.md) | Unifica el reparto de roles, la terminología de las fases y el orden de entrega |
| Comunidad y gobernanza | [Especificación de la guía de contribución](./contribution-guide-specification.md), [plantilla de guía de contribución](./contribution-guide-template.md), [especificación del código de conducta](./code-of-conduct-specification.md), [plantilla de código de conducta](./code-of-conduct-template.md) | Se completa antes de que el repositorio sea visible al exterior y después se ajusta con la escala de la comunidad |
| Legal y cumplimiento | [Especificación de conformidad de código abierto](./open-source-compliance-specification.md), [especificación de LICENSE](./license-specification.md), [especificación de NOTICE](./notice-specification.md), [exención de responsabilidad](./disclaimer.md), [plantilla de exención de responsabilidad](./disclaimer-template.md) | La licencia se determina en la fase uno y todos los documentos legales se completan antes de la fase seis |
| Redacción y multilingüismo | [Especificación general de redacción](./general-writing-specification.md), [especificación multilingüe](./multilingual-specification.md), [guía de redacción de características y compensaciones de ingeniería](./features-and-engineering-tradeoffs-guide.md), [matriz de documentación](./document-matrix.md) | Acompaña toda la producción documental y garantiza la coherencia de la expresión |
| Integración programática | [Especificación de metadatos legibles por máquina](./machine-readable-metadata-specification.md), [especificación de autoría de Skills](./skill-authoring-specification.md), [especificación de herramientas MCP](./mcp-tool-specification.md), [especificación de invocación de agentes y prompts](./agent-invocation-and-prompt-specification.md) | Se superpone cuando se requiere invocación mediante expert, Skill, MCP o línea de comandos |

## 11. Degradación y retroceso

1. Un repositorio privado de scripts temporales puede degradarse a ejecutar solo las puertas P0, pero debe declarar el «modo degradado» en los entregables y explicar los elementos no ejecutados.
2. Si la puerta de salida de una fase no se supera, no debe pasarse a la siguiente; los problemas, responsabilidades y acciones deben registrarse conforme al [formato del informe de auditoría](./audit-report-format.md).
3. Si se detecta un problema P0 después de la fase seis, debe volverse a la fase cinco para un nuevo dictamen y, si es necesario, ejecutar el procedimiento de gestión de incidentes de la [especificación de push y publicación](./push-and-release-specification.md).

## Archivos relacionados

- Para el flujo operativo dentro de cada fase, véase el [proceso de ejecución](./execution-process.md)
- Para el recorte de especificaciones según el tipo de proyecto, véase la [guía de selección de especificaciones](./specification-selection-guide.md)
- Para los criterios de dictamen de la puerta, véase la [puerta de calidad](./quality-gate.md)
- Para el formato de registro de problemas de auditoría, véase el [formato del informe de auditoría](./audit-report-format.md)
