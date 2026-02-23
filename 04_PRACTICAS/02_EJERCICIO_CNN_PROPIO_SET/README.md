# IA Oficina: Clasificador Visual de Documentos

## Objetivo del Proyecto
Desarrollar una aplicación local utilizando Inteligencia Artificial (Redes Neuronales Convolucionales, o CNNs) capaz de distinguir visualmente entre dos tipos de documentos comunes en una oficina:
1.  **Recibos / Tickets de gastos.**
2.  **Hojas de texto tamaño carta.**

## Plan de Acción (Fases del Proyecto)
Iremos marcando estas tareas conforme avancemos.

- [x] **Fase 1: Recolección y Preparación de Datos (El Dataset)**
  - Recolectar fotografías de recibos y hojas tamaño carta.
  - Organizar las imágenes en la estructura de directorios estandarizada (`dataset/clase/...`).
- [x] **Fase 2: Preparación del Código Python para Imágenes a Color**
  - Escribir el script para cargar las imágenes a color y leerlas como matrices numéricas (RGB, 3 canales).
  - Escalar todas las imágenes a un tamaño estándar (ej. 128x128 píxeles) y normalizarlas.
- [x] **Fase 3: Construcción del Modelo ConvNet (CNN)**
  - Definir la arquitectura de la red: Capas Convolucionales, *MaxPooling* y capas Densas finales.
  - Compilar el modelo seleccionando el optimizador y función de pérdida para clasificación binaria.
- [x] **Fase 4: Entrenamiento y Evaluación**
  - Entrenar el modelo con nuestro nuevo dataset.
  - Evaluar el desempeño (Precisión / Accuracy).
  - Guardar el modelo entrenado (un archivo `.keras`).
- [x] **Fase 5: Desarrollo de la MiniApp / Interfaz Gráfica**
  - Usar Gradio para crear una pequeña pantalla web donde puedas prender tu cámara web o subir una imagen de tu computadora.
  - Hacer la conexión para que el programa emita su veredicto (Ej. "Recibo detectado con 95% de seguridad").

### 🧹 Limpieza del Dataset (Troubleshooting)
Durante el desarrollo, nos encontramos con el error `INVALID_ARGUMENT: Unknown image file format` al intentar cargar las imágenes. 
**¿Por qué sucede?** TensorFlow espera imágenes estrictamente en formatos válidos (JPEG, PNG, etc.). Al pasar fotos desde dispositivos (como un iPhone con formato `.HEIC`), los archivos pueden corromperse o tener una extensión falsa `.jpg` que no corresponde a su contenido real.
**¿Cómo lo solucionamos?**
Creamos un script de Python usando la librería nativa `imghdr` (que lee el "ADN" o la cabecera real del archivo, ignorando su extensión) para detectar y eliminar los archivos no válidos. ¡Limpiar los datos de archivos corruptos es el paso número uno para que el modelo pueda entrenar!

---

## 📝 La Receta: Preparación de Datos (Fase 2)
Cualquier red neuronal que clasifique imágenes **siempre** requerirá que las fotos pasen por una "línea de ensamblaje matemática". Estos son los **5 Pasos Atómicos** obligatorios (La Receta) que verás programados en el archivo `001_Entrenamiento.py`:

*   **Paso Atómico 1: Definir Constantes.** Decidir dónde está la carpeta (`dataset`), a qué tamaño exacto forzaremos todas las fotos (ej. `128x128`) y en cuántos grupos las leeremos para no asfixiar la RAM (ej. lotes de `8`).
*   **Paso Atómico 2: Cargar y Dividir.** Usando utilidades de TensorFlow, agarramos la carpeta raíz y le decimos que la corte matemáticamente: el `80%` será para aprender (Training) y el `20%` será el examen sorpresa exclusivo para calificar (Validation).
*   **Paso Atómico 3: Identificar Clases.** Extraer automáticamente los nombres de los sub-directorios (ej. `hojas_carta`, `recibos`) para que el programa sepa qué es qué.
*   **Paso Atómico 4: Normalización.** El paso matemático más crucial en toda IA visual: transformar la intensidad bruta de los colores RGB (que va de 0 a 255) dividiéndola entre 255. Esto "aplasta" todos los valores a una escala de `0.0` a `1.0`, estabilizando inmediatamente el algoritmo de la red neuronal.
*   **Paso Atómico 5: Optimización de RAM.** Habilitar el `"Cache" y "Prefetch"` para que mientras la tarjeta gráfica entrena la foto actual, el procesador (CPU) vaya precargando en memoria RAM la siguiente foto desde tu disco duro a máxima velocidad.

