from flask import Blueprint, render_template, request
from .services.DataLoader import DataLoader

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
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
    
    if not df.empty:
        # 2. Preparar opciones dinámicas
        anios_disponibles = sorted(df['ANIO'].dropna().unique().tolist(), reverse=True)
        estados_disponibles = sorted(df['NOMBRE_ESTADO'].dropna().unique().tolist())
        
        # 3. Obtener Parámetros del Request (Filtros)
        # Año (Por defecto 2024 si está disponible, si no el más reciente)
        default_anio = 2024 if 2024 in anios_disponibles else (anios_disponibles[0] if anios_disponibles else None)
        anio_seleccionado = request.args.get('anio', default=default_anio, type=int)
        
        # Estado (Por defecto "Nacional")
        estado_seleccionado = request.args.get('estado', default="Nacional", type=str)
        
        # 4. Filtrado Dinámico
        df_filtrado = df.copy()
        
        if anio_seleccionado in anios_disponibles:
            df_filtrado = df_filtrado[df_filtrado['ANIO'] == anio_seleccionado]
            
        if estado_seleccionado != "Nacional" and estado_seleccionado in estados_disponibles:
            df_filtrado = df_filtrado[df_filtrado['NOMBRE_ESTADO'] == estado_seleccionado]
            
        # 5. Preparamos datos para la vista (Solo las primeras 5 filas para validación)
        total_registros = len(df_filtrado)
        df_vista = df_filtrado.head(5)
        columnas = df_vista.columns.tolist()
        df_filtrado_head = df_vista.values.tolist()

    # Renderizar la vista
    return render_template('index.html', 
                           anio_seleccionado=anio_seleccionado,
                           estado_seleccionado=estado_seleccionado,
                           anios=anios_disponibles,
                           estados=estados_disponibles,
                           columnas=columnas,
                           filas=df_filtrado_head,
                           total_registros=total_registros)
