# PI_Mineria_Datos_1

## Información general
Proyecto integrador de Minería de Datos 1. Análisis de comportamiento de usuarios de plataforma streaming.

Integrantes: Francis Feijoo.

Sede: Villa Ojo De Agua.

Fecha: 04/07/2026.

Enlace al repositorio: https://github.com/Talkiaooo/PI_Mineria_Datos_1)

Enlace a Streamlit Cloud: [Link a tu app]


## Objetivo del proyecto
Analizar el comportamiento de usuarios de una plataforma de streaming mediante técnicas de minería de datos, identificando patrones de consumo, calidad de datos y reducción de dimensionalidad para facilitar la toma de decisiones.

## Dataset
Dataset compuesto por registros de usuarios con variables como edad, plan de suscripción, tiempo de visualización, país, género favorito, último acceso y tickets de soporte. Contiene 80 registros con variaciones en formatos de texto y valores atípicos.

## Estructura del repositorio
- /data/raw: Datos originales.
- /data/processed: Datos limpios.
- /notebooks: Desarrollo secuencial.
- /app: Aplicación Streamlit.
- /reports: Informe final PDF.
- /logs: Registro ETL.

## Preparación y calidad de datos
Se normalizaron textos en `subscription_plan`, `country` y `favorite_genre`. Se eliminaron registros con edad igual a 0 y se imputaron nulos en `monthly_watch_time_mins` mediante la mediana. Se descartaron fechas futuras no válidas. El proceso se registró en `logs/pipeline_log.csv`.

## Resumen del análisis exploratorio
El EDA reveló una concentración de usuarios en el plan básico, con una alta dispersión en el tiempo de visualización. Se observaron diferencias regionales en las preferencias de género, donde el drama y el thriller predominan en la mayoría de los mercados analizados.

## Reducción de dimensionalidad
Se aplicó PCA sobre variables numéricas tras estandarización con StandardScaler. Se seleccionaron 2 componentes principales que explican la mayor parte de la varianza, permitiendo visualizar clústeres de comportamiento de usuarios.

## Conclusiones
El análisis confirmó que el plan de suscripción y la edad están correlacionados con el tiempo de visualización. El PCA permitió identificar grupos de usuarios con comportamiento homogéneo. Futuras mejoras incluyen la incorporación de datos temporales detallados.
