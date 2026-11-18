# Plantilla de guía de contribución

> Problema que resuelve este archivo: ofrece una plantilla de guía de contribución lista para copiar, con la que el proyecto puede generar su `CONTRIBUTING.md` y cubrir las formas de participación, la preparación del entorno, el modelo de ramas, las convenciones de commit, los requisitos de PR, los requisitos de pruebas, el código de conducta y la declaración de licencia; las instrucciones de cumplimentación que la acompañan cubren el modo de recorte para cada tipo de proyecto.

## 1. Instrucciones de uso

1. Copiar todo el contenido de la sección 3 «Cuerpo de la plantilla» y crear con él un archivo `CONTRIBUTING.md` en la raíz del proyecto.
2. Sustituir los marcadores de posición conforme a la sección 4; todos los comandos deben ser comandos reales y directamente ejecutables.
3. Recortar según la variante de escenario de la sección 5: en los proyectos de tipo documentación se elimina el apartado de comandos de prueba y se conserva el flujo de Issue y PR.
4. Para la base normativa, véase la [especificación de la guía de contribución](./contribution-guide-specification.md); para los detalles de ramas y commits, véanse respectivamente la [especificación de flujo de trabajo de Git y ramas](./git-workflow-and-branching-specification.md) y la [especificación de mensajes de commit](./commit-message-specification.md).

## 2. Principios de personalización

- **Ejecutable**: los comandos deben indicar el directorio de trabajo y los requisitos previos de dependencias; se prohíbe escribir solo «instalar dependencias» sin el comando concreto.
- **Con condiciones de activación**: cada paso debe indicar cuándo se ejecuta y qué resultado se espera.
- **Sin generalidades**: se prohíbe escribir solo «se aceptan PR» sin un proceso sustantivo; ello se corresponde con la comprobación de gobernanza comunitaria de la [puerta de calidad](./quality-gate.md).
- **Citar en lugar de copiar**: las reglas de commit y de pruebas remiten a su especificación correspondiente y no se reproducen íntegramente en este archivo.

## 3. Cuerpo de la plantilla

````markdown
# Guía de contribución

> Este archivo explica cómo participar en las contribuciones a {{项目名称}} y está dirigido a contribuidores externos y a quienes participan por primera vez.

## Formas de participación

| Forma | Supuesto de aplicación | Punto de entrada |
| --- | --- | --- |
| Discusión de issues | Propuestas de funcionalidad, reporte de problemas | {{议题入口}} |
| Mejora de la documentación | Erratas, ampliación de ejemplos, optimización de la estructura | Enviar un PR directamente |
| Contribución de código | Corrección de defectos, implementación de funcionalidad | Véase el flujo más abajo |
| Reporte de problemas | Bloqueo en el uso, reproducción de anomalías | {{问题反馈入口}} |

## Preparación del entorno de desarrollo

Requisitos previos: {{环境前提}}

```bash
# Clonar el repositorio
git clone {{仓库地址}}
cd {{项目目录名}}

# Instalar dependencias
{{依赖安装命令}}

# Ejecutar en local
{{本地运行命令}}
```

Resultado esperado: {{验证本地环境可用的方式}}

## Modelo de ramas

- Crear una rama personal a partir de {{基准分支}} con el formato de nombre `{{分支命名格式}}` (por ejemplo, `feat/descripcion-breve`).
- Cada PR debe abordar un solo asunto; si el alcance del cambio es excesivo, debe dividirse.
- Se prohíbe hacer commit directamente en {{受保护分支}}; la integración debe realizarse mediante PR.

## Convenciones de commit

