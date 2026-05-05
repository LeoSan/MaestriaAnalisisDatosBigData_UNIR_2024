from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Configuración central de la aplicación.
    Lee automáticamente las variables de un archivo .env
    """
    STACK_API_KEY: str = ""
    TAGS_LIST: List[str] = ["php", "python", "typescript", "java", "c#", "go", "r"]
    LOOKBACK_MONTHS: int = 24

    # Configura pydantic para buscar en el archivo .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# Instancia global de configuración
config = Settings()
