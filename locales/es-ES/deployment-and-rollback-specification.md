# Especificación de despliegue y reversión

> Problema que resuelve este archivo: define las plantillas, los campos y los criterios de ejecución de la lista de despliegue, la orden de cambio y el plan de reversión, para garantizar un despliegue controlable, un estado consultable y una recuperación rápida ante fallos.

## 1. Articulado de la especificación

1. Antes del despliegue deben superarse la CI, la revisión de código y la puerta de calidad (véase la [puerta de calidad](./quality-gate.md)).
2. El despliegue se basa en una versión de publicación ya etiquetada con tag y no utiliza commits sin etiquetar (véase la [especificación de gestión de versiones](./version-management-specification.md)).
3. La configuración del entorno se separa del código; la configuración sensible se inyecta mediante gestión de configuración y no se incorpora al repositorio (véase la [especificación de seguridad y privacidad](./security-and-privacy-specification.md)).
4. Los cambios de estructura de la base de datos se ejecutan mediante scripts de migración y deben ser compatibles con versiones anteriores (véase la [especificación de diseño de bases de datos](./database-design-specification.md)).
5. Cada despliegue debe registrar el número de versión, la hora, el operador y el contenido del cambio; un despliegue sin registro se considera no conforme.
6. Cada versión debe disponer de un plan de reversión preparado con antelación; sin plan de reversión no debe desplegarse.
7. Tras el despliegue deben ejecutarse la comprobación de estado y la validación de humo; la publicación solo termina cuando ambas se superan.

## 2. Plantilla de la lista de despliegue

```markdown
# Lista de despliegue: {{项目名称}} {{版本号}}

Versión: {{vX.Y.Z}} ｜ tag: {{vX.Y.Z}} ｜ Entorno de destino: {{预发布 / 生产}} ｜ Hora prevista: {{YYYY-MM-DD HH:MM}}

## Comprobaciones previas
- [ ] CI en verde; dirección de ejecución del flujo de trabajo: {{URL}}
- [ ] Revisión de código superada; aprobador: {{姓名}}
- [ ] Puertas de calidad A/B/C con PASS
- [ ] Registro de cambios y Release Notes preparados
- [ ] Plan de reversión revisado, véase el final de esta sección
- [ ] Script de migración de la base de datos revisado y compatible con versiones anteriores
- [ ] Lista de cambios de configuración confirmada (elementos inyectados que no entran en el repositorio)

## Contenido del cambio
| Elemento del cambio | Tipo | Alcance del impacto | Requisito vinculado | Modo de verificación |
| --- | --- | --- | --- | --- |
| {{功能 / 配置 / 数据迁移}} | {{新增 / 修改 / 移除}} | {{受影响模块}} | {{REQ-NNN}} | {{如何确认}} |

## Pasos de ejecución
1. {{步骤，含具体命令或平台操作}}
2. {{灰度比例与观察时长}}
3. {{全量放量条件}}

## Comprobación de estado y validación de humo
| Comprobación | Condición de dictamen | Modo de ejecución | Resultado |
| --- | --- | --- | --- |
| Servicio activo | {{HTTP 200}} | {{命令}} | {{通过 / 未通过}} |
| Ruta crítica | {{主流程完成}} | {{命令}} | {{通过 / 未通过}} |
| Tasa de errores | {{< X%}} | {{监控面板}} | {{通过 / 未通过}} |

## Registro de despliegue
| Elemento | Valor |
| --- | --- |
| Hora real del despliegue | {{YYYY-MM-DD HH:MM}} |
| Operador | {{姓名}} |
| Aprobador | {{姓名}} |
| Número de versión real | {{vX.Y.Z}} |
| Resultado | {{成功 / 回滚 / 中止}} |

## Plan de reversión
- Versión de destino de la reversión: {{vX.Y.Z}}
- Condición de activación: {{错误率 > X% 持续 N 分钟 / 冒烟失败 / 数据异常}}
- Responsable de la decisión: {{姓名}}
- Pasos de reversión: {{具体命令或操作}}
- Compatibilidad de datos: {{是否需要数据回滚；如果需要，说明方式}}
```

## 3. Plantilla del registro de despliegue

```markdown
## {{YYYY-MM-DD}} {{vX.Y.Z}} → {{环境}}

- Número de versión: {{vX.Y.Z}}
- tag: {{vX.Y.Z}}
- Hora: {{HH:MM}}
- Operador / Aprobador: {{姓名 / 姓名}}
- Resumen del cambio: {{一句话}}
- Comprobación de estado: {{通过 / 未通过}}
- Resultado: {{成功 / 回滚}}
- Publicación vinculada: {{Release Notes URL}}
- Observaciones: {{异常与处理记录；无则写「无」}}
```

## 4. Definición de campos

| Campo | Obligatorio | Tipo | Puntos de cumplimentación | Ejemplo |
| --- | --- | --- | --- | --- |
| tag | Sí | Texto | Idéntico al tag de la [especificación de gestión de versiones](./version-management-specification.md) | `v1.2.0` |
| Entorno de destino | Sí | Enumeración | Preproducción / producción; no deben mezclarse configuraciones | `Producción` |
| Tipo del elemento de cambio | Sí | Enumeración | Añadido / modificado / eliminado | `Modificado` |
| Requisito vinculado | Sí | Lista | Números REQ; si no hay cambio de requisito, escribir «ninguno» | `REQ-007` |
| Proporción de despliegue gradual | No | Porcentaje | Obligatorio cuando se despliega de forma gradual | `10% → 50% → 100%` |
| Condición de dictamen | Sí | Umbral | Observable y verificable | `HTTP 200` |
| Número de versión real | Sí | Texto | Si difiere del previsto, debe justificarse | `v1.2.1` |
| Condición de activación de la reversión | Sí | Umbral + duración | Se prohíben expresiones del tipo «si se nota algo raro» | `Tasa de errores >1 % durante 5 minutos` |
| Compatibilidad de datos | Sí | Texto | Precisar si se requiere reversión de datos | `No se requiere reversión de datos` |

