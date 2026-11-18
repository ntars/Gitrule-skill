# Formato del informe de revisión

> Problema que resuelve este archivo: define el formato único de entrega del informe de revisión, los requisitos de sus campos y los ejemplos de cumplimentación, para garantizar que el informe pueda ser ejecutado directamente por otro agente.

El informe es el único entregable de la fase de revisión. Cada problema debe reunir a la vez evidencia, responsable y acción; ninguna conclusión que no pueda ejecutarse debe incorporarse al informe.

## 1. Estructura del informe

````markdown
# Informe de revisión del push · {{仓库名}}

Conclusión: {{结论}}
Modo: {{模式}}
Repositorio: {{仓库名}} · {{可见性}} · {{许可证}} · Rama por defecto {{默认分支}}

## I. Estado de las puertas
| Puerta | Estado | Elementos pendientes |
| --- | --- | --- |
| A Seguridad | {{门禁状态}} | {{未决项}} |
| B Calidad | {{门禁状态}} | {{未决项}} |
| C Página principal | {{门禁状态}} | {{未决项}} |

## II. Lista de problemas
| Nivel | Dimensión | Problema | Evidencia (ruta:línea / salida de comando) | Agente responsable | Acción |
| --- | --- | --- | --- | --- | --- |
| {{等级}} | {{维度}} | {{问题}} | {{证据}} | {{责任agent}} | {{动作}} |

## III. Estado de la matriz documental
| Archivo | Estado | Elementos ausentes / pendientes de cambio |
| --- | --- | --- |
| {{文件路径}} | {{状态}} | {{待改项}} |

## IV. Lista de ejecución del push
- [ ] {{推送规则}}

## V. Justificación de la liberación
{{放行说明}}
````

## 2. Definición de campos

| Campo | Obligatorio | Tipo | Puntos clave de cumplimentación | Ejemplo |
| --- | --- | --- | --- | --- |
| Nombre del repositorio | Sí | Texto | Idéntico carácter a carácter al nombre del repositorio en GitHub | `markdown-lint-cli` |
| Conclusión | Sí | Enumeración | Solo `ALLOW PUSH` o `BLOCK PUSH`; si quedan P0 sin resolver debe ser esta última | `BLOCK PUSH` |
| Modo | Sí | Enumeración | En repositorios privados de scripts temporales puede escribirse «revisión simplificada»; en el resto, «revisión completa» | `完整审核` |
| Visibilidad | Sí | Enumeración | `private` / `public`; antes de publicar debe revisarse la licencia | `private` |
| Licencia | Sí | Identificador SPDX | Si no hay licencia se escribe `NONE` y en ese caso la conclusión debe ser `BLOCK PUSH` | `MIT` |
| Rama por defecto | Sí | Texto | Se escribe el nombre real de la rama, no un `main` supuesto | `main` |
| Estado de la puerta | Sí | Enumeración ×3 | Una fila por cada puerta A/B/C; en caso de `SKIP` debe indicarse el motivo en «elementos pendientes» | `FAIL` |
| Elementos pendientes | Obligatorio condicional | Texto | Obligatorio cuando el estado es `FAIL` o `SKIP`; enumera el motivo de bloqueo o de omisión | `D1 检出 .env` |
| Nivel | Sí | Enumeración | `P0` bloquea / `P1` corregir o registrar antes del push / `P2` recomendación | `P0` |
| Dimensión | Sí | `D1`–`D14` | Los códigos se detallan en la [matriz de dimensiones de revisión](./review-dimension-matrix.md) | `D1` |
| Problema | Sí | Texto | Una frase que expone un hecho; no se escriben suposiciones ni formulaciones emocionales | `根目录存在 .env` |
| Evidencia | Sí | Ruta:línea o salida de comando | Debe poder revisarse; si no es posible obtenerla se escribe `SKIP + 原因` | `.env:3` |
| Agente responsable | Sí | Nombre del agente | Se indica el rol ejecutor concreto, no «personal implicado» | `security-auditor` |
| Acción | Sí | Texto | Operación que puede ejecutarse directamente, con el archivo de destino | `删除 .env、轮换密钥并清理历史` |
| Ruta del archivo | Sí | Texto | Se enumeran uno por uno según la lista de la [matriz de documentación](./document-matrix.md) | `SECURITY.md` |
| Estado de la matriz documental | Sí | Tabla fila por fila | Se marca cada archivo como presente, ausente o pendiente de cambio | `SECURITY.md 缺失` |
| Lista de ejecución del push | Sí | Lista de casillas | Se despliega punto por punto según las reglas de la [especificación de push y publicación](./push-and-release-specification.md) | `- [ ] 确认 .gitignore 生效` |
| Explicación de liberación | Sí | Texto | En caso de bloqueo, se indica el motivo y las condiciones para levantarlo; en caso de liberación, las reglas absolutas ya cumplidas | `P0 清零后可复核` |

## 3. Instrucciones de cumplimentación

1. **La conclusión es prioritaria**: primero se determina el número de P0 y después se redacta la conclusión. Si queda algún P0 sin resolver no puede emitirse `ALLOW PUSH`.
2. **Evidencia obligatoria**: cada problema debe aportar `ruta:línea` o una salida de comando que pueda copiarse. Las conclusiones sin evidencia se marcan como `SKIP` con el motivo indicado; no puede escribirse `PASS`.
3. **Responsabilidad por rol**: el agente responsable utiliza los nombres de rol de la [matriz de dimensiones de revisión](./review-dimension-matrix.md); cada problema corresponde a un único responsable.
4. **Acciones ejecutables**: la acción debe indicar el archivo de destino y el tipo de operación; «tratar más adelante» o «ajustar por cuenta propia» se consideran inválidas.
5. **Coherencia de las puertas**: las tres filas de estado A/B/C se corresponden con la lista de problemas; si cualquiera de las puertas está en `FAIL`, la conclusión debe ser `BLOCK PUSH`.
6. **Matriz documental punto por punto**: se enumeran los archivos uno por uno según la lista; no puede escribirse solo «la documentación está básicamente completa».
7. **Despliegue de la lista**: la lista de ejecución del push debe desplegar las reglas punto por punto; no puede sustituirse por «ejecutar según la especificación».

