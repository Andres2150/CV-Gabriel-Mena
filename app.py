import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import re

# =====================================================
# 1. CONFIGURACIÓN DE LA PÁGINA
# =====================================================
st.set_page_config(
    page_title="Gabriel Mena | Portafolio Streamlit",
    page_icon="📊",
    layout="wide"
)

sns.set_theme(style="whitegrid")

# Inicialización obligatoria de st.session_state para conservar el dataset entre secciones
if 'df' not in st.session_state:
    st.session_state['df'] = None
if 'df_original' not in st.session_state:
    st.session_state['df_original'] = None

# =====================================================
# SIDEBAR / NAVEGACIÓN
# =====================================================
st.sidebar.title("📂 Gabriel Mena López")

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
st.sidebar.write("**Gabriel Andrés Mena López**")
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
        
        st.subheader("El Objetivo")
        st.info("""
        Construir una app en Streamlit capaz de procesar cualquiera de los cuatro datasets propuestos, 
        mostrando secciones de presentación, carga/procesamiento de datos y análisis visual mediante 
        gráficos interactivos.
        """)

        st.subheader("Tecnologías usadas")
        st.code("Python, Excel, GitHub, Streamlit, Pandas, Plotly, Seaborn, Matplotlib")

    with col2:
        st.header("Datos del Autor")
        st.markdown(f"### **Gabriel Andrés Mena López**")
        st.caption("Instituto DMC")
        st.write("""
        Profesional con amplia experiencia en el sector de hidrocarburos y GLP, especializado en análisis 
        comercial, inteligencia de negocios y gestión de información para la toma de decisiones. Cuento con 
        sólidos conocimientos de la cadena comercial de combustibles, normativa regulatoria del mercado 
        peruano y funcionamiento operativo del Sistema de Control de Órdenes de Pedido (SCOP).
        """)

    st.divider()
    
    st.header("Descripción de los cuatro datasets")
    d1, d2, d3, d4 = st.columns(4)
    
    with d1:
        st.markdown("📂 **Data 1: AI_Impact_on_Jobs_2030.csv**")
        st.caption("Mercado laboral e impacto de la inteligencia artificial en empleos, salarios, habilidades y demanda futura.")
    with d2:
        st.markdown("📂 **Data 2: sample_-_superstore.csv**")
        st.caption("Ventas de una tienda: pedidos, clientes, regiones, categorías, ventas, descuentos y utilidad.")
    with d3:
        st.markdown("📂 **Data 3: synthetic_ecommerce_order_risk_dataset.csv**")
        st.caption("Pedidos de e-commerce con variables de país, dispositivo, método de pago, valor de orden, entrega, devolución, fraude y etiqueta de riesgo.")
    with d4:
        st.markdown("📂 **Data 4: Teen_Mental_Health_Dataset.csv**")
        st.caption("Hábitos digitales, sueño, actividad física, interacción social y variables de bienestar en adolescentes.")