## 5. Instrucciones de cumplimentación

1. **Comprobaciones previas**: deben marcarse una por una; se prohíbe marcarlas todas de una vez; si alguna no se cumple, el despliegue se interrumpe.
2. **Contenido del cambio**: cada elemento debe vincularse a un número REQ; los cambios puramente operativos sin requisito asociado deben indicar «ninguno» y justificar la base del cambio.
3. **Comprobación de estado**: las condiciones deben poder dictaminarse automáticamente; «el servicio parece funcionar» no es admisible.
4. **Condición de activación de la reversión**: debe indicarse a la vez el umbral y la duración, para evitar activaciones falsas por fluctuaciones puntuales.
5. **Despliegue gradual**: tras cada tramo debe observarse el tiempo establecido y registrarse la conclusión, antes de pasar al siguiente tramo.
6. **Registro de despliegue**: se añade por orden cronológico y no sobrescribe el historial; el número de versión debe coincidir con el del push, el tag y las Release Notes.
7. **Ejecución de la reversión**: la reversión de código se realiza con `git revert`, que genera un commit inverso, sin forzar el push sobre un historial ya público (véase la [especificación de push y publicación](./push-and-release-specification.md)).

Errores frecuentes:

| Redacción incorrecta | Problema | Modo de corrección |
| --- | --- | --- |
| Desplegar con un commit sin tag | La versión no se puede reproducir | Etiquetar con tag antes de desplegar |
| Plan de reversión escrito como «si hay problemas, revertir» | Sin condiciones de activación ni pasos | Añadir umbral, responsable de la decisión y pasos |
| Cambio de base de datos incompatible con la versión anterior | Los datos no sirven tras la reversión | Aplicar el método de tres pasos: expandir, migrar y contraer |
| Registro de despliegue redactado a posteriori | El estado deja de ser fiable | Registrar en el momento del despliegue |
| Comprobación de estado limitada a la página principal | No se valida la ruta crítica | Añadir casos de humo del flujo principal |

## 6. Ejemplo completo

```markdown
# Lista de despliegue: markdown-lint-cli v1.0.0

Versión: v1.0.0 ｜ tag: v1.0.0 ｜ Entorno de destino: producción ｜ Hora prevista: 2026-11-20 10:00

## Comprobaciones previas
- [x] CI en verde: https://github.com/example/markdown-lint-cli/actions/runs/123
- [x] Revisión de código superada; aprobador: Li Si
- [x] Puertas de calidad A/B/C con PASS
- [x] Registro de cambios y Release Notes preparados
- [x] Plan de reversión revisado
- [x] Sin migración de base de datos
- [x] Lista de cambios de configuración confirmada: ninguno

## Contenido del cambio
| Elemento del cambio | Tipo | Alcance del impacto | Requisito vinculado | Modo de verificación |
| --- | --- | --- | --- | --- |
| Regla de espacios entre chino e inglés | Añadido | Motor de reglas | REQ-001 | Ejecutar TC-001 |
| Salida del informe de CLI | Modificado | Módulo de informes | REQ-007 | Ejecutar TC-012 |

## Pasos de ejecución
1. Obtener el tag v1.0.0 y verificar su suma de comprobación
2. Despliegue gradual al 10 %, observación de 10 minutos
3. Tras confirmar una tasa de errores <0,1 %, ampliar al 100 %

## Comprobación de estado y validación de humo
| Comprobación | Condición de dictamen | Modo de ejecución | Resultado |
| --- | --- | --- | --- |
| Servicio activo | HTTP 200 | curl /healthz | Superado |
| Ruta crítica | Comprobación de 50 documentos completada | script de shell | Superado |
| Tasa de errores | <0,1 % | Panel de monitorización | Superado |

## Plan de reversión
- Versión de destino de la reversión: v0.9.3
- Condición de activación: tasa de errores >1 % durante 5 minutos
- Responsable de la decisión: Li Si
- Pasos de reversión: cambiar la etiqueta de despliegue a v0.9.3 y ejecutar la comprobación de compatibilidad de datos
- Compatibilidad de datos: sin cambios en la base de datos; no se requiere reversión de datos
```

## Archivos relacionados

- Reglas de versión y tag: [especificación de gestión de versiones](./version-management-specification.md)
- Acciones de push y tratamiento de incidentes: [especificación de push y publicación](./push-and-release-specification.md)
- Clasificación de incidentes y retrospectiva: [especificación de respuesta a incidentes](./incident-response-specification.md)
- Soporte de indicadores y alertas: [especificación de observabilidad](./observability-specification.md)
- Scripts de migración y compatibilidad: [especificación de diseño de bases de datos](./database-design-specification.md)
- Inyección de configuración sensible: [especificación de seguridad y privacidad](./security-and-privacy-specification.md)