---

## 💡 Tips Teóricos y Preguntas de Entrevista

> [!TIP]
> **Data Cleaning (Limpieza de Datos) para Entrevistas**
> No te abrumes con este término. Si en una entrevista para nivel Junior/Mid te preguntan *"¿Qué técnicas de limpieza de datos conoces?"*, buscan saber si tienes **sentido común** antes de tirar código a ciegas. Menciona estas 3 balas:
> 1. **Manejo de Nulos/Corruptos (Lo que acabamos de hacer):** Detectar y eliminar archivos rotos, o en bases de datos, decidir qué hacer con las celdas vacías (borrar la fila o rellenarla con el promedio).
> 2. **Eliminación de Duplicados:** Si tienes 100 fotos exactamente iguales, el modelo memoriza en lugar de aprender. Hay que remover la data repetida.
> 3. **Detección de "Outliers" (Valores Atípicos):** Si hacemos una IA para predecir precios de casas y alguien por error puso que una casa cuesta $0.01 centavos, ese dato "ensuciará" las matemáticas. Hay que filtrarlo.
> *Saber aplicar eso te pone por encima del 80% de los principiantes que solo quieren armar redes neuronales apresuradamente.*

> [!TIP]
> **Lectura del Model Summary para Entrevistas**
> Cuando imprimes `modelo.summary()`, un reclutador podría preguntarte: *"¿Por qué tus Non-trainable params están en 0?"*. Esta es la respuesta ideal:
> - **Trainable params:** Son los "pesos" o "perillas matemáticas" que la red ajustará durante el entrenamiento. Que estén todos activos significa que creamos la red desde cero y todo su "cerebro" está aprendiendo de nuestras fotos.
> - **Non-trainable params en 0:** Es lo correcto en proyectos desde cero. Solo verías un número mayor a cero si usaras la técnica de **Transfer Learning** (Transferencia de Aprendizaje). Es decir, si descargaras un modelo pre-entrenado gigante (ej. de Google) y "congelaras" (non-trainable) el 99% de su cerebro para que no olvide lo que ya sabe, dejando solo la última capa libre para aprender tu problema específico.

> [!TIP]
> **Arquitectura en Keras: ¿Qué hay más allá de "Sequential"?**
> En la línea `tf.keras.models.Sequential([...])`, le estamos diciendo a TensorFlow cómo es la "estructura" de nuestro edificio neuronal. En Keras hay **3 formas principales** de construir modelos, y conocer la diferencia es clave para un nivel intermedio:
> 1. **Sequential (El que usamos):** Es como construir con bloques de Lego, una capa directamente sobre la otra. Es lineal: la entrada va a la capa 1, luego a la 2, luego a la 3 y sale. Es perfecto para el 80% de los proyectos comunes, como el nuestro de detectar recibos.
> 2. **Functional API (El Intermedio):** Se usa cuando tu red ya no es una simple línea recta. Imagina un escenario donde tu red tiene **dos entradas diferentes** (ej. lee la foto del recibo por un lado, y texto plano del ticket por otro) y toma una sola decisión. O redes que se "ramifican". Es más poderoso y flexible que *Sequential*.
> 3. **Model Subclassing (El Avanzado):** Se hace programando directamente utilizando Programación Orientada a Objetos en Python. Esto lo usan principalmente los investigadores que están inventando capas matemáticas que aún no existen en la librería de Keras. Para proyectos de negocios, casi nunca tendrás que llegar a este nivel.

