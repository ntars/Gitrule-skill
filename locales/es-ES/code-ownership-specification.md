# Especificación de propiedad del código

> Problema que resuelve este archivo: define la sintaxis del archivo `.github/CODEOWNERS`, la asignación de propiedad y las reglas de enrutamiento de revisiones, para que cada cambio se asigne automáticamente a revisores con responsabilidad sobre él.

## 1. Principios de diseño

1. **Correspondencia explícita entre ruta y persona**: cada regla indica quién es responsable de una ruta, evitando revisiones sin responsable o revisiones duplicadas.
2. **Owners mínimos necesarios**: los propietarios de una ruta deben limitarse a 1–3 personas; un número excesivo diluye la responsabilidad.
3. **Cobertura por defecto**: debe establecerse un propietario global por defecto que cubra las rutas no coincidentes con reglas explícitas.
4. **Sincronización con la estructura del equipo**: debe actualizarse cuando cambien los miembros para evitar que cuentas inactivas bloqueen las revisiones.

## 2. Ubicación del archivo y sintaxis

### 2.1 Rutas

El archivo `CODEOWNERS` puede ubicarse en cualquiera de las siguientes ubicaciones, tomándose la primera coincidencia por prioridad:

1. `CODEOWNERS` en la raíz del repositorio;
2. `docs/CODEOWNERS`;
3. `.github/CODEOWNERS` (recomendado).

### 2.2 Reglas de sintaxis

```text
# 注释以 # 开头
<路径模式>  <所有者>  [<所有者>...]
```

- Cada línea contiene una regla; al patrón de ruta le siguen uno o varios propietarios.
- El formato del propietario es `@usuario` o `@organización/equipo`.
- El uso de un correo electrónico como propietario exige que esté asociado a una cuenta de GitHub.
- Las rutas distinguen mayúsculas de minúsculas y admiten los comodines `*` y `**`.

### 2.3 Ejemplo

```text
# 默认所有者
*                       @org/maintainers

# 按目录分配
/src/core/              @org/core-team
/src/api/               @org/api-team @alice
/docs/                  @org/docs-team

# 按文件类型分配
*.md                    @org/docs-team
/.github/workflows/      @org/devops-team
```

## 3. Reglas de coincidencia

1. Solo surte efecto la última regla coincidente, sin acumulación; por ello, las reglas generales deben escribirse antes y las específicas después.
2. Una regla de directorio coincide con ese directorio y sus subdirectorios, salvo que comience por `/`, lo que restringe la ruta a la raíz.
3. El orden de las reglas determina la prioridad y debe ir de lo general a lo específico.
4. Las rutas sin coincidencia quedan bajo la responsabilidad del propietario por defecto.

## 4. Estrategia de asignación de propiedad

| Dimensión | Criterio de asignación |
| --- | --- |
| Directorio | Asignación según los límites de módulos o subsistemas |
| Tipo de archivo | La documentación, la configuración y las pruebas pueden asignarse de forma unificada por tipo |
| Rutas críticas | Seguridad, publicación y configuración de CI quedan en exclusiva de los mantenedores principales |
| Nuevos miembros | Participan primero como revisores no obligatorios y pasan a propietarios formales tras familiarizarse |

## 5. Vinculación con el flujo de revisión

1. Al crear un PR, GitHub solicita automáticamente la revisión de los propietarios de las rutas coincidentes.
2. La exigencia de revisión obligatoria se configura mediante reglas de protección de ramas, según la [especificación de flujo de trabajo de Git y ramas](./git-workflow-and-branching-specification.md).
3. Los propietarios deben responder dentro del plazo acordado; si lo superan, la responsabilidad pasa al propietario por defecto.
4. Los cambios de propietario deben reflejarse en el archivo para evitar que cuentas inactivas bloqueen el flujo (véase la [especificación de revisión de código](./code-review-specification.md)).

## 6. Requisitos de mantenimiento

1. Debe revisarse una vez tras cada cambio de estructura organizativa o de responsabilidades del equipo.
2. Ante la transferencia del repositorio o la salida de un miembro, debe eliminarse de inmediato el propietario correspondiente.
3. Todo cambio del archivo debe ser revisado por al menos un propietario actual, para impedir la expansión autónoma de permisos.
4. No deben asignarse propietarios a cuentas inactivas ni a cuentas de bot (salvo las dedicadas a automatización).

## 7. Prácticas prohibidas

1. Se prohíbe el uso de reglas comodín demasiado amplias que conviertan a todos en propietarios.
2. Se prohíbe asignar rutas sensibles (publicación, configuración de claves) a miembros sin capacidad de revisión.
3. Se prohíbe incluir datos de contacto personales en el archivo.
4. Se prohíbe mantener a largo plazo la propiedad de miembros que ya han dejado el proyecto.

## Archivos relacionados

- Límites de responsabilidad de los archivos: [matriz de documentación](./document-matrix.md)
- Criterios y responsabilidades de revisión: [especificación de revisión de código](./code-review-specification.md)
- Protección de ramas: [especificación de flujo de trabajo de Git y ramas](./git-workflow-and-branching-specification.md)
- Las comprobaciones automatizadas pertenecen a la dimensión D9: [matriz de dimensiones de revisión](./review-dimension-matrix.md)
