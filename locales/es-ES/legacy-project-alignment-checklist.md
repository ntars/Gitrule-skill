# Lista de verificación de alineación de proyectos existentes

> Problema que resuelve este archivo: al aplicar este conjunto de especificaciones a un proyecto ya existente, ofrece una lista de verificación que puede comprobarse punto por punto, con métodos de evaluación y criterios de superación, y abarca seis ámbitos: metadatos, nomenclatura de archivos, estructura de secciones, sincronización bilingüe, enlaces y push.

## 1. Ámbito de aplicación

Esta lista se utiliza en dos escenarios:

1. Primera incorporación de un repositorio ya existente a la gestión según este conjunto de especificaciones;
2. Tras actualizar el conjunto de especificaciones, verificación de regresión sobre repositorios ya alineados.

La lista se ejecuta en el orden «primero metadatos, después estructura y por último push». Si un grupo anterior no se supera, no se pasa al siguiente, evitando reescrituras masivas sobre una base errónea.

## 2. Elementos de comprobación

### 2.1 Metadatos (corresponde a la sección 5 de la [especificación de nomenclatura de proyectos](./project-naming-specification.md))

| Código | Elemento de comprobación | Método de evaluación | Criterio de superación |
| --- | --- | --- | --- |
| A1 | Nombre del repositorio conforme | Cotejar con la fórmula de nomenclatura y las reglas del conjunto de caracteres | Todo en minúsculas, kebab-case, de 2 a 25 caracteres, sin número de versión ni palabras informativas |
| A2 | Descripción en formato bilingüe combinado | Leer el área About del repositorio o `gh repo view --json description` | `idioma nacional \| inglés`, con un espacio a cada lado de la barra vertical |
| A3 | Longitud de la descripción | Contar caracteres, por separado en chino y en inglés | Cada uno no supera 120 caracteres y el total no supera 350 caracteres |
| A4 | Cantidad e idioma de los temas | `gh repo view --json repositoryTopics` | Exactamente 20, todos en inglés, en minúsculas y separados por guiones |
| A5 | Cobertura de los temas | Cotejar con las cinco categorías: lenguaje, dominio, formato, ecosistema y escenario | Hay cobertura en las cinco categorías y ningún tema es incompatible con el stack tecnológico |

Orden de actuación cuando se supera el límite: primero se comprime la versión en inglés y después la versión en chino; al comprimir, se eliminan primero los modificadores y las delimitaciones redundantes y luego se fusionan expresiones sinónimas.

### 2.2 Nomenclatura de archivos (corresponde a la [especificación multilingüe](./multilingual-specification.md))

| Código | Elemento de comprobación | Método de evaluación | Criterio de superación |
| --- | --- | --- | --- |
| B1 | Nomenclatura del README principal | Listar el directorio | En chino `README.md`, en inglés `README_EN.md` |
| B2 | Nomenclatura de los demás idiomas | Listar el directorio | `README_<CÓDIGO DE IDIOMA EN MAYÚSCULAS>.md`, por ejemplo `README_JA.md` |
| B3 | Coherencia de nomenclatura | Buscar los nombres antiguos en todo el repositorio | No quedan nomenclaturas antiguas del tipo `README.en.md` o `README.ja.md` |
| B4 | Sincronización de referencias | Buscar los nombres de archivo antiguos | Los enlaces de navegación, los ejemplos de árbol de directorios y las listas blancas de los scripts están actualizados |
| B5 | Enlaces de cambio de idioma | Abrir la primera línea de cada versión de idioma | Cada versión de idioma puede cambiar desde su primera línea a todas las demás |

El cambio de nombre de archivos debe realizarse con `git mv`, para preservar el historial del archivo. Los scripts del repositorio (comprobación previa, empaquetado, validación documental) suelen usar cadenas con los nombres de archivo como lista blanca; deben modificarse de forma sincronizada, ya que de lo contrario la validación fallará tras el push.

### 2.3 Estructura de secciones (corresponde a la [especificación de secciones del README](./readme-sections-specification.md))