> [!TIP]
> **El Enemigo Público #1: El Sobreajuste (Overfitting)**
> En entrevistas, casi siempre te pondrán este caso: *"Tu modelo tiene 98% de accuracy entrenando, pero en producción falla muchísimo. ¿Qué está pasando?"*
> **La respuesta es Overfitting.** Significa que le diste demasiadas vueltas de estudio (Épocas/Epochs) a la red con las mismas fotos. En lugar de aprender a reconocer los **conceptos generales** de qué hace a un recibo ser un recibo (letras pequeñas, papel blanco), el modelo **memorizó** las fotos exactas que le diste (memorizó que *esa* marca de agua estaba en *esa* esquina de tu escritorio).
> - **El Síntoma:** Lo ves en vivo cuando el `accuracy` de estudio sigue subiendo hacia el 100%, pero el `val_accuracy` (el examen sorpresa) se estanca en 75% o empieza a bajar, y el `val_loss` (la confusión en el examen) se dispara.
> - **La Solución (Nivel Entrevista):** Menciona que aplicarías técnicas como **"Early Stopping"** (detener el entrenamiento automáticamente cuando el examen sorpresa deja de mejorar) o **"Data Augmentation"** (rotar, hacer zoom o cambiar el brillo a tus fotos originales para engañar a la red y forzarla a aprender conceptos nuevos, no a memorizar imágenes fijas).

> [!TIP]
> **Conoce a tu Equipo: Los Optimizadores más populares en Keras**
> El optimizador es el algoritmo matemático responsable de reducir el "Loss" (error) ajustando los pesos de la red. Imagina que la red está bajando una montaña a ciegas buscando el punto más bajo (el error cero). El optimizador es la "estrategia" que usa para bajar.
> 
> 1. **SGD (Stochastic Gradient Descent):Descenso de gradiente estocástico** El abuelo de todos. Baja la montaña dando pasos fijos. **Pros:** Conceptualmente simple y teóricamente siempre llega al mejor resultado si le das demasiado tiempo. **Contras:** Es muy lento y puede quedarse atascado fácilmente en "baches" (mínimos locales) creyendo que llegó al final.

> 2. **Adam (Adaptive Moment Estimation): Estimación del momento adaptativo** El Rey Actual (el que usamos nosotros). Toma lo mejor de SGD y le añade "impulso" y memoria de sus pasos anteriores. **Pros:** Ajusta inteligentemente la velocidad de sus pasos (Learning Rate); si el camino es recto acelera, si hay curvas frena. Es el predeterminado para el 90% de problemas estándar.

> 3. **RMSprop (Root Mean Square Propagation): Propagación de la raíz cuadrada media** Inventado por los creadores del Deep Learning moderno (Geoffrey Hinton). **Pros:** Muy similar a Adam, soluciona los problemas de que el aprendizaje "se apague" prematuramente. Hoy en día se usa muchísimo para Redes Recurrentes (RNNs) o problemas de lenguaje (Texto secuencial, como lo que hace ChatGPT).

> 4. **Adagrad (Adaptive Gradient Algorithm): Algoritmo de gradiente adaptativo:** El especialista silencioso. **Pros:** Acorta o alarga el paso *por cada variable individual*. Da pasos grandes para características "raras" y pasos pequeños para características repetitivas. **Contras:** Con el tiempo, sus pasos se hacen tan microscópicos que la red deja de aprender antes de tiempo.

> [!TIP]
> **La Brújula de la Red: Funciones de Pérdida (Loss Functions) en la Industria**
> Si el optimizador es la *estrategia* para bajar la montaña, la Función de Pérdida es la **brújula** que le dice qué tan lejos está de su meta. Calcula matemáticamente qué tan equivocada estuvo la red en su última predicción (el "Loss"). Las más usadas en el mundo laboral son 4:
> 
> 1. **Binary Crossentropy (Entropía Cruzada Binaria):** La que usamos nosotros. Mide cuán lejos está una probabilidad pronosticada del valor real (0 o 1). **Uso Exclusivo:** *Clasificación Binaria* (Solo 2 opciones: Gato/Perro, Spam/No Spam, Hoja/Recibo). **Regla de oro:** Siempre va acompañada de la activación `sigmoid` en la última capa.
> 
> 2. **Categorical Crossentropy:** La hermana mayor de la anterior. **Uso:** *Clasificación Multiclase* donde las opciones son mutuamente excluyentes (ej. si clasifica una foto en Gato, Perro O Pájaro; solo puede ser uno). **Regla de oro:** Siempre va acompañada de la activación `softmax` en la última capa, y requiere que tus etiquetas (datos reales) estén "One-Hot Encoded" (ej. un arreglo como `[0, 1, 0]`).
> 
> 3. **Sparse Categorical Crossentropy:** Matemáticamente idéntica a la anterior, pero optimizada para ahorrar memoria. **Uso:** Misma *Clasificación Multiclase*, pero ideal cuando tienes decenas o miles de categorías. En lugar de obligarte a usar largos arreglos de ceros y unos, permite usar números enteros simples en tus etiquetas (ej. clase `5`, clase `12`).
> 
> 4. **MSE (Mean Squared Error / Error Cuadrático Medio):** El clásico inamovible de la estadística tradicional. **Uso:** No se usa para clasificar, se usa para **Regresión** (predecir un número continuo). Por ejemplo: predecir el precio exacto de una casa en dólares, los grados de temperatura mañana, o la edad numérica de una persona en una foto. **Regla de oro:** Suele ir con activación `linear` (o simplemente sin función de activación) en la neurona de salida.

