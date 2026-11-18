# Especificación de diseño de bases de datos

> Problema que resuelve este archivo: define las reglas de diseño de la estructura de tablas, los campos, los índices y las migraciones, garantizando datos coherentes, evolucionables y rastreables.

## 1. Convenciones de nomenclatura

1. Los nombres de tabla y de campo usan un estilo de nomenclatura uniforme y un significado inequívoco.
2. La nomenclatura de claves primarias, claves externas e índices sigue reglas de prefijo uniformes.
3. Las palabras reservadas y las abreviaturas deben tener una convención explícita que evite ambigüedades.

## 2. Diseño de campos

1. Cada campo debe precisar su tipo, si admite nulos, su valor predeterminado y su significado.
2. Los campos de tiempo usan una zona horaria y una precisión uniformes.
3. Los campos sensibles a la precisión, como los importes, usan tipos de coma fija y no coma flotante.
4. Los campos de estado usan enumeraciones explícitas con el significado de cada valor.

## 3. Índices y restricciones

1. Los índices se diseñan según los escenarios de consulta, evitando el exceso de índices.
2. La integridad se garantiza mediante restricciones y no depende de la validación en la capa de aplicación.
3. Las claves externas y las reglas de cascada deben declararse de forma explícita.

## 4. Gestión de migraciones

1. Los cambios de estructura se gestionan mediante scripts de migración, versionados y confirmados en el repositorio.
2. Las migraciones deben poder revertirse; los cambios que rompen la compatibilidad deben incluir un plan de migración de datos.
3. Los scripts de migración deben validarse en el entorno de pruebas antes de aplicarse en producción (véase [Especificación de despliegue y reversión](./deployment-and-rollback-specification.md)).

## 5. Seguridad

1. Los datos sensibles deben almacenarse cifrados o anonimizados (véase [Especificación de seguridad y privacidad](./security-and-privacy-specification.md)).
2. Las cadenas de conexión de la base de datos no deben confirmarse en el repositorio (corresponde a la regla absoluta H3).

## Archivos relacionados

- Líneas rojas sobre información sensible: [Especificación de seguridad y privacidad](./security-and-privacy-specification.md)
- Gestión de cambios: [Especificación de despliegue y reversión](./deployment-and-rollback-specification.md)
- Ubicación en la arquitectura: [Especificación del documento de diseño de arquitectura](./architecture-design-document-specification.md)
