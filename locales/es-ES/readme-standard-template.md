# Plantilla estándar de README

> Problema que resuelve este archivo: ofrece una plantilla general de README lista para copiar y aplicar sustituyendo los marcadores de posición, que cubre la presentación de la portada a lo largo de todo el ciclo de vida del proyecto, e incluye la tabla de correspondencia de marcadores de posición, la explicación de las secciones opcionales y la lista de autocomprobación previa a la entrega, de modo que cualquier desarrollador pueda personalizarla rápidamente según su propio proyecto.

## 1. Instrucciones de uso

1. Copiar todo el contenido de la sección 3, «Cuerpo de la plantilla», y crear con él un `README.md` en la raíz del proyecto.
2. Sustituir uno a uno los `{{...}}` según la tabla de correspondencia de marcadores de posición de la sección 4; los elementos no utilizados se eliminan junto con la línea o la sección completa en que se encuentran.
3. Cada subsección de la sección 3 corresponde a una de las 20 secciones de la [especificación de secciones del README](./readme-sections-specification.md) y se ordena según el ciclo de vida, de dentro hacia fuera; al eliminar una sección debe eliminarse también el enlace correspondiente en la navegación de la portada.
4. Unificar el estilo, el color y el número de insignias según la [especificación de insignias](./badge-specification.md); revisar la disposición de capturas de pantalla, tablas y bloques de código según la [especificación de maquetación visual del README](./readme-visual-layout-specification.md).
5. Seleccionar las secciones según el tipo de proyecto siguiendo la [guía de adaptación del README por categoría](./readme-category-adaptation-guide.md).
6. Antes de enviar, ejecutar la lista de autocomprobación de la sección 6 y confirmar que no quedan marcadores de posición residuales.

## 2. Principios de personalización

- **Elementos obligatorios**: nombre del proyecto, descripción del repositorio, posicionamiento en una frase, instalación, inicio rápido, licencia.
- **Orden fijo**: el orden de las secciones coincide con la [especificación de secciones del README](./readme-sections-specification.md) y las versiones en chino e inglés se corresponden capítulo a capítulo.
- **Prioridad a la evidencia**: las características principales, el rendimiento y las decisiones de ingeniería deben aportar evidencia verificable; se prohíben los elogios cualitativos.
- **Divulgación transparente**: los escenarios no aplicables, las limitaciones, los problemas conocidos y las funcionalidades no implementadas deben enumerarse de forma explícita y no deben ocultarse.
- **No compromiso**: la hoja de ruta se marca como «no es un compromiso» y no incluye fechas de entrega concretas.
- **Veracidad**: todos los comandos, ejemplos, enlaces e insignias deben ser realmente utilizables; los datos de contacto y los canales de notificación deben ser reales y accesibles.

## 3. Cuerpo de la plantilla

Esta sección se organiza según el ciclo de vida del proyecto «de dentro hacia fuera», en 20 apartados que se corresponden uno a uno con las 20 secciones de la [especificación de secciones del README](./readme-sections-specification.md). El texto dentro del bloque de código de cada apartado es el cuerpo copiable.

La correspondencia entre secciones y fases del ciclo de vida es la siguiente, para facilitar su localización:

| Fase del ciclo de vida | Apartados correspondientes | Enfoque de la presentación |
| --- | --- | --- |
| Inicio del proyecto | 3.1–3.2 | Posicionamiento, antecedentes, escenarios de aplicación y limitaciones |
| Análisis de requisitos | 3.2–3.3 | Límites funcionales, escenarios de aplicación, escenarios no aplicables |
| Diseño de arquitectura | 3.5–3.6, 3.11 | Decisiones de ingeniería, pila tecnológica, estructura de directorios |
| Desarrollo e implementación | 3.3–3.4, 3.9–3.10 | Funcionalidades, características, configuración, API |
| Pruebas y validación | 3.8, 3.12 | Ejemplo de inicio rápido, evidencia de rendimiento |
| Despliegue y puesta en producción | 3.7, 3.14 | Instalación y despliegue, matriz de compatibilidad |
| Operación y monitorización | 3.13, 3.15 | Seguridad y privacidad, problemas conocidos y limitaciones |
| Mantenimiento iterativo | 3.15–3.17 | Funcionalidades no implementadas, registro de cambios, hoja de ruta posterior |

