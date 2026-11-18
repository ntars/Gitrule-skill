# Especificación de gestión de versiones

> Problema que resuelve este archivo: define las reglas del versionado semántico, el registro de decisiones de versión, la base del incremento y las relaciones de vinculación, garantizando que el número de versión exprese la naturaleza del cambio, pueda ser interpretado por herramientas y sea coherente con los artefactos publicados.

## 1. Cláusulas de la especificación

1. El número de versión sigue el versionado semántico: `MAJOR.MINOR.PATCH`.
2. El número de versión no incluye año, fecha ni número de compilación como sujeto semántico; un número de versión ya publicado no puede reutilizarse.
3. Los cambios que rompen la compatibilidad deben tratarse de forma concentrada al subir la versión mayor e incluir la forma de migrar.
4. El número de versión coincide con el tag, cuyo formato es `vMAJOR.MINOR.PATCH` (véase [Especificación de push y publicación](./push-and-release-specification.md)).
5. Las versiones previas a la publicación usan los sufijos `-alpha`, `-beta` y `-rc`, y deben validarse antes de publicar la versión estable.

## 2. Formato del número de versión y base del incremento

| Posición | Condición de incremento | Tipo de commit que lo activa | Ejemplo |
| --- | --- | --- | --- |
| MAJOR | Cambio incompatible que rompe la compatibilidad | `feat!:` / `fix!:` / `BREAKING CHANGE:` | `1.9.2 → 2.0.0` |
| MINOR | Nueva funcionalidad compatible hacia atrás | `feat` | `1.2.3 → 1.3.0` |
| PATCH | Corrección de defectos compatible hacia atrás | `fix` | `1.2.3 → 1.2.4` |

Formato de prepublicación: `vMAJOR.MINOR.PATCH-alpha.N` / `-beta.N` / `-rc.N`, con el número incrementándose desde 1; al publicar la versión estable se elimina el sufijo.

## 3. Plantilla del registro de decisiones de versión

```markdown
## Decisión de versión: {{X.Y.Z}}

- Fecha de la decisión: {{YYYY-MM-DD}}
- Responsable de la decisión: {{姓名}}
- Versión actual: {{X.Y.Z}}
- Versión objetivo: {{X.Y.Z}}
- Posición incrementada: {{MAJOR / MINOR / PATCH}}
- Base: {{列举触发的提交类型与变更内容}}

| Cambio | Tipo de commit | Requisitos asociados | ¿Rompe la compatibilidad? |
| --- | --- | --- | --- |
| {{变更描述}} | {{feat / fix / BREAKING CHANGE}} | {{REQ-NNN}} | {{是 / 否}} |

- Tratamiento de los cambios que rompen la compatibilidad: {{迁移指南链接 / 不适用}}
- Entrada del registro de cambios: {{链接}}
- tag: {{vX.Y.Z}}
- Comprobación de publicación: {{已通过 / 待通过}}
```

## 4. Plantilla del libro de versiones

```markdown
# Libro de versiones: {{项目名称}}

| Versión | Fecha de publicación | Tipo | Cambios principales | tag | Registro de cambios | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| {{X.Y.Z}} | {{YYYY-MM-DD}} | {{主版本 / 次版本 / 修订}} | {{一句话}} | {{vX.Y.Z}} | {{链接}} | {{当前 / 历史 / 已废弃}} |
| {{X.Y.Z-rc.1}} | {{YYYY-MM-DD}} | Prepublicación | {{一句话}} | {{vX.Y.Z-rc.1}} | {{链接}} | ya sustituido |

Estados: actual / histórico / obsoleto / sustituido
```

## 5. Definición de campos

