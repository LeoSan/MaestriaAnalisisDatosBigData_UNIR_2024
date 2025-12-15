from flask import Blueprint, render_template
from app.services.data_loader import DataLoader
from app.services.chart_factory import ChartFactory # <-- Importamos la fábrica

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def dashboard():
    # 1. Cargar Datos
    loader = DataLoader()
    df = loader.load_data()
    
    charts = {}

    if not df.empty:
        # Estadísticas básicas para mostrar en el dashboard
        stats = {
            "total_records": len(df),
            "countries_count": df['Country Name'].nunique(),
            "year_min": df['Year'].min(),
            "year_max": df['Year'].max(),
            "sample_data": df.head(5).to_dict(orient='records') # Primeros 5 para tabla
        }
        status_msg = "Datos cargados y limpiados exitosamente ✅"
    else:
        stats = None
        status_msg = "⚠️ Error: No se pudieron cargar los datos (Revisa la ruta del CSV)"    
    
    if not df.empty:
        # Generamos los JSON de las gráficas
        factory = ChartFactory()
        charts['evolution_correct'] = factory.create_evolution_chart_correct(df)
        charts['evolution_manipulated'] = factory.create_evolution_chart_manipulated(df)
        
        status_msg = "Visualizaciones generadas correctamente 📊"
    else:
        status_msg = "⚠️ Error: No hay datos para graficar."

    print("status_msg", status_msg)
    print("charts", charts['evolution_correct'] )
    # Renderizamos la vista pasando los gráficos
    return render_template('dashboard.html', 
                           data={"title": "Análisis Parte 1: Evolución", "status": status_msg}, 
                           charts=charts, stats=stats)