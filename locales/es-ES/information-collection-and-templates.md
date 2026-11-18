# Recopilación de información y plantillas

> Problema que resuelve este archivo: define los campos de información del proyecto que deben recopilarse antes de redactar la documentación, las reglas de marcado de la información no confirmada, y proporciona un índice de marcadores de posición, una plantilla de correspondencia terminológica, una plantilla de inventario de dependencias y un cuerpo de recopilación de información del proyecto directamente copiable.

## 1. Campos obligatorios (su ausencia bloquea)

| Campo | Descripción | Capítulos afectados |
| --- | --- | --- |
| Nombre del proyecto | Nombre del repositorio y nombre de presentación; si no coinciden, debe explicarse | Documento completo |
| Posicionamiento en una frase | No más de 60 caracteres; indica qué es el proyecto y qué problema resuelve y para quién | Capítulo 1 |
| Descripción del repositorio (idioma nacional e inglés) | Cada idioma no más de 120 caracteres; indican respectivamente el tipo de proyecto y su uso principal | Capítulo 1 |
| Etiquetas de temas | Completar 20 palabras en inglés minúsculas, unidas por `-`; la mezcla de mayúsculas y minúsculas o el uso de otros idiomas se considera campo ausente | Capítulo 1 |
| Contexto del proyecto | Motivo del inicio del proyecto y carencias de las soluciones existentes | Capítulo 2 |
| Lista de funciones principales | Agrupada por módulos, con los comportamientos perceptibles por el usuario | Capítulo 3 |
| Pila tecnológica | Lenguaje, framework y restricciones de versión del entorno de ejecución | Capítulo 6 |
| Inventario de dependencias | Nombre, versión, licencia, titular de los derechos, dirección de origen | Capítulo 6, NOTICE |
| Tipo de licencia | Licencia del propio proyecto; debe ser un identificador SPDX | Capítulo 19 |
| Titular de los derechos | Nombre personal o denominación completa de la organización, y año | Capítulo 19, NOTICE |
| Forma de instalación y ejecución | Requisitos del entorno, comandos, resultados esperados | Capítulos 7 y 8 |

## 2. Campos opcionales

Lista de opciones de configuración, definición de API, estructura de directorios, datos de pruebas de rendimiento, matriz de compatibilidad, problemas conocidos, registro de cambios, hoja de ruta, flujo de contribución, política de seguridad, capturas de pantalla y dirección de demostración, origen de materiales externos.

## 3. Instrucciones de cumplimentación y ejemplos

| Campo | Instrucción de cumplimentación | Ejemplo |
| --- | --- | --- |
| Nombre del proyecto | El nombre del repositorio usa letras minúsculas, dígitos y `-`; el nombre de presentación puede usar la grafía de marca; si no coinciden, indicar el motivo | Nombre del repositorio `markdown-lint-cli`, nombre de presentación `Markdown Lint CLI` |
| Posicionamiento en una frase | Incluye el término de categoría y el calificador, sin acumular adjetivos, no más de 60 caracteres | `Herramienta de línea de comandos para la verificación de normas Markdown destinada a equipos de documentación técnica` |
| Descripción del repositorio (idioma nacional e inglés) | El idioma nacional y el inglés forman cada uno una frase independiente, ninguno supera los 120 caracteres y no se sustituye la descripción por un eslogan | `Español: herramienta de línea de comandos para verificar la estructura de documentos Markdown` / `English: A CLI tool for checking Markdown document structure` |
| Etiquetas de temas | Todas en inglés minúsculas, palabras unidas por `-`, completar 20 y cubrir por completo lenguaje, forma, uso, ecosistema y escenarios | `go cli markdown linter developer-tools` |
| Pila tecnológica | Indicar el lenguaje principal, el framework y las restricciones de versión del entorno de ejecución; no escribir «última versión» | `Go >= 1.22; Cobra v1.8.x` |
| Inventario de dependencias | Cada entrada incluye versión, licencia, titular de los derechos y dirección oficial; si el origen es desconocido, marcarlo como elemento no confirmado | Véase la plantilla de tabla del inventario de dependencias del apéndice C |
| Tipo de licencia | Usar el identificador SPDX; no emplear formulaciones vagas como «código abierto» o «de uso libre» | `MIT` |
| Forma de instalación y ejecución | Aportar el directorio de trabajo actual, el comando completo y la salida esperada verificable | Ejecutar `go install ./cmd/mdlint` en la raíz del repositorio; se muestra el número de versión |
| Elementos no confirmados | Usar la marca fija, indicar el contenido faltante y el responsable de completarlo; no sustituir por «provisional» | `【pendiente de confirmación: tipo de licencia de la dependencia foo, responsable: Zhang San】` |

## 4. Reglas de marcado de la información no confirmada

