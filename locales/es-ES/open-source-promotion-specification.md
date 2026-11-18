# Especificación de promoción del código abierto

> Problema que resuelve este archivo: define los canales de promoción antes y después de la publicación de un proyecto de código abierto, el ritmo de publicación, los materiales de la página principal y las normas de gestión comunitaria, para que el proyecto obtenga, sobre la base de contar con documentación utilizable, una difusión acorde con sus usuarios objetivo.

La lista de canales y los principios de este archivo se basan en el capítulo de promoción de la «Guía de recorrido por GitHub» de phodal; ese proyecto, con 11.362 star, ha validado la aplicabilidad de estas prácticas en la comunidad china de código abierto.

## 1. Principios básicos

1. **La calidad precede a la promoción**: la promoción solo amplifica la calidad existente y no repara carencias. No debe iniciarse la promoción antes de que el README, los ejemplos, la documentación y las pruebas estén listos.
2. **El proyecto no es todo lo que se promociona**: además del código y el README, deben prepararse documentación detallada, programas de ejemplo y un mecanismo de respuesta a problemas.
3. **Motivación explícita**: la promoción sirve a objetivos concretos (captar usuarios iniciales, reclutar contribuyentes, recoger comentarios) y no debe realizarse para perseguir el número de star.
4. **Adecuación del canal**: los canales se eligen según el stack tecnológico y los usuarios objetivo del proyecto, evitando difusiones indiscriminadas.
5. **Presentación honesta**: no deben inventarse cifras de star, volúmenes de descarga ni casos de uso; las comparaciones de funcionalidades deben basarse en hechos verificables.

## 2. Lista de preparación previa a la publicación

| Categoría | Requisito | Base de determinación |
| --- | --- | --- |
| Página principal | El README supera la comprobación de las cuatro preguntas (qué hace / qué resuelve / funcionalidades / ejemplos) | [especificación de secciones del README](./readme-sections-specification.md) |
| Texto de una frase | Define con claridad la categoría y los calificativos; puede repetirse de forma autónoma | Ídem, sección 1.1 |
| Ejemplo | Ofrece un hello world ejecutable en dos pasos | [plantilla estándar de README](./readme-standard-template.md) |
| Documentación | Instalación, configuración y documentación de API completas | [matriz de documentación](./document-matrix.md) |
| Licencia | LICENSE existe y coincide con la indicada en el README | [especificación de LICENSE](./license-specification.md) |
| Cumplimiento | NOTICE cubre las dependencias de terceros | [especificación de NOTICE](./notice-specification.md) |
| Accesos comunitarios | Plantillas de issue, guía de contribución y código de conducta disponibles | [especificación de la guía de contribución](./contribution-guide-specification.md) |
| Mecanismo de respuesta | Responsable de respuesta y plazo de respuesta definidos | [especificación de respuesta a incidentes](./incident-response-specification.md) |

Promocionar sin haber completado esta lista constituye una práctica prohibida por esta especificación.

## 3. Clasificación de canales

### 3.1 Comunidades técnicas internacionales

| Canal | Contenido adecuado | Advertencias |
| --- | --- | --- |
| Hacker News | Implementación técnica, ingeniería de cierta profundidad | El título debe ser sobrio y evitar formulaciones publicitarias |
| Subforos correspondientes de Reddit | Bibliotecas, herramientas, frameworks | Respetar las reglas de autopromoción de cada subforo |
| Lobsters | Programación de sistemas, prácticas de ingeniería | La comunidad es sensible a la publicidad |
| Boletines técnicos (JavaScript Weekly, etc.) | Bibliotecas y herramientas | Ofrecer un resumen conciso del proyecto |
| Blog oficial y sitio de documentación | Presentaciones en profundidad y notas de versión | Sirven de destino para los demás canales |

### 3.2 Comunidades técnicas chinas

| Canal | Contenido adecuado |
| --- | --- |
| Juejin | Frontend, móvil, prácticas de ingeniería |
| Developer Headlines | Proyectos técnicos generales |
| V2EX | Herramientas, software de productividad, proyectos emprendedores |
| Zhihu | Análisis técnicos y decisiones de diseño |
| Cuenta oficial de WeChat | Artículos largos en profundidad, series de tutoriales |
| Geek Headlines | Noticias técnicas generales |

