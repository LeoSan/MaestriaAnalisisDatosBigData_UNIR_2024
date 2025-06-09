import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


#Importación del dataset De Vehiculos
print("\n🎯 Paso 0: ----------------- Importamos el DataSet Vehiculos :------------------ 🎯")
url_descarga_directa = 'https://drive.google.com/uc?export=download&id=1jY1JAwakImo53OxBA0oiJTlAH9G5vi3d'
df = pd.read_csv(url_descarga_directa, sep=';')

#Caracterización del dataset
print("\n📋 Primeras 5 filas del dataset:")
print(df.head())

print("\n📋 INFORMACIÓN DETALLADA:")
print(df.info())

## Preprocesamiento de Datos
print("\n🎯 Paso 1: ------------ Preprocesamiento de Datos ------------------------ 🎯")
df_encoded = df.copy()
#print("\n🎯 DISTRIBUCIÓN DE LA VARIABLE OBJETIVO (class):")
# Columnas a codificar
# 'class' es la columna objetivo

features = ['Buying', 'Maintenance', 'Doors', 'Person', 'lug_boot', 'safety']
target = 'class'

# Aplicamos LabelEncoder a cada columna categórica, incluyendo la columna objetivo
for col in features + [target]:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df_encoded[col])
    print(f" 🔍 Mapeo de {col}: {dict(zip(le.classes_, le.transform(le.classes_)))}")

print("\n 📋 Primeras 5 filas del dataset codificado:")
print(df_encoded.head())

#Caracterización del Dataset
print("\n🎯 Paso 2: ------------ Caracterización del Dataset ------------------------ 🎯")

print(f"\n 📋 Número total de instancias: {df_encoded.shape[0]}")
print(f"\n 📋 Número de atributos de entrada: {df_encoded.shape[1] - 1}") # Excluyendo la columna 'class'
print(f"\n 📋 Dataset Vehiculos con {df_encoded.shape[0]} filas y {df_encoded.shape[1]} columnas")
print("\n 📋 Descripción de atributos de entrada y su tipo:")

columan_desc = {"Buying":"Precio de compra del vehículo, clasificado en categorías como vhigh (muy alto), high (alto), med (medio) y low (bajo)."
                , "Maintenance":"Costo de mantenimiento del vehículo, con la misma categorización que buying."
                , "Doors":"Número de puertas del automóvil, expresado en valores numéricos como '2', '3', '4', o '5more' (5 o más)."
                , "Person":"Capacidad de ocupantes del automóvil, con valores como '2', '4' y 'more (más de 4)."
                , "lug_boot":"Tamaño del maletero, categorizado como small (pequeño), med (medio) o big (grande)"
                , "safety":"Nivel de seguridad del automóvil, clasificado como low (bajo), med (medio) o high (alto)"}

for col in features:
    print(f" 🔍 Atributo: {col}, Descripción: [{columan_desc[col]}], Tipo: [categórico]") # Agrega el significado real
    print(f" Valores únicos (antes de codificar): {df[col].unique()}")
    
print("\n 📋 Información de la clase objetivo:")
print(f"\n - Columna de clase: '{target}'")
print(f"\n - Número de clases: {df_encoded[target].nunique()}")

print("\n 📋 Representación de las clases y su conteo:")
print(df[target].value_counts()) # Mostrar conteo de valores originales antes de codificar para mayor claridad
print(f"\n 📋 Porcentajes:")
print((df[target].value_counts() / len(df) * 100).round(2))

print(f"\n 📋 Tipo de valor de la clase (después de codificación): {df_encoded[target].dtype}")
#print(f"\n 📋 Memoria utilizada: {df_encoded.memory_usage(deep=True).sum()} bytes")

# Verificar valores desconocidos (nulos)
print("\n 📋 Valores nulos por columna:")
print(df_encoded.isnull().sum())

print("\n 📋 ESTADÍSTICAS DESCRIPTIVAS:")
print(df_encoded.describe(include='all'))

##Descripción Gráfica datos Originales
print("\n🎯 Paso 3: ------------ Descripción Gráfica datos originales------------------------ 🎯")
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(15, 10))

# Histograma de la distribución de las clases
plt.subplot(2, 2, 1)
sns.countplot(x=target, data=df)
plt.title('Distribución de la Clase de Aceptabilidad de Coches')
plt.xlabel('Clase (original)')
plt.ylabel('Conteo')

# Histograma de algunas características de entrada (después de codificación)
plt.subplot(2, 2, 2)
sns.countplot(x='Buying', data=df) # O df_encoded si prefieres los valores numéricos
plt.title('Distribución de Costo de Compra')

plt.subplot(2, 2, 3)
sns.countplot(x='Doors', data=df)
plt.title('Distribución de Número de Puertas')

plt.tight_layout()
plt.show()

