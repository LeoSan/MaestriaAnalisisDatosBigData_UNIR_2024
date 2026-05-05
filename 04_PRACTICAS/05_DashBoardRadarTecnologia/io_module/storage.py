import os
from pathlib import Path
from typing import List, Dict
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from core.logger import get_logger

logger = get_logger(__name__)

# Definir la estructura de carpetas
BASE_DATA_DIR = Path(__file__).parent.parent / "data"
RAW_DIR = BASE_DATA_DIR / "raw"
PROCESSED_DIR = BASE_DATA_DIR / "processed"

# Crear carpetas si no existen
RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def save_raw_to_parquet(data: List[Dict], tag: str, year_month: str) -> str:
    """
    Convierte la respuesta JSON en un DataFrame de Pandas, valida y limpia
    las columnas, y lo persiste en formato Parquet.
    """
    if not data:
        logger.warning(f"No hay datos para guardar en {tag} - {year_month}")
        return ""
        
    df = pd.DataFrame(data)
    
    # Contrato de datos: Asegurarnos de que las columnas existan
    expected_cols = {
        'creation_date': 'unix_date',
        'score': 'score',
        'view_count': 'views',
        'is_answered': 'answered',
        'answer_count': 'answers'
    }
    
    # Filtrar solo las que nos interesan
    cols_to_keep = []
    for col in expected_cols.keys():
        if col in df.columns:
            cols_to_keep.append(col)
            
    df = df[cols_to_keep]
    df.rename(columns=expected_cols, inplace=True)
    
    # Añadir columna del tag
    df['tag'] = tag
    
    # Validar tipos base
    if 'answered' in df.columns:
        df['answered'] = df['answered'].astype(bool)
        
    # Guardar a Parquet
    file_path = RAW_DIR / f"{tag}_{year_month}.parquet"
    df.to_parquet(file_path, index=False, engine='pyarrow')
    
    logger.info(f"Guardado exitoso: {file_path} con {len(df)} registros.")
    return str(file_path)
