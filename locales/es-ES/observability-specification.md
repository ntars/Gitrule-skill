# Especificación de observabilidad

> Problema que resuelve este archivo: define los campos de registro, los objetivos SLI/SLO, las reglas de alerta y la plantilla de ficha de respuesta a alertas, para garantizar que el estado del sistema sea visible, que los fallos puedan localizarse y que las alertas sean ejecutables.

## 1. Artículos de la especificación

1. La observabilidad se compone de tres pilares: registros, métricas y trazas; los tres deben correlacionarse mediante un identificador de petición unificado.
2. Los registros deben ser estructurados e incluir marca de tiempo, nivel e identificador de petición; no deben registrarse datos sensibles; las reglas de anonimización figuran en la [especificación de seguridad y privacidad](./security-and-privacy-specification.md).
3. Cada servicio crítico debe definir SLI y SLO, e indicar el criterio de cálculo y la ventana de medición.
4. Las reglas de alerta deben tener umbral, duración e responsable explícitos; no puede publicarse una alerta sin instrucciones de tratamiento.
5. Una vez activada una alerta, debe poder vincularse a la clasificación y al proceso de tratamiento de la [especificación de respuesta a incidentes](./incident-response-specification.md).
6. El criterio de las métricas debe unificarse con la [especificación de métricas de calidad](./quality-metrics-specification.md); no debe haber métricas con el mismo nombre y distinto significado.

## 2. Los tres pilares y sus campos

| Pilar | Campos obligatorios | Requisito | Clave de correlación |
| --- | --- | --- | --- |
| Registros | Marca de tiempo, nivel, identificador de petición, mensaje, contexto | Salida estructurada; el nivel solo puede ser DEBUG/INFO/WARN/ERROR | `trace_id` |
| Métricas | Nombre de la métrica, etiquetas, valor, momento de recogida | Criterio y valor objetivo explícitos | `service` |
| Trazas | Identificador de traza, identificador de span, span padre, duración, estado | Las llamadas entre servicios deben poder encadenarse | `trace_id` |

## 3. Plantilla de campos de registro

```markdown
| Campo | Tipo | Obligatorio | Descripción | Ejemplo |
| --- | --- | --- | --- | --- |
| timestamp | ISO 8601 | Sí | Hora UTC, con zona horaria | 2026-11-18T10:00:00Z |
| level | Enumeración | Sí | DEBUG / INFO / WARN / ERROR | ERROR |
| trace_id | Cadena | Sí | Identificador único de toda la traza | 4bf92f3577b34da6 |
| service | Cadena | Sí | Nombre del servicio | lint-api |
| message | Cadena | Sí | Descripción breve sin datos sensibles | rule load failed |
| context | Objeto | No | Campos de contexto que permiten localizar el problema | {"rule":"spacing"} |
```

## 4. Plantilla de definición de SLI/SLO

```markdown
# Definición de SLO: {{服务名}}

Versión: {{v1.0}} ｜ Responsable: {{姓名}} ｜ Periodicidad de revisión: {{每季度}}

## Alcance del servicio
- Responsabilidad del servicio: {{一句话}}
- Servicios de los que depende: {{上游 / 下游}}
- Operaciones críticas del usuario: {{列出 2–5 项}}

## Definición de SLI
| SLI | Definición | Criterio de cálculo | Fuente de datos |
| --- | --- | --- | --- |
| Disponibilidad | Peticiones exitosas / peticiones totales | Se considera exitosa una respuesta con código HTTP <500 | {{监控面板}} |
| Latencia | Distribución de la duración de las peticiones | Valor del percentil P95 | {{监控面板}} |
| Tasa de error | Peticiones fallidas / peticiones totales | Recuento de 5xx | {{监控面板}} |

## Objetivos de SLO
| SLI | Valor objetivo | Ventana de medición | Valor actual | Estado |
| --- | --- | --- | --- | --- |
| Disponibilidad | ≥99,9% | 30 días móviles | {{值}} | {{达标 / 未达标}} |
| Latencia P95 | <300ms | 7 días móviles | {{值}} | {{达标 / 未达标}} |
| Tasa de error | <0,1% | 24 horas móviles | {{值}} | {{达标 / 未达标}} |

## Presupuesto de error
- Forma de cálculo: {{1 - SLO 目标值，按统计窗口换算}}
- Alertas de consumo: {{消耗达 50% / 75% / 90% 时分别通知}}
- Política de agotamiento: {{冻结非关键发布，优先修复稳定性}}
```

## 5. Plantilla de regla de alerta

```markdown
### ALERT-{{三位序号}}：{{告警名称}}

- SLI asociado: {{可用性 / 延迟 / 错误率}}
- Expresión: {{可执行的查询表达式}}
- Umbral: {{数值 + 单位}}
- Duración: {{N 分钟}}
- Nivel de gravedad: {{P0 / P1 / P2}}
- Responsable: {{姓名 / 值班组}}
- Ejemplo de activación: {{给出一个会触发的样例数据}}
- Condición de silencio: {{何时允许静默，须有到期时间}}

Instrucciones de tratamiento:
1. {{第一步：确认现象的数据源与命令}}
2. {{第二步：常见原因与对应处理}}
3. {{第三步：升级条件与升级对象}}
- Nivel de incidente asociado: {{见事故响应规范的分级表}}
```

## 6. Definición de campos

