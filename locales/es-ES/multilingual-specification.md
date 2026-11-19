# Especificación de multilenguaje

> Problema que resuelve este archivo: define la disposición de archivos por directorio de código de idioma, el cambio de idioma, la consistencia de la traducción, la consistencia del código y las reglas de sincronización de modificaciones unilaterales.

## 1. Disposición de directorios

1. El `README.md` de la raíz del repositorio solo cumple la función de página de inicio del proyecto y de navegación de idiomas; no contiene el cuerpo de las especificaciones concretas.
2. Las especificaciones concretas se disponen de forma plana en el directorio `locales/<language-code>/`, por ejemplo `locales/zh-CN/角色与职责.md`.
3. El código de idioma sigue el estilo BCP 47, por ejemplo `zh-CN`, `en-US`, `ja-JP`, `ko-KR`; el código de idioma solo aparece en el nombre del directorio, no en el nombre del archivo.
4. **El nombre del archivo debe usar el propio idioma**: el directorio en chino usa nombres de archivo en chino (`角色与职责.md`), el directorio en inglés usa nombres de archivo en minúsculas con guiones (`roles-and-responsibilities.md`), y del mismo modo en los demás idiomas; se prohíbe mantener nombres de archivo en chino en directorios que no sean de chino.
5. No se exige que los nombres de archivo de los distintos directorios de idioma se correspondan literalmente, pero debe lograrse una correspondencia uno a uno: una misma especificación tiene la misma responsabilidad de contenido en cada directorio de idioma, y la relación de correspondencia se registra en el campo `paths` del archivo de inventario (véase la [especificación de metadatos legibles por máquina](./machine-readable-metadata-specification.md)).
6. El chino simplificado y el inglés son las versiones completadas en el primer lote; los demás idiomas se marcan en la tabla de idiomas del `README.md` raíz como «pendiente» o «completado», y los idiomas sin directorio creado no deben ofrecer enlaces vacíos.
7. Para añadir un idioma solo se crea el directorio de idioma correspondiente y se traduce documento por documento, sin modificar los archivos de idiomas existentes; solo se actualizan los demás idiomas completados cuando una revisión del idioma de origen requiera sincronización.

## 2. Cambio de idioma

1. El `README.md` de cada directorio de idioma debe ofrecer en la parte superior los enlaces de cambio de idioma.
2. Los enlaces usan rutas relativas al directorio de idioma actual, por ejemplo la forma de escritura en el directorio en español:
   `[English](../en-US/README.md) | [Español](./README.md)`.
3. El texto del enlace usa la autodenominación del idioma de destino, por ejemplo `English`, `Español`, `日本語`; no se escriben abreviaturas como `CN` o `EN`.
4. Los enlaces de cambio solo apuntan a directorios de idioma ya creados; los directorios de idioma no creados se marcan de forma unificada en la tabla de idiomas del `README.md` raíz, sin dejar enlaces rotos en el cuerpo del texto.

## 3. Consistencia de la traducción

1. La traducción debe ser completa; el número de secciones, el orden de las secciones, el número de columnas de las tablas y el número de bloques de código deben coincidir con el idioma de origen; no deben ofrecerse productos resumidos ni traducciones automáticas sin revisión.
2. Los comandos, rutas, nombres de claves de configuración, nombres de marcadores de posición y valores de parámetros dentro de los bloques de código se mantienen sin cambios; solo se traducen los comentarios y el texto explicativo. Por ejemplo, en un bloque de árbol de directorios como `├── SKILL.md   obligatorio: metadatos + flujo principal`, los símbolos de rama y las rutas se mantienen, mientras que la descripción posterior debe traducirse.
3. **Los campos de plantilla visibles para el usuario deben localizarse**: en la configuración `yaml` de un formulario de issue, `name`, `label`, `description`, `placeholder` y las opciones de lista desplegable se muestran directamente en la página de GitHub y deben traducirse al idioma de destino; los campos estructurados `type`, `id`, `labels`, `required` y `render` permanecen en inglés. El criterio es «si el elemento se muestra a una persona», no «si está dentro de un bloque de código». Por el mismo principio, el cuerpo de las plantillas copiables dentro de un bloque `markdown` siempre se traduce.
4. La terminología se unifica según la tabla de correspondencia de términos chino-inglés de [recopilación de información y plantillas](./information-collection-and-templates.md); un mismo concepto usa el mismo par de correspondencias en todos los idiomas.
5. Toda modificación unilateral debe sincronizarse con todos los idiomas completados y registrarse en el registro de actualizaciones el código de idioma y la versión sincronizados; mientras la sincronización no esté completada, la revisión no debe considerarse terminada.
6. La validación de consistencia pertenece a la puerta G10; véase la [puerta de calidad](./quality-gate.md).

## 4. Textos legales

1. El NOTICE se ofrece por defecto en versión china; los textos legales que impliquen el texto original de la licencia, la declaración de derechos de autor y la exención de responsabilidad conservan el texto original en inglés, sin traducirse ni reescribirse.
2. Los textos legales que requieran una versión bilingüe chino-inglés deben mostrar el texto original y la traducción en paralelo, indicando «la traducción es solo de referencia y prevalece el texto original».
3. Para el tratamiento del idioma de los textos legales, véanse la [especificación de NOTICE](./notice-specification.md) y la [exención de responsabilidad](./disclaimer.md).

## Archivos relacionados

- Navegación de idiomas raíz: [página de inicio del repositorio](../../README.md)
- Inventario de idiomas e identificadores estables: [especificación de metadatos legibles por máquina](./machine-readable-metadata-specification.md)
- El número y el orden de las secciones se basan en las 20 secciones de la [especificación de secciones del README](./readme-sections-specification.md)
- La plantilla de la tabla de correspondencia de términos se encuentra en [recopilación de información y plantillas](./information-collection-and-templates.md)
- Para los estándares de redacción, véase la [especificación general de redacción](./general-writing-specification.md)
- La sincronización bilingüe pertenece a la puerta G10; véase la [puerta de calidad](./quality-gate.md)
