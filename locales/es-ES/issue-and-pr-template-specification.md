# Especificación de plantillas de Issue y PR

> Problema que resuelve este archivo: define el diseño de campos, el formato y los requisitos de redacción de los formularios estructurados `.github/ISSUE_TEMPLATE/*.yml` y de la lista de autocomprobación `.github/PULL_REQUEST_TEMPLATE.md`, de modo que la notificación de problemas y el envío de cambios cuenten con restricciones de entrada ejecutables.

## 1. Principios de diseño

1. **Lo estructurado por encima del texto libre**: los formularios de Issue se definen en YAML y guían la cumplimentación mediante listas desplegables, casillas y campos obligatorios, reduciendo las notificaciones inútiles.
2. **Minimización de obligatorios**: solo se conservan los campos necesarios para localizar el problema; los campos opcionales no deben marcarse como obligatorios.
3. **Autocomprobación explícita**: la plantilla de PR enumera en forma de lista los elementos de autocomprobación marcables, evitando que quien contribuye omita pasos clave.
4. **Responsabilidad única**: el formulario de Issue recopila información y no aloja la presentación del proyecto; la plantilla de PR sirve para la autocomprobación y no repite la descripción funcional (corresponde a la [matriz de documentación](./document-matrix.md)).

## 2. Estructura del formulario de Issue

### 2.1 Archivos y denominación

- La ruta es fija: `.github/ISSUE_TEMPLATE/*.yml`, un archivo por plantilla.
- El nombre del archivo usa minúsculas y guiones, por ejemplo `bug-report.yml`, `feature-request.yml`, `question.yml`.
- Deben ofrecerse al menos dos tipos de plantilla: «informe de defecto» y «solicitud de funcionalidad».

### 2.2 Campos estándar

| Campo | Tipo | Obligatorio | Uso |
| --- | --- | --- | --- |
| `name` | Cadena | Sí | Nombre visible de la plantilla |
| `description` | Cadena | Sí | Descripción del uso de la plantilla |
| `title` | Prefijo de cadena | Sí | Prefijo automático del título del problema |
| `labels` | Array | No | Etiquetas añadidas automáticamente |
| `body` | Array | Sí | Lista de campos del formulario |

Tipos de campo habituales en `body`:

| Tipo | Escenario de aplicación | Ejemplo |
| --- | --- | --- |
| `markdown` | Texto explicativo, sin entrada | Instrucciones de cumplimentación |
| `textarea` | Descripción de texto largo | Pasos de reproducción del problema |
| `input` | Texto corto de una línea | Número de versión |
| `dropdown` | Opciones limitadas | Sistema operativo, gravedad |
| `checkboxes` | Confirmaciones múltiples | Si ya se buscaron problemas duplicados |

### 2.3 Lista de campos del informe de defecto

1. Descripción del problema (`textarea`, obligatorio): qué ocurrió.
2. Comportamiento esperado (`textarea`, obligatorio): qué debería ocurrir.
3. Pasos de reproducción (`textarea`, obligatorio): enumerados y reproducibles de forma independiente.
4. Entorno de ejecución (`input` o `dropdown`): sistema operativo, entorno de ejecución, versión del proyecto.
5. Registros o capturas de pantalla (`textarea`): aportar el mensaje de error; la información sensible debe anonimizarse.
6. Confirmación de búsqueda de duplicados (`checkboxes`, obligatorio): se han buscado issues existentes.

### 2.4 Lista de campos de la solicitud de funcionalidad

1. Planteamiento del problema (`textarea`, obligatorio): qué capacidad falta actualmente.
2. Escenario de uso (`textarea`, obligatorio): quién la necesita y en qué situación.
3. Solución esperada (`textarea`): cómo se desea implementar.
4. Alternativas (`textarea`): otras vías ya consideradas.
5. Impacto en la compatibilidad (`dropdown`): si implica cambios disruptivos.

## 3. Estructura de la plantilla de PR

### 3.1 Bloques obligatorios

`PULL_REQUEST_TEMPLATE.md` debe incluir los siguientes bloques, en orden fijo:

