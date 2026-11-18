# Prácticas prohibidas

> Problema que resuelve este archivo: reúne todas las conductas prohibidas que no pueden infringirse y sirve como lista final de líneas rojas durante la revisión y la redacción.

## 1. Líneas rojas de control general y push

1. Se prohíbe emitir «se puede subir primero y completar después» mientras P0 no esté en cero.
2. Se prohíbe inventar resultados de verificación; los elementos que no puedan verificarse deben marcarse como `SKIP + motivo` y no debe escribirse PASS.
3. Se prohíbe fusionar varios documentos en un solo archivo para la entrega.
4. Se prohíbe incluir en el README la API completa, la guía de contribución y el registro de cambios.
5. Se prohíbe usar `--force` para hacer push a ramas públicas, bajo ninguna circunstancia.
6. Se prohíbe limitarse a un «commit de eliminación» para tratar una clave ya filtrada.
7. Se prohíbe inventar nombres de repositorio al margen de la [especificación de nombres de proyecto](./project-naming-specification.md).
8. Se prohíbe escribir el proceso de pensamiento interno en los documentos de entrega.

## 2. Líneas rojas de redacción de documentación

1. No debe inventarse el nombre del proyecto, las funcionalidades, los datos de rendimiento, las versiones de dependencias, la licencia, la información del autor ni los resultados de pruebas.
2. No debe copiarse el README, la documentación, el código, las imágenes ni los textos de terceros; cuando sea necesario citar, debe indicarse la fuente y la licencia.
3. No debe elegirse un tipo de licencia sin confirmación previa.
4. No deben aparecer cifras de rendimiento no verificadas, conclusiones comparativas sin fuente, afirmaciones promisorias (como «garantiza» o «gratis para siempre»), descripciones despectivas de proyectos de terceros ni contenido promocional ajeno al proyecto.
5. No deben usarse materiales de procedencia desconocida; cuando falten la fuente y la licencia de imágenes, iconos o tipografías, debe marcarse como pendiente de confirmación y no debe usarse el material directamente.

## Archivos relacionados

- Para las reglas absolutas cuya infracción bloquea el push, véase [reglas absolutas](./hard-rules.md)
- Para el tratamiento de incidentes (filtración de claves, etc.), véase la sección 5 de la [especificación de push y publicación](./push-and-release-specification.md)
- Para las restricciones obligatorias de los roles, véase [roles y responsabilidades](./roles-and-responsibilities.md)
