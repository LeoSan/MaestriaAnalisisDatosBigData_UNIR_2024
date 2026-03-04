import pandas as pd
from functools import lru_cache

class DataLoader:
    @staticmethod
    @lru_cache(maxsize=1)
    def load_dataset() -> pd.DataFrame:
        """
        Carga el conjunto de datos optimizado desde el archivo CSV.
        Utiliza lru_cache nativo de Python para optimizar el rendimiento y 
        no recargar los datos del disco duro en cada iteración del dashboard.
        """
        file_path = "dataset/data_set_optimizado.csv"
        try:
            df = pd.read_csv(file_path)
            # Aseguramos que la columna de Año sea entera
            if 'ANIO' in df.columns:
                df['ANIO'] = df['ANIO'].astype(int)
            return df
        except Exception as e:
            print(f"Error crítico al cargar el dataset: {e}")
            return pd.DataFrame()