1. Formato unificado: `【pendiente de confirmación: qué falta concretamente】`; no deben usarse como sustituto formulaciones vagas como «provisional», «aproximadamente» o «posiblemente».
2. Ubicación del marcado: una vez en el lugar correspondiente del cuerpo del texto y otra vez en el «Resumen de puntos pendientes de confirmación» al final del documento.
3. Los elementos no confirmados relativos a licencia, derechos de autor u origen de dependencias deben marcarse expresamente en NOTICE; no debe omitirse la entrada completa.
4. El resumen de puntos pendientes de confirmación debe incluir número, campo, contenido faltante, responsable de completarlo y fecha prevista de finalización; las entradas sin responsable ni fecha no pueden entrar en la fase 0 (véase [Flujo de ejecución](./execution-process.md)).

## 5. Apéndice A · Índice de marcadores de posición

`{{项目名称}}`、`{{一句话定位}}`、`{{当前版本}}`、`{{维护状态}}`、`{{许可证 SPDX}}`、`{{著作权人}}`、`{{年份}}`、`{{分支名}}`、`{{仓库地址}}`、`{{最低运行时版本}}`

Reglas de uso:

1. Este índice solo enumera los campos básicos de la fase de recopilación; el conjunto completo de marcadores de posición del README y sus descripciones se rigen por la tabla de correspondencia de marcadores de posición de la [Plantilla estándar de README](./readme-standard-template.md).
2. Los marcadores de posición formales se escriben de forma unificada como `{{纯名}}`; no debe anidarse texto explicativo, comillas invertidas ni un segundo marcador de posición dentro de las llaves; el contenido en lenguaje natural entre llaves que aparece en los ejemplos de la especificación no se considera un marcador de posición formal.
3. Los campos en lenguaje natural de la tabla de recopilación no usan directamente marcadores de posición; al generar el README se mapean según la tabla de correspondencia, y en el documento final no debe quedar ningún contenido explicativo entre llaves.

## 6. Apéndice B · Plantilla de tabla de correspondencia terminológica chino-inglés

| Chino | English | Abreviatura | Descripción |
| --- | --- | --- | --- |
| pendiente | TBD | — | — |

## 7. Apéndice C · Plantilla de tabla del inventario de dependencias

| N.º | Nombre del componente | Versión | Forma de referencia | Titular de los derechos | Licencia | Dirección oficial | Uso en este proyecto | ¿Modificado? | Descripción de la modificación | Ubicación del texto original |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pendiente | pendiente | Directa | pendiente | pendiente | pendiente | pendiente | No | Ninguna | pendiente |

Los requisitos de los campos se indican en la [Especificación de cumplimiento de código abierto](./open-source-compliance-specification.md).

## 8. Sección de cumplimentación de la información del proyecto

Tras completar la información del proyecto a continuación, iniciar la fase 0 (véase [Flujo de ejecución](./execution-process.md)).

- Nombre del proyecto:
- Posicionamiento en una frase:
- Descripción del repositorio (idioma nacional e inglés):
- Etiquetas de temas:
- Contexto del proyecto:
- Funciones principales:
- Pila tecnológica y versiones:
- Inventario de dependencias (o ruta del archivo de inventario de dependencias):
- Tipo de licencia:
- Titular de los derechos y año:
- Forma de instalación y ejecución:
- Dirección del repositorio y rama de destino:
- Otros materiales complementarios:

## 9. Apéndice D · Cuerpo copiable de recopilación de información del proyecto

Copiar el contenido siguiente en el archivo `项目信息采集表.md` del proyecto de destino y sustituir elemento por elemento el contenido posterior a «Completar:». Los campos que no puedan confirmarse se marcan según las reglas de la sección 4 y se resumen en la sección 8.

````markdown
# Tabla de recopilación de información del proyecto

> Este archivo sirve para recopilar de una sola vez la información necesaria para generar la documentación. Una vez completado, se genera el README, el NOTICE y el resto de documentos entregables a partir de los resultados de la recopilación.

## 1. Información básica

| Campo | Contenido a completar |
| --- | --- |
| Nombre del repositorio | Completar: nombre del repositorio formado por letras minúsculas, dígitos y guiones |
| Nombre de presentación | Completar: nombre del proyecto de cara al exterior; si coincide con el nombre del repositorio, escribir «igual que el nombre del repositorio» |
| Dirección del repositorio | Completar: dirección HTTPS completa |
| Rama de destino | Completar: nombre de la rama por defecto |
| Código de idioma | Completar: código de idioma prioritario, por ejemplo zh-CN |
| Versión actual | Completar: número de versión semántica o «no publicada» |
| Estado de mantenimiento | Completar: mantenimiento activo / mantenimiento de baja frecuencia / archivado |

## 2. Posicionamiento y ámbito de aplicación

| Campo | Contenido a completar |
| --- | --- |
| Posicionamiento en una frase | Completar: no más de 60 caracteres, con término de categoría y calificador |
| Descripción del repositorio (idioma nacional) | Completar: no más de 120 caracteres |
| Descripción del repositorio (English) | Completar: no más de 120 caracteres |
| Etiquetas de temas | Completar: 20 palabras en inglés minúsculas, unidas por guiones |
| Contexto del proyecto | Completar: motivo del inicio del proyecto y carencias de las soluciones existentes |
| Escenarios aplicables | Completar: enumerar uno por uno, cada uno con su condición de activación |
| Escenarios no aplicables | Completar: enumerar uno por uno, cada uno con su motivo |
| Ventajas | Completar: cada una con una base verificable |
| Limitaciones | Completar: cada una con su ámbito de impacto y forma de evitarla |

