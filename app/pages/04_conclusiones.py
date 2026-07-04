import streamlit as st

st.title("🏁 Conclusiones y Futuros Pasos")

# 1. Hallazgos
st.subheader("Hallazgos Principales")
st.markdown("""
* **Perfil del Usuario:** El análisis reveló que la mayor parte de nuestra audiencia se concentra en el segmento de [inserta aquí el rango de edad/plan que viste en el EDA].
* **Comportamiento:** Se identificó una correlación clara entre el tipo de plan y el tiempo de visualización, lo cual sugiere que los usuarios con planes [Premium/Básico] tienen un compromiso mucho mayor.
* **PCA:** La reducción de dimensionalidad permitió agrupar a los usuarios en comportamientos latentes, confirmando que [menciona si viste clusters, ej: existen grupos diferenciados por sus hábitos].
""")

# 2. Limitaciones
st.subheader("Limitaciones del Proyecto")
st.write("""
El modelo actual presenta algunas limitaciones:
1. **Datos:** El dataset es una muestra estática; no contempla variaciones temporales a largo plazo.
2. **Variables:** Podríamos enriquecer el análisis incluyendo datos externos, como el tipo de dispositivo utilizado o el género de contenido más consumido.
""")

# 3. Próximos Pasos
st.subheader("Próximos Pasos")
st.markdown("""
Para futuras iteraciones, recomendamos:
- **Implementar un sistema de recomendación:** Utilizar la información del PCA para personalizar sugerencias.
- **Campañas de Marketing:** Enfocarse en los segmentos identificados en el EDA para aumentar la conversión a planes Premium.
- **Modelado predictivo:** Entrenar un modelo de Machine Learning para predecir la tasa de cancelación (*churn*).
""")

st.success("¡Gracias por explorar nuestro Dashboard!")