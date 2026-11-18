# Puerta de calidad

> Problema que resuelve este archivo: define las condiciones de liberación de las tres puertas, la plantilla de lista de dictamen y sus campos, para garantizar que el dictamen de liberación del push sea uniforme, ejecutable y verificable.

## 1. Las tres puertas

| Nivel | Significado | Condición de liberación |
| --- | --- | --- |
| Gate A · Puerta de seguridad | Claves, privacidad, licencia, archivos grandes | Cero P0 |
| Gate B · Puerta de calidad | Compilación, pruebas, lint, convenciones de commit, protección de ramas | Cero P0, P1 registrados como pendientes |
| Gate C · Puerta de página principal | README, metadatos, matriz de documentación, insignias, enlaces | Cero P0, P1 ≤ 3 y ya planificados |

Solo cuando A, B y C están en verde se emite `✅ ALLOW PUSH`. Los elementos no superados deben corregirse o justificarse, y el resultado se registra conforme al [formato del informe de auditoría](./audit-report-format.md).

## 2. Los 14 criterios previos a la entrega

Antes de entregar la documentación se dictamina punto por punto; los elementos no superados deben corregirse o justificarse.

| Número | Comprobación | Criterio de dictamen |
| --- | --- | --- |
| G1 | Coloquialismos y ambigüedad | Búsqueda en todo el texto de expresiones coloquiales y referencias imprecisas; número de coincidencias igual a 0 |
| G2 | Integridad de las secciones | Las versiones china e inglesa constan de 20 capítulos, en el mismo orden |
| G3 | Coherencia entre funcionalidad e índice | Cada funcionalidad descrita en el README tiene un módulo correspondiente en la estructura de directorios |
| G4 | Evidencia de las características | Cada característica cuenta con evidencia o está marcada como pendiente |
| G5 | Cobertura de los detalles de diseño | Las 10 categorías de la sección 8 cuentan con entrada o constan como no aplicables |
| G6 | Integridad de las dependencias | El número de dependencias directas e indirectas coincide con el árbol de dependencias |
| G7 | Exactitud de las licencias | El identificador SPDX de cada dependencia coincide con la declaración oficial |
| G8 | Texto original de las licencias | Las licencias que exigen texto completo lo incluyen en su versión original en inglés |
| G9 | Avisos de derechos de autor | Los avisos de derechos de autor propios y de terceros están completos |
| G10 | Sincronía bilingüe | Secciones, tablas, terminología y bloques de código son coherentes en ambos lados |
| G11 | Ejecutabilidad de los comandos | Los comandos de instalación, inicio rápido y push pueden ejecutarse directamente |
| G12 | Resumen de elementos por confirmar | Todos los elementos por confirmar están resumidos y su ubicación es localizable |
| G13 | Procedencia de los materiales | Todos los materiales cuentan con registro de fuente y licencia |
| G14 | Información sensible | Sin claves, tokens, direcciones de red interna ni información privada de personas |

## 3. Plantilla de la lista de dictamen de la puerta