1. Descripción del cambio: qué se ha modificado en esta ocasión y el número de issue correspondiente.
2. Tipo de cambio: marcado con casillas (funcionalidad, corrección, documentación, refactorización, pruebas, etc.; para los tipos, véase la [especificación de mensajes de commit](./commit-message-specification.md)).
3. Lista de autocomprobación: elementos de autocomprobación marcables.
4. Cambios disruptivos: si no los hay, escribir «ninguno»; si los hay, indicar la forma de migración (véase la [especificación de guía de migración](./migration-guide-specification.md)).
5. Documentación relacionada: si se han actualizado de forma sincronizada el README, el CHANGELOG y la documentación de API.

### 3.2 Ejemplo de lista de autocomprobación

```markdown
## Lista de autocomprobación

- [ ] La compilación local pasa
- [ ] Las pruebas relacionadas pasan y la nueva funcionalidad incluye pruebas
- [ ] El mensaje de commit se ha redactado según la [especificación de mensajes de commit](./commit-message-specification.md)
- [ ] La documentación se ha actualizado de forma sincronizada o se ha confirmado que no requiere cambios
- [ ] No se han introducido secretos, datos privados ni archivos grandes
```

## 4. Plantillas copiables

### 4.1 Formulario de informe de defecto

Guardar como `.github/ISSUE_TEMPLATE/bug-report.yml`:

```yaml
name: Informe de defecto
description: Reporta una anomalía funcional reproducible
title: "[Bug]: "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        Antes de enviar, busque primero si ya existe un issue para evitar duplicados.
        No pegue claves, tokens ni datos personales.
  - type: checkboxes
    id: duplicate-check
    attributes:
      label: Comprobación de duplicados
      options:
        - label: He buscado issues existentes y confirmo que este informe no está duplicado
          required: true
  - type: textarea
    id: description
    attributes:
      label: Descripción del problema
      description: Qué ocurrió realmente
      placeholder: Tras ejecutar el comando install, el programa termina con código 1
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Comportamiento esperado
      description: Qué debería ocurrir
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: Pasos de reproducción
      description: Enumérelos para que otra persona pueda reproducirlo de forma independiente
      placeholder: |
        1. Ejecutar el comando
        2. Observar la salida
        3. Aparece la anomalía
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: Versión del proyecto
      placeholder: v1.0.0
    validations:
      required: true
  - type: dropdown
    id: os
    attributes:
      label: Sistema operativo
      options:
        - macOS
        - Linux
        - Windows
        - Otro
    validations:
      required: true
  - type: textarea
    id: logs
    attributes:
      label: Registros o capturas
      description: Aporte el mensaje de error; los datos sensibles deben anonimizarse
      render: shell
  - type: checkboxes
    id: security
    attributes:
      label: Confirmación de seguridad de la información
      options:
        - label: Confirmo que no incluye claves, tokens ni datos personales
          required: true
```

### 4.2 Formulario de solicitud de funcionalidad

Guardar como `.github/ISSUE_TEMPLATE/feature-request.yml`:

```yaml
name: Solicitud de función
description: Propone una nueva capacidad o una mejora
title: "[Feature]: "
labels: ["enhancement"]
body:
  - type: textarea
    id: problem
    attributes:
      label: Planteamiento del problema
      description: Qué capacidad falta actualmente
    validations:
      required: true
  - type: textarea
    id: scenario
    attributes:
      label: Caso de uso
      description: Quién necesita esa capacidad y en qué circunstancias
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: Solución deseada
      description: Cómo se desea implementar
  - type: textarea
    id: alternatives
    attributes:
      label: Alternativas
      description: Otras vías ya consideradas
  - type: dropdown
    id: breaking
    attributes:
      label: ¿Implica cambios incompatibles?
      options:
        - No
        - Sí
        - No estoy seguro
    validations:
      required: true
```

### 4.3 Plantilla de PR

Guardar como `.github/PULL_REQUEST_TEMPLATE.md`:

````markdown
## Descripción del cambio

{{变更说明}}

## Tipo de cambio

