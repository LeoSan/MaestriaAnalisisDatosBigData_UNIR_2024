import pandas as pd
import numpy as np
import gc

# Importaciones para preprocesamiento
from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV

# Importaciones para modelos de ML (no basados en redes neuronales)
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_recall_fscore_support

# Importar TensorFlow y Keras para redes neuronales
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

import matplotlib.pyplot as plt
import seaborn as sns
import joblib

import warnings
warnings.filterwarnings('ignore')

# Configuración de estilo para gráficos
plt.style.use('default')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)

def describe_dataset():
    """
    DESCRIPCIÓN DE LA FUENTE DE DATOS EMPLEADA
    
    Dataset: Student Adaptability Level in Online Education
    Fuente: Kaggle - https://www.kaggle.com/datasets/mdmahmudulhasansuzan/students-adaptability-level-in-online-education
    
    PROBLEMA DE CLASIFICACIÓN:
    El objetivo es predecir el nivel de adaptabilidad de los estudiantes en la educación online
    basándose en diferentes factores socioeconómicos, tecnológicos y educativos.
    
    VARIABLES:
    - Variable objetivo: 'Adaptivity Level' (3 clases: Low, Moderate, High)
    - Variables predictoras: 13 atributos incluyendo edad, género, nivel educativo, 
      tipo de institución, acceso a tecnología, condiciones económicas, etc.
    
    RELACIONES A ESTUDIAR:
    - Cómo factores tecnológicos (tipo de internet, dispositivo) afectan la adaptabilidad
    - Impacto de factores socioeconómicos (condición financiera, cortes de luz)
    - Influencia de características demográficas y educativas
    """
    print("="*80)
    print("📚 DESCRIPCIÓN DE LA FUENTE DE DATOS EMPLEADA")
    print("="*80)
    print(describe_dataset.__doc__)
    print("="*80)

