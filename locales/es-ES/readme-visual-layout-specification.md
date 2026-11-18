# Especificación de maquetación visual del README

> Problema que resuelve este archivo: define la jerarquía de maquetación del README, la organización de párrafos, el uso de tablas, capturas de pantalla y GIF, así como su ubicación, para que la documentación alcance un equilibrio entre densidad informativa y atractivo visual.

Los datos empíricos de este documento proceden del muestreo estadístico de README de proyectos destacados de código abierto realizado por este proyecto (muestra N=120); las prácticas de referencia se extraen del estudio de la estructura de primera pantalla de varios proyectos con muchas estrellas.

## 1. Jerarquía de maquetación

### 1.1 Niveles de título

El README debe establecer una jerarquía de títulos clara y respetar las siguientes restricciones:

1. En todo el texto solo se conserva un título de primer nivel (`#`), que es el nombre del proyecto y se ubica en la primera línea del archivo.
2. Los títulos de segundo nivel (`##`) son las secciones principales; se recomienda que su número sea de 6 a 12, con una mediana empírica de 7.
3. Los títulos de tercer nivel (`###`) sirven para subdividir una sección y solo se usan cuando el contenido del título de segundo nivel es extenso.
4. No debe haber saltos en la jerarquía de títulos (por ejemplo, pasar de `#` directamente a `###`).
5. El texto del título debe ser conciso, con sustantivos o sintagmas nominales, y sin punto final.

### 1.2 Orden de la estructura de primera pantalla

La primera pantalla es el contenido que el lector ve sin desplazarse; se organiza en el siguiente orden:

1. Logotipo o banner del proyecto centrado (opcional);
2. Título de primer nivel (nombre del proyecto);
3. Línea de insignias (véase la [especificación de insignias](./badge-specification.md));
4. Posicionamiento en una frase (qué es el proyecto, para quién es y qué problema resuelve);
5. Línea de enlaces de navegación por secciones (opcional, para README extensos);
6. Resumen de las funciones o características principales.

Evidencia de referencia: `fd` y `ripgrep` sitúan la navegación por secciones inmediatamente después del posicionamiento; `next.js` y `rust-lang/rust` abren con logotipo centrado y banner; `vscode` inserta una captura del producto justo después del posicionamiento.

### 1.3 Párrafos y espacio en blanco

- Cada párrafo debe ocupar de 1 a 4 líneas para evitar bloques densos de texto.
- Debe dejarse una línea en blanco entre párrafos para preservar la respiración visual tras el renderizado.
- Las conclusiones clave deben ir primero y las explicaciones después.
- Debe conservarse un espacio entre el chino y el inglés o los números; la puntuación china y la inglesa se usan según su propio contexto.

## 2. Normas de uso de tablas

### 2.1 Casos de uso

Las tablas son adecuadas para información multidimensional y comparable. El 36,7 % de la muestra empírica usa tablas, y son el formato recomendado para descripciones de configuración, matrices de compatibilidad y correspondencias de comandos. Los casos de uso incluyen:

- Descripción de opciones de configuración (nombre de la clave, tipo, valor predeterminado, función);
- Matriz de compatibilidad de plataformas y versiones;
- Correspondencia de comandos o parámetros;
- Comparación de funciones (este proyecto frente a otras soluciones);
- Hoja de ruta y estado.

### 2.2 Ubicación

La tabla debe ir inmediatamente después del título de segundo nivel al que pertenece, precedida por una frase introductoria que explique su propósito; si tras la tabla hay excepciones, deben añadirse en un párrafo aparte.

### 2.3 Requisitos de redacción

| Requisito | Descripción |
| --- | --- |
| Control de columnas | De 3 a 6 columnas; si se superan las 6, debe considerarse la división |
| Encabezado explícito | Cada columna debe llevar un encabezado nominal breve; no deben dejarse encabezados vacíos |
| Alineación coherente | El modo de alineación de las tablas debe ser uniforme en todo el texto |
| Contenido breve | No deben escribirse párrafos largos en las celdas; cuando sea necesario, debe ampliarse con notas al pie o enlaces |
| Sin celdas vacías | Donde no haya contenido debe escribirse «ninguno» o «no aplica» |

## 3. Normas de uso de bloques de código

### 3.1 Casos de uso

Los bloques de código sirven para comandos, configuración, llamadas a la API y salidas de ejemplo. El 66,7 % de la muestra empírica contiene bloques de código, que son un elemento imprescindible de la sección «Inicio rápido», con una mediana de 2.

### 3.2 Requisitos de redacción

1. Cada bloque de código debe indicar el lenguaje, por ejemplo `bash`, `json`, `python` o `javascript`, para facilitar el resaltado de sintaxis.
2. Los ejemplos de comandos deben ofrecer el comando completo y ejecutable; no deben omitirse los pasos previos.
3. Cuando deba mostrarse el resultado, debe abrirse otro bloque de código marcado como `text` y explicarse en el texto la salida esperada.
4. Debe dejarse una línea en blanco antes y después de cada bloque de código.
5. El contenido de un bloque debe limitarse a 20 líneas; los ejemplos más largos deben dividirse en varios bloques o trasladarse al directorio `examples/` con un enlace.
6. Si se usa el indicador `$` en comandos interactivos, debe mantenerse de forma uniforme en todo el documento.

