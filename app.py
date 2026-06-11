import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# =====================================================
# CONFIGURACIÓN — debe ser la PRIMERA instrucción
# BUG CORREGIDO: había un segundo st.set_page_config()
# más abajo que rompía la app al instanciarla.
# =====================================================

st.set_page_config(
    page_title="Gabriel Mena | Portfolio",
    page_icon="📊",
    layout="wide"
)

sns.set_theme(style="whitegrid")

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("📂 Gabriel Mena López")

pagina = st.sidebar.radio(
    "Seleccione una sección",
    [
        "🏠 Inicio",
        "👨‍💼 Currículum",
        "📊 Proyecto PBI LATAM",
        "👨‍💼 Analiza tu data aquí",   # <- nombre exacto usado en el elif
    ]
)

st.sidebar.markdown("---")
st.sidebar.write("Gabriel Mena López")
st.sidebar.write("Business Intelligence")
st.sidebar.write("Linkedin: https://www.linkedin.com/in/andresmena1")


# =====================================================
# INICIO
# =====================================================

if pagina == "🏠 Inicio":
    st.title("📊 Portafolio Profesional")
    st.subheader("Gabriel Mena López")
    st.write("""
    Bienvenido a mi portafolio profesional.

    Profesional con amplia experiencia en el sector de hidrocarburos y GLP, especializado en análisis
    comercial, inteligencia de negocios y gestión de información para la toma de decisiones. Cuento con
    sólidos conocimientos de la cadena comercial de combustibles, normativa regulatoria del mercado
    peruano y funcionamiento operativo del Sistema de Control de Órdenes de Pedido (SCOP).

    Actualmente me desempeño como Asistente Comercial en el Centro de Control SCOP, donde participo en
    el monitoreo, análisis y seguimiento de operaciones comerciales vinculadas al abastecimiento y
    comercialización de combustibles a nivel nacional. Mi experiencia me permite comprender
    integralmente los procesos del sector, desde la generación y validación de pedidos hasta la
    atención y resolución de incidencias operativas de los agentes del mercado.

    Poseo cerca de nueve años de experiencia en análisis de datos, elaboración de reportes comerciales,
    generación de indicadores de gestión y desarrollo de informes Ad Hoc para distintas áreas de
    negocio. He trabajado con grandes volúmenes de información, identificando tendencias, oportunidades
    de mejora y patrones relevantes para la toma de decisiones estratégicas.

    Asimismo, he brindado capacitación y asistencia técnica a grifos, plantas envasadoras y
    distribuidores minoristas de combustibles líquidos y GLP, fortaleciendo mi capacidad para
    comunicar información técnica y regulatoria a diversos públicos.

    Actualmente busco consolidar mi carrera en áreas de Análisis Comercial, Business Intelligence,
    Data Analytics y Consultoría para el sector energético y agroindustrial, integrando conocimientos
    de negocio, análisis de datos y herramientas tecnológicas para generar valor y optimizar procesos.

    Este espacio reúne mi experiencia en:

        • Análisis Comercial y de Mercados
        • Business Intelligence
        • Power BI
        • Excel Avanzado
        • SQL
        • Python para Análisis de Datos
        • ETL y Transformación de Datos
        • Indicadores KPI
        • Dashboards Gerenciales
        • Análisis de Tendencias Comerciales
        • Mercado de Hidrocarburos y GLP
        • Normativa SCOP y Regulación Energética
        • Elaboración de Reportes Ejecutivos
        • Consultoría de Negocios

    Utilice el menú lateral para navegar entre las secciones.
    """)
    st.info("Seleccione una opción del menú lateral izquierdo.")


# =====================================================
# CURRICULUM
# =====================================================

