# Especificación de flujo de trabajo de Git y ramas

> Problema que resuelve este archivo: define el modelo de ramas, las reglas de denominación, la plantilla de descripción de solicitudes de extracción y la estrategia de fusión, garantizando una línea principal estable, una colaboración ordenada y cambios rastreables.

## 1. Cláusulas de la especificación

1. La rama predeterminada (`main` o `master`) debe estar protegida; se prohíbe el push directo (corresponde a la regla absoluta H7).
2. Todos los cambios se integran en la línea principal mediante una rama personal y una solicitud de extracción.
3. Las ramas de larga duración y las de corta duración deben delimitarse con claridad, evitando ramas que nunca se fusionan.
4. Se prohíbe `git push --force` sobre ramas públicas; para reescribir una rama personal se usa `--force-with-lease` (corresponde a H8).
5. Se prohíbe hacer rebase o amend sobre ramas públicas ya enviadas con push; antes de la fusión deben superarse la CI y la revisión de código.

## 2. Modelo de ramas

| Tipo de rama | Ciclo de vida | Se crea desde | Se fusiona en | Formato de denominación | Ejemplo |
| --- | --- | --- | --- | --- | --- |
| Rama predeterminada | Larga | — | — | `main` | `main` |
| Rama de funcionalidad | Corta, ≤2 semanas | `main` | `main` | `feat/<descripción breve>` | `feat/user-login` |
| Rama de corrección | Corta, ≤1 semana | `main` | `main` | `fix/<descripción breve>` | `fix/token-expiry` |
| Rama de documentación | Corta | `main` | `main` | `docs/<descripción breve>` | `docs/api-guide` |
| Rama de publicación | Media | `main` | `main` + etiqueta | `release/<versión>` | `release/1.2.0` |
| Corrección urgente | Corta, ≤24 horas | Etiqueta de publicación | `main` + etiqueta | `hotfix/<descripción breve>` | `hotfix/payment-error` |

Reglas de denominación: kebab-case en minúsculas, la descripción breve debe expresar la intención; se prohíben `test`, `temp`, `wip`, `my-xxx`; cuando se vincula a un requisito se añade el número de requisito, por ejemplo `feat/spacing-rule-req001`.

## 3. Plantilla de descripción de solicitudes de extracción

```markdown
## Propósito del cambio
{{一句话说明为什么需要此变更，关联需求编号}}

## Contenido del cambio
- {{具体改动 1}}
- {{具体改动 2}}

## Alcance de impacto
- Módulos afectados: {{模块名}}
- ¿Rompe la compatibilidad? {{是 / 否；是则给出迁移说明}}
- ¿Implica configuración o migración de datos? {{是 / 否；是则说明}}

## Forma de verificación
- Comando de autocomprobación: {{命令}}
- Pruebas añadidas o modificadas: {{TC 编号}}
- Dirección de ejecución de la CI: {{URL}}

## Vinculaciones
- Requisito: {{REQ-NNN}}
- Matriz de trazabilidad: {{已更新 / 待更新}}
- Documentación: {{docs/api.md#章节 / 无}}
- Issue: {{#编号 / 无}}

## Autocomprobación
- [ ] El mensaje de commit cumple la especificación
- [ ] No se incluye información sensible
- [ ] Se ha actualizado la matriz de trazabilidad de requisitos
- [ ] Los cambios disruptivos se han registrado en el registro de cambios
```

## 4. Definición de campos

| Campo | Obligatorio | Tipo | Puntos clave para completar | Ejemplo |
| --- | --- | --- | --- | --- |
| Descripción breve de la rama | Sí | kebab-case | Debe expresar la intención por sí misma; se prohíben palabras sin información | `spacing-rule` |
| Requisito vinculado | Sí | `REQ-NNN` | Coherente con el número de inicio del proyecto | `REQ-001` |
| Propósito del cambio | Sí | Texto | Explicar «por qué», no «qué se cambió» | `Corregir el falso positivo de la puntuación china` |
| Alcance de impacto | Sí | Texto | Debe indicar si rompe la compatibilidad | `No` |
| Comando de autocomprobación | Sí | Comando | Copiable y ejecutable | `npm test -- -t spacing` |
| Número de prueba | Sí | `TC-NNN` | Coherente con la numeración de la especificación de pruebas | `TC-001` |
| Dirección de la CI | Sí | URL | Facilita la verificación del revisor | `https://github.com/.../runs/123` |
| Lista de autocomprobación | Sí | Casillas | Marcar elemento por elemento; se prohíbe marcarla entera de una vez | — |