> [!TIP]
> **Familias de Funciones de Activación (Las más comunes en TensorFlow/Keras)**
> Aquí te presento a la familia de activaciones que verás frecuentemente en Deep Learning:
> 
> 1. **ReLU (Rectified Linear Unit)**
> ¿Qué hace? Es súper simple: si recibe un número negativo, lo convierte en 0.0. Si recibe un número positivo, lo deja pasar tal cual.
> ¿Por qué se usa tanto? Al ser una operación matemática tan sencilla, la computadora la ejecuta a la velocidad de la luz. Además, resuelve un problema matemático complejo llamado "desvanecimiento del gradiente" que las redes antiguas sufrían.
> ¿Dónde se usa? Es el estándar absoluto para todas las capas ocultas (las que van en medio) de casi cualquier red neuronal moderna, incluyendo las CNN.
> 
> 2. **Sigmoid (Sigmoide)**
> ¿Qué hace? Aplasta cualquier número que le des (por muy grande que sea, positivo o negativo) para que encaje perfectamente entre 0.0 y 1.0. Su gráfica parece una forma de "S".
> ¿Por qué se usa? Como sus valores siempre están entre 0 y 1, la interpretamos como un porcentaje de probabilidad. Si al final nos da 0.85, interpretamos: "Estoy 85% segura".
> ¿Dónde se usa? Se usa casi exclusivamente en la última neurona de salida cuando tenemos un problema binario (es un 3 vs. no es un 3 / es un gato vs. es un perro).
> 
> 3. **Softmax**
> ¿Qué hace? Es la hermana mayor de Sigmoid. Imagina que el problema no es binario, sino que quieres que te diga qué número es (del 0 al 9). Tendrías 10 neuronas de salida. Softmax toma el resultado de las 10 neuronas, lo convierte en probabilidades entre 0 y 1, y se asegura de que la suma total de las 10 probabilidades sea exactamente 1 (o 100%).
> ¿Dónde se usa? En la capa de salida para problemas Multiclase (cuando tienes 3 o más categorías posibles para predecir).
> 
> 4. **Tanh (Tangente Hiperbólica)**
> ¿Qué hace? Es muy parecida a Sigmoid (tiene forma de "S"), pero aplasta los números para que queden entre -1.0 y 1.0 (su centro está en el cero absoluto).
> ¿Dónde se usa? Antes de que existiera ReLU, Tanh era la reina de las capas ocultas. Hoy en día casi no se usa para procesamiento de imágenes, pero es común en redes neuronales antiguas o en procesamiento de texto (Redes Recurrentes RNN).
> 
> 5. **Leaky ReLU**
> ¿Qué hace? Es una mejora directa de ReLU. El problema con ReLU es que si a muchas neuronas les llegan números negativos se apagan (quedan en cero) y literalmente "mueren" para siempre sin poder aprender más. Leaky ReLU (ReLU con fuga) evita esto haciendo que, en vez de devolver cero en los negativos, devuelva un número pequeñíííto (como -0.01).
> ¿Dónde se usa? En las capas ocultas, en casos donde notes que tu red neuronal dejó de aprender repentinamente o se "congeló".


