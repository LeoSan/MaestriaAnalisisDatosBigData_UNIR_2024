# Práctica: Red Neuronal Convolucional (CNN) desde Cero

Este proyecto tiene como objetivo construir una Red Neuronal Convolucional (CNN) paso a paso utilizando TensorFlow y Keras. 

**Objetivo Específico:** Entrenar un modelo capaz de distinguir el número "3" de cualquier otro número utilizando el conjunto de datos MNIST (clasificación binaria).

## Pasos del Desarrollo

### Paso 1: Carga y Preparación Inicial de Datos
- **Conjunto de datos:** Utilizamos `mnist` de `tf.keras.datasets`, el cual contiene imágenes de 28x28 píxeles de números escritos a mano (0-9).
- **Transformación de Etiquetas:** Originalmente, las etiquetas van del 0 al 9. Como nuestro problema es binario (¿es un 3 o no?), convertimos las etiquetas en booleanos (`True` si es 3, `False` si no lo es) y posteriormente a enteros (`1` y `0`). A las redes neuronales se les facilita trabajar con números.

### Paso 2: Preprocesamiento de los Datos
Para que la red neuronal aprenda de forma rápida y matemáticamente estable, debemos aplicar dos ajustes a las imágenes de entrada:
1. **Normalización:** Los píxeles tienen valores entre 0 (negro) y 255 (blanco). Dividimos todas las imágenes entre `255.0` para escalar estos valores a un rango entre `0.0` y `1.0`. Esto evita problemas de explosión de gradientes.
2. **Reshape (Redimensionamiento):** TensorFlow espera que las imágenes de entrada para una CNN tengan el formato `(cantidad_imagenes, alto, ancho, canales)`. Como nuestras imágenes están en escala de grises, solo tienen un canal. Transformamos la forma de `(28, 28)` a `(28, 28, 1)`.

### Paso 3: Construcción de la Arquitectura (El Cerebro)
Una CNN funciona como una línea de ensamblaje dividida en dos grandes fases:
1. **Extracción de Características (Base de la red):**
   - Utilizamos capas `Conv2D` (Convolucionales) para escanear la imagen usando "filtros". La red aprende por sí sola a detectar líneas, bordes y curvas.
   - Utilizamos capas `MaxPooling2D` para reducir el tamaño de la imagen resultante, quedándonos solo con los patrones más fuertes e importantes. Esto hace a la red más rápida y evita que memorice ruido.
2. **Toma de Decisión (Cúspide de la red):**
   - Utilizamos la capa `Flatten` para "aplastar" nuestros mapas de características en una sola fila (1D), para que las neuronas tradicionales puedan leerlos.
   - Usamos capas `Dense` (Neuronas conectadas todas con todas) para hacer el razonamiento final ("*Si tiene una curva arriba y una abajo, entonces es un 3*").

**Funciones de Activación Utilizadas:**
Las Familias de Funciones (Las más comunes en TensorFlow/Keras)
Aquí te presento a las hermanas de relu que verás frecuentemente en Deep Learning:

1. ReLU (Rectified Linear Unit) - La que usamos en la Línea 54
¿Qué hace? Es súper simple: si recibe un número negativo, lo convierte en 0.0. Si recibe un número positivo, lo deja pasar tal cual.
¿Por qué se usa tanto? Al ser una operación matemática tan sencilla, la computadora la ejecuta a la velocidad de la luz. Además, resuelve un problema matemático complejo llamado "desvanecimiento del gradiente" que las redes antiguas sufrían.
¿Dónde se usa? Es el estándar absoluto para todas las capas ocultas (las que van en medio) de casi cualquier red neuronal moderna, incluyendo las CNN.

2. Sigmoid (Sigmoide) - La que usamos al final de nuestro código
¿Qué hace? Aplasta cualquier número que le des (por muy grande que sea, positivo o negativo) para que encaje perfectamente entre 0.0 y 1.0. Su gráfica parece una forma de "S".
¿Por qué se usa? Como sus valores siempre están entre 0 y 1, la interpretamos como un porcentaje de probabilidad. Si al final nos da 0.85, interpretamos: "Estoy 85% segura de que es un 3".
¿Dónde se usa? Se usa casi exclusivamente en la última neurona de salida cuando tenemos un problema binario (es un 3 vs. no es un 3 / es un gato vs. es un perro).

