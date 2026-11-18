# Plantilla de SECURITY

> Problema que resuelve este archivo: ofrece una plantilla de política de seguridad lista para copiar, con la que un proyecto puede generar su `SECURITY.md` y definir las versiones soportadas, los canales de notificación de vulnerabilidades, el proceso de respuesta y los principios de divulgación; las instrucciones de cumplimentación que la acompañan cubren la elección del canal de notificación y el tratamiento de información sensible.

## 1. Instrucciones de uso

1. Copiar todo el contenido de la sección 3 «Cuerpo de la plantilla» y crear con él un archivo `SECURITY.md` en la raíz del proyecto.
2. Sustituir los marcadores de posición según la sección 4; el canal de notificación debe ser una dirección real, accesible y que no exponga públicamente la superficie de ataque.
3. Recortar según el escenario conforme a la sección 5: los proyectos que no mantienen varias versiones deben eliminar de la tabla de versiones soportadas las filas de versiones antiguas.
4. Para las reglas de seguridad y los requisitos sobre información sensible, véase la [especificación de seguridad y privacidad](./security-and-privacy-specification.md); para la dimensión de gobernanza comunitaria, véase la [matriz de dimensiones de revisión](./review-dimension-matrix.md).

## 2. Principios de personalización

- **Prioridad de los canales privados**: la notificación de vulnerabilidades debe realizarse por canales privados; no debe exigirse a quien informa que revele detalles en un issue público.
- **Plazos explícitos**: deben indicarse los intervalos de primera respuesta y de corrección para evitar compromisos indefinidos.
- **Minimización de la información**: debe pedirse a quien informa únicamente la información mínima necesaria para reproducir el problema; no debe permitirse el envío de datos reales de producción.
- **Coherencia legal**: los principios de divulgación deben ser coherentes con la legislación aplicable y las políticas de la plataforma; en sectores regulados deben someterse a revisión jurídica.

## 3. Cuerpo de la plantilla

```markdown
# Política de seguridad

> Este archivo describe el alcance de soporte de seguridad de {{项目名称}} y la forma de notificar vulnerabilidades, y está dirigido a investigadores de seguridad, contribuyentes y usuarios.

## Versiones soportadas

| Versión | ¿Se aceptan informes de seguridad? |
| --- | --- |
| {{当前版本}} | Sí |
| {{上一版本}} | {{是否接受}} |
| Versiones anteriores | No |

## Canales de notificación

No deben notificarse vulnerabilidades de seguridad a través de issues públicos, foros de discusión o canales sociales. Debe utilizarse alguno de los siguientes canales privados:

- Correo de seguridad: {{真实可达的安全邮箱}}
- Portal de notificación privada: {{私有漏洞报告地址}}

Si no se dispone de los canales anteriores, debe contactarse con el mantenedor mediante {{备用私有联系方式}}.

## Contenido del informe

Para mejorar la eficiencia del tratamiento, debe aportarse en la medida de lo posible:

- Las versiones y los componentes afectados;
- El tipo de vulnerabilidad y su impacto potencial;
- Los pasos mínimos de reproducción o una prueba de concepto;
- La dirección de corrección sugerida (opcional).

No deben enviarse datos reales de producción, claves ni información de identidad personal.

## Proceso de respuesta

| Etapa | Plazo | Descripción |
| --- | --- | --- |
| Confirmación de recepción | {{首次响应时限}} | El mantenedor confirma la recepción del informe |
| Evaluación inicial | {{评估时限}} | Se determina si se trata de un problema de seguridad y su alcance de impacto |
| Corrección y verificación | {{修复时限}} | Se completa y verifica la corrección; los problemas complejos se negocian por separado |
| Divulgación pública | {{发布延迟}} tras la corrección | Se publica el aviso de seguridad y la versión corregida |

## Principios de divulgación

- El mantenedor mantendrá la confidencialidad sobre la identidad de quien informa y el contenido del informe hasta la publicación de la corrección.
- Sin el consentimiento del mantenedor, quien informa no debe divulgar los detalles de la vulnerabilidad antes de la publicación de la corrección.
- Tras la publicación de la corrección, el mantenedor reconocerá públicamente a quien informó en el aviso de seguridad (con su consentimiento).
- Las investigaciones de seguridad realizadas de buena fe y conformes con esta política no darán lugar a reclamación alguna.

## Excepciones y exención de responsabilidad

Esta política no constituye un compromiso de garantía de seguridad alguna; el contenido del proyecto se ofrece «tal cual», según se detalla en la [exención de responsabilidad](./DISCLAIMER.md) y la [LICENSE](./LICENSE).
```

