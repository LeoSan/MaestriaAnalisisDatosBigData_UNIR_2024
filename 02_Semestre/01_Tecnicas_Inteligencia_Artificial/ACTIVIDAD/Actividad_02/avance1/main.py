import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

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
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('-', '_').str.replace('.', '', regex=False).str.lower()    

    numerical_cols_for_eda = [
        'life_expectancy', 'adult_mortality', 'infant_deaths', 'alcohol', 
        'percentage_expenditure', 'hepatitis_b', 'measles', 'bmi', 
        'under_five_deaths', 'polio', 'total_expenditure', 'diphtheria', 
        'hiv/aids', 'gdp', 'population', 'thinness__1_19_years', 
        'thinness_5_9_years', 'income_composition_of_resources', 'schooling', 'year'
    ]
    categorical_cols_for_eda = ['country', 'status']

    imputer_numerical = SimpleImputer(strategy='mean')
    imputer_categorical = SimpleImputer(strategy='most_frequent')

    for col in numerical_cols_for_eda:
        if col in df.columns and df[col].isnull().any():
            print(f"Imputando valores nulos en columna numérica para EDA y Modelado: {col}")
            df[col] = imputer_numerical.fit_transform(df[[col]])

    for col in categorical_cols_for_eda:
        if col in df.columns and df[col].isnull().any():
            print(f"Imputando valores nulos en columna categórica para EDA y Modelado: {col}")
            df[col] = imputer_categorical.fit_transform(df[[col]])

    print("\n✅ Imputación de valores nulos completada.")

    print("\n📋 Depurando: Primeras 5 filas del dataset después de limpieza y imputación:")
    print(df.head())
    print("\n📋 Depurando: INFORMACIÓN DETALLADA DESPUÉS DE LIMPIEZA Y IMPUTACIÓN:")
    print(df.info())    
    print("\n📋 Depurando: Nombres de columnas después de la limpieza y imputación:")
    print(df.columns.tolist())
    print("\n📋 Depurando: Forma del DataFrame después de la limpieza y imputación:", df.shape)

    # --- INICIO: APARTADO A - CARACTERIZACIÓN DEL DATASET ---
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

    # 2. Caracterización Gráfica (mantener en tu archivo)
    print("\n--- 2.1: Histogramas para variables clave (se mostrarán ventanas de gráficos) ---")
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

    print("\n--- 2.2: Diagramas de Dispersión (Scatter Plots) con Esperanza de Vida (se mostrarán ventanas de gráficos) ---")
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

    print("\n--- 2.3: Diagrama de Cajas y Bigotes para Esperanza de Vida por Status (se mostrarán ventanas de gráficos) ---")
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='status', y='life_expectancy', data=df)
    plt.title('Esperanza de Vida por Estado de Desarrollo del País')
    plt.xlabel('Estado del País')
    plt.ylabel('Esperanza de Vida')
    plt.show()

    print("\n--- 2.4: Mapa de Calor de Correlación (se mostrará ventana de gráfico) ---")
    plt.figure(figsize=(12, 10))
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

    # 3.3 Ajustar el ColumnTransformer para el modelado (incluirá escalado para NN)
    categorical_features_model = ['country', 'status']
    numerical_features_model = [col for col in X.columns if col not in categorical_features_model]
    
    # Para Redes Neuronales, ES ALTAMENTE RECOMENDABLE escalar las características numéricas.
    # Usaremos StandardScaler.
    preprocessor_model = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features_model),
            ('num', StandardScaler(), numerical_features_model) # APLICAMOS StandardScaler aquí
        ],
        remainder='drop',
        sparse_threshold=0 
    )

    print("\n📋 Depurando: ColumnTransformer para modelado configurado (con StandardScaler para numéricas).")

    X_train_processed = preprocessor_model.fit_transform(X_train)
    X_test_processed = preprocessor_model.transform(X_test) 

    one_hot_feature_names_model = preprocessor_model.named_transformers_['cat'].get_feature_names_out(categorical_features_model)
    all_feature_names_model = list(one_hot_feature_names_model) + numerical_features_model

    X_train_final = pd.DataFrame(X_train_processed, columns=all_feature_names_model, index=X_train.index)
    X_test_final = pd.DataFrame(X_test_processed, columns=all_feature_names_model, index=X_test.index)

    print(f"\n✅ Datos de entrenamiento y prueba preprocesados y escalados:")
    print(f"   X_train_final.shape={X_train_final.shape}")
    print(f"   X_test_final.shape={X_test_final.shape}")
    print("📋 Primeras 5 filas de X_train_final (escaladas y codificadas):")
    print(X_train_final.head())


    # 3.4 Entrenar el Modelo Random Forest Regressor (como ya lo tienes)
    print("\n--- 3.4: Entrenando el Modelo Random Forest Regressor ---")
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    rf_model.fit(X_train_final, y_train)
    print("✅ Modelo Random Forest entrenado exitosamente.")

    # 3.5 Probar el Modelo y Evaluar (Random Forest)
    print("\n--- 3.5: Evaluando el Modelo Random Forest ---")
    y_pred_train_rf = rf_model.predict(X_train_final) 
    y_pred_test_rf = rf_model.predict(X_test_final)   

    mae_test_rf = mean_absolute_error(y_test, y_pred_test_rf)
    mse_test_rf = mean_squared_error(y_test, y_pred_test_rf)
    rmse_test_rf = np.sqrt(mse_test_rf)
    r2_test_rf = r2_score(y_test, y_pred_test_rf)

    print("\n--- Métricas en el Conjunto de Prueba (Random Forest) ---")
    print(f"MAE (Error Absoluto Medio): {mae_test_rf:.2f}")
    print(f"MSE (Error Cuadrático Medio): {mse_test_rf:.2f}")
    print(f"RMSE (Raíz del Error Cuadrático Medio): {rmse_test_rf:.2f}")
    print(f"R2 Score: {r2_test_rf:.2f}")

    print("\n🎯 Fin del Modelo de Regresión No Neuronal 🎯")
    # --- FIN: PASO 3 ---


    # --- INICIO: PASO 4 - MODELO DE RED NEURONAL PARA REGRESIÓN ---
    print("\n🎯 Paso 4: ------------ Modelo de Red Neuronal para Regresión ------------------------ 🎯")

    # 4.1 Definir la Arquitectura de la Red Neuronal
    print("\n--- 4.1: Definiendo la Arquitectura de la Red Neuronal ---")
    
    # El número de neuronas en la capa de entrada es el número de características después del preprocesamiento
    input_shape = (X_train_final.shape[1],) 

    model_nn = Sequential([
        # Capa de Entrada: Define la forma de los datos de entrada
        # No tiene neuronas per se, pero establece el 'input_shape'
        keras.Input(shape=input_shape), 
        
        # Primera Capa Intermedia (oculta)
        # 64 neuronas, función de activación ReLU para introducir no-linealidad
        layers.Dense(64, activation='relu', name='hidden_layer_1'),
        
        # Segunda Capa Intermedia (oculta)
        # 32 neuronas, función de activación ReLU
        layers.Dense(32, activation='relu', name='hidden_layer_2'),
        
        # Capa de Salida
        # 1 neurona para la regresión (una sola salida numérica)
        # Función de activación 'linear' (o ninguna) para obtener valores reales continuos
        layers.Dense(1, activation='linear', name='output_layer') 
    ])

    print("✅ Arquitectura de la Red Neuronal definida.")
    model_nn.summary() # Muestra un resumen de la arquitectura del modelo

    # 4.2 Compilar el Modelo
    print("\n--- 4.2: Compilando el Modelo de Red Neuronal ---")
    # Optimizador: 'adam' es una buena elección por defecto.
    # Función de Pérdida: 'mse' (Mean Squared Error) es estándar para regresión.
    # Métricas: 'mae' (Mean Absolute Error) para monitorear durante el entrenamiento.
    model_nn.compile(optimizer='adam',
                     loss='mse',
                     metrics=['mae'])
    print("✅ Modelo de Red Neuronal compilado.")

    # 4.3 Entrenar el Modelo
    print("\n--- 4.3: Entrenando el Modelo de Red Neuronal ---")
    # history guardará el progreso del entrenamiento (pérdida y métricas por época)
    history = model_nn.fit(X_train_final, y_train,
                           epochs=100,         # Número de épocas: cuántas veces se entrena sobre todo el dataset
                           batch_size=32,      # Tamaño del lote: número de muestras por actualización de gradiente
                           validation_split=0.2, # 20% de los datos de entrenamiento se usarán para validación
                           verbose=1)          # Muestra el progreso del entrenamiento

    print("✅ Modelo de Red Neuronal entrenado exitosamente.")

    # 4.4 Probar el Modelo y Evaluar
    print("\n--- 4.4: Evaluando el Modelo de Red Neuronal en el Conjunto de Prueba ---")
    # .evaluate() devuelve la pérdida y las métricas configuradas durante la compilación
    loss_nn, mae_nn = model_nn.evaluate(X_test_final, y_test, verbose=0)
    
    # Para calcular el R2 Score, necesitamos las predicciones
    y_pred_nn = model_nn.predict(X_test_final).flatten() # .flatten() convierte el array 2D de salida (n_samples, 1) a 1D

    r2_nn = r2_score(y_test, y_pred_nn)
    mse_nn = mean_squared_error(y_test, y_pred_nn)
    rmse_nn = np.sqrt(mse_nn)

    print(f"Pérdida (MSE) en el conjunto de prueba: {loss_nn:.2f}")
    print(f"MAE en el conjunto de prueba: {mae_nn:.2f}")
    print(f"RMSE en el conjunto de prueba: {rmse_nn:.2f}")
    print(f"R2 Score en el conjunto de prueba: {r2_nn:.2f}")

    print("\n--- Resumen de Resultados de Entrenamiento (Red Neuronal) ---")
    # Opcional: Visualizar el historial de entrenamiento
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(history.history['loss'], label='Pérdida de Entrenamiento')
    plt.plot(history.history['val_loss'], label='Pérdida de Validación')
    plt.xlabel('Época')
    plt.ylabel('Pérdida (MSE)')
    plt.title('Pérdida durante el Entrenamiento y Validación')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(history.history['mae'], label='MAE de Entrenamiento')
    plt.plot(history.history['val_mae'], label='MAE de Validación')
    plt.xlabel('Época')
    plt.ylabel('MAE')
    plt.title('MAE durante el Entrenamiento y Validación')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    print("\n🎯 Fin del Modelo de Red Neuronal para Regresión 🎯")
    # --- FIN: PASO 4 ---
    
if __name__ == "__main__":
    main()