### 3.3 Canales propios del proyecto

1. Los accesos comunitarios del README del proyecto (Discussions, Discord);
2. Las cuentas sociales propias del proyecto, para anunciar versiones y actividades;
3. El sitio de documentación y el sitio de ejemplos, como páginas de recepción del tráfico externo.

## 4. Ritmo de publicación

1. **Periodo de preparación**: completar la lista de la sección 2 y preparar el texto de una frase, las capturas de pantalla, los GIF de demostración y demás materiales.
2. **Periodo de lanzamiento inicial**: publicar en 1 o 2 canales de máxima afinidad, evitando saturar varias plataformas con el mismo contenido.
3. **Periodo de respuesta**: mantener un ritmo alto de respuesta durante las 72 horas siguientes al lanzamiento, atendiendo los issues y los comentarios.
4. **Periodo de iteración**: actualizar de forma continua siguiendo el ritmo de publicación de versiones, acompañando cada publicación de una nota de cambios.
5. **Periodo de consolidación**: organizar las preguntas más frecuentes en una FAQ y retroalimentar la documentación.

## 5. Requisitos de los materiales de la página principal

| Material | Especificación | Uso |
| --- | --- | --- |
| Texto de una frase | En chino, menos de 60 caracteres / en inglés, menos de 25 palabras; la Description del repositorio adopta el formato combinado bilingüe «idioma nacional \| inglés», véase la sección 5 de la [especificación de nomenclatura de proyectos](./project-naming-specification.md) | Description del repositorio, resumen en redes sociales |
| Capturas de pantalla | Dos versiones, para tema claro y oscuro, con anchura controlada | Primera pantalla del README |
| GIF de demostración | Volumen controlado tras la compresión, que muestre el flujo principal | Sección de demostración del README |
| Logotipo | Formato SVG, con versiones clara y oscura | Primera pantalla y tarjetas sociales |
| Tabla comparativa de funcionalidades | Basada en hechos verificables e incluyendo los escenarios no aplicables | README o sitio de documentación |

Los materiales deben actualizarse en sincronía con las versiones, evitando mostrar interfaces de versiones antiguas.

## 6. Gestión comunitaria

1. Ofrecer a los nuevos contribuyentes un acceso claro, como la etiqueta `good first issue`.
2. La respuesta a los problemas debe quedar registrada, para evitar que las mismas dudas reaparezcan de forma reiterada.
3. El código de conducta se aplica a todos los canales comunitarios, véase la [especificación de código de conducta](./code-of-conduct-specification.md).
4. El agradecimiento a los contribuyentes se concentra en un único lugar, evitando que quede disperso por el cuerpo del documento.
5. No deben obtenerse seguidores falsos mediante la inducción de star, el intercambio de «me gusta» u otros métodos.

## 7. Prácticas prohibidas

1. Se prohíbe promocionar cuando la lista de calidad no está completa.
2. Se prohíbe inventar o exagerar datos del proyecto y casos de uso.
3. Se prohíbe saturar varios canales con el mismo contenido repetido.
4. Se prohíbe menospreciar proyectos similares para mejorar la propia imagen.
5. Se prohíbe emplear métodos de inducción para obtener número de star.

## Archivos relacionados

- Las cuatro preguntas de la página principal y el texto de una frase se tratan en la [especificación de secciones del README](./readme-sections-specification.md)
- Las especificaciones de los materiales visuales se tratan en la [especificación de maquetación visual del README](./readme-visual-layout-specification.md)
- Las normas de los accesos comunitarios se tratan en la [especificación de la guía de contribución](./contribution-guide-specification.md)
- El mecanismo de respuesta a problemas se trata en la [especificación de respuesta a incidentes](./incident-response-specification.md)
- Las notas de versión publicadas se tratan en la [especificación de push y publicación](./push-and-release-specification.md)
- Las fuentes de la investigación se detallan en el [informe de investigación de plantillas de README](./readme-template-research-report.md)
