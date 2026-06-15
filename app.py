# Presentación del Proyecto
# Esta es una Aplicación Interactiva construida íntegramente en Python con Streamlit. 
# El objetivo es demostrar la capacidad de procesar, limpiar y analizar visualmente diversos conjuntos de datos de manera automatizada y dinámica.

# Realizado por GABRIEL ANDRES MENA LOPEZ 
# DMC PERU 

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import re

# 1. CONFIGURACIÓN DE LA PÁGINA

st.set_page_config(
    page_title="Gabriel Mena | Portafolio Streamlit",
    page_icon="📊",
    layout="wide"
)

# Configuración de estilos globales para gráficos estáticos
sns.set_theme(style="whitegrid")

# Inicialización de st.session_state para conservar el dataset entre secciones
if 'df' not in st.session_state:
    st.session_state['df'] = None
if 'df_original' not in st.session_state:
    st.session_state['df_original'] = None


# SIDEBAR / NAVEGACIÓN

st.sidebar.title("Gabriel Mena López")

pagina = st.sidebar.radio(
    "Seleccione una sección",
    [
        "Home",
        "2. Carga y Perfil",
        "3. Procesamiento",
        "4. Análisis Visual"
    ]
)

st.sidebar.markdown("---")
st.sidebar.write("**Gabriel Andrés Mena López**")
st.sidebar.write("Business Intelligence & Data Analytics")
st.sidebar.write("gmena50@gmail.com")
st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/andresmena1/)")

#SECCIÓN 1: HOME

if pagina == "Home":
    st.title("Portafolio Profesional: Data Analytics App")
    
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
        st.markdown("**Data 1: AI_Impact_on_Jobs_2030.csv**")
        st.caption("Mercado laboral e impacto de la inteligencia artificial en empleos, salarios, habilidades y demanda futura.")
    with d2:
        st.markdown("**Data 2: sample_-_superstore.csv**")
        st.caption("Ventas de una tienda: pedidos, clientes, regiones, categorías, ventas, descuentos y utilidad.")
    with d3:
        st.markdown("**Data 3: synthetic_ecommerce_order_risk_dataset.csv**")
        st.caption("Pedidos de e-commerce con variables de país, dispositivo, método de pago, valor de orden, entrega, devolución, fraude y etiqueta de riesgo.")
    with d4:
        st.markdown("**Data 4: Teen_Mental_Health_Dataset.csv**")
        st.caption("Hábitos digitales, sueño, actividad física, interacción social y variables de bienestar en adolescentes.")

# SECCIÓN 2: CARGA Y PERFIL DEL DATASET
elif pagina == "2. Carga y Perfil":
    st.title("Módulo 2: Carga y Perfil del Dataset")
    st.write("Permitir cargar el archivo CSV con st.file_uploader() o seleccionar uno de los datasets del proyecto. Mostrar vista previa, dimensiones, columnas, tipos de datos y resumen inicial.")
    
    st.divider()
    opcion_carga = st.radio("Seleccione el origen del archivo:", ["Subir mi propio CSV", "Seleccionar un Dataset del Proyecto"], horizontal=True)
    
    df_cargado = None

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

    if df_cargado is not None:
        st.session_state['df_original'] = df_cargado.copy()
        
        if (st.session_state['df'] is None or 
            not st.session_state['df'].columns.equals(df_cargado.columns) or 
            len(st.session_state['df']) != len(df_cargado)):
            
            st.session_state['df'] = df_cargado.copy()
            st.rerun()
            
        df_actual = st.session_state['df']
        st.success("¡Dataset inicializado y guardado en memoria de sesión!")

        # Clasificación automática de variables
        num_cols = df_actual.select_dtypes(include=[np.number]).columns.tolist()
        cat_cols = df_actual.select_dtypes(include=['object', 'category']).columns.tolist()
        date_cols = df_actual.select_dtypes(include=['datetime64[ns]']).columns.tolist()

        st.subheader("Métricas Rápidas del Dataset")
        m1, m2, m3, m4, m5, m6 = st.columns(6)
        m1.metric("Número de Filas", df_actual.shape[0])
        m2.metric("Número de Columnas", df_actual.shape[1])
        m3.metric("Var. Numéricas", len(num_cols))
        m4.metric("Var. Categóricas", len(cat_cols))
        m5.metric("Valores Nulos", df_actual.isnull().sum().sum())
        m6.metric("Reg. Duplicados", df_actual.duplicated().sum())

        if not num_cols: st.info("El dataset no contiene variables numéricas detectadas.")
        if not cat_cols: st.info("El dataset no contiene variables categóricas detectadas.")
        if not date_cols: st.info("El dataset no contiene variables explícitas de tipo fecha.")

        st.divider()

        st.subheader("Selección de Columnas para Análisis")
        columnas_filtradas = st.multiselect(
            "Seleccione las columnas que desea conservar para trabajar (Por defecto se muestran todas):",
            options=df_actual.columns.tolist(),
            default=df_actual.columns.tolist()
        )
        
        if columnas_filtradas:
            df_actual = df_actual[columnas_filtradas]
            st.session_state['df'] = df_actual
        else:
            st.warning("Debes seleccionar al menos una columna.")

        st.subheader("Estructura y Vista Previa de los Datos Seleccionados")
        tab_head, tab_types = st.tabs(["Head (Primeras 10 filas)", "Columnas y Tipos de Datos"])
        
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

