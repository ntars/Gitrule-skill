# Especificación de cumplimiento del código abierto

> Problema que resuelve este archivo: define el alcance de recogida del cumplimiento del código abierto, los campos del inventario de dependencias, el método de recogida, la evaluación de compatibilidad de licencias, la anotación de modificaciones y las reglas de cita de materiales, para garantizar que las declaraciones sean completas y verificables.

## 1. Alcance de la recogida

Debe abarcar cuatro tipos de fuentes: dependencias directas, dependencias indirectas y transitivas, cadena de herramientas de compilación y desarrollo, y materiales y recursos (iconos, tipografías, imágenes, audio, conjuntos de datos y origen de algoritmos).

## 2. Campos del inventario de dependencias

| Campo | Requisito |
| --- | --- |
| Nombre del componente | Coincide con el repositorio oficial |
| Versión | Versión realmente fijada, no una expresión de rango |
| Forma de referencia | Dependencia directa o dependencia indirecta |
| Titular del copyright | Nombre completo del titular declarado oficialmente |
| Licencia | Identificador SPDX; si hay varias licencias debe indicarse la forma de combinación |
| Dirección oficial | URL completa del repositorio o de la página principal |
| Uso en este proyecto | Ubicación concreta de la llamada o funcionalidad |
| ¿Modificado? | Sí o no |
| Descripción de la modificación | Archivos modificados, contenido de la modificación y motivo; si no hay modificación se indica «ninguna» |
| Ubicación del texto de la licencia | Ruta dentro del proyecto o enlace al archivo |

La plantilla de tabla del inventario de dependencias se encuentra en [recogida de información y plantillas](./information-collection-and-templates.md).

## 3. Método de recogida

Según el stack tecnológico, se genera el árbol de dependencias con el comando correspondiente y después se completan uno por uno la licencia y la información de copyright: `npm ls --all`, `pip freeze`, `go mod graph`, `cargo tree`, `mvn dependency:tree`, `gradle dependencies`, `composer show --tree`. Para el escaneo de licencias pueden emplearse herramientas como `license-checker`, `pip-licenses` o `cargo-license`; el resultado del escaneo debe revisarse manualmente y la salida de la herramienta no puede tomarse directamente como conclusión final.

## 4. Compatibilidad de licencias

1. Debe determinarse la compatibilidad entre la licencia del proyecto y las licencias de cada dependencia, prestando especial atención al alcance de propagación de GPL, AGPL, LGPL y MPL.
2. En las dependencias con Apache-2.0 debe confirmarse que se cumplen los requisitos sobre el archivo NOTICE.
3. Las licencias de materiales (como las tipografías SIL OFL o la familia CC) deben verificarse por separado en cuanto a los requisitos de atribución y difusión.
4. Cuando no pueda determinarse la compatibilidad, se marca «【pendiente de confirmación: compatibilidad de licencias】» y se explica el motivo de la duda.
5. Cuando el proyecto adopte licencias por capas, debe juzgarse capa por capa: una dependencia usada en una capa concreta se evalúa según la licencia de esa capa, y la licencia principal no debe representar a todo el repositorio. La disposición y el proceso de confirmación figuran en la [Especificación de LICENSE](./license-specification.md).
6. Cuando una misma dependencia atraviese varias capas de licencia, indique su ámbito real de uso y resuelva según la capa aplicable más estricta.

## 5. Anotación de modificaciones de código ajeno

1. Conservar en la cabecera del archivo la declaración original de copyright y de licencia.
2. Indicar en NOTICE la ruta de los archivos modificados, un resumen del contenido de la modificación y la fecha de la modificación.
3. Explicarlo de forma sincronizada en la sección correspondiente del README.

## 6. Citas y materiales

1. Al citar documentación o fragmentos de código ajenos deben indicarse la dirección de origen, el autor y la licencia.
2. Las imágenes, los iconos y las tipografías deben registrar su origen y su licencia; si faltan datos se marca como pendiente de confirmación y no puede usarse directamente.
3. No deben utilizarse materiales de origen desconocido.

## Archivos relacionados

- La conversión del inventario de dependencias en NOTICE se trata en la [especificación de NOTICE](./notice-specification.md)
- La elección de licencia y los requisitos de texto completo se tratan en la [especificación de LICENSE](./license-specification.md)
- La veracidad de las dependencias y del copyright corresponde a las puertas G6–G9 y G13, véase la [puerta de calidad](./quality-gate.md)