- [ ] Funcionalidad (feat)
- [ ] Corrección (fix)
- [ ] Documentación (docs)
- [ ] Formato (style)
- [ ] Refactorización (refactor)
- [ ] Pruebas (test)
- [ ] Compilación o cadena de herramientas (build / ci)

## Lista de autocomprobación

- [ ] La compilación local pasa
- [ ] Las pruebas relacionadas pasan y la nueva funcionalidad incluye pruebas
- [ ] El mensaje de commit se ha redactado según la especificación de mensajes de commit
- [ ] La documentación se ha actualizado de forma sincronizada o se ha confirmado que no requiere cambios
- [ ] No se han introducido secretos, datos privados ni archivos grandes

## Cambios disruptivos

{{破坏性变更说明}}

## Documentación relacionada

- [ ] El README se ha sincronizado o no requiere cambios
- [ ] El CHANGELOG está registrado
- [ ] La documentación de API se ha sincronizado o no requiere cambios
````

### 4.4 Tabla de correspondencia de marcadores de posición

| Marcador de posición | Obligatorio | Puntos clave para completar |
| --- | --- | --- |
| `{{变更说明}}` | Sí | Una frase que indique el contenido del cambio, con el número de issue en forma `#número` |
| `{{破坏性变更说明}}` | Sí | Si no hay cambios disruptivos, escribir «ninguno»; si los hay, indicar los pasos de migración y enlazar la guía de migración |

Los campos `name`, `description`, `title` y `labels` del formulario YAML son metadatos de la plantilla y se sustituyen según la situación real del proyecto; los tipos de campo y los valores de `required` en `body` se ajustan según las listas de campos de las secciones 2 y 3, sin reducir los campos obligatorios.

### 4.5 Ejemplo completo de cumplimentación

Ejemplo de cumplimentación de un informe de defecto:

````markdown
## Descripción del problema

Tras ejecutar `npm run build`, el proceso termina con código de salida 1.

## Comportamiento esperado

La compilación finaliza correctamente y genera el directorio `dist/`.

## Pasos de reproducción

1. Extraer la etiqueta v1.0.0
2. Ejecutar `npm ci`
3. Ejecutar `npm run build` y observar el código de salida 1

## Versión del proyecto

v1.0.0

## Sistema operativo

macOS

## Registros o capturas de pantalla

```
Error: Cannot find module 'mdlint-core'
```

## Confirmación de seguridad de la información

- [x] Se ha confirmado que no se incluyen secretos, tokens ni datos privados
````

## 5. Requisitos de redacción

1. Las descripciones de campo usan imperativo o enunciados declarativos; no deben ser coloquiales.
2. Cada campo obligatorio debe acompañarse de un ejemplo de cumplimentación o de un requisito de formato.
3. El texto de ayuda debe explicar «por qué se necesita esta información», evitando exigencias vacías.
4. Los campos que afectan a la privacidad deben advertir sobre la anonimización (véase la [especificación de seguridad y privacidad](./security-and-privacy-specification.md)).
5. Las plantillas se actualizan con la evolución del proyecto; los campos obsoletos deben eliminarse y no acumularse a largo plazo.

## 6. Prácticas prohibidas

1. Se prohíbe fusionar todos los tipos de problema en una única plantilla de texto libre.
2. Se prohíbe establecer campos obligatorios sin relación con la localización del problema.
3. Se prohíbe incluir presentaciones del proyecto o contenido de marketing en las plantillas.
4. Se prohíbe que la plantilla de PR omita la lista de autocomprobación y la declaración de cambios disruptivos.

## Archivos relacionados

- Para los límites de responsabilidad de los archivos, véase la [matriz de documentación](./document-matrix.md)
- Para el proceso de contribución, véase la [especificación de la guía de contribución](./contribution-guide-specification.md)
- Para los criterios de revisión, véase la [especificación de revisión de código](./code-review-specification.md)
- Para la migración de cambios disruptivos, véase la [especificación de guía de migración](./migration-guide-specification.md)
- Las comprobaciones de gobernanza comunitaria pertenecen a la dimensión D14; véase la [matriz de dimensiones de revisión](./review-dimension-matrix.md)