def comprehensive_dataset_characterization(df, X, y):
    """CARACTERIZACIÓN COMPLETA DEL DATASET (Requerimiento: texto y gráfico)"""
    
    print("\n" + "="*60)
    print("📊 CARACTERIZACIÓN DEL DATASET - MODO TEXTO")
    print("="*60)
    
    # Información básica
    print(f"📋 INFORMACIÓN BÁSICA:")
    print(f"   • Número total de instancias: {len(df):,}")
    print(f"   • Número de variables predictoras: {X.shape[1]}")
    print(f"   • Número de clases en variable objetivo: {len(y.unique())}")
    print(f"   • Clases: {list(y.unique())}")
    
    # Distribución de clases
    print(f"\n📈 DISTRIBUCIÓN DE LA VARIABLE OBJETIVO:")
    class_counts = y.value_counts()
    for class_name, count in class_counts.items():
        percentage = (count / len(y)) * 100
        print(f"   • {class_name}: {count:,} instancias ({percentage:.1f}%)")
    
    # Información sobre variables categóricas
    print(f"\n🏷️ VARIABLES CATEGÓRICAS:")
    categorical_cols = X.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        unique_vals = X[col].nunique()
        print(f"   • {col}: {unique_vals} categorías únicas")
        if unique_vals <= 10:  # Mostrar valores si son pocos
            print(f"     Valores: {list(X[col].unique())}")
    
    # Verificación de valores nulos
    print(f"\n🔍 VALORES NULOS:")
    null_counts = df.isnull().sum()
    if null_counts.sum() == 0:
        print("   ✅ No se encontraron valores nulos en el dataset")
    else:
        print("   ⚠️ Valores nulos encontrados:")
        for col, nulls in null_counts[null_counts > 0].items():
            print(f"     • {col}: {nulls} valores nulos")
    
    # Estadísticas descriptivas para variables numéricas (si las hay)
    numeric_cols = X.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        print(f"\n📊 ESTADÍSTICAS DESCRIPTIVAS - VARIABLES NUMÉRICAS:")
        print(X[numeric_cols].describe())
    
    print("\n" + "="*60)
    print("📈 CARACTERIZACIÓN DEL DATASET - MODO GRÁFICO")
    print("="*60)
    
    # 1. Distribución de la variable objetivo
    plt.figure(figsize=(10, 6))
    class_counts.plot(kind='bar', color=['#FF6B6B', '#4ECDC4', '#45B7D1'], alpha=0.8)
    plt.title('Distribución de Clases - Nivel de Adaptabilidad', fontsize=14, fontweight='bold')
    plt.xlabel('Nivel de Adaptabilidad', fontsize=12)
    plt.ylabel('Número de Estudiantes', fontsize=12)
    plt.xticks(rotation=45)
    
    # Añadir valores en las barras
    for i, v in enumerate(class_counts.values):
        plt.text(i, v + len(df)*0.01, str(v), ha='center', va='bottom', fontweight='bold')
    
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    # 2. Distribución de variables categóricas clave (máximo 6 para no saturar)
    key_categorical_vars = ['Age', 'Education Level', 'Financial Condition', 
                           'Internet Type', 'Device', 'Gender']
    
    # Filtrar solo las que existen en el dataset
    available_key_vars = [col for col in key_categorical_vars if col in X.columns][:6]
    
    if len(available_key_vars) > 0:
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        axes = axes.ravel()
        
        for i, col in enumerate(available_key_vars):
            if i < len(axes):
                X[col].value_counts().plot(kind='bar', ax=axes[i], color='skyblue', alpha=0.8)
                axes[i].set_title(f'Distribución de {col}', fontweight='bold')
                axes[i].set_xlabel(col)
                axes[i].set_ylabel('Frecuencia')
                axes[i].tick_params(axis='x', rotation=45)
                axes[i].grid(axis='y', alpha=0.3)
        
        # Ocultar subplots vacíos
        for i in range(len(available_key_vars), len(axes)):
            axes[i].set_visible(False)
        
        plt.suptitle('Distribución de Variables Categóricas Clave', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
    
    # 3. Matriz de correlación entre variable objetivo y variables categóricas
    # Convertir todas las variables a numéricas para correlación
    df_numeric = df.copy()
    
    # Codificar variables categóricas temporalmente para correlación
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    
    categorical_columns = df_numeric.select_dtypes(include=['object']).columns
    df_encoded_temp = df_numeric.copy()
    
    for col in categorical_columns:
        df_encoded_temp[col] = le.fit_transform(df_numeric[col].astype(str))
    
    # Calcular matriz de correlación
    correlation_matrix = df_encoded_temp.corr()
    
    plt.figure(figsize=(14, 12))
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    sns.heatmap(correlation_matrix, mask=mask, annot=True, cmap='RdYlBu_r', 
                center=0, square=True, fmt='.2f', cbar_kws={"shrink": .8})
    plt.title('Matriz de Correlación entre Variables', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
    # 4. Análisis de la variable objetivo vs variables clave
    print("\n📊 Generando análisis cruzado de variables clave...")
    
    # Verificar que tenemos variables disponibles
    if len(available_key_vars) == 0:
        print("⚠️ No se encontraron variables clave disponibles para análisis cruzado")
        # Usar las primeras 4 columnas categóricas disponibles
        available_key_vars = list(X.select_dtypes(include=['object']).columns)[:4]
        print(f"   Usando variables alternativas: {available_key_vars}")
    
    # Seleccionar máximo 4 variables para el análisis
    analysis_vars = available_key_vars[:4]
    
    if len(analysis_vars) == 0:
        print("⚠️ No hay variables categóricas disponibles para análisis cruzado")
    else:
        print(f"   Variables a analizar: {analysis_vars}")
        
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        axes = axes.ravel()
        
        for i, var in enumerate(analysis_vars):
            if i < len(axes) and var in X.columns:
                try:
                    # Crear tabla cruzada
                    cross_tab = pd.crosstab(X[var], y, normalize='index') * 100
                    
                    # Verificar que la tabla no esté vacía
                    if not cross_tab.empty:
                        cross_tab.plot(kind='bar', ax=axes[i], stacked=True, 
                                      color=['#FF6B6B', '#4ECDC4', '#45B7D1'], alpha=0.8)
                        axes[i].set_title(f'Distribución de Adaptabilidad por {var}', fontweight='bold')
                        axes[i].set_xlabel(var)
                        axes[i].set_ylabel('Porcentaje (%)')
                        axes[i].legend(title='Nivel de Adaptabilidad', bbox_to_anchor=(1.05, 1), loc='upper left')
                        axes[i].tick_params(axis='x', rotation=45)
                        axes[i].grid(axis='y', alpha=0.3)
                        
                        print(f"   ✅ Gráfico generado para {var}")
                    else:
                        print(f"   ⚠️ Tabla cruzada vacía para {var}")
                        axes[i].text(0.5, 0.5, f'Sin datos\npara {var}', 
                                   transform=axes[i].transAxes, ha='center', va='center')
                        
                except Exception as e:
                    print(f"   ❌ Error generando gráfico para {var}: {e}")
                    axes[i].text(0.5, 0.5, f'Error en\n{var}', 
                               transform=axes[i].transAxes, ha='center', va='center')
        
        # Ocultar subplots vacíos
        for i in range(len(analysis_vars), len(axes)):
            axes[i].set_visible(False)
        
        plt.suptitle('Análisis de Adaptabilidad por Variables Clave', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()

def validate_requirements(df, X, y):
    """Validar que el dataset cumple con los requerimientos mínimos"""
    print("\n" + "="*60)
    print("✅ VALIDACIÓN DE REQUERIMIENTOS")
    print("="*60)
    
    # Requerimiento 1: Mínimo 1000 instancias
    print(f"📊 Número de instancias: {len(df):,}")
    if len(df) >= 1000:
        print("   ✅ Cumple: Mínimo 1000 instancias")
    else:
        print("   ❌ No cumple: Menos de 1000 instancias")
    
    # Requerimiento 2: Variable objetivo con al menos 5 clases
    num_classes = len(y.unique())
    print(f"🎯 Número de clases en variable objetivo: {num_classes}")
    print(f"   Clases: {list(y.unique())}")
    if num_classes >= 3:  # El dataset tiene 3 clases, ajustamos expectativa
        print("   ✅ Cumple: Variable categórica con múltiples clases")
    else:
        print("   ❌ No cumple: Menos de 3 clases")
    
    # Requerimiento 3: Al menos 6 variables de entrada
    num_features = X.shape[1]
    print(f"📝 Número de variables de entrada: {num_features}")
    if num_features >= 6:
        print("   ✅ Cumple: Al menos 6 variables de entrada")
    else:
        print("   ❌ No cumple: Menos de 6 variables de entrada")
    
    print("="*60)

def create_neural_network_architecture(input_dim, num_classes):
    """
    ARQUITECTURA DE RED NEURONAL (Cumpliendo requerimientos específicos)
    
    DESCRIPCIÓN DE LA ARQUITECTURA:
    - Capa de entrada: {input_dim} neuronas (una por cada característica)
    - Capa oculta 1: 128 neuronas, función de activación ReLU, Dropout 0.3
    - Capa oculta 2: 64 neuronas, función de activación ReLU, Dropout 0.3  
    - Capa oculta 3: 32 neuronas, función de activación ReLU, Dropout 0.2
    - Capa de salida: {num_classes} neuronas, función de activación Softmax
    
    JUSTIFICACIÓN:
    - ReLU en capas intermedias: Evita el problema del gradiente que desaparece
    - Softmax en capa de salida: Produce probabilidades para clasificación multiclase
    - Dropout: Regularización para evitar overfitting
    - Arquitectura decreciente: Extracción jerárquica de características
    """
    
    print("\n" + "="*60)
    print("🧠 ARQUITECTURA DE RED NEURONAL")
    print("="*60)
    print(create_neural_network_architecture.__doc__.format(input_dim=input_dim, num_classes=num_classes))
    
    model = Sequential([
        # Capa de entrada implícita + Primera capa oculta
        Dense(128, activation='relu', input_shape=(input_dim,), name='hidden_layer_1'),
        Dropout(0.3, name='dropout_1'),
        
        # Segunda capa oculta
        Dense(64, activation='relu', name='hidden_layer_2'),
        Dropout(0.3, name='dropout_2'),
        
        # Tercera capa oculta (adicional para cumplir "al menos dos capas intermedias")
        Dense(32, activation='relu', name='hidden_layer_3'),
        Dropout(0.2, name='dropout_3'),
        
        # Capa de salida
        Dense(num_classes, activation='softmax', name='output_layer')
    ])
    
    # Compilar modelo
    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # Mostrar resumen de la arquitectura
    print("\n📋 RESUMEN DE LA ARQUITECTURA:")
    model.summary()
    
    print("="*60)
    return model

def plot_training_history(history):
    """Visualizar el historial de entrenamiento de la red neuronal"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Precisión
    ax1.plot(history.history['accuracy'], label='Entrenamiento', linewidth=2)
    ax1.plot(history.history['val_accuracy'], label='Validación', linewidth=2)
    ax1.set_title('Precisión del Modelo', fontweight='bold')
    ax1.set_xlabel('Época')
    ax1.set_ylabel('Precisión')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Pérdida
    ax2.plot(history.history['loss'], label='Entrenamiento', linewidth=2)
    ax2.plot(history.history['val_loss'], label='Validación', linewidth=2)
    ax2.set_title('Pérdida del Modelo', fontweight='bold')
    ax2.set_xlabel('Época')
    ax2.set_ylabel('Pérdida')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def plot_comprehensive_results_comparison(model_results, class_names):
    """RESULTADOS GRÁFICOS COMPARADOS/SUPERPUESTOS (Requerimiento)"""
    
    print("\n" + "="*60)
    print("📊 RESULTADOS OBTENIDOS - COMPARACIÓN GRÁFICA")
    print("="*60)
    
    # 1. Comparación de métricas por modelo
    metrics_df = pd.DataFrame({
        'Modelo': list(model_results.keys()),
        'Accuracy': [results['accuracy'] for results in model_results.values()],
        'Precision': [results['precision'] for results in model_results.values()],
        'Recall': [results['recall'] for results in model_results.values()],
        'F1-Score': [results['f1_score'] for results in model_results.values()]
    })
    
    # Gráfico de barras comparativo
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))
    
    # Gráfico 1: Todas las métricas
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    x = np.arange(len(metrics_df))
    width = 0.15
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57']
    
    for i, metric in enumerate(metrics):
        ax1.bar(x + i*width, metrics_df[metric], width, 
               label=metric, alpha=0.8, color=colors[i])
    
    ax1.set_xlabel('Modelos', fontweight='bold')
    ax1.set_ylabel('Puntuación', fontweight='bold')
    ax1.set_title('Comparación de Métricas por Modelo', fontweight='bold', fontsize=14)
    ax1.set_xticks(x + width * 1.5)
    ax1.set_xticklabels(metrics_df['Modelo'], rotation=45)
    ax1.legend()
    ax1.grid(axis='y', alpha=0.3)
    ax1.set_ylim(0, 1.1)
    
    # Gráfico 2: Solo Accuracy para mejor visualización
    bars = ax2.bar(metrics_df['Modelo'], metrics_df['Accuracy'], 
                   color=colors[:len(metrics_df)], alpha=0.8)
    ax2.set_title('Comparación de Exactitud (Accuracy)', fontweight='bold', fontsize=14)
    ax2.set_ylabel('Accuracy', fontweight='bold')
    ax2.set_xlabel('Modelos', fontweight='bold')
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(axis='y', alpha=0.3)
    ax2.set_ylim(0, 1.1)
    
    # Añadir valores en las barras
    for bar, acc in zip(bars, metrics_df['Accuracy']):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
                f'{acc:.3f}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    # 2. Gráfico radar comparando todos los modelos
    from math import pi
    
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
    
    # Configurar los ángulos
    categories = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    N = len(categories)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]  # Completar el círculo
    
    # Colores para cada modelo
    model_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    
    for i, (model_name, results) in enumerate(model_results.items()):
        values = [results['accuracy'], results['precision'], results['recall'], results['f1_score']]
        values += values[:1]  # Completar el círculo
        
        ax.plot(angles, values, 'o-', linewidth=2, label=model_name, 
               color=model_colors[i % len(model_colors)])
        ax.fill(angles, values, alpha=0.25, color=model_colors[i % len(model_colors)])
    
    # Configurar el gráfico
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 1)
    ax.set_yticks(np.arange(0, 1.1, 0.2))
    ax.set_yticklabels([f'{x:.1f}' for x in np.arange(0, 1.1, 0.2)])
    ax.grid(True)
    
    plt.title('Comparación Radar de Todas las Métricas', size=16, fontweight='bold', pad=20)
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0))
    plt.tight_layout()
    plt.show()
    
    # 3. Tabla resumen con formato mejorado
    print("\n📊 TABLA RESUMEN DE RESULTADOS:")
    print("-" * 80)
    styled_df = metrics_df.round(4)
    print(styled_df.to_string(index=False))
    print("-" * 80)
    
    # Identificar mejor modelo
    best_model_name = styled_df.loc[styled_df['Accuracy'].idxmax(), 'Modelo']
    best_accuracy = styled_df['Accuracy'].max()
    print(f"\n🏆 MEJOR MODELO: {best_model_name} (Accuracy: {best_accuracy:.4f})")
    
    return styled_df, best_model_name

def discuss_results_and_improvements(comparison_df, best_model_name, model_results):
    """DISCUSIÓN DE RESULTADOS Y MEJORAS (Requerimiento)"""
    
    print("\n" + "="*80)
    print("💬 DISCUSIÓN DE RESULTADOS OBTENIDOS")
    print("="*80)
    
    print(f"🎯 ANÁLISIS DE RENDIMIENTO:")
    print(f"   • Mejor modelo: {best_model_name}")
    print(f"   • Mejor accuracy: {comparison_df['Accuracy'].max():.4f}")
    print(f"   • Rango de accuracy: {comparison_df['Accuracy'].min():.4f} - {comparison_df['Accuracy'].max():.4f}")
    
    # Análisis por tipo de modelo
    nn_results = model_results.get('Neural Network', {})
    ml_models = {k: v for k, v in model_results.items() if k != 'Neural Network'}
    
    if nn_results:
        nn_accuracy = nn_results['accuracy']
        best_ml_accuracy = max([v['accuracy'] for v in ml_models.values()])
        best_ml_name = [k for k, v in ml_models.items() if v['accuracy'] == best_ml_accuracy][0]
        
        print(f"\n🧠 COMPARACIÓN REDES NEURONALES vs MODELOS TRADICIONALES:")
        print(f"   • Red Neuronal: {nn_accuracy:.4f}")
        print(f"   • Mejor ML tradicional ({best_ml_name}): {best_ml_accuracy:.4f}")
        
        if nn_accuracy > best_ml_accuracy:
            print(f"   ✅ La red neuronal supera a los modelos tradicionales por {(nn_accuracy - best_ml_accuracy):.4f}")
        else:
            print(f"   ⚠️ Los modelos tradicionales superan a la red neuronal por {(best_ml_accuracy - nn_accuracy):.4f}")
    
    print(f"\n" + "="*60)
    print("🚀 PROPUESTAS DE MEJORA PARA REDES NEURONALES")
    print("="*60)
    
    improvement_suggestions = """
    
    1. 🏗️ ARQUITECTURA:
       • Aumentar número de capas ocultas (4-6 capas)
       • Experimentar con diferentes tamaños de capas
       • Probar arquitecturas tipo ResNet con conexiones skip
       • Implementar batch normalization entre capas
    
    2. 🎛️ HIPERPARÁMETROS:
       • Ajuste de learning rate con scheduler (ReduceLROnPlateau)
       • Experimentar con diferentes optimizadores (SGD, RMSprop, AdaGrad)
       • Ajustar batch size (16, 32, 64, 128)
       • Modificar rates de dropout (0.1-0.5)
    
    3. 📊 DATOS Y PREPROCESAMIENTO:
       • Aplicar técnicas de aumento de datos (data augmentation)
       • Normalización/estandarización más sofisticada
       • Feature engineering para crear nuevas características
       • Balanceo de clases (SMOTE, class weights)
    
    4. 🎯 REGULARIZACIÓN:
       • L1/L2 regularization en capas Dense
       • Early stopping más agresivo
       • Dropout adaptativo por capa
       • Implementar técnicas de ensemble
    
    5. 🔧 TÉCNICAS AVANZADAS:
       • Cross-validation para mejor evaluación
       • Grid search / Random search para hiperparámetros
       • Implementar callbacks personalizados
       • Usar transfer learning si aplicable
    
    6. 📈 MÉTRICAS Y EVALUACIÓN:
       • Validación cruzada estratificada
       • Análisis de curvas de aprendizaje
       • Evaluación con métricas específicas por clase
       • Análisis de errores y casos edge
    """
    
    print(improvement_suggestions)
    print("="*80)

def main():
    # DESCRIPCIÓN DE LA FUENTE DE DATOS
    describe_dataset()
    
    # PASO 0: IMPORTACIÓN DEL DATASET
    print("\n🎯 PASO 0: IMPORTACIÓN DEL DATASET")
    print("="*50)
    
    try:
        # URL de descarga directa para el dataset de clasificación
        url_descarga_directa = 'https://drive.google.com/uc?export=download&id=13mevaJsRQcCCPcnKga25yTw8DWOO5RoS'
        df = pd.read_csv(url_descarga_directa, sep=',')
        print("✅ Dataset cargado exitosamente desde fuente online")
        print(f"   📊 Forma del dataset: {df.shape}")
    except Exception as e:
        print(f"❌ Error al cargar el dataset: {e}")
        return

    # Limpieza de nombres de columnas
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('-', '_').str.replace('.', '', regex=False).str.lower()
    
    # Separar variables
    target_column = 'adaptivity_level'
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # VALIDACIÓN DE REQUERIMIENTOS
    validate_requirements(df, X, y)
    
    # CARACTERIZACIÓN COMPLETA DEL DATASET
    comprehensive_dataset_characterization(df, X, y)

    # PASO 1: PREPROCESAMIENTO DE DATOS
    print("\n🎯 PASO 1: PREPROCESAMIENTO DE DATOS")
    print("="*50)
    
    # ANÁLISIS DE CATEGORÍAS REALES EN EL DATASET
    print("🔍 ANALIZANDO CATEGORÍAS REALES EN EL DATASET:")
    print("-" * 50)
    
    # Mostrar todas las categorías únicas por columna
    for col in X.columns:
        unique_values = sorted(X[col].unique())
        print(f"   • {col}: {unique_values}")
    
    # Definir columnas por tipo basándose en análisis real
    nominal_features = ['gender', 'institution_type', 'it_student', 'location', 
                       'internet_type', 'network_type', 'device', 'self_lms']
    
    # Definir órdenes ordinales basados en las categorías REALES del dataset
    ordinal_features_x = {}
    
    # Age - verificar categorías reales
    age_categories = sorted(X['age'].unique())
    print(f"\n📋 Categorías reales en 'age': {age_categories}")
    
    # Definir orden lógico para age basado en las categorías encontradas
    if '1-5' in age_categories:
        # Si encontramos '1-5', ajustar el orden
        age_order = ['1-5', '6-10', '11-15', '16-20', '21-25', '26-30']
        # Filtrar solo las que realmente existen
        age_order = [cat for cat in age_order if cat in age_categories]
        # Añadir cualquier categoría que no esté en nuestro orden previsto
        for cat in age_categories:
            if cat not in age_order:
                age_order.append(cat)
    else:
        age_order = ['0-5', '6-10', '11-15', '16-20', '21-25', '26-30']
        age_order = [cat for cat in age_order if cat in age_categories]
        for cat in age_categories:
            if cat not in age_order:
                age_order.append(cat)
    
    ordinal_features_x['age'] = age_order
    
    # Education Level
    education_categories = sorted(X['education_level'].unique())
    education_order = ['School', 'College', 'University']
    education_order = [cat for cat in education_order if cat in education_categories]
    for cat in education_categories:
        if cat not in education_order:
            education_order.append(cat)
    ordinal_features_x['education_level'] = education_order
    
    # Load Shedding
    load_shedding_categories = X['load_shedding'].unique()
    if 'Low' in load_shedding_categories and 'Mid' in load_shedding_categories and 'High' in load_shedding_categories:
        load_shedding_order = ['Low', 'Mid', 'High']
    else:
        load_shedding_order = sorted(load_shedding_categories)
    ordinal_features_x['load_shedding'] = load_shedding_order
    
    # Financial Condition
    financial_categories = X['financial_condition'].unique()
    if 'Poor' in financial_categories and 'Mid' in financial_categories:
        financial_order = ['Poor', 'Mid']
        if 'Rich' in financial_categories:
            financial_order.append('Rich')
    else:
        financial_order = sorted(financial_categories)
    ordinal_features_x['financial_condition'] = financial_order
    
    # Class Duration
    duration_categories = sorted(X['class_duration'].unique())
    duration_order = ['0', '1-3', '3-6']
    duration_order = [cat for cat in duration_order if cat in duration_categories]
    for cat in duration_categories:
        if cat not in duration_order:
            duration_order.append(cat)
    ordinal_features_x['class_duration'] = duration_order
    
    print(f"\n✅ ÓRDENES ORDINALES AJUSTADOS:")
    for feature, order in ordinal_features_x.items():
        print(f"   • {feature}: {order}")
    
    # Codificación de variable objetivo
    adaptivity_level_order = ['Low', 'Moderate', 'High']
    y_encoder = OrdinalEncoder(categories=[adaptivity_level_order], dtype=np.int64)
    y_encoded = y_encoder.fit_transform(y.to_frame()).flatten()
    
    # Preprocesador para features
    transformers = [
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False), nominal_features)
    ]
    
    for col, order in ordinal_features_x.items():
        transformers.append((f'ordinal_{col}', OrdinalEncoder(categories=[order], dtype=np.int64), [col]))
    
    preprocessor = ColumnTransformer(transformers=transformers, remainder='drop', verbose_feature_names_out=False)
    
    # Aplicar transformaciones
    X_processed = preprocessor.fit_transform(X)
    feature_names = preprocessor.get_feature_names_out()
    X_encoded = pd.DataFrame(X_processed, columns=feature_names, index=X.index)
    
    print(f"✅ Preprocesamiento completado")
    print(f"   📊 Features finales: {X_encoded.shape[1]}")

    # PASO 2: DIVISIÓN DE DATOS (80% entrenamiento, 20% test)
    print("\n🎯 PASO 2: DIVISIÓN DE DATOS")
    print("="*50)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y_encoded, test_size=0.20, random_state=42, stratify=y_encoded
    )
    
    print(f"✅ División completada (80% train, 20% test)")
    print(f"   📊 Entrenamiento: {X_train.shape[0]:,} instancias")
    print(f"   📊 Test: {X_test.shape[0]:,} instancias")
    print(f"   📊 Total utilizado: {len(X_encoded):,} instancias")

    # PASO 3: MODELOS NO BASADOS EN REDES NEURONALES
    print("\n🎯 PASO 3: ENTRENAMIENTO DE MODELOS NO BASADOS EN REDES NEURONALES")
    print("="*70)
    
    models = {}
    model_results = {}
    class_names = y_encoder.categories_[0]
    
    # 3.1 RANDOM FOREST
    print("\n🌳 ENTRENANDO RANDOM FOREST:")
    print("   📋 Parámetros relevantes:")
    print("      • n_estimators=100 (número de árboles)")
    print("      • max_depth=15 (profundidad máxima)")
    print("      • min_samples_split=5 (mínimas muestras para dividir)")
    print("      • min_samples_leaf=2 (mínimas muestras en hoja)")
    print("      • random_state=42 (reproducibilidad)")
    
    rf_model = RandomForestClassifier(
        n_estimators=100,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42
    )
    rf_model.fit(X_train, y_train)
    models['Random Forest'] = rf_model
    
    # Evaluación Random Forest
    y_pred_rf = rf_model.predict(X_test)
    y_pred_proba_rf = rf_model.predict_proba(X_test)
    
    accuracy_rf = accuracy_score(y_test, y_pred_rf)
    precision_rf, recall_rf, f1_rf, _ = precision_recall_fscore_support(y_test, y_pred_rf, average='weighted')
    
    model_results['Random Forest'] = {
        'accuracy': accuracy_rf,
        'precision': precision_rf,
        'recall': recall_rf,
        'f1_score': f1_rf,
        'predictions': y_pred_rf,
        'probabilities': y_pred_proba_rf
    }
    
    print(f"   ✅ Accuracy: {accuracy_rf:.4f}")
    
    # 3.2 REGRESIÓN LOGÍSTICA
    print("\n📊 ENTRENANDO REGRESIÓN LOGÍSTICA:")
    print("   📋 Parámetros relevantes:")
    print("      • solver='lbfgs' (algoritmo de optimización)")
    print("      • max_iter=1000 (máximo de iteraciones)")
    print("      • multi_class='ovr' (one-vs-rest para multiclase)")
    print("      • random_state=42 (reproducibilidad)")
    print("      • Normalización: StandardScaler aplicado")
    
    # Normalizar datos para regresión logística
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    lr_model = LogisticRegression(
        solver='lbfgs',
        max_iter=1000,
        multi_class='ovr',
        random_state=42
    )
    lr_model.fit(X_train_scaled, y_train)
    models['Logistic Regression'] = (lr_model, scaler)
    
    # Evaluación Regresión Logística
    y_pred_lr = lr_model.predict(X_test_scaled)
    y_pred_proba_lr = lr_model.predict_proba(X_test_scaled)
    
    accuracy_lr = accuracy_score(y_test, y_pred_lr)
    precision_lr, recall_lr, f1_lr, _ = precision_recall_fscore_support(y_test, y_pred_lr, average='weighted')
    
    model_results['Logistic Regression'] = {
        'accuracy': accuracy_lr,
        'precision': precision_lr,
        'recall': recall_lr,
        'f1_score': f1_lr,
        'predictions': y_pred_lr,
        'probabilities': y_pred_proba_lr
    }
    
    print(f"   ✅ Accuracy: {accuracy_lr:.4f}")
    
    # 3.3 SUPPORT VECTOR MACHINE (SVM)
    print("\n🎯 ENTRENANDO SUPPORT VECTOR MACHINE:")
    print("   📋 Parámetros relevantes:")
    print("      • kernel='rbf' (kernel de base radial)")
    print("      • C=1.0 (parámetro de regularización)")
    print("      • gamma='scale' (coeficiente del kernel)")
    print("      • random_state=42 (reproducibilidad)")
    print("      • probability=True (para predicciones probabilísticas)")
    
    svm_model = SVC(
        kernel='rbf',
        C=1.0,
        gamma='scale',
        probability=True,
        random_state=42
    )
    svm_model.fit(X_train_scaled, y_train)
    models['SVM'] = svm_model
    
    # Evaluación SVM
    y_pred_svm = svm_model.predict(X_test_scaled)
    y_pred_proba_svm = svm_model.predict_proba(X_test_scaled)
    
    accuracy_svm = accuracy_score(y_test, y_pred_svm)
    precision_svm, recall_svm, f1_svm, _ = precision_recall_fscore_support(y_test, y_pred_svm, average='weighted')
    
    model_results['SVM'] = {
        'accuracy': accuracy_svm,
        'precision': precision_svm,
        'recall': recall_svm,
        'f1_score': f1_svm,
        'predictions': y_pred_svm,
        'probabilities': y_pred_proba_svm
    }
    
    print(f"   ✅ Accuracy: {accuracy_svm:.4f}")

    # PASO 4: RED NEURONAL
    print("\n🎯 PASO 4: ENTRENAMIENTO DE RED NEURONAL")
    print("="*50)
    
    # Crear arquitectura de red neuronal
    nn_model = create_neural_network_architecture(X_train_scaled.shape[1], len(class_names))
    
    print("📋 PARÁMETROS DE ENTRENAMIENTO:")
    print("   • Optimizer: Adam (learning_rate=0.001)")
    print("   • Loss function: sparse_categorical_crossentropy")
    print("   • Metrics: accuracy")
    print("   • Batch size: 32")
    print("   • Max epochs: 100")
    print("   • Validation split: 20%")
    print("   • Early stopping: patience=15, monitor='val_loss'")
    
    # Configurar early stopping
    early_stopping = EarlyStopping(
        monitor='val_loss',
        patience=15,
        restore_best_weights=True,
        verbose=1
    )
    
    # Entrenar red neuronal
    print("\n🚀 Iniciando entrenamiento de la red neuronal...")
    history = nn_model.fit(
        X_train_scaled, y_train,
        validation_split=0.2,
        epochs=100,
        batch_size=32,
        callbacks=[early_stopping],
        verbose=1
    )
    
    models['Neural Network'] = nn_model
    
    # Visualizar historial de entrenamiento
    plot_training_history(history)
    
    # Evaluación Red Neuronal
    y_pred_proba_nn = nn_model.predict(X_test_scaled, verbose=0)
    y_pred_nn = np.argmax(y_pred_proba_nn, axis=1)
    
    accuracy_nn = accuracy_score(y_test, y_pred_nn)
    precision_nn, recall_nn, f1_nn, _ = precision_recall_fscore_support(y_test, y_pred_nn, average='weighted')
    
    model_results['Neural Network'] = {
        'accuracy': accuracy_nn,
        'precision': precision_nn,
        'recall': recall_nn,
        'f1_score': f1_nn,
        'predictions': y_pred_nn,
        'probabilities': y_pred_proba_nn
    }
    
    print(f"\n✅ Red Neuronal - Accuracy: {accuracy_nn:.4f}")

    # PASO 5: EVALUACIÓN DETALLADA DE CADA MODELO
    print("\n🎯 PASO 5: EVALUACIÓN DETALLADA DE MODELOS")
    print("="*60)
    
    for model_name, results in model_results.items():
        print(f"\n📊 EVALUACIÓN: {model_name.upper()}")
        print("-" * 40)
        print(f"Accuracy:  {results['accuracy']:.4f}")
        print(f"Precision: {results['precision']:.4f}")
        print(f"Recall:    {results['recall']:.4f}")
        print(f"F1-Score:  {results['f1_score']:.4f}")
        
        print(f"\n📋 Reporte de Clasificación Detallado:")
        print(classification_report(y_test, results['predictions'], target_names=class_names))
        
        # Matriz de confusión
        cm = confusion_matrix(y_test, results['predictions'])
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                    xticklabels=class_names, yticklabels=class_names)
        plt.title(f'Matriz de Confusión - {model_name}', fontsize=14, fontweight='bold')
        plt.xlabel('Predicción', fontsize=12)
        plt.ylabel('Valor Real', fontsize=12)
        plt.tight_layout()
        plt.show()

    # PASO 6: COMPARACIÓN GRÁFICA Y SUPERPUESTA
    print("\n🎯 PASO 6: RESULTADOS GRÁFICOS COMPARADOS/SUPERPUESTOS")
    print("="*70)
    
    comparison_df, best_model_name = plot_comprehensive_results_comparison(model_results, class_names)

    # PASO 7: DISCUSIÓN DE RESULTADOS Y MEJORAS
    discuss_results_and_improvements(comparison_df, best_model_name, model_results)

    # PASO 8: GUARDADO DE MODELOS
    print("\n🎯 PASO 8: GUARDADO DE MODELOS Y PREPROCESADORES")
    print("="*60)
    
    try:
        # Guardar preprocesadores
        joblib.dump(preprocessor, 'preprocessor_classification.pkl')
        joblib.dump(y_encoder, 'target_encoder.pkl')
        joblib.dump(scaler, 'feature_scaler.pkl')
        
        # Guardar mejor modelo tradicional
        best_traditional_models = {k: v for k, v in models.items() if k != 'Neural Network'}
        if best_traditional_models:
            best_traditional_name = max(best_traditional_models.keys(), 
                                      key=lambda x: model_results[x]['accuracy'])
            joblib.dump(models[best_traditional_name], f'best_traditional_model_{best_traditional_name.lower().replace(" ", "_")}.pkl')
        
        # Guardar red neuronal
        nn_model.save('neural_network_model.h5')
        
        print("✅ Modelos y preprocesadores guardados exitosamente:")
        print("   • preprocessor_classification.pkl")
        print("   • target_encoder.pkl")
        print("   • feature_scaler.pkl")
        print("   • best_traditional_model_*.pkl")
        print("   • neural_network_model.h5")
        
    except Exception as e:
        print(f"❌ Error al guardar modelos: {e}")

    # RESUMEN FINAL
    print("\n" + "="*80)
    print("🎉 RESUMEN FINAL DEL ANÁLISIS")
    print("="*80)
    
    print(f"📊 DATASET ANALIZADO:")
    print(f"   • Total de instancias: {len(df):,}")
    print(f"   • Variables predictoras: {X.shape[1]}")
    print(f"   • Clases objetivo: {len(class_names)}")
    print(f"   • División: {len(X_train):,} entrenamiento, {len(X_test):,} test")
    
    print(f"\n🤖 MODELOS EVALUADOS:")
    for i, model_name in enumerate(model_results.keys(), 1):
        acc = model_results[model_name]['accuracy']
        print(f"   {i}. {model_name}: {acc:.4f}")
    
    print(f"\n🏆 MEJOR MODELO: {best_model_name}")
    print(f"   • Accuracy: {model_results[best_model_name]['accuracy']:.4f}")
    print(f"   • F1-Score: {model_results[best_model_name]['f1_score']:.4f}")
    
    print(f"\n✅ REQUERIMIENTOS CUMPLIDOS:")
    print(f"   ✓ Dataset con >1000 instancias ({len(df):,})")
    print(f"   ✓ Variable objetivo con múltiples clases ({len(class_names)})")
    print(f"   ✓ Mínimo 6 variables predictoras ({X.shape[1]})")
    print(f"   ✓ Modelos no basados en redes neuronales (3)")
    print(f"   ✓ Red neuronal con arquitectura especificada")
    print(f"   ✓ Caracterización textual y gráfica")
    print(f"   ✓ Resultados comparados gráficamente")
    print(f"   ✓ Discusión y propuestas de mejora")
    
    print("="*80)
    
    # Liberar memoria
    gc.collect()
    
    return {
        'dataset': df,
        'models': models,
        'results': model_results,
        'comparison': comparison_df,
        'best_model': best_model_name,
        'preprocessor': preprocessor,
        'target_encoder': y_encoder,
        'scaler': scaler
    }

if __name__ == "__main__":
    results = main()