Nota: el README es la portada del proyecto; la documentación de proceso de cada fase (registros completos de requisitos, diseño, pruebas, despliegue y operación) es competencia de las especificaciones correspondientes, véase la [matriz de documentación](./document-matrix.md); esta sección solo presenta las conclusiones visibles para el usuario.

### 3.1 Nombre y posicionamiento del proyecto (corresponde al capítulo 1)

````markdown
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="{{LOGO_DARK_URL}}">
    <img alt="{{项目名称}} Logo" src="{{LOGO_LIGHT_URL}}" width="{{LOGO_WIDTH}}">
  </picture>

  <h1>{{项目名称}}</h1>

  [![build](https://img.shields.io/github/actions/workflow/status/{{OWNER}}/{{REPO}}/{{WORKFLOW}}?style=flat-square&logo=github)](https://github.com/{{OWNER}}/{{REPO}}/actions)
  [![version](https://img.shields.io/badge/version-{{VERSION}}-blue?style=flat-square)]({{RELEASE_URL}})
  [![license](https://img.shields.io/badge/license-{{LICENSE_SPDX}}-blue?style=flat-square)](./LICENSE)

  **Descripción del repositorio**: 【{{仓库描述中文}} | {{REPO_DESCRIPTION_EN}}】

  **Etiquetas de tema**: {{TOPICS}}

  {{一句话定位}}

  {{语言切换链接}}

  [Instalación](#instalación) · [Inicio rápido](#inicio-rápido) · [Características principales](#características-principales) · [Problemas conocidos y limitaciones](#problemas-conocidos-y-limitaciones) · [Hoja de ruta posterior](#hoja-de-ruta-posterior) · [Documentación](#documentación) · [Participación y contribución](#participación-y-contribución)
</div>
````

### 3.2 Introducción al proyecto (corresponde al capítulo 2)

````markdown
## Introducción al proyecto

{{背景}}

{{核心思路}}

**Escenarios de aplicación**

- {{适用场景一}}
- {{适用场景二}}

**Escenarios no aplicables**

- {{不适用场景一}}
- {{不适用场景二}}

### Ventajas y limitaciones

**Ventajas**

| Ventaja | Descripción | Forma de verificación |
| --- | --- | --- |
| {{优势名称}} | {{优势说明}} | {{证据}} |
| {{优势名称}} | {{优势说明}} | {{证据}} |

**Limitaciones**

| Limitación | Alcance de impacto | Forma de elusión temporal |
| --- | --- | --- |
| {{局限描述}} | {{影响范围}} | {{规避方式}} |
| {{局限描述}} | {{影响范围}} | {{规避方式}} |
````

### 3.3 Funcionalidades principales (corresponde al capítulo 3)

````markdown
## Funcionalidades principales

- {{功能一}}：{{触发条件与结果}}
- {{功能二}}：{{触发条件与结果}}
- {{功能三}}：{{触发条件与结果}}
````

### 3.4 Características principales (corresponde al capítulo 4)

Cada característica debe incluir la estructura completa de cinco partes; si falta alguna de ellas, no debe enumerarse. Para la base de redacción, véase [redacción de características y decisiones de ingeniería](./features-and-engineering-tradeoffs-guide.md).

````markdown
## Características principales

### {{特性名称}}

- **Valor**: {{价值}}
- **Forma de implementación**: {{实现方式}}
- **Diferenciación**: {{差异化}}
- **Evidencia**: {{证据}}
````

### 3.5 Detalles de diseño y decisiones de ingeniería (corresponde al capítulo 5)

Redactar según las tres partes «escenario → forma de tratamiento → motivo»; para las categorías cubiertas, véase la sección 2 de [redacción de características y decisiones de ingeniería](./features-and-engineering-tradeoffs-guide.md).

````markdown
## Detalles de diseño y decisiones de ingeniería

### {{取舍主题}}

- **Escenario**: {{场景}}
- **Forma de tratamiento**: {{处理方式}}
- **Motivo**: {{原因}}
````

### 3.6 Pila tecnológica y lista de dependencias (corresponde al capítulo 6)

````markdown
## Pila tecnológica y lista de dependencias

| Categoría | Tecnología o componente | Restricción de versión | Uso |
| --- | --- | --- | --- |
| Entorno de ejecución | {{运行时与版本}} | {{运行时版本约束}} | {{运行时用途}} |
| Compilación | {{构建工具与版本}} | {{构建版本约束}} | {{构建用途}} |
| Pruebas | {{测试工具与版本}} | {{测试版本约束}} | {{测试用途}} |

El detalle de las dependencias de terceros y sus licencias se encuentra en [NOTICE](./NOTICE).
````

### 3.7 Instalación y despliegue (corresponde al capítulo 7)

````markdown
## Instalación

Requisitos de entorno: {{运行时 / 操作系统 / 版本}}

```bash
{{包管理器安装命令}}
```

Verificar la instalación:

```bash
{{验证命令}}
```

Salida:

```text
{{预期输出}}
```

Actualización: `{{升级命令}}`. Desinstalación: `{{卸载命令}}`.

Despliegue en contenedor: {{容器化说明}}
````

### 3.8 Inicio rápido (corresponde al capítulo 8)

````markdown
## Inicio rápido

{{一句话说明本示例完成什么}}

```{{语言标识}}
{{最小可运行示例}}
```

Salida esperada:

```text
{{输出}}
```
````

### 3.9 Explicación de la configuración (corresponde al capítulo 9)

````markdown
## Explicación de la configuración

| Nombre de clave | Tipo | Valor predeterminado | Obligatorio | Rango de valores | Función | Ejemplo |
| --- | --- | --- | --- | --- | --- | --- |
| {{键名}} | {{类型}} | {{默认值}} | {{是否必填}} | {{取值范围}} | {{作用}} | {{示例值}} |

Prioridad de configuración: {{配置优先级}}.

Actualización en caliente: {{热更新支持说明}}
````

### 3.10 API o explicación de módulos (corresponde al capítulo 10)

````markdown
## API

{{模块概述}}

```{{语言标识}}
{{接口签名}}
```

Parámetros:

| Parámetro | Tipo | Obligatorio | Descripción |
| --- | --- | --- | --- |
| {{参数名}} | {{参数类型}} | {{参数是否必填}} | {{参数说明}} |

Valor de retorno: {{返回值说明}}

Códigos de error:

| Código de error | Significado | Forma de tratamiento |
| --- | --- | --- |
| {{错误码}} | {{错误含义}} | {{错误处理方式}} |

Ejemplo de llamada:

```{{语言标识}}
{{调用示例}}
```

Limitación de frecuencia y cuota: {{限流与配额说明}}

Para más detalles, véase la [documentación de API]({{API_DOC_PATH}}).
````

### 3.11 Estructura de directorios (corresponde al capítulo 11)

````markdown
## Estructura de directorios

```text
{{项目名}}/
├── {{目录条目}}   # {{职责}}
├── {{目录条目}}   # {{职责}}
└── {{目录条目}}   # {{职责}}
```
````

### 3.12 Rendimiento (corresponde al capítulo 12)

````markdown
## Rendimiento

Entorno de prueba: {{测试环境}}

Método de prueba: {{测试方法}}

| Métrica | Valor | Línea base de comparación |
| --- | --- | --- |
| {{性能指标}} | {{指标数值}} | {{对比基线}} |

Análisis de cuellos de botella: {{瓶颈分析}}

Recomendaciones de ajuste: {{调优建议}}
````

### 3.13 Seguridad y privacidad (corresponde al capítulo 13)

````markdown
## Seguridad y privacidad

Recogida y almacenamiento de datos: {{数据收集与存储说明}}

Cifrado en tránsito: {{传输加密说明}}

Modelo de permisos: {{权限模型说明}}

Riesgos conocidos: {{已知风险}}

Canal de notificación de vulnerabilidades: {{漏洞上报渠道}}

La política de seguridad se encuentra en [SECURITY.md](./SECURITY.md).
````

### 3.14 Explicación de compatibilidad (corresponde al capítulo 14)

````markdown
## Explicación de compatibilidad

| Dimensión | Alcance soportado | Estado de verificación |
| --- | --- | --- |
| Sistema operativo | {{操作系统}} | {{操作系统验证状态}} |
| Entorno de ejecución | {{运行时兼容版本}} | {{运行时验证状态}} |
| Navegador | {{浏览器}} | {{浏览器验证状态}} |
| Base de datos | {{数据库版本}} | {{数据库验证状态}} |

No soportado de forma explícita: {{明确不支持项}}
````

### 3.15 Problemas conocidos, limitaciones y funcionalidades no implementadas (corresponde al capítulo 15)

````markdown
## Problemas conocidos y limitaciones

**Problemas conocidos**

| Descripción del problema | Alcance de impacto | Solución temporal | Enlace de seguimiento |
| --- | --- | --- | --- |
| {{问题描述}} | {{影响范围}} | {{临时规避方案}} | {{跟踪链接}} |

**Limitaciones actuales**

{{当前限制说明}}

**Funcionalidades no implementadas**

| Funcionalidad | Motivo de no implementación | Estado de la planificación |
| --- | --- | --- |
| {{未实现功能}} | {{未实现原因}} | {{计划状态}} |
````

### 3.16 Registro de cambios (corresponde al capítulo 16)

````markdown
## Registro de cambios

Los cambios de versión siguen el versionado semántico y la estructura de Keep a Changelog; el registro completo se encuentra en [CHANGELOG.md](./CHANGELOG.md).
````

### 3.17 Hoja de ruta posterior (corresponde al capítulo 17)

Para la redacción del estado de los elementos planificados y de la versión objetivo, véase la [especificación de hoja de ruta](./roadmap-specification.md); debe marcarse «no es un compromiso».

````markdown
## Hoja de ruta posterior

> Los siguientes contenidos son elementos planificados y no constituyen un compromiso de entrega; el alcance y los plazos reales se rigen por el registro de publicaciones.

| Elemento planificado | Estado | Versión objetivo |
| --- | --- | --- |
| {{计划项}} | {{计划状态}} | {{目标版本}} |
| {{计划项}} | {{计划状态}} | {{目标版本}} |
````

### 3.18 Participación y contribución (corresponde al capítulo 18)

````markdown
## Participación y contribución

- Preparación del entorno de desarrollo: {{搭建步骤}}
- Modelo de ramas: {{说明}}
- Especificación de commits: {{Conventional Commits 等}}
- Requisitos de PR: {{要求}}
- Código de conducta: véase [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
- Plantillas de Issue: véase [.github/ISSUE_TEMPLATE/](./.github/ISSUE_TEMPLATE/)
````

### 3.19 Copyright y licencia (corresponde al capítulo 19)

````markdown
## Licencia

Copyright © {{年份}} {{著作权人}}. Licensed under {{SPDX 标识符}}.

Este proyecto se distribuye bajo la licencia {{许可证名称}}; el texto completo se encuentra en [LICENSE](./LICENSE).
````

### 3.20 Declaración de cumplimiento NOTICE (corresponde al capítulo 20)

````markdown
## Declaración de cumplimiento NOTICE

Este proyecto utiliza componentes y materiales de terceros; el resumen de sus licencias e información de copyright se encuentra en [NOTICE](./NOTICE). Esta sección no sustituye al archivo NOTICE.
````

## 4. Tabla de correspondencia de marcadores de posición

La tabla enumera todos los marcadores de posición que aparecen en el cuerpo de la plantilla. Están ordenados por sección; los elementos no utilizados se eliminan junto con la línea en que se encuentran.

| Marcador de posición | Significado | Ejemplo | Obligatorio |
| --- | --- | --- | --- |
| `{{项目名称}}` | Nombre visible del proyecto | `Awesome Tool` | Sí |
| `{{LOGO_DARK_URL}}` | Dirección del logo para tema oscuro | `media/logo-dark.svg` | No |
| `{{LOGO_LIGHT_URL}}` | Dirección del logo para tema claro | `media/logo-light.svg` | No |
| `{{LOGO_WIDTH}}` | Ancho de visualización del logo (px) | `200` | No |
| `{{OWNER}}` | Propietario del repositorio | `octocat` | No |
| `{{REPO}}` | Nombre del repositorio | `awesome-tool` | No |
| `{{WORKFLOW}}` | Nombre del archivo del flujo de trabajo de CI | `ci.yml` | No |
| `{{VERSION}}` | Número de versión actual | `1.2.0` | No |
| `{{LICENSE_SPDX}}` | Identificador SPDX de la licencia | `MIT` | Sí |
| `{{RELEASE_URL}}` | URL de la página de publicaciones | Enlace a GitHub Releases | No |
| `{{仓库描述中文}}` | Parte en chino de la descripción del repositorio, ≤120 caracteres | `herramienta ligera de CLI en Go para procesar JSON` | Sí |
| `{{REPO_DESCRIPTION_EN}}` | Parte en inglés de la descripción del repositorio, ≤120 caracteres | `A lightweight Go CLI for JSON processing` | Sí |
| `{{TOPICS}}` | Etiquetas de tema, completar 20 palabras en inglés minúsculas unidas por `-` | `go cli json command-line developer-tools` | No |
| `{{一句话定位}}` | Una frase que explica qué es el proyecto, para quién es y qué problema resuelve | `herramienta ligera de CLI en Go para procesar JSON` | Sí |
| `{{语言切换链接}}` | Enlace de cambio entre versiones de idioma | Texto del enlace `English`; la ruta de destino se completa según el directorio de idioma real, por ejemplo `../en-US/README.md` | No |
| `{{背景}}` | Motivo por el que surge el proyecto y problema que debe resolver | Según el proyecto | Sí |
| `{{核心思路}}` | Método clave o decisión de diseño adoptados | Según el proyecto | Sí |
| `{{适用场景一}}` / `{{适用场景二}}` | Situaciones en las que es adecuado usarlo | `necesidad de procesar rápidamente archivos JSON pequeños` | Sí |
| `{{不适用场景一}}` / `{{不适用场景二}}` | Situaciones claramente no recomendadas y su motivo | `necesidad de procesar en flujo archivos de nivel GB` | Sí |
| `{{优势名称}}` | Nombre sustantivo de la ventaja | `cero dependencias` | No |
| `{{优势说明}}` | Explicación concreta de la ventaja | `no introduce dependencias de terceros en tiempo de ejecución` | No |
| `{{证据}}` | Evidencia verificable o pasos reproducibles de la ventaja | `la salida de ldd está vacía` | No |
| `{{局限描述}}` | Descripción concreta de la limitación | `no admite escritura concurrente` | No |
| `{{影响范围}}` | Funcionalidad o escenario afectado por la limitación | `cuando varios procesos escriben a la vez` | No |
| `{{规避方式}}` | Solución de elusión temporal de la limitación | `bloqueo externo` | No |
| `{{功能一}}` / `{{功能二}}` / `{{功能三}}` | Nombre de la funcionalidad | `filtrado` | Sí |
| `{{触发条件与结果}}` | Condición de activación y resultado de la funcionalidad | `tras pasar --filter, genera la salida según la condición` | Sí |
| `{{特性名称}}` | Nombre de la característica, no más de 15 caracteres | `distribución en un solo archivo` | No |
| `{{价值}}` | Problema concreto que resuelve la característica y consecuencia de no resolverlo | Según el proyecto | No |
| `{{实现方式}}` | Tecnología, mecanismo o algoritmo adoptados, con los archivos o funciones clave | Según el proyecto | No |
| `{{差异化}}` | Dimensión de comparación objetivamente evaluable frente a soluciones nombradas | Según el proyecto | No |
| `{{证据}}` | Pruebas reproducibles, benchmarks, ubicación en el código o pasos | Según el proyecto | No |
| `{{取舍主题}}` | Tema de la decisión de ingeniería | `escritura concurrente` | No |
| `{{场景}}` | Situación concreta que activa ese diseño | Según el proyecto | No |
| `{{处理方式}}` | Solución adoptada | Según el proyecto | No |
| `{{原因}}` | Motivo para no adoptar otras soluciones | Según el proyecto | No |
| `{{运行时与版本}}` / `{{构建工具与版本}}` / `{{测试工具与版本}}` | Nombre y versión del componente de la pila tecnológica | `Go 1.22` | No |
| `{{运行时版本约束}}` / `{{构建版本约束}}` / `{{测试版本约束}}` | Rango de restricción de versión | `>=1.22` | No |
| `{{运行时用途}}` / `{{构建用途}}` / `{{测试用途}}` | Uso del componente | `compilación y ejecución` | No |
| `{{运行时 / 操作系统 / 版本}}` | Requisitos del entorno de instalación | `Go 1.22+、Linux/macOS` | Sí |
| `{{包管理器安装命令}}` | Comando de instalación real | `go install example.com/tool@latest` | Sí |
| `{{验证命令}}` | Comando para verificar la instalación | `tool --version` | No |
| `{{预期输出}}` | Resultado esperado del comando de verificación | `tool 1.2.0` | No |
| `{{升级命令}}` / `{{卸载命令}}` | Comandos de actualización y desinstalación | `go install example.com/tool@latest` | No |
| `{{容器化说明}}` | Explicación de contenedorización o dirección de la imagen | `docker run ...` | No |
| `{{一句话说明本示例完成什么}}` | Objetivo del ejemplo de inicio rápido | `generar la salida del JSON filtrado por campo` | Sí |
| `{{语言标识}}` | Identificador de lenguaje del bloque de código | `bash` | Sí |
| `{{最小可运行示例}}` | Ejemplo mínimo ejecutable | Según el proyecto | Sí |
| `{{输出}}` | Salida esperada del ejemplo | Según el proyecto | Sí |
| `{{键名}}` | Nombre de la clave de configuración | `output.format` | No |
| `{{类型}}` | Tipo del valor de configuración | `string` | No |
| `{{默认值}}` | Valor predeterminado de la configuración | `json` | No |
| `{{是否必填}}` | Si es obligatorio | `No` | No |
| `{{取值范围}}` | Rango de valores permitido | `json / yaml` | No |
| `{{作用}}` | Función de la configuración | `especificar el formato de salida` | No |
| `{{示例值}}` | Ejemplo de configuración | `yaml` | No |
| `{{配置优先级}}` | Orden de prioridad de configuraciones de varias fuentes | `argumentos de línea de comandos > variables de entorno > archivo de configuración` | No |
| `{{热更新支持说明}}` | Si se admite la actualización en caliente y de qué forma | `no se admite; requiere reinicio` | No |
| `{{模块概述}}` | Resumen del uso del módulo | Según el proyecto | No |
| `{{接口签名}}` | Firma de la función o interfaz | `func Filter(in io.Reader, key string) error` | No |
| `{{参数名}}` / `{{参数类型}}` / `{{参数是否必填}}` / `{{参数说明}}` | Campos de los parámetros de la interfaz | `in / io.Reader / Sí / flujo de entrada` | No |
| `{{返回值说明}}` | Significado del valor de retorno | `devuelve nil si tiene éxito` | No |
| `{{错误码}}` / `{{错误含义}}` / `{{错误处理方式}}` | Campos del código de error | `E001 / entrada vacía / comprobar la entrada` | No |
| `{{调用示例}}` | Código de llamada a la interfaz | Según el proyecto | No |
| `{{限流与配额说明}}` | Reglas de limitación de frecuencia y cuota | `sin limitación de frecuencia` | No |
| `{{API_DOC_PATH}}` | Ruta relativa de la documentación de API | `./docs/api.md` | No |
| `{{项目名}}` | Nombre del nodo raíz del árbol de directorios | `awesome-tool` | Sí |
| `{{目录条目}}` / `{{职责}}` | Entrada del árbol de directorios y su responsabilidad | `cmd/ / punto de entrada de comandos` | Sí |
| `{{测试环境}}` | Hardware, sistema y versión del entorno de ejecución | `Intel i7 / Ubuntu 22.04 / Go 1.22` | No |
| `{{测试方法}}` | Método de prueba de rendimiento | `go test -bench` | No |
| `{{性能指标}}` / `{{指标数值}}` / `{{对比基线}}` | Campos de la métrica de rendimiento | `rendimiento / 120 MB/s / 80 MB/s` | No |
| `{{瓶颈分析}}` | Explicación del cuello de botella de rendimiento | Según el proyecto | No |
| `{{调优建议}}` | Recomendaciones de ajuste de rendimiento | Según el proyecto | No |
| `{{数据收集与存储说明}}` | Alcance de recogida de datos y forma de almacenamiento | `no se recogen datos de usuario` | No |
| `{{传输加密说明}}` | Forma de cifrado en tránsito | `HTTPS` | No |
| `{{权限模型说明}}` | Explicación del modelo de permisos | `basado en Token` | No |
| `{{已知风险}}` | Riesgo de seguridad conocido | Según el proyecto | No |
| `{{漏洞上报渠道}}` | Canal de notificación de vulnerabilidades real y accesible | `security@example.com` | No |
| `{{操作系统}}` / `{{操作系统验证状态}}` | Alcance de soporte de sistemas operativos y estado de verificación | `Linux, macOS / verificado` | No |
| `{{运行时兼容版本}}` / `{{运行时验证状态}}` | Alcance de compatibilidad del entorno de ejecución y estado de verificación | `Go 1.20+ / verificado` | No |
| `{{浏览器}}` / `{{浏览器验证状态}}` | Alcance de soporte de navegadores y estado de verificación | `Chrome 100+ / verificado` | No |
| `{{数据库版本}}` / `{{数据库验证状态}}` | Versión de base de datos y estado de verificación | `PostgreSQL 14+ / verificado` | No |
| `{{明确不支持项}}` | Entorno explícitamente no soportado | `Windows de 32 bits` | No |
| `{{问题描述}}` | Descripción del problema conocido | `alto consumo de memoria con entradas muy largas` | No |
| `{{影响范围}}` | Funcionalidad o escenario afectado por el problema | `cuando la entrada supera los 100 MB` | No |
| `{{临时规避方案}}` | Forma de elusión temporal | `procesamiento por lotes` | No |
| `{{跟踪链接}}` | Dirección de seguimiento del problema | Enlace a un Issue de GitHub | No |
| `{{当前限制说明}}` | Limitación funcional actual | `actualmente no se admite la escritura concurrente` | No |
| `{{未实现功能}}` | Funcionalidad aún no implementada | `actualización en caliente de la configuración` | No |
| `{{未实现原因}}` | Motivo de la no implementación | `baja prioridad` | No |
| `{{计划状态}}` | Estado de la planificación (para funcionalidades no implementadas y hoja de ruta) | `planificado` | No |
| `{{计划项}}` | Elemento planificado de la hoja de ruta | `admitir actualización en caliente del archivo de configuración` | No |
| `{{目标版本}}` | Versión objetivo del elemento planificado | `v1.3.0` | No |
| `{{搭建步骤}}` | Pasos o enlace para preparar el entorno de desarrollo | `véase CONTRIBUTING.md` | No |
| `{{说明}}` | Explicación del modelo de ramas | `crear una rama feat a partir de main` | No |
| `{{Conventional Commits 等}}` | Explicación de la especificación de commits | `Conventional Commits` | No |
| `{{要求}}` | Requisitos de PR | `cambio único, pruebas superadas` | No |
| `{{年份}}` | Año del copyright | `2026` | Sí |
| `{{著作权人}}` | Titular de los derechos de autor | `Ntarstudio` | Sí |
| `{{SPDX 标识符}}` | Identificador SPDX en la línea de copyright | `MIT` | Sí |
| `{{许可证名称}}` | Nombre completo de la licencia | `MIT` | Sí |

## 5. Explicación de las secciones opcionales

La sección 3 ya ofrece el cuerpo copiable de las 20 secciones. A continuación se recogen las indicaciones complementarias para añadir o eliminar secciones según el tipo de proyecto; al eliminar una sección debe eliminarse también el enlace correspondiente en la navegación de la portada.

| Sección | Tipo en que se recomienda conservarla | Condición para poder eliminarla |
| --- | --- | --- |
| Características principales | Todos | Puede eliminarse si no hay evidencia verificable, sin sustituirla por descripciones cualitativas |
| Detalles de diseño y decisiones de ingeniería | Marcos de trabajo, aplicaciones, servicios | Puede eliminarse si no hay decisiones clave |
| Pila tecnológica y lista de dependencias | Bibliotecas, marcos de trabajo | Puede eliminarse si no hay dependencias externas |
| Rendimiento | CLI, bibliotecas, servicios | Puede eliminarse si no hay datos de prueba; se prohíben las cifras estimadas |
| Seguridad y privacidad | Servicios, aplicaciones, proyectos que tratan datos personales | Puede simplificarse en herramientas puramente locales |
| Explicación de compatibilidad | Bibliotecas, SDK, aplicaciones multiplataforma | Puede simplificarse si hay un único entorno de ejecución |
| Registro de cambios | Todos | Solo si no existe CHANGELOG se sustituye por un resumen integrado de cambios |
| Hoja de ruta posterior | Todos | Puede eliminarse si no hay planes públicos |
| Declaración de cumplimiento NOTICE | Proyectos con dependencias de terceros | Puede eliminarse si no hay dependencias de terceros |

## 6. Lista de autocomprobación previa a la entrega

- [ ] No quedan marcadores de posición `{{...}}` residuales.
- [ ] La portada incluye la descripción del repositorio 【chino | inglés】 y las etiquetas de tema, coherentes ambas con los metadatos del repositorio.
- [ ] La descripción del repositorio, en chino y en inglés, no supera los 120 caracteres en cada caso.
- [ ] Las etiquetas de tema están completas (20), todas en inglés minúsculas y unidas por `-`.
- [ ] El posicionamiento en una frase incluye la palabra de categoría; en chino no supera los 60 caracteres y en inglés no supera las 25 palabras.
- [ ] Cada característica principal incluye la estructura de cinco partes y evidencia verificable.
- [ ] Ventajas y limitaciones están separadas; las limitaciones incluyen alcance de impacto y forma de elusión.
- [ ] Los problemas conocidos incluyen enlace de seguimiento; las funcionalidades no implementadas incluyen motivo y estado de la planificación.
- [ ] La hoja de ruta está marcada como «no es un compromiso» y no contiene fechas de entrega concretas.
- [ ] Se han enumerado los escenarios no aplicables y los elementos explícitamente no soportados.
- [ ] El título de primer nivel es único, los títulos de segundo nivel mantienen una jerarquía continua y el orden de las secciones coincide con las 20 secciones de la especificación.
- [ ] El estilo de las insignias es uniforme, los enlaces son válidos y el texto `alt` es inequívoco.
- [ ] El comando de instalación y el ejemplo de inicio rápido se han probado y son ejecutables.
- [ ] Todos los bloques de código indican el lenguaje y todas las imágenes tienen texto `alt`.
- [ ] Las rutas relativas funcionan tanto en un Fork como sin conexión.
- [ ] Existe LICENSE y el identificador SPDX coincide con el del README.
- [ ] El orden de las secciones de las versiones en chino e inglés se corresponde uno a uno.

## Archivos relacionados

- Para la definición completa de las secciones, véase la [especificación de secciones del README](./readme-sections-specification.md)
- Para la configuración de insignias, véase la [especificación de insignias](./badge-specification.md)
- Para la especificación visual, véase la [especificación de maquetación visual del README](./readme-visual-layout-specification.md)
- Para el recorte por tipo, véase la [guía de adaptación del README por categoría](./readme-category-adaptation-guide.md)
- Para la base de la investigación, véase el [informe de investigación de plantillas de README](./readme-template-research-report.md)
- Para la redacción de características y decisiones, véase [redacción de características y decisiones de ingeniería](./features-and-engineering-tradeoffs-guide.md)
- Para las reglas de metadatos, véase la [especificación de nombres de proyecto](./project-naming-specification.md)
- Para las reglas de la hoja de ruta, véase la [especificación de hoja de ruta](./roadmap-specification.md)
