# Especificación de plantillas del manual de desarrollo

> Problema que resuelve este archivo: define el esqueleto del manual de desarrollo en dos fases «redacción en la nube, ejecución local», el formato de las tarjetas de tarea, el protocolo de transferencia y las puertas de comprobación, de modo que una misma idea pueda ser transcrita por el modelo de la nube en tarjetas de tarea sin ambigüedad y ejecutada por relevos parciales por el modelo de codificación local.

## 1. Posicionamiento y flujo de uso

1. Esta especificación se orienta al escenario de reparto «un modelo de razonamiento en la nube + un modelo de codificación local»: la nube se encarga de transcribir las ideas difusas en planes claros y lo local se encarga de ejecutarlos de forma determinista.
2. El flujo de uso se fija en cuatro pasos, y su orden no admite saltos:
   - Verificación previa: comprobar si la idea contiene premisas erróneas, saltos lógicos o información faltante; si falta información, preguntar primero al usuario, está prohibido inventarla.
   - Redacción en la nube: explorar las soluciones de código abierto conforme a la sección 9 y rellenar el manual.
   - Revisión del usuario: revisar con especial atención los comandos de aceptación, el registro de adopciones y las zonas prohibidas.
   - Ejecución local: inyectar los capítulos y los registros de transferencia correspondientes según el índice legible por máquina y ejecutar parte por parte.
3. En el cuerpo del manual está prohibido el uso de palabras vagas como «etcétera», «relacionado», «adecuado», «en lo posible», «cuando sea necesario»; en cada caso se dará o bien un valor preciso, o bien una regla de decisión.

## 2. Esqueleto del manual

Cada manual de desarrollo contiene fijas las siguientes partes, en orden invariable:

| Parte | Responsabilidad |
| --- | --- |
| Índice legible por máquina | Tabla de navegación de rutas de capítulos, directorios de código correspondientes, comandos de aceptación y marcas de fase |
| Registro de adopciones | Tabla de registro de la cadena de suministro de código abierto, única fuente de verdad de todo el proyecto (véase la sección 11) |
| Constitución del proyecto | Invariantes de todo el proyecto, inyectada obligatoriamente en cada parte |
| Glosario | Correspondencia entre términos y explicaciones llanas, y con el código correspondiente |
| Capítulos de módulo | Un capítulo por módulo, redactado según la estructura de la sección 4 |
| Capítulo de distribución | Normativa de compilación y distribución; las acciones de publicación requieren confirmación del usuario |
| Capítulo de textos del sitio web | Normativa de textos orientada a usuarios corrientes, no se inyecta al modelo local |
| Registro de cambios | Fecha, capítulo, cambio y quien decide |

## 3. Constitución del proyecto

La constitución del proyecto es el conjunto de invariantes inyectado obligatoriamente en cada parte de ejecución local, y contiene fijas cinco entradas:

1. Pila tecnológica y versiones: precisas hasta el número de versión.
2. Convención de estructura de directorios: diagrama en árbol más una frase de responsabilidad por cada directorio.
3. Normativa de codificación: recortada según el tipo de proyecto; la línea base es carga bajo demanda modular, código mínimo y más directo, sin añadir funciones no solicitadas, comentarios completos y con los conceptos técnicos explicados en lenguaje llano; los proyectos de interfaz siguen las Apple HIG, la unidad tipográfica es siempre px o rem, y está prohibido usar rpx.
4. Zonas prohibidas globales: lo que jamás se permite hacer, por ejemplo no introducir dependencias que no estén en el registro de adopciones ni modificar archivos de contrato.
5. Normativa de idioma de salida: las explicaciones, los registros, el progreso y los mensajes de error se redactan en chino simplificado; el código, los comandos, las rutas de archivo y los nombres propios pueden conservarse en su forma original.

## 4. Estructura del capítulo de módulo

Cada capítulo de módulo contiene fijas nueve secciones, en orden invariable:

| Sección | Responsabilidad |
| --- | --- |
| Responsabilidad del módulo | De 1 a 3 frases que aclaren qué hace y qué no hace |
| Soluciones de código abierto de las que depende | Nombre, uso y número del registro de adopciones |
| Lista de archivos | Ruta, acción (crear/modificar/solo lectura) y responsabilidad; el total no excede de 10 archivos, si se supera se divide el capítulo |
| Contrato de interfaz | Firmas, rutas y campos de protocolo precisos hasta el tipo, con ejemplos completos de entrada y salida |
| Datos y estado | Qué se almacena, dónde y en qué formato; los conceptos técnicos se explican en lenguaje llano |
| Relaciones de dependencia | Tres listas de archivos: los que hay que leer antes, los que se invocarán y los que jamás se modifican |
| Tarjeta de tarea | Las partes en que se divide el módulo, cada tarjeta se ejecuta de forma independiente |
| Zonas prohibidas del capítulo | Lo que en este módulo se prohíbe hacer de manera especial |
| Notas de diseño | Motivos de la selección, soluciones descartadas, distinción entre hechos y conjeturas; no se inyectan al modelo local |

