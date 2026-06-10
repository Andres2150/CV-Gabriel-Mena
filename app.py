
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
# SIDEBAR
# =====================================================

st.sidebar.title("📂 Gabriel Mena López")

pagina = st.sidebar.radio(
    "Seleccione una sección",
    [
        "🏠 Inicio",
        "👨‍💼 Currículum",
        "📊 Proyecto PBI LATAM"
        "📊 Proyecto entregable Python"
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

    Profesional con amplia experiencia en el sector de hidrocarburos y GLP, especializado en análisis comercial, inteligencia de negocios y gestión de información para la toma de decisiones. Cuento con sólidos conocimientos de la cadena comercial de combustibles, normativa regulatoria del mercado peruano y funcionamiento operativo del Sistema de Control de Órdenes de Pedido (SCOP).

Actualmente me desempeño como Asistente Comercial en el Centro de Control SCOP, donde participo en el monitoreo, análisis y seguimiento de operaciones comerciales vinculadas al abastecimiento y comercialización de combustibles a nivel nacional. Mi experiencia me permite comprender integralmente los procesos del sector, desde la generación y validación de pedidos hasta la atención y resolución de incidencias operativas de los agentes del mercado.

Poseo cerca de nueve años de experiencia en análisis de datos, elaboración de reportes comerciales, generación de indicadores de gestión y desarrollo de informes Ad Hoc para distintas áreas de negocio. He trabajado con grandes volúmenes de información, identificando tendencias, oportunidades de mejora y patrones relevantes para la toma de decisiones estratégicas.

Asimismo, he brindado capacitación y asistencia técnica a grifos, plantas envasadoras y distribuidores minoristas de combustibles líquidos y GLP, fortaleciendo mi capacidad para comunicar información técnica y regulatoria a diversos públicos.

Actualmente busco consolidar mi carrera en áreas de Análisis Comercial, Business Intelligence, Data Analytics y Consultoría para el sector energético y agroindustrial, integrando conocimientos de negocio, análisis de datos y herramientas tecnológicas para generar valor y optimizar procesos.

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

    st.subheader(
        "Business Intelligence | Data Analytics | Python"
    )

    st.write("""
    Profesional orientado al análisis de datos,
    Business Intelligence, automatización de reportes
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

Monitoreo y análisis de información comercial relacionada con la distribución y comercialización de hidrocarburos líquidos y GLP a nivel nacional.
Extracción, validación y depuración de datos provenientes de sistemas corporativos Oracle para asegurar la calidad y consistencia de la información utilizada en reportes de gestión.
Elaboración de reportes analíticos mediante Excel avanzado (tablas dinámicas, segmentaciones, indicadores y gráficos ejecutivos) para el seguimiento de ventas y operaciones del sector energético.
Identificación de incidencias y anomalías en registros comerciales, contribuyendo a la mejora de la calidad de datos y continuidad operativa.
Análisis de tendencias y comportamiento de registros comerciales para apoyar procesos de supervisión y toma de decisiones.
Participación en pruebas funcionales y validación de cambios antes de pases a producción del sistema SCOP.
Capacitación a empresas del sector energético sobre procesos comerciales, flujos operativos y normativa
    """)

    # ==========================================
    # ESTUDIOS
    # ==========================================

    st.header("🎓 Estudios y Certificaciones")

    st.markdown("### Bachiller en Ingeniería Industrial")
    st.write("Universidad Tecnológica del Perú")
    st.write("Egresado Año 2013")

    st.divider()

    st.markdown("### Especialización en Gestión de la Producción")
    st.write("Planeamiento, Costos, Mantenimiento, Mejora Continua y Calidad")
    st.write("Universidad Nacional de Ingeniería")
    st.write("Setiembre 2010 – Febrero 2011")
    st.write("100 horas")

    st.divider()

    st.markdown("### Curso Taller: Auditoría de Sistemas Integrados de Gestión")
    st.write("ISO 9001, ISO 14001 y OHSAS 18001")
    st.write("Universidad Nacional de Ingeniería")
    st.write("Agosto – Setiembre 2010")
    st.write("20 horas")

    st.divider()

    st.markdown("### Diplomado Business Analyst")
    st.write("Identificar necesidades del negocio, analizar procesos y datos, y convertirlos en soluciones que mejoren la toma de decisiones y los resultados de la empresa.")
    st.write("Instituto DMC")
    st.write("Abril 2026 – Septiembre 2026")
    st.write("116 horas")

    st.divider()

    st.markdown("### Diplomado en Data Science")
    st.write("Analisis de datos y construcción de modelos de Machine Learning que permitan predecir resultados, segmentar clientes y apoyar la toma de decisiones basada en datos.")
    st.write("Modelos Supervisados, Clusterización y Machine Learning")
    st.write("Instituto DMC")
    st.write("Noviembre 2025 – Marzo 2026")
    st.write("96 horas")

    st.divider()
    
    st.markdown("### Programa Especializado en Machine Learning con Python")
    st.write("Laboratorio de Datos Sociales")
    st.write("Septiembre 2025 – Enero 2026")
    st.write("75 horas")

    st.divider()
    
    st.markdown("### Especialización Power BI")
    st.write("Instituto DMC")
    st.write("Julio 2025 – Septiembre 2025")
    st.write("44 horas")

    st.divider()

    st.markdown("### Programa de Alta Especialización en Análisis Predictivo")
    st.write("Pronósticos y Forecasting")
    st.write("Escuela Global")
    st.write("Enero – Junio 2025")
    st.write("200 horas")

    st.divider()

    st.markdown("### Diplomado Especializado en Derecho de la Energía e Hidrocarburos")
    st.write("ICADEG")
    st.write("Noviembre 2024 – Enero 2025")
    st.write("120 horas")

    st.divider()

    st.markdown("### Especialización en SQL Server for BI ")
    st.write("Instituto DMC")
    st.write("Noviembre 2023 – Enero 2024")
    st.write("44 horas")
    
    st.divider()

    st.markdown("### Programación y Ciencia de Datos con Python y RStudio")
    st.write("Escuela Global")
    st.write("Setiembre – Diciembre 2023")
    st.write("170 horas")

    st.divider()

    st.markdown("### Curso de Tablas Dinámicas con Excel")
    st.write("Instituto DMC")
    st.write("Enero 2017")
    st.write("8 horas")

    # ==========================================
    # ÁREAS DE ESPECIALIZACIÓN
    # ==========================================

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

    mask = np.triu(np.ones_like(corr, dtype=bool))

    corr_masked = corr.mask(mask)

    fig, ax = plt.subplots(figsize=(10, 8))

    im = ax.imshow(corr_masked)

    ax.set_xticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=90)

    ax.set_yticks(range(len(corr.columns)))
    ax.set_yticklabels(corr.columns)

    plt.colorbar(im)

    st.pyplot(fig)

    st.success(
        "Proyecto de análisis económico desarrollado en Python."
    )

# =====================================================
# PIE DE PÁGINA
# =====================================================

st.sidebar.markdown("---")
st.sidebar.write("Gabriel Mena López")
st.sidebar.write("Business Intelligence")
st.sidebar.write("Linkedin: https://www.linkedin.com/in/andresmena1")

