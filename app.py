import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# =====================================================
# 1. CONFIGURACIÓN DE LA PÁGINA
# =====================================================
st.set_page_config(
    page_title="Gabriel Mena | Portafolio Streamlit",
    page_icon="📊",
    layout="wide"
)

# Estilo de Seaborn
sns.set_theme(style="whitegrid")

# Inicializar el estado de la aplicación para persistencia de datos
if 'df' not in st.session_state:
    st.session_state['df'] = None

# =====================================================
# SIDEBAR / NAVEGACIÓN
# =====================================================
st.sidebar.title("🚀 Menú de Navegación")
st.sidebar.markdown(f"**Autor:** Gabriel Mena López")

pagina = st.sidebar.radio(
    "Seleccione una sección",
    [
        "🏠 Home",
        "📂 2. Carga y Perfil",
        "⚙️ 3. Procesamiento",
        "📊 4. Análisis Visual"
    ]
)

st.sidebar.markdown("---")
st.sidebar.write("📩 gmena50@gmail.com")
st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/andresmena1/)")

# =====================================================
# SECCIÓN 1: HOME
# =====================================================
if pagina == "🏠 Home":
    st.title("📊 Portafolio Profesional: Data Analytics App")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Presentación del Proyecto")
        st.write("""
        Esta es una **Aplicación Interactiva** construida íntegramente en **Python con Streamlit**. 
        El objetivo es demostrar la capacidad de procesar, limpiar y analizar visualmente diversos conjuntos de datos 
        de manera automatizada y dinámica.
        """)
        
        st.subheader("Objetivo del Sistema")
        st.info("""
        Construir una herramienta capaz de procesar datasets de distintas industrias, 
        permitiendo al usuario cargar sus propios archivos o utilizar datos predefinidos, 
        pasando por fases de perfilado, limpieza y análisis visual avanzado con gráficos interactivos.
        """)

        st.subheader("Tecnologías Utilizadas")
        st.code("Python, Pandas, Streamlit, Plotly, Seaborn, Matplotlib, GitHub, Excel")

    with col2:
        st.header("Sobre el Autor")
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100) # Imagen representativa
        st.markdown(f"**Gabriel Andrés Mena López**")
        st.caption("Instituto DMC")
        st.write("""
        Profesional con amplia experiencia en el sector de hidrocarburos y GLP, especializado en análisis comercial, 
        inteligencia de negocios y gestión de información para la toma de decisiones. 
        Poseo sólidos conocimientos del mercado peruano y el sistema SCOP.
        """)

    st.divider()
    
    st.header("Datasets Disponibles en el Proyecto")
    d1, d2, d3, d4 = st.columns(4)
    
    with d1:
        st.markdown("**Data 1: AI Impact 2030**")
        st.caption("Mercado laboral e impacto de la IA en empleos, salarios y demanda futura.")
    with d2:
        st.markdown("**Data 2: Superstore Sales**")
        st.caption("Ventas minoristas: pedidos, clientes, regiones, categorías y utilidad.")
    with d3:
        st.markdown("**Data 3: E-commerce Risk**")
        st.caption("Detección de fraude: métodos de pago, valor de orden y etiquetas de riesgo.")
    with d4:
        st.markdown("**Data 4: Teen Mental Health**")
        st.caption("Hábitos digitales, sueño y bienestar en adolescentes.")

# =====================================================
# SECCIÓN 2: CARGA Y PERFIL
# =====================================================
elif pagina == "📂 2. Carga y Perfil":
    st.title("📂 Carga y Perfil del Dataset")
    
    opcion_carga = st.radio("Seleccione origen de datos:", ["Subir mi propio CSV", "Seleccionar Dataset del Proyecto"])
    
    df_cargado = None

    if opcion_carga == "Subir mi propio CSV":
        archivo = st.file_uploader("Cargue su archivo CSV", type=["csv"])
        if archivo:
            df_cargado = pd.read_csv(archivo)
    else:
        dataset_selec = st.selectbox("Elija un dataset:", [
            "AI_Impact_on_Jobs_2030.csv", 
            "sample_-_superstore.csv", 
            "synthetic_ecommerce_order_risk_dataset.csv", 
            "Teen_Mental_Health_Dataset.csv"
        ])
        st.info(f"Nota: En el entorno local, asegúrese de que el archivo '{dataset_selec}' esté en la carpeta del proyecto.")
        # Simulación de carga (sustituir por rutas reales)
        try:
            df_cargado = pd.read_csv(dataset_selec)
        except:
            st.error("Archivo no encontrado localmente. Por favor use la opción de 'Subir mi propio CSV'.")

    if df_cargado is not None:
        st.session_state['df'] = df_cargado
        st.success("¡Datos cargados exitosamente!")
        
        tab1, tab2 = st.tabs(["👀 Vista Previa", "📊 Resumen Estadístico"])
        
        with tab1:
            st.subheader("Primeras filas")
            st.dataframe(df_cargado.head(10))
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Filas", df_cargado.shape[0])
            c2.metric("Columnas", df_cargado.shape[1])
            c3.write("**Tipos de Datos:**")
            st.write(df_cargado.dtypes)

        with tab2:
            st.subheader("Análisis Descriptivo")
            st.write(df_cargado.describe(include='all'))
    else:
        st.warning("Por favor, cargue un archivo para continuar.")