> [!TIP]
> **El Secreto de la Velocidad: `cache()` vs `prefetch()`**
> En el código `dataset.cache().prefetch(buffer_size=AUTOTUNE)`, estamos haciendo dos cosas distintas pero complementarias para optimizar la velocidad:
> 
> 1. **`.cache()` (La Memoria):** Le dice a TensorFlow: *"Oye, ya que cargaste estas fotos en la memoria RAM, no las borres cuando termines la época. Guárdalas ahí listas para la siguiente vuelta"*. Esto es vital si tu disco duro es lento (HDD) o si el dataset es pequeño y cabe en la RAM. Evita leer el disco duro repetidamente.
> 
> 2. **`.prefetch(buffer_size=AUTOTUNE)` (El Paralelismo):** Le dice a TensorFlow: *"Mientras la GPU está trabajando en la época actual (época 1), empieza a preparar en segundo plano las fotos de la siguiente época (época 2)"*. `AUTOTUNE` significa que TensorFlow elige automáticamente cuántas fotos preparar de antemano basándose en tu hardware.
> 
> **La analogía:** Imagina que la GPU es un chef cocinando. Sin `prefetch`, el chef termina un plato, espera a que alguien le traiga los ingredientes del siguiente y luego cocina. Con `prefetch`, mientras el chef cocina el plato 1, un asistente ya está cortando las verduras para el plato 2. El chef nunca espera. 


> [!TIP]
> **Sin Dropout vs Con Dropout**
> Imagina que esas 128 neuronas son el "Comité de Jueces" que tiene que votar si es una Hoja o un Recibo.
> 
> **Sin Dropout:** Con el tiempo, los 128 jueces se vuelven "flojos". Descubren que el Juez #43 y el Juez #12 son buenísimos detectando logos corporativos, así que los demás dejen de pensar y simplemente le copian la respuesta a ellos dos. La red "memoriza" en lugar de aprender el panorama completo.
> 
> **Con Dropout(0.5):** En cada maldita pasada de entrenamiento (bach/época), el algoritmo duerme aleatoriamente a la mitad de los jueces. El Juez #43 ya no está. Ahora los demás jueces se ven obligados a aprender a detectar cosas por sí mismos porque no pueden depender del "juez líder".


> [!TIP]
> **Otras Funciones de Pérdida Binaria (Alternativas a Binary Crossentropy)**
> 1. **Hinge Loss (Pérdida Bisagra):**
> ¿Qué hace? En lugar de medir porcentajes de "qué tan seguro estás" de la respuesta (como hace crossentropy), simplemente dibuja una línea divisoria (vector) en el espacio matemático y te dice: "Estás en el lado correcto" o "Estás en el lado incorrecto de la línea". Si estás del lado correcto, tu pérdida (Loss) es 0 total, no le importa si estás por poco o por 1 kilometro de seguro.
> ¿Dónde se usa? Es el corazón matemático de los algoritmos SVM (Support Vector Machines), que son los antecesores de las redes neuronales. Casi nunca lo verás en una CNN moderna de Keras, excepto en un experimento académico muy "old-school".
> Regla Rara: Exige que tus resultados matemáticos finales no sean 0 y 1, sino -1 y 1.
> 
> 2. **Squared Hinge Loss (Pérdida Bisagra al Cuadrado):**
> ¿Qué hace? Es idéntica al Hinge Loss normal, pero penaliza exponencialmente a las predicciones que están en el "lado equivocado de la línea".
> ¿Dónde se usa? Si el Hinge Loss normal no logra converger (si tu red neural no aprende), a veces cambiar a esta versión al cuadrado empuja a los pesos matemáticos a encontrar la división más rápido.
> 
> 3. **Focal Loss (Pérdida Focal - El Secreto de Google):**
> Esta es la única alternativa real y moderna a Binary Crossentropy.
> ¿Qué hace? Toma la `binary_crossentropy` y le añade un "botón de ignorar las cosas fáciles". Si la red está 99% segura de que es una "Hoja", le dice al optimizador: *"Ya dominaste eso, no gastes tiempo computacional ni fuerza de memoria ajustando pesos para esta foto. Enfócate exclusivamente en las fotos de Recibos todos borrosos en los que siempre fallas"*.
> ¿Dónde se usa? En Imágenes Médicas o Casos Súper Desbalanceados. Imagina un detector de cáncer donde el 99.9% de las fotos del dataset son de personas sanas y el 0.1% son tumores. Usar `binary_crossentropy` haría a la red perezosa, diría: *"Todas son sanas para sacar 99.9% de accuracy seguro"*. Usar `Focal Loss` obliga a la red a enfocarse exclusivamente en aprender el caso anómalo sin desviar recursos a lo obvio.
> 
> **Resumen para Entrevistas:**
> *"Para redes profundas modernas con tareas binarias, la norma industrial es `binary_crossentropy` siempre emparejada con `sigmoid`. Técnicamente existen funciones clásicas basadas en margen como `hinge loss`, pero son propias del algoritmo SVM clásico. El único escenario donde cambiaría de función en la vida real sería si el dataset estuviera brutalmente desbalanceado (ej. 1% Fraude Bancario vs 99% Transacciones Reales), en ese caso escribiría una Focal Loss personalizada en Keras para obligar a la red a no ignorar a la minoría."*

