from flask import Blueprint, render_template
from .services.DataLoader import DataLoader
from .services.ChartFactory import ChartFactory

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # Obtener los datos limpios y preparados
    data = DataLoader.get_sample_data()
    
    # Generar la gráfica interactiva basada en los datos
    chart_html = ChartFactory.create_sample_chart(data)
    
    # Renderizar la vista
    return render_template('index.html', chart=chart_html)
