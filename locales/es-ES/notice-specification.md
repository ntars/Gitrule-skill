# Especificación de NOTICE

> Problema que resuelve este archivo: define las siete partes que el archivo NOTICE debe contener y los requisitos de coherencia con el README, con el fin de asegurar que las declaraciones de terceros constituyan un archivo independiente y que la información sea exacta.

## 1. Archivo independiente

NOTICE constituye un archivo independiente; no debe fusionarse con el README ni sustituirse por una lista del README. Debe contener las siguientes partes:

1. **Declaración del propio proyecto**: nombre del proyecto, titular de los derechos, año, licencia e identificador SPDX.
2. **Inventario de componentes de terceros**: enumeración elemento por elemento según los campos del inventario de dependencias de la [Especificación de cumplimiento de código abierto](./open-source-compliance-specification.md).
3. **Anexo del texto original de las licencias**: cuando la licencia exija adjuntar el texto completo, debe adjuntarse el texto original de cada una; el texto original se mantiene en inglés y no se traduce.
4. **Declaración de modificaciones**: ubicación y contenido de las modificaciones realizadas al código de terceros.
5. **Declaración de procedencia de materiales y datos**.
6. **Exención de responsabilidad**: se conserva el texto original en inglés y puede adjuntarse una versión en chino a modo de comparación.
7. **Puntos pendientes de confirmación**: los elementos cuya licencia o titularidad de derechos no pueda verificarse se marcan expresamente como «pendiente de confirmación».

## 2. Requisitos de coherencia

La información de componentes y licencias de NOTICE y la de los capítulos 6 (pila tecnológica e inventario de dependencias), 19 (copyright y licencia) y 20 (declaración de cumplimiento NOTICE) del README debe ser completamente idéntica; no deben aparecer divergencias en versiones, identificadores de licencia ni titulares de derechos.

## 3. Modo de declaración con licencias por capas

Cuando el proyecto adopte licencias por capas, la «declaración del propio proyecto» de la sección 1 debe desglosarse por capas y no limitarse a la licencia principal.

1. Cada capa ocupa una línea con: ámbito de aplicación (por ejemplo «el código fuente bajo `cli/` y `mcp/`»), nombre de la licencia, identificador SPDX y ubicación del texto completo.
2. La expresión SPDX resultante de reunir las capas debe coincidir literalmente con el capítulo 19 del README; no debe leerse `MIT AND CC-BY-4.0` en un lugar y solo `MIT` en el otro.
3. Indique en una frase el fundamento de la estratificación, por ejemplo «el código y la documentación tienen necesidades de reutilización distintas», para que los mantenedores posteriores puedan atribuir un archivo a su capa.
4. Si hay contenido que no puede atribuirse a ninguna capa, enumere su ruta en los «puntos pendientes de confirmación»; no lo impute por defecto a la licencia principal.
5. La exención de responsabilidad debe estar redactada de forma idéntica en el capítulo 19 del README y en `LICENSING.md` si existe, indicando que la elección de licencia y la división en capas las confirma el titular del proyecto y que las herramientas y plantillas no constituyen asesoramiento jurídico.

## Archivos relacionados

- Los campos del inventario de dependencias y el método de recopilación se describen en la [Especificación de cumplimiento de código abierto](./open-source-compliance-specification.md)
- Los requisitos sobre el texto completo de las licencias se describen en la [Especificación de LICENSE](./license-specification.md)
- Los capítulos correspondientes del README se describen en la [Especificación de secciones del README](./readme-sections-specification.md)
- La coherencia pertenece a las puertas G7–G9; véase [Puertas de calidad](./quality-gate.md)
