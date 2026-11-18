# Especificación de respuesta a incidentes

> Problema que resuelve este archivo: define la plantilla de informe de incidentes, el registro de la línea temporal, las plantillas de comunicación y los campos de la retrospectiva, para garantizar que las fallas sean controlables, la información esté sincronizada y la experiencia pueda consolidarse.

## 1. Artículos de la especificación

1. Clasificación de incidentes: P0, la funcionalidad central no está disponible o hay corrupción de datos; P1, una función importante está gravemente afectada y afecta a la mayoría de los usuarios; P2, problema localizado de impacto limitado.
2. Proceso de respuesta: detección → clasificación → contención → localización → corrección → anuncio; la contención tiene prioridad sobre la localización.
3. Todo incidente P0/P1 debe someterse a retrospectiva, registrando la línea temporal, la causa raíz, el impacto, el tratamiento y las acciones de mejora.
4. Las acciones de mejora deben incorporarse a la [especificación de hoja de ruta](./roadmap-specification.md) para su seguimiento hasta el cierre.
5. La retrospectiva se centra en la mejora del sistema y no persigue responsabilidades individuales.
6. Filtración de claves: rotación inmediata → limpieza del historial → anuncio; no debe limitarse a un commit de eliminación (véase la [especificación de seguridad y privacidad](./security-and-privacy-specification.md)).
7. Push accidental de archivos grandes: migración a LFS o reescritura del historial (véase la [especificación de push y publicación](./push-and-release-specification.md)).

## 2. Plantilla de informe de incidentes

```markdown
# Informe de incidentes: {{INC-YYYYMMDD-NN}}

- Nivel del incidente: {{P0 / P1 / P2}}
- Momento de detección: {{YYYY-MM-DD HH:MM}}
- Momento de recuperación: {{YYYY-MM-DD HH:MM}}
- Duración: {{N 分钟}}
- Responsable de la coordinación: {{姓名}}
- Estado actual: {{处理中 / 已恢复 / 已复盘}}

## Alcance del impacto
| Dimensión | Descripción |
| --- | --- |
| Funciones afectadas | {{具体功能}} |
| Proporción de usuarios afectados | {{估算值与依据}} |
| Impacto en datos | {{无 / 描述}} |
| Impacto en el negocio | {{可量化的损失或阻塞}} |

## Línea temporal
| Hora | Evento | Fuente | Operador |
| --- | --- | --- | --- |
| {{HH:MM}} | Activación de la alerta | {{监控面板}} | {{姓名}} |
| {{HH:MM}} | Clasificación como P1 | {{判断依据}} | {{姓名}} |
| {{HH:MM}} | Ejecución de la reversión | {{命令 / 平台}} | {{姓名}} |
| {{HH:MM}} | Recuperación del servicio | {{验证方式}} | {{姓名}} |

## Causa raíz
- Causa directa: {{触发故障的具体事件}}
- Causa fundamental: {{为何未被预防或及时检测}}
- Factores de amplificación: {{扩大影响的因素}}

## Tratamiento y verificación
1. {{止血措施}}
2. {{修复措施}}
3. {{验证方式与结果}}

## Acciones de mejora
| Código | Acción | Responsable | Fecha límite | Método de verificación | Estado |
| --- | --- | --- | --- | --- | --- |
| {{A-NN}} | {{具体动作}} | {{姓名}} | {{YYYY-MM-DD}} | {{可判定阈值}} | {{待开始}} |
```

## 3. Plantillas de comunicación

```markdown
## Aviso de incidente (primero)

- Hora: {{YYYY-MM-DD HH:MM}}
- Nivel: {{P0 / P1 / P2}}
- Síntoma: {{用户可感知的现象，不写内部细节}}
- Impacto: {{受影响范围}}
- Medidas en curso: {{正在做什么}}
- Próxima actualización: {{HH:MM}}

## Aviso de incidente (recuperación)

- Momento de recuperación: {{HH:MM}}
- Confirmación de recuperación: {{验证方式与结果}}
- Impacto residual: {{无 / 描述}}
- Continuidad: {{复盘安排}}
```

## 4. Definición de campos

| Campo | Obligatorio | Tipo | Puntos de cumplimentación | Ejemplo |
| --- | --- | --- | --- | --- |
| Código del incidente | Sí | `INC-YYYYMMDD-NN` | Número secuencial del día, consecutivo y sin reutilización | `INC-20261118-01` |
| Nivel del incidente | Sí | Enumeración | P0 / P1 / P2 | `P1` |
| Duración | Sí | Duración | Minutos entre la detección y la recuperación | `42 minutos` |
| Responsable de la coordinación | Sí | Texto | Único; responsable de las decisiones y de la sincronización | `Li Si` |
| Proporción de usuarios afectados | Sí | Texto | Debe indicarse la base de la estimación | `Aproximadamente 8 %, según el recuento de registros de error` |
| Línea temporal | Sí | Tabla | Cada hito incluye hora y fuente | Véase la plantilla |
| Causa fundamental | Sí | Texto | Diferenciar la causa directa de la causa fundamental | `Falta de simulacros de reversión` |
| Acciones de mejora. Método de verificación | Sí | Texto | Verificable, con umbral | `La próxima simulación de reversión en <5 minutos` |
| Próxima actualización | Sí | Hora | Obligatorio durante el tratamiento; se prohíbe «actualización en cualquier momento» | `18:30` |

