import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps
import gradio as gr
import os

MODEL_FILENAME = 'mi_cerebro_reconoce_tres.keras'

# Intentar cargar el modelo al iniciar
try:
    if os.path.exists(MODEL_FILENAME):
        modelo = tf.keras.models.load_model(MODEL_FILENAME)
        modelo_cargado = True
    else:
        modelo_cargado = False
except Exception as e:
    print(f"Error cargando modelo: {e}")
    modelo_cargado = False

def predecir_numero(img):
    if not modelo_cargado:
        return f"Error: No se encontró el archivo '{MODEL_FILENAME}' en la carpeta."
    
    if img is None:
        return "Por favor, sube o dibuja una imagen."

    try:
        # Preprocesar la imagen
        # 1. Escala de grises
        img_gris = ImageOps.grayscale(img)
        
        # 2. Invertir colores si el fondo es blanco (número negro)
        arr_gris = np.array(img_gris)
        # Asumimos que la esquina superior izquierda (0,0) es el fondo
        if arr_gris[0, 0] > 127: 
            img_gris = ImageOps.invert(img_gris)

        # 3. Redimensionar a 28x28 (como MNIST)
        img_28x28 = img_gris.resize((28, 28), Image.Resampling.LANCZOS)
        
        # 4. Normalizar (0 a 1)
        img_matriz = np.array(img_28x28) / 255.0
        
        # 5. Darle la forma que espera TensorFlow: (1, 28, 28, 1)
        imagen_final = np.expand_dims(img_matriz, axis=(0, -1))

        # ¡Hacer predicción!
        prediccion = modelo.predict(imagen_final)[0][0]
        porcentaje = prediccion * 100
        
        if prediccion > 0.5:
            resultado = f"✅ ¡Es un 3!\nSeguridad: {porcentaje:.2f}%"
        else:
            resultado = f"❌ NO es un 3.\nProbabilidad de ser 3: {porcentaje:.2f}%"
            
        return resultado
    except Exception as e:
        return f"Error procesando la imagen: {str(e)}"

# Crear la interfaz moderna basada en navegador con Gradio
interfaz = gr.Interface(
    fn=predecir_numero,
    inputs=gr.Image(type="pil", label="Sube o Dibuja un Número"),
    outputs=gr.Textbox(label="¡Veredicto de la Inteligencia Artificial!", lines=3),
    title="Inteligencia Artificial: Reconocedor de Números (El 3)",
    description="Sube una imagen con un número manuscrito para que nuestro cerebro artificial, recién entrenado en Colab, determine si es un '3' o no.",
    theme="default"
)

if __name__ == "__main__":
    if modelo_cargado:
        print(f"Modelo cargado correctamente. Iniciando la interfaz web...")
        interfaz.launch(inbrowser=True)
    else:
        print(f"¡ATENCIÓN! Falta el archivo '{MODEL_FILENAME}'.")
        print("Por favor descarga el archivo de Colab y ponlo en esta misma carpeta, luego vuelve a ejecutar este script.")
