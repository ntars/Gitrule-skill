# Especificación de accesibilidad

> Problema que resuelve este archivo: define los requisitos de accesibilidad de la documentación del proyecto, del README y de las interfaces de usuario, para que el contenido sea igualmente utilizable por lectores que emplean lectores de pantalla, que operan con teclado o que presentan distintas condiciones visuales.

## 1. Ámbito de aplicación

1. Accesibilidad de la documentación: README, sitio de documentación, código de ejemplo, tablas e imágenes.
2. Accesibilidad de la interfaz: la interfaz de usuario de aplicaciones y proyectos web.
3. Accesibilidad de la línea de comandos: texto de ayuda, mensajes de error y formato de salida.

## 2. Accesibilidad de la documentación

### 2.1 Imágenes y medios

1. Cada imagen debe incluir un texto `alt` que describa el contenido y la función de la imagen; las imágenes decorativas usan un `alt` vacío.
2. No deben usarse como `alt` textos sin información como «imagen», «captura de pantalla» o «image».
3. Los GIF animados deben explicar su contenido en el texto contiguo, evitando transmitir información únicamente mediante la animación.
4. Los gráficos deben ir acompañados de una descripción textual o de una tabla de datos; no debe distinguirse las series de datos solo por color.

### 2.2 Títulos y estructura

1. La jerarquía de títulos es continua y no deben saltarse niveles (véase la [especificación de maquetación visual del README](./readme-visual-layout-specification.md)).
2. En todo el documento solo hay un título de primer nivel.
3. Las listas emplean la sintaxis Markdown correcta para que el lector de pantalla las identifique como listas.
4. Las tablas deben tener fila de encabezado; no debe maquetarse la página con tablas sin encabezado.

### 2.3 Enlaces y texto

1. El texto del enlace debe describir el destino por sí mismo; se prohíbe usar «haz clic aquí» o «más».
2. El color no debe ser el único medio de transmitir información; debe acompañarse de texto o iconos.
3. En la combinación de caracteres latinos y de otros alfabetos se conservan los espacios, para garantizar la segmentación correcta de palabras y la lectura en voz alta.
4. La primera vez que aparece una abreviatura se indica su forma completa.

### 2.4 Código y tablas

1. Los bloques de código indican el lenguaje para facilitar su identificación por las herramientas de asistencia (véase la [especificación de maquetación visual del README](./readme-visual-layout-specification.md)).
2. El contenido de las celdas de tabla es conciso; debe evitarse la combinación de celdas que dificulta el análisis por los lectores.
3. Los comandos largos se presentan divididos en líneas, sin depender del desplazamiento horizontal.

## 3. Accesibilidad de la interfaz

### 3.1 Operación con teclado

1. Todos los elementos interactivos deben ser alcanzables y operables con el teclado.
2. El orden del foco coincide con el orden visual y el estado del foco es claramente visible.
3. Se ofrece un acceso rápido para saltar contenido repetido (por ejemplo, ir al contenido principal).

### 3.2 Semántica y etiquetas

1. Se emplean etiquetas semánticas para expresar estructura y roles; debe evitarse simular controles con elementos sin semántica.
2. Los controles de formulario deben tener una etiqueta asociada, y los mensajes de error deben estar vinculados al campo correspondiente.
3. Los cambios dinámicos de estado se comunican a las tecnologías de asistencia mediante avisos accesibles.

### 3.3 Condiciones visuales

1. El contraste entre texto y fondo cumple los requisitos de legibilidad; el contraste del texto normal no es inferior a 4,5:1 y el del texto grande no es inferior a 3:1.
2. Se admiten los temas claro y oscuro del sistema, y el cambio de tema no altera la estructura de la información (véase la [especificación de maquetación visual del README](./readme-visual-layout-specification.md)).
3. Las animaciones ofrecen la opción de reducirse y se evita el contenido con parpadeos frecuentes en reproducción automática.
4. Con el texto ampliado al 200 % la maquetación sigue siendo utilizable y no se produce truncamiento de contenido.

## 4. Accesibilidad de la línea de comandos

1. Los mensajes de error explican la causa y la acción de corrección posible; no deben limitarse a mostrar un código de error.
2. La salida de `--help` está claramente categorizada y enumera los parámetros obligatorios y los valores predeterminados.
3. Se admite una variable de entorno que desactiva la salida en color, para facilitar el uso con lectores de pantalla y el procesamiento de registros.
4. Las solicitudes interactivas ofrecen parámetros equivalentes no interactivos, para admitir escenarios automatizados.

## 5. Lista de verificación

- [ ] Todas las imágenes tienen un texto `alt` con información explícita.
- [ ] La jerarquía de títulos es continua y hay un solo título de primer nivel en todo el documento.
- [ ] El texto de los enlaces se comprende por sí mismo.
- [ ] Las tablas tienen encabezado y el color no es el único portador de información.
- [ ] Los bloques de código indican el lenguaje.
- [ ] Los elementos de la interfaz se operan con teclado y el foco es visible.
- [ ] El contraste cumple el mínimo exigido y el contenido es legible en temas claro y oscuro.
- [ ] El texto de ayuda y los mensajes de error orientan sobre el siguiente paso.

## 6. Prácticas prohibidas

1. Se prohíbe transmitir información clave solo mediante imágenes sin ofrecer alternativa textual.
2. Se prohíbe indicar estados o errores únicamente con color.
3. Se prohíbe usar textos de enlace sin significado.
4. Se prohíbe eliminar los estilos de indicación del foco sin ofrecer una alternativa.

## Archivos relacionados

- La maquetación documental se trata en la [especificación de maquetación visual del README](./readme-visual-layout-specification.md)
- Los requisitos de accesibilidad de las insignias se tratan en la [especificación de insignias](./badge-specification.md)
- Los estándares de redacción se tratan en la [especificación general de redacción](./general-writing-specification.md)
- La calidad documental corresponde a la dimensión D12, véase la [matriz de dimensiones de revisión](./review-dimension-matrix.md)