elif pagina == "👨‍💼 Currículum":

    st.title("👨‍💼 Gabriel Mena López")
    st.subheader("Business Analyst | Data Analyst | BI Analyst | SQL | Python | Power BI | Machine Learning")
    st.write("""
    Profesional orientado al análisis de datos, Business Intelligence, automatización de reportes
    y generación de indicadores para la toma de decisiones.
    """)

    # ==========================================
    # HABILIDADES
    # ==========================================

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

    # ==========================================
    # EXPERIENCIA
    # ==========================================

    st.header("💼 Experiencia Profesional")
    st.markdown("""
    ### OSINERGMIN

    - Monitoreo y análisis de información comercial relacionada con la distribución y comercialización
      de hidrocarburos líquidos y GLP a nivel nacional.
    - Extracción, validación y depuración de datos provenientes de sistemas corporativos Oracle para
      asegurar la calidad y consistencia de la información utilizada en reportes de gestión.
    - Elaboración de reportes analíticos mediante Excel avanzado (tablas dinámicas, segmentaciones,
      indicadores y gráficos ejecutivos) para el seguimiento de ventas y operaciones del sector
      energético.
    - Identificación de incidencias y anomalías en registros comerciales, contribuyendo a la mejora
      de la calidad de datos y continuidad operativa.
    - Análisis de tendencias y comportamiento de registros comerciales para apoyar procesos de
      supervisión y toma de decisiones.
    - Participación en pruebas funcionales y validación de cambios antes de pases a producción del
      sistema SCOP.
    - Capacitación a empresas del sector energético sobre procesos comerciales, flujos operativos
      y normativa.
    """)
     # ==========================================
