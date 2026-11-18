# Contrato de asignación de subagentes

> Problema que resuelve este archivo: define los cuatro elementos que deben especificarse obligatoriamente al asignar tareas a los subagentes y las restricciones de colaboración, garantizando conclusiones estructuradas, verificables y sin desviación de reglas.

## 1. Los cuatro elementos de la asignación

Cada asignación debe especificar claramente los cuatro elementos:

```text
TASK:    <一句话任务>
INPUT:   <需要的文件/上下文，只给必要部分>
OUTPUT:  <结构化格式，表格或 JSON，禁止散文>
FAIL:    <做不了时返回什么，而不是瞎编>
```

## 2. Restricciones

- Un subagente realiza una sola cosa por vez; se prohíbe «de paso, escribe también el README».
- El subagente solo puede leer y solo puede producir propuestas; **la escritura de archivos y las operaciones de git las ejecuta de forma unificada el control principal**.
- Las conclusiones del subagente deben incluir evidencia (ruta del archivo + número de línea / salida de comando); las conclusiones sin evidencia se consideran inválidas.
- Los subagentes no se comunican directamente entre sí; todo se consolida a través del control principal para evitar desviaciones de reglas.

## Archivos relacionados

- Para los destinatarios de la asignación y las dimensiones, véase la [matriz de dimensiones de revisión](./review-dimension-matrix.md)
- Para la asignación de la redacción de documentación, véase la [matriz de documentación](./document-matrix.md)
- La asignación se produce en la Phase 2 y la Phase 4 del [proceso de ejecución](./execution-process.md)