## Entrenamiento y Evaluación de Modelos
print("\n🎯 Paso 4: ------------ Procesasamiento del dataset Transformaciones previas necesarias para la modelación------------------------ 🎯")
## División del Dataset en Entrenamiento y Prueba
# Definimos las características de entrada (X) y la variable objetivo (y)   
X = df_encoded[features]
y = df_encoded[target]
# Divido el dataset en conjuntos de entrenamiento y prueba
# utilizo una proporción de 70-30% o 80-20%
# Aseguramos que la división mantenga la proporción de clases utilizando stratify=y
# stratify=y es importante para mantener la misma proporción de clases en los conjuntos de entrenamiento y prueba

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.3,      # 30% para prueba
    random_state=42,    # Para reproducibilidad
    stratify=y          # Mantener proporción de clases
)
print("\n 📋 Divido el dataset en conjuntos de entrenamiento y prueba. Una proporción común es 70-30% o 80-20% ")
print(f"\n ✅ Dimensiones de X_train: {X_train.shape}")
print(f"\n ✅ Dimensiones de X_test: {X_test.shape}")

## Selección y Entrenamiento de Modelos
print("\n 📋 Selección y Entrenamiento de Modelos ")
print("\n 📋 Decision Tree Classifier ")

from sklearn.tree import DecisionTreeClassifier

dt_model = DecisionTreeClassifier(
    random_state=42,
    max_depth=5,           # Profundidad máxima
    min_samples_split=4,   # Mínimo de muestras para dividir
    min_samples_leaf=2     # Mínimo de muestras en hoja
)
dt_model.fit(X_train, y_train)
y_pred_dt = dt_model.predict(X_test)

##Random Forest Classifier:
print("\n 📋 Random Forest Classifier: ")

from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(
    n_estimators=100
    , random_state=42
)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

## Entrenamiento y Evaluación de Modelos
print("\n🎯 Paso 5: ------------ Entrenamiento y Evaluación de Modelos------------------------ 🎯")
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay 

print("\n 🧠 ------- Métricas de Clasificación -------")
print("\n 🧠 Evaluación del Modelo Decision Tree ---")
print(f"\n 🧠 Accuracy Decision Tree: {accuracy_score(y_test, y_pred_dt):.4f}")
print("\n 🧠 Matriz de Confusión Decision Tree:")
print(confusion_matrix(y_test, y_pred_dt))
print("\n 🧠 Reporte de Clasificación Decision Tree:")
print(classification_report(y_test, y_pred_dt, target_names=[str(cls) for cls in le.inverse_transform(sorted(y.unique()))]))

print("\n 🧠 Evaluación del Modelo Random Forest ---")
print(f"\n 🧠 Accuracy Random Forest: {accuracy_score(y_test, y_pred_rf):.4f}")
print("\n 🧠 Matriz de Confusión Random Forest:")
print(confusion_matrix(y_test, y_pred_rf))
print("\n 🧠 Reporte de Clasificación Random Forest:")
print(classification_report(y_test, y_pred_rf, target_names=[str(cls) for cls in le.inverse_transform(sorted(y.unique()))]))

## Evaluación y Comparación de Resultados
print("\n🎯 Paso 6: ------------  Evaluación y Comparación de Resultados ------------------------ 🎯")

print("\n 📈 -------Comparación Gráfica de Resultados: -------")
   
# Ejemplo de comparación de accuracy
models = ['Decision Tree', 'Random Forest']
accuracies = [accuracy_score(y_test, y_pred_dt), accuracy_score(y_test, y_pred_rf)]

plt.figure(figsize=(8, 5))
sns.barplot(x=models, y=accuracies)
plt.title('Comparación de Accuracy entre Modelos')
plt.ylabel('Accuracy')
plt.ylim(0, 1)
plt.show()

# Visualización de matrices de confusión
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.heatmap(confusion_matrix(y_test, y_pred_dt), annot=True, fmt='d', cmap='Blues', ax=axes[0])
axes[0].set_title('Matriz de Confusión: Decision Tree')
axes[0].set_xlabel('Predicho')
axes[0].set_ylabel('Real')

sns.heatmap(confusion_matrix(y_test, y_pred_rf), annot=True, fmt='d', cmap='Blues', ax=axes[1])
axes[1].set_title('Matriz de Confusión: Random Forest')
axes[1].set_xlabel('Predicho')
axes[1].set_ylabel('Real')

plt.tight_layout()
plt.show()

# --- Para el Modelo Decision Tree ---
print("\n 📈 --- Métricas del Modelo Decision Tree ---")

# 1. Instancias clasificadas correctamente e incorrectamente
correct_dt = accuracy_score(y_test, y_pred_dt) * len(y_test)
incorrect_dt = len(y_test) - correct_dt

