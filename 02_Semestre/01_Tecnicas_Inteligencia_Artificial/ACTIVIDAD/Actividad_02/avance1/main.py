import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

# Configuración de estilo para gráficos
plt.style.use('default')
sns.set_palette("husl")

def main():
    # PASO 0: IMPORTACIÓN DEL DATASET
    print("\n🎯 Paso 0: ----------------- Importamos el DataSet de Esperanza de Vida:------------------ 🎯")
    
    try:
        # URL de descarga directa para LifeExpectancyData.csv
        url_descarga_directa = 'https://drive.google.com/uc?export=download&id=1EFa-JqAtrXtL1BrYP_mfxFVgAsADd_jn'
        df = pd.read_csv(url_descarga_directa, sep=',')
        print("✅ Dataset cargado exitosamente")
        print("\n📋 Depurando: DF después de pd.read_csv - Forma:", df.shape)
        print("📋 Depurando: DF después de pd.read_csv - Columnas (primeras 5):", df.columns.tolist()[:20], "...")
    except Exception as e:
        print(f"❌ Error al cargar el dataset: {e}")
        return

    # PASO 1: PREPROCESAMIENTO DE DATOS (Incluyendo imputación)
    print("\n🎯 Paso 1: ------------ Preprocesamiento de Datos (para caracterización) ------------------------ 🎯")
    # Limpiamos los nombres de las columnas
	df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('-', '_').str.replace('.', '', regex=False).str.lower()    

    # Identificamos columnas categóricas y numéricas
    # Incluimos todas las numéricas relevantes, incluyendo 'life_expectancy' para la caracterización
    numerical_cols_for_eda = [
        'life_expectancy', 'adult_mortality', 'infant_deaths', 'alcohol', 
        'percentage_expenditure', 'hepatitis_b', 'measles', 'bmi', 
        'under_five_deaths', 'polio', 'total_expenditure', 'diphtheria', 
        'hiv/aids', 'gdp', 'population', 'thinness__1_19_years', 
        'thinness_5_9_years', 'income_composition_of_resources', 'schooling', 'year'
    ]
    categorical_cols_for_eda = ['country', 'status']

    # Imputamos los valores faltantes para poder realizar la caracterización
    imputer_numerical = SimpleImputer(strategy='mean')
    imputer_categorical = SimpleImputer(strategy='most_frequent')

    for col in numerical_cols_for_eda:
        if col in df.columns and df[col].isnull().any():
            print(f"Imputando valores nulos en columna numérica para EDA: {col}")
            df[col] = imputer_numerical.fit_transform(df[[col]])

    for col in categorical_cols_for_eda:
        if col in df.columns and df[col].isnull().any():
            print(f"Imputando valores nulos en columna categórica para EDA: {col}")
            df[col] = imputer_categorical.fit_transform(df[[col]])

    print("\n📋 Depurando: Primeras 5 filas del dataset después de limpieza de columnas:")
    print(df.head())

    print("\n📋 Depurando: INFORMACIÓN DETALLADA DESPUÉS DE LIMPIEZA DE COLUMNAS:")
    print(df.info())    

    print("\n📋 Depurando: Nombres de columnas después de la limpieza:")
    print(df.columns.tolist())
    print("\n📋 Depurando: Forma del DataFrame después de la limpieza:", df.shape)

    # --- INICIO: APARTADO A - CARACTERIZACIÓN DEL DATASET ---
    print("\n🎯 Paso 2: ------------ Gráficas ------------------------ 🎯")
    print("\n🎯 Apartado A: ------------ Caracterización del Dataset ------------------------ 🎯")

    # 1. Iniciamos Caracterización en Modo Texto
    print("\n--- 1.1: Estadísticas Descriptivas de Variables Numéricas ---")
    print(df[numerical_cols_for_eda].describe().round(2))

    print("\n--- 1.2: Estadísticas Descriptivas de Variables Categóricas ---")
    print(df[categorical_cols_for_eda].describe())

    print("\n--- 1.3: Conteo de Valores Únicos para 'Status' ---")
    print(df['status'].value_counts())
    print(f"\nNúmero total de países únicos: {df['country'].nunique()}")

    print("\n--- 1.4: Matriz de Correlación (primeras 5x5 columnas) ---")
    # Se muestra el valor de las correlaciones con la variable objetivo o un subconjunto relevante
    correlation_matrix = df[numerical_cols_for_eda].corr()
    print(correlation_matrix.head(5).iloc[:, :5].round(2)) # Muestra solo un subconjunto para no saturar la memoria

    # Se muestra la correlación de todas las features con 'life_expectancy'
    print("\n--- 1.5: Correlación de Features Numéricas con 'life_expectancy' ---")
    print(correlation_matrix['life_expectancy'].sort_values(ascending=False).round(2))

    # 2. Inicia Caracterización Gráfica
    print("\n--- 2.1: Histogramas para variables clave ---")
    plt.figure(figsize=(15, 10))
    
    plt.subplot(2, 2, 1)
    sns.histplot(df['life_expectancy'], kde=True)
    plt.title('Distribución de la Esperanza de Vida')
    plt.xlabel('Esperanza de Vida')
    plt.ylabel('Frecuencia')

    plt.subplot(2, 2, 2)
    sns.histplot(df['gdp'], kde=True)
    plt.title('Distribución del PIB')
    plt.xlabel('PIB')
    plt.ylabel('Frecuencia')

    plt.subplot(2, 2, 3)
    sns.histplot(df['schooling'], kde=True)
    plt.title('Distribución de Años de Escolaridad')
    plt.xlabel('Años de Escolaridad')
    plt.ylabel('Frecuencia')

    plt.subplot(2, 2, 4)
    sns.histplot(df['adult_mortality'], kde=True)
    plt.title('Distribución de Mortalidad Adulta')
    plt.xlabel('Mortalidad Adulta')
    plt.ylabel('Frecuencia')
    
    plt.tight_layout()
    plt.show()

    print("\n--- 2.2: Diagramas de Dispersión (Scatter Plots) con Esperanza de Vida ---")
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    sns.scatterplot(x='gdp', y='life_expectancy', data=df, alpha=0.6)
    plt.title('Esperanza de Vida vs. PIB')
    plt.xlabel('PIB')
    plt.ylabel('Esperanza de Vida')

    plt.subplot(2, 2, 2)
    sns.scatterplot(x='schooling', y='life_expectancy', data=df, alpha=0.6)
    plt.title('Esperanza de Vida vs. Escolaridad')
    plt.xlabel('Años de Escolaridad')
    plt.ylabel('Esperanza de Vida')

    plt.subplot(2, 2, 3)
    sns.scatterplot(x='adult_mortality', y='life_expectancy', data=df, alpha=0.6)
    plt.title('Esperanza de Vida vs. Mortalidad Adulta')
    plt.xlabel('Mortalidad Adulta')
    plt.ylabel('Esperanza de Vida')

    plt.subplot(2, 2, 4)
    sns.scatterplot(x='hiv/aids', y='life_expectancy', data=df, alpha=0.6)
    plt.title('Esperanza de Vida vs. HIV/AIDS')
    plt.xlabel('Prevalencia HIV/AIDS')
    plt.ylabel('Esperanza de Vida')

    plt.tight_layout()
    plt.show()

    print("\n--- 2.3: Diagrama de Cajas y Bigotes para Esperanza de Vida por Status ---")
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='status', y='life_expectancy', data=df)
    plt.title('Esperanza de Vida por Estado de Desarrollo del País')
    plt.xlabel('Estado del País')
    plt.ylabel('Esperanza de Vida')
    plt.show()

    print("\n--- 2.4: Mapa de Calor de Correlación ---")
    plt.figure(figsize=(12, 10))
    # Selecciona un subconjunto de columnas si el heatmap es demasiado grande
    cols_for_heatmap = ['life_expectancy', 'adult_mortality', 'infant_deaths', 'gdp', 'schooling', 
                        'hiv/aids', 'income_composition_of_resources', 'bmi', 'alcohol']
    sns.heatmap(df[cols_for_heatmap].corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Mapa de Calor de Correlación de Características Seleccionadas')
    plt.show()

    print("\n🎯 Paso 3: ------------ Aplicacando Técnica de Preprocesamiento de Datos Usaremos 'Codificación One-Hot ------------------------ 🎯")

    # Identificamos las columnas categóricas y numéricas para nuestro estudio 
    categorical_features = ['country', 'status']
    numerical_features = ['adult_mortality', 'infant_deaths', 'schooling', 'gdp', 'hiv/aids', 'income_composition_of_resources', 'year'] 
    
    # Validamos que las columnas existen en el DataFrame
    print("\n📋 Depurando: Verificando existencia de columnas para preprocesamiento:")
    for col_list_name, col_list in [("Categorical Features", categorical_features), ("Numerical Features", numerical_features)]:
        missing_cols = [col for col in col_list if col not in df.columns]
        if missing_cols:
            print(f"❌ Faltan columnas en {col_list_name}: {missing_cols}")
            print(f"📋 Columnas disponibles: {df.columns.tolist()}")
            return  # Salir si faltan columnas críticas
        else:
            print(f"✅ Todas las columnas en {col_list_name} existen en el DataFrame.")

    for col in numerical_features:
        if col in df.columns and df[col].isnull().any():
            print(f"Imputando valores nulos en columna numérica: {col}")
            df[col] = imputer_numerical.fit_transform(df[[col]]).flatten()

    for col in categorical_features:
        if col in df.columns and df[col].isnull().any():
            print(f"Imputando valores nulos en columna categórica: {col}")
            df[col] = imputer_categorical.fit_transform(df[[col]]).flatten()
    
    # Definir la variable objetivo
    target_column = 'life_expectancy' 
    
    # Aplicamos transformación OneHotEncoder    
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features),
            ('num', 'passthrough', numerical_features)
        ],
        remainder='drop',
        sparse_threshold=0  # Esto fuerza la salida a ser un array denso
    )

    print("\n📋 Depurando: Antes de aplicar ColumnTransformer:")
    print("Columnas que se pasarán al OneHotEncoder:", categorical_features)
    print("Columnas que se pasarán como numéricas (passthrough):", numerical_features)
    print("Forma del DataFrame df antes de ColumnTransformer.fit_transform:", df.shape)
    
    # Verificar que las columnas categóricas tienen datos
    for col in categorical_features:
        print(f"📋 Depurando: Valores únicos en {col}: {df[col].nunique()}")
        print(f"📋 Depurando: Primeros 3 valores únicos en {col}: {df[col].unique()[:3]}")

    # Aplicar las transformaciones al DataFrame
    df_processed_array = preprocessor.fit_transform(df)

    print("\n📋 Depurando: Después de aplicar ColumnTransformer:")
    print("Forma de df_processed_array:", df_processed_array.shape)
    print("Tipo de df_processed_array:", type(df_processed_array))

    #Verificamos si es un array sparse y convertirlo
    if hasattr(df_processed_array, 'toarray'):
        df_processed_array = df_processed_array.toarray()
        print("📋 Depurando: Convertido de sparse a array denso")
        print("📋 Depurando: Nueva forma después de toarray():", df_processed_array.shape)

    # Obtener los nombres de las nuevas columnas
    try:
        one_hot_features_names = preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_features)
        all_feature_names = list(one_hot_features_names) + numerical_features
        
        print("📋 Depurando: Número de columnas One-Hot generadas:", len(one_hot_features_names))
        print("📋 Depurando: Número total de columnas esperadas:", len(all_feature_names))
        print("📋 Depurando: Forma final del array procesado:", df_processed_array.shape)
        
        # Verificamos coherencia de dimensiones
        if df_processed_array.shape[1] != len(all_feature_names):
            print(f"❌ ERROR: Dimensiones no coinciden!")
            print(f"   Array tiene {df_processed_array.shape[1]} columnas")
            print(f"   Nombres de columnas: {len(all_feature_names)}")
            return
        
        # Creamos el DataFrame final
        df_encoded = pd.DataFrame(df_processed_array, columns=all_feature_names)
        
        print("\n✅ DataFrame codificado creado exitosamente!")
        print("📋 Primeras 5 filas del dataset codificado con One-Hot Encoding:")
        print(df_encoded.head())
        print(f"\n📋 Dimensiones del nuevo DataFrame codificado: {df_encoded.shape}")
        
    except Exception as e:
        print(f"❌ Error al crear los nombres de columnas o el DataFrame: {e}")
        print("📋 Depurando: Intentando diagnóstico adicional...")
        print("📋 Transformadores disponibles:", list(preprocessor.named_transformers_.keys()))
        return

    #Anexamos la variable objetivo en el DataFrame final
    if target_column in df.columns:
        df_final = pd.concat([df_encoded, df[target_column].reset_index(drop=True)], axis=1)
        print("\n📋 DataFrame final con variable objetivo creado:")
        print(f"   Dimensiones: {df_final.shape}")
    else:
        print(f"\nAdvertencia: La columna objetivo '{target_column}' no se encontró en el DataFrame original.")
        df_final = df_encoded

if __name__ == "__main__":
    main()
