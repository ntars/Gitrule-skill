# Plantilla de exención de responsabilidad

> Problema que resuelve este archivo: ofrece una plantilla genérica de exención de responsabilidad lista para copiar y aplicar sustituyendo los marcadores de posición, de modo que cualquier proyecto pueda delimitar con el mínimo coste la naturaleza de su contenido, sus límites de responsabilidad y las obligaciones del usuario; las instrucciones de cumplimentación y las variantes por escenario que la acompañan cubren proyectos personales, empresariales, de código abierto y de código cerrado.

## 1. Instrucciones de uso

1. Copiar todo el contenido de la sección 3 «Cuerpo de la plantilla» y crear con él un archivo `DISCLAIMER.md` en la raíz del proyecto, o integrarlo como sección independiente en `README.md`.
2. Sustituir uno por uno los `{{...}}` según la tabla de correspondencia de marcadores de posición de la sección 4; las secciones completas que no se utilicen deben eliminarse, sin dejar marcadores de posición vacíos.
3. Recortar las cláusulas según el escenario conforme a la sección 5: el software de código cerrado pone el énfasis en la sección 3.5, y los proyectos de código abierto deben conservar la explicación de la relación con la licencia de la sección 3.6.
4. Esta plantilla es un texto de referencia genérico y no constituye asesoramiento jurídico. Cuando se trate de una publicación oficial de cara al exterior, una distribución transfronteriza o un sector regulado, debe utilizarse tras la revisión jurídica correspondiente, según lo establecido en la sección 2 de la [exención de responsabilidad](./disclaimer.md).
5. Comprobaciones antes del envío: que todos los marcadores de posición se hayan sustituido, que los datos de contacto sean reales y accesibles, y que no exista conflicto con las cláusulas de la [LICENSE](../../LICENSE).

## 2. Principios de personalización

- **Primacía de la legalidad**: todas las cláusulas de exención solo surten efecto en la medida permitida por la legislación aplicable; se prohíben formulaciones absolutas como «exención incondicional de toda responsabilidad», que pueden invalidar la cláusula completa.
- **Sin extralimitación**: no deben revocarse ni reducirse los derechos concedidos por la licencia; en caso de conflicto prevalece el texto de la licencia, según el principio recogido en la [especificación de LICENSE](./license-specification.md).
- **Verificabilidad**: los datos de contacto, la fecha de entrada en vigor y el nombre del sujeto deben ser información real; se prohíbe conservar valores de ejemplo.
- **Independencia**: las cláusulas son independientes entre sí; la nulidad de una no afecta a la validez de las demás.

## 3. Cuerpo de la plantilla

El contenido que figura a partir de la sección 3.1 constituye el cuerpo de la plantilla y puede copiarse directamente.

### 3.1 Finalidad y ámbito de aplicación de la declaración

```markdown
# Exención de responsabilidad

> Esta declaración se aplica a todo el contenido publicado por {{项目名称}} (en adelante, «este proyecto»), incluidos el código fuente, la documentación, las plantillas, los ejemplos, los datos y los materiales relacionados (en adelante, «contenido del proyecto»), con independencia de que se utilice mediante lectura humana, invocación programática u otras formas.

1. Esta declaración sirve para aclarar la naturaleza del contenido del proyecto, advertir de los riesgos de uso y precisar los límites de responsabilidad; no constituye una restricción adicional de los derechos de ningún sujeto, ni supone la revocación o reducción de los derechos concedidos por la licencia del proyecto.
2. Todo sujeto que acceda, copie, cite, adapte, distribuya o utilice la totalidad o parte del contenido del proyecto (en adelante, «usuario») se considera que ha leído y comprendido esta declaración.
3. La fecha de la última actualización de esta declaración es {{更新日期}}.
```

### 3.2 Naturaleza del contenido