## 5. Instrucciones de cumplimentación

1. **Clasificación**: debe clasificarse según el alcance y la gravedad del impacto; en caso de duda debe clasificarse por lo alto, ajustando después y registrando el motivo.
2. **Prioridad de la contención**: primero debe restablecerse el servicio (reversión, degradación, limitación de tráfico) y después localizar la causa raíz; la localización no debe retrasar la contención.
3. **Línea temporal**: debe registrarse en orden cronológico, con fuentes consultables (identificador de alerta, comando, fragmento de registro); se prohíbe completarla después de memoria.
4. **Causa raíz**: la causa directa es el evento desencadenante y la causa fundamental es el defecto del sistema; ambas deben cumplimentarse.
5. **Comunicación**: el primer aviso debe indicar la próxima actualización; el aviso de recuperación debe explicar el método de verificación y el impacto residual.
6. **Acciones de mejora**: como máximo tres, incorporadas a la hoja de ruta para su seguimiento; ninguna acción sin responsable debe entrar en el informe.
7. **Retrospectiva**: debe centrarse en la mejora del sistema y de los procesos, sin evaluar a personas; no deben perseguirse responsabilidades ni escribirse expresiones del tipo «alguien se descuidó».
8. **Incidentes especiales**: la filtración de claves se trata según H12; el push accidental de archivos grandes se trata mediante migración a LFS; ambos deben dejar constancia por separado.

Errores frecuentes:

| Redacción incorrecta | Problema | Forma de corrección |
| --- | --- | --- |
| Localizar la causa raíz antes de contener | Prolonga la duración de la falla | Revertir primero para restablecer |
| Completar la línea temporal después | Los hechos no son fiables | Registrar en el momento durante el tratamiento |
| Causa raíz «alguien se descuidó» | Culpa a la persona y no aporta mejora | Indagar hasta el nivel de proceso o herramienta |
| Aviso con «corrección lo antes posible» | Sin próxima actualización | Indicar una hora concreta |
| Acción de mejora sin método de verificación | Cierre no verificable | Añadir umbral y momento de comprobación |

## 6. Ejemplo completo

```markdown
# Informe de incidentes: INC-20261118-01

- Nivel del incidente: P1
- Momento de detección: 2026-11-18 10:12
- Momento de recuperación: 2026-11-18 10:54
- Duración: 42 minutos
- Responsable de la coordinación: Li Si
- Estado actual: Retrospectiva realizada

## Alcance del impacto
| Dimensión | Descripción |
| --- | --- |
| Funciones afectadas | La interfaz de comprobación de reglas devuelve 5xx |
| Proporción de usuarios afectados | Aproximadamente 8 %, según el recuento de registros 5xx |
| Impacto en datos | Ninguno |
| Impacto en el negocio | Imposibilidad de enviar tareas de comprobación durante 42 minutos |

## Causa raíz
- Causa directa: la ruta de carga del complemento de reglas fue sobrescrita por la nueva configuración, lo que provocó un fallo de arranque.
- Causa fundamental: el cambio de configuración no se incorporó a la verificación previa a la publicación.

## Acciones de mejora
| Código | Acción | Responsable | Fecha límite | Método de verificación | Estado |
| --- | --- | --- | --- | --- | --- |
| A-01 | Incorporar los cambios de configuración a la lista de verificación previa a la publicación | Wang Wu | 2026-11-25 | Los próximos 5 cambios incluyen registro de comprobación | Pendiente |
```

## Archivos relacionados

- Origen de alertas y guía de tratamiento: [especificación de observabilidad](./observability-specification.md)
- Operaciones de reversión: [especificación de despliegue y reversión](./deployment-and-rollback-specification.md)
- Tratamiento de claves e información sensible: [especificación de seguridad y privacidad](./security-and-privacy-specification.md)
- Archivos grandes y reescritura del historial: [especificación de push y publicación](./push-and-release-specification.md)
- Seguimiento de acciones de mejora: [especificación de hoja de ruta](./roadmap-specification.md)
- Retrospectiva de mejora de procesos: [especificación de retrospectiva de iteración](./iteration-retrospective-specification.md)
- Criterios de determinación de alertas: [especificación de métricas de calidad](./quality-metrics-specification.md)
