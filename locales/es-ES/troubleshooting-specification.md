# Especificación de resolución de problemas

> Problema que resuelve este archivo: define la estructura del documento de resolución de problemas (Troubleshooting / FAQ), la forma de redactar las entradas y el mecanismo de mantenimiento, de modo que los usuarios puedan localizar la causa a partir del síntoma y resolver por sí mismos los problemas frecuentes.

## 1. Ámbito de aplicación

Debe ofrecerse un documento de resolución de problemas en los casos siguientes:

1. El fallo de instalación o de compilación tiene varias causas frecuentes.
2. Existen conflictos entre opciones de configuración y el mensaje de error no basta para explicar la solución.
3. Hay limitaciones conocidas en una plataforma o versión concreta.
4. Los usuarios plantean repetidamente el mismo tipo de pregunta y la respuesta puede estandarizarse.

## 2. Ubicación y denominación del archivo

1. Si el contenido es escaso, se incluye como una sección del README titulada «Preguntas frecuentes» o «Resolución de problemas».
2. Si el contenido es abundante, se crea un archivo propio `docs/troubleshooting.md` o `FAQ.md` y el README conserva un enlace de entrada.
3. Los problemas se agrupan por tema, por ejemplo «instalación», «configuración», «ejecución», «rendimiento», «red».

## 3. Estructura del documento

1. **Introducción**: alcance de los problemas frecuentes que cubre el documento y versiones aplicables.
2. **Índice de problemas**: títulos de los problemas ordenados por tema, con salto rápido.
3. **Entradas de problema**: cada una desarrollada con una estructura uniforme.
4. **Si el problema persiste**: remisión a los canales de ayuda, como issues o el foro de discusión.

## 4. Estructura de una entrada

Cada entrada de problema debe contener las partes siguientes:

| Parte | Contenido | Requisito |
| --- | --- | --- |
| Síntoma | Manifestación concreta que ve el usuario | Incluir el mensaje de error completo; no basta con escribir «da error» |
| Condición desencadenante | Cuándo aparece | Precisar versión, plataforma y operación |
| Causa | Causa raíz | Explicar el mecanismo, no solo dar la conclusión |
| Solución | Pasos ejecutables | Enumerados y numerados, con comandos o configuración |
| Verificación | Cómo confirmar que se ha corregido | Ofrecer la salida esperada |
| Relación | Enlaces a documentación o issues relacionados | Opcional |

## 5. Ejemplo de redacción de una entrada

```markdown
### Al instalar aparece `EACCES: permission denied`

**Síntoma**: al ejecutar `npm install -g <package>` se indica que los permisos son insuficientes.

**Condición desencadenante**: instalación global como usuario normal en Linux o macOS.

**Causa**: el permiso de escritura del directorio de instalación global pertenece al administrador del sistema y el usuario actual no puede escribir en él.

**Solución**:

```bash
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
npm install -g <package>
```

**Verificación**: si al ejecutar `<package> --version` se imprime el número de versión, la operación se ha realizado correctamente.

## 6. Requisitos de redacción

1. El título del problema debe usar la expresión que buscaría el usuario, no terminología interna.
2. El mensaje de error se conserva tal cual para que el usuario pueda compararlo; la información sensible debe anonimizarse (véase [Especificación de seguridad y privacidad](./security-and-privacy-specification.md)).
3. La solución ofrece el comando completo y no da por hecho que el usuario ya ha definido variables de entorno.
4. Una entrada resuelve un solo problema y no combina varias causas.
5. Cuando se trata de un defecto conocido, se indica el alcance del impacto y la forma de evitarlo, sin prometer plazos de corrección.
6. Los problemas relacionados con la migración enlazan a la guía de migración (véase [Especificación de la guía de migración](./migration-guide-specification.md)).

## 7. Mecanismo de mantenimiento

1. Cuando la misma pregunta se plantea más de tres veces, debe añadirse o reescribirse la entrada.
2. Tras una actualización de versión se revisan todas las entradas y se elimina el contenido que haya quedado obsoleto.
3. Cada entrada puede indicar la última versión en la que se verificó, para juzgar si sigue siendo aplicable.
4. El índice de problemas se actualiza de forma sincronizada con el alta y la baja de entradas.

## 8. Prácticas prohibidas

1. Se prohíbe convertir el documento de resolución de problemas en una presentación de funcionalidades.
2. Se prohíben respuestas sin valor diagnóstico, como «reinicia e inténtalo de nuevo».
3. Se prohíbe omitir el mensaje de error y la condición desencadenante.
4. Se prohíbe conservar entradas ya corregidas o que hayan quedado obsoletas.

## Archivos relacionados

- Pertenencia de la sección del README: véase el capítulo 15 de [Especificación de secciones del README](./readme-sections-specification.md)
- Requisitos de divulgación de problemas conocidos: véase el capítulo 15 de [Especificación de secciones del README](./readme-sections-specification.md)
- Problemas de actualización: [Especificación de la guía de migración](./migration-guide-specification.md)
- Canales de recogida de problemas: [Especificación de plantillas de Issue y PR](./issue-and-pr-template-specification.md)
- La calidad de la documentación corresponde a la dimensión D12, véase [Matriz de dimensiones de revisión](./review-dimension-matrix.md)