# SECCIÓN 3: PROCESAMIENTO DE DATOS (FLEXIBLE)

elif pagina == "3. Procesamiento":
    st.title("Módulo 3: Procesamiento de Datos")
    st.write("Detección flexible y automática según la estructura interna del archivo cargado. Herramientas de ajuste estructural y control de calidad.")

    if st.session_state['df'] is not None:
        df = st.session_state['df']

        num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        date_cols = df.select_dtypes(include=['datetime64[ns]']).columns.tolist()

        st.subheader("1. Estandarización de Estructura")
        if st.button("Estandarizar Nombres de Columnas"):
            try:
                nuevos_nombres = {col: re.sub(r'[^a-zA-Z0-9_]', '', col.replace(' ', '_')).lower() for col in df.columns}
                df = df.rename(columns=nuevos_nombres)
                st.session_state['df'] = df
                st.success("¡Columnas estandarizadas con éxito!")
                st.rerun()
            except Exception as e:
                st.error(f"No se pudieron estandarizar las columnas de forma automática: {e}")

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

        st.subheader("2. Diagnóstico de Integridad e Imputación")
        nulos_conteo = df.isnull().sum()
        nulos_porcentaje = (df.isnull().sum() / len(df)) * 100
        
        reporte_nulos = pd.DataFrame({
            "Valores Faltantes": nulos_conteo,
            "Porcentaje de Nulos (%)": nulos_porcentaje.round(2)
        })
        st.dataframe(reporte_nulos, use_container_width=True)

        duplicados_cant = df.duplicated().sum()
        if duplicados_cant > 0:
            st.warning(f"Se detectaron {duplicados_cant} registros exactamente idénticos (duplicados).")
            if st.button("Eliminar registros duplicados automáticamente"):
                df = df.drop_duplicates()
                st.session_state['df'] = df
                st.success("¡Duplicados eliminados!")
                st.rerun()
        else:
            st.success("El conjunto de datos no presenta filas duplicadas.")

        st.divider()

        st.subheader("3. Análisis de Outliers (Método IQR)")
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

        st.subheader("4. Configuración de Filtros Dinámicos de Trabajo")
        st.info("Los filtros configurados aquí afectarán de manera transversal a la visualización de la sección final.")
        
        st.sidebar.markdown("### Filtros Dinámicos")
        df_filtrado = df.copy()

        if num_cols:
            col_f_num = st.sidebar.selectbox("Filtrar Rango Numérico:", ["Ninguno"] + num_cols)
            if col_f_num != "Ninguno":
                min_val = float(df[col_f_num].min())
                max_val = float(df[col_f_num].max())
                if min_val != max_val:
                    rango = st.sidebar.slider(f"Rango de {col_f_num}", min_val, max_val, (min_val, max_val))
                    df_filtrado = df_filtrado[(df_filtrado[col_f_num] >= rango[0]) & (df_filtrado[col_f_num] <= rango[1])]

        if cat_cols:
            col_f_cat = st.sidebar.selectbox("Filtrar por Categoría:", ["Ninguno"] + cat_cols)
            if col_f_cat != "Ninguno":
                opciones_cat = df[col_f_cat].dropna().unique().tolist()
                seleccion_cat = st.sidebar.multiselect(f"Valores de {col_f_cat}", opciones_cat, default=opciones_cat[:3])
                if seleccion_cat:
                    df_filtrado = df_filtrado[df_filtrado[col_f_cat].isin(seleccion_cat)]

        if date_cols:
            col_f_fec = st.sidebar.selectbox("Filtrar por Rango Temporal:", ["Ninguno"] + date_cols)
            if col_f_fec != "Ninguno":
                min_date = df[col_f_fec].min()
                max_date = df[col_f_fec].max()
                rango_fecha = st.sidebar.date_input(f"Fechas de {col_f_fec}", [min_date, max_date])
                if len(rango_fecha) == 2:
                    df_filtrado = df_filtrado[(df_filtrado[col_f_fec].dt.date >= rango_fecha[0]) & (df_filtrado[col_f_fec].dt.date <= rango_fecha[1])]

        if st.sidebar.button("Guardar y Aplicar Filtros"):
            st.session_state['df'] = df_filtrado
            st.success(f"¡Filtros aplicados! {df_filtrado.shape[0]} filas resultantes.")
            st.rerun()

        if st.button("Restablecer Dataset Original sin Filtros"):
            st.session_state['df'] = st.session_state['df_original'].copy()
            st.success("Se han eliminado todas las modificaciones y filtros.")
            st.rerun()
    else:
        st.error("No hay datos cargados en la sesión. Diríjase al Módulo 2 para inicializar.")