| Código | Elemento de comprobación | Método de evaluación | Criterio de superación |
| --- | --- | --- | --- |
| C1 | Secciones completas | Extraer los títulos de segundo nivel y cotejarlos con la lista de 20 capítulos | Los 20 capítulos existen y no falta ninguno |
| C2 | Denominación de las secciones | Cotejar el texto de los títulos uno por uno | Coincide con la terminología de la especificación; no se emplean variantes como «aspectos clave» o «detalles de diseño y pequeños trucos» |
| C3 | Orden de las secciones | Cotejar según el orden de aparición | Coincide con el orden de la especificación |
| C4 | Secciones adicionales | Comprobar si existen secciones adicionales | El contenido adicional se coloca como «apéndice» después de los 20 capítulos, sin insertarse en el orden del cuerpo |
| C5 | Correspondencia entre versiones de idioma | Cotejar la cantidad y el orden de los títulos de segundo nivel en chino e inglés | Existe correspondencia uno a uno entre ambos idiomas |

Cuando en el cuerpo aparecen nombres de sección que no coinciden con la especificación, se unifican según la terminología de esta; si la sección contiene mucho contenido ya existente, se prioriza el cambio de nombre frente a la reescritura del texto.

### 2.4 Sincronización bilingüe (corresponde a la [especificación multilingüe](./multilingual-specification.md))

| Código | Elemento de comprobación | Método de evaluación | Criterio de superación |
| --- | --- | --- | --- |
| D1 | Número de versión coherente | Buscar la cadena de versión | Ambas versiones de idioma indican el mismo número de versión y estado |
| D2 | Cifras coherentes | Cotejar el número de funcionalidades, de pruebas y de plataformas | Un mismo indicador tiene el mismo valor en ambas versiones |
| D3 | Enlaces coherentes | Cotejar el conjunto de enlaces relativos | Ambas versiones apuntan al mismo conjunto de archivos |
| D4 | Terminología coherente | Muestrear términos técnicos | Un mismo concepto usa la misma traducción en ambas versiones |
| D5 | Estructura coherente | Cotejar la cantidad de tablas y listas | La cantidad de tablas y listas dentro de las secciones es la misma |

Cuando una versión modifica contenido fáctico, la otra debe actualizarse en el mismo commit; no se admite completar la traducción en commits posteriores.

### 2.5 Enlaces y contenido (corresponde a la [especificación general de redacción](./general-writing-specification.md))

| Código | Elemento de comprobación | Método de evaluación | Criterio de superación |
| --- | --- | --- | --- |
| E1 | Enlaces relativos accesibles | Resolverlos uno por uno y comprobar si el archivo existe | Número de enlaces rotos igual a 0 |
| E2 | Identificador de lenguaje en bloques de código | Buscar los delimitadores | Todos indican lenguaje; no hay delimitadores sin lenguaje |
| E3 | Número de columnas de las tablas | Cotejar la fila separadora y las filas de datos de cada tabla | El número de columnas es coherente |
| E4 | Expresiones prohibidas | Buscar coloquialismos, signos de exclamación, puntos suspensivos y emojis | Sin coincidencias; al citar un texto original debe ir entre comillas y con la fuente indicada |
| E5 | Datos no verificados | Buscar cifras de rendimiento | Cada cifra cuenta con entorno y método de prueba |
| E6 | Formulaciones de compromiso | Buscar términos como «garantizar», «permanente» o «definitivo» | Pueden mantenerse las delimitaciones técnicas; deben eliminarse las formulaciones de compromiso hacia el exterior |

### 2.6 Archivos comunitarios y push (corresponde a la [matriz de documentación](./document-matrix.md) y a la [especificación de push y publicación](./push-and-release-specification.md))

| Código | Elemento de comprobación | Método de evaluación | Criterio de superación |
| --- | --- | --- | --- |
| F1 | Archivos obligatorios completos | Listar el directorio | `LICENSE`, `NOTICE`, `CONTRIBUTING.md` y `SECURITY.md` están completos |
| F2 | Coherencia entre licencia y NOTICE | Cotejar la tabla de enrutamiento por niveles | La licencia por nivel de directorio coincide con lo declarado en NOTICE |
| F3 | Reglas de ignorados | Consultar `.gitignore` | Los artefactos de compilación, los directorios de dependencias, `.DS_Store` y `.workbuddy/` están ignorados |
| F4 | Mensajes de commit | Revisar `git log` | Cumplen `<type>(<scope>): <subject>` |
| F5 | Coherencia con el remoto | Cotejar el `HEAD` local con `origin/main` | Ambos coinciden y el árbol de trabajo está limpio |

## 3. Comprobaciones adicionales para repositorios multilingües

