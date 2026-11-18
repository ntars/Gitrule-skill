# Especificación de pruebas

> Problema que resuelve este archivo: define los niveles de prueba, la plantilla y los campos del plan de pruebas y de los casos de prueba, el criterio de cobertura y el estándar de ejecución, garantizando que cada requisito sea verificable y que cada cambio pueda someterse a regresión.

## 1. Cláusulas de la especificación

1. Las pruebas se dividen en tres niveles: unitarias, de integración y de extremo a extremo; cada nivel debe indicar el objeto bajo prueba y el alcance no cubierto, para evitar solapamientos.
2. Cada requisito de nivel «obligatorio» debe tener al menos un caso de prueba correspondiente; la relación de trazabilidad se detalla en la [Especificación de la matriz de trazabilidad de requisitos](./requirements-traceability-matrix-specification.md).
3. La corrección de un defecto debe añadir primero el caso de regresión y después modificar el código; el caso de regresión debe reproducir el defecto original.
4. El umbral de cobertura se fija por proyecto y se incorpora a la CI; no debe quedar por debajo del umbral establecido (corresponde a la regla absoluta H9).
5. Las pruebas deben ser reproducibles y no depender de estado externo; las que dependen de servicios externos deben aislarse o simularse con mock.
6. La denominación de las pruebas debe expresar el comportamiento bajo prueba y el resultado esperado; las pruebas, el lint, el format y la comprobación de tipos deben ejecutarse automáticamente en la CI, y solo con todo en verde puede fusionarse (véase [Especificación de revisión de código](./code-review-specification.md)).

## 2. Niveles de prueba

| Nivel | Objeto bajo prueba | Debe cubrir | No cubre | Herramientas típicas |
| --- | --- | --- | --- | --- |
| Pruebas unitarias | Funciones, módulos de lógica pura | Lógica central, condiciones límite, ramas de excepción | Colaboración entre módulos, E/S externa | Runner propio del lenguaje |
| Pruebas de integración | Colaboración entre módulos | Cadenas de llamada clave, adaptadores, interacción con la persistencia | Flujo completo del usuario | Contenedor de pruebas / servidor mock |
| Pruebas de extremo a extremo | Escenarios de usuario completos | Rutas de uso principales, circuitos de negocio clave | Enumeración exhaustiva de ramas, pruebas de carga | Controlador de navegador / CLI |

## 3. Plantilla del plan de pruebas

```markdown
# Plan de pruebas: {{项目名称}} {{版本号}}

Versión: {{v1.0}} ｜ Alcance de requisitos correspondiente: {{REQ-001 ~ REQ-020}} ｜ Responsable: {{姓名}}

## Alcance de las pruebas
- Incluido: {{模块 / 需求编号列表}}
- Excluido: {{不在本期验证的范围及原因}}
- Criterios de éxito del inicio del proyecto asociados: {{G1 / G2}}

## Estrategia por niveles
| Nivel | Objeto bajo prueba | Objetivo de cobertura | Herramienta | Momento de ejecución |
| --- | --- | --- | --- | --- |
| Unitario | {{对象}} | {{覆盖率阈值}} | {{工具}} | en cada commit |
| Integración | {{对象}} | {{关键链路清单}} | {{工具}} | en cada fusión |
| Extremo a extremo | {{场景}} | {{主要路径清单}} | {{工具}} | en cada publicación |

## Entorno y datos
- Entorno: {{操作系统 / 运行时版本 / 依赖服务版本}}
- Datos de prueba: {{构造方式；禁止使用生产敏感数据}}
- Dependencias externas: {{需 mock 的服务及隔离方式}}

## Criterios de entrada y salida
- Entrada: {{进入测试的前置条件，如开发自测通过}}
- Salida: {{通过率 100%、无 P0/P1 缺陷、覆盖率达标}}
- Condiciones de pausa: {{阻塞性问题清单}}

## Riesgos y concesiones
- Alcance no probado y motivo: {{例如第三方付费接口以 mock 替代}}
- Riesgos conocidos: {{例如并发场景仅做 10 路验证}}
```

## 4. Plantilla del caso de prueba

```markdown
### TC-{{三位序号}}: {{用例标题}}

- Requisitos asociados: {{REQ-001}}
- Nivel: {{单元 / 集成 / 端到端}}
- Prioridad: {{P0 / P1 / P2}}
- Tipo: {{正常 / 边界 / 异常}}
- Condiciones previas: {{环境与数据准备}}
- Pasos y resultados esperados:
  | Paso | Acción | Resultado esperado |
  | --- | --- | --- |
  | 1 | {{操作}} | {{可判定的结果}} |
  | 2 | {{操作}} | {{可判定的结果}} |
- Limpieza: {{恢复环境的操作；无则写「无」}}
```

## 5. Definición de campos

### 5.1 Campos del plan de pruebas

| Campo | Obligatorio | Tipo | Puntos clave | Ejemplo |
| --- | --- | --- | --- | --- |
| Alcance de requisitos correspondiente | Sí | Lista | Usar el intervalo de números REQ | `REQ-001 ~ REQ-020` |
| Alcance excluido | Sí | Texto | Indicar el motivo de no probar | `interfaz de pago no probada: sin cuenta de pruebas` |
| Objetivo de cobertura | Sí | Umbral | La cobertura debe ser un porcentaje numérico | `cobertura de líneas ≥80%` |
| Momento de ejecución | Sí | Enumeración | Commit / fusión / publicación | `en cada fusión` |
| Datos de prueba | Sí | Texto | Declarar la forma de construcción; se prohíben datos sensibles reales | `generados con fixture` |
| Criterios de salida | Sí | Texto | Verificables, con umbral de gravedad de defectos | `ningún defecto P0/P1 sin cerrar` |