```markdown
# Dictamen de la puerta: {{项目名称}} {{版本号}}

Fecha del dictamen: {{YYYY-MM-DD}} ｜ Responsable del dictamen: {{姓名}} ｜ Repositorio: {{owner/repo}}

## Gate A · Puerta de seguridad
| Número | Comprobación | Conclusión | Evidencia | Nivel | Actuación |
| --- | --- | --- | --- | --- | --- |
| A1 | Claves en el área de trabajo | PASS / FAIL / SKIP | {{命令输出}} | {{P0}} | {{动作}} |
| A2 | Claves en el historial | PASS / FAIL / SKIP | {{命令输出}} | {{P0}} | {{动作}} |
| A3 | Limpieza de información sensible | PASS / FAIL / SKIP | {{证据}} | {{P0}} | {{动作}} |
| A4 | Existencia y tipo de LICENSE | PASS / FAIL / SKIP | {{路径}} | {{P0}} | {{动作}} |
| A5 | Archivos grandes y LFS | PASS / FAIL / SKIP | {{命令输出}} | {{P0}} | {{动作}} |

Conclusión: {{PASS / FAIL}}, elementos pendientes: {{列出 / 无}}

## Gate B · Puerta de calidad
| Número | Comprobación | Conclusión | Evidencia | Nivel | Actuación |
| --- | --- | --- | --- | --- | --- |
| B1 | Compilación superada | PASS / FAIL / SKIP | {{CI URL}} | {{P0}} | {{动作}} |
| B2 | Pruebas superadas | PASS / FAIL / SKIP | {{CI URL}} | {{P0}} | {{动作}} |
| B3 | lint / format | PASS / FAIL / SKIP | {{CI URL}} | {{P1}} | {{动作}} |
| B4 | Convención de mensajes de commit | PASS / FAIL / SKIP | {{git log}} | {{P1}} | {{动作}} |
| B5 | Protección de ramas | PASS / FAIL / SKIP | {{平台设置截图说明}} | {{P0}} | {{动作}} |

Conclusión: {{PASS / FAIL}}, elementos pendientes: {{列出 / 无}}

## Gate C · Puerta de página principal
| Número | Comprobación | Conclusión | Evidencia | Nivel | Actuación |
| --- | --- | --- | --- | --- | --- |
| C1 | Los cuatro elementos del README | PASS / FAIL / SKIP | {{路径:行号}} | {{P1}} | {{动作}} |
| C2 | Matriz de documentación completa | PASS / FAIL / SKIP | {{清单}} | {{P1}} | {{动作}} |
| C3 | Metadatos completos | PASS / FAIL / SKIP | {{平台设置}} | {{P1}} | {{动作}} |
| C4 | Insignias operativas | PASS / FAIL / SKIP | {{HTTP 检查}} | {{P2}} | {{动作}} |
| C5 | Enlaces válidos | PASS / FAIL / SKIP | {{校验输出}} | {{P1}} | {{动作}} |

Conclusión: {{PASS / FAIL}}, elementos pendientes: {{列出 / 无}}

## Los 14 criterios previos a la entrega
| Número | Conclusión | Evidencia | Actuación |
| --- | --- | --- | --- |
| G1 ~ G14 | {{PASS / FAIL / SKIP}} | {{证据}} | {{动作}} |

## Dictamen global
- A: {{PASS / FAIL}} ｜ B: {{PASS / FAIL}} ｜ C: {{PASS / FAIL}}
- Conclusión de liberación: {{✅ ALLOW PUSH / ⛔ BLOCK PUSH}}
- Motivo del bloqueo: {{无 / 列出 P0}}
```

## 4. Definición de campos

| Campo | Obligatorio | Tipo | Puntos de cumplimentación | Ejemplo |
| --- | --- | --- | --- | --- |
| Responsable del dictamen | Sí | Texto | Único; se prohíbe «el equipo» | `Wang Wu` |
| Conclusión | Sí | Enumeración | PASS / FAIL / SKIP | `PASS` |
| Evidencia | Sí | Texto | Ruta + número de línea o salida de comando; se prohíbe dictaminar sin evidencia | `gitleaks: 0 findings` |
| Nivel | Obligatorio según el caso | Enumeración | Obligatorio en caso de FAIL: P0 / P1 / P2 | `P0` |
| Actuación | Obligatorio según el caso | Texto | Obligatorio en caso de FAIL: acción concreta y responsable | `Rotar la clave y limpiar el historial` |
| Motivo del SKIP | Obligatorio según el caso | Texto | Obligatorio en caso de SKIP; se prohíbe omitir sin justificación | `Sin script de compilación` |
| Conclusión de liberación | Sí | Enumeración | ALLOW PUSH / BLOCK PUSH | `BLOCK PUSH` |
| Motivo del bloqueo | Obligatorio según el caso | Texto | Obligatorio en caso de BLOCK; se enumeran los P0 | `A2 con coincidencia de clave en el historial` |

## 5. Instrucciones de cumplimentación

