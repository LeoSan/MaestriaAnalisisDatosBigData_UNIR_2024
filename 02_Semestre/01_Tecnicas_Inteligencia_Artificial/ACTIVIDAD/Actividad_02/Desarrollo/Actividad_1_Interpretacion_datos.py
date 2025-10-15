import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, confusion_matrix, classification_report,
                           ConfusionMatrixDisplay, precision_recall_fscore_support)
import warnings
warnings.filterwarnings('ignore')

# Configuración de estilo para gráficos
plt.style.use('default')
sns.set_palette("husl")

def main():
    # PASO 0: IMPORTACIÓN DEL DATASET
    print("\n🎯 Paso 0: ----------------- Importamos el DataSet Vehículos :------------------ 🎯")

    try:
        url_descarga_directa = 'https://drive.google.com/uc?export=download&id=1jY1JAwakImo53OxBA0oiJTlAH9G5vi3d'
        df = pd.read_csv(url_descarga_directa, sep=';')
        print("✅ Dataset cargado exitosamente")
    except Exception as e:
        print(f"❌ Error al cargar el dataset: {e}")
        return

    # Caracterización inicial del dataset
    print("\n📋 Primeras 5 filas del dataset:")
    print(df.head())

    print("\n📋 INFORMACIÓN DETALLADA:")
    print(df.info())

    # PASO 1: PREPROCESAMIENTO DE DATOS
    print("\n🎯 Paso 1: ------------ Preprocesamiento de Datos ------------------------ 🎯")

    df_encoded = df.copy()
    features = ['Buying', 'Maintenance', 'Doors', 'Person', 'lug_boot', 'safety']
    target = 'class'

    # Diccionario para almacenar los encoders
    encoders = {}

    # Aplicamos LabelEncoder a cada columna categórica
    for col in features + [target]:
        le = LabelEncoder()
        df_encoded[col] = le.fit_transform(df_encoded[col])
        encoders[col] = le  # Guardamos el encoder para uso posterior
        print(f"🔍 Mapeo de {col}: {dict(zip(le.classes_, le.transform(le.classes_)))}")

    print("\n📋 Primeras 5 filas del dataset codificado:")
    print(df_encoded.head())

    # PASO 2: CARACTERIZACIÓN DEL DATASET
    print("\n🎯 Paso 2: ------------ Caracterización del Dataset ------------------------ 🎯")

    print(f"\n📋 Número total de instancias: {df_encoded.shape[0]}")
    print(f"📋 Número de atributos de entrada: {df_encoded.shape[1] - 1}")
    print(f"📋 Dataset Vehículos con {df_encoded.shape[0]} filas y {df_encoded.shape[1]} columnas")

    # Descripción mejorada de atributos
    column_desc = {
        "Buying": "Precio de compra del vehículo, clasificado en categorías como vhigh (muy alto), high (alto), med (medio) y low (bajo).",
        "Maintenance": "Costo de mantenimiento del vehículo, con la misma categorización que buying.",
        "Doors": "Número de puertas del automóvil, expresado en valores numéricos como '2', '3', '4', o '5more' (5 o más).",
        "Person": "Capacidad de ocupantes del automóvil, con valores como '2', '4' y 'more' (más de 4).",
        "lug_boot": "Tamaño del maletero, categorizado como small (pequeño), med (medio) o big (grande)",
        "safety": "Nivel de seguridad del automóvil, clasificado como low (bajo), med (medio) o high (alto)"
    }

    print("\n📋 Descripción de atributos de entrada y su tipo:")
    for col in features:
        print(f"🔍 Atributo: {col}")
        print(f"   Descripción: {column_desc[col]}")
        print(f"   Tipo: categórico")
        print(f"   Valores únicos: {sorted(df[col].unique())}")
        print()

    # Información de la clase objetivo
    print("📋 Información de la clase objetivo:")
    print(f"- Columna de clase: '{target}'")
    print(f"- Número de clases: {df_encoded[target].nunique()}")

    print("\n📋 Distribución de las clases:")
    class_counts = df[target].value_counts()
    class_percentages = (class_counts / len(df) * 100).round(2)

    for clase, count in class_counts.items():
        percentage = class_percentages[clase]
        print(f"   {clase}: {count} instancias ({percentage}%)")

    # Verificar valores nulos
    print("\n📋 Valores nulos por columna:")
    null_counts = df_encoded.isnull().sum()
    if null_counts.sum() == 0:
        print("✅ No hay valores nulos en el dataset")
    else:
        print(null_counts)

    print("\n📋 ESTADÍSTICAS DESCRIPTIVAS:")
    print(df_encoded.describe(include='all'))


    # PASO 3: VISUALIZACIÓN DE DATOS
    print("\n🎯 Paso 3: ------------ Descripción Gráfica datos originales ------------------------ 🎯")

    # Crear figura con subplots mejorados
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('Análisis Exploratorio del Dataset de Vehículos', fontsize=16, fontweight='bold')

    # Distribución de la clase objetivo
    sns.countplot(data=df, x=target, ax=axes[0, 0])
    axes[0, 0].set_title('Distribución de Clases de Aceptabilidad')
    axes[0, 0].set_xlabel('Clase')
    axes[0, 0].set_ylabel('Conteo')
    axes[0, 0].tick_params(axis='x', rotation=45)

    # Distribuciones de características
    characteristics = ['Buying', 'Maintenance', 'Doors', 'safety', 'lug_boot']

    for i, char in enumerate(characteristics):
        row = (i + 1) // 3
        col = (i + 1) % 3
        sns.countplot(data=df, x=char, ax=axes[row, col])
        axes[row, col].set_title(f'Distribución de {char}')
        axes[row, col].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()

    # PASO 4: PREPARACIÓN PARA MODELADO
    print("\n🎯 Paso 4: ------------ Preparación del dataset para modelado ------------------------ 🎯")

    # Definir características y variable objetivo
    X = df_encoded[features]
    y = df_encoded[target]

    # División del dataset con validación
    X_train, X_test, y_train, y_test = train_test_split(
        X,      #   Características de entrada
        y,      #   Variable objetivo
        test_size=0.3,      # 30% para prueba
        random_state=42,    # Para reproducibilidad
        stratify=y          # Mantener proporción de clases
    )

    print("📋 División del dataset completada:")
    print(f"✅ Dimensiones de X_train: {X_train.shape}")
    print(f"✅ Dimensiones de X_test: {X_test.shape}")
    print(f"✅ Proporción de entrenamiento: {X_train.shape[0]/(X_train.shape[0]+X_test.shape[0]):.1%}")
    print(f"✅ Proporción de prueba: {X_test.shape[0]/(X_train.shape[0]+X_test.shape[0]):.1%}")


    # PASO 5: ENTRENAMIENTO DE MODELOS
    print("\n🎯 Paso 5: ------------ Entrenamiento de Modelos ------------------------ 🎯")

    # Decision Tree con parámetros optimizados
    print("🌳 Entrenando Arbol de Decisión...")
    dt_model = DecisionTreeClassifier(
        random_state=42,         # Semilla para reproducibilidad
        max_depth=10,            # Profundidad máxima del árbol
        min_samples_split=5,     # Mínimo de muestras para dividir un nodo
        min_samples_leaf=2,      # Mínimo de muestras en una hoja
        criterion='gini'         # Criterio de división
    )
    dt_model.fit(X_train, y_train)
    y_pred_dt = dt_model.predict(X_test)

    # Random Forest
    print("🌲 Entrenando Bosque Aleatorio...")
    rf_model = RandomForestClassifier(
        n_estimators=100,    # Número de árboles en el bosque
        random_state=42,     # Semilla para reproducibilidad
        max_depth=10,        # Profundidad máxima de los árboles
        min_samples_split=5, # Mínimo de muestras para dividir un nodo
        min_samples_leaf=2   # Mínimo de muestras en una hoja
    )
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)


    # PASO 6: EVALUACIÓN DE MODELOS
    print("\n🎯 Paso 6: ------------ Evaluación de Modelos ------------------------ 🎯")

    # Función para evaluar modelo
    def evaluate_model(y_true, y_pred, model_name, encoder):
        """Función para evaluar un modelo de clasificación"""
        print(f"\n🧠 ------- Evaluación del Modelo {model_name} -------")

        # efectividad
        efectividad = accuracy_score(y_true, y_pred)
        print(f"🎯 Efectividad: {efectividad:.4f} ({efectividad*100:.2f}%)")


        # Instancias correctas e incorrectas
        correct = int(efectividad * len(y_true))
        incorrect = len(y_true) - correct
        print(f"✅ Instancias clasificadas correctamente: {correct}")
        print(f"❌ Instancias clasificadas incorrectamente: {incorrect}")

        # Matriz de confusión
        cm = confusion_matrix(y_true, y_pred)
        print(f"\n📊 Matriz de Confusión:")
        print(cm)

        # Reporte de clasificación
        class_names = encoder.inverse_transform(sorted(np.unique(y_true)))
        print(f"\n📈 Reporte de Clasificación:")
        print(classification_report(y_true, y_pred, target_names=class_names))

        return efectividad, cm, class_names

    # Evaluar ambos modelos
    target_encoder = encoders[target]

    dt_efectividad, dt_cm, class_names = evaluate_model(y_test, y_pred_dt, "Árbol decisión", target_encoder)
    rf_efectividad, rf_cm, class_names = evaluate_model(y_test, y_pred_rf, "Bosque Aleatorio", target_encoder)


    # PASO 7: COMPARACIÓN Y VISUALIZACIÓN DE RESULTADOS
    print("\n🎯 Paso 7: ------------ Comparación de Resultados ------------------------ 🎯")

    # Comparación de accuracies
    models = ['Árbol decisión', 'Bosque Aleatorio']
    accuracies = [dt_efectividad, rf_efectividad]

    # Gráfico de comparación
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Comparación de efectividad
    bars = axes[0].bar(models, accuracies, color=['skyblue', 'red'])
    axes[0].set_title('Comparación de efectividad entre Modelos', fontweight='bold')
    axes[0].set_ylabel('efectividad')
    axes[0].set_ylim(0, 1)

    # Agregar valores en las barras
    for bar, acc in zip(bars, accuracies):
        height = bar.get_height()
        axes[0].text(bar.get_x() + bar.get_width()/2., height + 0.01,
                    f'{acc:.3f}', ha='center', va='bottom', fontweight='bold')

    # Matrices de confusión
    sns.heatmap(dt_cm, annot=True, fmt='d', cmap='Blues', ax=axes[1],
                xticklabels=class_names, yticklabels=class_names)
    axes[1].set_title('Matriz de Confusión: Árbol decisión', fontweight='bold')
    axes[1].set_xlabel('Predicho')
    axes[1].set_ylabel('Real')

    sns.heatmap(rf_cm, annot=True, fmt='d', cmap='Reds', ax=axes[2],
                xticklabels=class_names, yticklabels=class_names)
    axes[2].set_title('Matriz de Confusión: Bosque Aleatorio', fontweight='bold')
    axes[2].set_xlabel('Predicho')
    axes[2].set_ylabel('Real')

    plt.tight_layout()
    plt.show()

    # Resumen final
    print("\n🏆 RESUMEN FINAL:")
    print("=" * 50)
    print(f"🌳 Árbol decisión - efectividad: {dt_efectividad:.4f} ({dt_efectividad*100:.2f}%)")
    print(f"🌲 Bosque Aleatorio - efectividad: {rf_efectividad:.4f} ({rf_efectividad*100:.2f}%)")

    best_model = "Bosque Aleatorio" if rf_efectividad > dt_efectividad else "Árbol decisión"
    best_efectividad = max(rf_efectividad, dt_efectividad)
    print(f"\n🥇 Mejor modelo: {best_model} con {best_efectividad:.4f} de efectividad")

    # Importancia de características para Bosque Aleatorio
    if rf_efectividad >= dt_efectividad:
        print(f"\n📊 Importancia de características ({best_model}):")
        feature_importance = pd.DataFrame({
            'feature': features,
            'importance': rf_model.feature_importances_
        }).sort_values('importance', ascending=False)

        for _, row in feature_importance.iterrows():
            print(f"   {row['feature']}: {row['importance']:.4f}")

if __name__ == "__main__":
    main()
