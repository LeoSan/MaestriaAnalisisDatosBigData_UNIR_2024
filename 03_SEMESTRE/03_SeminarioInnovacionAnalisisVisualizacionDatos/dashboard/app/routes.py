from flask import Blueprint, render_template
from app.controllers.dashboard_controller import DashboardController

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """
    Ruta principal del Dashboard.
    Delega la lógica al DashboardController para mantener el archivo de rutas limpio.
    """
    return DashboardController.index_action()

@bp.route('/nosotros')
def nosotros():
    """
    Ruta para la página de Nosotros.
    """
    return render_template('nosotros.html')
