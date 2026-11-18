# Especificación de LICENSE

> Problema que resuelve este archivo: define el marcado SPDX de la licencia del proyecto, los requisitos del texto completo de LICENSE, la ubicación de la línea de copyright y la explicación de licencias múltiples, así como la regla de no escribir nada sin confirmación.

## Reglas de LICENSE

1. La licencia del proyecto debe indicarse expresamente en el README mediante el identificador SPDX y debe aportarse el archivo LICENSE correspondiente.
2. El archivo LICENSE debe contener el texto completo oficial en inglés de dicha licencia, sin suprimir ni modificar cláusulas.
3. La línea de copyright se coloca en el encabezado del archivo o en el capítulo 19 del README; el formato se indica en [Especificación de secciones del README](./readme-sections-specification.md).
4. Cuando se emplee licencia dual o múltiple, deben explicarse las condiciones de aplicación y la forma de elección.
5. Si el usuario no ha confirmado la elección de licencia, no debe escribirse directamente en la documentación; solo se ofrecen opciones candidatas y la explicación de sus diferencias.

## Archivos relacionados

- La ausencia de LICENSE bloquea el push; es la regla absoluta H2, véase [Reglas absolutas](./hard-rules.md)
- El juicio de compatibilidad de licencias de dependencias se indica en [Especificación de cumplimiento de código abierto](./open-source-compliance-specification.md)
- La declaración de terceros en archivo independiente se indica en [Especificación de NOTICE](./notice-specification.md)
- La exactitud de la licencia pertenece a las puertas G7/G8; véase [Puertas de calidad](./quality-gate.md)
