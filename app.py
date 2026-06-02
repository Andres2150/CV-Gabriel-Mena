import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =====================================================
# CONFIGURACIÓN (DEBE IR PRIMERO)
# =====================================================

st.set_page_config(
    page_title="Gabriel Mena | Business Intelligence",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# PRESENTACIÓN
# =====================================================

st.title("👨‍💼 Gabriel Mena López")

st.subheader("Business Intelligence | Data Analytics | Python")

st.write("""
Profesional orientado al análisis de datos, Business Intelligence,
automatización de reportes y análisis comercial.

Actualmente desarrollando proyectos en Python, SQL,
Machine Learning y visualización de datos.
""")

# =====================================================
# PERFIL Y HABILIDADES
# =====================================================

col1, col2 = st.columns([1,2])

with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=180
    )

with col2:

    st.markdown("### Competencias")

    st.write("SQL")
    st.progress(85)

    st.write("Python")
    st.progress(80)

    st.write("Power BI")
    st.progress(85)

    st.write("Excel")
    st.progress(90)

    st.write("Machine Learning")
    st.progress(70)

# =====================================================
# DATA PBI LATAM
# =====================================================

st.header("📈 Base de Datos PBI América Latina")

data = {
    "Country": [
        "BRAZIL","MEXICO","ARGENTINA","COLOMBIA","CHILE","PERU",
        "ECUADOR","REP_DOM","GUATEMALA","COSTA_RICA","PANAMA",
        "URUGUAY","BOLIVIA","PARAGUAY","HONDURAS",
        "EL_SALVADOR","NICARAGUA"
    ],

    2020:[1476.107,1121.065,385.741,270.348,253.88,209.984,
          95.865,78.625,77.718,62.396,57.06,
          53.557,36.897,35.432,23.35,24.921,12.73],

    2021:[1670.647,1316.569,486.564,318.525,315.457,229.832,
          107.179,95.067,86.443,64.961,67.396,
          60.742,40.701,39.951,28.146,29.043,14.208],

    2022:[1951.924,1466.935,632.79,345.632,301.227,248.204,
          116.133,113.813,95.642,69.244,76.479,
          70.6,44.329,41.953,31.425,31.87,15.634],

    2023:[2191.137,1794.41,646.075,366.292,335.518,271.78,
          121.147,120.794,104.354,86.498,83.812,
          77.997,45.464,43.118,34.356,33.854,17.813],

    2024:[2179.413,1830.489,633.267,418.818,330.267,294.675,
          124.676,124.613,113.19,95.35,86.524,
          80.961,46.967,44.458,37.1,35.365,19.694]
}

df = pd.DataFrame(data)
df = df.set_index("Country")

st.dataframe(df)

# =====================================================
# MATRIZ DE CORRELACIÓN TRIANGULAR
# =====================================================

st.header("🔍 Matriz de Correlación Triangular")

corr = df.T.corr()

mask = np.triu(np.ones_like(corr, dtype=bool))

corr_masked = corr.mask(mask)

fig, ax = plt.subplots(figsize=(10,8))

im = ax.imshow(corr_masked, aspect="auto")

ax.set_xticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=90)

ax.set_yticks(range(len(corr.columns)))
ax.set_yticklabels(corr.columns)

plt.colorbar(im)

plt.title("Correlación del PBI entre países")

st.pyplot(fig)

# =====================================================
# CONTACTO
# =====================================================

st.header("📞 Contacto")

st.write("📍 Lima, Perú")
st.write("🐙 GitHub: github.com/Andres2150")
st.write("📊 Business Intelligence & Data Analytics")

st.success("Gracias por visitar mi portafolio profesional.")
