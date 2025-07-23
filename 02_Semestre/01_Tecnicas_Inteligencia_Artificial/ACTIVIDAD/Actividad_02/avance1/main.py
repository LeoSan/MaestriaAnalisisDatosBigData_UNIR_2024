import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

# Configuración de estilo para gráficos
plt.style.use('default')
sns.set_palette("husl")

def main():
    # PASO 0: IMPORTACIÓN DEL DATASET
    print("\n🎯 Paso 0: ----------------- Importamos el DataSet Vehículos :------------------ 🎯")
    
    try:
        url_descarga_directa = '../data/Public_School_Characteristics_2018-19.csv'
        df = pd.read_csv(url_descarga_directa, sep=';')
        print("✅ Dataset cargado exitosamente")
    except Exception as e:
        print(f"❌ Error al cargar el dataset: {e}")
        return
    
    # Caracterización inicial del dataset
    print("\n📋 Primeras 5 filas del dataset:")
    print(df.head())



if __name__ == "__main__":
    main()
    