```markdown
## Naturaleza del contenido

1. El contenido del proyecto es {{内容性质描述}} y no representa el estándar oficial, el dictamen jurídico ni la conclusión de asesoramiento profesional de ninguna organización, sector ni jurisdicción.
2. El contenido del proyecto no ofrece compromiso alguno de aplicabilidad para ninguna pila tecnológica, entorno de ejecución o requisito de cumplimiento concreto, ni constituye asesoramiento profesional en materia jurídica, de cumplimiento, de seguridad, financiera o fiscal; cuando se trate de estas cuestiones, el usuario debería consultar por su cuenta a profesionales con la cualificación correspondiente.
3. Los ejemplos, parámetros e información estadística del contenido del proyecto solo sirven para ilustrar el método o mostrar la forma de redacción y no deben tomarse directamente como valores recomendados para entornos de producción; su validez se supedita a {{数据或示例的时点与范围说明}}.
```

### 3.3 Exención de garantías

```markdown
## Exención de garantías

En la máxima medida permitida por la ley, el contenido del proyecto se proporciona «tal cual», y {{主体名称}} no otorga garantía alguna, expresa o implícita, incluidas, entre otras:

- Que el contenido sea absolutamente exacto, completo, exento de errores u omisiones;
- Que el contenido sea adecuado para el propósito concreto, el entorno concreto o los requisitos de cumplimiento concretos del usuario;
- Que la aplicación conforme al contenido del proyecto alcance necesariamente el resultado esperado o supere necesariamente cualquier proceso de auditoría, prueba, publicación o certificación;
- Que el contenido del proyecto esté disponible de forma continuada, no se modifique o siga siendo compatible con las herramientas, plataformas o servicios de terceros que el usuario adopte posteriormente;
- Que el contenido del proyecto no infrinja derechos de terceros.
```

### 3.4 Responsabilidad del usuario

```markdown
## Responsabilidad del usuario

1. Antes de adoptar el contenido del proyecto, el usuario debería evaluar de forma independiente su aplicabilidad considerando el tipo de su proyecto, la legislación aplicable, los requisitos del sector y su capacidad de asunción de riesgos, y debería decidir por sí mismo si lo adopta, qué partes adopta y cómo las ajusta.
2. Antes de su uso, el usuario debería verificar las plantillas, configuraciones, fragmentos de scripts y parámetros, incluidas la validación sintáctica, la verificación de compilación, la verificación mediante pruebas y la revisión de seguridad; no debe aplicarlos directamente, sin verificación, en entornos de producción, servicios de cara al exterior o escenarios que impliquen datos sensibles.
3. Cuando el usuario adapte, reduzca, combine o vuelva a publicar el contenido del proyecto, debería comprobar por su cuenta si el resultado es coherente con sus necesidades y con las cláusulas aplicables, y es responsable de la documentación, la configuración y los entregables que de ello se deriven.
4. El usuario debería cumplir la legislación aplicable y el régimen interno de su jurisdicción y del sector en que se encuadra el proyecto; el contenido del proyecto no sustituye el cumplimiento de las obligaciones correspondientes.
```

### 3.5 Limitación de responsabilidad

