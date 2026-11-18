# Especificación de redacción de Skill

> Problema que resuelve este archivo: define la estructura, las condiciones de activación y la carga progresiva al encapsular el conjunto de especificaciones como Skill, con el fin de garantizar que el Skill sea descubrible, mantenible y no duplique contenido.

## 1. Estructura de directorios

El Skill adopta una estructura de «punto de entrada + recursos bajo demanda»:

```text
skill-name/
├── SKILL.md          必需：元数据 + 核心流程
├── references/       规范正文，按需加载
└── assets/           模板与素材（可选）
```

## 2. Requisitos de SKILL.md

1. Los metadatos incluyen `name` y `description`; la descripción debe indicar «qué hace + cuándo se usa» para facilitar la activación.
2. El cuerpo solo conserva las reglas y el flujo principales de presencia permanente; el contenido detallado de consulta va en `references/`.
3. Emplear redacción imperativa o infinitiva, evitando la segunda persona.
4. Al referenciar recursos, indicar la ruta explícita y la condición de «cuándo leerlos».

## 3. Reglas obligatorias

1. El texto de las especificaciones se mantiene en un solo lugar: el Skill referencia los archivos de este conjunto de especificaciones y no copia el texto completo, evitando la deriva por duplicación.
2. Un Skill hace una sola cosa; se prohíbe concentrar múltiples responsabilidades en el mismo Skill.
3. Las condiciones de activación deben indicar frases concretas, evitando activaciones demasiado amplias.
4. La versión se actualiza de forma sincronizada con la versión del conjunto de especificaciones.

## Archivos relacionados

- Estructura del listado de metadatos: [Especificación de metadatos legibles por máquina](./machine-readable-metadata-specification.md)
- Responsabilidad única de la documentación: [Matriz de documentación](./document-matrix.md)
- Convenciones de invocación de Agent: [Especificación de invocación de Agent y de prompts](./agent-invocation-and-prompt-specification.md)