# =====================================================
# SECCIÓN 2: CARGA Y PERFIL DEL DATASET
# =====================================================
elif pagina == "📂 2. Carga y Perfil":
    st.title("📂 Módulo 2: Carga y Perfil del Dataset")
    
    opcion_carga = st.radio("Seleccione el origen del archivo:", ["Subir mi propio CSV", "Seleccionar un Dataset del Proyecto"], horizontal=True)
    df_cargado = None

    # Usar st.file_uploader() para cargar archivos .csv
    if opcion_carga == "Subir mi propio CSV":
        archivo = st.file_uploader("Cargar dataset (.csv)", type=["csv"])
        if archivo:
            try:
                df_cargado = pd.read_csv(archivo)
            except Exception as e:
                st.error(f"Error al leer el archivo CSV: {e}")
    else:
        dataset_selec = st.selectbox("Elija uno de los datasets predefinidos:", [
            "AI_Impact_on_Jobs_2030.csv", 
            "sample_-_superstore.csv", 
            "synthetic_ecommerce_order_risk_dataset.csv", 
            "Teen_Mental_Health_Dataset.csv"
        ])
        try:
            df_cargado = pd.read_csv(dataset_selec)
        except Exception:
            st.warning(f"Archivo '{dataset_selec}' no encontrado localmente. Por favor, sube tu propio archivo usando la opción 'Subir mi propio CSV'.")

    # Validar obligatoriamente que el archivo fue cargado antes de ejecutar análisis
    if df_cargado is not None:
        # Se guarda tanto el original como el de trabajo en st.session_state para persistencia entre navegación
        st.session_state['df_original'] = df_cargado.copy()
        if st.session_state['df'] is None:
            st.session_state['df'] = df_cargado.copy()
            
        df_actual = st.session_state['df']
        st.success("¡Dataset inicializado y guardado en memoria de sesión!")

        # Identificación de tipos de columnas mediante funciones controladas
        num_cols = df_actual.select_dtypes(include=[np.number]).columns.tolist()
        cat_cols = df_actual.select_dtypes(include=['object', 'category']).columns.tolist()
        date_cols = df_actual.select_dtypes(include=['datetime64[ns]']).columns.tolist()

        # Incluir métricas rápidas requeridas en el módulo
        st.subheader("📊 Métricas Rápidas del Dataset")
        m1, m2, m3, m4, m5, m6 = st.columns(6)
        m1.metric("Número de Filas", df_actual.shape[0])
        m2.metric("Número de Columnas", df_actual.shape[1])
        m3.metric("Var. Numéricas", len(num_cols))
        m4.metric("Var. Categóricas", len(cat_cols))
        m5.metric("Valores Nulos", df_actual.isnull().sum().sum())
        m6.metric("Reg. Duplicados", df_actual.duplicated().sum())

        # Mostrar mensajes claros si el dataset carece de algún tipo de variable
        if not num_cols: st.info("ℹ️ El dataset no contiene variables numéricas detectadas.")
        if not cat_cols: st.info("ℹ️ El dataset no contiene variables categóricas detectadas.")
        if not date_cols: st.info("ℹ️ El dataset no contiene variables explícitas de tipo fecha.")

        st.divider()

        # Permitir seleccionar columnas relevantes mediante selectbox o multiselect
        st.subheader("🎯 Selección de Columnas para Análisis")
        columnas_filtradas = st.multiselect(
            "Seleccione las columnas que desea conservar para trabajar (Por defecto se muestran todas):",
            options=df_actual.columns.tolist(),
            default=df_actual.columns.tolist()
        )
        
        if columnas_filtradas:
            df_actual = df_actual[columnas_filtradas]
            st.session_state['df'] = df_actual
        else:
            st.warning("⚠️ Debes seleccionar al menos una columna.")

        # Mostrar head(), dimensiones, nombres de columnas y tipos de datos
        st.subheader("👀 Estructura y Vista Previa de los Datos Seleccionados")
        tab_head, tab_types = st.tabs(["📋 Head (Primeras 10 filas)", "🧬 Columnas y Tipos de Datos"])
        
        with tab_head:
            st.dataframe(df_actual.head(10), use_container_width=True)
            st.caption(f"Dimensiones actuales: {df_actual.shape[0]} filas x {df_actual.shape[1]} columnas.")
            
        with tab_types:
            info_dtypes = pd.DataFrame({
                "Nombre de Columna": df_actual.columns,
                "Tipo de Dato": [str(t) for t in df_actual.dtypes]
            })
            st.dataframe(info_dtypes, use_container_width=True)
    else:
        st.info("A la espera de la carga de un archivo para inicializar el perfilamiento.")