# =====================================================
# SECCIÓN 3: PROCESAMIENTO
# =====================================================
elif pagina == "⚙️ 3. Procesamiento":
    st.title("⚙️ Procesamiento de Datos")
    
    if st.session_state['df'] is not None:
        df = st.session_state['df']
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Detección de Variables")
            num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            cat_cols = df.select_dtypes(include=['object']).columns.tolist()
            date_cols = df.select_dtypes(include=['datetime', 'period']).columns.tolist()
            
            st.write(f"🔢 **Numéricas:** {', '.join(num_cols) if num_cols else 'Ninguna'}")
            st.write(f"🔤 **Categóricas:** {', '.join(cat_cols) if cat_cols else 'Ninguna'}")
            st.write(f"📅 **Fechas:** {', '.join(date_cols) if date_cols else 'Ninguna'}")

        with col2:
            st.subheader("Validación de Calidad")
            nulos = df.isnull().sum().sum()
            duplicados = df.duplicated().sum()
            
            st.write(f"❓ **Valores Nulos:** {nulos}")
            st.write(f"👯 **Valores Duplicados:** {duplicados}")
        
        st.divider()
        st.subheader("Herramientas de Limpieza Rápida")
        
        c1, c2 = st.columns(2)
        if c1.button("Eliminar Duplicados"):
            df = df.drop_duplicates()
            st.session_state['df'] = df
            st.rerun()
            
        if c2.button("Limpiar Nulos (Media/Moda)"):
            for col in df.columns:
                if df[col].dtype in [np.float64, np.int64]:
                    df[col] = df[col].fillna(df[col].mean())
                else:
                    df[col] = df[col].fillna(df[col].mode()[0])
            st.session_state['df'] = df
            st.rerun()

    else:
        st.error("No hay datos para procesar. Vaya a la sección '2. Carga y Perfil'.")

# =====================================================
# SECCIÓN 4: ANÁLISIS VISUAL
# =====================================================
elif pagina == "📊 4. Análisis Visual":
    st.title("📊 Analiza tu Data Aquí")
    
    if st.session_state['df'] is not None:
        df = st.session_state['df']
        
        tab_uni, tab_bi, tab_multi, tab_temp = st.tabs([
            "📈 Univariado", "♊ Bivariado", "💠 Multivariado", "⏳ Temporal"
        ])
        
        # --- UNIVARIADO ---
        with tab_uni:
            st.subheader("Distribución de una sola variable")
            col_sel = st.selectbox("Seleccione columna:", df.columns, key="uni")
            
            c1, c2 = st.columns(2)
            with c1:
                # Plotly
                fig = px.histogram(df, x=col_sel, title=f"Histograma de {col_sel}", color_discrete_sequence=['#636EFA'])
                st.plotly_chart(fig, use_container_width=True)
            with c2:
                # Seaborn
                fig2, ax2 = plt.subplots()
                sns.boxplot(data=df, y=col_sel, ax=ax2, color="#00CC96")
                ax2.set_title(f"Boxplot de {col_sel}")
                st.pyplot(fig2)

        # --- BIVARIADO ---
        with tab_bi:
            st.subheader("Relación entre dos variables")
            num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            if len(num_cols) >= 2:
                c1, c2 = st.columns(2)
                with c1:
                    vx = st.selectbox("Eje X:", num_cols)
                    vy = st.selectbox("Eje Y:", num_cols)
                
                fig_bi = px.scatter(df, x=vx, y=vy, trendline="ols", title=f"{vx} vs {vy}")
                st.plotly_chart(fig_bi, use_container_width=True)
            else:
                st.warning("Se requieren al menos 2 columnas numéricas.")

        # --- MULTIVARIADO ---
        with tab_multi:
            st.subheader("Análisis de múltiples dimensiones")
            if len(num_cols) >= 2:
                cat_cols = df.select_dtypes(include=['object']).columns.tolist()
                color_col = st.selectbox("Color por (Categoría):", [None] + cat_cols)
                
                fig_multi = px.scatter(df, x=num_cols[0], y=num_cols[1], color=color_col, 
                                       size=num_cols[0] if len(num_cols)>0 else None,
                                       hover_data=df.columns)
                st.plotly_chart(fig_multi, use_container_width=True)
                
                st.markdown("**Matriz de Correlación (Heatmap)**")
                fig_corr, ax_corr = plt.subplots()
                sns.heatmap(df[num_cols].corr(), annot=True, cmap="RdBu", ax=ax_corr)
                st.pyplot(fig_corr)

        # --- TEMPORAL ---
        with tab_temp:
            st.subheader("Análisis de Series de Tiempo")
            # Intentar detectar fechas si no fueron detectadas
            potential_date_cols = [c for c in df.columns if 'Date' in c or 'Fecha' in c or 'Year' in c]
            
            if potential_date_cols:
                date_sel = st.selectbox("Columna de fecha:", potential_date_cols)
                val_sel = st.selectbox("Valor a medir:", num_cols, key="temp_val")
                
                # Convertir a datetime para el gráfico
                df_temp = df.copy()
                df_temp[date_sel] = pd.to_datetime(df_temp[date_sel], errors='coerce')
                df_temp = df_temp.sort_values(date_sel)
                
                fig_line = px.line(df_temp, x=date_sel, y=val_sel, title="Tendencia Temporal")
                st.plotly_chart(fig_line, use_container_width=True)
            else:
                st.info("No se detectaron columnas de fecha obvias para el análisis temporal.")

    else:
        st.error("No hay datos para analizar. Vaya a la sección '2. Carga y Perfil'.")

# =====================================================
# FOOTER
# =====================================================
st.sidebar.markdown("---")
st.sidebar.caption("© 2024 Gabriel Mena López - Dashboard Analytics")
