import streamlit as st

st.title("Proyecto final Diploma BI")

st.sidebar.title("Parametros")

st.sidebar.image("dmc.jpg", use_container_width=True)
st.write("Elaborado por Gabriel Mena")



```python
# ==========================================================
# DASHBOARD STREAMLIT
# Determinantes del Acceso a la Salud en el Perú
# ENAHO 2020 - Correlación y Regresión Logística
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------------------------
# CONFIGURACIÓN
# ----------------------------------------------------------

st.set_page_config(
    page_title="Acceso a la Salud - Perú",
    page_icon="🏥",
    layout="wide"
)

sns.set_theme(style="whitegrid")

# ----------------------------------------------------------
# TITULO
# ----------------------------------------------------------

st.title("🏥 Determinantes del Acceso a la Salud en el Perú")
st.subheader("Análisis de Correlación y Regresión Logística - ENAHO 2020")

st.markdown("""
### Objetivo General

Determinar la influencia de factores institucionales y demográficos
en la probabilidad de acceso a consulta médica.

### Variables Analizadas

- Edad
- Sexo
- Área geográfica
- Enfermedad crónica
- SIS
- EsSalud

### Metodología

- Limpieza de datos
- Correlación
- Regresión logística
- Odds Ratio
- Probabilidades predichas
""")

# ----------------------------------------------------------
# SIDEBAR
# ----------------------------------------------------------

st.sidebar.title("⚙️ Parámetros")

archivo = st.sidebar.file_uploader(
    "Cargar archivo Excel ENAHO",
    type=["xlsx"]
)

if archivo is not None:

    # ------------------------------------------------------
    # CARGA DE DATOS
    # ------------------------------------------------------

    df = pd.read_excel(archivo)

    columnas_deseadas = [
        'P208A',
        'P207',
        'AREA',
        'P401',
        'P4195',
        'P4191',
        'P414N$01'
    ]

    columnas_presentes = [
        col for col in columnas_deseadas
        if col in df.columns
    ]

    df = df[columnas_presentes]

    # ------------------------------------------------------
    # MAPEO
    # ------------------------------------------------------

    mapeo = {
        'Hombre': 1,
        'Mujer': 0,
        'URBANO': 1,
        'RURAL': 0,
        'Si': 1,
        'No': 0,
        'Seguro Integral de Salud (SIS)': 1,
        'EsSalud': 1,
        'Consulta': 1
    }

    df_modelo = df.copy()

    for col in [
        'P207',
        'AREA',
        'P401',
        'P4195',
        'P4191',
        'P414N$01'
    ]:

        df_modelo[col] = df_modelo[col].map(mapeo)

    df_modelo['P414N$01'] = df_modelo['P414N$01'].fillna(0)

    df_modelo['P208A'] = pd.to_numeric(
        df_modelo['P208A'],
        errors='coerce'
    )

    df_modelo = df_modelo.dropna()

    # ------------------------------------------------------
    # KPIs
    # ------------------------------------------------------

    st.header("📊 Indicadores Principales")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Registros",
        f"{len(df_modelo):,}"
    )

    col2.metric(
        "Edad Promedio",
        round(df_modelo["P208A"].mean(), 1)
    )

    col3.metric(
        "Edad Máxima",
        int(df_modelo["P208A"].max())
    )

    col4.metric(
        "Edad Mediana",
        int(df_modelo["P208A"].median())
    )

    # ------------------------------------------------------
    # DATOS
    # ------------------------------------------------------

    with st.expander("Ver datos"):

        st.dataframe(df_modelo.head(20))

    # ------------------------------------------------------
    # HISTOGRAMA
    # ------------------------------------------------------

    st.header("📈 Distribución de Edad")

    fig1, ax1 = plt.subplots(figsize=(10,5))

    sns.histplot(
        df_modelo["P208A"],
        kde=True,
        bins=30,
        ax=ax1
    )

    ax1.axvline(
        df_modelo["P208A"].mean(),
        linestyle="--"
    )

    ax1.set_title("Distribución de Edad")

    st.pyplot(fig1)

    # ------------------------------------------------------
    # CORRELACIÓN
    # ------------------------------------------------------

    st.header("🔥 Mapa de Calor de Correlación")

    variables = [
        'P208A',
        'P207',
        'AREA',
        'P401',
        'P4195',
        'P4191'
    ]

    matriz_corr = df_modelo[variables].corr()

    fig2, ax2 = plt.subplots(figsize=(8,6))

    sns.heatmap(
        matriz_corr,
        annot=True,
        cmap="RdYlGn",
        fmt=".2f",
        ax=ax2
    )

    st.pyplot(fig2)

    st.info("""
    La relación más fuerte observada corresponde a:
    Edad ↔ Enfermedad Crónica.
    """)

    # ------------------------------------------------------
    # REGRESIÓN LOGÍSTICA
    # ------------------------------------------------------

    st.header("📉 Regresión Logística")

    y = df_modelo["P414N$01"]

    X = df_modelo[
        [
            'P208A',
            'P207',
            'AREA',
            'P401',
            'P4195',
            'P4191'
        ]
    ]

    X = sm.add_constant(X)

    modelo = sm.Logit(y, X).fit(disp=False)

    resumen = modelo.summary2().tables[1]

    resumen["Odds Ratio"] = np.exp(
        resumen["Coef."]
    )

    resumen["Lower CI"] = np.exp(
        resumen["[0.025"]
    )

    resumen["Upper CI"] = np.exp(
        resumen["0.975]"]
    )

    st.dataframe(
        resumen[
            [
                "Coef.",
                "P>|z|",
                "Odds Ratio",
                "Lower CI",
                "Upper CI"
            ]
        ].round(4)
    )

    # ------------------------------------------------------
    # FOREST PLOT
    # ------------------------------------------------------

    st.header("🌲 Forest Plot")

    resultados = resumen.iloc[1:]

    fig3, ax3 = plt.subplots(figsize=(10,6))

    ax3.errorbar(
        resultados["Odds Ratio"],
        resultados.index,
        xerr=[
            resultados["Odds Ratio"] -
            resultados["Lower CI"],
            resultados["Upper CI"] -
            resultados["Odds Ratio"]
        ],
        fmt="o"
    )

    ax3.axvline(
        x=1,
        linestyle="--"
    )

    ax3.set_xlabel("Odds Ratio")

    st.pyplot(fig3)

    # ------------------------------------------------------
    # PROBABILIDADES PREDICHAS
    # ------------------------------------------------------

    st.header("📍 Probabilidades Predichas")

    coef = modelo.params

    edades = np.arange(0, 101)

    def probabilidad(edad, sis):

        logit = (
            coef['const']
            + coef['P208A'] * edad
            + coef['P207'] * 1
            + coef['AREA'] * 1
            + coef['P401'] * 0
            + coef['P4195'] * sis
            + coef['P4191'] * 0
        )

        return 1 / (1 + np.exp(-logit))

    prob_sis = [
        probabilidad(e, 1)
        for e in edades
    ]

    prob_no = [
        probabilidad(e, 0)
        for e in edades
    ]

    fig4, ax4 = plt.subplots(figsize=(10,6))

    ax4.plot(
        edades,
        prob_sis,
        linewidth=3,
        label="Con SIS"
    )

    ax4.plot(
        edades,
        prob_no,
        linestyle="--",
        label="Sin SIS"
    )

    ax4.set_title(
        "Probabilidad Predicha de Consulta Médica"
    )

    ax4.set_xlabel("Edad")

    ax4.set_ylabel("Probabilidad")

    ax4.legend()

    st.pyplot(fig4)

    # ------------------------------------------------------
    # CONCLUSIONES
    # ------------------------------------------------------

    st.header("📌 Hallazgos Principales")

    st.success("""
    ✔ El SIS aparece como el principal factor institucional.

    ✔ La edad incrementa la probabilidad de consulta médica.

    ✔ La enfermedad crónica no muestra un efecto
    estadísticamente significativo.

    ✔ El acceso depende más del aseguramiento que
    de la necesidad clínica.

    ✔ Existen desafíos importantes de equidad en el
    sistema sanitario peruano.
    """)

else:

    st.info(
        "⬅️ Cargue el archivo Excel de ENAHO para iniciar el análisis."
    )
```

