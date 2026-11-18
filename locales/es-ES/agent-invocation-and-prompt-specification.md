# Especificación de invocación de Agent y de prompts

> Problema que resuelve este archivo: define el contrato de reparto y la forma de redactar prompts cuando un Agent invoca el conjunto de especificaciones, con el fin de garantizar que la invocación sea verificable, no exceda sus atribuciones y no derive.

## 1. Principios de invocación

1. Responsabilidad única: una invocación completa una sola tarea; se prohíbe realizar otras tareas «de paso».
2. Separación de lectura y escritura: el subagente solo lee y analiza; la escritura de archivos y las operaciones de git las ejecuta de forma centralizada el controlador (véase [Contrato de reparto de subagentes](./sub-agent-dispatch-contract.md)).
3. Exigencia de evidencia: las conclusiones deben aportar evidencia (ruta + número de línea / salida de comando); sin evidencia se consideran inválidas.
4. Sin comunicación directa: los subagentes no se comunican entre sí; todo se agrega a través del controlador.

## 2. Estructura del prompt

El prompt de invocación debe contener cuatro elementos:

```text
TASK:    <一句话任务>
INPUT:   <必要上下文，只给所需部分>
OUTPUT:  <结构化输出格式，表格或 JSON，禁止散文>
FAIL:    <无法完成时的返回约定，不得瞎编>
```

## 3. Redacción del prompt

1. Emplear lenguaje escrito y oraciones imperativas, con información completa y sin depender de inferencias del contexto (véase [Especificación general de redacción](./general-writing-specification.md)).
2. Especificar el formato de salida y el retorno en caso de fallo, para evitar que el modelo improvise.
3. Al citar especificaciones, indicar la ruta del archivo (véase [Especificación de metadatos legibles por máquina](./machine-readable-metadata-specification.md)).
4. Usar un formato unificado para plantillas y marcadores de posición (véase [Recopilación de información y plantillas](./information-collection-and-templates.md)).

## 4. Reglas obligatorias

1. No debe exigirse al Agent que invente resultados de verificación; los elementos no verificables se marcan como SKIP + motivo.
2. No debe incluirse el proceso de razonamiento interno en los entregables (véase [Prácticas prohibidas](./prohibited-practices.md)).
3. El contenido relacionado con seguridad se trata conforme a la [Especificación de seguridad y privacidad](./security-and-privacy-specification.md).

## Archivos relacionados

- Contrato de reparto: [Contrato de reparto de subagentes](./sub-agent-dispatch-contract.md)
- Metadatos de máquina: [Especificación de metadatos legibles por máquina](./machine-readable-metadata-specification.md)
- Encapsulado de Skill: [Especificación de redacción de Skill](./skill-authoring-specification.md)
- Herramientas MCP: [Especificación de herramientas MCP](./mcp-tool-specification.md)
