import gradio as gr
import tensorflow as tf
import numpy as np

# =====================================================================
# FASE 5: DESARROLLO DE LA MINI APP (INTERFAZ GRÁFICA)
# =====================================================================

print("⚙️ Cargando el cerebro de la IA...")
# 1. Cargar el modelo que guardamos en la Fase 4
try:
    modelo = tf.keras.models.load_model('modelo_oficina.keras')
    print("✅ ¡Modelo 'modelo_oficina.keras' cargado correctamente!")
except Exception as e:
    print(f"❌ Error al cargar el modelo. ¿Aseguraste ejecutar el entrenamiento primero?: {e}")
    exit()

# Nombres de nuestras clases, en orden alfabético como los leyó Keras
nombres_clases = ['hojas_carta', 'recibos']

# 2. La función que hará el trabajo pesado al recibir la foto
def clasificar_documento(imagen_usuario):
    # a) Si por algún error no hay imagen, pedimos una.
    if imagen_usuario is None:
        return "Por favor, toma una foto o sube una imagen."
        
    # b) Gradio nos entrega la imagen, pero debemos ajustarla a (128, 128)
    # Igual a como lo hicimos en el entrenamiento.
    imagen_redimensionada = tf.image.resize(imagen_usuario, (128, 128))
    
    # c) Normalizamos (dividimos entre 255.0) para que esté en la escala [0, 1]
    imagen_normalizada = imagen_redimensionada / 255.0
    
    # d) El modelo no procesa imágenes solas, procesa "lotes". 
    # Creamos un lote artificial de 1 sola imagen.
    lote_de_imagenes = tf.expand_dims(imagen_normalizada, 0)
    
    # e) Obtener la Predicción (La calificación de nuestra neurona de salida)
    # Como nuestra última capa es un Sigmoid de 1 neurona, nos devuelve un arreglo con 1 solo progreso decimal.
    prediccion_decimal = modelo.predict(lote_de_imagenes)[0][0]
    
    # f) Interpretar el sigmoide (0.0 a 1.0)
    # Valores menores a 0.5 tienden a la Clase 0 (hojas_carta)
    # Valores mayores o iguales a 0.5 tienden a la Clase 1 (recibos)
    if prediccion_decimal < 0.5:
        resultado = f"📄 Parece ser una Hoja Carta"
        # Su seguridad es qué tan lejos está del 0.5 hacia el 0
        seguridad = (1.0 - prediccion_decimal) * 100
    else:
        resultado = f"🧾 Parece ser un Recibo"
        # Su seguridad es qué tan cerca está del 1.0
        seguridad = prediccion_decimal * 100
        
    return f"{resultado} (Seguridad: {seguridad:.2f}%)"

# 3. Armar la interfaz visual de la App
print("\n🚀 Preparando la página web...")
interfaz_web = gr.Interface(
    fn=clasificar_documento, # ¿Qué función llamamos cuando pongan la foto?
    inputs=gr.Image(label="Sube aquí tu imagen o usa tu cámara"), # El cuadro de entrada
    outputs=gr.Text(label="Veredicto del Modelo"), # El cuadro de respuesta
    title="🤖 Clasificador de Documentos de Oficina",
    description="Sube una fotografía de un recibo o una hoja tamaño carta y deja a la IA adivinar qué es.",
    allow_flagging="never" # Quitamos el botón extra de "Marcar error" de Gradio para que se vea más limpio
)

# 4. Iniciar el servidor local
print("🌐 ¡Todo listo! Lanzando servidor...")
interfaz_web.launch()
