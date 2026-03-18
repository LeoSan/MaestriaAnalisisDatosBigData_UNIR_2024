import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image
# 1. Cargar el modelo que acabamos de entrenar
print("Cargando el cerebro artificial...")
modelo = tf.keras.models.load_model('modelo_semaforos.keras')
print("¡Modelo cargado!")
# Nombres de las clases en el MISMO ORDEN que nos dio tf.dataset (alfabético por defecto)
clases = ['amarillo', 'apagado', 'rojo', 'verde']
def predecir_semaforo(imagen_pil):
    # Gradio nos manda una imagen PIL. La redimensionamos a 128x128 (lo que usaste en Fase 2)
    imagen = imagen_pil.resize((128, 128))
    
    # Convertimos a arreglo matemático
    img_array = tf.keras.preprocessing.image.img_to_array(imagen)
    
    # ⚠️ IMPORTANTE: Normalizamos los píxeles (igual que en Fase 2.4)
    img_array = img_array / 255.0
    
    # Añadimos la dimensión del "lote" (batch) porque el modelo espera (lote, alto, ancho, canales)
    img_array = tf.expand_dims(img_array, 0)
    
    # Hacemos la predicción
    predicciones = modelo.predict(img_array)[0] # Tomamos el primer y único resultado
    
    # Las predicciones son las 4 probabilidades Softmax (ej. [0.1, 0.05, 0.8, 0.05])
    # ⚠️ TU RETO FINAL: Empaquetar esto en un diccionario para Gradio
    # Gradio espera un dict donde la clave es el nombre y el valor es la probabilidad (float)
    resultado = {clases[i]: float(predicciones[i]) for i in range(len(clases))}
    
    return resultado
# 3. Construir la Interfaz Visual Web
interfaz = gr.Interface(
    fn=predecir_semaforo, 
    inputs=gr.Image(label="Sube la foto del Semáforo", type="pil"),
    outputs=gr.Label(label="¿Qué color es?", num_top_classes=4),
    title="🚦 Clasificador Multiclase de Semáforos",
    description="Sube una foto de un semáforo (Rojo, Amarillo, Verde o Apagado) y la IA te dirá qué estado tiene."
)
# ¡Lanzar el servidor web local!
interfaz.launch()