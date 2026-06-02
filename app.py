import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==================================================
# CONFIGURACIÓN
# ==================================================

st.set_page_config(
    page_title="Gabriel Mena Portfolio",
    page_icon="📊",
    layout="wide"
)

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("📂 Menú")

pagina = st.sidebar.radio(
    "Seleccione una sección:",
    ["🏠 Inicio", "👨‍💼 Currículum", "📊 Proyecto PBI LATAM"]
)

# ==================================================
# PORTADA
# ==================================================

if pagina == "🏠 Inicio":

    st.title("📊 Portafolio Profesional")

    st.subheader("Gabriel Mena López")

    st.write("""
    Bienvenido a mi portafolio profesional desarrollado en Streamlit.

    En este sitio encontrará:

    ✅ Mi perfil profesional

    ✅ Experiencia en Business Intelligence

    ✅ Conocimientos en Python, SQL y Power BI

    ✅ Proyecto de análisis económico de América Latina

    Utilice el menú lateral izquierdo para navegar.
    """)

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=250
    )

# ==================================================
# CURRICULUM
# ==================================================

elif pagina == "👨‍💼 Currículum":

    st.title("👨‍💼 Gabriel Mena López")

    st.subheader(
        "Business Intelligence | Data Analytics | Python"
    )

    col1, col2 = st.columns([1,2])

    with col1:
        st.image(
            "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
            width=200
        )

    with col2:

        st.markdown("""
        ### Perfil Profesional

        Profesional orientado al análisis de datos,
        Business Intelligence y automatización de reportes.

        Experiencia en monitoreo de información,
        indicadores de gestión y análisis comercial.
        """)

    st.header("💼 Experiencia")

    st.write("""
    **OSINERGMIN**

    - Monitoreo de información.
    - Elaboración de reportes.
    - Validación de datos.
    - Atención de usuarios.
    - Seguimiento de indicadores.
    """)

    st.header("🛠 Habilidades")

    st.write("Excel")
    st.progress(90)

    st.write("Power BI")
    st.progress(85)

    st.write("SQL")
    st.progress(85)

    st.write("Python")
    st.progress(80)

    st.write("Machine Learning")
    st.progress(70)

    st.header("🎓 Formación")

    st.write("""
    - Diplomado en Business Intelligence
    - Python para Ciencia de Datos
    - Power BI
    - Análisis Comercial
    - Inteligencia Artificial
    """)

# ==================================================
# PROYECTO PBI LATAM
# ==================================================

elif pagina == "📊 Proyecto PBI LATAM":

    st.title("📊 Proyecto: PBI de América Latina")

    st.write("""
    Análisis exploratorio del Producto Bruto Interno
    de países latinoamericanos.
    """)

    data = {
        "Country": [
            "BRAZIL","MEXICO","ARGENTINA","COLOMBIA",
            "CHILE","PERU","ECUADOR","URUGUAY"
        ],

        2020:[1476,1121,385,270,253,209,95,53],
        2021:[1670,1316,486,318,315,229,107,60],
        2022:[1951,1466,632,345,301,248,116,70],
        2023:[2191,1794,646,366,335,271,121,77],
        2024:[2179,1830,633,418,330,294,124,80]
    }

    df = pd.DataFrame(data)
    df = df.set_index("Country")

    st.subheader("Base de datos")

    st.dataframe(df)

    st.subheader("Matriz de correlación")

    corr = df.T.corr()

    mask = np.triu(
        np.ones_like(corr, dtype=bool)
    )

    corr_mask = corr.mask(mask)

    fig, ax = plt.subplots(figsize=(8,6))

    im = ax.imshow(corr_mask)

    ax.set_xticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=90)

    ax.set_yticks(range(len(corr.columns)))
    ax.set_yticklabels(corr.columns)

    plt.colorbar(im)

    st.pyplot(fig)

    st.subheader("Estadísticos descriptivos")

    st.dataframe(df.T.describe())
