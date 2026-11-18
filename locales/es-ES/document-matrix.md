# Matriz de documentación

> Problema que resuelve este archivo: define la responsabilidad única de cada documento entregable, el contenido estrictamente prohibido y las restricciones de división, asegurando un archivo por responsabilidad y la prohibición de fusionarlos.

## 1. Archivos y responsabilidades

| Archivo | Responsabilidad única | Prohibido incluir |
|---|---|---|
| `README.md` | Portada: qué es, cómo se instala, cómo se ejecuta y dónde se consultan los detalles | La API completa, el flujo de contribución, el registro de cambios |
| `LICENSE` | Texto íntegro de la licencia | Cualquier texto explicativo |
| `CHANGELOG.md` | Cambios de versión orientados al usuario | Detalles internos de refactorización, planes de desarrollo |
| `CONTRIBUTING.md` | Flujo y especificaciones para colaboradores externos | Descripción de las funcionalidades del proyecto |
| `CODE_OF_CONDUCT.md` | Código de conducta | Contenido técnico |
| `SECURITY.md` | Canal de reporte de vulnerabilidades y política de respuesta | Lista de vulnerabilidades conocidas |
| `docs/api.md` | Referencia completa de la API | Tutoriales |
| `docs/architecture.md` | Arquitectura y límites entre módulos | Ejemplos de uso |
| `docs/naming.md` | Especificación de nomenclatura | Otras especificaciones |
| `docs/release.md` | Proceso de publicación y política de versiones | Registro de cambios |
| `.github/PULL_REQUEST_TEMPLATE.md` | Lista de autocomprobación del PR | Presentación del proyecto |
| `.github/ISSUE_TEMPLATE/*.yml` | Formularios estructurados de issue | Texto libre |
| `.github/workflows/*.yml` | CI/CD | Documentación explicativa |

> Nota: el texto normativo de `docs/naming.md` se encuentra en [Especificación de nomenclatura de proyectos](./project-naming-specification.md); el de `docs/release.md`, en [Especificación de push y publicación](./push-and-release-specification.md).

## 2. Restricciones

- Un archivo de más de 300 líneas debe dividirse en `docs/`, y el README conserva solo el resumen y el enlace.
- El nombre del archivo va en mayúsculas fijas, la ruta es fija y no deben inventarse niveles de directorio.
- Cada documento abre con una frase que explica «qué problema resuelve este archivo» y cierra con enlaces cruzados a los archivos relacionados.

## Archivos relacionados

- La estructura de 20 capítulos del README: [Especificación de secciones del README](./readme-sections-specification.md)
- Especificación independiente de NOTICE: [Especificación de NOTICE](./notice-specification.md)
- Especificación independiente de LICENSE: [Especificación de LICENSE](./license-specification.md)
- La integridad y la calidad de la documentación corresponden a las dimensiones D11/D12, véase [Matriz de dimensiones de revisión](./review-dimension-matrix.md)
