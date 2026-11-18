# Especificación de gestión de dependencias

> Problema que resuelve este archivo: define las plantillas y los campos de la solicitud de incorporación de dependencias, el inventario de dependencias, el bloqueo y la actualización, para garantizar compilaciones reproducibles, dependencias trazables y conformidad de licencias.

## 1. Artículos de la especificación

1. La incorporación de una nueva dependencia debe explicar su propósito, licencia y estado de mantenimiento (véase la [especificación de conformidad de código abierto](./open-source-compliance-specification.md)).
2. Deben preferirse dependencias con licencia compatible y comunidad activa; se prohíbe incorporar dependencias de origen desconocido o licencia incierta.
3. La versión de las dependencias debe registrarse en el lockfile y versionarse en el repositorio para garantizar compilaciones reproducibles en un entorno limpio (corresponde a la regla absoluta H9 y a la dimensión D5).
4. El número de versión debe fijar la versión realmente resuelta; no deben usarse expresiones de rango como entrega final.
5. La actualización de dependencias debe apoyarse en herramientas automatizadas y, tras la actualización, debe superar la CI; las vulnerabilidades deben tratarse a tiempo o registrarse con medidas de mitigación.
6. El inventario de dependencias debe mantenerse coherente con el NOTICE (véase la [especificación de NOTICE](./notice-specification.md)).

## 2. Plantilla de solicitud de incorporación de dependencias

```markdown
## Solicitud de incorporación de dependencias: {{包名}}

- Número de solicitud: {{DEP-NNN}}
- Solicitante: {{姓名}}
- Propósito: {{一句话说明解决什么问题}}
- ¿Es posible implementarlo internamente?: {{是 / 否；是则说明为何仍引入}}
- Evaluación de alternativas: {{已评估的替代包及未选原因}}

| Campo | Valor |
| --- | --- |
| Nombre del paquete | {{包名}} |
| Versión incorporada | {{精确版本号}} |
| Licencia | {{SPDX ID}} |
| Compatibilidad de licencia | {{兼容 / 不兼容 / 需法务确认}} |
| Última publicación | {{YYYY-MM-DD}} |
| Estado de mantenimiento | {{活跃 / 低频 / 停滞}} |
| Descargas semanales | {{数值}} |
| Número de dependencias transitivas | {{数值}} |
| Vulnerabilidades conocidas | {{无 / CVE 编号与处置}} |
| Impacto en el tamaño del paquete | {{增量 KB}} |

- Conclusión: {{批准 / 拒绝 / 有条件批准}}
- Aprobador: {{姓名}}
```

## 3. Plantilla de inventario de dependencias

```markdown
# Inventario de dependencias: {{项目名称}}

Fecha de actualización: {{YYYY-MM-DD}} ｜ lockfile: {{路径}} ｜ Herramienta de generación: {{工具与版本}}

| Dependencia | Versión incorporada | Versión bloqueada | Tipo | Licencia | Propósito | Última revisión |
| --- | --- | --- | --- | --- | --- | --- |
| {{包名}} | {{^1.2.0}} | {{1.2.3}} | Directa / Transitiva | {{MIT}} | {{用途}} | {{YYYY-MM-DD}} |

## Registro de actualizaciones
| Fecha | Dependencia | Cambio de versión | Motivo | Resultado de la verificación |
| --- | --- | --- | --- | --- |
| {{YYYY-MM-DD}} | {{包名}} | {{1.2.2 → 1.2.3}} | {{安全修复}} | {{CI 全绿}} |

## Excepciones y mitigación
| Dependencia | Problema | Medida de mitigación | Fecha de reexamen |
| --- | --- | --- | --- |
| {{包名}} | {{漏洞 / 停滞}} | {{限制使用范围}} | {{YYYY-MM-DD}} |
```

## 4. Definición de campos

| Campo | Obligatorio | Tipo | Puntos de cumplimentación | Ejemplo |
| --- | --- | --- | --- | --- |
| Número de solicitud | Sí | `DEP-NNN` | Consecutivo, sin reutilización | `DEP-007` |
| Propósito | Sí | Texto | Explicar el problema que resuelve; se prohíbe «facilitar el desarrollo» | `Analizar la configuración TOML` |
| Evaluación de alternativas | Sí | Texto | Evaluar al menos 1 alternativa | `Se evaluó toml-js y se descartó por mantenimiento estancado` |
| Versión incorporada | Sí | Versión exacta | No deben usarse `^` ni `~` | `1.2.3` |
| Versión bloqueada | Sí | Versión exacta | Coherente con el lockfile | `1.2.3` |
| Licencia | Sí | SPDX ID | Coherente con la [especificación de LICENSE](./license-specification.md) | `MIT` |
| Estado de mantenimiento | Sí | Enumeración | Activo / Baja frecuencia / Estancado, con base de determinación | `Activo (commits en los últimos 30 días)` |
| Número de dependencias transitivas | Sí | Numérico | Si es excesivo, deben explicarse el tamaño y el impacto de riesgo | `12` |
| Vulnerabilidades conocidas | Sí | Texto | Si no hay, escribir «ninguna»; no debe dejarse vacío | `Ninguna` |
| Fecha de reexamen | Sí | Fecha | Las excepciones deben tener fecha de reexamen | `2026-12-31` |

