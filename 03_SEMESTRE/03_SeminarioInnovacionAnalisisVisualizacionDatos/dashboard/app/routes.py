from flask import Blueprint
from app.controllers.dashboard_controller import DashboardController

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """
    Ruta principal del Dashboard.
    Delega la lógica al DashboardController para mantener el archivo de rutas limpio.
    """
    return DashboardController.index_action()
