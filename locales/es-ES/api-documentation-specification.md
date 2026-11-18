# Especificación de documentación de API

> Problema que resuelve este archivo: define la estructura y los campos de una documentación de referencia de API completa, como base para redactar docs/api.md, y la mantiene estrictamente separada del contenido de tipo tutorial.

## 1. Estructura obligatoria

Cada entrada de API debe incluir:

| Campo | Requisito |
| --- | --- |
| Firma de la interfaz | Método, ruta o prototipo de función, completo y copiable |
| Parámetros | Nombre, tipo, obligatoriedad, valor predeterminado, rango de valores, descripción |
| Valor de retorno | Tipo y descripción de la estructura |
| Códigos de error | Código de error, condición que lo desencadena, forma de tratamiento |
| Ejemplo de llamada | Ejemplo mínimo ejecutable, con el lenguaje indicado |
| Limitación de frecuencia y cuota | Límite de frecuencia de llamada, cuota, tratamiento del exceso |

## 2. Reglas obligatorias

1. Los parámetros y los valores de retorno deben indicar tipo y restricciones; no debe omitirse el valor predeterminado.
2. Los códigos de error deben enumerarse por completo; no debe escribirse solo «puede producir error».
3. Los bloques de código deben indicar el identificador de lenguaje y los ejemplos deben poder ejecutarse de forma independiente.
4. Este archivo solo contiene información de referencia; no incluye tutoriales, antecedentes ni explicaciones de diseño (para tutoriales y antecedentes, véase la [especificación de secciones del README](./readme-sections-specification.md)).

## 3. Requisitos de coherencia

Las firmas de interfaz de la documentación de API deben coincidir con la implementación real del código; la denominación de parámetros debe cumplir los requisitos de precisión de la [especificación general de redacción](./general-writing-specification.md); para la terminología, véase el [glosario](./glossary.md).

## Archivos relacionados

- Para los límites de responsabilidad de la documentación, véase la [matriz de documentación](./document-matrix.md)
- Para la especificación de diseño de API (cómo diseñar interfaces), véase la [especificación de diseño de API](./api-design-specification.md)
- La calidad de la documentación pertenece a la dimensión D12; véase la [matriz de dimensiones de revisión](./review-dimension-matrix.md)
