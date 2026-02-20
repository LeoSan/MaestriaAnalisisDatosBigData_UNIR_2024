import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

## CARGA DE DATA 
# Ya tenemos los datos (Paso 1 y 2) y tenemos el cerebro construido (Paso 3). 

# Se enumeran pasos para mejor comprensión 
# 1. Cargar el conjunto de datos MNIST
# Usaremos una data para este tipo de ejercicios del tipo de red neuronal que vamos a crear
mnist = tf.keras.datasets.mnist
(x_entrenamiento_completo, y_entrenamiento_completo), (x_prueba_completo, y_prueba_completo) = mnist.load_data()

# 2. Simplificar nuestro problema: "Es un 3" (True/1) vs "No es un 3" (False/0)
# Convertimos las etiquetas originales (0 al 9) en booleanos (True si es 3, False en caso contrario)
# Luego los convertimos a enteros (1 y 0) para que la red neuronal los entienda mejor.
y_entrenamiento_binario = (y_entrenamiento_completo == 3).astype(int)
y_prueba_binario = (y_prueba_completo == 3).astype(int)

# 3. Mostrar un ejemplo para comprobar qué tenemos (Pruebas de Nuestra Data)
indice_ejemplo = 10 # Puedes cambiar este número para ver otras imágenes
etiqueta_original = y_entrenamiento_completo[indice_ejemplo]
es_un_tres = y_entrenamiento_binario[indice_ejemplo]
# plt.imshow(x_entrenamiento_completo[indice_ejemplo], cmap='gray')
# plt.title(f"Etiqueta Original: {etiqueta_original} | ¿Es un 3?: {bool(es_un_tres)}")
# plt.axis('off')
# plt.show()

## NORMALIZACIÓN:  HASTA aqui nada nuevo solo tomanos la data que ya esta en binario y validamos si esta correcta 

# 4. Normalización: Escalar los valores de los píxeles de 0-255 a 0.0-1.0, como estamos validando imagenes debemos scalar los valores en pixeles 
x_entrenamiento = x_entrenamiento_completo / 255.0
x_prueba = x_prueba_completo / 255.0
print(f"Valor máximo de un píxel antes: {x_entrenamiento_completo.max()}")
print(f"Valor máximo de un píxel ahora: {x_entrenamiento.max()}")

# 5. Reshape (Redimensionar): Añadir la dimensión del canal de color
# MNIST viene como una lista de 60000 matrices de 28x28. 
# Las CNN de TensorFlow esperan el formato (cantidad_imagenes, alto, ancho, canales)
x_entrenamiento = x_entrenamiento.reshape(-1, 28, 28, 1)
x_prueba = x_prueba.reshape(-1, 28, 28, 1)
print(f"Nueva forma matemática de los datos de entrenamiento: {x_entrenamiento.shape}")


##ARQUITECTURA: Este bloque solo construirá el diseño (la arquitectura). 


