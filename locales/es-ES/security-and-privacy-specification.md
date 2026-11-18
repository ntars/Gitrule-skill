# Especificación de seguridad y privacidad

> Problema que resuelve este archivo: define la protección de información sensible, el inventario de privacidad de datos, la plantilla de SECURITY.md y los campos de notificación de vulnerabilidades, para garantizar que no haya filtraciones antes de la publicación, que el tratamiento de datos sea conforme y que los canales de vulnerabilidades sean accesibles.

## 1. Artículos de la especificación

1. No deben commitearse claves, tokens, claves privadas, archivos `.env`, claves AK/SK de proveedores cloud ni cadenas de conexión a bases de datos (corresponde a la regla absoluta H3).
2. El escaneo de claves debe abarcar el árbol de trabajo y el historial completo, y ejecutarse antes del push (véase la [especificación de push y publicación](./push-and-release-specification.md)).
3. Los dominios internos, las direcciones IP, los datos personales y los residuos en registros deben depurarse antes de la publicación (corresponde a la dimensión D1).
4. Si una clave ya se ha pusheado, debe rotarse de inmediato y depurarse el historial; no debe limitarse a un commit de eliminación (corresponde a H12).
5. Debe indicarse qué datos se recogen, con qué finalidad, dónde se almacenan y durante cuánto tiempo se conservan; el transporte y el almacenamiento se cifran y la visualización se anonimiza.
6. El modelo de permisos sigue el principio de mínimo privilegio necesario; los casos con datos transfronterizos deben evaluarse por separado.
7. Debe ofrecerse un canal de notificación de vulnerabilidades que llegue directamente al mantenedor, con compromiso de confidencialidad y plazo de respuesta; los riesgos conocidos se explican con veracidad y no se promete seguridad absoluta.

## 2. Plantilla de autocomprobación de información sensible

```markdown
# Autocomprobación de información sensible: {{项目名称}}

Fecha de comprobación: {{YYYY-MM-DD}} ｜ Ejecutor: {{姓名}} ｜ Historial cubierto: {{是 / 否}}

| Elemento de comprobación | Herramienta / comando | Resultado | Tratamiento |
| --- | --- | --- | --- |
| Claves en el árbol de trabajo | {{扫描工具}} | {{命中数}} | {{已清理 / 无}} |
| Claves en los commits históricos | {{扫描工具 --all}} | {{命中数}} | {{已轮换 / 无}} |
| Archivos `.env` y de credenciales | `git ls-files \| grep -E ...` | {{文件数}} | {{已移除 / 无}} |
| Dominios / IP internos | {{检索命令}} | {{命中数}} | {{已替换 / 无}} |
| Datos personales | {{检索命令}} | {{命中数}} | {{已脱敏 / 无}} |
| Residuos en registros e instantáneas | {{检查命令}} | {{命中数}} | {{已清理 / 无}} |

Conclusión: {{通过 / 不通过}}
- Lista de claves rotadas: {{无 / 列出}}
- Revisor: {{姓名}}
```

## 3. Plantilla de inventario de privacidad de datos

```markdown
# Inventario de privacidad de datos: {{项目名称}}

## Elementos de datos
| Elemento de datos | Finalidad de la recogida | Forma de recogida | Ubicación de almacenamiento | Plazo de conservación | Cifrado | Anonimización | Cesión a terceros |
| --- | --- | --- | --- | --- | --- | --- | --- |
| {{如邮箱}} | {{账号识别}} | {{用户填写}} | {{数据库字段}} | {{删除账号后 30 天}} | {{是}} | {{展示时掩码}} | {{无}} |

## Modelo de permisos
| Rol | Datos accesibles | Base del permiso | Periodicidad de revisión |
| --- | --- | --- | --- |
| {{角色}} | {{最小必要范围}} | {{业务需要}} | {{每季度}} |

## Evaluación de cumplimiento
- Normativa aplicable por región: {{列举}}
- Transferencia transfronteriza de datos: {{无 / 评估结论与措施}}
- Respuesta a los derechos del usuario: {{查询 / 更正 / 删除的渠道与时限}}
```

## 4. Plantilla de SECURITY.md

```markdown
# Política de seguridad

## Versiones soportadas
| Versión | ¿Se aceptan informes de seguridad? |
| --- | --- |
| {{最新主版本}} | Sí |
| {{旧版本}} | No / Solo problemas graves |

## Canales de notificación
- Preferente: {{私密渠道，如 GitHub Security Advisories}}
- Alternativo: {{加密邮箱}}
- No notifique vulnerabilidades mediante un issue público.

## Compromisos de respuesta
| Etapa | Plazo |
| --- | --- |
| Confirmación de recepción | {{2 个工作日}} |
| Confirmación inicial | {{5 个工作日}} |
| Corrección y divulgación | {{视严重程度，目标 30 天}} |

## Proceso de tratamiento
Recepción → Confirmación → Corrección → Divulgación → Anuncio

## Riesgos conocidos
{{如实说明当前已知风险；无则写「暂无已知风险」，不得承诺绝对安全}}
```

