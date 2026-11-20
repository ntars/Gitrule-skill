# Especificación de LICENSE

> Problema que resuelve este archivo: define el marcado SPDX de la licencia del proyecto, los requisitos del texto completo de LICENSE, la ubicación de la línea de copyright, el mecanismo de detección de GitHub, la disposición de archivos en caso de licencias por capas y el proceso de confirmación, así como la regla de no escribir nada sin confirmación.

## 1. Reglas básicas

1. La licencia del proyecto debe indicarse expresamente en el README mediante el identificador SPDX y debe aportarse el archivo LICENSE correspondiente.
2. El archivo LICENSE debe contener el texto completo oficial en inglés de dicha licencia, sin suprimir ni modificar cláusulas. Reformular, reordenar los párrafos o recompaginar en Markdown hace fracasar la detección automática.
3. La línea de copyright se coloca en el encabezado del archivo o en el capítulo 19 del README; el formato se indica en [Especificación de secciones del README](./readme-sections-specification.md).

## 2. Mecanismo de detección de GitHub

GitHub determina la licencia de un repositorio con la herramienta de código abierto licensee. El resultado condiciona la insignia de la página del repositorio, el campo `license` de la API y que una búsqueda por la palabra clave `license` encuentre o no el repositorio. Las reglas son:

1. Solo se examinan dos ubicaciones: la raíz del proyecto y un directorio `LICENSES/` de primer nivel. Los archivos con el mismo nombre dentro de `locales/`, `docs/` u otros subdirectorios no participan.
2. En la raíz, los archivos se puntúan por su nombre y gana la puntuación más alta: `LICENSE` vale 1.00, `LICENSE.md` 0.95, `COPYING` 0.90, las formas con sufijo como `LICENSE-MIT` 0.70.
3. Dentro de un directorio `LICENSES/` de primer nivel, un nombre de archivo con formato de identificador SPDX y extensión `.txt`, `.md`, `.markdown` o `.html` vale 1.00; cualquier otro vale 0.00.
4. El contenido debe coincidir estrechamente con el texto completo oficial de la licencia. Un archivo que solo contenga una mención del tipo «este proyecto usa la licencia X» no será detectado, y el resultado que produjera sería un valor no estándar.
5. Cuando se detectan varias licencias distintas, el resultado a nivel de proyecto puede no devolver una licencia concreta, y la página del repositorio muestra `View license` u `Other`.
6. Las declaraciones en lenguaje natural del README no participan. Escribir «este proyecto tiene licencia MIT» no hace que se detecte como MIT.

Por lo tanto: **la declaración del README y el archivo LICENSE son dos mecanismos independientes y ambos son necesarios.** Además, cuando existen varios archivos de licencia en la raíz, cuál se reporta finalmente depende tanto de la puntuación del nombre como de la coincidencia del contenido, y no es predecible; en las mediciones, los repositorios con doble licencia reportaron solo una de las dos.

## 3. Disposición de archivos en caso de licencias por capas

Las licencias por capas significan que distintas partes de un repositorio se rigen por licencias distintas, por ejemplo código bajo MIT y documentación bajo CC BY 4.0. La disposición se decide en este orden:

| Opción | Qué va en la raíz | Resultado de la detección | Condición de uso |
| --- | --- | --- | --- |
| Capa única (predeterminada) | Un solo `LICENSE` | Detección estable de esa licencia | Todas las capas usan la misma licencia, o la diferencia no altera las obligaciones de los usuarios |
| Capas con explicación | `LICENSE` lleva la licencia principal, más un `LICENSING.md` | Detección estable de la licencia del `LICENSE` raíz | Se necesita estratificar y la insignia debe seguir siendo inequívoca |
| Capas con REUSE | `LICENSES/` de primer nivel contiene cada texto completo | Puede degradarse a un valor no estándar | Solo si la parte aguas abajo exige expresamente conformidad REUSE |

Contrapartidas:

