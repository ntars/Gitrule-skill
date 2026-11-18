# Especificación de la retrospectiva de iteración

> Problema que resuelve este archivo: define la plantilla de retrospectiva posterior a una iteración, sus campos y el mecanismo de seguimiento de las acciones de mejora, para garantizar que los problemas se conviertan en acciones ejecutables y verificables para la siguiente ronda y evitar la repetición de errores.

## 1. Articulado de la especificación

1. Al término de cada iteración debe completarse la retrospectiva en un plazo de cinco días hábiles; todo retraso debe justificarse.
2. La retrospectiva debe basarse en datos factuales; se prohíbe sustituir la medición por impresiones; para las fuentes de datos, véase la [especificación de métricas de calidad](./quality-metrics-specification.md).
3. Cada problema debe precisar su causa raíz, la acción de mejora, el responsable y el modo de verificación; los elementos sin responsable o sin modo de verificación no deben entrar en la lista de acciones.
4. El número máximo de acciones de mejora es de tres, ordenadas por impacto; si se superan las tres, deben fusionarse o degradarse a recomendaciones.
5. Las acciones de mejora de la ronda anterior deben verificarse una por una en la retrospectiva de la ronda actual; las no completadas deben justificarse y reprogramarse.
6. La documentación de retrospectiva solo registra la mejora del proceso y no el contenido de los cambios de versión, que corresponde a la [especificación del registro de cambios](./changelog-specification.md).

## 2. Plantilla del documento de retrospectiva

```markdown
# Retrospectiva de iteración: {{项目名称}} {{迭代标识}}

Ciclo de la iteración: {{YYYY-MM-DD ~ YYYY-MM-DD}} ｜ Moderación: {{姓名}} ｜ Participantes: {{姓名列表}} ｜ Fecha de la retrospectiva: {{YYYY-MM-DD}}

## 1. Revisión de objetivos
| Objetivo de la iteración | Origen | Grado de consecución | Base del dictamen |
| --- | --- | --- | --- |
| {{目标描述}} | {{路线图 / 立项书}} | {{达成 / 未达成 / 部分达成}} | {{数据或交付物}} |

## 2. Instantánea de datos
| Indicador | Valor de la ronda anterior | Valor de esta ronda | Variación | Objetivo |
| --- | --- | --- | --- | --- |
| Requisitos entregados | | | | |
| Defectos escapados | | | | |
| Duración media de CI | | | | |
| Cobertura de requisitos | | | | |
| Número de incidentes | | | | |

## 3. Lista de hechos
- Favorable: {{基于数据的事实，如「本轮 CI 全绿率 98%」}}
- Obstáculo: {{基于数据的障碍，如「集成环境等待平均 4 小时」}}
- Imprevisto: {{未预见的事件及其影响}}

## 4. Problemas y causas raíz
| Número | Problema | Evidencia | Causa raíz | Impacto |
| --- | --- | --- | --- | --- |
| R-01 | {{问题描述}} | {{数据 / 事件}} | {{根因，非表象}} | {{造成的影响}} |

## 5. Acciones de mejora
| Número | Problema vinculado | Acción | Responsable | Fecha límite | Modo de verificación | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| A-01 | R-01 | {{具体动作}} | {{姓名}} | {{YYYY-MM-DD}} | {{如何验证生效}} | Pendiente de inicio |

## 6. Verificación de las acciones de la ronda anterior
| Número | Acción | Estado en la ronda anterior | Conclusión de esta ronda | Tratamiento posterior |
| --- | --- | --- | --- | --- |
| A-00 | {{动作}} | En curso | {{完成 / 未完成 / 放弃}} | {{继续 / 重排 / 关闭并说明}} |

## 7. Consensos y cuestiones pendientes
- Consenso de esta ronda: {{需要长期遵守的约定}}
- Cuestiones pendientes: {{不在本轮处理的问题及原因}}
```

## 3. Plantilla de entrada de acción de mejora

```markdown
### A-{{两位序号}}：{{动作标题}}

- Problema vinculado: {{R-NN}}
- Acción: {{一个可执行的动作，含具体对象}}
- Responsable: {{姓名，唯一}}
- Fecha límite: {{YYYY-MM-DD}}
- Modo de verificación: {{可判定的检查和阈值}}
- Efecto esperado: {{用指标描述}}
- Estado: Pendiente de inicio / en curso / completado / abandonado
```

## 4. Definición de campos

| Campo | Obligatorio | Tipo | Puntos de cumplimentación | Ejemplo |
| --- | --- | --- | --- | --- |
| Identificador de iteración | Sí | Texto | Coherente con el número de fase de la [especificación de la hoja de ruta](./roadmap-specification.md) | `Sprint-12` |
| Grado de consecución | Sí | Enumeración | Alcanzado / no alcanzado / parcialmente alcanzado | `Parcialmente alcanzado` |
| Base del dictamen | Sí | Texto | Enlace a datos o entregables; no debe quedar vacío | `REQ-001 publicado` |
| Instantánea de datos | Sí | Tabla | Al menos 3 indicadores, con valores de la ronda anterior y de la actual | `Defectos escapados 2 → 0` |
| Causa raíz | Sí | Texto | Debe distinguirse el síntoma de la causa raíz y encadenarse con «porque» de forma verificable | `Porque el entorno no está integrado en CI` |
| Acción | Sí | Texto | Acción única, con objeto y comportamiento | `Integrar el entorno de integración en CI` |
| Responsable | Sí | Texto | Único; se prohíbe escribir «el equipo» | `Wang Wu` |
| Modo de verificación | Sí | Texto | Verificable, con el momento de la comprobación | `Duración de CI de la próxima ronda <10 minutos` |
| Estado | Sí | Enumeración | Uno de los cuatro estados | `Completado` |