1. **Evidencia obligatoria**: cada dictamen debe contar con evidencia; un PASS sin evidencia se considera inválido y debe cambiarse a SKIP con la correspondiente justificación.
2. **Correspondencia de niveles**: el FAIL debe indicar nivel; el P0 bloquea directamente la liberación, el P1 debe registrarse como pendiente y el P2 se anota como recomendación.
3. **Umbral del Gate C**: solo puede obtenerse PASS con P1 ≤ 3 y ya planificados; si se supera, debe aplicarse un tratamiento degradado o el bloqueo.
4. **Uso de SKIP**: cuando no pueda comprobarse, debe marcarse SKIP con el motivo, sin escribir PASS; la comprobación se completará cuando concurran las condiciones.
5. **Coherencia**: el dictamen de la puerta debe ser coherente con los niveles P0/P1/P2 de la [matriz de dimensiones de revisión](./review-dimension-matrix.md) y con las reglas de bloqueo de las [reglas absolutas](./hard-rules.md).
6. **Liberación**: solo con las tres puertas en verde puede emitirse `✅ ALLOW PUSH`; cualquier FAIL obliga a emitir `⛔ BLOCK PUSH` y a enumerar el motivo del bloqueo.
7. **Formato de entrega**: el resultado del dictamen se emite conforme al [formato del informe de auditoría](./audit-report-format.md); una vez superado, se ejecuta la [especificación de push y publicación](./push-and-release-specification.md).

Errores frecuentes:

| Redacción incorrecta | Problema | Modo de corrección |
| --- | --- | --- |
| Conclusión PASS con evidencia vacía | Dictamen inválido | Añadir evidencia o cambiar a SKIP |
| Escribir ALLOW PUSH con P0 sin cerrar | Infringe las reglas absolutas | Cambiar a BLOCK PUSH |
| SKIP sin motivo | Posible omisión de comprobación | Añadir el motivo |
| Gate C con 5 elementos P1 y aun así PASS | Supera el umbral | Degradar o bloquear |
| Dictamen solo en texto sin lista | No verificable | Cumplimentar la plantilla punto por punto |

## 6. Ejemplo completo

```markdown
# Dictamen de la puerta: markdown-lint-cli v1.0.0

Fecha del dictamen: 2026-11-20 ｜ Responsable del dictamen: Wang Wu ｜ Repositorio: example/markdown-lint-cli

## Gate A · Puerta de seguridad
| Número | Comprobación | Conclusión | Evidencia | Nivel | Actuación |
| --- | --- | --- | --- | --- | --- |
| A1 | Claves en el área de trabajo | PASS | gitleaks detect: 0 findings | — | — |
| A2 | Claves en el historial | PASS | gitleaks --log-opts=--all: 0 findings | — | — |
| A4 | Existencia y tipo de LICENSE | PASS | LICENSE, línea 1: MIT | — | — |
| A5 | Archivos grandes y LFS | PASS | find -size +50M: ninguno | — | — |

Conclusión: PASS, elementos pendientes: ninguno

## Gate B · Puerta de calidad
| Número | Comprobación | Conclusión | Evidencia | Nivel | Actuación |
| --- | --- | --- | --- | --- | --- |
| B1 | Compilación superada | PASS | run #128 | — | — |
| B2 | Pruebas superadas | PASS | 132/132 passed | — | — |
| B4 | Convención de mensajes de commit | PASS | git log --oneline: todo conforme | — | — |

Conclusión: PASS, elementos pendientes: ninguno

## Dictamen global
- A: PASS ｜ B: PASS ｜ C: PASS
- Conclusión de liberación: ✅ ALLOW PUSH
- Motivo del bloqueo: ninguno
```

## Archivos relacionados

- Base del dictamen y niveles de fallo: [matriz de dimensiones de revisión](./review-dimension-matrix.md)
- Reglas que bloquean al infringirse: [reglas absolutas](./hard-rules.md)
- Formato de salida del dictamen: [formato del informe de auditoría](./audit-report-format.md)
- Ejecución tras superar la puerta: [especificación de push y publicación](./push-and-release-specification.md)
- Fuente de evidencia de la puerta de seguridad: [especificación de seguridad y privacidad](./security-and-privacy-specification.md)
- Fuente de evidencia de la puerta de calidad: [especificación de pruebas](./testing-specification.md), [especificación del flujo de trabajo de CI](./ci-workflow-specification.md)
- Base del dictamen de la puerta de página principal: [plantilla estándar de README](./readme-standard-template.md), [matriz de documentación](./document-matrix.md)
