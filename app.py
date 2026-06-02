import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(
    page_title="Gabriel Mena | Portfolio",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# MENÚ LATERAL
# =====================================================

st.sidebar.title("📂 Portafolio")

pagina = st.sidebar.radio(
    "Seleccionar sección",
    [
        "🏠 Inicio",
        "👨‍💼 Currículum",
        "📊 Proyecto PBI LATAM"
    ]
)

# =====================================================
# INICIO
# =====================================================

if pagina == "🏠 Inicio":

    st.title("📊 Portafolio Profesional")

    st.subheader("Gabriel Mena López")

    st.write("""
    Bienvenido a mi portafolio profesional.

    Este espacio reúne mi experiencia en:

    - Business Intelligence
    - Análisis de Datos
    - Python
    - SQL
    - Power BI
    - Machine Learning
    - Forecasting
    - Inteligencia Artificial

    Utilice el menú lateral para navegar entre las secciones.
    """)

    st.image(
        "dmc.jpg",
        width=300
    )

# =====================================================
# CURRICULUM
# =====================================================

elif pagina == "👨‍💼 Currículum":

    st.title("👨‍💼 Gabriel Mena López")

    st.subheader(
        "Business Intelligence | Data Analytics | Python"
    )

    st.write("""
    Profesional orientado al análisis de datos,
    Business Intelligence, automatización de reportes
    y generación de indicadores para la toma de decisiones.
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
    st.progress(75)

    st.write("Forecasting")
    st.progress(75)

    st.header("💼 Experiencia Profesional")

    st.markdown("""
    **OSINERGMIN**

    - Monitoreo y validación de información.
    - Elaboración de reportes.
    - Atención de usuarios.
    - Seguimiento de indicadores.
    - Análisis de información para toma de decisiones.
    """)

    st.header("🎓 Estudios y Certificaciones")

    st.markdown("""
    ### Bachiller en Ingeniería Industrial
    Universidad Tecnológica del Perú

    ---

    ### Especialización en Gestión de la Producción
    Planeamiento, Costos, Mantenimiento, Mejora Continua y Calidad

    Universidad Nacional de Ingeniería

    Setiembre 2010 – Febrero 2011

    100 horas

    ---

    ### Curso Taller: Auditoría de Sistemas Integrados de Gestión
    ISO 9001, ISO 14001 y OHSAS 18001

    Universidad Nacional de Ingeniería

    Agosto – Setiembre 2010

    20 horas

    ---

    ### Diplomado en Data Science

    Modelos Supervisados, Clusterización y Machine Learning

    Instituto DMC

    Noviembre 2025 – Marzo 2026

    96 horas

    ---

    ### Programa Especializado en Machine Learning con Python

    Laboratorio de Datos Sociales

    Septiembre 2025 – Enero 2026

    75 horas

    ---

    ### Programa de Alta Especialización en Análisis Predictivo,
    Pronósticos y Forecasting

    Escuela Global

    Enero – Junio 2025

    200 horas

    ---

    ### Diplomado Especializado en Derecho de la Energía e Hidrocarburos

    ICADEG

    Noviembre 2024 – Enero 2025

    120 horas

    ---

    ### Programación y Ciencia de Datos con Python y RStudio

    Escuela Global

    Setiembre – Diciembre 2023

    170 horas

    ---

    ### Curso de Tablas Dinámicas con Excel

    Instituto DMC

    Enero 2017

    8 horas
    """)

    st.header("🚀 Áreas de Especialización")

    st.markdown("""
    - Business Intelligence
    - Data Analytics
    - SQL
    - Python
    - Power BI
    - Machine Learning
    - Forecasting
    - Inteligencia Artificial
    - Análisis Comercial
    - Exportaciones
    - Hidrocarburos y Energía
    """)

# =====================================================
# PROYECTO PBI LATAM
# =====================================================

elif pagina == "📊 Proyecto PBI LATAM":

    st.title("📊 Proyecto PBI América Latina")

    st.write("""
    Análisis exploratorio del Producto Bruto Interno
    de países latinoamericanos.
    """)

    data = {
        "Country": [
            "BRAZIL",
            "MEXICO",
            "ARGENTINA",
            "COLOMBIA",
            "CHILE",
            "PERU",
            "ECUADOR",
            "URUGUAY"
        ],

        2020: [1476,1121,385,270,253,209,95,53],
        2021: [1670,1316,486,318,315,229,107,60],
        2022: [1951,1466,632,345,301,248,116,70],
        2023: [2191,1794,646,366,335,271,121,77],
        2024: [2179,1830,633,418,330,294,124,80]
    }

    df = pd.DataFrame(data)
    df = df.set_index("Country")

    st.subheader("Base de Datos")

    st.dataframe(df)

    st.subheader("Estadísticos Descriptivos")

    st.dataframe(df.T.describe())

    st.subheader("Matriz de Correlación")

    corr = df.T.corr()

    mask = np.triu(
        np.ones_like(corr, dtype=bool)
    )

    corr_masked = corr.mask(mask)

    fig, ax = plt.subplots(figsize=(10, 8))

    im = ax.imshow(corr_masked)

    ax.set_xticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=90)

    ax.set_yticks(range(len(corr.columns)))
    ax.set_yticklabels(corr.columns)

    plt.colorbar(im)

    st.pyplot(fig)

    st.success("Proyecto de análisis económico desarrollado en Python.")

# =====================================================
# PIE DE PÁGINA
# =====================================================

st.sidebar.markdown("---")
st.sidebar.write("Gabriel Mena López")
st.sidebar.write("Business Intelligence")