# 6. Construir la Arquitectura de la CNN
# Usamos un modelo Secuencial, que es simplemente apilar las capas una tras otra.
modelo = tf.keras.models.Sequential([
    # Especificamos explícitamente la capa de Entrada (esto evita el warning en versiones nuevas de Keras)
    tf.keras.Input(shape=(28, 28, 1)),
    
    # -- 1. EXTRAER CARACTERÍSTICAS --
    # Capa de Convolución: 32 filtros diferentes, cada uno de 3x3 píxeles. 
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    # Capa de Pooling: Reduce todo a la mitad (se queda con lo más fuerte de áreas 2x2)
    tf.keras.layers.MaxPooling2D(2, 2),
    
    # Segunda ronda: buscar patrones más complejos.
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    
    # -- 2. TOMAR LA DECISIÓN --
    # Aplastar toda esa información a 1 dimensión
    tf.keras.layers.Flatten(),
    
    # Capa de pensamiento profundo (128 neuronas)
    tf.keras.layers.Dense(128, activation='relu'),
    
    # Capa de salida: 1 neurona (es 3 o no lo es). 
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Mostrar un resumen de cómo quedó nuestro modelo construido
# modelo.summary()  # Lo comentamos para que no ensucie tanto la consola en las siguientes ejecuciones

# --- PASO 4: COMPILAR Y ENTRENAR EL MODELO ---

# 4.1 Compilar: Definir las "reglas del juego" de cómo va a aprender la red
modelo.compile(
    optimizer='adam', # El algoritmo que ajusta los pesos mágicamente para aprender rápido (es el mejor para empezar)
    loss='binary_crossentropy', # La función matemática que mide "qué tan equivocada" está la red (usamos binary por ser prob binario)
    metrics=['accuracy'] # Queremos que nos muestre el porcentaje de "Precisión" (imágenes correctas)
)

print("\n--- INICIANDO EL ENTRENAMIENTO ---")
# 4.2 Entrenar (Fit = Ajustar): Le pasamos los datos y las respuestas para que aprenda.
historial = modelo.fit(
    x_entrenamiento, y_entrenamiento_binario, # Datos de estudio y respuestas de estudio
    epochs=5, # ¿Cuántas vueltas completas al libro de estudio le dará? (Vamos a empezar con 5 repasos completos)
    validation_data=(x_prueba, y_prueba_binario) # Examen rápido al final de cada vuelta para ver si realmente aprende o solo memoriza
)
print("--- ENTRENAMIENTO FINALIZADO ---")

# --- PASO 5: EVALUAR EL MODELO Y HACER PREDICCIONES ---

# Vamos a escoger una imagen al azar del "examen final" (x_prueba) que la red NUNCA ha visto durante el entrenamiento.
indice_prueba = 18 # Puedes cambiar este número para probar con diferentes imágenes
imagen_a_predecir = x_prueba[indice_prueba]
etiqueta_real_binaria = y_prueba_binario[indice_prueba]
etiqueta_real_original = y_prueba_completo[indice_prueba]

# IMPORTANTE: Keras siempre espera recibir paquetes (lotes) de imágenes, no una sola.
# Tenemos que convertir nuestra imagen de forma (28, 28, 1) a (1, 28, 28, 1)
imagen_como_lote = np.expand_dims(imagen_a_predecir, axis=0)

# ¡La hora de la verdad! Le pedimos al modelo que prediga
prediccion_probabilidad = modelo.predict(imagen_como_lote)[0][0]

# Convertimos esa probabilidad a una respuesta humana (Sí o No)
es_un_tres_prediccion = prediccion_probabilidad > 0.5 

print("\n--- RESULTADOS DE LA PREDICCIÓN ---")
print(f"Probabilidad calculada por la Red Neuronal: {prediccion_probabilidad:.4f} ({(prediccion_probabilidad*100):.2f}%)")
print(f"La Red Neuronal dice que ¿Es un 3?: {es_un_tres_prediccion}")
print(f"La verdad absoluta (Etiqueta Original): Era un número {etiqueta_real_original} (Es 3: {bool(etiqueta_real_binaria)})")

# Dibujemos la imagen para ver si la red tuvo razón
plt.imshow(imagen_a_predecir.reshape(28, 28), cmap='gray')
color_titulo = 'green' if es_un_tres_prediccion == bool(etiqueta_real_binaria) else 'red'
plt.title(f"Predicción red: {es_un_tres_prediccion} | Verdad: {bool(etiqueta_real_binaria)}", color=color_titulo)
plt.axis('off')
plt.show()


# --- PASO 6: GUARDAR EL MODELO PARA USARLO EN EL FUTURO ---
# Guardamos toooooodo lo aprendido (pesos y arquitectura) en un archivo.
modelo.save('mi_cerebro_reconoce_tres.keras')
print("¡Cerebro artificial guardado con éxito!")