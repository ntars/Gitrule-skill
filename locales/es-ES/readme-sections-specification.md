# Especificación de secciones del README

> Problema que resuelve este archivo: define las 20 secciones que debe incluir el README de cada directorio de idioma, el contenido que cada sección debe incluir y no debe incluir, así como el formato estándar de la línea de copyright.

## 1. Requisitos generales de las secciones

Las siguientes 20 secciones deben existir todas, en orden fijo, y corresponderse una a una en cada versión de idioma.

| Número | Sección | Debe incluir | No debe aparecer |
| --- | --- | --- | --- |
| 1 | Nombre y posicionamiento del proyecto | Nombre del proyecto, descripción del repositorio (formato bilingüe combinado `idioma nacional \| inglés`), etiquetas de tema (completar las 20, solo en inglés), posicionamiento en una frase, enlaces de cambio de idioma, versión actual, estado de mantenimiento | Adjetivos vacíos; descripción del repositorio de más de 120 caracteres; etiquetas de tema con mayúsculas y minúsculas mezcladas o con palabras que no sean en inglés |
| 2 | Introducción al proyecto | Antecedentes, problema por resolver, idea central, escenarios de aplicación, escenarios no aplicables, y ventajas y limitaciones presentadas por separado (las limitaciones deben incluir el alcance de impacto y la forma de elusión) | Resumirlo en una frase; enumerar solo ventajas sin limitaciones |
| 3 | Funcionalidades principales | Entradas de funcionalidad agrupadas por módulo, cada una con condición de activación y resultado | Enumerar solo nombres de funcionalidad |
| 4 | Características principales | Desarrolladas según la estructura de [redacción de características y decisiones de ingeniería](./features-and-engineering-tradeoffs-guide.md) | Elogios sin evidencia |
| 5 | Detalles de diseño y decisiones de ingeniería | Desarrollados según la estructura de [redacción de características y decisiones de ingeniería](./features-and-engineering-tradeoffs-guide.md) | Descripciones duplicadas con la funcionalidad |
| 6 | Pila tecnológica y lista de dependencias | Entorno de ejecución, compilación, cadena de herramientas de pruebas y restricciones de versión; el detalle de dependencias apunta al NOTICE | Falta de número de versión |
| 7 | Instalación y despliegue | Requisitos de entorno, pasos de instalación, comandos de verificación, forma de actualización y desinstalación, explicación de contenedorización | Omitir pasos o la verificación |
| 8 | Inicio rápido | Ejemplo mínimo ejecutable, con comandos completos y salida esperada | Pseudocódigo no ejecutable |
| 9 | Explicación de la configuración | Tabla de elementos de configuración (nombre de clave, tipo, valor predeterminado, obligatoriedad, rango de valores, función, ejemplo), prioridad de configuración, soporte de actualización en caliente | Falta de valor predeterminado |
| 10 | API o explicación de módulos | Firma de la interfaz, parámetros, valor de retorno, códigos de error, ejemplo de llamada, limitación de frecuencia y cuota | Falta de códigos de error |
| 11 | Estructura de directorios | Estructura de árbol y responsabilidad de cada nivel | Enumeración archivo por archivo sin explicación |
| 12 | Rendimiento | Entorno de prueba, método de prueba, datos de métricas, análisis de cuellos de botella, recomendaciones de ajuste | Cifras sin condiciones de prueba |
| 13 | Seguridad y privacidad | Recogida y almacenamiento de datos, cifrado en tránsito, modelo de permisos, canal de notificación de vulnerabilidades, riesgos conocidos | Prometer seguridad absoluta |
| 14 | Explicación de compatibilidad | Matriz de versiones de sistema operativo, entorno de ejecución, navegador y base de datos, con indicación explícita de lo no soportado | Expresiones ambiguas |
| 15 | Problemas conocidos y limitaciones | Problemas conocidos (descripción, alcance de impacto, solución temporal, enlace de seguimiento), limitaciones actuales, lista de funcionalidades no implementadas (funcionalidad, motivo de no implementación, estado de la planificación) | Ocultar defectos graves; presentar como implementada una funcionalidad no implementada |
| 16 | Registro de cambios | Siguiendo la estructura de Keep a Changelog, con números de versión según versionado semántico | Entradas sin fecha |
| 17 | Hoja de ruta posterior | Elementos planificados, estado, versión objetivo, con la marca «no es un compromiso» | Prometer fechas de entrega |
| 18 | Participación y contribución | Preparación del entorno de desarrollo, modelo de ramas, especificación de commits, requisitos de PR, código de conducta, plantillas de Issue | Escribir solo «se aceptan PR» |
| 19 | Copyright y licencia | Línea de copyright, nombre de la licencia, identificador SPDX, ubicación del texto completo de la licencia | Falta del titular de los derechos |
| 20 | Declaración de cumplimiento NOTICE | Resumen de dependencias de terceros, enlace relativo al archivo NOTICE | Sustituir el NOTICE por esta sección |

