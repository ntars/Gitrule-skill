# Informe de investigación sobre plantillas de README

> Problema que resuelve este archivo: registra el método de investigación, el tamaño de la muestra y los hallazgos cuantitativos de esta plantilla estándar de README, proporcionando una base de datos a la [plantilla estándar de README](./readme-standard-template.md) y a las distintas especificaciones específicas, y delimita con claridad los límites y las limitaciones del método.

## 1. Objetivo y método de la investigación

### 1.1 Objetivo

Investigar proyectos de código abierto destacados con mayor número de estrellas, resumir las pautas de estructura, organización de secciones, presentación visual y uso de insignias de sus README y documentación relacionada, y formar una especificación general y una plantilla reutilizables.

### 1.2 Fuentes de datos

- Metadatos de repositorios: GitHub GraphQL Search API, ordenados por estrellas de forma descendente, con el filtro `is:public archived:false fork:false`.
- Texto original de los README: GitHub REST Contents API (punto de acceso `readme`), obtenido en formato base64 o raw y posteriormente analizado.
- Parámetros de insignias: documentación oficial de Shields.io (páginas Static Badge y Logos) y la descripción del formato de badge-maker.
- Práctica de la comunidad china: documentación del proyecto, mensajes de commit y capítulos de promoción de phodal/github (*Guía de exploración de GitHub*, 11,362 estrellas), utilizados para complementar los principios de redacción y la experiencia operativa que las estadísticas legibles por máquina no cubren.

### 1.3 Método de recogida

1. **Metadatos**: una consulta a GitHub Search API devuelve como máximo 1000 registros. Para ampliar la muestra se aplicó un particionado por intervalos de estrellas: mediante bisección se localizó el umbral de estrellas correspondiente a cada 1000 puestos, acumulando 11 lotes descendentes, y se obtuvieron finalmente los metadatos de 10,995 repositorios destacados.
2. **Muestreo de README**: dentro de los 1000 repositorios destacados se realizó un muestreo estratificado por lenguaje principal, cubriendo Python, TypeScript, JavaScript, Rust, Go, C++ y otros lenguajes principales; se muestrearon 120 repositorios y se obtuvo con éxito el texto original del README de todos ellos.
3. **Criterio estadístico**: la tasa de aparición de secciones y la tasa de uso de elementos se calculan por repositorio; los estilos de insignia y los parámetros de logo se contabilizan según el número de apariciones en las URL.

### 1.4 Limitaciones del método (deben explicitarse)

- GitHub Search API impone un límite de 1000 registros por consulta; este informe amplía la escala mediante la acumulación por particiones, pero los límites de partición se ven afectados por empates en el número de estrellas, por lo que la muestra es un conjunto aproximado de proyectos destacados, no una clasificación estrictamente continua.
- El tamaño de la muestra de README es de 120; las conclusiones reflejan tendencias y rasgos comunes, no una distribución estadísticamente significativa de todos los proyectos destacados.
- La identificación de secciones se basa en la coincidencia de palabras clave en los títulos, por lo que existen desviaciones estadísticas debidas a diferencias de redacción.
- La estadística de parámetros de insignias se refiere a los parámetros que aparecen explícitamente en la URL; no se contabilizan los parámetros predeterminados de las insignias dinámicas.

## 2. Distribución de los repositorios destacados (metadatos)

### 2.1 Tamaño de la muestra

- Una sola consulta permite obtener de forma estable los 1000 repositorios destacados, con un intervalo de estrellas de aproximadamente 563,574 a 30,857.
- Mediante la acumulación de 11 lotes particionados se amplió a 10,995 repositorios destacados, con un límite inferior de 5,452 estrellas.

### 2.2 Distribución por lenguaje (basada en los 1000 destacados)

| Lenguaje | Cantidad | Porcentaje |
| --- | --- | --- |
| Python | 223 | 22.3% |
| TypeScript | 178 | 17.8% |
| JavaScript | 112 | 11.2% |
| Rust | 80 | 8.0% |
| Sin lenguaje principal | 74 | 7.4% |
| Go | 68 | 6.8% |
| C++ | 55 | 5.5% |
| Java | 27 | 2.7% |