| Campo | Obligatorio | Tipo | Puntos clave de cumplimentación | Ejemplo |
| --- | --- | --- | --- | --- |
| Definición de SLI | Sí | Texto | Debe ser una proporción o un percentil calculable | Peticiones exitosas / peticiones totales |
| Criterio de cálculo | Sí | Texto | Indicar con claridad las condiciones de inclusión y exclusión | Excluir las peticiones de comprobación de estado |
| Valor objetivo de SLO | Sí | Umbral | Valor + unidad + porcentaje | `≥99,9%` |
| Ventana de medición | Sí | Duración | Ventana móvil; se prohíben formulaciones vagas como «mes natural» | `30 días móviles` |
| Presupuesto de error | Sí | Valor numérico | Se deriva del objetivo de SLO | `月允许 43 分钟不可用` |
| Expresión de alerta | Sí | Consulta | Debe poder pegarse y ejecutarse directamente | `rate(http_5xx[5m]) > 0.01` |
| Duración | Sí | Duración | Evita falsos positivos por fluctuaciones momentáneas | `5 分钟` |
| Instrucciones de tratamiento | Sí | Lista | Al menos 3 pasos, con condiciones de escalado | Véase la plantilla |
| Condición de silencio | Sí | Texto | Debe tener fecha de caducidad | `发布窗口内，最长 30 分钟` |

## 7. Instrucciones de cumplimentación

1. **Selección de SLI**: elegir de 2 a 5 dimensiones perceptibles por el usuario; no se sustituyen los SLI de usuario por métricas de recursos internos como CPU o memoria.
2. **Unificación del criterio**: una métrica con el mismo nombre debe usar el mismo criterio de cálculo en los registros, los paneles de monitorización y las expresiones de alerta.
3. **Fijación de objetivos**: los objetivos de SLO deberían basarse en los valores medidos actuales y en la tolerancia del negocio; se prohíbe aplicar sin más «cuatro nueves» sin justificación.
4. **Presupuesto de error**: deben indicarse el resultado de la conversión y las acciones escalonadas de consumo; cuando el presupuesto se agote, se congelan las publicaciones no críticas.
5. **Alertas ejecutables**: cada alerta debe responder a tres preguntas: «qué vigilar, cómo investigar, cuándo escalar»; si falta una, no puede publicarse.
6. **Gestión de la fatiga de alertas**: las alertas que durante 30 días consecutivos no hayan generado un tratamiento efectivo deberían rebajarse de nivel o eliminarse, indicando el motivo.
7. **Anonimización**: si en los campos de contexto de los registros pueden aparecer claves, tokens o datos personales, deben anonimizarse antes de la salida.

Errores frecuentes:

| Redacción errónea | Problema | Corrección |
| --- | --- | --- |
| Usar el uso de CPU como SLI | No es perceptible por el usuario | Emplear disponibilidad, latencia y tasa de error |
| Una alerta que solo dice «servicio anómalo» | Sin umbral ni instrucciones | Añadir expresión, umbral y pasos de tratamiento |
| Registros que imprimen la cabecera completa de la petición | Riesgo de fuga de datos privados y claves | Salida por lista blanca de los campos necesarios |
| Alerta sin fecha de caducidad del silencio | Un silencio prolongado provoca omisiones | Fijar una duración máxima de silencio |
| SLO sin ventana de medición | El objetivo no es verificable | Añadir la ventana móvil |

## 8. Ejemplo completo

```markdown
# Definición de SLO: lint-api

Versión: v1.0 ｜ Responsable: Wang Wu ｜ Periodicidad de revisión: cada trimestre

## Definición de SLI
| SLI | Definición | Criterio de cálculo | Fuente de datos |
| --- | --- | --- | --- |
| Disponibilidad | Peticiones exitosas / peticiones totales | Código de estado <500, excluyendo comprobaciones de estado | Grafana lint-overview |
| Latencia | Duración P95 de las peticiones de comprobación | Solo se cuenta la ruta /check | Grafana lint-overview |

## Objetivos de SLO
| SLI | Valor objetivo | Ventana de medición | Valor actual | Estado |
| --- | --- | --- | --- | --- |
| Disponibilidad | ≥99,9% | 30 días móviles | 99,94% | alcanzado |
| Latencia P95 | <300ms | 7 días móviles | 268ms | alcanzado |

## Presupuesto de error
- Forma de cálculo: 0,1% × 30 días = 43 minutos/mes
- Alertas de consumo: al 50% se notifica al responsable, al 75% al grupo de guardia, al 90% se congelan las publicaciones no críticas
- Política de agotamiento: se suspenden las publicaciones de funcionalidades y solo se permiten correcciones de estabilidad

### ALERT-001: tasa de error 5xx por encima del umbral
- SLI asociado: disponibilidad
- Expresión: `rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])`
- Umbral: >0.01
- Duración: 5 minutos
- Nivel de gravedad: P1
- Responsable: Wang Wu
- Instrucciones de tratamiento:
  1. Abrir Grafana lint-overview y confirmar el servicio de origen del error
  2. Consultar los registros ERROR y encadenar la traza de llamadas por trace_id; la causa habitual es el fallo de carga de un plugin de reglas
  3. Si no se localiza en 10 minutos, escalar a Li Si y entrar en el proceso de incidente P1
```

## Archivos relacionados

- Criterio de métricas y definición de medidas: [especificación de métricas de calidad](./quality-metrics-specification.md)
- Proceso de tratamiento tras una alerta: [especificación de respuesta a incidentes](./incident-response-specification.md)
- Comprobación de estado del despliegue: [especificación de despliegue y reversión](./deployment-and-rollback-specification.md)
- Anonimización de registros y protección de la privacidad: [especificación de seguridad y privacidad](./security-and-privacy-specification.md)
- Entradas habituales de resolución de problemas: [especificación de resolución de problemas](./troubleshooting-specification.md)