> [!TIP]
> **El Enemigo del Dataset Pequeño: Overfitting Perfecto**
> ¿Qué pasa si tu modelo alcanza un `accuracy` de **1.0000** (100%) y un `loss` bajísimo durante el entrenamiento, pero en el examen sorpresa (`val_accuracy`) saca **66%** y un `val_loss` por los cielos?
> 
> **La respuesta:** Tu dataset es microscópico. 
> Incluso con herramientas como `Dropout(0.5)`, si tienes (por ejemplo) 118,337 parámetros matemáticos intentando aprender de solo **52 fotos**, la red neuronal actúa como un alumno con memoria fotográfica: **se memoriza las respuestas exactas (las 52 fotos) pixel por pixel, en lugar de aprender los conceptos subyacentes.**
> 
> Al memorizar con éxito las 52 fotos, su calificación de estudio es 100%. Pero cuando llega el examen final (que solo tiene 12 fotos nuevas), al fallar en apenas 4 de ellas su calificación colapsa al 66%.
> 
> **¿Cómo solucionarlo en la vida real?**
> 1. **Conseguir más datos (El Rey):** Pasar de 64 fotos a miles de fotos reales.
> 2. **Data Augmentation (Aumento de Datos):** Forzar a la red a no memorizar texturas fijas rotando, haciendo zoom o metiendo ruido visual a las fotos originales de manera aleatoria.
> 3. **Early Stopping:** Programar a Keras para que aborte el entrenamiento automáticamente en cuanto note que el examen sorpresa (`val_loss`) empieza a empeorar, salvando el modelo de esa época antes de que se vuelva "tonto" por memorizar.