```markdown
## Limitación de responsabilidad

1. En la máxima medida permitida por la ley, {{主体名称}} no asume responsabilidad alguna por las pérdidas, daños, responsabilidades, costes o gastos que se produzcan o se alegue que se han producido por las siguientes circunstancias, ya se basen en contrato, en ilícito civil (incluida la negligencia) o en cualquier otro fundamento jurídico, y con independencia de que se haya advertido o no al sujeto de la posibilidad correspondiente:
   - El uso, la cita, la copia, la adaptación, la distribución o la ejecución de la totalidad o parte del contenido del proyecto;
   - Las decisiones adoptadas, las acciones emprendidas o las acciones omitidas sobre la base del contenido del proyecto;
   - Los resultados de funcionamiento en el flujo de trabajo de la documentación, la configuración y las plantillas elaboradas conforme al contenido del proyecto;
   - Las interrupciones, fallos o anomalías de datos derivados de problemas de compatibilidad entre el contenido del proyecto y herramientas, plataformas o servicios de terceros;
   - La modificación, la suspensión de la puesta a disposición o el cese del mantenimiento del contenido del proyecto.
2. Las pérdidas y daños mencionados en el párrafo anterior incluyen, entre otros: daños directos, daños indirectos, daños incidentales, daños consecuenciales, daños punitivos, así como lucro cesante, pérdida de ingresos, interrupción de la actividad, pérdida o deterioro de datos, daño al fondo de comercio, costes adicionales de adquisición y reclamaciones de terceros.
3. Las cláusulas de limitación de esta declaración solo surten efecto en la medida permitida por la legislación aplicable. Si alguna jurisdicción no permite la limitación o exclusión de una responsabilidad determinada, dicha limitación no se aplicará en el ámbito de esa jurisdicción y el resto de las cláusulas seguirán siendo válidas.
```

### 3.6 Contenido de terceros y relación con la licencia

```markdown
## Contenido de terceros y relación con la licencia

1. Los enlaces externos, herramientas, servicios, iconos, tipografías y materiales citados en el contenido del proyecto son proporcionados por los terceros correspondientes y se rigen por sus propias condiciones; {{主体名称}} no asume responsabilidad alguna por su contenido, disponibilidad, exactitud, seguridad o legalidad, ni implica respaldo alguno. El usuario debería verificar por su cuenta sus condiciones y su aplicabilidad; las obligaciones de licencia de los recursos de terceros no se transfieren ni se eximen por la cita en el contenido del proyecto.
2. Este proyecto utiliza la licencia {{许可证名称及 SPDX 标识符}}, cuyo texto completo figura en [LICENSE](./LICENSE). Esta declaración es una explicación, desde la perspectiva del uso, de las cláusulas de exención de responsabilidad de la licencia, y no sustituye, modifica ni debilita las cláusulas de dicha licencia.
3. En caso de conflicto interpretativo entre esta declaración y las cláusulas de la licencia, prevalecerá el texto de la licencia. Ninguna manifestación de esta declaración debe interpretarse como un cobro, una condición o una restricción adicionales de los derechos concedidos.
4. Al volver a publicar el contenido del proyecto o contenido derivado, deberían conservarse el aviso de derechos de autor y el aviso de licencia conforme a los requisitos de la licencia, y puede adjuntarse esta declaración para que los usuarios posteriores conozcan los límites de responsabilidad.
```

### 3.7 Modificación y entrada en vigor

```markdown
## Modificación y entrada en vigor

1. Esta declaración es revisada por {{维护主体}} según las necesidades de actualización de contenido y de cumplimiento; tras la revisión prevalece la versión más reciente de {{仓库地址或发布渠道}}.
2. Esta declaración entra en vigor desde {{生效日期}}. Si el usuario continúa utilizando el contenido del proyecto tras la revisión de la declaración, se aplicará la versión revisada; si el usuario no está de acuerdo con el contenido revisado, debería cesar su uso.
3. Las cláusulas de esta declaración son independientes entre sí. La declaración de nulidad o de no exigibilidad de una cláusula no afecta a la validez de las demás.
4. Datos de contacto: {{真实可达的联系邮箱或渠道}}.
```

## 4. Tabla de correspondencia de marcadores de posición y definición de campos

