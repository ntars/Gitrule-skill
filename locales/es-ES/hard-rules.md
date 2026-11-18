# Reglas absolutas

> Problema que resuelve este archivo: enumera las reglas inviolables cuya infracción, por sí sola, bloquea el push y no admite el criterio de «primero se sube y luego se corrige».

## Tabla de reglas absolutas

| # | Regla |
|---|---|
| H1 | El nombre del repositorio debe cumplir la [especificación de nombres de proyecto](./project-naming-specification.md); mayúsculas y minúsculas, caracteres y longitud deben ser conformes en su totalidad |
| H2 | Debe existir un archivo `LICENSE`; la ausencia de licencia equivale a reserva de derechos por defecto y el proyecto no debe hacerse público |
| H3 | No debe hacerse commit de ninguna clave, token, clave privada, archivo `.env`, AK/SK de proveedor de nube ni cadena de conexión a base de datos |
| H4 | No debe hacerse commit de artefactos de compilación, directorios de dependencias, configuración del IDE ni archivos temporales del sistema |
| H5 | Un archivo individual no debe superar los 100 MB; por encima de 50 MB debe usarse LFS o excluirse |
| H6 | Debe existir `README.md` y debe contener: posicionamiento en una frase, instalación, ejemplo mínimo ejecutable y licencia |
| H7 | La rama por defecto debe estar protegida; se prohíbe el push directo a `main`/`master` |
| H8 | Se prohíbe `git push --force` sobre ramas públicas; en ramas personales solo se permite `--force-with-lease` |
| H9 | Antes del push, `build` y `test` deben pasar; si la CI está en rojo, no debe fusionarse en la rama principal |
| H10 | El mensaje de commit debe cumplir Conventional Commits; se prohíben commits sin información como `wip`/`update`/`fix bug` |
| H11 | Cada documento debe ser un archivo independiente con responsabilidad propia; se prohíbe acumular todo el contenido en el README (véase la [matriz de documentación](./document-matrix.md)) |
| H12 | Una vez que una clave ha sido enviada con push, debe rotarse la clave de inmediato y limpiarse el historial; no debe limitarse a un commit de eliminación |

## Restricciones de ejecución

- La infracción de cualquiera de las reglas **bloquea el push**; no se admite el criterio de «primero se sube y luego se corrige».
- El resultado de la evaluación de H1–H12 debe reflejarse en la lista de problemas del [formato del informe de auditoría](./audit-report-format.md), con evidencia en cada entrada (ruta:línea / salida de comando).
- Cuando se infringe H12, debe seguirse el procedimiento de gestión de incidentes de la [especificación de push y publicación](./push-and-release-specification.md).

## Archivos relacionados

- Para el detalle de nomenclatura, véase la [especificación de nombres de proyecto](./project-naming-specification.md)
- Para las condiciones de liberación de la puerta, véase la [puerta de calidad](./quality-gate.md)
- Para el compendio de prácticas prohibidas, véase [prácticas prohibidas](./prohibited-practices.md)