Ejemplo de formato:

```bash
npm install <package-name>
```

```text
✓ Installation complete
```

## 4. Normas de uso de capturas de pantalla y GIF

### 4.1 Casos de uso y criterios de elección

| Elemento | Casos de uso | Precauciones |
| --- | --- | --- |
| Captura estática | Interfaz de la aplicación, resultados de ejecución, gráficos | Uso empírico del 63,3 %, el más frecuente |
| GIF / animación | Demostraciones de línea de comandos, flujos interactivos, comparaciones antes y después | Archivo voluminoso; debe comprimirse y limitarse su duración |
| Logotipo / banner | Identificación de marca, primera pantalla | Debe ofrecerse en versión clara y oscura |
| Diagrama esquemático | Arquitectura, flujos, flujo de datos | Debe actualizarse junto con la versión de la documentación |

El 63,3 % de la muestra empírica incluye imágenes. Evidencia de referencia: `fd` usa `doc/screencast.svg` como demo, `ripgrep` usa una captura de los resultados de búsqueda, `vscode` usa una captura del producto en funcionamiento, y `rust` y `next.js` usan banners de logotipo con adaptación a tema claro y oscuro.

### 4.2 Ubicación

1. Logotipo / banner: en la parte superior del archivo, centrado.
2. Captura del producto: después del posicionamiento en una frase y antes de «Inicio rápido», para establecer una comprensión intuitiva.
3. Demostración en GIF: en una sección independiente «Demo / Demostración», inmediatamente después de «Funciones principales».
4. Diagrama de arquitectura: en la sección «Arquitectura» o «Diseño», o trasladado a `docs/architecture.md` con un enlace desde el README.

### 4.3 Requisitos de redacción

- Cada imagen debe incluir un texto `alt` que describa su contenido; no deben usarse textos sin significado como `image` o «captura».
- Las imágenes deben referenciarse con rutas relativas a los recursos del repositorio, o con una URL absoluta estable; deben evitarse los enlaces temporales con caducidad.
- Las imágenes que deban adaptarse al tema deben usar el elemento HTML `<picture>` junto con `prefers-color-scheme` para ofrecer versiones clara y oscura.
- Debe controlarse el tamaño de las imágenes: en las capturas deben preferirse WebP o PNG optimizado, y los GIF deben convertirse preferentemente en vídeos cortos o animaciones comprimidas.
- La anchura de las imágenes debe ajustarse: debe usarse el atributo `width` o un contenedor externo que la limite para evitar que rompan la página.

## 5. Enlaces y navegación

### 5.1 Navegación por secciones

Cuando el README supere las 200 líneas, debe añadirse en la primera pantalla una línea de enlaces de navegación que apunte a las secciones principales:

```markdown
[Instalación](#instalación) · [Inicio rápido](#inicio-rápido) · [Documentación](#documentación) · [Contribución](#contribución)
```

### 5.2 Preferencia por enlaces relativos

La documentación, las imágenes y la licencia dentro del repositorio deben usar siempre rutas relativas, para que sigan siendo utilizables tras un Fork y en lectura sin conexión. Los enlaces externos deben apuntar a fuentes autorizadas (documentación oficial, páginas de gestores de paquetes, páginas de CI).

## 6. Lista de verificación de estética y atractivo

1. La primera pantalla cuenta con logotipo o un título claro que comunica el posicionamiento del proyecto en 3 segundos.
2. Las insignias tienen estilo uniforme, colores semánticos y una cantidad moderada.
3. El título de primer nivel es único, hay de 6 a 12 títulos de segundo nivel y no existen saltos de jerarquía.
4. Existe al menos un ejemplo de código copiable y ejecutable.
5. Existe al menos una captura o demo que muestre el valor del producto.
6. Las tablas se emplean para información comparativa, con columnas controladas y encabezados claros.
7. Todas las imágenes tienen `alt` y todos los bloques de código indican el lenguaje.
8. Los documentos extensos cuentan con navegación por secciones.
9. Las imágenes y las insignias son legibles en tema claro y en tema oscuro.

## Archivos relacionados

- Para el estilo y la paleta de las insignias, véase la [especificación de insignias](./badge-specification.md)
- Para la lista completa de secciones, véase la [especificación de secciones del README](./readme-sections-specification.md)
- Para el énfasis visual según el tipo de proyecto, véase la [guía de adaptación del README por categoría](./readme-category-adaptation-guide.md)
- Para un esqueleto de maquetación directamente aplicable, véase la [plantilla estándar de README](./readme-standard-template.md)
- Para la muestra empírica y el método, véase el [informe de investigación de plantillas de README](./readme-template-research-report.md)