## 3. Funciones y características

| Módulo | Comportamiento perceptible por el usuario | Condición de activación | Resultado | Evidencia o enlace |
| --- | --- | --- | --- | --- |
| Completar: nombre del módulo | Completar: descripción del comportamiento | Completar: forma de activación | Completar: salida o cambio de estado | Completar: enlace a pruebas, capturas o documentación |

## 4. Tecnología y dependencias

| Campo | Contenido a completar |
| --- | --- |
| Lenguaje principal y restricciones de versión | Completar: por ejemplo `Go >= 1.22` |
| Framework y herramientas de compilación | Completar: nombre y restricciones de versión |
| Requisitos de entorno de ejecución y sistema | Completar: sistema operativo, entorno de ejecución, navegador o versión de base de datos |
| Inventario de dependencias | Completar: ruta del archivo de inventario de dependencias, o insertar en esta sección la tabla del apéndice C |
| Materiales externos | Completar: origen y licencia de tipografías, imágenes, iconos y conjuntos de datos |

## 5. Entrega y uso

| Campo | Contenido a completar |
| --- | --- |
| Requisitos del entorno | Completar: condiciones necesarias antes de la instalación |
| Comando de instalación | Completar: comando completo con indicación del directorio de trabajo actual |
| Comando de verificación y salida esperada | Completar: comando directamente ejecutable y resultado verificable |
| Forma de actualización y desinstalación | Completar: comandos o pasos de la operación |
| Lista de opciones de configuración | Completar: nombre de la clave, tipo, valor por defecto, obligatoriedad, rango de valores y función |
| Descripción de API o módulos | Completar: firma de la interfaz, parámetros, valor de retorno, códigos de error y ejemplo de llamada |
| Matriz de compatibilidad | Completar: combinaciones de versiones admitidas y no admitidas de forma explícita |
| Datos de rendimiento | Completar: entorno de prueba, método, métricas y cuellos de botella; si no hay datos, escribir «no aportados, no debe inferirse» |

## 6. Riesgos y límites

| Campo | Contenido a completar |
| --- | --- |
| Problemas conocidos | Completar: descripción, ámbito de impacto, solución provisional y enlace de seguimiento |
| Limitaciones actuales | Completar: lo que la versión actual no puede hacer, de forma explícita |
| Funciones no implementadas | Completar: función, motivo de no implementación y estado previsto |
| Seguridad y privacidad | Completar: recopilación, almacenamiento y transmisión de datos, modelo de permisos y riesgos conocidos |
| Canal de notificación de vulnerabilidades | Completar: correo electrónico, plantilla de Issue o dirección específica |

## 7. Cumplimiento y responsabilidad

| Campo | Contenido a completar |
| --- | --- |
| Tipo de licencia | Completar: identificador SPDX, por ejemplo `MIT` |
| Titular de los derechos | Completar: nombre personal o denominación completa de la organización |
| Año de los derechos de autor | Completar: año o intervalo de años |
| Ubicación del texto completo de la licencia | Completar: ruta del archivo LICENSE |
| Ruta del archivo NOTICE | Completar: ruta del archivo NOTICE; si no hay dependencias de terceros, escribir «no aplicable, motivo: ……» |
| Exención de responsabilidad | Completar: límites de responsabilidad o adopción de cláusulas de no garantía |

## 8. Resumen de puntos pendientes de confirmación

| Número | Campo | Contenido faltante | Responsable de completarlo | Fecha prevista de finalización | Ámbito de impacto |
| --- | --- | --- | --- | --- | --- |
| T-001 | Completar: nombre del campo | Completar: qué falta concretamente | Completar: nombre o rol | Completar: AAAA-MM-DD | Completar: capítulos o puertas de calidad afectados |

## 9. Especificaciones relacionadas

- Estructura de capítulos: [Especificación de secciones del README](./readme-sections-specification.md)
- Plantilla copiable: [Plantilla estándar de README](./readme-standard-template.md)
- Detalle de los campos de dependencias: [Especificación de cumplimiento de código abierto](./open-source-compliance-specification.md)
- Determinación de puertas de calidad: [Puertas de calidad](./quality-gate.md)
````

## Archivos relacionados

- Las reglas de preguntas y las condiciones de entrada a la fase 0 se indican en [Flujo de ejecución](./execution-process.md)
- La correspondencia de capítulos afectados se indica en [Especificación de secciones del README](./readme-sections-specification.md)
- La correspondencia completa de marcadores de posición del README se indica en [Plantilla estándar de README](./readme-standard-template.md)
- El detalle de los campos de dependencias se indica en [Especificación de cumplimiento de código abierto](./open-source-compliance-specification.md)
- El resumen de puntos pendientes de confirmación pertenece a la puerta G12; véase [Puertas de calidad](./quality-gate.md)