## 5. Definición de campos

| Campo | Obligatorio | Tipo | Puntos clave de cumplimentación | Ejemplo |
| --- | --- | --- | --- | --- |
| Cobertura del historial | Sí | Enumeración | Debe elegirse «sí» para poder determinar la superación | `是` |
| Elemento de comprobación.Resultado | Sí | Valor numérico | Se indica el número de coincidencias; se prohíbe «probablemente no hay» | `0` |
| Lista de claves rotadas | Obligatorio condicional | Lista | Obligatorio si hay claves detectadas; enumera las credenciales rotadas | `API_KEY 已轮换` |
| Elemento de datos.Plazo de conservación | Sí | Texto | Duración concreta; no puede escribirse «a largo plazo» | `账号删除后 30 天` |
| Elemento de datos.Cesión a terceros | Sí | Texto | Si no existe, se escribe «ninguna» | `无` |
| Versiones soportadas | Sí | Tabla | Indica qué versiones aceptan informes | `2.x：是` |
| Canal de notificación | Sí | Texto | Al menos un canal no público | `Security Advisories` |
| Plazo de respuesta | Sí | Duración | Cada etapa tiene un valor numérico | `2 个工作日` |

## 6. Instrucciones de cumplimentación

1. **Escaneo del historial**: el escaneo de claves debe incluir el historial de git completo; escanear solo el árbol de trabajo se considera inválido.
2. **Claves detectadas**: ante una clave ya pusheada, primero se rota y después se depura el historial; el orden no puede invertirse (corresponde a H12).
3. **Anonimización**: los campos sensibles que aparecen en la visualización y en los registros deben enmascararse; se prohíbe imprimir tokens, números de documento de identidad o números de teléfono completos.
4. **Plazo de conservación**: «conservación indefinida» no es aceptable; debe indicarse un plazo concreto o un evento que desencadene la eliminación.
5. **Versiones soportadas**: deben listarse al menos la versión principal actual; si las versiones antiguas no están soportadas, debe indicarse expresamente para evitar notificaciones erróneas de los usuarios.
6. **Canal de notificación**: debe ser un canal no público; revelar vulnerabilidades en un issue público amplía el riesgo.
7. **Riesgos conocidos**: deben enumerarse con veracidad; «este sistema es absolutamente seguro» es una formulación prohibida.

Errores frecuentes:

| Redacción errónea | Problema | Corrección |
| --- | --- | --- |
| Eliminar el commit con la clave sin rotarla | Infringe H12 | Rotar primero y después depurar el historial |
| Autocomprobación que solo escanea el árbol de trabajo | Se pasan por alto filtraciones en el historial | Añadir el escaneo del historial |
| Conservación de datos indicada como «permanente» | Sin límite | Indicar un plazo concreto |
| Vulnerabilidades por issue público | Amplía la superficie expuesta | Cambiar a un canal privado e indicarlo en SECURITY.md |
| Prometer «seguridad absoluta» | Formulación falsa | Sustituirla por una exposición veraz de los riesgos conocidos |

## 7. Ejemplo completo

```markdown
### Autocomprobación de información sensible: markdown-lint-cli

Fecha de comprobación: 2026-11-18 ｜ Ejecutor: Wang Wu ｜ Historial cubierto: sí

| Elemento de comprobación | Herramienta / comando | Resultado | Tratamiento |
| --- | --- | --- | --- |
| Claves en el árbol de trabajo | gitleaks detect | 0 | Ninguna |
| Claves en los commits históricos | gitleaks detect --log-opts=--all | 0 | Ninguna |
| Archivos `.env` y de credenciales | git ls-files | 0 | Ninguno |
| Dominios / IP internos | Búsqueda con expresión regular | 0 | Ninguno |

Conclusión: superado
- Lista de claves rotadas: ninguna
- Revisor: Li Si
```

## Archivos relacionados

- Líneas rojas sobre claves H3/H12: [reglas absolutas](./hard-rules.md)
- Tratamiento de incidentes con claves ya filtradas: [especificación de respuesta a incidentes](./incident-response-specification.md)
- Ejecución del escaneo antes del push: [especificación de push y publicación](./push-and-release-specification.md)
- Anonimización de registros: [especificación de observabilidad](./observability-specification.md)
- Límites de la documentación SECURITY: [matriz de documentación](./document-matrix.md)
- Exposición de riesgos conocidos en el README: [especificación de secciones del README](./readme-sections-specification.md)
- Acuerdos de conducta comunitaria: [especificación de código de conducta](./code-of-conduct-specification.md)