Los proyectos destacados son mayoritariamente de Python, TypeScript y JavaScript, que en conjunto superan el 50%; los lenguajes de sistemas como Rust y Go tienen una presencia notable. Esto determina que la plantilla deba cubrir comandos de instalación con gestores de paquetes de varios lenguajes e insignias de múltiples entornos de ejecución.

### 2.3 Distribución por licencia (basada en los 1000 destacados)

| Licencia | Cantidad | Porcentaje |
| --- | --- | --- |
| MIT | 399 | 39.9% |
| Apache-2.0 | 197 | 19.7% |
| No identificada (NOASSERTION) | 148 | 14.8% |
| Sin licencia (NONE) | 65 | 6.5% |
| GPL-3.0 | 51 | 5.1% |
| AGPL-3.0 | 50 | 5.0% |
| BSD-3-Clause | 17 | 1.7% |

MIT domina claramente y es la recomendación predeterminada de la plantilla general; al mismo tiempo deben conservarse los marcadores de posición del identificador SPDX para opciones como Apache-2.0 y GPL.

## 3. Hallazgos sobre la estructura del README (N=120)

### 3.1 Tasa de aparición de secciones

| Palabra clave de la sección | Repositorios en que aparece | Tasa de aparición |
| --- | --- | --- |
| Contributing | 66 | 55.0% |
| License | 52 | 43.3% |
| Install | 49 | 40.8% |
| Quick Start | 28 | 23.3% |
| Documentation | 25 | 20.8% |
| Development | 22 | 18.3% |
| Configuration | 19 | 15.8% |
| Features | 19 | 15.8% |
| Security | 15 | 12.5% |
| Usage | 12 | 10.0% |
| Requirements | 11 | 9.2% |
| API | 10 | 8.3% |
| Examples | 10 | 8.3% |

Hallazgo: la guía de contribución y la licencia son estándar en los proyectos destacados, lo que refleja la prioridad de la gobernanza comunitaria y el cumplimiento normativo; la instalación y el inicio rápido les siguen de cerca. Por ello la plantilla los considera ambos obligatorios.

### 3.2 Tasa de uso de elementos visuales

| Elemento | Repositorios en que aparece | Tasa de aparición | Mediana (por repositorio) |
| --- | --- | --- | --- |
| Bloques de código | 80 | 66.7% | 2 |
| Imágenes | 76 | 63.3% | 2 |
| Insignias (Shields.io) | 61 | 50.8% | 1 |
| Tablas | 44 | 36.7% | 0 |

Mediana de niveles de título: 7 títulos de segundo nivel; mediana de longitud del archivo: 171 líneas. Esto indica que los README destacados se mantienen por lo general en una longitud media, organizados con 6–12 títulos de segundo nivel.

### 3.3 Adaptación de tema (primeras 40 muestras)

| Característica | Repositorios en que aparece |
| --- | --- |
| Contenedor centrado (`align="center"`) | 27 |
| Elemento `<picture>` | 12 |
| Cambio de tema claro/oscuro (`prefers-color-scheme`) | 12 |
| `for-the-badge` combinado con `labelColor` | 2 |

El contenedor centrado es la técnica dominante en la portada; alrededor de un tercio de los proyectos ofrece imágenes en dos versiones, para tema claro y oscuro.

## 4. Hallazgos sobre insignias

### 4.1 Parámetros de estilo (por número de apariciones en URL, N=120)

| style | Apariciones |
| --- | --- |
| `for-the-badge` | 65 |
| `flat-square` | 60 |
| `flat` | 32 |
| `social` | 12 |
| `plastic` | 1 |

`for-the-badge` y `flat-square` son los más populares; `plastic` está prácticamente en desuso. Para más detalles, véase la [especificación de insignias](./badge-specification.md).

### 4.2 Parámetros logo (por número de apariciones, N=120)