Los mensajes de commit siguen Conventional Commits con el formato `type(scope): subject`. Tipos habituales: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`. Ejemplo:

```text
feat(cli): add config file support
```

Para las reglas completas, véase la [especificación de mensajes de commit]({{提交规范链接}}).

## Requisitos de PR

Antes de enviar un PR deben completarse las siguientes comprobaciones:

- [ ] El alcance del cambio es único y cuenta con un issue o una explicación correspondiente.
- [ ] El mensaje de commit respeta el formato anterior.
- [ ] La ejecución local de `{{测试命令}}` se completa sin fallos.
- [ ] La documentación se actualiza junto con el código.
- [ ] No se introducen claves, claves privadas ni información sensible.
- [ ] La descripción indica el contenido del cambio, su motivo y el modo de verificación.

## Requisitos de pruebas

| Comprobación | Comando | Criterio de superación |
| --- | --- | --- |
| Pruebas unitarias | `{{单元测试命令}}` | Todas superadas |
| Análisis estático | `{{lint 命令}}` | Sin errores |
| Verificación de compilación | `{{构建命令}}` | Compilación correcta |

Umbral de cobertura: {{覆盖率要求}}.

## Código de conducta

Participar en este proyecto implica aceptar el [código de conducta](./CODE_OF_CONDUCT.md).

## Convenciones de Issue

- Antes de preguntar debe buscarse si el issue ya existe, para evitar duplicados.
- El informe de defectos debe incluir: información del entorno, pasos de reproducción, resultado esperado, resultado real y registro de errores.
- La propuesta de funcionalidad debe explicar el supuesto de uso y la alternativa en caso de no adoptarse.

## Declaración de licencia

El contenido aportado se rige por defecto por la licencia del proyecto {{许可证名称及 SPDX 标识符}}, cuyo texto completo figura en [LICENSE](./LICENSE). El envío implica que se tiene derecho a autorizar la contribución bajo dicha licencia.
````

## 4. Tabla de correspondencia de marcadores de posición y definición de campos

| Marcador de posición | Obligatorio | Definición del campo | Ejemplo de cumplimentación |
| --- | --- | --- | --- |
| `{{项目名称}}` | Sí | Nombre público del proyecto | `FooBar` |
| `{{议题入口}}` | Sí | Dirección real y accesible de los issues | `https://github.com/owner/repo/issues` |
| `{{问题反馈入口}}` | No | Canal específico cuando difiere del punto de entrada de issues | `https://github.com/owner/repo/issues/new` |
| `{{环境前提}}` | Sí | Versión del lenguaje, gestor de paquetes y dependencias del sistema | `Node.js 20+、pnpm 8+` |
| `{{仓库地址}}` | Sí | Dirección clonable del repositorio | `https://github.com/owner/repo.git` |
| `{{项目目录名}}` | Sí | Nombre del directorio tras la clonación | `repo` |
| `{{依赖安装命令}}` | Sí | Comando de instalación real | `pnpm install` |
| `{{本地运行命令}}` | Sí | Comando de arranque real | `pnpm dev` |
| `{{验证本地环境可用的方式}}` | Sí | Señal observable de éxito | `Al acceder a localhost:3000 aparece la página principal` |
| `{{基准分支}}` | Sí | Rama de origen de la que se crea la rama | `main` |
| `{{分支命名格式}}` | Sí | Regla de nomenclatura de ramas | `feat/descripcion-breve` |
| `{{受保护分支}}` | Sí | Rama en la que se prohíbe el commit directo | `main` |
| `{{提交规范链接}}` | No | Dirección interna o externa de la especificación de commit | `./docs/COMMIT_CONVENTION.md` |
| `{{测试命令}}` | Sí | Comando de pruebas real | `pnpm test` |
| `{{lint 命令}}` | Sí | Comando de análisis estático real | `pnpm lint` |
| `{{构建命令}}` | Sí | Comando de compilación real | `pnpm build` |
| `{{覆盖率要求}}` | No | Umbral de cobertura del código nuevo | `El código nuevo no debe bajar del 80 %` |
| `{{许可证名称及 SPDX 标识符}}` | Sí | Nombre completo y SPDX ID de la licencia del proyecto | `Licencia MIT (MIT)` |

## 5. Instrucciones de cumplimentación y variantes por escenario

| Escenario | Secciones que deben conservarse | Secciones que pueden recortarse | Puntos de ajuste |
| --- | --- | --- | --- |
| Proyecto de código | Todas | Ninguna | Los comandos deben ejecutarse realmente y superar la verificación |
| Proyecto de documentación | Formas de participación, requisitos de PR, código de conducta, licencia | Requisitos de pruebas, preparación del entorno de desarrollo | Eliminar la tabla de pruebas y conservar la autocomprobación del PR |
| Proyecto personal | Formas de participación, requisitos de PR, código de conducta, licencia | La preparación del entorno puede simplificarse | Precisar si se aceptan contribuciones externas |
| Proyecto empresarial | Todas | Ninguna | Añadir el enlace al acuerdo de licencia de contribuidor (CLA) y los requisitos jurídicos |

Correspondencia de errores frecuentes:

| Redacción incorrecta | Consecuencia | Redacción correcta |
| --- | --- | --- |
| «Se agradece cualquier forma de contribución» | No hay ruta concreta y el contribuidor no sabe por dónde empezar | Enumerar la tabla de formas de participación y los puntos de entrada |
| «Basta con ejecutar las pruebas» | No se conoce el comando ni el criterio de superación | Indicar el comando, el criterio de superación y el umbral de cobertura |
| Escribir `npm install` cuando el proyecto usa pnpm | El comando no se puede ejecutar | Ajustarlo al lockfile real |

## 6. Ejemplo completo

A continuación se muestra un ejemplo cumplimentado del apartado de comandos, solo como referencia de formato.

```bash
# Clonar el repositorio
git clone https://github.com/owner/repo.git
cd repo

# Instalar dependencias
pnpm install

# Ejecutar en local
pnpm dev
```

Resultado esperado: al acceder a localhost:3000 aparece la página principal.

## Archivos relacionados

- Especificación correspondiente: [especificación de la guía de contribución](./contribution-guide-specification.md)
- Plantillas complementarias: [plantilla de código de conducta](./code-of-conduct-template.md), [plantilla de SECURITY](./security-template.md)
- Detalles de pruebas: [especificación de pruebas](./testing-specification.md)
- Dimensión de gobernanza comunitaria: [matriz de dimensiones de revisión](./review-dimension-matrix.md)
- Volver al índice en chino simplificado: [README](./README.md)
