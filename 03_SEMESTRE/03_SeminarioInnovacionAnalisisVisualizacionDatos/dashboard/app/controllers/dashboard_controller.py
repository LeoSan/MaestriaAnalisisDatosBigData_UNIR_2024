from flask import render_template, request
import json
import plotly
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from app.services.DataLoader import DataLoader

class DashboardController:
    @staticmethod
    def index_action():
        """
        Maneja la lógica principal para la vista del dashboard.
        Obtiene los datos, aplica los filtros dinámicos y prepara 
        las variables para el template.
        """
        # 1. Cargar Datos
        df = DataLoader.load_dataset()
        
        # Valores por defecto para la vista en caso de error
        anios_disponibles = []
        estados_disponibles = []
        anio_seleccionado = 2024
        estado_seleccionado = "Nacional"
        df_filtrado_head = []
        total_registros = 0
        columnas = []
        
        # --- BLOQUE CONTROLADOR (Paso 2): Variables por defecto para KPIs ---
        # Inicializamos en 0 por si ocurre un error o no hay datos
        kpi_abandono = 0.0
        kpi_salud = 0.0
        kpi_ingreso = 0.0
        kpi_vivienda = 0.0
        
        # --- BLOQUE CONTROLADOR (Paso 3): Variables JSON por defecto para los Mapas ---
        mapa_abandono_json = "{}"
        mapa_salud_json = "{}"

        # --- BLOQUE CONTROLADOR (Paso 4): Variables JSON por defecto para Evolución Temporal ---
        evolucion_temporal_json = "{}"

        # --- BLOQUE CONTROLADOR (Paso 5): Variables JSON por defecto para ML ---
        rf_bar_json = "{}"
        kmeans_scatter_json = "{}"
        
        if not df.empty:
            # 2. Preparar opciones dinámicas
            anios_disponibles = sorted(df['PERIODO_ANIO'].dropna().unique().tolist(), reverse=True)
            estados_disponibles = sorted(df['NOMBRE_ESTADO'].dropna().unique().tolist())
            
            # 3. Obtener Parámetros del Request (Filtros)
            default_anio = 2024 if 2024 in anios_disponibles else (anios_disponibles[0] if anios_disponibles else None)
            anio_seleccionado = request.args.get('anio', default=default_anio, type=int)
            estado_seleccionado = request.args.get('estado', default="Nacional", type=str)
            
            # 4. Filtrado Dinámico
            df_filtrado = df.copy()
            
            estado_mapping = {
                'AGUAS_CALIENTES': 'Aguascalientes', 'BAJA_CALIFORNIA': 'Baja California', 'BAJA_CALIFORNIA_SUR': 'Baja California Sur',
                'CAMPECHE': 'Campeche', 'CHIAPAS': 'Chiapas', 'CHIHUAHUA': 'Chihuahua', 'CIUDAD_DE_MEXICO': 'Ciudad de México',
                'COAHUILA': 'Coahuila', 'COLIMA': 'Colima', 'DURANGO': 'Durango', 'ESTADO_MEXICO': 'México', 'GUANAJUATO': 'Guanajuato',
                'GUERRERO': 'Guerrero', 'HIDALGO': 'Hidalgo', 'JALISCO': 'Jalisco', 'MICHOCAN': 'Michoacán', 'MORELOS': 'Morelos',
                'NAYARIT': 'Nayarit', 'NUEVO_LEON': 'Nuevo León', 'OAXACA': 'Oaxaca', 'PUEBLA': 'Puebla', 'QUERETARO': 'Querétaro',
                'QUINTANA_ROO': 'Quintana Roo', 'SAN_LUIS_POTOSI': 'San Luis Potosí', 'SINALOA': 'Sinaloa', 'SONORA': 'Sonora',
                'TABASCO': 'Tabasco', 'TAMAULIPAS': 'Tamaulipas', 'TLAXCALA': 'Tlaxcala', 'VERACRUZ': 'Veracruz', 'YUCATAN': 'Yucatán',
                'ZACATECAS': 'Zacatecas'
            }
            df_filtrado['ESTADO_GEOJSON'] = df_filtrado['NOMBRE_ESTADO'].map(estado_mapping)

            if anio_seleccionado in anios_disponibles:
                df_filtrado = df_filtrado[df_filtrado['PERIODO_ANIO'] == anio_seleccionado]
                
            if estado_seleccionado != "Nacional" and estado_seleccionado in estados_disponibles:
                df_filtrado = df_filtrado[df_filtrado['NOMBRE_ESTADO'] == estado_seleccionado]
                
            # 5. Preparamos datos para la vista
            total_registros = len(df_filtrado)
            
            # --- BLOQUE CONTROLADOR (Paso 2): Cálculo de KPIs ---
            # Se usa pandas .mean() para calcular el promedio de las variables clave del dataframe filtrado.
            # Se usa la función round(valor, 2) para redondear el resultado a dos decimales.
            kpi_abandono = round(df_filtrado['TASA_ABANDONO_PRIMARIA'].mean(), 2) if not df_filtrado['TASA_ABANDONO_PRIMARIA'].isna().all() else 0.0
            kpi_salud = round(df_filtrado['CARENCIA_SALUD'].mean(), 2) if not df_filtrado['CARENCIA_SALUD'].isna().all() else 0.0
            kpi_ingreso = round(df_filtrado['RAZON_INGRESO'].mean(), 2) if not df_filtrado['RAZON_INGRESO'].isna().all() else 0.0
            kpi_vivienda = round(df_filtrado['VIVIENDA_PISO_TIERRA'].mean(), 2) if not df_filtrado['VIVIENDA_PISO_TIERRA'].isna().all() else 0.0
            
            df_vista = df_filtrado
            columnas = df_vista.columns.tolist()
            df_filtrado_head = df_vista.values.tolist()

            # --- BLOQUE CONTROLADOR (Paso 3): Generación de Mapas Plotly ---
            # URL de GeoJSON público con los estados de México
            geojson_url = "https://raw.githubusercontent.com/angelnmara/geojson/master/mexicoHigh.json"
            
            # Mapa 1: Tasa de Abandono Primaria
            fig_abandono = px.choropleth(
                df_filtrado, 
                geojson=geojson_url, 
                locations='ESTADO_GEOJSON', 
                featureidkey='properties.name',
                color='TASA_ABANDONO_PRIMARIA',
                color_continuous_scale="RdYlGn_r", # Invertimos para que verde sea bajo y rojo alto riesgo
                title="Tasa de Abandono en Primaria (%)"
            )
            # Centrar y enfocar en las locaciones proporcionadas, quitar fondo
            fig_abandono.update_geos(fitbounds="locations", visible=False, bgcolor="rgba(0,0,0,0)", projection_type="mercator")
            fig_abandono.update_layout(template="plotly_dark", margin={"r":0,"t":40,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color="white"))
            mapa_abandono_json = json.dumps(fig_abandono, cls=plotly.utils.PlotlyJSONEncoder)

            # Mapa 2: Carencia de Salud
            fig_salud = px.choropleth(
                df_filtrado, 
                geojson=geojson_url, 
                locations='ESTADO_GEOJSON', 
                featureidkey='properties.name',
                color='CARENCIA_SALUD',
                color_continuous_scale="RdYlGn_r", 
                title="Carencia de Acceso a Servicios de Salud (%)"
            )
            fig_salud.update_geos(fitbounds="locations", visible=False, bgcolor="rgba(0,0,0,0)", projection_type="mercator")
            fig_salud.update_layout(template="plotly_dark", margin={"r":0,"t":40,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color="white"))
            mapa_salud_json = json.dumps(fig_salud, cls=plotly.utils.PlotlyJSONEncoder)

            # --- BLOQUE CONTROLADOR (Paso 4): Evolución Temporal (Convergencia / Divergencia) ---
            # Agrupamos el DataFrame original (no el filtrado por año) para obtener el Nacional por año
            df_nacional_tendencia = df.groupby('PERIODO_ANIO')['TASA_ABANDONO_PRIMARIA'].mean().reset_index()
            # Aseguramos que el año sea categórico/texto para el eje X
            df_nacional_tendencia['PERIODO_ANIO_STR'] = df_nacional_tendencia['PERIODO_ANIO'].astype(str)
            
            # Inicializamos la figura de Plotly para agregar trazados (líneas)
            fig_evolucion = go.Figure()
            
            # 1. Agregamos siempre la línea Promedio Nacional (Referencia)
            fig_evolucion.add_trace(go.Scatter(
                x=df_nacional_tendencia['PERIODO_ANIO_STR'],
                y=df_nacional_tendencia['TASA_ABANDONO_PRIMARIA'],
                mode='lines+markers',
                name='Promedio Nacional',
                line=dict(color='gray', width=2, dash='dash'),
                marker=dict(size=8)
            ))
            
            # 2. Si hay un estado seleccionado diferente al Nacional, agregamos su línea
            if estado_seleccionado != "Nacional":
                # Filtramos el histórico completo de ese estado en todos los años
                df_estado_tendencia = df[df['NOMBRE_ESTADO'] == estado_seleccionado].copy()
                df_estado_tendencia['PERIODO_ANIO_STR'] = df_estado_tendencia['PERIODO_ANIO'].astype(str)
                df_estado_tendencia = df_estado_tendencia.sort_values(by='PERIODO_ANIO')
                
                fig_evolucion.add_trace(go.Scatter(
                    x=df_estado_tendencia['PERIODO_ANIO_STR'],
                    y=df_estado_tendencia['TASA_ABANDONO_PRIMARIA'],
                    mode='lines+markers',
                    name=estado_seleccionado,
                    line=dict(color='#ef4444', width=4), # Rojo Tailwind destacado
                    marker=dict(size=10, symbol='diamond')
                ))

            fig_evolucion.update_layout(
                title=f"Evolución Tasa Abandono Primaria (2021-2024)",
                xaxis_title="Año",
                yaxis_title="Tasa Abandono (%)",
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                margin=dict(l=40, r=40, t=60, b=40),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            
            evolucion_temporal_json = json.dumps(fig_evolucion, cls=plotly.utils.PlotlyJSONEncoder)

            # --- BLOQUE CONTROLADOR (Paso 5): Machine Learning (Diagnóstico y Perfiles) ---
            
            # Gráfico 1: Random Forest (Importancia de Factores) - Estático pre-calculado
            rf_data = {
                'Variable': ['Carencia Salud', 'Vulnerable Carencias', 'Piso de Tierra', 'Razón Ingreso', 'Inasistencia', 'Inseg. Alimentaria'],
                'Importancia': [0.22, 0.21, 0.20, 0.13, 0.12, 0.11]
            }
            df_rf = pd.DataFrame(rf_data).sort_values(by='Importancia', ascending=True)
            
            fig_rf = px.bar(
                df_rf, 
                x='Importancia', 
                y='Variable', 
                orientation='h',
                title="Top Factores de Riesgo (Modelo Random Forest)",
                color='Importancia',
                color_continuous_scale="Reds"
            )
            fig_rf.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", margin=dict(l=0, r=0, t=40, b=0))
            rf_bar_json = json.dumps(fig_rf, cls=plotly.utils.PlotlyJSONEncoder)

            # Gráfico 2: K-Means Clustering (Dinámico sobre 2024)
            df_2024 = df[df['PERIODO_ANIO'] == 2024].copy()
            
            if not df_2024.empty:
                # Variables para clustering
                features = ['CARENCIA_SALUD', 'INSEG_ALIMENTARIA', 'TASA_ABANDONO_PRIMARIA']
                # Llenamos nulos con la media para evitar errores en KMeans
                df_cluster = df_2024[features].fillna(df_2024[features].mean())
                
                # Escalado
                scaler = StandardScaler()
                scaled_features = scaler.fit_transform(df_cluster)
                
                # KMeans
                kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
                df_2024['Perfil_Vulnerabilidad'] = kmeans.fit_predict(scaled_features)
                
                # Mapeo de nombres descriptivos para los clusters
                cluster_names = {0: 'Riesgo Moderado', 1: 'Riesgo Crítico', 2: 'Anomalía'}
                df_2024['Perfil_Nombre'] = df_2024['Perfil_Vulnerabilidad'].map(cluster_names)
                
                # Gráfico Scatter
                fig_kmeans = px.scatter(
                    df_2024,
                    x='CARENCIA_SALUD',
                    y='TASA_ABANDONO_PRIMARIA',
                    color='Perfil_Nombre',
                    hover_name='NOMBRE_ESTADO',
                    title="Agrupación de Estados por Perfil (K-Means 2024)",
                    labels={'CARENCIA_SALUD': 'Carencia Salud (%)', 'TASA_ABANDONO_PRIMARIA': 'Abandono Primaria (%)'},
                    color_discrete_sequence=['#3b82f6', '#ef4444', '#f59e0b'], # Azul, Rojo, Amarillo tailwind
                    size_max=12
                )
                fig_kmeans.update_traces(marker=dict(size=10, line=dict(width=1, color='DarkSlateGrey')))
                fig_kmeans.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", margin=dict(l=0, r=0, t=40, b=0), legend_title_text='Perfil')
                kmeans_scatter_json = json.dumps(fig_kmeans, cls=plotly.utils.PlotlyJSONEncoder)


        # Renderizar la vista
        return render_template('index.html', 
                               anio_seleccionado=anio_seleccionado,
                               estado_seleccionado=estado_seleccionado,
                               anios=anios_disponibles,
                               estados=estados_disponibles,
                               columnas=columnas,
                               filas=df_filtrado_head,
                               total_registros=total_registros,
                               # --- BLOQUE CONTROLADOR (Paso 2): Paso de contexto a vista ---
                               # Estas variables se inyectan en Jinja2 para ser renderizadas
                               kpi_abandono=kpi_abandono,
                               kpi_salud=kpi_salud,
                               kpi_ingreso=kpi_ingreso,
                               kpi_vivienda=kpi_vivienda,
                               # --- BLOQUE CONTROLADOR (Paso 3): Paso de los JSON a la vista ---
                               mapa_abandono_json=mapa_abandono_json,
                               mapa_salud_json=mapa_salud_json,
                               # --- BLOQUE CONTROLADOR (Paso 4): Paso de gráfico evolución ---
                               evolucion_temporal_json=evolucion_temporal_json,
                               # --- BLOQUE CONTROLADOR (Paso 5): JSON de Machine Learning ---
                               rf_bar_json=rf_bar_json,
                               kmeans_scatter_json=kmeans_scatter_json)
