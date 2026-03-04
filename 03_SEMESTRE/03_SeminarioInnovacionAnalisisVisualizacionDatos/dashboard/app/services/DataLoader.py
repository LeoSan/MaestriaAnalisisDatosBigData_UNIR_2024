import pandas as pd
import streamlit as st

class DataLoader:
    @staticmethod
    @st.cache_data
    def load_dataset() -> pd.DataFrame:
        """
        Carga el conjunto de datos optimizado desde el archivo CSV.
        Utiliza caché de Streamlit (@st.cache_data) para optimizar el rendimiento y 
        no recargar los datos del disco duro en cada iteración del dashboard.
        """
        file_path = "dataset/data_set_optimizado.csv"
        try:
            df = pd.read_csv(file_path)
            # Aseguramos que la columna de Año sea entera (por si se lee como flotante)
            if 'ANIO' in df.columns:
                df['ANIO'] = df['ANIO'].astype(int)
            return df
        except Exception as e:
            st.error(f"Error crítico al cargar el dataset: {e}")
            return pd.DataFrame()
