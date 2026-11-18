# Especificación de insignias

> Problema que resuelve este archivo: define la sintaxis de URL de las insignias (Badge) en el README, los parámetros de estilo, la codificación de colores, la selección de información, el orden de disposición y el control de cantidad, tomando Shields.io como implementación principal y ofreciendo ejemplos de formato directamente copiables y configuraciones de parámetros recomendadas.

Los parámetros descritos en este archivo se verificaron con la documentación oficial de Shields.io (páginas Static Badge y Logos, descripción del formato badge-maker); los datos de frecuencia de aparición provienen del muestreo estadístico de README de proyectos open source destacados realizado por este proyecto y se marcan como «medido».

## 1. Sintaxis básica

### 1.1 Estructura de URL de una insignia estática

Las insignias estáticas reciben parámetros a través de la ruta de la URL; la estructura estándar es la siguiente:

```text
https://img.shields.io/badge/<标签>-<消息>-<颜色>?style=<样式>&<其他查询参数>
```

Los tres segmentos de la ruta se separan con guiones `-`:

| Segmento | Nombre | ¿Obligatorio? | Descripción |
| --- | --- | --- | --- |
| 1.º segmento | Etiqueta (label) | No | Texto de la izquierda, indica el nombre del indicador |
| 2.º segmento | Mensaje (message) | Sí | Texto de la derecha, muestra el valor del indicador |
| 3.º segmento | Color (color) | Sí | Color de fondo de la derecha |

La forma de dos segmentos (se omite la etiqueta y solo quedan mensaje y color) también es válida:

```text
https://img.shields.io/badge/<消息>-<颜色>
```

### 1.2 Reglas de escape de caracteres

Los espacios y caracteres especiales de la ruta de la URL deben escaparse; las reglas son las siguientes:

| Carácter de entrada | Notación en la URL | Ejemplo |
| --- | --- | --- |
| Espacio | `_` o `%20` | `v0.1 prototype` → `v0.1%20prototype` |
| Guion bajo `_` | `__` (doble guion bajo) | `my_label` → `my__label` |
| Guion `-` | `--` (doble guion) | `dev-build` → `dev--build` |

El ejemplo de prototipo aportado por el usuario cumple esta sintaxis y puede usarse directamente:

```markdown
![Status](https://img.shields.io/badge/status-v0.1%20prototype-8957e5?style=flat-square)
```

Su significado es: etiqueta `status`, mensaje `v0.1 prototype` (el espacio con `%20`), color `8957e5` (violeta hexadecimal), estilo `flat-square`.

### 1.3 Formato de inserción en Markdown

```markdown
![versión](https://img.shields.io/badge/version-1.2.0-blue?style=flat-square)
```

Cuando se necesita un salto al hacer clic, se envuelve la imagen con un enlace:

```markdown
[![Licencia](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
```

## 2. Parámetro de estilo (style)

`style` determina el diseño visual global de la insignia; admite cinco valores y su valor predeterminado es `flat`.

| Valor | Características visuales | Casos de uso | Apariciones medidas (N=120) |
| --- | --- | --- | --- |
| `flat` | Ángulos rectos, plano, valor predeterminado de Shields.io | Opción general preferente, compatible con la mayoría de los temas | 32 |
| `flat-square` | Ángulos rectos, sin esquinas redondeadas, algo más compacto | Portadas que buscan orden y solidez | 60 |
| `for-the-badge` | Cuerpo grande en negrita, alto contraste | Elemento visual principal de la cabecera, insignias de énfasis | 65 |
| `social` | Esquinas redondeadas, bicolor izquierda-derecha, plano | Portadas de estilo social | 12 |
| `plastic` | Brillo con degradado, skeuomórfico | Estilo retro, hoy poco usado | 1 |

**Configuración recomendada**:

- Todas las insignias de un mismo README deben compartir el mismo `style`; se prohíbe mezclarlos. Es el primer requisito de coherencia visual.
- En proyectos generales se prefiere `flat` o `flat-square`; cuando se refuerza la portada de marca se usa `for-the-badge` de forma uniforme.
- En las mediciones, `for-the-badge` (65 apariciones) y `flat-square` (60) son los más populares; cualquiera de los dos sirve como elección predeterminada.

Ejemplos de formato:

```markdown
![build](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)
![build](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)
```

## 3. Parámetros de color (color / labelColor)

### 3.1 Tres notaciones de color

Según la descripción de badge-maker, tanto `color` (lado derecho) como `labelColor` (fondo del lado izquierdo) admiten las tres notaciones siguientes:

**Método uno: colores con nombre de Shields.io**

| Semántica | Colores con nombre |
| --- | --- |
| Éxito | `brightgreen`, `green`, `success` |
| Aviso | `yellow`, `yellowgreen`, `orange`, `important` |
| Alerta | `red`, `critical` |
| Información | `blue`, `informational` |
| Neutro | `grey` / `gray`, `lightgrey` / `lightgray`, `inactive` |

