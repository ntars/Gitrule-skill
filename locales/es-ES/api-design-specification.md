# Especificación de diseño de API

> Problema que resuelve este archivo: define los principios de coherencia y las convenciones del diseño de interfaces, garantizando que la API sea fácil de usar, predecible y evolutiva.

## 1. Principios de diseño

1. Denominación coherente: los recursos y las operaciones del mismo tipo usan reglas de denominación uniformes.
2. Previsibilidad: las operaciones con la misma semántica tienen la misma estructura.
3. Lo explícito por encima de lo implícito: los valores predeterminados, los campos obligatorios y el comportamiento ante errores deben ser inequívocos.
4. Compatibilidad hacia atrás: los cambios deben preservar la compatibilidad de forma prioritaria; los cambios disruptivos deben versionarse (véase la [especificación de gestión de versiones](./version-management-specification.md)).

## 2. Convenciones obligatorias

1. **Denominación**: reglas de denominación de recursos, métodos y campos.
2. **Parámetros**: tipo, obligatoriedad, valor predeterminado, rango de valores.
3. **Errores**: estructura de error unificada, códigos de error, estado HTTP o mecanismo equivalente.
4. **Paginación y filtrado**: convenciones de paginación, ordenación y filtrado en escenarios de gran volumen de datos.
5. **Idempotencia**: garantía de idempotencia de las operaciones de escritura.
6. **Limitación de frecuencia y cuota**: límites de frecuencia y respuesta ante el exceso.
7. **Versión**: estrategia de versiones de la API y forma de evolución.

## 3. Reglas obligatorias

1. Las respuestas de error deben incluir un código de error localizable y una descripción, sin exponer detalles de implementación interna.
2. Los cambios disruptivos deben incrementar la versión y ofrecer un periodo de migración (véase la [especificación de registro de cambios](./changelog-specification.md)).
3. Toda interfaz debe tener documentación correspondiente y campos completos (véase la [especificación de documentación de API](./api-documentation-specification.md)).

## Archivos relacionados

- Para la redacción de la documentación de referencia de API, véase la [especificación de documentación de API](./api-documentation-specification.md)
- Para los aspectos de seguridad, véase la [especificación de seguridad y privacidad](./security-and-privacy-specification.md)
- El tratamiento de errores es una decisión de ingeniería; véase [redacción de características y decisiones de ingeniería](./features-and-engineering-tradeoffs-guide.md)