Cuando el repositorio tiene tres o más versiones de idioma, se añaden tres comprobaciones a las anteriores:

1. **Cotejo de títulos de sección por idioma**: los títulos de los 20 capítulos de cada idioma deben ser coherentes en significado con la referencia en chino o en inglés, y ningún idioma puede tener capítulos ausentes;
2. **Coherencia del número de filas de las tablas**: las listas de proyectos, las tablas de estado y las tablas de parámetros tienen el mismo número de filas en todas las versiones de idioma;
3. **Sincronización del glosario**: la tabla de correspondencia terminológica se sitúa en un archivo independiente compartido por ambos idiomas, y todas las versiones de idioma remiten a la misma.

## 4. Errores frecuentes y su tratamiento

| Error | Síntoma | Tratamiento |
| --- | --- | --- |
| Confundir números chinos al cambiar números de capítulo en lote | «十、» se identifica como «二十、» y el capítulo 10 se sobrescribe con el título del capítulo 20 | Pasar a un reemplazo uno a uno explícito «cadena antigua → cadena nueva» y escribir solo tras verificar cada coincidencia |
| Cambiar la ruta del enlace sin cambiar el texto mostrado | El enlace es pulsable, pero el cuerpo sigue indicando el nombre antiguo de la sección | Buscar el nombre antiguo de la sección en todo el texto y actualizar a la vez la ruta y el texto mostrado |
| Cambiar el nombre de un archivo sin sincronizar los scripts | La documentación local funciona, pero el script de validación falla tras el push | Buscar todas las cadenas con nombres de archivo del repositorio, incluidos scripts, configuración y ejemplos de documentación |
| Modificar solo un lado de la versión bilingüe | Ambas versiones difieren en los hechos | Tomar como referencia el estado real del repositorio, modificar primero la versión principal y después la otra en el mismo commit |
| Índice no sincronizado | El archivo nuevo no está en el índice y se considera huérfano | Tras añadir un archivo, actualizar de inmediato el recuento y la entrada del índice, y revisar la suma de recuentos por dominio |
| Descripción del repositorio incoherente con el cuerpo | En el área About figuran siete proyectos y en el cuerpo nueve | Actualizar la descripción tomando como referencia la lista del cuerpo e indicarlo en el mensaje de commit |

## 5. Plantilla de registro de aceptación

```text
仓库：{{仓库名}}
检查日期：{{日期}}
规范版本：{{版本或提交号}}

元数据：A1 {{通过/不通过}} A2 {{通过/不通过}} A3 {{通过/不通过}} A4 {{通过/不通过}} A5 {{通过/不通过}}
文件命名：B1 {{ }} B2 {{ }} B3 {{ }} B4 {{ }} B5 {{ }}
章节结构：C1 {{ }} C2 {{ }} C3 {{ }} C4 {{ }} C5 {{ }}
双语同步：D1 {{ }} D2 {{ }} D3 {{ }} D4 {{ }} D5 {{ }}
链接与内容：E1 {{ }} E2 {{ }} E3 {{ }} E4 {{ }} E5 {{ }} E6 {{ }}
社区与推送：F1 {{ }} F2 {{ }} F3 {{ }} F4 {{ }} F5 {{ }}

未通过项与处置：{{逐条列出}}
放行结论：{{通过 / 有条件通过 / 阻断}}
```

## 6. Definición de campos

| Campo | Significado | Valores |
| --- | --- | --- |
| Nombre del repositorio | Nombre completo del repositorio sometido a comprobación | `propietario/repositorio` |
| Versión de la especificación | Estado del conjunto de especificaciones en que se basa esta comprobación | Número de commit o de versión |
| Superado | El elemento cumple el criterio de superación | Booleano |
| Conclusión de liberación | Tratamiento del resultado de la comprobación | Superado / Superado con condiciones / Bloqueado |

## Archivos relacionados

- La nomenclatura del repositorio y los metadatos se tratan en la [especificación de nomenclatura de proyectos](./project-naming-specification.md)
- La lista de secciones se trata en la [especificación de secciones del README](./readme-sections-specification.md)
- Las reglas bilingües se tratan en la [especificación multilingüe](./multilingual-specification.md)
- La redacción y las expresiones prohibidas se tratan en la [especificación general de redacción](./general-writing-specification.md)
- Las acciones de push se tratan en la [especificación de push y publicación](./push-and-release-specification.md)