| Marcador de posición | Obligatorio | Definición del campo | Ejemplo de cumplimentación |
| --- | --- | --- | --- |
| `{{项目名称}}` | Sí | Nombre público del proyecto, coherente con la primera línea del README | `FooBar` |
| `{{主体名称}}` | Sí | Denominación completa del sujeto que asume o renuncia a la responsabilidad; en proyectos personales, el nombre; en proyectos empresariales, la razón social | `某某科技有限公司` |
| `{{维护主体}}` | Sí | Organización o persona responsable de revisar la declaración | `Equipo de mantenimiento de FooBar` |
| `{{更新日期}}` | Sí | Fecha de la última revisión de esta declaración, con formato uniforme YYYY-MM-DD | `2026-11-18` |
| `{{生效日期}}` | Sí | Fecha en que esta declaración entra en vigor; puede coincidir con la fecha de actualización | `2026-11-18` |
| `{{内容性质描述}}` | Sí | Frase que explica qué es el proyecto y su grado de madurez | `Implementación de ejemplo para referencia de desarrolladores, no un componente de nivel de producción` |
| `{{数据或示例的时点与范围说明}}` | No | Momento de recopilación y ámbito de aplicación de los datos o parámetros de los ejemplos | `Estadística de octubre de 2026 sobre 120 muestras` |
| `{{许可证名称及 SPDX 标识符}}` | Sí | Nombre completo y SPDX ID de la licencia del proyecto | `Licencia MIT (MIT)` |
| `{{仓库地址或发布渠道}}` | Sí | Ubicación autorizada de la versión más reciente de la declaración | `https://github.com/owner/repo` |
| `{{真实可达的联系邮箱或渠道}}` | Sí | Dirección real por la que el usuario puede contactar con el mantenedor | `security@example.com` |

## 5. Instrucciones de cumplimentación y variantes por escenario

| Escenario | Cláusulas que deben conservarse | Cláusulas que pueden recortarse | Puntos de ajuste |
| --- | --- | --- | --- |
| Proyecto personal | 3.1 / 3.2 / 3.3 / 3.5 / 3.7 | 3.4 puede simplificarse | El nombre del sujeto debe ser el nombre real; el contacto debe ser un buzón de larga permanencia |
| Proyecto empresarial | Todas las cláusulas | Ninguna | El nombre del sujeto debe ser la razón social del registro mercantil; solo puede publicarse tras la revisión jurídica |
| Proyecto de código abierto | Todas las cláusulas, en especial la 3.6 | Ninguna | Conservar la explicación de la relación con la licencia; no deben reducirse los derechos concedidos por esta |
| Software de código cerrado | 3.1 / 3.2 / 3.3 / 3.4 / 3.5 / 3.7 | De la 3.6 pueden eliminarse los párrafos 2 a 4 | Eliminar las referencias a licencias de código abierto y sustituirlas por la referencia al contrato de licencia de usuario final |
| Prototipo experimental | 3.1 / 3.2 / 3.3 / 3.7 | 3.5 puede simplificarse | Marcar expresamente «prototipo» en la naturaleza del contenido para evitar que se tome por una versión estable |
| Tratamiento de datos personales | Todas las cláusulas | Ninguna | Añadir el rol del tratamiento de datos, el plazo de conservación y el canal de ejercicio de derechos del interesado, véase además la [especificación de seguridad y privacidad](./security-and-privacy-specification.md) |

Correspondencia de errores frecuentes:

| Redacción incorrecta | Consecuencia | Redacción correcta |
| --- | --- | --- |
| «Este proyecto no asume responsabilidad alguna» | Formulación absoluta, fácilmente declarada inválida | «En la máxima medida permitida por la ley, no asume responsabilidad...» |
| «El derecho de interpretación final corresponde al autor» | Conflictúa con la concesión de la licencia y genera controversias | «En caso de conflicto, prevalece el texto de la licencia» |
| Dejar `test@example.com` como contacto | Inaccesible; se pierde el canal de comunicación | Indicar un buzón real y de larga vigencia |
| Copiar la declaración de otro proyecto sin cambiar el sujeto | Sujeto erróneo; la declaración carece de sentido | Sustituir uno por uno los marcadores de posición y verificar la coherencia del sujeto |

## 6. Ejemplo completo