# SECCIÓN 4: ANÁLISIS VISUAL OBLIGATORIO

elif pagina == "4. Análisis Visual":
    st.title("Módulo 4: Análisis Visual Obligatorio")
    st.write("Ecosistema modular de visualizaciones interactivas avanzado para la exploración analítica completa.")
    st.divider()

    if st.session_state['df'] is not None:
        df = st.session_state['df']
        
        # Mapeo y clasificación de columnas
        num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        date_cols = df.select_dtypes(include=['datetime64[ns]']).columns.tolist()
        bin_cols = [col for col in df.columns if df[col].dropna().nunique() == 2]

        # Estructuración obligatoria mediante 6 st.tabs()
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "Tab 1: Resumen",
            "Tab 2: Análisis Univariado",
            "Tab 3: Análisis Bivariado",
            "Tab 4: Análisis Multivariado",
            "Tab 5: Análisis Temporal",
            "Tab 6: Insights"
        ])

        # --- TAB 1: RESUMEN ---
        with tab1:
            st.subheader("Estado Estructural del Dataset")
            
            c1, col_m1, col_m2, col_m3 = st.columns([1, 1, 1, 1])
            with c1: st.metric("Dimensión del Dataframe", f"{df.shape[0]} x {df.shape[1]}")
            with col_m1: st.metric("Variables Binarias", len(bin_cols))
            with col_m2: st.metric("Total de Nulos", df.isnull().sum().sum())
            with col_m3: st.metric("Filas Duplicadas", df.duplicated().sum())
            
            st.divider()
            
            c_check1, c_check2 = st.columns(2)
            mostrar_crudos = c_check1.checkbox("Mostrar Muestra de Datos Crudos (Head)")
            mostrar_desc = c_check2.checkbox("Mostrar Descripción Estadística Detallada")
            
            col_t1, col_t2 = st.columns(2)
            with col_t1:
                if mostrar_crudos:
                    st.markdown("**Muestra de Registros (Head)**")
                    st.dataframe(df.head(5), use_container_width=True)
                else:
                    st.info("Activa el checkbox superior para inspeccionar la muestra de filas (datos crudos).")
            with col_t2:
                st.markdown("**Metadatos y Tipos de Datos**")
                meta_df = pd.DataFrame({
                    "Tipo de columna": [str(t) for t in df.dtypes],
                    "Nulos totales": df.isnull().sum().values,
                    "¿Es Binaria?": ["Sí" if c in bin_cols else "No" for c in df.columns]
                }, index=df.columns)
                st.dataframe(meta_df, use_container_width=True)
                
            st.divider()
            
            if mostrar_desc:
                st.markdown("**Resumen Estadístico Numérico Descriptivo Completo**")
                if num_cols:
                    resumen_est = df.describe().T
                    resumen_est["skewness (Asimetría)"] = df.skew(numeric_only=True)
                    st.dataframe(resumen_est, use_container_width=True)
                else:
                    st.info("Sin variables numéricas para calcular resúmenes descriptivos.")

        # --- TAB 2: ANÁLISIS UNIVARIADO ---
        with tab2:
            st.subheader("Exploración Individual de Variables")
            opcion_uni = st.radio("Tipo de variable a inspeccionar:", ["Numéricas", "Categóricas / Binarias"], horizontal=True, key="op_uni")
            
            if opcion_uni == "Numéricas" and num_cols:
                col_sel_u = st.selectbox("Seleccione Variable Numérica:", num_cols, key="sb_uni_num")
                
                col_g1, col_g2 = st.columns(2)
                with col_g1:
                    fig_hist = px.histogram(df, x=col_sel_u, title=f"Histograma de Distribución: {col_sel_u}", color_discrete_sequence=["#1f77b4"])
                    st.plotly_chart(fig_hist, use_container_width=True)
                with col_g2:
                    fig_box = px.box(df, y=col_sel_u, title=f"Diagrama de Caja (Boxplot) & Outliers: {col_sel_u}", color_discrete_sequence=["#2ca02c"])
                    st.plotly_chart(fig_box, use_container_width=True)
                    
            elif opcion_uni == "Categóricas / Binarias" and cat_cols:
                col_sel_c = st.selectbox("Seleccione Variable Categórica:", cat_cols, key="sb_uni_cat")
                
                conteo_cats = df[col_sel_c].value_counts().reset_index()
                conteo_cats.columns = [col_sel_c, 'Conteo']
                conteo_cats['Proporción (%)'] = ((conteo_cats['Conteo'] / len(df)) * 100).round(2)
                
                col_gc1, col_gc2 = st.columns(2)
                with col_gc1:
                    st.markdown(f"**Distribución de frecuencias para {col_sel_c}**")
                    st.dataframe(conteo_cats, use_container_width=True)
                with col_gc2:
                    fig_bar = px.bar(conteo_cats, x=col_sel_c, y='Conteo', text='Proporción (%)', title=f"Frecuencias de {col_sel_c}", color=col_sel_c)
                    st.plotly_chart(fig_bar, use_container_width=True)
            else:
                st.warning("No existen variables aptas en esta categoría para mapear la distribución.")

        # --- TAB 3: ANÁLISIS BIVARIADO ---
        with tab3:
            st.subheader("Comparación e Interacción de Variables")
            tipo_bivariado = st.selectbox("Seleccione el enfoque del análisis bivariado:", [
                "Numérica vs Numérica (Scatter Plot)",
                "Numérica por Categoría (Boxplot Comparativo)",
                "Categórica vs Categórica (Barras Agrupadas)"
            ])
            
            if tipo_bivariado == "Numérica vs Numérica (Scatter Plot)" and len(num_cols) >= 1:
                c_bx1, c_bx2 = st.columns(2)
                with c_bx1: bx_x = st.selectbox("Variable Eje X (Numérica):", num_cols, key="bx_x")
                with c_bx2: 
                    b_idx = 1 if len(num_cols) > 1 else 0
                    bx_y = st.selectbox("Variable Eje Y (Numérica):", num_cols, index=b_idx, key="bx_y")
                
                if bx_x == bx_y:
                    st.warning("Por favor, seleccione variables distintas en cada eje.")
                else:
                    fig_scat = px.scatter(df, x=bx_x, y=bx_y, title=f"Dispersión e Interacción: {bx_x} vs {bx_y}", template="plotly_white")
                    st.plotly_chart(fig_scat, use_container_width=True)
                    
            elif tipo_bivariado == "Numérica por Categoría (Boxplot Comparativo)" and num_cols and cat_cols:
                c_bxc1, c_bxc2 = st.columns(2)
                with c_bxc1: box_cat = st.selectbox("Variable Categórica (Agrupador):", cat_cols, key="box_cat")
                with c_bxc2: box_num = st.selectbox("Variable Numérica (Métrica):", num_cols, key="box_num")
                
                fig_box_comp = px.box(df, x=box_cat, y=box_num, color=box_cat, title=f"Distribución de {box_num} según {box_cat}")
                st.plotly_chart(fig_box_comp, use_container_width=True)
                
            elif tipo_bivariado == "Categórica vs Categórica (Barras Agrupadas)" and len(cat_cols) >= 2:
                c_bg1, c_bg2 = st.columns(2)
                with c_bg1: bar_c1 = st.selectbox("Categoría Principal (Eje X):", cat_cols, key="bar_c1")
                with c_bg2: bar_c2 = st.selectbox("Categoría de Cruce (Color):", cat_cols, index=1 if len(cat_cols)>1 else 0, key="bar_c2")
                
                df_cross = df.groupby([bar_c1, bar_c2]).size().reset_index(name='Conteo')
                fig_grouped_bar = px.bar(df_cross, x=bar_c1, y='Conteo', color=bar_c2, barmode="group", title=f"Cruce de frecuencias: {bar_c1} vs {bar_c2}")
                st.plotly_chart(fig_grouped_bar, use_container_width=True)
            else:
                st.warning("No se cuenta con la combinación requerida de variables en el archivo actual.")

        # --- TAB 4: ANÁLISIS MULTIVARIADO ---
        with tab4:
            st.subheader("Análisis Multidimensional y Correlaciones Estructuradas")
            col_m1, col_m2 = st.columns([1, 2])
            
            with col_m1:
                st.markdown("**Matriz de Correlación Lineal**")
                if len(num_cols) >= 2:
                    corr_mat = df[num_cols].corr()
                    mask = np.triu(np.ones_like(corr_mat, dtype=bool))
                    
                    fig_hm, ax_hm = plt.subplots(figsize=(6, 5))
                    sns.heatmap(corr_mat, mask=mask, annot=True, cmap="coolwarm", fmt=".2f", ax=ax_hm, cbar=True, square=True)
                    st.pyplot(fig_hm)
                else:
                    st.info("Se necesitan al menos dos variables numéricas en el dataset para estructurar el Heatmap de correlación.")
                    
            with col_m2:
                st.markdown("**Análisis combinado de tres variables (Segmentación Completa)**")
                if len(num_cols) >= 2 and cat_cols:
                    mx = st.selectbox("Eje X (Numérico):", num_cols, key="mx")
                    my = st.selectbox("Eje Y (Numérico):", num_cols, index=1 if len(num_cols)>1 else 0, key="my")
                    m_color = st.selectbox("Segmentación por Categoría (Color):", cat_cols, key="m_color")
                    
                    if mx != my:
                        fig_multi_scat = px.scatter(df, x=mx, y=my, color=m_color, title=f"Gráfico Multivariado: {mx} vs {my} por {m_color}", template="plotly_white")
                        st.plotly_chart(fig_multi_scat, use_container_width=True)
                else:
                    st.info("Insuficientes variables numéricas o categóricas para habilitar el gráfico de dispersión tri-variable.")

        # --- TAB 5: ANÁLISIS TEMPORAL ---
        with tab5:
            st.subheader("Análisis Evolutivo y Tendencias en el Tiempo")
            potenciales_fechas = date_cols + [c for c in df.columns if any(k in c.lower() for k in ['date', 'fecha', 'year', 'año']) if c not in date_cols]
            
            if potenciales_fechas and num_cols:
                c_t1, c_t2 = st.columns(2)
                with c_t1: date_target = st.selectbox("Seleccione la Variable Temporal/Fecha:", potenciales_fechas, key="dt_t")
                with c_t2: metric_target = st.selectbox("Seleccione la Métrica a Evaluar:", num_cols, key="mt_t")
                
                df_t = df.copy()
                df_t[date_target] = pd.to_datetime(df_t[date_target], errors='coerce')
                df_t = df_t.dropna(subset=[date_target]).sort_values(date_target)
                
                if not df_t.empty:
                    agrupar_por_mes = st.checkbox("Agrupar métrica promediada por Mes/Año para suavizar tendencia")
                    
                    if agrupar_por_mes:
                        df_t['Periodo'] = df_t[date_target].dt.to_period('M').astype(str)
                        df_g_temp = df_t.groupby('Periodo')[metric_target].mean().reset_index()
                        fig_line_t = px.line(df_g_temp, x='Periodo', y=metric_target, title=f"Evolución Mensual Promedio de {metric_target}", markers=True)
                    else:
                        fig_line_t = px.line(df_t, x=date_target, y=metric_target, title=f"Evolución Histórica Detallada de {metric_target}")
                    
                    st.plotly_chart(fig_line_t, use_container_width=True)
                else:
                    st.error("No se hallaron registros temporales válidos que puedan ser procesados secuencialmente.")
            else:
                st.info("Se requiere una columna formateada como fecha o año en conjunto con variables numéricas para trazar la pestaña temporal.")

        # --- TAB 6: INSIGHTS ---
        with tab6:
            st.subheader("Resumen de Hallazgos Clave e Inteligencia de Negocio")
            st.write("Interpretación algorítmica y patrones de datos extraídos directamente del comportamiento de las variables activas:")
            
            if num_cols:
                st.markdown("### Patrones en Variables Métricas")
                for col in num_cols[:2]:
                    col_mean = df[col].mean()
                    col_std = df[col].std()
                    col_min = df[col].min()
                    col_max = df[col].max()
                    
                    coef_variacion = (col_std / col_mean) if col_mean != 0 else 0
                    grado_dispersion = "Alta volatilidad/dispersión" if coef_variacion > 0.3 else "Estabilidad comercial razonable"
                    
                    st.info(f"**Variable '{col}':** Presenta un promedio de `{col_mean:.2f}` con un rango de oscilación que va desde `{col_min:.2f}` hasta `{col_max:.2f}`. El coeficiente de variación indica un estado de: **{grado_dispersion}**.")
            
            if len(num_cols) >= 2:
                st.markdown("### Correlaciones e Interdependencia")
                try:
                    c_matrix = df[num_cols].corr().abs()
                    c_matrix_np = c_matrix.to_numpy()
                    np.fill_diagonal(c_matrix_np, 0)
                    
                    c_matrix_clean = pd.DataFrame(c_matrix_np, index=c_matrix.index, columns=c_matrix.columns)
                    
                    if not c_matrix_clean.empty and c_matrix_clean.max().max() > 0:
                        max_corr_val = c_matrix_clean.max().max()
                        v1 = c_matrix_clean.max().idxmax()
                        v2 = c_matrix_clean[v1].idxmax()
                        st.success(f"**Patrón de Asociación Detectado:** Las variables **{v1}** y **{v2}** muestran la mayor fuerza de asociación lineal en el dataset actual con una correlación de `{max_corr_val:.2f}`. Cualquier cambio operativo o comercial en una de ellas repercutirá directamente en el comportamiento de la otra.")
                except Exception as e:
                    st.info("No se pudo automatizar el cálculo asociativo. Puedes revisar el mapa completo en la Tab 4.")
            
            st.markdown("### Conclusión Estratégica para la Toma de Decisiones")
            st.markdown(f"""
            * **Optimización de Calidad:** La base de datos cuenta actualmente con un volumen de `{df.shape[0]}` filas válidas. Haber mitigado nulos o duplicados asegura certidumbre metodológica.
            * **Enfoque en Procesos:** Se sugiere usar las segmentaciones cruzadas provistas en la **Tab 3** y **Tab 4** para identificar los nichos, categorías o clústeres operativos que concentran las anomalías estadísticas más críticas, reduciendo así la incertidumbre en las proyecciones de gestión.
            """)
            
    else:
        st.error("No hay datos cargados en el buffer. Regrese al Módulo '📂 2. Carga y Perfil' para inicializar el motor gráfico.")