## 1.1 Las cuatro preguntas de la primera pantalla y el texto en una frase

La primera pantalla del README debe responder cuatro preguntas, en orden fijo:

1. qué hace el proyecto;
2. qué problema resuelve el proyecto;
3. qué características tiene el proyecto;
4. el ejemplo mínimo de hello world.

La primera pregunta corresponde al «posicionamiento en una frase» y debe cumplir tres condiciones a la vez: indicar el tipo de proyecto, tener calificativos precisos y poder repetirse directamente. Los textos públicos de proyectos maduros pueden servir de referencia:

| Proyecto | Texto en una frase | Análisis de la estructura |
| --- | --- | --- |
| Angular | One framework. Mobile & desktop. | Categoría + alcance de cobertura |
| React | A declarative, efficient, and flexible JavaScript library for building user interfaces. | Tres calificativos + categoría + uso |
| Vue | A progressive, incrementally-adoptable JavaScript framework for building UI on the web. | Dos características + categoría + uso |

Restricciones de redacción:

- No deben usarse adjetivos sin información como «potente», «excelente» o «revolucionario»;
- Debe indicarse la palabra de categoría (biblioteca, marco de trabajo, herramienta, aplicación) para que el lector pueda clasificarlo de un vistazo;
- Los calificativos de características no deben superar tres, evitando la acumulación;
- La versión en chino debe mantenerse dentro de 60 caracteres y la versión en inglés dentro de 25 palabras.

La tercera pregunta, «qué características tiene», debe revelar al mismo tiempo los escenarios no aplicables. Ejemplo de redacción eficaz: indicar que cierto middleware de mensajería «solo admite el nivel de QoS 0, por lo que no es aplicable a escenarios que requieren el nivel 1»; la redacción ineficaz consiste en enumerar solo ventajas. La comparación de características debe basarse en hechos verificables y no debe menospreciar proyectos similares.

El ejemplo de hello world de la cuarta pregunta debe permitir completar la instalación y la ejecución en dos pasos; los proyectos con pasos de instalación engorrosos deberían ofrecer una imagen de contenedor o un entorno de demostración en línea, para que el lector no abandone tras leer el README.

## 2. Formato estándar de la línea de copyright

```text
Copyright © {{年份}} {{著作权人}}. Licensed under {{SPDX 标识符}}.
```

## Archivos relacionados

- Para los límites del contenido de las secciones, véase la [matriz de documentación](./document-matrix.md)
- Para las reglas de descripción del repositorio y etiquetas de tema, véase la sección 5 de la [especificación de nombres de proyecto](./project-naming-specification.md)
- Para la coherencia entre las versiones en chino e inglés, véase la [especificación de multilenguaje](./multilingual-specification.md)
- Para el NOTICE al que apunta el detalle de dependencias, véase la [especificación de NOTICE](./notice-specification.md)
- Para los estándares de redacción, véase la [especificación general de redacción](./general-writing-specification.md)
