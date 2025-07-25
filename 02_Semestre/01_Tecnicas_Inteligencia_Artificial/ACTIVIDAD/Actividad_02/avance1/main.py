import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder, StandardScaler # Importamos StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split # Importamos train_test_split
from sklearn.ensemble import RandomForestRegressor # Importamos RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score # Métricas de evaluación

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
        url_descarga_directa = 'https://drive.google.com/uc?export=download&id=1EFa-JqAtrXtL1BrYP_mfxFVgAsADd_jn'
        df = pd.read_csv(url_descarga_directa, sep=',')
        print("✅ Dataset cargado exitosamente")
        print("\n📋 Depurando: DF después de pd.read_csv - Forma:", df.shape)
        print("📋 Depurando: DF después de pd.read_csv - Columnas (primeras 5):", df.columns.tolist()[:20], "...")
    except Exception as e:
        print(f"❌ Error al cargar el dataset: {e}")
        return

    # PASO 1: PREPROCESAMIENTO DE DATOS (PARA EDA Y MODELADO)
    print("\n🎯 Paso 1: ------------ Preprocesamiento Inicial de Datos ------------------------ 🎯")
    # Limpiamos los nombres de las columnas
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('-', '_').str.replace('.', '', regex=False).str.lower()    

    # Identificamos columnas categóricas y numéricas (para imputación y caracterización)
    numerical_cols_for_eda = [
        'life_expectancy', 'adult_mortality', 'infant_deaths', 'alcohol', 
        'percentage_expenditure', 'hepatitis_b', 'measles', 'bmi', 
        'under_five_deaths', 'polio', 'total_expenditure', 'diphtheria', 
        'hiv/aids', 'gdp', 'population', 'thinness__1_19_years', 
        'thinness_5_9_years', 'income_composition_of_resources', 'schooling', 'year'
    ]
    categorical_cols_for_eda = ['country', 'status']

    # Imputamos los valores faltantes
    imputer_numerical = SimpleImputer(strategy='mean')
    imputer_categorical = SimpleImputer(strategy='most_frequent')

    for col in numerical_cols_for_eda:
        if col in df.columns and df[col].isnull().any():
            print(f"Imputando valores nulos en columna numérica para EDA y Modelado: {col}")
            # .reshape(-1, 1) es redundante con df[[col]], .flatten() es para array 1D
            # La forma (n_samples, 1) es lo que espera fit_transform, df[[col]] ya lo da.
            df[col] = imputer_numerical.fit_transform(df[[col]]) # Dejarlo así está bien

    for col in categorical_cols_for_eda:
        if col in df.columns and df[col].isnull().any():
            print(f"Imputando valores nulos en columna categórica para EDA y Modelado: {col}")
            df[col] = imputer_categorical.fit_transform(df[[col]]) # Dejarlo así está bien

    print("\n✅ Imputación de valores nulos completada.")

    print("\n📋 Depurando: Primeras 5 filas del dataset después de limpieza y imputación:")
    print(df.head())
    print("\n📋 Depurando: INFORMACIÓN DETALLADA DESPUÉS DE LIMPIEZA Y IMPUTACIÓN:")
    print(df.info())    
    print("\n📋 Depurando: Nombres de columnas después de la limpieza y imputación:")
    print(df.columns.tolist())
    print("\n📋 Depurando: Forma del DataFrame después de la limpieza y imputación:", df.shape)

    # --- INICIO: APARTADO A - CARACTERIZACIÓN DEL DATASET (tal como lo tienes) ---
    print("\n🎯 Paso 2: ------------ Caracterización del Dataset ------------------------ 🎯")

    # 1. Caracterización en Modo Texto
    print("\n--- 1.1: Estadísticas Descriptivas de Variables Numéricas ---")
    print(df[numerical_cols_for_eda].describe().round(2))

    print("\n--- 1.2: Estadísticas Descriptivas de Variables Categóricas ---")
    print(df[categorical_cols_for_eda].describe())

    print("\n--- 1.3: Conteo de Valores Únicos para 'Status' ---")
    print(df['status'].value_counts())
    print(f"\nNúmero total de países únicos: {df['country'].nunique()}")

    print("\n--- 1.4: Matriz de Correlación (con life_expectancy) ---")
    correlation_matrix = df[numerical_cols_for_eda].corr()
    print("\n--- 1.5: Correlación de Features Numéricas con 'life_expectancy' ---")
    print(correlation_matrix['life_expectancy'].sort_values(ascending=False).round(2))

    # 2. Caracterización Gráfica (Código de gráficas omitido aquí por brevedad, pero mantenlo en tu archivo)
    # ... Tus llamadas a plt.show() para los histogramas, scatter plots, box plots y heatmap.
    print("\n--- 2.1: Histogramas para variables clave (se mostrarán ventanas de gráficos) ---")
    # ... (Tu código de histogramas aquí)
    plt.figure(figsize=(15, 10)) # Asegúrate de tener este bloque de código en tu main()
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

    print("\n--- 2.2: Diagramas de Dispersión (Scatter Plots) con Esperanza de Vida (se mostrarán ventanas de gráficos) ---")
    # ... (Tu código de scatter plots aquí)
    plt.figure(figsize=(15, 10)) # Asegúrate de tener este bloque de código en tu main()
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

    print("\n--- 2.3: Diagrama de Cajas y Bigotes para Esperanza de Vida por Status (se mostrarán ventanas de gráficos) ---")
    # ... (Tu código de box plot aquí)
    plt.figure(figsize=(8, 6)) # Asegúrate de tener este bloque de código en tu main()
    sns.boxplot(x='status', y='life_expectancy', data=df)
    plt.title('Esperanza de Vida por Estado de Desarrollo del País')
    plt.xlabel('Estado del País')
    plt.ylabel('Esperanza de Vida')
    plt.show()

    print("\n--- 2.4: Mapa de Calor de Correlación (se mostrará ventana de gráfico) ---")
    # ... (Tu código de heatmap aquí)
    plt.figure(figsize=(12, 10)) # Asegúrate de tener este bloque de código en tu main()
    cols_for_heatmap = ['life_expectancy', 'adult_mortality', 'infant_deaths', 'gdp', 'schooling', 
                        'hiv/aids', 'income_composition_of_resources', 'bmi', 'alcohol']
    sns.heatmap(df[cols_for_heatmap].corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Mapa de Calor de Correlación de Características Seleccionadas')
    plt.show()

    print("\n🎯 Fin de la Caracterización del Dataset 🎯")
    # --- FIN: APARTADO A - CARACTERIZACIÓN DEL DATASET ---

    # --- INICIO: PASO 3 - PREPARACIÓN DE DATOS PARA MODELADO Y MODELO DE REGRESIÓN NO NEURONAL ---
    print("\n🎯 Paso 3: ------------ Preparación de Datos y Modelo de Regresión No Neuronal ------------------------ 🎯")

    # 3.1 Separar Características (X) y Variable Objetivo (y)
    target_column = 'life_expectancy'
    X = df.drop(columns=[target_column])
    y = df[target_column]
    print(f"\n✅ Datos separados: X.shape={X.shape}, y.shape={y.shape}")

    # 3.2 Dividir los Datos en Conjuntos de Entrenamiento y Prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"✅ Datos divididos en entrenamiento y prueba (test_size=0.2, random_state=42):")
    print(f"   X_train.shape={X_train.shape}, y_train.shape={y_train.shape}")
    print(f"   X_test.shape={X_test.shape}, y_test.shape={y_test.shape}")

    # 3.3 Ajustar el ColumnTransformer para el modelado (puede incluir escalado)
    # Las columnas categóricas y numéricas son las que irán en X
    categorical_features_model = ['country', 'status']
    # Excluimos la variable objetivo de las features numéricas para el modelo
    numerical_features_model = [col for col in X.columns if col not in categorical_features_model]
    
    # Random Forest no NECESITA escalado, pero a veces ayuda.
    # Si quisieras escalado, el preprocessor sería así:
    # transformers=[
    #    ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features_model),
    #    ('num', StandardScaler(), numerical_features_model) # Aquí se usa StandardScaler
    # ]
    
    preprocessor_model = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features_model),
            ('num', 'passthrough', numerical_features_model) # Usamos 'passthrough' si no queremos escalar
        ],
        remainder='drop',
        sparse_threshold=0 # Asegura salida densa
    )

    print("\n📋 Depurando: ColumnTransformer para modelado configurado.")
    print(f"   Columnas categóricas para modelado: {categorical_features_model}")
    print(f"   Columnas numéricas para modelado: {numerical_features_model}")

    # Aplicar transformaciones SOLO a los conjuntos de entrenamiento y prueba
    X_train_processed = preprocessor_model.fit_transform(X_train)
    X_test_processed = preprocessor_model.transform(X_test) # Usar transform, no fit_transform, en el set de prueba

    # Obtener nombres de columnas finales para el DataFrame transformado
    # Importante: obtener los nombres DESPUÉS de fit en X_train
    one_hot_feature_names_model = preprocessor_model.named_transformers_['cat'].get_feature_names_out(categorical_features_model)
    all_feature_names_model = list(one_hot_feature_names_model) + numerical_features_model

    # Convertir a DataFrame para mejor manejo y visualización (opcional, el modelo de sklearn puede usar arrays)
    X_train_final = pd.DataFrame(X_train_processed, columns=all_feature_names_model, index=X_train.index)
    X_test_final = pd.DataFrame(X_test_processed, columns=all_feature_names_model, index=X_test.index)

    print(f"\n✅ Datos de entrenamiento y prueba preprocesados:")
    print(f"   X_train_final.shape={X_train_final.shape}")
    print(f"   X_test_final.shape={X_test_final.shape}")
    print("📋 Primeras 5 filas de X_train_final:")
    print(X_train_final.head())


    # 3.4 Entrenar el Modelo Random Forest Regressor
    print("\n--- 3.4: Entrenando el Modelo Random Forest Regressor ---")
    # Parámetros básicos para empezar. Puedes ajustarlos (hiperparámetros)
    # n_estimators: número de árboles en el bosque
    # random_state: para reproducibilidad
    # n_jobs: -1 usa todos los núcleos de la CPU
    
    # Definimos el modelo
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    
    # Entrenamos el modelo con los datos de entrenamiento preprocesados
    rf_model.fit(X_train_final, y_train)
    print("✅ Modelo Random Forest entrenado exitosamente.")


    # 3.5 Probar el Modelo y Evaluar
    print("\n--- 3.5: Evaluando el Modelo Random Forest ---")
    y_pred_train = rf_model.predict(X_train_final) # Predicciones en entrenamiento
    y_pred_test = rf_model.predict(X_test_final)   # Predicciones en prueba

    # Métricas de evaluación
    mae_train = mean_absolute_error(y_train, y_pred_train)
    mse_train = mean_squared_error(y_train, y_pred_train)
    rmse_train = np.sqrt(mse_train)
    r2_train = r2_score(y_train, y_pred_train)

    mae_test = mean_absolute_error(y_test, y_pred_test)
    mse_test = mean_squared_error(y_test, y_pred_test)
    rmse_test = np.sqrt(mse_test)
    r2_test = r2_score(y_test, y_pred_test)

    print("\n--- Métricas en el Conjunto de Entrenamiento ---")
    print(f"MAE (Error Absoluto Medio): {mae_train:.2f}")
    print(f"MSE (Error Cuadrático Medio): {mse_train:.2f}")
    print(f"RMSE (Raíz del Error Cuadrático Medio): {rmse_train:.2f}")
    print(f"R2 Score: {r2_train:.2f}")

    print("\n--- Métricas en el Conjunto de Prueba (¡Importante para evaluar el rendimiento general!) ---")
    print(f"MAE (Error Absoluto Medio): {mae_test:.2f}")
    print(f"MSE (Error Cuadrático Medio): {mse_test:.2f}")
    print(f"RMSE (Raíz del Error Cuadrático Medio): {rmse_test:.2f}")
    print(f"R2 Score: {r2_test:.2f}")

    print("\n🎯 Fin del Modelo de Regresión No Neuronal 🎯")
    # --- FIN: PASO 3 ---

    # El resto de tu código si tuvieras más pasos
    
if __name__ == "__main__":
    main()
