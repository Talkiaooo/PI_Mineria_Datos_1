import sys
import os
import streamlit as st

# Esto añade la carpeta 'app/' al camino de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import load_data
from utils import load_data

st.title("📂 Descripción del Dataset")

# 1. Cargar datos
df = load_data()

# 2. Descripción general
st.subheader("Resumen del Conjunto de Datos")
st.markdown("""
Este conjunto de datos contiene información sobre los usuarios de nuestra plataforma de streaming,
incluyendo detalles sobre sus planes, comportamiento de visualización y datos demográficos.
""")

# 3. Métricas de Calidad
st.subheader("Calidad de los Datos")
col1, col2 = st.columns(2)
col1.metric("Total de Registros", len(df))
col2.metric("Valores Nulos", df.isnull().sum().sum())

st.write("Tras el proceso de limpieza (ETL), se eliminaron registros con edades inválidas (0) y se imputaron los valores faltantes en tiempo de visualización utilizando la mediana.")

# 4. Vista previa
st.subheader("Vista Previa (Primeras 10 filas)")
st.dataframe(df.head(10))

# 5. Diccionario de datos (Muy valorado por profesores)
st.subheader("Diccionario de Variables")
st.table(pd.DataFrame({
    "Variable": ["Edad", "Plan de Suscripción", "Minutos de Visualización", "País", "Género Favorito"],
    "Descripción": ["Edad del usuario", "Tipo de suscripción (Básico, Estándar, Premium)", 
                    "Minutos consumidos al mes", "País de residencia", "Género preferido"]
}))