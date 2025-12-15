import pandas as pd
import numpy as np
import os
from flask import current_app

class DataLoader:
    """
    Servicio encargado de la extracción, limpieza y transformación (ETL)
    del dataset de Coeficiente de Gini del Banco Mundial.
    """

    def __init__(self):
        # Definimos la ruta relativa al archivo CSV
        self.file_path = os.path.join(os.getcwd(), 'data', 'API_SI.POV.GINI_DS2_es_csv_v2_113538.csv')
        
        # Universo de datos: Seleccionamos los paises europeos para nuestro estudio 
        self.target_countries = [
            'España', 'Portugal', 'Francia', 'Alemania', 'Italia', 'Reino Unido', 
            'Irlanda', 'Bélgica', 'Países Bajos', 'Luxemburgo', 'Suiza', 'Austria',
            'Suecia', 'Noruega', 'Finlandia', 'Dinamarca', 'Islandia',
            'Polonia', 'República Checa', 'Eslovaquia', 'Hungría', 'Rumania', 'Bulgaria',
            'Grecia', 'Chipre', 'Malta', 'Estonia', 'Letonia', 'Lituania', 'Croacia', 'Eslovenia'
        ]

    def load_data(self):
        """
        Orquesta el proceso de carga y devuelve un DataFrame limpio.
        Retorna: pd.DataFrame con columnas ['Country', 'Year', 'Gini']
        """
        try:
            # Cargamos el archivo CSV, saltando las 4 primeras filas de metadatos basura del BM
            df = pd.read_csv(self.file_path, skiprows=4)
            
            # Limpiamos los nombres de columnas (espacios extra)
            df.columns = df.columns.str.strip()

            # Filtramos solo países europeos
            if 'Country Name' not in df.columns:
                raise ValueError("El formato del CSV no es correcto (falta 'Country Name')")
            
            df_eu = df[df['Country Name'].isin(self.target_countries)].copy()

            # Transformamos (Unpivoting): De Columnas anuales a Filas (Formato Tidy)
            # Esto es crucial para poder graficar series temporales correctamente [cite: 20]
            year_cols = [col for col in df_eu.columns if col.isdigit()]
            
            df_long = df_eu.melt(
                id_vars=['Country Name', 'Country Code'], 
                value_vars=year_cols, 
                var_name='Year', 
                value_name='Gini'
            )

            # Validación de Tipos y Limpieza de Nulos
            df_long['Year'] = pd.to_numeric(df_long['Year'])
            df_long['Gini'] = pd.to_numeric(df_long['Gini'], errors='coerce')

            # Eliminamos nulos
            df_clean = df_long.dropna(subset=['Gini'])

            # Filtramos rango útil (2000-2022) para evitar gráficos con huecos históricos
            df_clean = df_clean[(df_clean['Year'] >= 2000)]

            # Ordenamos para presentación
            df_clean = df_clean.sort_values(by=['Country Name', 'Year'])
            
            print(f"✅ Datos cargados correctamente: {len(df_clean)} registros de Europa procesados.")
            return df_clean


        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo en {self.file_path}")
            return pd.DataFrame() # Retorna vacío para no romper la app
        except Exception as e:
            print(f"❌ Error procesando datos: {str(e)}")
            return pd.DataFrame()