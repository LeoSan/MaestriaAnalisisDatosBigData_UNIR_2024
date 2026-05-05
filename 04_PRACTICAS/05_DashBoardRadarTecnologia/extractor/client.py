import time
import requests
from typing import List, Dict, Any
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type

from core.config import config
from core.logger import get_logger

logger = get_logger(__name__)

class StackAPIError(Exception):
    """Excepción personalizada para errores de la API de Stack Exchange."""
    pass

class StackExtractor:
    """
    Clase cliente para extraer datos de la API de Stack Exchange de manera resiliente.
    Maneja rate limits, backoff y parámetros de consulta de forma automática.
    """
    BASE_URL = "https://api.stackexchange.com/2.3/questions"

    def __init__(self):
        self.api_key = config.STACK_API_KEY
        self.site = "stackoverflow"
        
    @retry(
        wait=wait_exponential(multiplier=1, min=2, max=60), 
        stop=stop_after_attempt(5),
        retry=retry_if_exception_type((requests.RequestException, StackAPIError))
    )
    def _make_request(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ejecuta la petición HTTP con reintentos exponenciales en caso de fallas de red
        o cuotas de la API. También respeta explícitamente el parámetro de "backoff".
        """
        # Inyectar key si existe
        if self.api_key:
            params['key'] = self.api_key
            
        params['site'] = self.site
        
        logger.info(f"Solicitando API de Stack Exchange con params: {params.get('tagged')} | Desde: {params.get('fromdate')} Hasta: {params.get('todate')}")
        response = requests.get(self.BASE_URL, params=params)
        
        if response.status_code == 429:
            logger.warning("Rate limit excedido (429 HTTP). Lanzando excepción para activar backoff exponencial...")
            raise StackAPIError("HTTP 429 Too Many Requests")
            
        response.raise_for_status()
        data = response.json()
        
        # Verificar cuotas internas y campo "backoff"
        if "error_id" in data:
            raise StackAPIError(f"Error de la API: {data.get('error_message')}")
            
        # Si Stack Exchange nos pide esperar explícitamente, pausamos el thread
        if "backoff" in data:
            backoff_secs = data["backoff"]
            logger.warning(f"La API requiere backoff. Pausando ejecución por {backoff_secs} segundos...")
            time.sleep(backoff_secs)
            
        # Loggear cuota restante para monitoreo
        quota_remaining = data.get("quota_remaining", "N/A")
        logger.info(f"Petición exitosa. Cuota restante: {quota_remaining}")
        
        return data

    def test_connection(self) -> bool:
        """
        Modo Dry Run: Solicita 5 registros de un tag de prueba y valida que el payload 
        retorne todos los campos clave (score, view_count, is_answered, answer_count, creation_date).
        """
        logger.info("Iniciando prueba de conexión (Dry Run)...")
        params = {
            "order": "desc",
            "sort": "creation",
            "tagged": "python",
            "pagesize": 5
        }
        
        try:
            data = self._make_request(params)
            items = data.get("items", [])
            
            if not items:
                logger.error("No se encontraron registros en el test.")
                return False
                
            sample_item = items[0]
            expected_fields = ["score", "view_count", "is_answered", "answer_count", "creation_date"]
            
            missing_fields = [f for f in expected_fields if f not in sample_item]
            
            if missing_fields:
                logger.error(f"Faltan campos esperados en el payload: {missing_fields}")
                logger.debug(f"Payload de muestra: {sample_item}")
                return False
                
            logger.info("Test de conexión exitoso. El payload por defecto contiene todos los campos requeridos.")
            return True
            
        except Exception as e:
            logger.error(f"Test de conexión fallido debido a: {str(e)}")
            return False

    def fetch_data(self, tag: str, from_date: int, to_date: int) -> List[Dict]:
        """
        Extrae datos paginados para una tecnología en un periodo de tiempo específico.
        """
        all_items = []
        page = 1
        has_more = True
        
        while has_more:
            params = {
                "order": "desc",
                "sort": "creation",
                "tagged": tag,
                "fromdate": from_date,
                "todate": to_date,
                "pagesize": 100,
                "page": page
            }
            
            data = self._make_request(params)
            items = data.get("items", [])
            all_items.extend(items)
            
            has_more = data.get("has_more", False)
            page += 1
            
        logger.info(f"Extracción completada para {tag}. Total de items: {len(all_items)}")
        return all_items