# =====================================================
# SECCIÓN 3: PROCESAMIENTO DE DATOS (FLEXIBLE)
# =====================================================
elif pagina == "⚙️ 3. Procesamiento":
    st.title("⚙️ Módulo 3: Procesamiento de Datos")
    st.write("Detección flexible y automática según la estructura interna del archivo cargado. Herramientas de ajuste estructural y control de calidad.")

    if st.session_state['df'] is not None:
        df = st.session_state['df']

        # Detección automática y flexible de tipos de variables usando funciones nativas limpias
        num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        date_cols = df.select_dtypes(include=['datetime64[ns]']).columns.tolist()

        # 1. Herramienta: Estandarizar nombres de columnas si es necesario
        st.subheader("🔤 1. Estandarización de Estructura")
        if st.button("Estandarizar Nombres de Columnas"):
            try:
                # Reemplaza espacios por guiones bajos, remueve caracteres especiales y convierte a minúsculas
                nuevos_nombres = {col: re.sub(r'[^a-zA-Z0-9_]', '', col.replace(' ', '_')).lower() for col in df.columns}
                df = df.rename(columns=nuevos_nombres)
                st.session_state['df'] = df
                st.success("¡Columnas estandarizadas! (Ej: 'Ventas Totales (%)' -> 'ventas_totales')")
                st.rerun()
            except Exception as e:
                st.error(f"No se pudieron estandarizar las columnas de forma automática: {e}")

        # 2. Herramienta: Convertir columnas de fecha cuando existan
        if cat_cols:
            col_a_fecha = st.selectbox("Convertir columna categórica/texto a Tipo Fecha:", ["Ninguna"] + cat_cols)
            if col_a_fecha != "Ninguna":
                if st.button("Aplicar Conversión de Fecha"):
                    try:
                        df[col_a_fecha] = pd.to_datetime(df[col_a_fecha], errors='coerce')
                        st.session_state['df'] = df
                        st.success(f"¡Columna '{col_a_fecha}' convertida a formato temporal con éxito!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error al transformar a fecha: {e}")

        st.divider()

        # 3. Herramienta: Calcular valores faltantes por columna y porcentaje de nulos
        st.subheader("🔍 2. Diagnóstico de Integridad e Imputación")
        nulos_conteo = df.isnull().sum()
        nulos_porcentaje = (df.isnull().sum() / len(df)) * 100
        
        reporte_nulos = pd.DataFrame({
            "Valores Faltantes": nulos_conteo,
            "Porcentaje de Nulos (%)": nulos_porcentaje.round(2)
        })
        st.dataframe(reporte_nulos, use_container_width=True)

        # Detectar duplicados y reportar su cantidad
        duplicados_cant = df.duplicated().sum()
        if duplicados_cant > 0:
            st.warning(f"⚠️ Se detectaron {duplicados_cant} registros exactamente idénticos (duplicados).")
            if st.button("Eliminar registros duplicados automáticamente"):
                df = df.drop_duplicates()
                st.session_state['df'] = df
                st.success("¡Duplicados eliminados!")
                st.rerun()
        else:
            st.success("✨ El conjunto de datos no presenta filas duplicadas.")

        st.divider()

        # 4. Herramienta: Identificar outliers en variables numéricas usando IQR
        st.subheader("📈 3. Análisis de Outliers (Método IQR)")
        if num_cols:
            col_outlier_analisis = st.selectbox("Seleccione columna numérica para calcular Outliers:", num_cols)
            try:
                q1 = df[col_outlier_analisis].quantile(0.25)
                q3 = df[col_outlier_analisis].quantile(0.75)
                iqr = q3 - q1
                limite_inferior = q1 - 1.5 * iqr
                limite_superior = q3 + 1.5 * iqr
                
                outliers_df = df[(df[col_outlier_analisis] < limite_inferior) | (df[col_outlier_analisis] > limite_superior)]
                
                c_out1, c_out2 = st.columns(2)
                c_out1.metric("Cantidad de Outliers Detectados", len(outliers_df))
                c_out2.metric("Porcentaje del Total", f"{((len(outliers_df)/len(df))*100):.2f}%")
                
                if len(outliers_df) > 0:
                    with st.expander("Ver registros considerados Outliers"):
                        st.dataframe(outliers_df, use_container_width=True)
            except Exception as e:
                st.warning(f"No se pudieron calcular los outliers para {col_outlier_analisis}: {e}")
        else:
            st.info("No hay columnas numéricas disponibles para calcular métricas de dispersión (IQR).")

        st.divider()

        # 5. Herramienta: Permitir filtros dinámicos por categorías, rangos numéricos o fechas en el Sidebar
        st.subheader("🎛️ 4. Configuración de Filtros Dinámicos de Trabajo")
        st.info("Los filtros configurados aquí afectarán la data que se visualiza e interpreta en el siguiente módulo de Análisis Visual.")
        
        # Guardamos filtros en la barra lateral de forma dinámica según disponibilidad
        st.sidebar.markdown("### 🛠️ Filtros Dinámicos")
        df_filtrado = df.copy()

        # Filtro numérico si aplica
        if num_cols:
            col_f_num = st.sidebar.selectbox("Filtrar Rango Numérico:", ["Ninguno"] + num_cols)
            if col_f_num != "Ninguno":
                min_val = float(df[col_f_num].min())
                max_val = float(df[col_f_num].max())
                if min_val != max_val:
                    rango = st.sidebar.slider(f"Rango de {col_f_num}", min_val, max_val, (min_val, max_val))
                    df_filtrado = df_filtrado[(df_filtrado[col_f_num] >= rango[0]) & (df_filtrado[col_f_num] <= rango[1])]

        # Filtro categórico si aplica
        if cat_cols:
            col_f_cat = st.sidebar.selectbox("Filtrar por Categoría:", ["Ninguno"] + cat_cols)
            if col_f_cat != "Ninguno":
                opciones_cat = df[col_f_cat].dropna().unique().tolist()
                seleccion_cat = st.sidebar.multiselect(f"Valores de {col_f_cat}", opciones_cat, default=opciones_cat[:3])
                if seleccion_cat:
                    df_filtrado = df_filtrado[df_filtrado[col_f_cat].isin(seleccion_cat)]

        # Filtro de fechas si aplica
        if date_cols:
            col_f_fec = st.sidebar.selectbox("Filtrar por Rango Temporal:", ["Ninguno"] + date_cols)
            if col_f_fec != "Ninguno":
                min_date = df[col_f_fec].min()
                max_date = df[col_f_fec].max()
                rango_fecha = st.sidebar.date_input(f"Fechas de {col_f_fec}", [min_date, max_date])
                if len(rango_fecha) == 2:
                    df_filtrado = df_filtrado[(df_filtrado[col_f_fec].dt.date >= rango_fecha[0]) & (df_filtrado[col_f_fec].dt.date <= rango_fecha[1])]

        if st.sidebar.button("💾 Guardar y Aplicar Filtros"):
            st.session_state['df'] = df_filtrado
            st.success(f"¡Filtros aplicados! El dataset se redujo a {df_filtrado.shape[0]} filas.")
            st.rerun()

        if st.button("🔄 Restablecer Dataset Original sin Filtros"):
            st.session_state['df'] = st.session_state['df_original'].copy()
            st.success("Se han eliminado todas las modificaciones y filtros.")
            st.rerun()

    else:
        st.error("No hay datos cargados en la sesión. Diríjase al Módulo 2 para inicializar.")