| logo slug | Apariciones |
| --- | --- |
| `github` | 35 |
| `discord` | 20 |
| `npm` | 4 |
| `apple` / `docker` / `linkedin` / `x` | 2–3 cada uno |

GitHub y Discord son los iconos más frecuentes, correspondientes a las dos categorías de información «repositorio de código fuente» y «canales de comunidad».

## 5. Evidencia de la primera pantalla en proyectos de referencia

| Proyecto | Tipo | Características de la portada |
| --- | --- | --- |
| `sindresorhus/awesome` | Colección de recursos | Logo centrado, zona de patrocinio, índice por categorías temáticas |
| `axios/axios` | Biblioteca | Aviso importante, tabla de patrocinio, multilenguaje |
| `sharkdp/fd` | CLI | Insignias + enlaces multilingües, navegación por secciones, GIF de Demo |
| `BurntSushi/ripgrep` | CLI | Insignias, enlaces rápidos, captura de búsqueda, comparación de rendimiento |
| `vercel/next.js` | Marco de trabajo | Logo centrado, insignias `for-the-badge`, entradas a documentación y comunidad |
| `microsoft/vscode` | Aplicación | Insignias, descripción del repositorio, captura del producto, entradas de contribución y comentarios |
| `rust-lang/rust` | Lenguaje | Banner centrado, fila de navegación, puntos de valor Why Rust |
| `phodal/github` | Libro electrónico en chino | Cuatro preguntas de la portada, ejemplo de texto en una frase, principio de simplificación de la instalación, lista de canales de promoción |

Rasgos comunes: la primera pantalla responde a «qué es, cómo se usa y dónde está el detalle»; las insignias van pegadas al título; la captura de pantalla o la Demo sigue al posicionamiento; las entradas de contribución y comunidad quedan más abajo pero son imprescindibles.

## 6. Conclusiones

1. La plantilla general debe tener como eje «posicionamiento → instalación → inicio rápido → documentación → contribución → licencia».
2. Las insignias usan por defecto `flat-square` o `for-the-badge`, de forma uniforme en todo el documento, en número de 4–6.
3. Las imágenes y los bloques de código son el núcleo de una portada atractiva y deben acompañarse de `alt` e identificación de lenguaje.
4. El tipo de proyecto determina la selección de secciones; véase la [guía de adaptación del README por categoría](./readme-category-adaptation-guide.md).
5. El cumplimiento normativo y la gobernanza comunitaria (licencia, guía de contribución) son un consenso en los proyectos destacados y se consideran obligatorios.

## 7. Explicación de la escala de datos

Resultado acumulado del particionado de metadatos de repositorios destacados: 10,995 repositorios, con un intervalo de estrellas de 563,575 a 5,452. La distribución de licencias y lenguajes de esta muestra de escala diezmilésima es la siguiente, coherente con las conclusiones de la muestra de los 1000 destacados:

| Dimensión | Distribución |
| --- | --- |
| Lenguaje | Python 1,995, TypeScript 1,529, JavaScript 1,279, sin lenguaje principal 888, Go 847, C++ 531, Java 528, Rust 507 |
| Licencia | MIT 4,160 (37.8%), Apache-2.0 2,073 (18.9%), no identificada 1,463, sin licencia 1,106, GPL-3.0 747 |

La muestra de estadística profunda de README es de 120, obtenida con éxito en su totalidad. El particionado emplea umbrales aproximados de estrellas; la escala es un conjunto aproximado de proyectos destacados, no una clasificación estrictamente continua.

## Archivos relacionados

- Para la plantilla aplicable directamente, véase la [plantilla estándar de README](./readme-standard-template.md)
- Para la especificación de insignias, véase la [especificación de insignias](./badge-specification.md)
- Para la especificación visual, véase la [especificación de maquetación visual del README](./readme-visual-layout-specification.md)
- Para la adaptación por categoría, véase la [guía de adaptación del README por categoría](./readme-category-adaptation-guide.md)
- Para la definición de secciones, véase la [especificación de secciones del README](./readme-sections-specification.md)
