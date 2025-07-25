# Pasos para la actividad Avance Version 1 

## Configuracion 
- Creamos nuestro entorno  con el siguiente comandi ´python3 -m venv <nombre>´
- luego activamos ´source ./nombreEntorno/bin/activate´
- Instalamos librerias 
    - pip install pandas
    - pip install seabron
    - pip install scikit-learn
    - pip install tensorflow 


## Iniciamos avance 
    - Buscamos un dataset para aplicar los conocimientos 
    - creamos un archivo llamado main.py que contendra el script 
    - activamos entorno asi -> ´source ./avance2/bin/activate´
    - Ejecutamos así ´python3 main.py´ estando en el directorio -> ~/Documents/Dev/python/maestria

# Parte  1 Descripción del Dataset

- Nombre del Dataset: 'LifeExpectancyData.csv'.
- Fuente: Se extrajo el dataset de la plataforma Kaggle cuyo enlace publico se consigue en el siguiente enlace público  'https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who/suggestions'

- Hipótesis: Se desea predecir la esperanza de vida de México usando un dataset con información de otros países para el 2030. 

- Contexto: Se tomaran las siguientes variables para validar la hipotesis y aplicar el conocimiento adquirido durante las clases las variables son: 

    - Adult Mortality (Mortalidad Adulta): Es una de las variables más directamente relacionadas con la esperanza de vida Menor mortalidad adulta debería implicar mayor esperanza de vida.

    - infant deaths (Muertes Infantiles): Similar a la mortalidad adulta, una reducción en las muertes infantiles contribuye directamente al aumento de la esperanza de vida de una población.

    - Schooling (Escolaridad): Un mayor nivel de escolaridad suele correlacionarse con una mayor conciencia sobre la salud, mejores trabajos, ingresos y acceso a atención médica, lo que se traduce en mayor esperanza de vida. 

    - GDP (Producto Interno Bruto): Representa la salud económica de un país. Un PIB más alto generalmente implica mejores infraestructuras de salud, nutrición y condiciones de vida.

    - HIV/AIDS (VIH/SIDA): La prevalencia de enfermedades crónicas y pandemias tiene un impacto directo y negativo en la esperanza de vida. Esta variable captura un aspecto importante de la salud pública.

    - Income composition of resources (Composición de los recursos de ingresos): Esta variable suele ser un índice que combina GNI per cápita, años de escolaridad y esperanza de vida. tomamos esta variables como un buen indicador compuesto del desarrollo humano y es probable que tenga una fuerte correlación con la esperanza de vida.

    - Year: Por ultima variables pero no menos importante el año esto nos ayudará en establecer la predicción para años a futuros. 

    - Country (Pais): El total de paises que se realizó el estudio previo. 

    - Status: 

- Variables Clave: (Life expectancy) consideramos esta variable numérica continua y es el objetivo de la predicción, lo que la hace la variable de salida perfecta para un problema de regresión y nos apoya para resolver la problemática de estudio.
 
- Técnicas de Preprocesamiento de Datos: Usaremos 'Codificación One-Hot'
Porque validando las variables nos encontramos con categiorias nominales y el número de categorias no es muy grande y el OneHotEncoder para las variables categóricas, que es lo más adecuado para este caso, y cómo manejar las variables numéricas sin aplicarles codificación inapropiada.Consideramos que el dataset LifeExpectancyData.csv las variables que típicamente serían categóricas y se beneficiarían del One-Hot Encoding son 'Country' y 'Status'. Las demás variables que se mencionan como ('Adult Mortality', 'infant deaths', 'Schooling', 'GDP', 'HIV/AIDS', 'Income composition of resources', 'Year', y 'Life expectancy') son numéricas y deben tratarse como tal, posiblemente con escalado si es necesario para el modelo, pero no con codificación que altere su significado numérico.

## Variables clave que vamos a caracterizar:

- Variable Objetivo (Target): life_expectancy

- Variables Numéricas (Features): adult_mortality, infant_deaths, alcohol, percentage_expenditure, hepatitis_b, measles, bmi, under_five_deaths, polio, total_expenditure, diphtheria, hiv/aids, gdp, population, thinness__1_19_years, thinness_5_9_years, income_composition_of_resources, schooling, year.

- Variables Categóricas (Features): country, status

## Definición de Graficas 
Se discución con el equipo y se usó las siguientes graficas por su amplia demostración de los datos: 

a) Histogramas para Variables Numéricas:
Muestran la distribución de una sola variable. Nos ayudó a ver si la distribución es normal, sesgada, bimodal, Para life_expectancy entre otras características numéricas importantes: GDP, Schooling, Adult Mortality, HIV/AIDS, etc.

b) Diagramas de Dispersión (Scatter Plots) para Relaciones  Numéricas:
Nos mostró la visualización y la relación entre dos variables numéricas. fue excelente ya que nos permitió identificar correlaciones, tendencias y posibles valores atípicos.

Comparación 
- life_expectancy vs. GDP: ¿Mayor PIB significa mayor esperanza de vida?
- life_expectancy vs. Schooling: ¿Más años de escolaridad se relacionan con mayor esperanza de vida?
- life_expectancy vs. Adult Mortality: ¿Mayor mortalidad adulta se relaciona con menor esperanza de vida? (esperaríamos una correlación negativa).
- life_expectancy vs. HIV/AIDS: ¿Relación con la prevalencia de VIH/SIDA?

c) Diagramas de Cajas y Bigotes (Box Plots):
Nos permitió visualizar la distribución de una variable numérica en función de una variable categórica. Muestra la mediana, los cuartiles y la presencia de valores atípicos.

Comparación 
- life_expectancy por Status (Developing/Developed): ¿Hay diferencias claras en la esperanza de vida entre países desarrollados y en desarrollo?

d) Mapa de Calor de Correlación (Heatmap):
Nos permitió ver la representación visual de la matriz de correlación, haciendo que sea muy fácil identificar relaciones fuertes (positivas o negativas) en un par de vistazos.

Consideramos estas como las mas utiles y faciles de comprender y de desarrollar, sabemos que existe una gran variedad de graficas y de extender mas la comprensión de la data, debemos nosotros como futuros analistas ampliar nuestra experiencia y adquirir mas criterios de analisis y de curiosidad para mejorar en este mundo de la big data. 

## Modelo de Regresión No Neuronal:

Para este caso usaremos el random forest regression por ser muy robusto y versátil para tareas de regresión, tomando en cuenta sus ventajas muy claras como **Alta Precisión**, Tiende a producir resultados muy precisos, especialmente en datasets complejos con relaciones no lineales. **Manejo de Multicolinealidad**  nos permite tener menos sensibilidad a la multicolinealidad entre características en comparación con la regresión lineal, **Robustez a Outliers** es bastante robusto a los valores atípicos (outliers) y al ruido en los datos, **Manejo de Datos Faltantes** lo bueno de esta ventaja es que si tenemos una gestión para datos imputados, los árboles de decisión que componen el **Random Forest** pueden manejar bien algunos tipos de datos con patrones de valores faltantes, aunque ya los estemos imputamos, es una ventaja general del método. 




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



