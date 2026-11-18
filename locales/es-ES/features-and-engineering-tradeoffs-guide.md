# Redacción de características y decisiones de ingeniería

> Problema que resuelve este archivo: define la redacción de los capítulos «Características principales» y «Detalles de diseño y decisiones de ingeniería» del README, y presenta respectivamente la estructura en cinco partes de las características y las diez categorías de cobertura obligatoria de las decisiones de ingeniería.

## 1. Redacción de las características principales

Cada característica se redacta según la siguiente estructura en cinco partes; si falta cualquiera de ellas, no debe listarse como característica.

1. **Nombre de la característica**: no más de 15 caracteres, mediante sintagma nominal.
2. **Valor**: el problema concreto que resuelve y las consecuencias de no resolverlo.
3. **Forma de implementación**: la tecnología, el mecanismo o el algoritmo empleados, indicando archivos o funciones clave.
4. **Diferenciación**: las dimensiones de comparación frente a las soluciones habituales, que deben ser dimensiones evaluables objetivamente.
5. **Evidencia**: datos de pruebas, resultados de referencia, ubicación en el código, opciones de configuración o pasos reproducibles.

Restricciones:
1. La evidencia debe ser reproducible; las características que no puedan aportar evidencia se marcan como «【pendiente: forma de verificación】» y no debe sustituirse por descripciones cualitativas.
2. La evidencia de rendimiento debe indicar el entorno y el método de prueba.
3. El objeto de comparación debe ser una solución con nombre; no deben usarse referencias vagas como «las soluciones tradicionales» u «otras herramientas».

## 2. Redacción de los detalles de diseño y las decisiones de ingeniería

Cada entrada se redacta según la estructura de tres partes «escenario → forma de tratamiento → motivo», explicando por qué se diseñó así y no de otra manera.

Categorías de cobertura obligatoria:
1. Entradas anómalas y casos límite (valores nulos, longitud excesiva, caracteres ilegales, valores numéricos extremos)
2. Estrategias de tiempo de espera, reintento, retroceso progresivo, corte de circuito y degradación
3. Niveles de caché, estrategias de invalidación, protección frente a penetración y avalancha de caché
4. Control de concurrencia, granularidad de bloqueos, consistencia de datos e idempotencia
5. Optimización de memoria y almacenamiento (procesamiento por lotes, lectura y escritura en flujo, compresión)
6. Medidas de seguridad (autenticación y autorización, limitación de tasa, validación de entrada, enmascaramiento de información sensible)
7. Detalles de interacción (prevención de errores, confirmación secundaria, reversibilidad, estados de carga y estados vacíos)
8. Criterio de los valores de los parámetros por defecto
9. Estrategias de compatibilidad hacia atrás y adaptación multiplataforma
10. Tratamiento de redes deficientes y modo sin conexión, recuperación de estado

## Archivos relacionados

- Corresponden a los capítulos 4 y 5 del README; véase [Especificación de secciones del README](./readme-sections-specification.md)
- La redacción de datos de rendimiento debe respetar los requisitos de exactitud; véase [Especificación general de redacción](./general-writing-specification.md)
- La evidencia de características y la cobertura de decisiones pertenecen a las puertas G4/G5; véase [Puertas de calidad](./quality-gate.md)