## 5. Instrucciones de cumplimentación

1. **Evaluación de implementación interna**: primero debe responderse «¿puede resolverse con la biblioteca estándar o con capacidades existentes?»; si se incorpora pese a poder implementarse internamente, deben explicarse los motivos.
2. **Licencia**: debe ser un SPDX ID; `UNLICENSED` y las licencias personalizadas deben pasar a «requiere confirmación jurídica» y no deben incorporarse directamente.
3. **Estado de mantenimiento**: debe basarse en la fecha de la última publicación y en la respuesta a los issues; se prohíbe «parece que alguien lo mantiene».
4. **Bloqueo de versión**: en la entrega, el lockfile debe contener la versión exacta resuelta; `package.json` puede conservar expresiones de rango, pero el lockfile debe ser exacto.
5. **Ritmo de actualización**: la actualización automatizada debe estar activada y la fusión confirmarse manualmente; cada actualización debe superar la CI y verificar los cambios de licencia.
6. **Tratamiento de vulnerabilidades**: debe priorizarse la actualización a una versión segura; cuando no sea posible, deben indicarse la medida de mitigación y la fecha de reexamen, e incorporarse al registro de riesgos de la [especificación de respuesta a incidentes](./incident-response-specification.md).
7. **Sincronización del inventario**: tras incorporar o retirar una dependencia deben actualizarse el inventario y el NOTICE; los tres elementos (lockfile, inventario y NOTICE) deben ser coherentes.

Errores frecuentes:

| Redacción incorrecta | Problema | Forma de corrección |
| --- | --- | --- |
| «Usar una biblioteca para gestionar la configuración» | Sin nombre de paquete ni propósito concreto | Indicar nombre, versión y problema que resuelve |
| Licencia «código abierto» | No permite determinar la compatibilidad | Indicar el SPDX ID |
| Lockfile no versionado | Compilación no reproducible | Versionar el lockfile (corresponde a H9) |
| Número de dependencias transitivas vacío | Riesgo invisible | Indicar el valor concreto |
| Vulnerabilidad sin medida de mitigación | Riesgo sin seguimiento | Añadir medida y fecha de reexamen |

## 6. Ejemplo completo

```markdown
## Solicitud de incorporación de dependencias: remark

- Número de solicitud: DEP-001
- Solicitante: Wang Wu
- Propósito: servir como capa de análisis de Markdown y sustentar la localización de nodos que requiere el motor de reglas (REQ-001, REQ-004).
- ¿Es posible implementarlo internamente?: No; una implementación interna no cubriría los casos límite de GFM dentro del límite de esfuerzo disponible.
- Evaluación de alternativas: se evaluó marked, descartado por su insuficiente capacidad de localización de nodos en chino.

| Campo | Valor |
| --- | --- |
| Nombre del paquete | remark |
| Versión incorporada | 15.0.1 |
| Licencia | MIT |
| Compatibilidad de licencia | Compatible |
| Última publicación | 2026-11-02 |
| Estado de mantenimiento | Activo (commits en los últimos 30 días) |
| Descargas semanales | 4.200.000 |
| Número de dependencias transitivas | 18 |
| Vulnerabilidades conocidas | Ninguna |
| Impacto en el tamaño del paquete | +42 KB |

- Conclusión: Aprobada, se implementa junto con ADR-0002
- Aprobador: Li Si
```

## Archivos relacionados

- Determinación de compatibilidad de licencias: [especificación de conformidad de código abierto](./open-source-compliance-specification.md)
- Anotación SPDX de licencias: [especificación de LICENSE](./license-specification.md)
- Coherencia del NOTICE: [especificación de NOTICE](./notice-specification.md)
- La compilación reproducible pertenece a la dimensión D5: [matriz de dimensiones de revisión](./review-dimension-matrix.md)
- La actualización automatizada pertenece a la dimensión D9: [matriz de dimensiones de revisión](./review-dimension-matrix.md)
- Pruebas y tratamiento de vulnerabilidades: [especificación de pruebas](./testing-specification.md), [especificación de seguridad y privacidad](./security-and-privacy-specification.md)
- Vinculación con las decisiones de arquitectura: [especificación de documentos de diseño de arquitectura](./architecture-design-document-specification.md)