## 4. Tabla de correspondencia de marcadores de posición y definición de campos

| Marcador de posición | Obligatorio | Definición del campo | Ejemplo de cumplimentación |
| --- | --- | --- | --- |
| `{{项目名称}}` | Sí | Nombre público del proyecto | `FooBar` |
| `{{当前版本}}` | Sí | Versión más reciente en mantenimiento o `main` | `v2.3.0` |
| `{{上一版本}}` | No | Versión anterior que aún se mantiene | `v2.2.x` |
| `{{是否接受}}` | Sí | Si esa versión acepta informes de seguridad | `Sí` |
| `{{真实可达的安全邮箱}}` | Sí | Buzón dedicado a informes de seguridad | `security@example.com` |
| `{{私有漏洞报告地址}}` | Sí | Portal de notificación privada | `https://github.com/owner/repo/security/advisories/new` |
| `{{备用私有联系方式}}` | No | Vía alternativa cuando el canal principal no está disponible | `Mensaje privado a la cuenta del mantenedor` |
| `{{首次响应时限}}` | Sí | Plazo para confirmar la recepción del informe | `3 días hábiles` |
| `{{评估时限}}` | Sí | Plazo para completar la evaluación inicial | `7 días hábiles` |
| `{{修复时限}}` | Sí | Plazo para completar la corrección | `30 días` |
| `{{发布延迟}}` | Sí | Intervalo hasta la divulgación pública tras la corrección | `7 días` |

## 5. Instrucciones de cumplimentación y variantes por escenario

| Escenario | Secciones que deben conservarse | Secciones que pueden recortarse | Puntos de ajuste |
| --- | --- | --- | --- |
| Proyecto de una sola versión | Canales de notificación, contenido del informe, proceso de respuesta, principios de divulgación | En la tabla de versiones soportadas, eliminar las filas de versiones antiguas | Indicar `main` o el tag más reciente como versión actual |
| Mantenimiento de varias versiones | Todas | Ninguna | Enumerar fila por fila las versiones que aún aceptan informes |
| Proyecto personal | Todas | La tabla de versiones soportadas puede simplificarse | Usar como canal privado un buzón de larga permanencia |
| Proyecto empresarial | Todas | Ninguna | Los plazos deben ser coherentes con el régimen interno de seguridad y someterse a revisión jurídica |
| Sector regulado | Todas | Ninguna | Añadir las obligaciones de notificación regulatoria y los requisitos de conservación de datos |

Correspondencia de errores frecuentes:

| Redacción incorrecta | Consecuencia | Redacción correcta |
| --- | --- | --- |
| «Notifiquen las vulnerabilidades en un Issue» | Divulgación pública de detalles y ampliación del riesgo | Usar un canal privado |
| «Lo atenderemos lo antes posible» | Sin expectativa definida; quien informa no puede evaluar | Indicar plazos por etapas |
| Plazo «corrección en 24 horas» | Compromiso excesivo e incumplible | Indicar un plazo razonable y señalar que los problemas complejos se negocian por separado |
| No exigir la anonimización | Quien informa podría enviar datos reales de producción | Prohibir expresamente el envío de datos reales y claves |

## 6. Ejemplo completo

A continuación se muestra un ejemplo cumplimentado del párrafo de canales de notificación, solo como referencia de formato.

```markdown
## Canales de notificación

No deben notificarse vulnerabilidades de seguridad a través de issues públicos, foros de discusión o canales sociales. Debe utilizarse alguno de los siguientes canales privados:

- Correo de seguridad: security@example.com
- Portal de notificación privada: https://github.com/example/democli/security/advisories/new

No deben enviarse datos reales de producción, claves ni información de identidad personal.
```

## Archivos relacionados

- Especificación correspondiente: [especificación de seguridad y privacidad](./security-and-privacy-specification.md)
- Plantillas complementarias: [plantilla de código de conducta](./code-of-conduct-template.md), [plantilla de guía de contribución](./contribution-guide-template.md), [plantilla de exención de responsabilidad](./disclaimer-template.md)
- Dimensión de notificación de vulnerabilidades: [matriz de dimensiones de revisión](./review-dimension-matrix.md)
- Tratamiento de incidentes de filtración de claves: [especificación de push y publicación](./push-and-release-specification.md)
- Volver al índice en chino simplificado: [README](./README.md)