### 5.2 Campos del caso de prueba

| Campo | Obligatorio | Tipo | Puntos clave | Ejemplo |
| --- | --- | --- | --- | --- |
| Número | Sí | `TC-NNN` | Continuo, sin reutilización | `TC-007` |
| Requisitos asociados | Sí | Lista | Al menos un número REQ | `REQ-001` |
| Prioridad | Sí | Enumeración | P0 / P1 / P2 | `P0` |
| Tipo | Sí | Enumeración | Normal / Límite / Excepción | `límite` |
| Pasos y resultados esperados | Sí | Tabla | Cada paso debe tener un resultado verificable | Véase la plantilla |
| Limpieza | Sí | Texto | Si no hay limpieza se escribe «ninguna»; no puede quedar vacío | `ninguna` |

### 5.3 Criterios de cobertura

| Criterio | Definición | Nivel aplicable | Umbral recomendado |
| --- | --- | --- | --- |
| Cobertura de líneas | Sentencias ejecutadas / sentencias totales | Unitario | ≥80% |
| Cobertura de ramas | Ramas ejecutadas / ramas totales | Unitario | ≥70% |
| Cobertura de requisitos | Requisitos «obligatorios» con caso de prueba / total de requisitos «obligatorios» | Todos los niveles | 100% |
| Cobertura de rutas | Rutas principales verificadas / rutas principales identificadas | Extremo a extremo | 100% |

Aclaración: la cobertura es un medio para descubrir zonas no probadas, no un objetivo de calidad en sí mismo; una cobertura alta no sustituye la calidad de las aserciones, que deben verificar el comportamiento y no solo ejecutar el código.

## 6. Instrucciones de cumplimentación

1. **Requisitos asociados**: debe indicarse el número REQ; los casos que no puedan asociarse deben trasladarse al registro de pruebas exploratorias y no incluirse en el conjunto formal de casos.
2. **Resultado esperado**: debe ser verificable. «Devuelve el resultado correcto» no es válido; «devuelve el código de estado 200 y el campo `name` no está vacío» sí lo es.
3. **Distribución por tipos**: cada requisito de nivel «obligatorio» cuenta al menos con un caso normal y un caso límite o de excepción.
4. **Limpieza**: los casos que afectan a archivos, bases de datos o estado global deben incluir los pasos de limpieza; si no se escriben, el caso se considera incompleto.
5. **Casos de regresión**: la corrección de un defecto debe nombrarse con el número del defecto como prefijo, por ejemplo `TC-007-regression-142`.
6. **Aislamiento**: los casos no deben depender del orden de ejecución; los que comparten estado deben reconstruirlo en las condiciones previas.

Errores frecuentes:

| Escritura errónea | Problema | Corrección |
| --- | --- | --- |
| Escribir como esperado «la función es normal» | No verificable | Escribir el valor de retorno o el estado concreto |
| Caso sin requisito asociado | Se rompe la cadena de trazabilidad | Añadir el número REQ |
| Probar solo la ruta normal | Defectos de límite no detectados | Añadir casos de excepción y de límite |
| Caso que depende del resultado del anterior | No se puede ejecutar repetidamente | Reconstruir el estado en las condiciones previas |
| Probar con datos de producción | Riesgo de privacidad y cumplimiento | Usar fixtures |

## 7. Ejemplo completo

```markdown
# Plan de pruebas: markdown-lint-cli v1.0

Versión: v1.0 ｜ Alcance de requisitos correspondiente: REQ-001 ~ REQ-014 ｜ Responsable: 王五

## Alcance de las pruebas
- Incluido: motor de reglas, análisis de parámetros de la CLI, salida del informe (REQ-001 ~ REQ-014)
- Excluido: integración con el plugin del editor (aplazada a v1.1, sin requisito correspondiente)
- Criterios de éxito del inicio del proyecto asociados: G1, G2

## Estrategia por niveles
| Nivel | Objeto bajo prueba | Objetivo de cobertura | Herramienta | Momento de ejecución |
| --- | --- | --- | --- | --- |
| Unitario | Funciones de reglas | cobertura de líneas ≥85% | runner nativo del lenguaje | en cada commit |
| Integración | CLI → motor de reglas → informe | 3 cadenas clave | contenedor de pruebas | en cada fusión |
| Extremo a extremo | Comprobación por lotes en un repositorio real | 2 rutas principales | controlador de shell | en cada publicación |

### TC-001: detección de la falta de espacio entre chino e inglés
- Requisitos asociados: REQ-001
- Nivel: Unitario
- Prioridad: P0
- Tipo: Límite
- Condiciones previas: Cargar la regla `spacing`
- Pasos y resultados esperados:
  | Paso | Acción | Resultado esperado |
  | --- | --- | --- |
  | 1 | Introducir «使用Node.js开发» | Devuelve 1 coincidencia, línea 1 |
  | 2 | Introducir «使用 Node.js 开发» | Devuelve 0 coincidencias |
- Limpieza: ninguna
```

## Archivos relacionados

- Trazabilidad bidireccional entre requisitos y casos: [Especificación de la matriz de trazabilidad de requisitos](./requirements-traceability-matrix-specification.md)
- Criterios por niveles y definición de indicadores: [Especificación de métricas de calidad](./quality-metrics-specification.md)
- Puerta de entrada: [Puerta de calidad](./quality-gate.md)
- Dimensión de revisión D6: [Matriz de dimensiones de revisión](./review-dimension-matrix.md)
- Configuración de ejecución automática en la CI: [Especificación del flujo de trabajo de CI](./ci-workflow-specification.md)
- Ejecución local antes del commit: [Especificación de push y publicación](./push-and-release-specification.md)
