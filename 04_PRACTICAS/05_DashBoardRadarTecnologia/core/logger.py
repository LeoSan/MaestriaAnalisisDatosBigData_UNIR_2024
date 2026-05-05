import logging
import os
from pathlib import Path

# Asegurar que el directorio de logs exista
LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "extraction.log"

def get_logger(name: str) -> logging.Logger:
    """
    Configura y devuelve un logger centralizado.
    Escribe tanto en consola como en un archivo de log.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Si ya tiene handlers, no se los agregamos nuevamente
    if not logger.handlers:
        # Formato de los logs
        formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s'
        )

        # File Handler (Guarda en logs/extraction.log)
        file_handler = logging.FileHandler(LOG_FILE, mode='a', encoding='utf-8')
        file_handler.setFormatter(formatter)

        # Console Handler (Imprime en la terminal)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