A continuación se muestra un ejemplo cumplimentado de proyecto personal de código abierto, solo como referencia de formato; no debe copiarse directamente como declaración propia.

```markdown
# Exención de responsabilidad

> Esta declaración se aplica a todo el contenido publicado por DemoCLI (en adelante, «este proyecto»), incluidos el código fuente, la documentación, las plantillas, los ejemplos, los datos y los materiales relacionados (en adelante, «contenido del proyecto»).

1. Esta declaración sirve para aclarar la naturaleza del contenido del proyecto, advertir de los riesgos de uso y precisar los límites de responsabilidad; no constituye una restricción adicional de los derechos de ningún sujeto, ni supone la revocación o reducción de los derechos concedidos por la licencia del proyecto.
2. Todo sujeto que acceda, copie, cite, adapte, distribuya o utilice la totalidad o parte del contenido del proyecto se considera que ha leído y comprendido esta declaración.
3. La fecha de la última actualización de esta declaración es 2026-11-18.

## Naturaleza del contenido

1. El contenido del proyecto es una herramienta de ejemplo de línea de comandos para referencia de desarrolladores y no representa el estándar oficial, el dictamen jurídico ni la conclusión de asesoramiento profesional de ninguna organización, sector ni jurisdicción.
2. El contenido del proyecto no ofrece compromiso alguno de aplicabilidad para ninguna pila tecnológica, entorno de ejecución o requisito de cumplimiento concreto, ni constituye asesoramiento profesional en materia jurídica, de cumplimiento, de seguridad, financiera o fiscal.
3. Los parámetros de ejemplo del contenido del proyecto solo sirven para mostrar la forma de redacción y no deben tomarse directamente como valores recomendados para entornos de producción.

## Exención de garantías

En la máxima medida permitida por la ley, Zhang San no otorga garantía alguna, expresa o implícita, incluidas, entre otras, que el contenido sea absolutamente exacto, que sea adecuado para un propósito concreto, que su aplicación alcance necesariamente el resultado esperado, que esté disponible de forma continuada y que no infrinja derechos de terceros.

## Limitación de responsabilidad

En la máxima medida permitida por la ley, Zhang San no asume responsabilidad alguna por las pérdidas derivadas del uso, la adaptación o la ejecución del contenido del proyecto, ya se basen en contrato, en ilícito civil o en cualquier otro fundamento jurídico. Si alguna jurisdicción no permite la limitación o exclusión de una responsabilidad determinada, dicha limitación no se aplicará en el ámbito de esa jurisdicción y el resto de las cláusulas seguirán siendo válidas.

## Contenido de terceros y relación con la licencia

Este proyecto utiliza la licencia MIT (MIT), cuyo texto completo figura en [LICENSE](./LICENSE). Esta declaración es una explicación, desde la perspectiva del uso, de las cláusulas de exención de responsabilidad de la licencia, y no sustituye, modifica ni debilita las cláusulas de dicha licencia; en caso de conflicto interpretativo, prevalece el texto de la licencia.

## Modificación y entrada en vigor

Esta declaración entra en vigor el 2026-11-18, es revisada por el equipo de mantenimiento de DemoCLI y prevalece la versión más reciente de https://github.com/example/democli. Las cláusulas son independientes entre sí. Datos de contacto: maintainer@example.com.
```

## Archivos relacionados

- Declaración de instancia de este proyecto: [exención de responsabilidad](./disclaimer.md)
- Reglas de licencia: [especificación de LICENSE](./license-specification.md)
- Seguridad y privacidad: [especificación de seguridad y privacidad](./security-and-privacy-specification.md)
- Conformidad de código abierto: [especificación de conformidad de código abierto](./open-source-compliance-specification.md)
- Convenciones generales de redacción: [especificación general de redacción](./general-writing-specification.md)
- Volver al índice en chino simplificado: [README](./README.md)
- Volver a la página principal del repositorio: [README](../../README.md)