Nota: el valor predeterminado de `labelColor` es `grey` y el de `color` es `lightgrey` (la documentación señala además que `inactive` también es uno de los colores predeterminados); algunos colores con nombre difieren ligeramente de los homónimos de CSS; prevalece el resultado renderizado por Shields.io.

**Método dos: color hexadecimal**

Admite tres o seis dígitos hexadecimales y se puede omitir o conservar el prefijo `#`:

```text
?color=8957e5
?color=007fff
?color=%23007fff    ← al conservar # debe codificarse como %23
```

**Método tres: valor de color CSS**

Admite `rgb(...)`, `rgba(...)`, `hsl(...)`, `hsla(...)` y colores con nombre de CSS (como `aqua`, `fuchsia`, `lightslategray`); al usarlos debe aplicarse codificación de URL.

### 3.2 Mapa semántico de colores (configuración recomendada)

| Tipo de información | Color recomendado | Mensaje de ejemplo |
| --- | --- | --- |
| Compilación superada, pruebas superadas | `brightgreen` / `success` | `passing` |
| Compilación fallida | `red` / `critical` | `failing` |
| Versión estable | `blue` | `v1.2.0` |
| Prepublicación, prototipo | Violeta personalizado `8957e5` / `orange` | `v0.1 prototype` |
| Licencia | `blue` / `green` | `MIT` |
| Estado de la documentación | `yellowgreen` | `docs` |
| Obsoleto, sin mantenimiento | `red` / `inactive` | `deprecated` |

**Configuración recomendada**: el color de marca y el color de estado se fijan en un único conjunto dentro de cada proyecto y no deben cambiarse a la ligera; una misma semántica usa el mismo código de color en todo el repositorio.

Ejemplos de formato:

```markdown
![cobertura](https://img.shields.io/badge/coverage-95%25-orange?style=flat-square)
![estado](https://img.shields.io/badge/status-v0.1%20prototype-8957e5?style=flat-square)
![licencia](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
```

## 4. Parámetros de icono (logo / logoColor / logoSize)

### 4.1 Uso de Simple Icons

El parámetro `logo` toma el slug del icono de Simple Icons, con el formato `?logo=<slug>`. Los slugs habituales son los siguientes:

| Uso | slug | Apariciones medidas (N=120) |
| --- | --- | --- |
| Repositorio de GitHub | `github` | 35 |
| Comunidad de Discord | `discord` | 20 |
| Paquete de npm | `npm` | 4 |
| Plataformas de Apple | `apple` | 3 |
| Docker | `docker` | 3 |
| Plataforma social X | `x` | 3 |
| Paquete de Python | `pypi` | 2 |

El conjunto completo de slugs se rige por el sitio de Simple Icons o por el archivo `slugs.md` del repositorio simple-icons.

### 4.2 Color y tamaño del icono

- `logoColor`: establece el color del icono de Simple Icons; admite hexadecimal, rgb, hsl y colores con nombre de CSS; solo surte efecto en iconos de Simple Icons, no en iconos personalizados.
- `logoSize`: al fijarlo en `auto`, el icono se escala de forma adaptativa según el contenido, lo que conviene a iconos anchos; también surte efecto solo en Simple Icons.

Ejemplos de formato:

```markdown
![repo](https://img.shields.io/badge/github-repo-blue?logo=github)
![color del logo](https://img.shields.io/badge/logo-javascript-blue?logo=javascript&logoColor=f5f5f5)
```

Los iconos personalizados pueden pasarse mediante `logo=data:image/svg+xml;base64,...`, pero la URL resulta extremadamente larga y difícil de mantener, por lo que no se recomienda salvo necesidad especial.

## 5. Otros parámetros de consulta

| Parámetro | Función | Ejemplo |
| --- | --- | --- |
| `label` | Sobrescribe el texto predeterminado de la izquierda (los espacios deben codificarse) | `?label=healthiness` |
| `labelColor` | Color de fondo del lado izquierdo | `?labelColor=abcdef` |
| `color` | Color de fondo del lado derecho | `?color=fedcba` |
| `cacheSeconds` | Duración de la caché HTTP en segundos; los valores inferiores al predeterminado se ignoran | `?cacheSeconds=3600` |
| `link` | Especifica la dirección de salto al hacer clic en cada mitad | Solo surte efecto dentro de la etiqueta `<object>`; no funciona en imágenes de Markdown |

## 6. Insignias dinámicas

Las insignias dinámicas obtienen datos en tiempo real de servicios externos mediante Shields.io y no requieren actualizar el valor a mano. Tipos habituales:

| Categoría | Patrón de URL | Uso |
| --- | --- | --- |
| Estado de compilación | `https://img.shields.io/github/actions/workflow/status/<owner>/<repo>/<workflow>` | Estado de CI |
| Versión | `https://img.shields.io/npm/v/<package>` | Última versión en npm |
| Licencia | `https://img.shields.io/npm/l/<package>` | Licencia del paquete |
| Número de stars | `https://img.shields.io/github/stars/<owner>/<repo>` | Popularidad |
| Número de issues | `https://img.shields.io/github/issues/<owner>/<repo>` | Cuestiones pendientes |
| Descargas | `https://img.shields.io/npm/dt/<package>` | Descargas acumuladas |

A las insignias dinámicas se les pueden añadir parámetros como `?style=` o `?logo=`, con las mismas reglas que las estáticas. Los proyectos de referencia suelen adoptar la combinación «insignias dinámicas para indicadores reales más insignias estáticas para estados personalizados».

## 7. Selección de información y orden de disposición

### 7.1 Selección de información

Las insignias deben transmitir información de estado «verificable y útil para el lector». Se recomienda conservar solo las categorías siguientes:

1. Estado de compilación / pruebas;
2. Versión o última publicación;
3. Licencia;
4. Estado de la documentación;
5. Canales de comunidad (Discord, foro de discusión);
6. Estados personalizados del proyecto (prototipo, en mantenimiento, obsoleto).

No deben incluirse: cifras de descargas sin fuente, etiquetas de marketing ajenas al proyecto, valoraciones no verificables ni bloques de color meramente decorativos.

### 7.2 Orden de disposición

Se recomienda ordenar como «estado → versión → licencia → plataforma/comunidad → estado personalizado», con importancia decreciente de izquierda a derecha. Motivo: el estado de compilación determina si el lector adopta el proyecto, la versión determina el juicio de compatibilidad y la licencia determina si puede usarse; los tres son información previa a la decisión.

### 7.3 Control de cantidad

- Proyectos habituales: 4–6 insignias.
- Recopilaciones de recursos o proyectos de ecosistema: puede ampliarse a 8–10 insignias.
- Todas las insignias se colocan después del nombre del proyecto y de la frase de posicionamiento y antes del cuerpo del texto, en una línea propia o en un contenedor centrado, sin dispersarse por el texto.

### 7.4 Insignia estática de estado de entrega

La implementación estándar del punto 6 del apartado 7.1, «estado personalizado del proyecto», es la insignia estática de estado de entrega, cuyo valor actualiza manualmente el autor del proyecto y que sirve para el progreso de entrega y el estado de mantenimiento cuando no hay fuente de datos externa:

```text
![Status](https://img.shields.io/badge/status-4%20of%204%20delivered-brightgreen?style=flat-square)
```

1. La estructura estándar es `badge/<etiqueta>-<mensaje>-<color>` y el estilo debe ser uniformemente `?style=flat-square`; el ejemplo significa «los 4 entregables están entregados».
2. En el texto del mensaje los espacios se escriben `%20`, los guiones `--` y los guiones bajos `__`; no deben aparecer saltos de línea ni otros caracteres especiales sin escapar.
3. Convención semántica de colores: `brightgreen` indica completado, `yellow` en curso, `red` bloqueado y `lightgrey` no iniciado.
4. Cuando cambie el valor debe actualizarse sincrónicamente la insignia y el cuerpo del texto; la insignia no debe quedarse rezagada respecto del estado real durante mucho tiempo. Si no puede garantizarse la sincronización, se debe usar una insignia dinámica.
5. El texto `alt` debe declarar el significado real, por ejemplo `![estado de entrega]`; puede enlazarse a la lista de entregables o a la sección del índice correspondiente.

## 8. Accesibilidad y adaptación a temas

- El texto `alt` de cada insignia debe declarar su significado real, por ejemplo `![estado de compilación]` en lugar de `![badge]`.
- En temas oscuros o claros puede conmutarse la fuente de la imagen de la insignia mediante `<picture>`; usar `for-the-badge` junto con `labelColor=000` mantiene un contraste estable en ambos temas.
- La insignia debe poder hacer clic y saltar a la fuente de datos correspondiente (el estado de compilación a la CI, la versión a la página del gestor de paquetes, la licencia al archivo LICENSE).

## Archivos relacionados

- Pertenencia y orden de las secciones: [Especificación de secciones del README](./readme-sections-specification.md)
- Jerarquía visual y ubicación: [Especificación de maquetación visual del README](./readme-visual-layout-specification.md)
- Recomendaciones de insignias diferenciadas por tipo de proyecto: [Guía de adaptación del README por categoría](./readme-category-adaptation-guide.md)
- Línea completa de insignias lista para usar: [Plantilla estándar del README](./readme-standard-template.md)
- Método de investigación y muestras medidas: [Informe de investigación de plantillas del README](./readme-template-research-report.md)
