import tensorflow as tf
import os
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models


# =====================================================================
# FASE 1: SE SELECCIONO LOS DOCUMENTOS SEPARANDOLOS EN 4 DIRECTORIOS YA QUE SON 4 CALSES  
# =====================================================================

print("📷 Se busco las imagenes de los semafotos en la carpeta dataset...\n")

# =====================================================================
# FASE 2: INICIAMOS FASE DOS DEFINIMOS EL DIRECTORIO DONDE TOMARA LAS IMAGENES O DATASET
# =====================================================================
print("📷 INICIAMOS FASE DOS DEFINIMOS EL DIRECTORIO DONDE TOMARA LAS IMAGENES O DATASET ...\n")
# -> FASE 2.1: Definir Variables Constantes
DIRECTORIO_DATASET = 'dataset'
TAMANIO_IMAGEN = (128, 128) # Redimensionar TODAS las fotos a este estándar
TAMANIO_LOTE = 4 # Agrupar de 4 en 4 para no saturar memoria RAM

# -> FASE 2.2: Cargar y Dividir el Dataset (80% / 20%)
print("🏋️‍♀️-> Reservando 80% para estudiar (Training):")
dataset_entrenamiento = tf.keras.utils.image_dataset_from_directory(
    DIRECTORIO_DATASET,
    validation_split=0.2, # Apartamos el 20% para examen sorpresa
    subset="training",
    seed=123, # Semilla aleatoria para siempre mezclar igual
    image_size=TAMANIO_IMAGEN,
    batch_size=TAMANIO_LOTE,
    label_mode='categorical' #Esto es lo que activará el "One-Hot Encoding"
)

print("\n 🏋️‍♀️-> Reservando 20% para el examen final (Validation):")
dataset_validacion = tf.keras.utils.image_dataset_from_directory(
    DIRECTORIO_DATASET,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=TAMANIO_IMAGEN,
    batch_size=TAMANIO_LOTE,
    label_mode='categorical'
)


# -> FASE 2.3: Identificar Clases Categóricas
nombres_clases = dataset_entrenamiento.class_names
print(f"\n🏋️‍♀️ Clases inferidas por las carpetas: {nombres_clases}")

# -> FASE 2.4: Normalización de Píxeles (Escala 0.0 a 1.0)
print("\n⚙️ Normalizando píxeles (dividiendo RGB entre 255)...")
capa_normalizacion = tf.keras.layers.Rescaling(1./255)

# -> FASE 2.5: Optimización de Hardware (Uso de Caché en RAM)
AUTOTUNE = tf.data.AUTOTUNE
dataset_entrenamiento = dataset_entrenamiento.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
dataset_validacion = dataset_validacion.cache().prefetch(buffer_size=AUTOTUNE)

print("🚀 ¡La Receta está completa! Las imágenes están listas matemáticamente.")

# -> FASE 2.6: Auditoría Visual (El "Top" de lo que vamos a entrenar)
print("\n📊 Paso 3: Abriendo ventana para visualizar un 'Top' de las imágenes cargadas...")

plt.figure(figsize=(10, 10))
# Tomamos solo el primer lote
for imagenes, etiquetas in dataset_entrenamiento.take(1):
    # Validamos cuántas fotos trajo realmente este lote (por si es menor a 4)
    cantidad_real = imagenes.shape[0]
    for i in range(min(4, cantidad_real)):
        ax = plt.subplot(3, 3, i + 1)
        # Convertimos los píxeles a enteros (0-255) para que imshow no se queje
        plt.imshow(imagenes[i].numpy().astype("uint8"))
        # Como usamos 'categorical', la etiqueta es un arreglo One-Hot (ej. [0, 1, 0, 0])
        # Usamos tf.argmax para sacar la posición del '1' (que es el índice de la clase)
        indice_clase = int(tf.argmax(etiquetas[i]).numpy())
        nombre_real = nombres_clases[indice_clase]
        plt.title(nombre_real)
        plt.axis("off")

plt.show()#Me imprime una ventana y valido si esta bien las coincidencias 

# =====================================================================
# FASE 3: CONSTRUIR LA ARQUITECTURA DE LA CNN
# =====================================================================

print("\n🧠 Construyendo el 'cerebro' (Modelo CNN)...")

modelo = models.Sequential([

    layers.RandomFlip("horizontal", input_shape=(TAMANIO_IMAGEN[0], TAMANIO_IMAGEN[1], 3)), ## Nos permite modificar la misma imagen en varios angulos para evitar la momoria y realizar un aprensizaje mas profundo 
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),

    # Bloque 1: Extraer formas y colores basicos 
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(TAMANIO_IMAGEN[0], TAMANIO_IMAGEN[1], 3)),
    layers.MaxPooling2D(2, 2),

    # Bloque 2: Reconocer patrones mas complejos 
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),

    # Aplanar el mapa espacial a un vctor 1D ## Primer Aplanado
    layers.Flatten(),

    # Capa Oculta de Razonamiento
    layers.Dense(128, activation='relu'),
    
    # Capa de Salida: Neuronas = Número de Clases
    layers.Dense(len(nombres_clases), activation='softmax')

])
       
print("\n🧠 'cerebro' counstuido con 4 neuronas (Modelo CNN)...")
print("Resumen del modelo: ")
print(modelo.summary())


print("\n🧠 'Iniciamos Optimizacion' Usando ADAM y Categorical Crossentropy")
modelo.compile(
    optimizer='adam',# Optimizador Adam, SGD, RMSprop, adagrad 
    loss='categorical_crossentropy',#Me permite evaluar las perdidas de las categorias 
    metrics=['accuracy']#Me indica el promedio exacto de aciertos 
)   

print("\n🧠 'Iniciamos entrenamiento' con 15 epocas")
historial = modelo.fit(
    dataset_entrenamiento,
    epochs=10,
    validation_data=dataset_validacion
)
print("\n--- ENTRENAMIENTO FINALIZADO ---")

print("\n--- EVALUANDO EL MODELO EN EL EXAMEN SORPRES A ---")
perdida, precision = modelo.evaluate(dataset_validacion)
print(f"📊 Precisión Final (Accuracy) en imágenes nuevas: {precision*100:.2f}%")

print("\n💾 Guardando el modelo para usarlo en la app de Gradio...")
modelo.save('modelo_semaforos.keras')
print("✅ ¡Modelo guardado exitosamente como 'modelo_semaforos.keras'!")

