# Especificación general de redacción

> Problema que resuelve este archivo: define el registro, la exactitud, la coherencia terminológica, las reglas de formato y el contenido prohibido de todos los documentos de entrega, garantizando una expresión precisa, sin ambigüedad y reproducible.

## 1. Registro

1. Usar lenguaje escrito, con oraciones enunciativas e imperativas.
2. No deben usarse expresiones coloquiales, por ejemplo «咱们», «超简单», «搞定», «贼快», «一键起飞».
3. No deben usarse signos de exclamación, puntos suspensivos, abreviaturas de red ni emoticonos.
4. No deben usarse oraciones interrogativas retóricas ni preguntas didácticas como inicio de sección.

## 2. Exactitud

1. Cada oración debe expresar una semántica completa; no debe depender de la deducción por contexto.
2. No deben usarse referencias vagas como «esto», «este», «relacionado», «algunos» o «varios»; cuando sea necesario referirse a algo, debe usarse el sustantivo completo.
3. Las fechas, los números de versión, las rutas, los comandos, los nombres de funciones y los nombres de claves de configuración deben ser precisos y coherentes con la situación real del proyecto.
4. Los comandos deben ser ejecutables directamente e incluir la indicación necesaria del directorio de trabajo actual.
5. Cuando se trate de números de versión, debe indicarse la semántica de la restricción de versión, por ejemplo `>=1.2.0 <2.0.0`.

## 3. Coherencia terminológica

1. La primera vez que aparece un término debe darse su definición, con el formato «término en chino (English Term, abreviatura)».
2. Un mismo concepto usa una sola expresión en todo el texto; los términos de las versiones china e inglesa se corresponden uno a uno.
3. Debe mantenerse una tabla de correspondencia de términos chino-inglés, ubicada en el apéndice del README o en un archivo independiente; las versiones bilingües comparten la misma tabla (la plantilla se encuentra en [recopilación de información y plantillas](./information-collection-and-templates.md)).

## 4. Reglas de formato

1. La jerarquía de títulos comienza en `##` (`#` se reserva para el nombre del proyecto); no deben saltarse niveles.
2. Cada título de segundo nivel corresponde a una sección establecida en la [especificación de secciones del README](./readme-sections-specification.md); el orden no debe alterarse.
3. Las tablas deben tener encabezado y un número de columnas coherente; los comandos, rutas, código y nombres de claves de configuración usan marcado de código en línea.
4. Los bloques de código deben indicar el identificador de lenguaje; los comandos de varias líneas deben poder copiarse y ejecutarse en su totalidad.
5. Los enlaces externos usan la URL completa, no enlaces cortos; los saltos internos usan anclas de ruta relativa.
6. Debe añadirse un espacio entre el chino y el inglés o los números; no deben mezclarse la puntuación china y la inglesa.

## 5. Convención de marcadores de posición

1. Los marcadores de posición formales de las plantillas copiables se escriben de forma unificada como `{{纯名}}`, por ejemplo `{{仓库地址}}`; el nombre no debe contener conjunciones que indiquen elección entre varias opciones, como «o» o «,», ni escribirse como una frase explicativa.
2. Los marcadores de posición formales deben registrarse en la tabla de correspondencia de marcadores de posición de la plantilla a la que pertenecen; la entrada de registro incluye el significado, un ejemplo y si es obligatorio.
3. El contenido entre llaves en lenguaje natural de los ejemplos de especificación o de las indicaciones de cumplimentación es solo un ejemplo y no constituye un marcador de posición formal, por lo que no se incluye en la tabla de correspondencia; al generar el documento final debe sustituirse en su totalidad por el contenido real.
4. No deben usarse llaves anidadas, comillas invertidas ni un segundo marcador de posición como nombre de un marcador de posición.

## 6. Lista de prohibiciones

No deben aparecer: cifras de rendimiento no verificadas, conclusiones comparativas sin fuente, afirmaciones promisorias (como «garantiza la compatibilidad con todos los entornos» o «gratis para siempre»), descripciones despectivas de proyectos de terceros ni contenido promocional ajeno al proyecto.

## Archivos relacionados

- Para la estructura de secciones, véase la [especificación de secciones del README](./readme-sections-specification.md)
- Para la correspondencia de términos bilingües, véase la [especificación de multilenguaje](./multilingual-specification.md)
- Para la evaluación de calidad G1 (coloquialismo y ambigüedad), véase la [puerta de calidad](./quality-gate.md)