> [!TIP]
> **Preguntas Trampa en Entrevistas Técnicas (Basadas en esta Práctica)**
>
> 1. **¿Por qué divides los píxeles entre 255 al cargar imágenes?**
> * ✅ **Correcto:** "Es Normalización. Si le damos a la red valores de 0 a 255, los cálculos (gradientes) pueden explotar. Al pasarlos a una escala de 0.0 a 1.0, la red estabiliza sus pesos mucho más rápido".
> 
> 2. **¿Por qué usamos `sigmoid` en la última capa en lugar del famoso `softmax`?**
> * ✅ **Correcto:** "Porque estamos haciendo Clasificación Binaria (Hoja o Recibo). `sigmoid` comprime la salida en una probabilidad de 0 a 1 para una sola neurona. Si tuviéramos múltiples clases (Hoja, Recibo, Pluma), usaríamos `softmax` con múltiples neuronas de salida".
>
> 3. **¿Qué pasaría si entrenamos con 1,000 fotos de Recibos y solo 10 de Hojas Carta?**
> * ✅ **Correcto:** "Problema de Dataset Desbalanceado. El modelo se hace 'perezoso' y aprenderá a decir siempre 'Recibo' para garantizar un alto Accuracy sin aprender reglas reales. Hay que balancear las clases (Data Augmentation o Undersampling)".
>
> 4. **Diferencia entre `accuracy` (estudio) y `val_accuracy` (validación).**
> * ✅ **Correcto:** "`accuracy` mide qué tan bien memoriza los datos de estudio, `val_accuracy` mide qué tan bien generaliza en datos que nunca ha visto. Si el primero es alto y el segundo bajo, hay Overfitting(Sobreajuste)".
>
> 5. **¿Qué hace exactamente la capa `Conv2D`?**
> * ✅ **Correcto:** "Aplica 'filtros' (matrices matemáticas) que se deslizan sobre la imagen original para extraer características como bordes horizontales, verticales, texturas o formas complejas en capas más profundas".
>
> 6. **¿Por qué usamos `MaxPooling2D` después de una Convolución?**
> * ✅ **Correcto:** "Sirve para 'Reducción de Dimensionalidad'. Se queda con el píxel más fuerte de una zona pequeña (ej. 2x2). Esto reduce el tamaño de la imagen a la mitad, haciéndolo computacionalmente más barato y ayudando al modelo a enfocarse solo en lo importante (invarianza espacial)".
>
> 7. **¿Por qué usas activación `ReLU` en las capas ocultas y no `sigmoid`?**
> * ✅ **Correcto:** "ReLU (Rectified Linear Unit) evita el problema del 'Desvanecimiento del Gradiente' (Vanishing Gradient). Es matemáticamente más simple (convierte los negativos a 0) y permite que la red aprenda mucho más rápido y profundo que con sigmoide".
>
> 8. **Si mi Accuracy es de 99% pero el Loss es alto, ¿es un buen modelo?**
> * ✅ **Correcto:** "No necesariamente. Un loss (pérdida) alto indica que el modelo no está seguro de sus predicciones, aunque le haya atinado. Ejemplo: acertó que era 'Recibo', pero solo con un 51% de seguridad. Queremos accuracy alto y loss bajo".
>
> 9. **¿Qué significa definir `input_shape=(128, 128, 3)`?**
> * ✅ **Correcto:** "Significa que esperamos imágenes de entrada de 128 píxeles de alto, 128 de ancho, y `3` canales de color (Rojo, Verde, Azul - RGB). Si fuera escala de grises, el último número sería un `1`".
>
> 10. **¿Por qué dividimos en Train (80%) y Validation (20%)?**
> * ✅ **Correcto:** "Para simular un entorno del mundo real. Si evaluamos al modelo con las mismas fotos que usó para entrenar, siempre sacaría 100% por trampa de memorización. Validation nos dice la verdad sobre su capacidad de generalizar".
>
> 11. **¿Qué es un 'Batch Size' (Tamaño de Lote) de 8?**
> * ✅ **Correcto:** "Significa que la red no actualiza sus pesos foto por foto, sino que promedia el error después de ver 8 fotos a la vez. Esto ahorra memoria RAM frente a intentar cargar todo de golpe, y hace que el aprendizaje sea menos caótico".
>
> 12. **¿Qué es una 'Época' (Epoch) en entrenamiento?**
> * ✅ **Correcto:** "Una época se completa cuando la red neuronal ha pasado y procesado absolutalmente todas las imágenes de entrenamiento exactamente una vez. Entrenar por 15 épocas significa que leyó el 'libro completo' 15 veces".
>
> 13. **¿Por qué es necesario la capa `Flatten` antes de la capa `Dense`?**
> * ✅ **Correcto:** "Las capas Convolucionales pasan mapas 2D (imágenes). Pero las capas Densas clásicas (Fully Connected) solo entienden vectores 1D (una lista simple de números). `Flatten` 'aplasta' la matriz en una sola línea".
"Las capas Convolucionales (Conv2D) son excelentes para ver la imagen como un mapa 2D y encontrar patrones (como los bordes de un recibo). Sin embargo, para tomar la decisión final de clasificación, necesito un **'panel de jueces' (la capa Dense).** Como la capa Dense solo acepta datos en una sola dimensión (1D), uso Flatten para 'aplastar' ese mapa de características en una lista plana de números. Así, me aseguro de que el algoritmo asigne un peso matemático específico a cada característica detectada, dándome una probabilidad final (0 o 1) sin ambigüedades."