print(f"\n 🧠 Instancias clasificadas correctamente (Decision Tree): {int(correct_dt)}")
print(f"\n 🧠 Instancias clasificadas incorrectamente (Decision Tree): {int(incorrect_dt)}")

# 2. Matriz de Confusión
cm_dt = confusion_matrix(y_test, y_pred_dt)

print("\n Matriz de Confusión (Decision Tree):")
print(cm_dt)

# Visualizar la Matriz de Confusión
disp_dt = ConfusionMatrixDisplay(confusion_matrix=cm_dt, display_labels=le.inverse_transform(sorted(y.unique()))) # Usa las etiquetas originales
disp_dt.plot(cmap=plt.cm.Blues)
plt.title('Matriz de Confusión: Decision Tree')
plt.show()

# 3. TP Rate y FP Rate (usando classification_report o calculándolos manualmente desde la CM)
# El classification_report te da Precision, Recall (TP Rate), F1-Score y Support
report_dt = classification_report(y_test, y_pred_dt, output_dict=True, target_names=le.inverse_transform(sorted(y.unique())))

print("\n Reporte de Clasificación (Decision Tree):")
for class_label, metrics in report_dt.items():
    if class_label in le.inverse_transform(sorted(y.unique())): # Solo para las clases reales
        recall = metrics['recall'] # TP Rate
        # Para FP Rate, es un poco más complejo y depende de si es binario o multiclase
        # FP = Suma de la columna - True Positives para esa clase
        # TN = Suma de las filas y columnas excepto la fila y columna de esa clase
        # FP Rate = FP / (FP + TN)

        print(f"Clase '{class_label}':")
        print(f"  TP Rate (Recall): {recall:.4f}")
        # Para FP Rate por clase:
        # True Negatives (TN) for a class 'i': sum of all cells NOT in row 'i' AND NOT in column 'i'
        # False Positives (FP) for a class 'i': sum of column 'i' cells MINUS True Positives of class 'i'
        TP_dt = cm_dt[le.transform([class_label])[0], le.transform([class_label])[0]] # True Positive for this class
        FN_dt = np.sum(cm_dt[le.transform([class_label])[0], :]) - TP_dt # False Negatives for this class
        FP_dt = np.sum(cm_dt[:, le.transform([class_label])[0]]) - TP_dt # False Positives for this class
        TN_dt = np.sum(cm_dt) - (TP_dt + FN_dt + FP_dt) # True Negatives for this class

        # Manejar la división por cero si FP + TN es 0
        fp_rate_dt = FP_dt / (FP_dt + TN_dt) if (FP_dt + TN_dt) > 0 else 0
        print(f"  FP Rate: {fp_rate_dt:.4f}")
        print("-" * 20)

print("\n")

# --- Para el Modelo Random Forest ---
print("\n 🧠 Métricas del Modelo Random Forest ---")

# 1. Instancias clasificadas correctamente e incorrectamente
correct_rf = accuracy_score(y_test, y_pred_rf) * len(y_test)
incorrect_rf = len(y_test) - correct_rf

print(f"\n 🧠Instancias clasificadas correctamente (Random Forest): {int(correct_rf)}")
print(f"\n 🧠Instancias clasificadas incorrectamente (Random Forest): {int(incorrect_rf)}")

# 2. Matriz de Confusión
cm_rf = confusion_matrix(y_test, y_pred_rf)
print("\n 🧠 Matriz de Confusión (Random Forest):")
print(cm_rf)

# Visualizar la Matriz de Confusión
disp_rf = ConfusionMatrixDisplay(confusion_matrix=cm_rf, display_labels=le.inverse_transform(sorted(y.unique())))
disp_rf.plot(cmap=plt.cm.Blues)
plt.title('Matriz de Confusión: Random Forest')
plt.show()

# 3. TP Rate y FP Rate
report_rf = classification_report(y_test, y_pred_rf, output_dict=True, target_names=le.inverse_transform(sorted(y.unique())))

print("\n 🧠 Reporte de Clasificación (Random Forest):")
for class_label, metrics in report_rf.items():
    if class_label in le.inverse_transform(sorted(y.unique())):
        recall = metrics['recall'] # TP Rate

        print(f"Clase '{class_label}':")
        print(f"  TP Rate (Recall): {recall:.4f}")

        # Para FP Rate por clase:
        TP_rf = cm_rf[le.transform([class_label])[0], le.transform([class_label])[0]]
        FN_rf = np.sum(cm_rf[le.transform([class_label])[0], :]) - TP_rf
        FP_rf = np.sum(cm_rf[:, le.transform([class_label])[0]]) - TP_rf
        TN_rf = np.sum(cm_rf) - (TP_rf + FN_rf + FP_rf)

        fp_rate_rf = FP_rf / (FP_rf + TN_rf) if (FP_rf + TN_rf) > 0 else 0
        print(f"  FP Rate: {fp_rate_rf:.4f}")
        print("-" * 20)