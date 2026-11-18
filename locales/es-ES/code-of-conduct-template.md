# Plantilla de código de conducta

> Problema que resuelve este archivo: ofrece una plantilla de código de conducta lista para copiar, con la que el proyecto puede generar su `CODE_OF_CONDUCT.md` y precisar el compromiso de participación, los comportamientos esperados, los comportamientos inaceptables, la responsabilidad de aplicación y los canales de denuncia; las instrucciones de cumplimentación que la acompañan cubren la procedencia de la adaptación y la declaración de versión.

## 1. Instrucciones de uso

1. Copiar todo el contenido de la sección 3 «Cuerpo de la plantilla» y crear con él un archivo `CODE_OF_CONDUCT.md` en la raíz del proyecto.
2. Sustituir los marcadores de posición conforme a la sección 4; el canal de denuncia debe ser una dirección real y accesible.
3. Si se adopta o adapta un código de conducta con versión propia, debe declararse la versión y la licencia en la sección 5 según los requisitos de la fuente; para la base, véase el punto 8 de la sección 1 de la [especificación del código de conducta](./code-of-conduct-specification.md).
4. Enlazar este archivo desde la [plantilla de guía de contribución](./contribution-guide-template.md) y desde la sección de contribución del README, manteniendo la accesibilidad en ambos sentidos.

## 2. Principios de personalización

- **Independiente de la tecnología**: el código no contiene contenido técnico y solo regula las normas de comportamiento en la participación; sus límites figuran en la [matriz de documentación](./document-matrix.md).
- **Ejecutable**: el tratamiento por niveles debe indicar las condiciones de activación y las medidas; se prohíbe enunciar solo principios sin consecuencias.
- **Accesibilidad**: el canal de denuncia debe ser real y efectivo; se prohíbe dejar direcciones de ejemplo.
- **Fuente conforme**: al adaptar un código de terceros deben conservarse sus requisitos de atribución y licencia; véase la [especificación de conformidad de código abierto](./open-source-compliance-specification.md).

## 3. Cuerpo de la plantilla

```markdown
# Código de conducta

## Nuestro compromiso

Como participantes, contribuidores y mantenedores de {{项目名称}}, nos comprometemos a crear conjuntamente un entorno de participación abierto, acogedor y libre de acoso, con independencia de la edad, la complexión física, la discapacidad, la etnia, la identidad y expresión de género, el nivel de experiencia, la formación académica, la posición socioeconómica, la nacionalidad, la apariencia física o la orientación sexual.

## Ámbito de aplicación

Este código se aplica a los espacios del proyecto, los issues, las solicitudes de extracción, la revisión de código, los canales sociales y los actos públicos en los que una persona actúe como representante del proyecto.

## Comportamientos esperados

- Respetar los distintos puntos de vista y experiencias, y comunicarse de buena fe.
- Aceptar las críticas constructivas y centrarse en el problema y no en la persona.
- Atender al interés común de la comunidad y evitar perjudicar al proyecto y a sus participantes.
- Ser paciente con las personas recién llegadas y ofrecer sugerencias de mejora que puedan llevarse a la práctica.

## Comportamientos inaceptables

- Ataques personales, comentarios insultantes o despectivos.
- Comentarios discriminatorios y acoso basados en cualquier característica protegida.
- Acoso público o privado, seguimiento y contacto persistente sin consentimiento.
- Publicación no autorizada de información privada de terceros.
- Cualquier otro comportamiento que pueda considerarse razonablemente inapropiado en un entorno profesional.

## Responsabilidad de aplicación

Los mantenedores del proyecto son responsables de aclarar la aplicación de este código, dirimir las infracciones y tienen facultad para eliminar, editar o rechazar contenido que no se ajuste a él. Los mantenedores deben ejercer sus funciones de forma coherente e imparcial, y deben apartarse voluntariamente de cualquier controversia en la que estén implicados.

## Medidas de actuación

Las infracciones se tratan por niveles según su gravedad:

| Nivel | Supuestos de aplicación | Medida |
| --- | --- | --- |
| Nivel uno (Correction) | Falta de intención ofensiva, incorrección leve | Aviso y aclaración en privado |
| Nivel dos (Warning) | Repetición o infracción manifiesta | Advertencia pública y plazo para subsanar |
| Nivel tres (Temporary Ban) | Acoso grave o ataque malintencionado | Suspensión temporal del permiso de participación |
| Nivel cuatro (Permanent Ban) | Conducta grave persistente o irreparable | Expulsión permanente con conservación de registro |

## Canal de denuncia

Si se sufre o se detecta un comportamiento contrario a este código, debe contactarse con el equipo de mantenimiento a través de {{真实可达的举报邮箱或渠道}}. Todas las denuncias se tratarán de forma confidencial y los mantenedores no deben revelar la identidad de la persona denunciante a la persona denunciada, salvo consentimiento expreso de aquella.

## Atribución y procedencia

{{准则来源声明}}
```

