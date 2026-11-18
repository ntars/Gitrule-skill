# Matriz de dimensiones de revisión

> Problema que resuelve este archivo: define las 14 dimensiones de la revisión paralela de la fase 2, sus puntos de comprobación, el agente sugerido y el nivel de fallo, como base para la asignación y la determinación.

## Matriz de dimensiones de revisión

| # | Dimensión | Puntos de comprobación (palabras clave; el detalle lo despliega el subagente) | Agente sugerido | Nivel de fallo |
|---|---|---|---|---|
| D1 | Seguridad y privacidad | Escaneo de claves, `.env`, claves privadas, dominios/IP internos, datos personales, residuos en registros | security-auditor | P0 |
| D2 | Licencia y aspectos legales | Existencia y tipo de LICENSE, compatibilidad de licencias de dependencias, NOTICE, declaraciones de terceros | license-checker | P0 |
| D3 | Higiene del repositorio | Cobertura de .gitignore, artefactos y directorios de dependencias, .gitattributes, fin de línea LF, bits de ejecución, conflictos de mayúsculas y minúsculas en nombres de archivo | repo-hygienist | P0/P1 |
| D4 | Tamaño y binarios | Archivos >50MB, compresión de imágenes, configuración de LFS, crecimiento del historial | repo-hygienist | P1 |
| D5 | Compilación reproducible | Commit del lockfile, declaración de versión del motor, scripts de compilación, compilación correcta en entorno limpio | build-verifier | P0 |
| D6 | Pruebas y análisis estático | Pruebas unitarias correctas, cobertura, lint, format, comprobación de tipos | ci-runner | P0/P1 |
| D7 | Historial de commits | Conventional Commits, atomicidad, ausencia de WIP, información del autor, ausencia de mensajes de commit sensibles | commit-reviewer | P1 |
| D8 | Ramas y publicación | Protección de main, nomenclatura de ramas, etiquetas SemVer, etiquetas anotadas, Release Notes | release-manager | P1 |
| D9 | Automatización | Flujo de CI ejecutable, insignias de estado, dependabot, CODEOWNERS, plantillas de issue/PR | ci-runner | P1 |
| D10 | Metadatos del repositorio | description (formato combinado bilingüe `idioma nacional \| inglés`, ≤120 caracteres en cada idioma), topics (20 en total, solo en inglés y en minúsculas), rama por defecto, enlaces del área About, social preview | metadata-agent | P1 |
| D11 | Integridad de la documentación | Verificación de existencia de cada elemento de la matriz documental | docs-orchestrator | P0/P1 |
| D12 | Calidad de la documentación | Jerarquía de títulos, indicación del lenguaje en bloques de código, validez de enlaces, texto alt de las imágenes, espacios entre chino e inglés, ausencia de marcadores de posición | docs-orchestrator | P1/P2 |
| D13 | Página principal del README | Posicionamiento en una frase, instalación, inicio rápido, ≤4 insignias, capturas de pantalla, ausencia de rutas absolutas locales | readme-writer | P1 |
| D14 | Gobernanza comunitaria | CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, plantillas de issue, canales de soporte | docs-orchestrator | P2 |

## Significado de los niveles

- **P0**: bloquea el push.
- **P1**: debe corregirse antes del push o registrarse obligatoriamente como tarea pendiente.
- **P2**: mejora recomendada.

## Asignación y consolidación

- La forma de asignación de cada dimensión se detalla en el [contrato de asignación de subagentes](./sub-agent-dispatch-contract.md).
- Los resultados de la determinación se consolidan en la lista de problemas del [formato del informe de revisión](./audit-report-format.md); cada entrada debe incluir evidencia.
- La base de verificación de D11/D12 se detalla en la [matriz de documentación](./document-matrix.md) y en la [puerta de calidad](./quality-gate.md).

## Archivos relacionados

- El momento de ejecución se detalla en la fase 2 del [proceso de ejecución](./execution-process.md)
- Las condiciones de liberación de las puertas se detallan en la [puerta de calidad](./quality-gate.md)
