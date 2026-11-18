# Guía de adaptación del README por categoría

> Problema que resuelve este archivo: ofrece recomendaciones diferenciadas sobre la selección de secciones del README, el enfoque visual y la configuración de insignias para distintos tipos de proyecto —bibliotecas, aplicaciones, herramientas de línea de comandos, marcos de trabajo y colecciones de recursos— y explica cómo cada tipo de elemento mejora la estética y el atractivo.

La plantilla general sirve para todos los proyectos, pero los lectores de distintos tipos de proyecto se fijan en cosas diferentes. Este archivo ofrece recomendaciones de ajuste por tipo sobre la especificación general. El lector debe tomar como base la [plantilla estándar de README](./readme-standard-template.md) y recortarla según el tipo correspondiente en este archivo.

## 1. Visión general de tipos

| Tipo | Primera pregunta del lector | Centro de gravedad de la portada | Secciones obligatorias | Secciones omitibles |
| --- | --- | --- | --- | --- |
| Biblioteca / SDK | Forma de instalación y uso de la API | Versión y licencia | Instalación, inicio rápido, API, compatibilidad | Despliegue, capturas de pantalla |
| Aplicación | Aspecto de la aplicación y funcionalidades principales | Capturas de pantalla y funcionalidades | Funcionalidades, capturas de pantalla, instalación, inicio rápido | Referencia de API |
| Herramienta de línea de comandos | Uso de comandos y rendimiento | Ejemplos de comandos y Demo | Instalación, uso, tabla de comandos, Demo | Arquitectura, configuración (cuando es escasa) |
| Marco de trabajo | Ecosistema y coste de aprendizaje | Entrada a la documentación y ejemplos | Posicionamiento, inicio rápido, documentación, comunidad | Detalles de rendimiento (pueden enlazarse externamente) |
| Colección de recursos | Qué se recopila y cómo se busca | Categorías del índice y navegación | Índice, categorías, guía de contribución | Instalación, API |

## 2. Biblioteca / SDK

Representantes típicos: clientes HTTP como axios, bibliotecas de funciones utilitarias, SDK de cliente.

### 2.1 Selección de secciones

- Anteponer «posicionamiento en una frase + versión + licencia», para que el lector juzgue la compatibilidad con esa base.
- «Instalación» va en primer lugar, con los comandos del gestor de paquetes (npm, pip, cargo, etc.).
- «Inicio rápido» debe ser un ejemplo completo ejecutable de forma independiente.
- La «referencia de API» se detalla en el README principal o se enlaza a `docs/api.md`; si hay demasiadas entradas de API, el README solo incluye un resumen + enlace.
- «Compatibilidad» indica las versiones de lenguaje, los entornos de ejecución y las plataformas soportadas.

### 2.2 Enfoque visual

- Insignias destacadas: versión, estado de compilación, licencia, descargas, tamaño del paquete.
- Uso comedido de imágenes; normalmente no se necesitan capturas de pantalla; puede usarse un logo pequeño para crear identidad.
- Los parámetros de la API se presentan en tabla, para mejorar la legibilidad.

### 2.3 Puntos clave para mejorar la estética

1. Las insignias de versión y licencia van arriba, para establecer credibilidad de inmediato.
2. El bloque de código de inicio rápido se sitúa cerca de la primera pantalla, para reducir la barrera de prueba.
3. La tabla de API unifica el ancho de columna y la columna de valor predeterminado, para reducir la carga cognitiva.

## 3. Aplicación

Representantes típicos: editores, herramientas de escritorio, productos para usuario final.

### 3.1 Selección de secciones

- La primera pantalla debe incluir una captura de pantalla del producto o una imagen en ejecución: mostrar primero el valor y después la implementación.
- Las «funcionalidades principales» se organizan por escenario de usuario, no por módulo técnico.
- «Instalación» cubre los paquetes de instalación o puntos de descarga de cada plataforma.
- «Inicio rápido» ofrece la ruta de entrada más corta.
- Las instrucciones de compilación desde el código fuente pueden enlazarse externamente a `CONTRIBUTING.md`.

### 3.2 Enfoque visual

- Insignias destacadas: versión, estado de compilación, licencia, descargas.
- La captura de pantalla va después del posicionamiento y es el elemento central de la portada.
- La lista de funcionalidades se acompaña de iconos o capturas breves, para mejorar la eficiencia de escaneo.

### 3.3 Puntos clave para mejorar la estética

1. Mostrar centrada una captura de pantalla de alta calidad del producto, adaptable a temas claros y oscuros.
2. Usar frases cortas + iconos para los puntos funcionales, evitando descripciones largas.
3. Puntos de descarga llamativos, mediante enlaces con forma de botón.

## 4. Herramienta de línea de comandos

Representantes típicos: herramientas de terminal como fd y ripgrep.

