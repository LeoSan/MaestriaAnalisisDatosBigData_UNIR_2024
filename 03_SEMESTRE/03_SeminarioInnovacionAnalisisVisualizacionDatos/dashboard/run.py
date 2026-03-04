import streamlit as st
from app.services.DataLoader import DataLoader

# ==========================================
# 1. CONFIGURACIÓN DE LA ESTRUCTURA GLOBAL
# ==========================================
st.set_page_config(
    page_title="Monitor de Vulnerabilidad Educativa y Abandono Escolar",
    layout="wide",
    page_icon="🎓"
)

# Título Principal
st.title("Monitor de Vulnerabilidad Educativa y Abandono Escolar (2021-2024)")

# ==========================================
# 2. CARGA DE DATOS (Arquitectura MVC: Servicio)
# ==========================================
df = DataLoader.load_dataset()

if not df.empty:
    # ==========================================
    # 3. BARRA LATERAL DE FILTROS (Sidebar)
    # ==========================================
    st.sidebar.header("Filtros Dinámicos")
    
    # Preparar opciones dinámicas basadas en los datos
    anios_disponibles = sorted(df['ANIO'].dropna().unique().tolist(), reverse=True)
    estados_disponibles = sorted(df['NOMBRE_ESTADO'].dropna().unique().tolist())
    
    # Determinar el índice por defecto para 2024 si existe
    indice_2024 = anios_disponibles.index(2024) if 2024 in anios_disponibles else 0
    
    # --- FILTRO 1: Año ---
    anio_seleccionado = st.sidebar.selectbox(
        "📅 Selecciona el Año:",
        options=anios_disponibles,
        index=indice_2024
    )
    
    # --- FILTRO 2: Estado ---
    # Agregamos "Nacional" a la cima de las opciones
    opciones_estado = ["Nacional"] + estados_disponibles
    
    estado_seleccionado = st.sidebar.selectbox(
        "📍 Selecciona el Estado:",
        options=opciones_estado,
        index=0  # "Nacional" será la opción predeterminada
    )
    
    # ==========================================
    # 4. FILTRADO DINÁMICO (Lógica Controller)
    # ==========================================
    # Realizamos una copia en base al filtro para no afectar el dataframe original en caché
    df_filtrado = df.copy()
    
    # Filtrar por año obligatorio
    df_filtrado = df_filtrado[df_filtrado['ANIO'] == anio_seleccionado]
    
    # Filtrar por estado si es distinto a "Nacional" (ya que Nacional incluye a todos)
    if estado_seleccionado != "Nacional":
        df_filtrado = df_filtrado[df_filtrado['NOMBRE_ESTADO'] == estado_seleccionado]
        
    # ==========================================
    # 5. VALIDACIÓN VISUAL (Vista Primaria)
    # ==========================================
    st.markdown("---")
    st.subheader(f"📊 Datos filtrados ({estado_seleccionado} - {anio_seleccionado})")
    
    # Mostramos métricas rápidas opcionales para contexto
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Registros Encontrados", df_filtrado.shape[0])
        
    # Mostramos las primeras 5 filas (Validador requerido)
    st.dataframe(df_filtrado.head(5), use_container_width=True)

else:
    # En caso de error de lectura de CSV
    st.warning("⚠️ No se pudieron cargar los datos. Verifica que el archivo data_set_optimizado.csv se encuentre en la carpeta /dataset/.")
