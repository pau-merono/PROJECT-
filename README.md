# PROJECT TECNOLOGIA-
# Análisis de Factores que Afectan la Fertilidad Masculina

## Introducción
Este estudio analiza la relación entre diversos factores sociodemográficos, ambientales, estado de salud y hábitos de vida con la calidad del semen en una muestra de 100 voluntarios. Las muestras fueron analizadas siguiendo los criterios de la OMS 2010 para determinar la concentración espermática.

## Dataset
### Descripción General
- **Tamaño de la muestra**: 100 voluntarios
- **Variables**: 9 características + 1 variable objetivo
- **Tipo**: Datos multivariant
- **Área**: Salud y Medicina
- **Tareas asociadas**: Clasificación y Regresión
- **Valores perdidos**: No

### Variables del Estudio
1. **Estación** (-1, -0.33, 0.33, 1)
   - Invierno, Primavera, Verano, Otoño
   
2. **Edad** (normalizada entre 0 y 1)
   - Rango: 18-36 años

3. **Enfermedades Infantiles** (0, 1)
   - Incluye: varicela, sarampión, paperas, polio
   - 1: Sí, 0: No

4. **Accidentes o Traumas Graves** (0, 1)
   - 1: Sí, 0: No

5. **Intervenciones Quirúrgicas** (0, 1)
   - 1: Sí, 0: No

6. **Fiebres Altas en el Último Año** (-1, 0, 1)
   - -1: Hace menos de 3 meses
   - 0: Hace más de 3 meses
   - 1: No

7. **Consumo de Alcohol** (normalizado entre 0 y 1)
   - Frecuencia desde "varias veces al día" hasta "casi nunca o nunca"

8. **Hábito de Fumar** (-1, 0, 1)
   - -1: Nunca
   - 0: Ocasional
   - 1: Diario

9. **Horas Sentado por Día** (normalizado entre 0 y 1)
   - Rango: 1-16 horas

### Variable Objetivo
- **Diagnóstico**:
  - N: Normal
  - O: Alterado

## Objetivos del Análisis
1. Identificar los factores más influyentes en la calidad del semen
2. Analizar las correlaciones entre las variables
3. Desarrollar modelos predictivos para clasificar la calidad del semen
4. Proporcionar insights sobre los factores de riesgo modificables

## Metodología
El análisis se realizará siguiendo estos pasos:
1. Preprocesamiento y limpieza de datos
2. Análisis exploratorio de datos (EDA)
3. Análisis estadístico
4. Modelado predictivo
5. Interpretación de resultados
