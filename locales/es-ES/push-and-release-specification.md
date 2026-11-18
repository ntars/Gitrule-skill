# Especificación de push y publicación

> Problema que resuelve este archivo: define la lista de acciones antes, durante y después del push, las reglas de tag y publicación, el flujo de tratamiento de incidentes, así como la guía completa de push a GitHub y la matriz de resolución de fallos.

## 1. Antes del push

1. `git status` está limpio y no hay archivos sensibles sin seguimiento.
2. `git log` no contiene WIP, ni `fix bug`, ni filtraciones de datos personales.
3. Se confirma que `.gitignore` surte efecto y que los artefactos y las dependencias no están bajo seguimiento.
4. La compilación, las pruebas y el lint pasan en local.
5. Se ejecuta un escaneo completo de secretos (incluidos los commits históricos).
6. La matriz de documentación está completa (véase [Matriz de documentación](./document-matrix.md)).

## 2. Acciones de push

7. Se hace push de la rama personal: `git push -u origin feat/xxx`.
8. La línea principal solo avanza mediante PR, nunca con push directo.
9. Se prohíbe `push --force`; para reescribir la propia rama se usa `--force-with-lease`.
10. Se prohíbe hacer rebase o amend sobre ramas públicas ya enviadas con push.
11. Los archivos individuales de más de 50 MB pasan primero por LFS y luego se envían.
12. Antes del primer push se confirma la visibilidad del repositorio: por defecto private; solo se cambia a public si realmente debe ser público.

## 3. Tag y publicación

13. El formato del tag es `vMAJOR.MINOR.PATCH` y debe ser annotated: `git tag -a v1.0.0 -m "release: 1.0.0"`.
14. El tag solo se crea cuando la CI está en verde y las Release Notes están listas.
15. Los cambios que rompen la compatibilidad deben usar `feat!:` o `BREAKING CHANGE:` y ofrecer en el CHANGELOG la forma de migrar.

## 4. Fase 6 · Después del push (Post-Push)

- Crear el tag anotado;
- Escribir las Release Notes;
- Verificar que las insignias y los enlaces funcionan;
- Confirmar que la CI está en verde;
- Confirmar que la información de la sección About es correcta (description / topics / enlaces / social preview).

## 5. Tratamiento de incidentes

16. **Secreto ya enviado con push**: rotación inmediata → limpieza con `git filter-repo` → el push forzado a una rama protegida requiere el procedimiento de administrador → anuncio público.
17. **Archivo grande enviado por error**: migración a LFS o reescritura del historial; no basta con borrar el archivo.

## 6. Especificación de la guía de push a GitHub

La guía debe contener las siete partes siguientes, con versiones completas y ejecutables de los comandos.

### 6.1 Seguridad previa

1. Antes del push deben respaldarse por completo el repositorio local y el remoto; se recomienda `git clone --mirror` para generar una copia espejo.
2. Confirmar que el repositorio remoto no tiene colaboradores o que se les ha avisado para que pausen sus push.
3. Confirmar que la rama de destino no tiene activada la protección contra push forzado.

### 6.2 Orden del entorno local

```bash
git status
git diff --name-status HEAD
git ls-files
```

Se contrastan las tres salidas para confirmar que los cambios pendientes coinciden con el directorio local y que no quedan archivos temporales, artefactos de compilación ni documentos de versiones anteriores. `.gitignore` debe cubrir los artefactos de compilación y los archivos de configuración locales.

### 6.3 Verificación de coherencia

```bash
git fetch origin
git diff --name-status HEAD origin/{{分支名}}
```

Este comando lista las diferencias entre los archivos remotos y los locales. Los archivos que existen en el remoto y se han eliminado en local deben eliminarse con `git rm` y luego confirmarse con un commit, para que la eliminación entre en el historial de versiones.

### 6.4 Commit y push

```bash
git add -A
git commit -m "docs: 重建项目文档（README、README_EN、NOTICE）"
git push --force-with-lease origin {{分支名}}
```

Se emplea `--force-with-lease` en lugar de `--force`, de modo que el push se rechaza si en el remoto existen nuevos commits de otras personas, evitando sobrescribir su trabajo. Eliminar el repositorio remoto y recrearlo es una operación de alto riesgo que solo se usa en repositorios personales y cuando ya se ha hecho la copia espejo; la guía debe marcar de forma explícita el riesgo de pérdida de datos.

### 6.5 Verificación posterior al push

```bash
git ls-remote --heads origin
gh repo view --web
```

En la interfaz web se confirma uno por uno que la lista de archivos, el renderizado del README, los enlaces de cambio de idioma y el enlace a NOTICE son válidos.

### 6.6 Matriz de resolución de fallos

| Tipo de error | Manifestación típica | Solución | Advertencia de riesgo |
| --- | --- | --- | --- |
| Fallo de autenticación | `Authentication failed`, `Permission denied (publickey)` | Cambiar de HTTPS a SSH y configurar la clave, o usar `gh auth login` antes del push | Ninguno |
| Corte de red | `Failed to connect`, `RPC failed` | Cambiar de red, configurar un proxy, ejecutar `git config --global http.postBuffer 524288000` | Ninguno |
| Archivo sobredimensionado | `remote: error: File exceeds 100 MB` | Quitar el archivo grande del historial de commits o activar Git LFS | Tras reescribir el historial debe avisarse a los colaboradores para que vuelvan a clonar |
| Conflicto de mayúsculas y minúsculas | Nombres de archivo con distinto uso de mayúsculas que generan entradas duplicadas | Corregir con `git mv` y confirmar con un commit | Ninguno |
| Conflicto de historial | `non-fast-forward`, `fetch first` | Preferir `git pull --rebase`; si de verdad hay que sobrescribir, usar `--force-with-lease` | Sobrescribir commits de otras personas no tiene vuelta atrás |
| Protección de rama | `protected branch hook declined` | Fusionar mediante el flujo de PR o pedir al administrador que ajuste temporalmente la regla | Todo ajuste de reglas debe quedar registrado |
| Repositorio dañado | `fatal: not a git repository`, objetos ausentes | Volver a clonar y luego copiar los cambios del directorio de trabajo | Debe respaldarse antes el directorio de trabajo |

### 6.7 Reversión

Si tras completar el push se detecta un problema, se usa `git revert` para generar un commit inverso; no debe volver a hacerse un push forzado que sobrescriba un historial ya público.

## Archivos relacionados

- Antes del push deben superarse las tres capas de la [Puerta de calidad](./quality-gate.md)
- Las líneas rojas sobre secretos y archivos grandes aparecen en H3/H5/H12 de [Reglas absolutas](./hard-rules.md)
- La especificación de mensajes de commit corresponde a la dimensión D7, véase [Matriz de dimensiones de revisión](./review-dimension-matrix.md)
- Las responsabilidades del documento de publicación `docs/release.md` se detallan en [Matriz de documentación](./document-matrix.md)
