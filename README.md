# PI_Mineria_Datos_1

Alumno: Francis Feijoo
Sede:Villa Ojo De Agua
Proyecto de Minería de Datos: Análisis de Usuarios de Streaming
Información general
Este proyecto presenta un análisis integral de los patrones de consumo en plataformas de streaming, utilizando técnicas de minería de datos para transformar datos crudos en conocimiento accionable.

Objetivo del proyecto
El objetivo principal es realizar una exploración profunda y una reducción de dimensionalidad sobre el comportamiento de usuarios de streaming. Buscamos identificar segmentos clave, correlaciones significativas entre variables demográficas y de consumo, y validar la estructura latente de los datos para optimizar futuras estrategias de retención. Este análisis actúa como base para la toma de decisiones basada en datos, permitiendo entender qué perfiles de usuario presentan mayor compromiso con el servicio y qué factores técnicos influyen en su permanencia.

Dataset
El dataset original se encuentra en data/raw/ y contiene información demográfica y de actividad de usuarios, incluyendo edad, plan de suscripción, país de origen, tiempo mensual de visualización, género favorito y tickets de soporte técnico. Se trata de un archivo en formato JSON que requiere procesamiento para su correcta interpretación. La calidad inicial presentaba registros con valores atípicos (edades negativas), valores nulos en variables de tiempo y falta de estandarización en categorías textuales como planes y países. El archivo resultante, tras el proceso de ETL, se encuentra en data/processed/ para su análisis.

Estructura del repositorio
/app: Código fuente de la aplicación Streamlit.

/data: Contiene subcarpetas raw/ (datos originales) y processed/ (datos limpios).

/logs: Archivo pipeline_log.csv con el registro de transformaciones ETL.

/notebooks: Notebooks de Jupyter con el flujo completo de trabajo.

/reports: Informe final en formato PDF (informe_final.pdf).

requirements.txt: Dependencias del entorno.

README.md: Documentación del proyecto.

Preparación y calidad de datos
El proceso de limpieza se encuentra documentado en logs/pipeline_log.csv. Las tareas principales incluyeron:

Lectura del archivo JSON original mediante el uso de librerías de manipulación de datos.

Normalización de variables categóricas para eliminar duplicidad por espacios, errores de escritura o diferencias en capitalización.

Filtrado de registros inválidos, específicamente eliminando usuarios con edades menores o iguales a cero.

Imputación de valores nulos en la variable de tiempo de visualización usando la mediana para preservar la distribución.

Traducción y renombramiento de columnas al español para asegurar la consistencia en los informes.

Estandarización de escalas para variables numéricas, permitiendo que algoritmos de Machine Learning operen correctamente.

Resumen del análisis exploratorio
Se realizó un EDA para comprender las distribuciones univariadas, las relaciones bivariadas y las dependencias multivariadas. Observamos que el plan de suscripción tiene una relación directa con el tiempo de visualización, indicando niveles de engagement diferenciados según el tipo de plan. El análisis de correlación permitió detectar relaciones lineales entre las variables numéricas, revelando qué factores, como el rango etario, influyen más en el volumen de tickets de soporte generados. Las visualizaciones permiten concluir que existen grupos de usuarios con comportamientos homogéneos claramente identificables.

Reducción de dimensionalidad
Para reducir la complejidad del dataset, se aplicó la técnica de Análisis de Componentes Principales (PCA). Tras escalar los datos, se seleccionaron los dos componentes principales que explican la mayor parte de la varianza del sistema. Este proceso facilitó la visualización de la estructura de los datos en un plano 2D, permitiendo identificar la formación de clusters naturales en los hábitos de consumo de los usuarios, lo cual simplifica la interpretación de variables múltiples hacia factores de comportamiento más generales.

Visualización interactiva
La aplicación desarrollada en Streamlit permite navegar por todas las etapas del análisis, desde el dataset procesado hasta los hallazgos del EDA y PCA. Accede a la aplicación aquí: https://pimineriadatos1-z7n4gimetkp58bxjdutics.streamlit.app/

Cómo ejecutar localmente
Clonar el repositorio: git clone https://github.com/Talkiaooo/PI_Mineria_Datos_1/

Crear un entorno virtual: python -m venv .venv

Activar el entorno e instalar dependencias: pip install -r requirements.txt

Ejecutar la aplicación: streamlit run app/Home.py

Conclusiones
El proyecto permitió confirmar que el comportamiento del usuario no es aleatorio, sino que responde a segmentos claramente definidos por su plan y actividad. El PCA validó la existencia de grupos latentes, sugiriendo que las estrategias de marketing deberían personalizarse según estos clusters. Como limitación, se identifica que el dataset es una muestra estática, omitiendo posibles cambios estacionales o de tendencia a largo plazo. Se recomienda integrar más variables de contexto en futuras iteraciones para robustecer el sistema. Consulta el informe detallado en reports/informe_final.pdf para una visión ejecutiva.
