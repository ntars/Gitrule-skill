# Especificación de métricas de calidad

> Problema que resuelve este archivo: define indicadores de calidad rastreables y su método de cálculo, para evitar evaluar la calidad de un proyecto con cifras sin fundamento.

## 1. Principios de los indicadores

1. Los indicadores deben ser medibles y reproducibles, y deben indicar el modo de recogida y el criterio estadístico.
2. Los indicadores sirven para mejorar, no para clasificar sin más ni para generar presión.
3. Cada indicador debe indicar su valor objetivo y su valor actual, y debe revisarse periódicamente.

## 2. Indicadores recomendados

| Categoría | Indicador | Descripción del criterio |
| --- | --- | --- |
| Pruebas | Cobertura de pruebas | Proporción de líneas de código cubiertas; debe indicarse la herramienta de medición |
| Pruebas | Tasa de éxito de las pruebas | Casos superados / casos totales |
| Compilación | Tasa de éxito de la compilación | Compilaciones correctas / compilaciones totales |
| Defectos | Densidad de defectos | Número de defectos detectados por unidad de tamaño de código |
| Defectos | Tiempo medio de corrección | Tiempo medio transcurrido desde la detección hasta la corrección completa |
| Rendimiento | Tiempo de respuesta | Debe precisarse el escenario y el percentil (por ejemplo, P95) |
| Dependencias | Número de vulnerabilidades graves | Cantidad de vulnerabilidades graves en dependencias sin corregir |

## 3. Reglas obligatorias

1. Los indicadores de rendimiento deben indicar el entorno y el método de prueba; se prohíben las cifras sin condiciones (en correspondencia con la [especificación general de redacción](./general-writing-specification.md)).
2. La recogida de datos de los indicadores debe ser automatizada, para reducir el sesgo de la medición manual.
3. Las anomalías de los indicadores deben tener un registro de seguimiento e incorporarse a la [especificación de la hoja de ruta](./roadmap-specification.md) o al seguimiento de problemas.

## Archivos relacionados

- Para la puerta de calidad, véase la [puerta de calidad](./quality-gate.md)
- Para los requisitos de pruebas, véase la [especificación de pruebas](./testing-specification.md)
- Para la redacción de la sección de rendimiento, véase la [especificación de secciones del README](./readme-sections-specification.md)
