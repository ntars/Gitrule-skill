# Especificación de flujos de trabajo de CI

> Problema que resuelve este archivo: define las condiciones de activación, la división de tareas, la estrategia de caché y la configuración de seguridad de los flujos de trabajo de integración continua en `.github/workflows/*.yml`, de modo que la compilación, las pruebas y las comprobaciones sean reproducibles y auditables.

## 1. Principios de diseño

1. **Responsabilidad única**: cada flujo de trabajo se ocupa de un solo tipo de objetivo (compilación, pruebas, publicación, despliegue de documentación); no debe mezclarse la publicación con las pruebas en un mismo flujo de trabajo.
2. **Retroalimentación rápida**: las comprobaciones ligeras (lint, formato) van primero y las tareas costosas (matriz completa de pruebas) después.
3. **Reproducibilidad**: se fijan las versiones de las dependencias, se usan Actions de versión fija y la caché solo sirve para acelerar, sin alterar el resultado.
4. **Mínimo privilegio**: el flujo de trabajo concede permisos por tarea, con solo lectura por defecto, y las tareas de publicación elevan sus privilegios por separado (véase la [especificación de seguridad y privacidad](./security-and-privacy-specification.md)).

## 2. Estructura del archivo

### 2.1 Denominación y ruta

- La ruta es fija: `.github/workflows/*.yml`.
- El nombre del archivo usa minúsculas y guiones, y se nombra según su responsabilidad, por ejemplo `ci.yml`, `release.yml`, `docs.yml`.
- El campo `name` del flujo de trabajo debe ser coherente con la semántica del nombre del archivo.

### 2.2 Bloques obligatorios

| Bloque | Función | Requisito |
| --- | --- | --- |
| `name` | Nombre visible del flujo de trabajo | Conciso, que permita leer la responsabilidad |
| `on` | Condiciones de activación | Especificar rama, ruta o evento |
| `permissions` | Declaración de permisos | Declaración explícita, mínima por defecto |
| `jobs` | Conjunto de tareas | Dividido por responsabilidad |

### 2.3 Diseño de las condiciones de activación

| Evento de activación | Aplicación | Atención |
| --- | --- | --- |
| `push` | Rama principal y ramas de publicación | Limitar el alcance de ramas para evitar activaciones en todas ellas |
| `pull_request` | Todas las PR | Garantizar las comprobaciones antes de la fusión |
| `workflow_dispatch` | Activación manual | Para operaciones controladas como publicación y reversión |
| `schedule` | Tareas programadas | Para comprobación de actualizaciones de dependencias y compilaciones nocturnas |
| `release` | Acciones posteriores a la publicación | Para la carga de artefactos y los anuncios |

## 3. División de tareas

Orden de fases recomendado:

1. **Análisis estático**: formato, lint, comprobación de tipos.
2. **Compilación**: generar el artefacto de compilación para reutilizarlo en tareas posteriores.
3. **Pruebas**: pruebas unitarias y de integración, paralelizables mediante matriz.
4. **Validación de artefactos**: comprobar tamaño, firma o integridad del artefacto de compilación.
5. **Publicación**: ejecutar solo cuando la CI esté completamente en verde y se cumplan las condiciones (véase la [especificación de push y publicación](./push-and-release-specification.md)).

Las tareas declaran sus dependencias mediante `needs`, de modo que un fallo interrumpa de inmediato; las tareas posteriores no deben continuar en estado de fallo.

## 4. Compilación matricial

Usar `strategy.matrix` para cubrir múltiples versiones y plataformas:

```yaml
strategy:
  fail-fast: false
  matrix:
    os: [ubuntu-latest, macos-latest, windows-latest]
    node-version: [18, 20, 22]
```

Requisitos:

- La cobertura de versiones debe incluir la versión mínima y la más reciente que el proyecto declara soportar (véase el capítulo 14 de la [explicación de compatibilidad](./readme-sections-specification.md)).
- `fail-fast` se establece en `false` para que cada combinación se ejecute por completo y sea más fácil localizar problemas de compatibilidad.
- Las dimensiones de la matriz no deben superar tres, para evitar una explosión combinatoria.

## 5. Estrategia de caché

| Objeto de caché | Clave sugerida | Atención |
| --- | --- | --- |
| Directorio de dependencias | Hash del archivo de bloqueo del gestor de paquetes | Se invalida al cambiar el archivo de bloqueo |
| Artefacto de compilación | Hash del código fuente y la configuración | Coherente con las entradas de compilación |
| Cadena de herramientas | Número de versión | Se invalida al actualizar la versión |

La caché solo acelera, no altera el resultado de la compilación; aunque haya acierto de caché, deben ejecutarse igualmente las pruebas completas.

## 6. Configuración de seguridad

1. Los secretos se inyectan mediante los Secrets del repositorio; se prohíbe escribirlos en el archivo del flujo de trabajo o en los registros.
2. Cada flujo de trabajo declara `permissions` de forma explícita, con `contents: read` por defecto.
3. Las Actions de terceros se referencian por versión fija o hash de commit, evitando etiquetas flotantes.
4. Cuando la PR proviene de un Fork, se prohíbe inyectar Secrets, para prevenir ataques de elevación de privilegios.
5. Las tareas de publicación se separan de las comprobaciones principales y solo se activan en ramas protegidas o en etiquetas.

## 7. Insignias de estado

El flujo de trabajo debe proporcionar al README una insignia de estado, con el formato:

```markdown
[![CI](https://github.com/{owner}/{repo}/actions/workflows/ci.yml/badge.svg)](https://github.com/{owner}/{repo}/actions/workflows/ci.yml)
```

Para los parámetros y la disposición de las insignias, véase la [especificación de insignias](./badge-specification.md).

## 8. Prácticas prohibidas

1. Se prohíbe codificar de forma rígida secretos o direcciones internas en el flujo de trabajo.
2. Se prohíbe usar `continue-on-error` para ocultar fallos de pruebas.
3. Se prohíbe configurar varias reglas de activación mutuamente conflictivas para una misma condición.
4. Se prohíbe publicar mientras las comprobaciones de la rama principal no hayan pasado.

## Archivos relacionados

- Para los límites de responsabilidad de los archivos, véase la [matriz de documentación](./document-matrix.md)
- Para la compilación y las pruebas locales, véase la [especificación de pruebas](./testing-specification.md)
- Para la vinculación con la publicación, véase la [especificación de push y publicación](./push-and-release-specification.md)
- Las comprobaciones automatizadas pertenecen a la dimensión D9; véase la [matriz de dimensiones de revisión](./review-dimension-matrix.md)
- Para las líneas rojas sobre secretos, véase H3 en las [reglas absolutas](./hard-rules.md)