| Campo | Obligatorio | Tipo | Puntos clave | Ejemplo |
| --- | --- | --- | --- | --- |
| Versión actual | Sí | `X.Y.Z` | Coincide con el tag más reciente | `1.2.3` |
| Versión objetivo | Sí | `X.Y.Z` | Solo se incrementa una posición | `1.3.0` |
| Posición incrementada | Sí | Enumeración | MAJOR / MINOR / PATCH | `MINOR` |
| Base | Sí | Lista | Enumerar los cambios que la activan; se prohíbe «actualización rutinaria» | `新增 TOML 支持` |
| Tratamiento de cambios que rompen la compatibilidad | Obligatorio condicional | Enlace | Obligatorio al incrementar MAJOR | `[迁移指南]` |
| Entrada del registro de cambios | Sí | Enlace | Apunta al tramo de la versión correspondiente | `[1.3.0]` |
| tag | Sí | `vX.Y.Z` | Correspondencia uno a uno con el número de versión | `v1.3.0` |
| Fecha de publicación | Sí | `YYYY-MM-DD` | Prevalece la fecha de creación del tag | `2026-11-20` |
| Estado | Sí | Enumeración | Actual / histórico / obsoleto / sustituido | `actual` |

## 6. Instrucciones de cumplimentación

1. **Incremento de una sola posición**: cada publicación incrementa solo una posición; cuando coexisten feat y BREAKING CHANGE se toma la posición más alta (MAJOR) y el resto de cambios se integran en esa versión.
2. **Concentración de rupturas**: varios cambios que rompen la compatibilidad se agrupan en una misma versión mayor para evitar incrementos MAJOR consecutivos.
3. **Prohibición de reutilización**: un número de versión publicado queda ocupado de forma permanente; si se retira una publicación se incrementa PATCH y se publica una versión de revisión, sin reutilizar el número original.
4. **Prepublicación**: `alpha` para validación interna, `beta` para prueba pública y `rc` para candidata a publicación; cada nivel debe pasar la CI.
5. **Verificación de coherencia**: el número de versión debe coincidir en cinco lugares: tag, registro de cambios, Release Notes, registro de despliegue y libro de versiones; si no coinciden, prevalece el tag y se corrigen los demás.
6. **Vinculación**: la base del incremento proviene del tipo de la [Especificación de mensajes de commit](./commit-message-specification.md); la explicación externa se detalla en la [Especificación del registro de cambios](./changelog-specification.md); la ruta de actualización se detalla en la [Especificación de la guía de migración](./migration-guide-specification.md).

Errores frecuentes:

| Escritura errónea | Problema | Corrección |
| --- | --- | --- |
| `v2026.11` | La fecha como sujeto semántico | Cambiar a `v2.1.0` |
| Incrementar dos posiciones en una misma versión | Semántica confusa | Incrementar solo la posición más alta |
| Reutilizar un número de versión retirado | No se pueden distinguir los artefactos | Incrementar PATCH y publicar una revisión |
| Incremento MAJOR sin guía de migración | El usuario no puede actualizar | Añadir la guía de migración y enlazarla |
| El número de versión solo existe en el tag | Libro de versiones y registro incoherentes | Sincronizar los cinco lugares |

## 7. Ejemplo completo

```markdown
## Decisión de versión: 2.0.0

- Fecha de la decisión: 2026-12-01
- Responsable de la decisión: 李四
- Versión actual: 1.9.2
- Versión objetivo: 2.0.0
- Posición incrementada: MAJOR
- Base: El formato del archivo de configuración pasa de objeto a ruta de archivo, lo que constituye un cambio incompatible.

| Cambio | Tipo de commit | Requisitos asociados | ¿Rompe la compatibilidad? |
| --- | --- | --- | --- |
| Configuración por ruta de archivo | BREAKING CHANGE | REQ-021 | Sí |
| Análisis de TOML añadido | feat | REQ-001 | No |

- Tratamiento de los cambios que rompen la compatibilidad: [Guía de migración v2.0]
- Entrada del registro de cambios: [2.0.0]
- tag: v2.0.0
- Comprobación de publicación: superada
```

## Archivos relacionados

- Tipos de commit y marcas de ruptura: [Especificación de mensajes de commit](./commit-message-specification.md)
- tag y Release Notes: [Especificación de push y publicación](./push-and-release-specification.md)
- Entradas del registro de cambios: [Especificación del registro de cambios](./changelog-specification.md)
- Ruta de actualización: [Especificación de la guía de migración](./migration-guide-specification.md)
- Origen de la versión objetivo: [Especificación de la hoja de ruta](./roadmap-specification.md)
- Coherencia de la versión en el registro de despliegue: [Especificación de despliegue y reversión](./deployment-and-rollback-specification.md)