### 4.1 Selección de secciones

- Tras el «posicionamiento en una frase» va inmediatamente la navegación por secciones, para facilitar los saltos.
- «Instalación» enumera los gestores de paquetes principales y los binarios por plataforma.
- «Uso» está orientado a tareas y ofrece ejemplos de comandos habituales.
- La «tabla de comandos» o la «comparación con herramientas similares» es una necesidad frecuente.
- La «Demo» usa GIF o grabación de terminal para mostrar el efecto real.
- Los datos de rendimiento deben indicar el entorno y el método de prueba.

### 4.2 Enfoque visual

- Insignias destacadas: versión, estado de compilación, soporte de plataformas, licencia.
- El GIF de la Demo es el activo visual central: muestra la velocidad y la experiencia de uso.
- Los comandos usan bloques de código con lenguaje indicado; las salidas usan bloques `text`.

### 4.3 Puntos clave para mejorar la estética

1. Los ejemplos de comandos van arriba, para que el lector pueda copiarlos y usarlos sin desplazarse.
2. El GIF de la Demo muestra el efecto real de la terminal, reforzando la impresión de «rapidez».
3. Los enlaces multilingües (por ejemplo, traducciones al chino o al coreano) se sitúan cerca de la fila de insignias.

## 5. Marco de trabajo

Representantes típicos: marcos full stack como next.js.

### 5.1 Selección de secciones

- La primera pantalla destaca el posicionamiento, la escala del ecosistema y la entrada de aprendizaje.
- La entrada a la «documentación» debe ser llamativa y normalmente apunta a un sitio de documentación independiente.
- «Comunidad» explica las zonas de debate, los canales de mensajería instantánea y el código de conducta.
- «Inicio rápido» ofrece el comando mínimo de creación de proyecto.
- Los contenidos profundos (arquitectura, API) se enlazan externamente y no se desarrollan en el README.

### 5.2 Enfoque visual

- Insignias destacadas: versión, estado de compilación, licencia, canales de comunidad.
- Combinación del logo de marca con insignias de estilo `for-the-badge`, para reforzar la portada.
- Pueden usarse capturas de Showcase para mostrar casos del ecosistema.

### 5.3 Puntos clave para mejorar la estética

1. Logo centrado + insignias grandes de estilo uniforme, para formar una portada con identidad de marca.
2. Las entradas a la documentación y a la comunidad se presentan como bloques de navegación llamativos.
3. Entradas para principiantes como Good First Issues reducen la barrera de contribución.

## 6. Colección de recursos

Representantes típicos: listas de la serie awesome.

### 6.1 Selección de secciones

- Es habitual abrir la primera pantalla con el logo y la información de patrocinio.
- El cuerpo organiza el índice por categorías temáticas y ofrece una navegación clara.
- La «guía de contribución» explica los criterios de inclusión y el formato de envío.
- No se necesitan secciones de instalación, API ni despliegue.

### 6.2 Enfoque visual

- El número de insignias puede ser más flexible, pero debe mantener un estilo uniforme.
- Las categorías del índice usan títulos de segundo nivel + listas, con una breve descripción en cada entrada.
- Los logos de patrocinadores se disponen en tabla o cuadrícula, manteniendo la alineación.

### 6.3 Puntos clave para mejorar la estética

1. Estructura del índice clara y jerarquía de títulos de categoría coherente.
2. Cada entrada lleva una frase de descripción, evitando que haya solo enlaces.
3. Las zonas de patrocinio y agradecimientos están alineadas y ordenadas, sin dificultar la lectura del cuerpo.

## 7. Principios generales entre tipos

1. **Prioridad al lector**: la primera pantalla responde a lo que más le importa al lector; las diferencias de tipo solo afectan al orden, no a la integridad de la información.
2. **Estilo uniforme**: las insignias, los títulos y los bloques de código de un mismo proyecto deben ser coherentes.
3. **Ejemplos copiables**: cualquier tipo debe ofrecer al menos un ejemplo ejecutable directamente.
4. **Enlaces externos**: los contenidos profundos que exceden la responsabilidad de la portada se enlazan a documentación independiente.
5. **Sincronización continua**: las capturas de pantalla, las insignias de versión y la lista de funcionalidades deben actualizarse con cada versión, evitando que la información obsoleta dañe la credibilidad.

## Archivos relacionados

- Para la lista general de secciones, véase la [especificación de secciones del README](./readme-sections-specification.md)
- Para la especificación de elementos visuales, véase la [especificación de maquetación visual del README](./readme-visual-layout-specification.md)
- Para la configuración de insignias, véase la [especificación de insignias](./badge-specification.md)
- Para la plantilla general, véase la [plantilla estándar de README](./readme-standard-template.md)
- Para la evidencia de la distribución por tipos, véase el [informe de investigación de plantillas de README](./readme-template-research-report.md)