# =====================================================
# SECCIÓN 4: ANÁLISIS VISUAL
# =====================================================
elif pagina == "📊 4. Análisis Visual":
    st.title("🚀 Advanced Analytics Dashboard")
    st.write("Sección ANALIZA TU DATA organizada dinámicamente mediante pestañas.")
    
    st.divider()

    if st.session_state['df'] is not None:
        df = st.session_state['df']
        
        num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📊 Exploración",
            "🔍 Calidad de Datos",
            "📉 Visualización Avanzada",
            "🤖 Análisis Estadístico",
            "⚠️ Detección de Anomalías",
        ])

        # --- TAB 1: EXPLORACIÓN ---
        with tab1:
            st.subheader("Vista Previa del Dataset Filtrado")
            st.dataframe(df.head(10), use_container_width=True)
            st.write(f"Dimensiones de trabajo actuales: {df.shape[0]} filas, {df.shape[1]} columnas")

        # --- TAB 2: CALIDAD DE DATOS ---
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
            nulos_por_col = df.isnull().sum()
            nulos_activos = nulos_por_col[nulos_por_col > 0]

            if not nulos_activos.empty:
                st.warning(f"Se encontraron valores nulos en {len(nulos_activos)} columnas.")
                st.bar_chart(nulos_activos)
            else:
                st.success("¡Integridad de datos: Sin valores nulos detectados!")
                datos_cero = pd.DataFrame({"Nulos": 0}, index=df.columns)
                st.bar_chart(datos_cero)

        # --- TAB 3: VISUALIZACIÓN AVANZADA ---
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
                key="tipo_graf_suite"
            )

            c1, c2 = st.columns(2)
            with c1:
                col_x = st.selectbox("Eje X", df.columns, key="v_suite_x")
            with c2:
                default_idx = 1 if len(num_cols) > 1 else 0
                col_y = st.selectbox("Eje Y (Numérico)", num_cols, index=default_idx, key="v_suite_y")

            if tipo_graf == "Relación (Plotly)":
                if col_x == col_y:
                    st.warning("⚠️ Selecciona columnas diferentes para el Eje X y el Eje Y para evitar conflictos.")
                else:
                    fig = px.scatter(df, x=col_x, y=col_y, color=df.columns[0], template="plotly_white")
                    st.plotly_chart(fig, use_container_width=True)

            elif tipo_graf == "Distribución (Seaborn)":
                if num_cols:
                    fig, ax = plt.subplots(figsize=(10, 5))
                    sns.histplot(df[col_y], kde=True, color="teal", ax=ax)
                    st.pyplot(fig)
                else:
                    st.warning("No hay columnas numéricas para graficar distribuciones.")

            elif tipo_graf == "Correlación (Heatmap)":
                if len(num_cols) >= 2:
                    corr = df[num_cols].corr()
                    mask = np.triu(np.ones_like(corr, dtype=bool))
                    fig, ax = plt.subplots(figsize=(10, 8))
                    sns.heatmap(corr, mask=mask, annot=True, cmap="coolwarm", fmt=".2f", ax=ax, square=True)
                    st.pyplot(fig)
                else:
                    st.warning("Se necesitan al menos 2 variables numéricas para correlaciones.")

            elif tipo_graf == "Boxplot (Outliers)":
                if num_cols:
                    fig = px.box(df, y=col_y, title=f"Outliers: {col_y}", template="plotly_white")
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("Requiere columnas numéricas.")

            elif tipo_graf == "Densidad (Skew/Kurt)":
                if num_cols:
                    from scipy.stats import shapiro
                    skew = df[col_y].skew()
                    kurt = df[col_y].kurt()
                    
                    df_clean = df[col_y].dropna()
                    if len(df_clean) > 5000:
                        df_clean = df_clean.sample(5000, random_state=42)
                    
                    if len(df_clean) >= 3:
                        stat, p = shapiro(df_clean)
                        p_val_str = f"{p:.4f}"
                    else:
                        p_val_str = "Insuficientes datos"

                    fig, ax = plt.subplots(figsize=(10, 4))
                    sns.kdeplot(df[col_y], fill=True, color="purple", ax=ax)
                    ax.set_title(f"Normalidad: P-value {p_val_str} | Skew: {skew:.2f} | Kurt: {kurt:.2f}")
                    st.pyplot(fig)

        # --- TAB 4: ANÁLISIS ESTADÍSTICO ---
        with tab4:
            st.subheader("Resumen Estadístico Profundo")
            if num_cols:
                resumen = df.describe().T
                resumen["skew"] = df.skew(numeric_only=True)
                resumen["kurt"] = df.kurt(numeric_only=True)
                st.dataframe(resumen, use_container_width=True)
            else:
                st.info("No hay columnas numéricas para extraer un resumen descriptivo profundo.")

        # --- TAB 5: DETECCIÓN DE ANOMALÍAS ---
        with tab5:
            st.subheader("⚠️ Detección Automática de Anomalías")
            umbral = st.slider("Seleccionar umbral de Z-Score", 1.5, 3.5, 3.0, key="sensibilidad_z")
            col_outlier = st.selectbox("Seleccionar columna para buscar anomalías", num_cols, key="outlier_target")

            if col_outlier:
                if df[col_outlier].std() == 0:
                    st.error("No es posible calcular anomalías en una columna con desviación estándar de cero.")
                else:
                    z_scores = np.abs((df[col_outlier] - df[col_outlier].mean()) / df[col_outlier].std())
                    anomalies = df[z_scores > umbral]

                    if not anomalies.empty:
                        st.warning(f"Se detectaron {len(anomalies)} filas fuera del rango estadístico.")
                        st.dataframe(anomalies, use_container_width=True)
                    else:
                        st.success("¡No se detectaron anomalías significativas con este umbral!")
    else:
        st.error("No hay datos para analizar. Vaya primero a la sección '2. Carga y Perfil'.")