## 5. Formato de la tarjeta de tarea

Una tarjeta de tarea equivale a una sesión local y equivale a un comando de aceptación; los campos son fijos:

| Campo | Requisito |
| --- | --- |
| Objetivo | Una frase, verificable por máquina |
| Precondiciones | La parte anterior y los archivos de los que depende existen ya |
| Pasos | Enumerados con números, cada paso una acción determinista, realizada de una vez sin interrupciones ni preguntas |
| Comando de aceptación | Copiable y ejecutable directamente; cuando aún no existe un sistema de aceptación, la primera tarjeta debe construir primero el comando de aceptación |
| Resultado esperado | Salida exacta, código de salida o número de aserciones |
| Tratamiento del fallo | Disposición enumerada por cada error típico; tras 3 fallos consecutivos hay que detenerse y escribirlo en el registro de transferencia |
| Requisitos de transferencia | Declara los campos que deben escribirse obligatoriamente en el registro de transferencia |

Restricciones estrictas:

1. Si una tarjeta toca más de 10 archivos, se divide la tarjeta; si un capítulo supera las 6 tarjetas, se divide el capítulo.
2. Toda tarjeta que implique una autoverificación de la entrega debe enumerar explícitamente la limpieza de código redundante y los puntos de sincronización con README, NOTICE y LICENSE.
3. Las acciones que impliquen eliminar o sobrescribir archivos se detienen siempre, se escriben en el campo block del registro de transferencia y se espera la confirmación del usuario.
4. Las tareas tan vagas que no permiten escribir un comando de aceptación no pueden rellenarse en tarjeta; se marcan aparte como «requiere decisión del usuario».

## 6. Protocolo de transferencia PROGRESS

El archivo de registro de transferencia PROGRESS.md es la única fuente de verdad entre parte y parte; su formato es fijo:

| Campo | Requisito |
| --- | --- |
| done | Si se alcanzó el objetivo de esta tarjeta |
| files | Lista real de archivos modificados |
| decisions | Decisiones tomadas durante el proceso, con el formato «se eligió A, porque B» |
| next | Número de la siguiente tarjeta y su punto de entrada; debe escribirse la ruta de archivo y la función de entrada, no se admite «seguir mejorando» |
| block | Problemas sin resolver; si no hay, se deja vacío |

1. Al cerrar cada tarjeta debe añadirse una entrada, y su formato no puede modificarse.
2. En la ejecución local solo se inyecta la última entrada; las entradas históricas no se inyectan.
3. Reanudación desde un punto de interrupción: al recibir la orden «continuar», leer primero la última entrada para confirmar el punto de interrupción y continuar desde la entrada señalada por next; está prohibido rehacer pasos ya completados por memoria o por conjetura.

## 7. Presupuesto de inyección local

El harness ensambla el contexto de cada parte según la tabla siguiente; el presupuesto total no excede de 24K (el 75 % de la ventana de trabajo de 32K):

| Elemento inyectado | Presupuesto |
| --- | --- |
| Constitución del proyecto | 2-3K |
| Capítulo al que pertenece la tarjeta de tarea actual | 2-5K |
| Última entrada del registro de transferencia | unos 0,5K |
| Esqueleto del prompt de transferencia | unos 0,3K |
| Código y salidas de herramientas | el saldo restante |

No se inyectan: la tabla completa del registro de adopciones (solo las entradas que afectan a esta tarjeta), las notas de diseño y el capítulo de textos del sitio web.

## 8. Reglas de hierro del prompt de transferencia

Al empezar cada parte se inyecta una apertura fija, con seis reglas de hierro fijas:

1. Usar chino simplificado en toda la salida; el código, los comandos, las rutas y los nombres propios pueden conservarse en su forma original.
2. Hacer solo lo que está en la tarjeta de tarea, sin añadir funciones, configuraciones ni capacidades de extensión no solicitadas.
3. No inventar ni fabricar; ante una firma de API incierta, declarar directamente la incertidumbre; distinguir explícitamente los hechos de las conjeturas.
4. Si el comando de aceptación falla, aplicar el tratamiento de fallo de la tarjeta de tarea; no se permite alterar por cuenta propia los criterios de aceptación.
5. Las acciones que impliquen eliminar o sobrescribir archivos se detienen siempre, a la espera de la confirmación del usuario.
6. Al terminar, escribir el registro de transferencia conforme estrictamente a los requisitos de transferencia, y después finalizar.

## 9. Normativa de relleno en la nube

Antes de rellenar el manual, el modelo de la nube completa dos verificaciones previas y después rellena capítulo por capítulo:

1. Comprobación de premisas: revisar premisas erróneas, saltos lógicos y información faltante; si falta algo, preguntar primero al usuario.
2. Exploración de soluciones de código abierto: buscar soluciones ya hechas disponibles en el ecosistema de código abierto, explorar antes de rellenar, usar soluciones maduras antes que reinventar la rueda, y registrar los resultados en el registro de adopciones.

Al rellenar se observa:

1. Eliminar toda palabra vaga, dando en cada caso un valor preciso o una regla de decisión.
2. Las decisiones de diseño se escriben en las notas de diseño, con los motivos de la selección y las soluciones descartadas, para su revisión por el usuario, y no se inyectan al modelo local.
3. Las instrucciones para el modelo local se redactan según el principio «no conoce el contexto del proyecto», escribiendo explícitamente todas las premisas.
4. Línea base de conformidad: si la licencia es poco clara, marcar «pendiente de confirmar»; las soluciones con copyleft fuerte se anotan con un aviso de las obligaciones derivadas; el código abierto modificado conserva el aviso de copyright original y la explicación de las modificaciones; cada adopción debe sincronizarse con README, README_EN, NOTICE y LICENSE, y la sincronización figura como paso explícito y contenido de aceptación de la tarjeta de tarea correspondiente.
5. Las referencias a normativas de formato de documentos apuntan a las especificaciones correspondientes de este repositorio, sin copiar el texto normativo dentro del manual.

## 10. Marcas de fase y ventana de trabajo

Cada capítulo del índice legible por máquina lleva una marca de fase, según la cual se ajusta la ventana de trabajo local:

| Fase | Características | Ventana de trabajo |
| --- | --- | --- |
| Greenfield | Rellenar la implementación según el contrato congelado | 16-24K |
| Crecimiento | Funciones entre módulos, nivel por defecto | 32K |
| Mantenimiento | Refactorización y diagnóstico entre módulos | 48-64K, con paralelismo reducido en proporción |

Los capítulos en fase de mantenimiento deben añadir además una guía de diagnóstico con tres columnas: síntomas, ubicaciones posibles y comandos de verificación.

## 11. Registro de adopciones, distribución y textos del sitio web

1. Los campos de la tabla del registro de adopciones son fijos: nombre, categoría, versión, uso, licencia, titular de los derechos, dirección oficial, si se ha modificado, explicación de la modificación, forma de declaración y estado de adopción; el estado de adopción se divide en tres niveles: «aplicable de inmediato», «requiere evaluación» y «aún no disponible».
2. El capítulo de distribución cubre los scripts de compilación, la matriz de CI, el checksum y la plantilla de variables de entorno de firma; el comando de aceptación de la tarjeta de distribución es la comprobación del artefacto compilado; las acciones de publicación externa no pasan por el modelo local, sino que las ejecuta el usuario tras su confirmación.
3. El capítulo de textos del sitio web se orienta a usuarios corrientes: está prohibido aparecer código, línea de comandos, términos técnicos y palabras vacías; su estructura es posicionamiento en la primera pantalla, puntos de dolor, puntos fuertes, confianza, descarga, historias de escenario y preguntas frecuentes; el tono es sereno y contenido.

## 12. Referencia entre proyectos y comprobación

1. Cuando un proyecto de destino hace referencia a esta especificación, lee el texto completo mediante `gitrule spec` y copia el esqueleto del manual como esqueleto inicial del manual dentro del proyecto; esta especificación no se revisa con el proyecto, y la evolución del manual dentro del proyecto se cierra en el propio repositorio del proyecto.
2. Las tarjetas de tarea que producen documentos añaden `gitrule check` al comando de aceptación; los proyectos multilingües añaden además `gitrule xcheck`; tras cambiar el glosario se ejecuta `gitrule termcheck`.
3. Las infracciones documentales de `gitrule check` son de tipo autocorregible: puede ejecutarse primero `gitrule optimize` y volver a comprobar; si sigue sin pasar, se escribe en el campo block del registro de transferencia.
4. Las especificaciones de Gitrule solo gobiernan la documentación y las normas del repositorio; la calidad del código corresponde a las pruebas y scripts de verificación de cada proyecto, sin que uno sustituya al otro.

## Archivos relacionados

- [Índice general](./README.md): punto de registro de esta especificación
- [Reglas absolutas](./hard-rules.md): restricción de rango superior de las puertas de aceptación de esta especificación
- [Matriz de documentación](./document-matrix.md): definición de la responsabilidad exclusiva del documento entregable al que pertenece el manual
- [Especificación general de redacción](./general-writing-specification.md): estándar de redacción del cuerpo del manual
- [Especificación de multilingüismo](./multilingual-specification.md): reglas de sincronización multilingüe de esta especificación
- [Especificación de metadatos legibles por máquina](./machine-readable-metadata-specification.md): identificador estable y mapa de rutas de esta especificación
- [Recopilación de información y plantillas](./information-collection-and-templates.md): tabla de equivalencias de términos y convenciones de campos de las plantillas
