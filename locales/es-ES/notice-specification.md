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

## Archivos relacionados

- Los campos del inventario de dependencias y el método de recopilación se describen en la [Especificación de cumplimiento de código abierto](./open-source-compliance-specification.md)
- Los requisitos sobre el texto completo de las licencias se describen en la [Especificación de LICENSE](./license-specification.md)
- Los capítulos correspondientes del README se describen en la [Especificación de secciones del README](./readme-sections-specification.md)
- La coherencia pertenece a las puertas G7–G9; véase [Puertas de calidad](./quality-gate.md)
