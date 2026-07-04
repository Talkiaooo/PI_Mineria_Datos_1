import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data

st.title("📊 Análisis Exploratorio de Datos (EDA)")
df = load_data()

# 1. Univariadas
st.subheader("1. Distribución de Planes de Suscripción")
fig1, ax1 = plt.subplots()
sns.countplot(x='Plan de Suscripción', data=df, palette='viridis', ax=ax1)
st.pyplot(fig1)
st.write("**Interpretación:** Observamos qué plan tiene mayor volumen de usuarios, lo que permite identificar el segmento principal de la plataforma.")

st.subheader("2. Distribución de Edad de los Usuarios")
fig2, ax2 = plt.subplots()
sns.histplot(df['Edad'], bins=20, kde=True, color='skyblue', ax=ax2)
st.pyplot(fig2)
st.write("**Interpretación:** Este histograma muestra el rango etario predominante, ayudando a perfilar la audiencia objetivo.")

# 2. Bivariadas
st.subheader("3. Minutos de Visualización según Plan")
fig3, ax3 = plt.subplots()
sns.boxplot(x='Plan de Suscripción', y='Minutos de Visualización', data=df, ax=ax3)
st.pyplot(fig3)
st.write("**Interpretación:** Comparamos el engagement entre planes. Si el plan Premium tiene una mediana superior, indica mayor fidelización.")

st.subheader("4. Edad vs. Minutos de Visualización")
fig4, ax4 = plt.subplots()
sns.scatterplot(x='Edad', y='Minutos de Visualización', data=df, hue='Plan de Suscripción', ax=ax4)
st.pyplot(fig4)
st.write("**Interpretación:** Identificamos si existe una correlación entre la edad y el consumo de tiempo, segmentado por tipo de suscripción.")

# 3. Multivariada
st.subheader("5. Correlación entre Variables Numéricas")
# Seleccionamos solo columnas numéricas para la matriz
df_numeric = df.select_dtypes(include=['number'])
fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.heatmap(df_numeric.corr(), annot=True, cmap='coolwarm', ax=ax5)
st.pyplot(fig5)
st.write("**Interpretación:** Esta matriz permite ver relaciones lineales entre todas las variables numéricas (como Edad vs Tickets de Soporte), detectando posibles dependencias ocultas.")