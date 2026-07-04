import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from utils import load_data

st.title("📉 Análisis de Componentes Principales (PCA)")

df = load_data()

# 1. Preparación: Seleccionamos solo columnas numéricas
df_num = df.select_dtypes(include=['number'])

# 2. Escalamiento (CRUCIAL para PCA)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_num)

# 3. Aplicar PCA
pca = PCA(n_components=2)
components = pca.fit_transform(df_scaled)
df_pca = pd.DataFrame(data=components, columns=['PC1', 'PC2'])

# 4. Resultados
st.subheader("Varianza Explicada")
varianza = pca.explained_variance_ratio_
st.write(f"Varianza explicada por PC1: {varianza[0]:.2%}")
st.write(f"Varianza explicada por PC2: {varianza[1]:.2%}")
st.write(f"**Varianza acumulada:** {sum(varianza):.2%}")

# 5. Visualizaciones (Máximo 2 permitidas)
st.subheader("Gráfico de Componentes Principales")
fig, ax = plt.subplots()
ax.scatter(df_pca['PC1'], df_pca['PC2'], alpha=0.5)
ax.set_xlabel('Componente Principal 1')
ax.set_ylabel('Componente Principal 2')
st.pyplot(fig)

st.write("**Interpretación:** El PCA nos permite visualizar la estructura de los datos en dos dimensiones. Si observas grupos (clusters) definidos, indica que hay patrones subyacentes claros en el comportamiento de los usuarios.")