3. Softmax
¿Qué hace? Es la hermana mayor de Sigmoid. Imagina que el problema no es binario, sino que quieres que te diga qué número es (del 0 al 9). Tendrías 10 neuronas de salida. Softmax toma el resultado de las 10 neuronas, lo convierte en probabilidades entre 0 y 1, y se asegura de que la suma total de las 10 probabilidades sea exactamente 1 (o 100%).
¿Dónde se usa? En la capa de salida para problemas Multiclase (cuando tienes 3 o más categorías posibles para predecir).

4. Tanh (Tangente Hiperbólica)
¿Qué hace? Es muy parecida a Sigmoid (tiene forma de "S"), pero aplasta los números para que queden entre -1.0 y 1.0 (su centro está en el cero absoluto).
¿Dónde se usa? Antes de que existiera ReLU, Tanh era la reina de las capas ocultas. Hoy en día casi no se usa para procesamiento de imágenes, pero es común en redes neuronales antiguas o en procesamiento de texto (Redes Recurrentes RNN).

5. Leaky ReLU
¿Qué hace? Es una mejora directa de ReLU. El problema con ReLU es que si a muchas neuronas les llegan números negativos se apagan (quedan en cero) y literalmente "mueren" para siempre sin poder aprender más. Leaky ReLU (ReLU con fuga) evita esto haciendo que, en vez de devolver cero en los negativos, devuelva un número pequeñíííto (como -0.01).
¿Dónde se usa? En las capas ocultas, en casos donde notes que tu red neuronal dejó de aprender repentinamente o se "congeló".

### Entendiendo el Resumen del Modelo (`modelo.summary()`)
La tabla que se imprime es vital para todo Ingeniero en Inteligencia Artificial. Nos dice:
1. Las capas están conectadas en orden.
2. Fíjate en la columna de la derecha (`Param #`). ¡Nuestra red neuronal tiene que ajustar **223,873 conexiones matemáticas (pesos)** para aprender a distinguir un "3"!

Parece mucho, pero para la computadora esto tomará apenas unos segundos.