## 4. Tabla de correspondencia de marcadores de posición y definición de campos

| Marcador de posición | Obligatorio | Definición del campo | Ejemplo de cumplimentación |
| --- | --- | --- | --- |
| `{{项目名称}}` | Sí | Nombre público del proyecto, coherente con la primera línea del README | `FooBar` |
| `{{真实可达的举报邮箱或渠道}}` | Sí | Dirección real por la que puede contactarse con los mantenedores | `conduct@example.com` |
| `{{准则来源声明}}` | Sí | Si es original, indicar «original»; si es adaptado, indicar el nombre de la fuente, la versión y la licencia | `Adaptado de Contributor Covenant 2.1 (CC BY 4.0)` |

## 5. Instrucciones de cumplimentación y variantes por escenario

| Escenario | Puntos de ajuste |
| --- | --- |
| Proyecto personal | El mantenedor se identifica con su propio nombre; el canal de denuncia debe ser un buzón de larga permanencia |
| Proyecto empresarial | Debe precisarse que el sujeto de aplicación es el departamento jurídico o el equipo de comunidad; las medidas de actuación deben ser coherentes con el régimen interno |
| Adopción de un código reconocido | Debe conservarse su texto original completo y su versión, y solo añadirse el canal de denuncia y la atribución |
| Proyecto multilingüe | Las cláusulas de cada versión lingüística deben corresponderse una a una; debe indicarse cuál es la versión autoritativa (la inglesa o la china) |

Correspondencia de errores frecuentes:

| Redacción incorrecta | Consecuencia | Redacción correcta |
| --- | --- | --- |
| Escribir solo «se agradece una comunicación cordial» | No hay base de aplicación y no puede dirimirse en caso de controversia | Enumerar los comportamientos esperados, los inaceptables y el tratamiento por niveles |
| Dejar un buzón de ejemplo como canal de denuncia | Inaccesible; el mecanismo de denuncia queda inoperante | Indicar una dirección real y de larga vigencia |
| Adaptar un código sin atribución | Infringe los requisitos de licencia de la fuente | Declarar la fuente, la versión y la licencia |

## 6. Ejemplo completo

A continuación se muestra un extracto de un escenario de adaptación, solo como referencia de formato.

```markdown
## Canal de denuncia

Si se sufre o se detecta un comportamiento contrario a este código, debe contactarse con el equipo de mantenimiento a través de conduct@example.com. Todas las denuncias se tratarán de forma confidencial.

## Atribución y procedencia

Este código se ha adaptado de Contributor Covenant 2.1 y se distribuye bajo la licencia CC BY 4.0.
```

## Archivos relacionados

- Especificación correspondiente: [especificación del código de conducta](./code-of-conduct-specification.md)
- Plantillas complementarias: [plantilla de guía de contribución](./contribution-guide-template.md), [plantilla de SECURITY](./security-template.md)
- Dimensión de gobernanza comunitaria: [matriz de dimensiones de revisión](./review-dimension-matrix.md)
- Volver al índice en chino simplificado: [README](./README.md)
