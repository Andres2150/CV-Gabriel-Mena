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
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
        st.markdown(f"**Gabriel Andrés Mena López**")
        st.caption("Instituto DMC")
        st.write("""
        Profesional con amplia experiencia en el sector de hidrocarburos y GLP, especializado en análisis comercial, 
        inteligencia de negocios y gestión de información para la toma de decisiones. 
        Cuento con sólidos conocimientos de la cadena comercial de combustibles, normativa regulatoria del mercado peruano 
        y el funcionamiento operativo del Sistema de Control de Órdenes de Pedido (SCOP).
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
        st.caption("Pedios de e-commerce: métodos de pago, valor de orden y etiquetas de riesgo.")
    with d4:
        st.markdown("**Data 4: Teen Mental Health**")
        st.caption("Hábitos digitales, sueño, actividad física y bienestar en adolescentes.")

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
        
        # Intentar cargar localmente
        try:
            df_cargado = pd.read_csv(dataset_selec)
        except Exception as e:
            st.error(f"No se pudo cargar '{dataset_selec}' automáticamente. Asegúrate de que el archivo esté subido en tu repositorio de GitHub o usa la opción 'Subir mi propio CSV'.")

    if df_cargado is not None:
        st.session_state['df'] = df_cargado
        st.success("¡Datos cargados exitosamente!")
        
        tab1, tab2 = st.tabs(["👀 Vista Previa", "📊 Resumen Estadístico"])
        
        with tab1:
            st.subheader("Primeras filas")
            st.dataframe(df_cargado.head(10), use_container_width=True)
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Filas", df_cargado.shape[0])
            c2.metric("Columnas", df_cargado.shape[1])
            with c3:
                st.write("**Tipos de Datos detectados:**")
                st.dataframe(df_cargado.dtypes.astype(str).to_frame(name="Tipo de Dato"), use_container_width=True)

        with tab2:
            st.subheader("Análisis Descriptivo")
            st.write(df_cargado.describe(include='all'))
    else:
        st.warning("Por favor, cargue o seleccione un archivo para continuar.")

# =====================================================
# SECCIÓN 3: PROCESAMIENTO (BUG CORREGIDO PARA PYTHON 3.14)
# =====================================================
elif pagina == "⚙️ 3. Procesamiento":
    st.title("⚙️ Procesamiento de Datos")
    
    if st.session_state['df'] is not None:
        df = st.session_state['df']
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Detección de Variables")
            
            # SOLUCIÓN BUG: Evitamos strings genéricos que rompen select_dtypes en Python 3.14
            num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
            
            # Buscamos columnas de fecha de forma explícita y segura
            date_cols = df.select_dtypes(include=['datetime64[ns]']).columns.tolist()
            
            st.write(f"🔢 **Numéricas:** {', '.join(num_cols) if num_cols else 'Ninguna'}")
            st.write(f"🔤 **Categóricas:** {', '.join(cat_cols) if cat_cols else 'Ninguna'}")
            st.write(f"📅 **Fechas:** {', '.join(date_cols) if date_cols else 'Ninguna'}")

        with col2:
            st.subheader("Validación de Calidad")
            nulos = df.isnull().sum().sum()
            duplicados = df.duplicated().sum()
            
            st.write(f"❓ **Valores Nulos totales:** {nulos}")
            st.write(f"👯 **Valores Duplicados:** {duplicados}")
        
        st.divider()
        st.subheader("Herramientas de Limpieza Rápida")
        
        c1, c2, c3 = st.columns(3)
        if c1.button("Eliminar Duplicados"):
            df_limpio = df.drop_duplicates()
            st.session_state['df'] = df_limpio
            st.success("¡Duplicados eliminados!")
            st.rerun()
            
        if c2.button("Limpiar Nulos (Media/Moda)"):
            df_limpio = df.copy()
            for col in df_limpio.columns:
                if df_limpio[col].dtype in [np.float64, np.int64]:
                    df_limpio[col] = df_limpio[col].fillna(df_limpio[col].mean())
                else:
                    if not df_limpio[col].mode().empty:
                        df_limpio[col] = df_limpio[col].fillna(df_limpio[col].mode()[0])
            st.session_state['df'] = df_limpio
            st.success("¡Valores nulos imputados!")
            st.rerun()
            
        with c3:
            # Opción extra segura para convertir texto con formato de fecha a datetime real
            columnas_a_fecha = st.selectbox("Convertir columna a tipo Fecha:", ["Seleccionar"] + cat_cols)
            if columnas_a_fecha != "Seleccionar":
                if st.button("Convertir a Fecha"):
                    df_limpio = df.copy()
                    df_limpio[columnas_a_fecha] = pd.to_datetime(df_limpio[columnas_a_fecha], errors='coerce')
                    st.session_state['df'] = df_limpio
                    st.success(f"¡Columna '{columnas_a_fecha}' convertida a fecha!")
                    st.rerun()

    else:
        st.error("No hay datos para procesar. Vaya a la sección '2. Carga y Perfil'.")

# =====================================================
# SECCIÓN 4: ANÁLISIS VISUAL (BUG CORREGIDO DE DUPLICADOS EN EJES)
# =====================================================
elif pagina == "📊 4. Análisis Visual":
    st.title("📊 Analiza tu Data Aquí")
    
    if st.session_state['df'] is not None:
        df = st.session_state['df']
        
        # Extraer nombres de columnas por tipo para los selectores
        num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        
        tab_uni, tab_bi, tab_multi, tab_temp = st.tabs([
            "📈 Univariado", "♊ Bivariado", "💠 Multivariado", "⏳ Temporal"
        ])
        
        # --- UNIVARIADO ---
        with tab_uni:
            st.subheader("Distribución de una sola variable")
            col_sel = st.selectbox("Seleccione columna para analizar:", df.columns, key="uni")
            
            c1, c2 = st.columns(2)
            with c1:
                fig = px.histogram(df, x=col_sel, title=f"Histograma de {col_sel}", color_discrete_sequence=['#636EFA'])
                st.plotly_chart(fig, use_container_width=True)
            with c2:
                try:
                    fig2, ax2 = plt.subplots(figsize=(6, 4))
                    sns.boxplot(data=df, y=col_sel, ax=ax2, color="#00CC96")
                    ax2.set_title(f"Boxplot de {col_sel}")
                    st.pyplot(fig2)
                except Exception as e:
                    st.info("No se puede generar un diagrama de caja (boxplot) para datos que no sean numéricos.")

        # --- BIVARIADO ---
        with tab_bi:
            st.subheader("Relación entre dos variables")
            if len(num_cols) >= 1:
                c1, c2 = st.columns(2)
                with c1:
                    vx = st.selectbox("Seleccione Variable Eje X:", num_cols, key="bx")
                with c2:
                    # SOLUCIÓN BUG: Forzamos a que el eje Y seleccione el segundo elemento por defecto (si existe)
                    # para evitar que 'vx' y 'vy' apunten a la misma columna al inicio y explote Plotly Express/Narwhals
                    default_y_index = 1 if len(num_cols) > 1 else 0
                    vy = st.selectbox("Seleccione Variable Eje Y:", num_cols, index=default_y_index, key="by")
                
                # Control preventivo: Si el usuario selecciona manualmente la misma columna en ambos ejes
                if vx == vy:
                    st.warning("⚠️ Por favor, seleccione dos variables numéricas **diferentes** en el eje X y eje Y para evitar errores de graficación.")
                else:
                    try:
                        # Dibujamos el Scatter Plot interactivo de forma segura
                        fig_bi = px.scatter(df, x=vx, y=vy, trendline="ols", title=f"Dispersión: {vx} vs {vy}")
                        st.plotly_chart(fig_bi, use_container_width=True)
                    except Exception as e:
                        # Si falla el cálculo matemático de la línea de tendencia 'ols', graficamos sin ella de respaldo
                        fig_bi = px.scatter(df, x=vx, y=vy, title=f"Dispersión: {vx} vs {vy}")
                        st.plotly_chart(fig_bi, use_container_width=True)
            else:
                st.warning("Se requieren columnas numéricas en el dataset para realizar gráficos de dispersión.")

        # --- MULTIVARIADO ---
        with tab_multi:
            st.subheader("Análisis de múltiples dimensiones")
            if len(num_cols) >= 2:
                color_col = st.selectbox("Segmentar color por (Categoría):", [None] + cat_cols, key="multi_color")
                
                # Evitamos duplicación del primer índice usando el índice seguro para Y
                vy_idx = 1 if len(num_cols) > 1 else 0
                fig_multi = px.scatter(df, x=num_cols[0], y=num_cols[vy_idx], color=color_col, 
                                       title="Análisis Multivariado de Muestra")
                st.plotly_chart(fig_multi, use_container_width=True)
                
                st.markdown("**Matriz de Correlación Lineal (Heatmap)**")
                fig_corr, ax_corr = plt.subplots(figsize=(8, 5))
                sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax_corr, vmin=-1, vmax=1)
                st.pyplot(fig_corr)
            else:
                st.warning("Se requieren al menos 2 columnas numéricas para correlaciones.")

        # --- TEMPORAL ---
        with tab_temp:
            st.subheader("Análisis de Series de Tiempo")
            
            # Buscamos columnas de fecha explícitas o con nombres relacionados
            date_cols_actual = df.select_dtypes(include=['datetime64[ns]']).columns.tolist()
            potential_date_cols = date_cols_actual + [c for c in df.columns if any(k in c.lower() for k in ['date', 'fecha', 'year', 'año']) if c not in date_cols_actual]
            
            if potential_date_cols and num_cols:
                date_sel = st.selectbox("Seleccione columna de tiempo/fecha:", potential_date_cols, key="t_date")
                val_sel = st.selectbox("Seleccione valor métrico a medir:", num_cols, key="t_val")
                
                df_temp = df.copy()
                # Asegurar conversión temporal para evitar desfases de tipos en gráficos lineales
                df_temp[date_sel] = pd.to_datetime(df_temp[date_sel], errors='coerce')
                df_temp = df_temp.dropna(subset=[date_sel]).sort_values(date_sel)
                
                if not df_temp.empty:
                    fig_line = px.line(df_temp, x=date_sel, y=val_sel, title=f"Evolución de {val_sel} a lo largo de {date_sel}")
                    st.plotly_chart(fig_line, use_container_width=True)
                else:
                    st.error("La columna de tiempo seleccionada no contiene registros válidos o parseables.")
            else:
                st.info("No se detectaron columnas de tiempo estructuradas o variables numéricas para trazar gráficos temporales.")

    else:
        st.error("No hay datos para analizar. Vaya a la sección '2. Carga y Perfil'.")