**¿Cómo sé si la cantidad de Parámetros (Param #) está bien o está mal?**
No hay un número "mágico" que debas calcular a mano. La cantidad de parámetros es el resultado directo de la arquitectura que tú diseñaste (el tamaño de tus imágenes y el número de neuronas/filtros de cada capa). Se aprende por experiencia.

Verás con la práctica que tu cantidad de parámetros está "mal" bajo estos dos extremos:
* **Muy pocós parámetros (Ej. 500 parámetros):** A esto se le llama **Underfitting (Subajuste)**. La red es "muy pequeña (tonta)" para entender el problema. No logrará aprender las curvas de un número "3" por más que entrene. Su porcentaje de acierto en el entrenamiento se quedará bajo (ej: `50%`).
* **Demasiados parámetros (Ej. 50,000,000 parámetros):** A esto se le llama **Overfitting (Sobreajuste)**. La red es demasiado grande. Tiene un cerebro gigantesco para un problema pequeño. ¿Qué pasa? En lugar de "aprender" a reconocer un número 3 general, de tanta capacidad mental que tiene se "memoriza" píxel por píxel todas las imágenes de entrenamiento (incluyendo su ruido y manchas). Su acierto en entrenamiento será del `100%`, pero cuando le pases una imagen nunca antes vista del examen de validación fallará miserablemente porque no memorizó *esa* imagen en específico. Adicional a eso, te va a saturar la memoria de tu computadora al entrenar.

Nuestro número de `223,873` es bastante **sano y adecuado** para el tamaño y complejidad de encontrar un número en imágenes de 28x28 píxeles. Tiene suficiente capacidad para aprender sin asfixiarse.

### Paso 4: Compilar y Entrenar el Modelo (La Práctica)
Una vez que el "cerebro" (la arquitectura) está construido, necesita dos cosas fundamentales: reglas de juego para aprender y horas de estudio.

1. **Compilación (`modelo.compile`):**
   - **Optimizador (`adam`):** Es el algoritmo que ajusta los valores matemáticos internos (pesos) de la red para que cada vez se equivoque menos. Es muy popular por ser rápido y eficiente.
   - **Función de Pérdida (`binary_crossentropy`):** Mide gráficamente "qué tan mal" lo está haciendo la red neuronal en sus predicciones. Como nuestro problema es de 1 (es 3) y 0 (no es 3), usamos la entropía cruzada binaria.
   - **Métricas (`accuracy`):** Para nosotros los humanos, pedimos que nos muestre qué porcentaje de imágenes está acertando correctamente.

2. **Entrenamiento (`modelo.fit`):**
   - **Épocas (`epochs`):** Es la cantidad de veces que la red neuronal revisará **todo** el conjunto de datos de entrenamiento para aprender de sus errores.
   - **Validation Data (`x_prueba, y_prueba_binario`):** Al final de cada época, la red neuronal realizará un "examen sorpresa" con imágenes que **nunca ha visto** durante su estudio. Esto evita que la red simplemente "memorice" las imágenes de entrenamiento (un problema grave llamado *Overfitting* o Sobreajuste).

### Resultados del Entrenamiento (Análisis Técnico)

Después de correr el `modelo.fit()`, los resultados obtenidos son espectaculares. Analicémoslos juntos como ingenieros:

* **`accuracy: 0.9990`:** ¡Guau! En la Época 5, la red neuronal logró un **99.90% de precisión** con las imágenes de estudio. Prácticamente no se equivoca nunca.
* **`loss: 0.0027`:** El margen de "confusión matemática" bajó casi a cero. Se empezó con `0.0704` y terminó en `0.0027`. La red está sumamente segura de sus respuestas.
* **`val_accuracy: 0.9981`** Este es el número **más importante de todos**. En el "examen sorpresa" con imágenes que nunca antes había visto tu red, obtuvo un asombroso **99.81% de precisión**.

**Conclusión técnica:** Tu modelo entrenó a la perfección. No tenemos *Underfitting* (porque el accuracy es altísimo) y tampoco llegamos al *Overfitting* (porque el `val_accuracy` es prácticamente idéntico al `accuracy` de entrenamiento, la red aprendió a generalizar muy bien qué es un "3").

### Paso 6: Guardar el "Cerebro" Entrenado
No queremos tener que volver a entrenar la red durante 5 minutos cada vez que deseamos que reconozca un número.
Por eso, una vez finalizado el entrenamiento, guardamos todos esos `223,873` parámetros (los pesos matemáticos aprendidos) en un archivo ligero con extensión `.keras` o `.h5`.

En Google Colab, se ejecuta lo siguiente al final:
```python
modelo.save('mi_cerebro_reconoce_tres.keras')
```

### Paso 7 y 8: Ejecutar nuestra Mini App en Local (Inferencia)
Ahora que el cerebro está entrenado, podemos usarlo en nuestra propia computadora (Inferencia) implementando una pequeña interfaz gráfica para que cualquier humano pueda probarlo subiendo sus imágenes.

**¿Cómo ejecutarlo en tu Mac?**

1. **Descargar el Cerebro:** Descarga el archivo `mi_cerebro_reconoce_tres.keras` desde la barra lateral izquierda de tu Google Colab.
2. **Ubicar el Archivo:** Guarda ese archivo exactamente en esta ruta: `/Users/fernando/Documents/DEV/AgenteIA/PracticaCNN/DesceCero/`. Debe de estar en la misma carpeta que el código `002_MiniApp_CNN.py`.
3. **Activar el Entorno:** Abre tu terminal y actívalo si no lo has hecho:
   ```bash
   cd /Users/fernando/Documents/DEV/AgenteIA/PracticaCNN
   source venv/bin/activate
   ```
4. **Dependencias:** Asegúrate de tener instalados los paquetes ejecutando:
   ```bash
   pip install -r requirements.txt
   ```
5. **¡A Jugar!:** Finalmente, métete a la carpeta donde está el código local y arranca la interfaz:
   ```bash
   cd DesceCero
   python3 002_MiniApp_CNN.py
   ```
   **Nota:** Se abrirá una pequeña ventana. Puedes buscar o dibujar en Paint/Vista Previa números en fondo blanco o negro (no importa la resolución, el software la adaptará a 28x28 automáticamente) y cargarlos. ¡Verás cómo el modelo que tú mismo creaste ahora tiene vida!

---

## 🚀 Hoja de Ruta del Proyecto (Completada)

- [x] Paso 1: Obtener y preparar los datos (MNIST)
- [x] Paso 2: Preprocesamiento de las imágenes (Normalización y Reshape)
- [x] Paso 3: Construir la Arquitectura de la CNN (Extracción de características y Decisión)
- [x] Paso 4: Compilar y Entrenar el Modelo
- [x] Paso 5: Evaluar el modelo y hacer predicciones (Ejemplo Práctico)
- [x] Paso 6: Guardar modelo entrenado en Colab (`.keras`)
- [x] Paso 7: Descargar y cargar modelo en entorno local
- [x] Paso 8: Crear mini-aplicación con interfaz gráfica para probar imágenes personalizadas

---

## 🛠️ Stack Tecnológico y Versiones

Este logro fue construido utilizando el siguiente ecosistema de herramientas de Inteligencia Artificial y Python. El entorno local fue ajustado específicamente para Mac (arquitectura ARM64):

- **Lenguaje Base:** Python 3.9+ 
- **TensorFlow & Keras (v2.10+):** El motor principal para la creación, entrenamiento veloz vía Tensores y exportación de la Red Neuronal Convolucional.
- **NumPy (v1.26.4):** Herramienta indispensable para la manipulación ultra rápida de matrices numéricas (las imágenes antes de pasarlas por la red).
- **Pillow (PIL) (v11.3.0):** Para el procesamiento, recorte, inversión de color y edición general de imágenes que sube el usuario en la aplicación web.
- **Gradio (v3.50.2):** Framework especializado para crear interfaces web interactivas para modelos de Machine Learning en minutos. (Escogimos la versión estable 3.5 para evitar colisiones nativas de Mac).
- **Google Colab:** Entorno de Jupyter Notebooks en la nube con poder computacional gratuito usado para *entrenar* la red sin saturar la computadora personal.

---

## 🌐 Comunidad y Recursos: Síguele la pista a la IA

Si te maravilló lo rápido que pudimos levantar una interfaz de inteligencia artificial predictiva con **Gradio**, te interesará seguir muy de cerca a su empresa creadora: **Hugging Face**. Son actualmente la comunidad y repositorio *Open Source* de Inteligencia Artificial más grande e innovadora del planeta (conocidos coloquialmente en la industria como el "GitHub del Machine Learning").

Síguelos de cerca en redes sociales para mantenerte al día sobre los nuevos modelos de lenguaje abiertos (como Llama 3 o Mistral), herramientas revolucionarias para ingenieros ("transformers") y mucha educación:

1. **X (Twitter - Global):** [@huggingface](https://twitter.com/huggingface) (Su principal canal de anuncios técnicos casi a diario).
2. **LinkedIn:** [Hugging Face](https://www.linkedin.com/company/huggingface) (Artículos, comunidad de negocios e integraciones corporativas).
3. **YouTube:** [Hugging Face](https://www.youtube.com/@HuggingFace) (Cursos en video gratuitos desde Cero a Experto en Deep Learning, procesamiento de lenguaje natural y audio).
4. **Sitio Web Principal (El Hub):** [huggingface.co](https://huggingface.co/) (Aquí es donde debes buscar herramientas para descargar cerebros pre-entrenados del mundo entero en el futuro, no solo números, sino voces, textos, generación de imágenes, etc).
5. **Discord Oficial:** [Hugging Face Discord](https://discord.gg/huggingface) (El lugar ideal para pedir ayuda a otros ingenieros sobre `gradio` u otros modelos de su ecosistema).