## 5. Instrucciones de cumplimentación

1. **Ciclo de vida de la rama**: las ramas de funcionalidad que superen las 2 semanas sin fusionarse deben justificarse en la retrospectiva de iteración y dividirse o cerrarse.
2. **Denominación de la descripción breve**: tomar el sustantivo central y la acción del propósito del cambio; se prohíben nombres vagos como `fix2` o `new-feature`.
3. **Propósito del cambio**: escribir el problema y el valor; «actualizar código» u «optimizar la lógica» no son aceptables.
4. **Alcance de impacto**: al marcar que rompe la compatibilidad, debe indicarse simultáneamente `BREAKING CHANGE:` en el registro de cambios.
5. **Comando de autocomprobación**: el revisor debe poder copiarlo y ejecutarlo obteniendo la misma conclusión; si los pasos son complejos, indicar la ruta del script.
6. **Matriz de trazabilidad**: antes de fusionar la PR debe actualizarse el campo de PR de implementación y el de estado en la [especificación de la matriz de trazabilidad de requisitos](./requirements-traceability-matrix-specification.md).
7. **force push**: usar `--force-with-lease` solo en ramas propias que nadie más haya revisado, y explicar el motivo en la PR.

Errores frecuentes:

| Redacción incorrecta | Problema | Forma de corrección |
| --- | --- | --- |
| Nombre de rama `test`, `temp` | Sin información de intención | Cambiar a `feat/<capacidad concreta>` |
| Descripción de PR que solo dice «corregir bug» | Imposible revisar el impacto | Añadir propósito, impacto y forma de verificación |
| Push directo a `main` | Infringe H7 | Integrar mediante PR |
| Reescritura de una rama ya revisada seguida de push forzado | La conclusión de la revisión queda invalidada | Añadir commits nuevos para responder a los comentarios |
| No eliminar la rama de origen tras la fusión | La lista de ramas se infla | Eliminar inmediatamente tras la fusión |

## 6. Ejemplo completo

```markdown
## Propósito del cambio
Corregir el falso positivo de la regla de espaciado cuando la puntuación china está junto a una palabra en inglés (REQ-004).

## Contenido del cambio
- El motor de reglas añade detección de límites de puntuación
- Se añade el caso de regresión correspondiente

## Alcance de impacto
- Módulos afectados: regla spacing
- ¿Rompe la compatibilidad? No
- ¿Implica configuración o migración de datos? No

## Forma de verificación
- Comando de autocomprobación: `npm test -- -t "中文标点"`
- Pruebas añadidas o modificadas: TC-007-regression-142
- Dirección de ejecución de la CI: https://github.com/example/markdown-lint-cli/actions/runs/128

## Vinculaciones
- Requisito: REQ-004
- Matriz de trazabilidad: actualizada
- Documentación: ninguna
- Issue: #142

## Autocomprobación
- [x] El mensaje de commit cumple la especificación
- [x] No se incluye información sensible
- [x] Se ha actualizado la matriz de trazabilidad de requisitos
- [x] Los cambios disruptivos se han registrado en el registro de cambios (este cambio no es disruptivo)
```

## Archivos relacionados

- Criterios de revisión y gradación de comentarios: [especificación de revisión de código](./code-review-specification.md)
- Formato de los commits: [especificación de mensajes de commit](./commit-message-specification.md)
- Actualización del estado de trazabilidad: [especificación de la matriz de trazabilidad de requisitos](./requirements-traceability-matrix-specification.md)
- Ramas y publicación corresponden a la dimensión D8: [matriz de dimensiones de revisión](./review-dimension-matrix.md)
- Reglas obligatorias H7/H8: [reglas absolutas](./hard-rules.md)
- Operaciones de push: [especificación de push y publicación](./push-and-release-specification.md)