>
> 14. **En Keras, ¿qué optimizador recomendarías por defecto y por qué?**
> * ✅ **Correcto:** "El optimizador `adam`. Es muy popular porque ajusta su propia tasa de aprendizaje (Learning Rate) automáticamente a medida que entrena, siendo muy rápido y eficiente para arrancar proyectos frente a otros manuales como SGD". 

- "El optimizador `adam` es como un entrenador personal muy inteligente para la red. En lugar de ajustar la velocidad de aprendizaje (Learning Rate) de forma manual y rígida (como lo haría SGD), `adam` monitorea cómo se está equivocando la red en cada paso y ajusta esa velocidad automáticamente. Si está muy perdido, acelera; si está cerca de la respuesta correcta, frena. Esto lo hace extremadamente rápido para empezar y muy robusto para la mayoría de los problemas."

>
> 15. **¿Qué función de pérdida (loss function) usaste para tu Clasificación Binaria?**
> * ✅ **Correcto:** "`binary_crossentropy`. Mide matemáticamente la distancia entre nuestra predicción (ej. 0.9) y la respuesta real (ej. 1). Es la estándar obligatoria de la industria para resolver problemas de 2 clases con neurona de salida Sigmoid."

- "La función de pérdida (`binary_crossentropy`) es como el 'juez' que califica qué tan mal lo está haciendo la red. En un problema de clasificación binaria (como 'Recibo' o 'No Recibo'), la red da una probabilidad (ej. 0.9). Si la respuesta real era 1 (Recibo), el juez calcula la penalización. Si la red dijo 0.9, la penalización es baja (está cerca). Si hubiera dicho 0.2, la penalización sería altísima. El objetivo del entrenamiento es ajustar los pesos de la red para minimizar esa penalización (pérdida) en todas las fotos de entrenamiento."

>
> 16. **Si las imágenes fueran demasiado grandes (ej. 4K), ¿por qué no entrenar el modelo en ese tamaño?**
> * ✅ **Correcto:** "Colapsaría la memoria de la tarjeta gráfica (VRAM) u obligaría a tener un batch size muy pequeño. Además, la mayoría de los objetos (como un número o letras en un papel) son perfectamente reconocibles a resoluciones bajas como 128x128. Redimensionar prioriza velocidad y recursos."
>
> 17. **¿Qué son los 'Pesos' (Weights) en una red neuronal?**
> * ✅ **Correcto:** "Son literalmente los números que el modelo ajusta (multiplica) a medida que aprende. Si un píxel es irrelevante, el peso de esa conexión se vuelve casi cero. El objetivo de la red es encontrar los pesos matemáticos perfectos".
>


> 18. **¿Para qué sirve pre-cachear el dataset ( `dataset.cache().prefetch()` )?**
> * ✅ **Correcto:** "Cuello de botella I/O. La tarjeta de video calcula súper rápido, pero el disco duro lee lento. Poner las fotos en la memoria RAM (Caché) con un buffer (Prefetch) asegura que la GPU nunca esté de brazos cruzados esperando datos".
>



> 19. **Tu modelo sobreajusta (overfitting). Menciona dos herramientas en código para mitigarlo.**
> * ✅ **Correcto:** "1) Implementar la capa `tf.keras.layers.Dropout(0.5)` que apaga aleatoriamente el 50% de las neuronas para forzarlas a no depender de un solo camino. 2) Utilizar 'Data Augmentation' para engañar a la red generando nuevas vistas del mismo objeto".
>


> 20. **¿Por qué los parámetros 'No-Entrenables' de tu modelo están en 0?**
> * ✅ **Correcto:** "Porque construimos y entrenaremos el modelo completamente desde cero, así que la red tiene permiso de modificar toda su arquitectura. Verías esto en distinto a cero si estuviéramos aplicando Transfer Learning sobre un modelo ya hecho por otra empresa (ej. ResNet50)".



---

## Comandos MAC y mentales 
- sudo powermetrics --samplers gpu_power
- top -o cpu | grep -i "python"
- ls -lsh : visualiza el tamaño de los archivos
- lsof -i -P | grep LISTEN
- pip install -r requirements.txt


- python 001_Entrenamiento.py  => Entrenamiento 
- python 002_Mini_App.py => App con Gradio vemos la ejecución en el navegador