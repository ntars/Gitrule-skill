# Especificación de la guía de migración

> Problema que resuelve este archivo: define la estructura, los elementos de contenido y el momento de publicación de la guía de migración ante un cambio disruptivo, para que el usuario pueda actualizarse de forma gradual desde la versión antigua a la nueva siguiendo unos pasos.

## 1. Condiciones de activación

Debe ofrecerse una guía de migración cuando concurra cualquiera de las siguientes circunstancias:

1. El mensaje de commit contiene `BREAKING CHANGE:`, `feat!:` o `fix!:` (véase la [especificación de mensajes de commit](./commit-message-specification.md)).
2. Cambian los nombres de claves de configuración, los valores por defecto o su prioridad.
3. Cambian las firmas de la API, la estructura de retorno o los códigos de error.
4. Se eleva la versión mínima de tiempo de ejecución o se deja de soportar una plataforma.
5. Cambia la estructura de directorios o la nomenclatura de archivos y ello afecta a las rutas que el usuario referencia.

## 2. Ubicación y nomenclatura de los archivos

1. Las indicaciones de migración de menor alcance se incluyen en la entrada de la versión correspondiente de `CHANGELOG.md`.
2. Cuando el cambio es mayor e implica operaciones de varios pasos, se crea un archivo independiente en el directorio `docs/migration/`, nombrado por versión, por ejemplo `docs/migration/v2.md`.
3. La ruta de migración completa entre versiones mayores se indexa en `docs/migration/README.md`.
4. El README solo incluye el aviso de migración y el enlace, sin desplegar los pasos (véase la [matriz de documentación](./document-matrix.md)).

## 3. Estructura del documento

La guía de migración debe organizarse en el siguiente orden:

1. **Título y versión**: indicar la versión de origen y la de destino, por ejemplo «Migración de v1.x a v2.0».
2. **Visión general del impacto**: enumerar las categorías de cambio y su alcance, y precisar qué usuarios deben migrar obligatoriamente.
3. **Requisitos previos**: las preparaciones que deben completarse antes de migrar, como copias de seguridad o actualización de la versión del entorno.
4. **Lista de cambios**: enumerar uno por uno los cambios disruptivos, cada uno con «comportamiento anterior», «comportamiento nuevo» y «motivo del cambio».
5. **Pasos de migración**: enumerar de forma numerada las operaciones ejecutables, con comandos o ejemplos de código.
6. **Modo de verificación**: cómo confirmar el éxito tras la migración, con comandos de comprobación o salidas esperadas.
7. **Modo de reversión**: cómo restaurar la versión antigua si la migración falla.
8. **Preguntas frecuentes**: enumerar las preguntas más habituales y sus respuestas.
9. **Obtención de ayuda**: remitir a los issues, al foro de discusión o al sitio de documentación.

### 3.1 Plantilla en blanco copiable

La siguiente plantilla se corresponde punto por punto con las nueve partes de la sección 3; basta copiarla y sustituir los marcadores de posición para utilizarla:

````markdown
# Migración de {{源版本}} a {{目标版本}}

> Esta guía describe todas las operaciones necesarias para actualizar de {{源版本}} a {{目标版本}} y se aplica a {{适用使用者范围}}.

## 1. Visión general del impacto

| Categoría de cambio | Contenido concreto | Alcance del impacto | Migración obligatoria |
| --- | --- | --- | --- |
| {{变更类别}} | {{变更内容}} | {{受影响的使用者场景}} | {{是否必须迁移}} |

## 2. Requisitos previos

- {{前置准备}}
- {{检查项与确认命令}}

## 3. Lista de cambios

### {{变更项名称}}

- Comportamiento anterior: {{旧版本行为}}
- Comportamiento nuevo: {{新版本行为}}
- Motivo del cambio: {{变更原因}}

Antes de migrar:

```{{代码语言}}
{{旧配置或旧代码}}
```

Después de migrar:

```{{代码语言}}
{{新配置或新代码}}
```

## 4. Pasos de migración

1. {{迁移步骤}}
2. {{迁移步骤}}
3. {{人工处理步骤}}

## 5. Modo de verificación

```bash
{{可独立运行的检查命令}}
```

Salida esperada: {{预期结果}}

## 6. Modo de reversión

1. {{恢复旧版本的操作}}
2. {{恢复旧配置的操作}}

## 7. Preguntas frecuentes

### {{问题}}

Respuesta: {{解答}}

## 8. Obtención de ayuda

- Reporte de problemas: {{issue 地址}}
- Foro de discusión: {{讨论区地址}}
- Documentación relacionada: {{文档链接}}
````

Correspondencia de marcadores de posición:

| Marcador de posición | Obligatorio | Puntos de cumplimentación |
| --- | --- | --- |
| `{{源版本}}` / `{{目标版本}}` | Sí | Coherente con el tag de destino, formato `vX.Y.Z` |
| `{{适用使用者范围}}` | Sí | Precisar qué usuarios deben migrar obligatoriamente, evitando formulaciones ambiguas |
| `{{变更类别}}` | Sí | Al menos una de las cuatro categorías: configuración, API, tiempo de ejecución, directorios |
| `{{是否必须迁移}}` | Sí | Precisar si el cambio exige al usuario ejecutar la migración |
| `{{旧行为}}` / `{{新行为}}` | Sí | Contraposición punto por punto; no debe escribirse solo uno de los dos lados |
| `{{代码语言}}` | Sí | Identificador de lenguaje del bloque de código, como `yaml`, `json`, `js` |
| `{{前置准备}}` | Sí | Copia de seguridad y comprobaciones del entorno que deben completarse antes de migrar |
| `{{迁移步骤}}` | Sí | Cada paso debe ser directamente ejecutable e incluir comandos o código |
| `{{人工处理步骤}}` | Sí | Los pasos no automatizables deben marcarse expresamente aquí |
| `{{检查命令}}` / `{{预期结果}}` | Sí | El comando debe poder ejecutarse de forma independiente y el resultado debe ser verificable |
| `{{回滚方式}}` | Sí | No debe omitirse; véase la sección 7 de prácticas prohibidas |

## 4. Requisitos de contenido

### 4.1 Ejemplo de contraposición de cambios

```markdown
### La clave de configuración `timeout` pasa a llamarse `timeoutMs`

- Comportamiento anterior: se usaba `timeout: 5000` en el archivo de configuración, en segundos.
- Comportamiento nuevo: se usa `timeoutMs: 5000`, en milisegundos.
- Motivo del cambio: unificar la unidad de tiempo y evitar incoherencias con los parámetros de la API.

Antes de migrar:

```yaml
timeout: 5
```

Después de migrar:

```yaml
timeoutMs: 5000
```

### 4.2 Requisitos de redacción

1. Cada paso debe ofrecer un comando o código directamente ejecutable; no basta con describir «modificar la configuración».
2. Debe ofrecerse la contraposición entre antes y después de la migración, para facilitar la comprobación punto por punto.
3. Deben marcarse expresamente los pasos no automatizables que requieren intervención manual.
4. El alcance del impacto debe ser concreto; deben evitarse formulaciones ambiguas como «puede afectar a parte de los usuarios».
5. Los comandos de verificación deben poder ejecutarse de forma independiente e incluir la salida esperada.

## 5. Momento de publicación y vinculaciones

1. La guía de migración debe publicarse de forma sincronizada con la versión que contiene el cambio disruptivo, sin retraso.
2. La entrada correspondiente de `CHANGELOG.md` debe enlazar con la guía de migración (véase la [especificación del registro de cambios](./changelog-specification.md)).
3. El bloque de cambios disruptivos de la plantilla de PR debe indicar que se cumplimente el modo de migración (véase la [especificación de plantillas de Issue y PR](./issue-and-pr-template-specification.md)).
4. El número de versión sigue el versionado semántico y todo cambio disruptivo debe incrementar la versión mayor (véase la [especificación de gestión de versiones](./version-management-specification.md)).
5. El README debe avisar en un lugar destacado a los usuarios de versiones antiguas de que lean la guía de migración.

## 6. Política de obsolescencia y conservación

1. La guía de migración debe conservarse de forma permanente y no debe eliminarse tras publicar la nueva versión.
2. La documentación de versiones antiguas puede marcarse como «ya no mantenida», pero debe conservarse su punto de entrada.
3. Las actualizaciones que cruzan varias versiones mayores deben ofrecer una ruta por etapas y no deben exigir cruzar todos los cambios de una sola vez.

## 7. Prácticas prohibidas

1. Se prohíbe escribir solo «hay cambios disruptivos; ajústelo por su cuenta».
2. Se prohíbe omitir el modo de reversión.
3. Se prohíbe utilizar en los pasos de migración pseudocódigo que no pueda ejecutarse.
4. Se prohíbe eliminar las guías de migración de versiones históricas.

## Archivos relacionados

- Para la estructura del registro de cambios, véase la [especificación del registro de cambios](./changelog-specification.md)
- Para las reglas de incremento de versión, véase la [especificación de gestión de versiones](./version-management-specification.md)
- Para la declaración de cambios disruptivos en el mensaje de commit, véase la [especificación de mensajes de commit](./commit-message-specification.md)
- Para los límites de responsabilidad documental, véase la [matriz de documentación](./document-matrix.md)
- Para el proceso de publicación, véase la [especificación de push y publicación](./push-and-release-specification.md)