1. No coloque varios archivos de licencia en la raíz. En las mediciones, cada repositorio con doble licencia reportó solo una de sus dos licencias; la otra quedó invisible en la página del repositorio y en la API, lo que equivale a declarar públicamente una sola licencia.
2. La disposición REUSE entra en conflicto con la claridad de la insignia: varias licencias en `LICENSES/` se leen como varias licencias, lo que compra un `reuse lint` en verde a cambio de un resultado de detección ambiguo. Ambos no pueden satisfacerse plenamente a la vez; el proyecto debe elegir.
3. Con la opción «capas con explicación», el nombre `LICENSING.md` no coincide con el patrón `LICENSE` ni con el patrón `COPYING`, por lo que no se confunde con un archivo de licencia y no afecta a la detección del `LICENSE` raíz.
4. Sea cual sea la disposición elegida, el capítulo 19 del README debe indicar la expresión SPDX (por ejemplo `MIT AND CC-BY-4.0`) y el ámbito de cada capa. Es el único lugar donde la información sobrevive a nivel de lectura humana.

## 4. Decisión de estratificación y proceso de confirmación

Las licencias por capas tienen alcance jurídico. Antes de redactar u optimizar, confirme ronda tras ronda; no invente nada.

1. No introduzca estratificación por iniciativa propia. Cuando el usuario no lo haya pedido expresamente, trate el proyecto como de capa única e indique en el informe: «Si se necesita estratificar, las opciones candidatas y sus diferencias son las siguientes».
2. Toda propuesta de estratificación debe exponer su fundamento: qué cubre realmente cada capa, las licencias candidatas y la diferencia de sus obligaciones, el efecto sobre los usuarios aguas abajo y cómo cambiaría el resultado de la detección.
3. Confirme al menos dos veces antes de escribir: primero la combinación (qué licencia para qué capa), después la disposición de archivos (qué licencia va en el archivo raíz y si se crea `LICENSES/`).
4. Confirme de nuevo antes de hacer push. Una vez generados los archivos, indique expresamente «Los archivos se han generado; revíselos y confírmelos usted mismo» y nunca confirme ni haga push en lugar del usuario.
5. Las opciones no confirmadas van solo a un informe o a un archivo temporal; no deben escribirse como `LICENSE`, `LICENSES/` ni `LICENSING.md`.
6. Cuando una parte no pueda atribuirse a ninguna capa, márquela como «[pendiente de confirmación: asignación de capa]» y enumere los archivos dudosos; no la clasifique por defecto.

## 5. Requisitos de la exención de responsabilidad

Los textos de licencia tienen eficacia jurídica. Las plantillas y herramientas solo aportan reglas de decisión y disposición de archivos, y no constituyen asesoramiento jurídico.

1. El capítulo 19 del README o el archivo `LICENSING.md` debe contener una exención de responsabilidad que indique que la elección de licencia la confirma el titular del proyecto.
2. La exención de responsabilidad debe coincidir con la de NOTICE; no debe existir en un lugar y faltar en el otro.
3. No afirme que «la revisión de cumplimiento ha concluido». Indique solo que «se ha comprobado conforme a las reglas la disposición de archivos y la completitud del marcado SPDX».
4. La eficacia jurídica de las licencias por capas sigue el texto completo de cada licencia. El texto descriptivo dentro del repositorio es solo un índice y no modifica las cláusulas.

## Archivos relacionados

- La ausencia de LICENSE bloquea el push; es la regla absoluta H2, véase [Reglas absolutas](./hard-rules.md)
- El juicio de compatibilidad de licencias de dependencias se indica en [Especificación de cumplimiento de código abierto](./open-source-compliance-specification.md)
- La declaración de terceros en archivo independiente se indica en [Especificación de NOTICE](./notice-specification.md)
- La exactitud de la licencia pertenece a las puertas G7/G8; véase [Puertas de calidad](./quality-gate.md)