## 5. Instrucciones de cumplimentación

1. **Revisión de objetivos**: se toma como referencia el objetivo original del inicio del proyecto o de la hoja de ruta y no se reescribe el objetivo para que coincida con el resultado.
2. **Instantánea de datos**: debe utilizarse el mismo criterio que en la ronda anterior; si el criterio cambia, deben indicarse al mismo tiempo «criterio modificado» y las definiciones antigua y nueva.
3. **Lista de hechos**: solo se escriben hechos verificables; los juicios subjetivos del tipo «la comunicación no fue fluida» deben convertirse en sucesos y momentos concretos.
4. **Causa raíz**: debe indagarse de forma sucesiva hasta llegar a un nivel sobre el que pueda actuarse; «porque las pruebas son insuficientes» sigue siendo un síntoma, mientras que «porque los requisitos no están vinculados a casos de prueba» sí es una causa raíz.
5. **Número de acciones**: como máximo tres; si hay más de tres problemas, se ordenan por impacto y los no incluidos se registran en «cuestiones pendientes».
6. **Modo de verificación**: debe indicar el momento de la comprobación y el umbral de dictamen; «observar más adelante» no es admisible.
7. **Verificación de la ronda anterior**: debe darse una conclusión para cada acción, sin omitir bloques completos; los abandonos deben justificarse.

Errores frecuentes:

| Redacción incorrecta | Problema | Modo de corrección |
| --- | --- | --- |
| «Todos debemos dar más importancia a la calidad» | Sin acción ni responsable | Convertir en una acción y un responsable concretos |
| Causa raíz escrita como «descuido» | No verificable ni mejorable | Indagar hasta el nivel de proceso o herramienta |
| Ocho acciones de mejora | Imposible de ejecutar | Ordenar por impacto y tomar las tres primeras |
| Modo de verificación escrito como «ver cómo va» | No verificable | Añadir umbral y momento de comprobación |
| Acciones de la ronda anterior sin verificar | Se rompe el ciclo de mejora | Cumplimentar la conclusión de esta ronda para cada acción |

## 6. Ejemplo completo

```markdown
# Retrospectiva de iteración: markdown-lint-cli Sprint-12

Ciclo de la iteración: 2026-11-10 ~ 2026-11-21 ｜ Moderación: Li Si ｜ Participantes: Wang Wu y Zhao Liu ｜ Fecha de la retrospectiva: 2026-11-23

## 1. Revisión de objetivos
| Objetivo de la iteración | Origen | Grado de consecución | Base del dictamen |
| --- | --- | --- | --- |
| Publicar las reglas básicas de v1.0.0 | Hoja de ruta S12 | Alcanzado | tag v1.0.0 publicado |
| Cobertura de requisitos del 100 % | Inicio del proyecto G1 | Parcialmente alcanzado | 13/14 requisitos obligatorios cerrados |

## 2. Instantánea de datos
| Indicador | Valor de la ronda anterior | Valor de esta ronda | Variación | Objetivo |
| --- | --- | --- | --- | --- |
| Requisitos entregados | 6 | 14 | +8 | 14 |
| Defectos escapados | 2 | 1 | -1 | 0 |
| Cobertura de requisitos | 85% | 92.9% | +7.9% | 100% |

## 4. Problemas y causas raíz
| Número | Problema | Evidencia | Causa raíz | Impacto |
| --- | --- | --- | --- | --- |
| R-01 | REQ-003 sin caso de prueba | El campo TC de la matriz de trazabilidad figura como «pendiente» | Porque en la revisión de requisitos no se validaba obligatoriamente la integridad de la matriz de trazabilidad | Cobertura de requisitos por debajo del objetivo |

## 5. Acciones de mejora
| Número | Problema vinculado | Acción | Responsable | Fecha límite | Modo de verificación | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| A-01 | R-01 | Añadir la comprobación «matriz de trazabilidad cumplimentada» a la lista de revisión de requisitos | Wang Wu | 2026-11-27 | Los 5 registros de revisión de la próxima ronda incluyen dicha casilla marcada | Pendiente de inicio |
```

## Archivos relacionados

- Datos de trazabilidad de requisitos a publicación: [especificación de la matriz de trazabilidad de requisitos](./requirements-traceability-matrix-specification.md)
- Criterios de los indicadores y método estadístico: [especificación de métricas de calidad](./quality-metrics-specification.md)
- Fases y origen de los objetivos: [especificación de la hoja de ruta](./roadmap-specification.md)
- Contenido de los cambios de versión: [especificación del registro de cambios](./changelog-specification.md)
- Retrospectiva y mejora de incidentes: [especificación de respuesta a incidentes](./incident-response-specification.md)
- Fase de ejecución del seguimiento: [proceso de ejecución](./execution-process.md)