Errores frecuentes:

| Redacción errónea | Problema | Corrección |
| --- | --- | --- |
| Campo de evidencia con «parece que hay un problema» | Sin ruta ni salida, no verificable | Añadir `ruta del archivo:número de línea` o la salida del comando |
| P0 sin resolver y aun así `ALLOW PUSH` | Infringe las reglas absolutas | Cambiar a `BLOCK PUSH` e indicar las condiciones para levantarlo |
| Elementos que no pueden comprobarse marcados como `PASS` | Se inventan resultados | Escribir `SKIP` e indicar el motivo en los elementos pendientes |
| Responsable escrito como «personal implicado» | Sin sujeto responsable | Escribir el nombre concreto del agente |
| Acción escrita como «tratar más adelante» | No ejecutable | Indicar el archivo de destino y la operación concreta |
| Rama por defecto escrita como `main` sin verificar | No coincide con la realidad | Tomar como referencia la salida de `git branch` |

## 4. Ejemplo completo

A continuación se muestra un ejemplo completo de cumplimentación de `BLOCK PUSH`:

````markdown
# Informe de revisión del push · markdown-lint-cli

Conclusión: BLOCK PUSH
Modo: revisión completa
Repositorio: markdown-lint-cli · private · NONE · Rama por defecto main

## I. Estado de las puertas
| Puerta | Estado | Elementos pendientes |
| --- | --- | --- |
| A Seguridad | FAIL | D1 detecta .env, D2 sin LICENSE |
| B Calidad | SKIP | El repositorio no tiene las dependencias instaladas; no puede ejecutarse la compilación ni las pruebas |
| C Página principal | FAIL | Al README le falta la sección de instalación y el ejemplo mínimo |

## II. Lista de problemas
| Nivel | Dimensión | Problema | Evidencia (ruta:línea / salida de comando) | Agente responsable | Acción |
| --- | --- | --- | --- | --- | --- |
| P0 | D1 | Existe un .env en el directorio raíz | `.env:3` contiene DATABASE_URL | security-auditor | Eliminar .env, rotar las credenciales de base de datos y depurar el historial |
| P0 | D2 | No hay archivo de licencia | La salida de `ls LICENSE` es `No such file or directory` | license-checker | Generar LICENSE una vez que el propietario del repositorio confirme la licencia |
| P1 | D13 | Al README le falta la sección de instalación | `README.md:1-28` no contiene el título «Instalación» | readme-writer | Añadir la instalación y el ejemplo mínimo según la plantilla estándar de README |

## III. Estado de la matriz documental
| Archivo | Estado | Elementos ausentes / pendientes de cambio |
| --- | --- | --- |
| README.md | Pendiente de cambio | Faltan la sección de instalación y el ejemplo mínimo |
| LICENSE | Ausente | Pendiente de que el propietario confirme el tipo de licencia |
| SECURITY.md | Ausente | Aún no se ha creado |

## IV. Lista de ejecución del push
- [ ] Confirmar que git status está limpio
- [ ] Ejecutar el escaneo completo de claves (incluidos los commits históricos)
- [ ] Superar localmente build, test y lint
- [ ] Matriz documental completa

## V. Justificación de la liberación
Motivo del bloqueo: existen 2 elementos P0 (fuga de credenciales y ausencia de licencia) y la puerta de calidad no puede determinarse porque las dependencias no están instaladas. Condiciones para levantarlo: completar la rotación de claves y la depuración del historial, determinar la licencia, volver a ejecutar las pruebas en un entorno compilable y revisar de nuevo tras dejar los P0 a cero.
````

En caso de `ALLOW PUSH`, la quinta sección puede redactarse así: «Se han cumplido todas las reglas absolutas, las tres puertas están en `PASS` y puede ejecutarse el push». Las demás secciones se cumplimentan según la situación real, sin omitir la evidencia ni la lista.

## 5. Orden de entrega

1. Contenido completo de la navegación de idiomas del README raíz.
2. Contenido completo del README de cada directorio de idioma ya terminado, enumerando uno por uno el código de idioma y la ruta del archivo.
3. Contenido del archivo NOTICE.
4. Explicación del esquema de LICENSE (si el usuario no ha especificado una licencia, se ofrecen solo los candidatos y sus diferencias, sin generarla directamente).
5. Resumen de los elementos pendientes de confirmación.
6. Informe de revisión (este informe).
7. Guía de push a GitHub.

## Archivos relacionados

- La determinación del estado de las puertas se trata en la [puerta de calidad](./quality-gate.md)
- Los códigos de dimensión de la lista de problemas se detallan en la [matriz de dimensiones de revisión](./review-dimension-matrix.md)
- El estado de la matriz documental se trata en la [matriz de documentación](./document-matrix.md)
- La lista de ejecución del push procede de la [especificación de push y publicación](./push-and-release-specification.md)
- La forma de asignación se trata en el [contrato de asignación de subagentes](./sub-agent-dispatch-contract.md)
