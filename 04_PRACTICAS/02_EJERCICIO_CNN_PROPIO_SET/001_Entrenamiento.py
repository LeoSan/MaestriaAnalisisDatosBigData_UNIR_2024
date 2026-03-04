import tensorflow as tf
import os
import matplotlib.pyplot as plt

# =====================================================================
# FASE 1: SE SELECCIONO LOS DOCUMENTOS SEPARANDOLOS EN DOS DIRECTORIOS 
# =====================================================================

# =====================================================================
# FASE 2: LA RECETA DE PREPARACIÓN DE DATOS A COLOR
# =====================================================================

# -> PASO ATÓMICO 1: Definir Variables Constantes
DIRECTORIO_DATASET = 'dataset'
TAMANIO_IMAGEN = (128, 128) # Redimensionar TODAS las fotos a este estándar
TAMANIO_LOTE = 8 # Agrupar de 8 en 8 para no saturar memoria RAM

print("📷 Iniciando Receta de Datos...\n")

# -> PASO ATÓMICO 2: Cargar y Dividir el Dataset (80% / 20%)
print("-> Reservando 80% para estudiar (Training):")
dataset_entrenamiento = tf.keras.utils.image_dataset_from_directory(
    DIRECTORIO_DATASET,
    validation_split=0.2, # Apartamos el 20% para examen sorpresa
    subset="training",
    seed=123, # Semilla aleatoria para siempre mezclar igual
    image_size=TAMANIO_IMAGEN,
    batch_size=TAMANIO_LOTE
)

print("\n-> Reservando 20% para el examen final (Validation):")
dataset_validacion = tf.keras.utils.image_dataset_from_directory(
    DIRECTORIO_DATASET,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=TAMANIO_IMAGEN,
    batch_size=TAMANIO_LOTE
)

# -> PASO ATÓMICO 3: Identificar Clases Categóricas
nombres_clases = dataset_entrenamiento.class_names
print(f"\n✅ Clases inferidas por las carpetas: {nombres_clases}")

# -> PASO ATÓMICO 4: Normalización de Píxeles (Escala 0.0 a 1.0)
print("\n⚙️ Normalizando píxeles (dividiendo RGB entre 255)...")
capa_normalizacion = tf.keras.layers.Rescaling(1./255)

dataset_entrenamiento = dataset_entrenamiento.map(lambda x, y: (capa_normalizacion(x), y))
dataset_validacion = dataset_validacion.map(lambda x, y: (capa_normalizacion(x), y))

# -> PASO ATÓMICO 5: Optimización de Hardware (Uso de Caché en RAM)
AUTOTUNE = tf.data.AUTOTUNE
dataset_entrenamiento = dataset_entrenamiento.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
dataset_validacion = dataset_validacion.cache().prefetch(buffer_size=AUTOTUNE)

print("🚀 ¡La Receta está completa! Las imágenes están listas matemáticamente.")

# =====================================================================
# AUDITORÍA VISUAL (El "Top" de lo que vamos a entrenar)
# =====================================================================
print("\n📊 Paso 3: Abriendo ventana para visualizar un 'Top' de las imágenes cargadas...")

plt.figure(figsize=(10, 10))
# Tomamos solo el primer lote
for imagenes, etiquetas in dataset_entrenamiento.take(1):
    # Validamos cuántas fotos trajo realmente este lote (por si es menor a 8)
    cantidad_real = imagenes.shape[0]
    for i in range(min(8, cantidad_real)):
        ax = plt.subplot(3, 3, i + 1)
        # Las imágenes ya están normalizadas, pyplot las dibuja directamente
        plt.imshow(imagenes[i].numpy())
        # Buscamos el nombre del folder original
        nombre_real = nombres_clases[int(etiquetas[i])]
        plt.title(nombre_real)
        plt.axis("off")

plt.show()


# =====================================================================
# FASE 3: CONSTRUIR LA ARQUITECTURA DE LA CNN
# =====================================================================

# Usamos un modelo Secuencial, que es simplemente apilar las capas una tras otra.
modelo = tf.keras.models.Sequential([
    # Especificamos explícitamente la capa de Entrada (esto evita el warning en versiones nuevas de Keras)
    tf.keras.Input(shape=(128, 128, 3)),
    
    # -- 1. EXTRAER CARACTERÍSTICAS --
    # Capa de Convolución: 32 filtros diferentes, cada uno de 3x3 píxeles. 
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    # Capa de Pooling: Reduce todo a la mitad (se queda con lo más fuerte de áreas 2x2)
    tf.keras.layers.MaxPooling2D(2, 2),
    
    # Segunda ronda: buscar patrones más complejos.
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    
    # Tercera ronda: buscar patrones más complejos.
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),

    # -- 2. TOMAR LA DECISIÓN --
    # Aplastar toda esa información a 1 dimensión
    tf.keras.layers.Flatten(),
    
    # Capa de pensamiento profundo (128 neuronas)
   # tf.keras.layers.Dense(128, activation='relu'),
    
    # # ¡NUEVA DEFENSA CONTRA OVERFITTING!
    # # "Apagamos" aleatoriamente el 50% de las neuronas en cada paso de estudio
    # # para forzar a la red a no memorizar el dataset
    # tf.keras.layers.Dropout(0.5),
    
    # # Capa de salida: 1 neurona (es 3 o no lo es). 
     tf.keras.layers.Dense(1, activation='sigmoid')
])

print("Resumen del modelo: ")
print(modelo.summary())

# Compilar: Definir las "reglas del juego" de cómo va a aprender la red
modelo.compile(
    optimizer='adam', # El algoritmo que ajusta los pesos mágicamente para aprender rápido (es el mejor para empezar)
    loss='binary_crossentropy', # La función matemática que mide "qué tan equivocada" está la red (usamos binary por ser prob binario)
    metrics=['accuracy'] # Queremos que nos muestre el porcentaje de "Precisión" (imágenes correctas)
)

print("\n--- INICIANDO EL ENTRENAMIENTO ---")
# Entrenar (Fit = Ajustar): Le pasamos el dataset (que ya contiene las imágenes y las etiquetas).
historial = modelo.fit(
    dataset_entrenamiento, # Nuestro dataset de estudio
    epochs=15, # Subimos a 15 para analizar el 'Sobreajuste' (Overfitting)
    validation_data=dataset_validacion # Nuestro examen sorpresa
)
print("--- ENTRENAMIENTO FINALIZADO ---")

print("\n--- EVALUANDO EL MODELO EN EL EXAMEN SORPRESA ---")
# Esto es hacer el examen final con las fotos del 20% que el modelo no ha visto en entrenamiento
perdida, precision = modelo.evaluate(dataset_validacion)
print(f"📊 Precisión Final (Accuracy) en imágenes nuevas: {precision*100:.2f}%")

# Guardar el modelo para no tener que entrenarlo de nuevo cada vez que queramos usarlo
modelo.save("modelo_oficina.keras")
print("✅ ¡Modelo guardado como 'modelo_oficina.keras'!")