# FORMACIÓN ACADÉMICA
# ==========================================

    st.header("🎓 Formación Académica")
    st.markdown("### Bachiller en Ingeniería Industrial")
    st.write("Universidad Tecnológica del Perú")
    st.write("Egresado 2013")
    
    st.divider()
    
    # ==========================================
    # DATOS, ANALÍTICA E IA
    # ==========================================
    
    st.header("📊 Datos, Analítica e Inteligencia Artificial")
    
    st.markdown("### Diplomado Business Analyst")
    st.write("Instituto DMC | Abril 2026 – Septiembre 2026 | 116 horas")
    
    st.divider()
    
    st.markdown("### Diplomado en Data Science")
    st.write("Modelos Supervisados, Clusterización y Machine Learning")
    st.write("Instituto DMC | Noviembre 2025 – Marzo 2026 | 96 horas")
    
    st.divider()
    
    st.markdown("### Programa Especializado en Machine Learning con Python")
    st.write("Laboratorio de Datos Sociales | Septiembre 2025 – Enero 2026 | 75 horas")
    
    st.divider()
    
    st.markdown("### Programa de Alta Especialización en Análisis Predictivo")
    st.write("Forecasting y Pronósticos")
    st.write("Escuela Global | Enero – Junio 2025 | 200 horas")
    
    st.divider()
    
    st.markdown("### Especialización Power BI")
    st.write("Instituto DMC | Julio 2025 – Septiembre 2025 | 44 horas")
    
    st.divider()
    
    st.markdown("### Especialización SQL Server for BI")
    st.write("Instituto DMC | Noviembre 2023 – Enero 2024 | 44 horas")
    
    st.divider()
    
    st.markdown("### Programación y Ciencia de Datos con Python y RStudio")
    st.write("Escuela Global | Setiembre – Diciembre 2023 | 170 horas")
    
    st.divider()
    
    # ==========================================
    # ESPECIALIZACIÓN SECTORIAL
    # ==========================================
    
    st.header("⚡ Especialización Sectorial")
    
    st.markdown("### Diplomado Especializado en Derecho de la Energía e Hidrocarburos")
    st.write("ICADEG | Noviembre 2024 – Enero 2025 | 120 horas")
    
    st.divider()
    
    # ==========================================
    # GESTIÓN INDUSTRIAL Y CALIDAD
    # ==========================================
    
    st.header("🏭 Gestión Industrial y Calidad")
    
    st.markdown("### Especialización en Gestión de la Producción")
    st.write("Planeamiento, Costos, Mantenimiento, Mejora Continua y Calidad")
    st.write("Universidad Nacional de Ingeniería")
    st.write("Setiembre 2010 – Febrero 2011 | 100 horas")
    
    st.divider()
    
    st.markdown("### Auditoría de Sistemas Integrados de Gestión")
    st.write("ISO 9001, ISO 14001 y OHSAS 18001")
    st.write("Universidad Nacional de Ingeniería")
    st.write("Agosto – Setiembre 2010 | 20 horas")
    
    st.divider()
    
    # ==========================================
    # HERRAMIENTAS DE ANÁLISIS
    # ==========================================
    
    st.header("📈 Herramientas de Análisis")
    
    st.markdown("### Excel para Análisis de Datos")
    st.write("Curso de Tablas Dinámicas con Excel")
    st.write("Instituto DMC | Enero 2017 | 8 horas")
    
    # ==========================================
    # ÁREAS DE ESPECIALIZACIÓN
    # ==========================================
    
    st.header("🚀 Áreas de Especialización")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **📊 Data & Analytics**
        - Business Intelligence
        - Data Analytics
        - Business Analytics
        - Data Science
        - Machine Learning
        - Forecasting
        - Inteligencia Artificial
        """)
    
    with col2:
        st.markdown("""
        **💼 Negocio y Sectorial**
        - SQL Server
        - Python
        - Power BI
        - Análisis Comercial
        - Inteligencia de Mercados
        - Exportaciones
        - Hidrocarburos y Energía
        """)

# =====================================================
# PROYECTO PBI LATAM
# =====================================================

elif pagina == "📊 Proyecto PBI LATAM":

    st.title("📊 Proyecto PBI América Latina")
    st.write("Análisis exploratorio del Producto Bruto Interno de países latinoamericanos.")

    data = {
        "Country": [
            "BRAZIL", "MEXICO", "ARGENTINA", "COLOMBIA",
            "CHILE", "PERU", "ECUADOR", "URUGUAY"
        ],
        2020: [1476, 1121, 385, 270, 253, 209, 95, 53],
        2021: [1670, 1316, 486, 318, 315, 229, 107, 60],
        2022: [1951, 1466, 632, 345, 301, 248, 116, 70],
        2023: [2191, 1794, 646, 366, 335, 271, 121, 77],
        2024: [2179, 1830, 633, 418, 330, 294, 124, 80],
    }

    df = pd.DataFrame(data).set_index("Country")

    st.subheader("Base de Datos")
    st.dataframe(df)

    st.subheader("Estadísticos Descriptivos")
    st.dataframe(df.T.describe())

    st.subheader("Matriz de Correlación")

    corr = df.T.corr()

    # BUG CORREGIDO: el código original usaba ax.imshow() con una
    # máscara triangular que producía una imagen en blanco (la máscara
    # booleana invertía los valores y ocultaba todo el contenido).
    # Se reemplaza con sns.heatmap(), que maneja correctamente la
    # máscara, los valores anotados y la barra de color.
    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        square=True,
        linewidths=0.5,
        ax=ax,
    )
    ax.set_title("Correlación PBI LATAM (2020–2024)", fontsize=14, pad=12)
    st.pyplot(fig)

    st.success("Proyecto de análisis económico desarrollado en Python.")


# =====================================================
# ENTREGABLE PYTHON — Dashboard de carga de archivos
# BUG CORREGIDO: la condición original era
#   elif pagina == "Entregable Python"
# (sin el emoji 👨‍💼), por lo que esta sección NUNCA se
# renderizaba. Se corrige el string para que coincida
# exactamente con el radio button del sidebar.
# =====================================================

elif pagina == "👨‍💼 Analiza tu data aquí":

    st.title("🚀 Advanced Analytics Dashboard")

    # --- FUNCIONES DE PROCESAMIENTO ---
    @st.cache_data
    def cargar_datos(archivo):
        if archivo.name.endswith(".csv"):
            return pd.read_csv(archivo)
        return pd.read_excel(archivo)

    def generar_reporte_nulos(df):
        nulos = df.isnull().sum()
        return nulos[nulos > 0]

    # --- CARGA DE ARCHIVO ---
    st.sidebar.header("Carga de Datos")
    archivo = st.sidebar.file_uploader("Subir dataset", type=["csv", "xlsx"])

    if archivo:
        df = cargar_datos(archivo)

        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📊 Exploración",
            "🔍 Calidad de Datos",
            "📉 Visualización Avanzada",
            "🤖 Análisis Estadístico",
            "⚠️ Detección de Anomalías",
        ])

        with tab1:
            st.subheader("Vista Previa del Dataset")
            st.dataframe(df.head(10), use_container_width=True)
            st.write(f"Dimensiones: {df.shape[0]} filas, {df.shape[1]} columnas")

        with tab2:
            st.subheader("🔍 Auditoría de Calidad de Datos")

            col1, col2, col3 = st.columns(3)
            col1.metric("Total Filas", df.shape[0])
            col2.metric("Total Columnas", df.shape[1])
            duplicados = df.duplicated().sum()
            col3.metric(
                "Filas Duplicadas",
                duplicados,
                delta_color="inverse" if duplicados > 0 else "normal",
            )

            st.divider()

            st.subheader("Diagnóstico de Nulos")
            nulos = generar_reporte_nulos(df)

            if not nulos.empty:
                st.warning(f"Se encontraron valores nulos en {len(nulos)} columnas.")
                st.bar_chart(nulos)
            else:
                st.success("¡Integridad de datos: Sin valores nulos detectados!")
                datos_cero = pd.DataFrame({"Nulos": 0}, index=df.columns)
                st.bar_chart(datos_cero)
                st.info("La ausencia de barras confirma que el dataset está completo.")

        with tab3:
            st.subheader("Suite de Visualización")
            tipo_graf = st.radio(
                "Seleccionar tipo de gráfico",
                [
                    "Relación (Plotly)",
                    "Distribución (Seaborn)",
                    "Correlación (Heatmap)",
                    "Boxplot (Outliers)",
                    "Densidad (Skew/Kurt)",
                ],
                horizontal=True,
            )

            c1, c2 = st.columns(2)
            with c1:
                col_x = st.selectbox("Eje X", df.columns)
            with c2:
                col_y = st.selectbox("Eje Y", df.select_dtypes(include=np.number).columns)

            if tipo_graf == "Relación (Plotly)":
                fig = px.scatter(
                    df, x=col_x, y=col_y,
                    color=df.columns[0],
                    template="plotly_dark",
                )
                # NOTA: config={'renderer': 'svg'} NO es un parámetro válido de
                # st.plotly_chart() — Streamlit gestiona el renderer internamente.
                # Si hay problemas de WebGL en el entorno, la solución correcta es
                # usar template="plotly_white" o "simple_white" en lugar de
                # "plotly_dark", que es más ligero en GPU. Aquí se deja el template
                # original y se elimina el config inválido.
                st.plotly_chart(fig, use_container_width=True)

            elif tipo_graf == "Distribución (Seaborn)":
                fig, ax = plt.subplots(figsize=(10, 5))
                sns.histplot(df[col_y], kde=True, color="teal", ax=ax)
                st.pyplot(fig)

            elif tipo_graf == "Correlación (Heatmap)":
                corr = df.select_dtypes(include=np.number).corr()
                mask = np.triu(np.ones_like(corr, dtype=bool))
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.heatmap(
                    corr, mask=mask, annot=True,
                    cmap="coolwarm", fmt=".2f",
                    ax=ax, square=True,
                )
                st.pyplot(fig)

            elif tipo_graf == "Boxplot (Outliers)":
                fig = px.box(df, y=col_y, title=f"Outliers: {col_y}", template="plotly_white")
                st.plotly_chart(fig, use_container_width=True)

            elif tipo_graf == "Densidad (Skew/Kurt)":
                from scipy.stats import shapiro

                skew = df[col_y].skew()
                kurt = df[col_y].kurt()
                stat, p = shapiro(df[col_y].dropna())

                fig, ax = plt.subplots(figsize=(10, 4))
                sns.kdeplot(df[col_y], fill=True, color="purple", ax=ax)
                ax.set_title(
                    f"Normalidad: P-value {p:.4f} | Skew: {skew:.2f} | Kurt: {kurt:.2f}"
                )
                st.pyplot(fig)

        with tab4:
            st.subheader("Resumen Estadístico Profundo")
            resumen = df.describe().T
            resumen["skew"] = df.skew(numeric_only=True)
            resumen["kurt"] = df.kurt(numeric_only=True)
            st.dataframe(resumen, use_container_width=True)

        with tab5:
            st.subheader("⚠️ Detección Automática de Anomalías")
            umbral = st.slider(
                "Seleccionar umbral de Z-Score (sensibilidad)", 1.5, 3.5, 3.0
            )
            col_outlier = st.selectbox(
                "Seleccionar columna para buscar anomalías",
                df.select_dtypes(include=np.number).columns,
            )

            z_scores = np.abs(
                (df[col_outlier] - df[col_outlier].mean()) / df[col_outlier].std()
            )
            anomalies = df[z_scores > umbral]

            if not anomalies.empty:
                st.warning(f"Se detectaron {len(anomalies)} filas fuera del rango estadístico.")
                st.dataframe(anomalies)
                csv = anomalies.to_csv(index=False).encode("utf-8")
                st.download_button(
                    "Descargar Anomalías (CSV)", csv, "anomalias.csv", "text/csv"
                )
            else:
                st.success("¡No se detectaron anomalías significativas con este umbral!")

    else:
        # BUG CORREGIDO: el else original estaba al nivel global del script,
        # por lo que se ejecutaba en TODAS las páginas cuando no había archivo
        # cargado (mostraba el mensaje incluso en Inicio, Currículum, etc.).
        # Ahora está correctamente anidado dentro del elif de esta página.
        st.info("Cargue un archivo en la barra lateral para inicializar el motor de análisis.")
