# Primera Clase 
> 16 Mayo 2025 - Presencial - Grabada 

- Profesora: Adriana Cervantes Castillo

# Tema: Redes Neuronales 
**Caracteristicas**
- Inspiarda de la bilogia huamana
- trata de emular el funcionamiento del cerebro humamano pero aun sin conciencia
- son utilies una vez apredndiad la funcion obejtivo se puede usar facil despues
- El tiempo de entrenamiento es mucho mayor que arbol de decisiones
- Se considera de modelo de caja negra por lo dificil de seguir
- Es muy usada porque se adapta puede trabajar con datos ruidosos y tener buenos resultados
- Se usa en problemas complejos con mucha información o dificil de comprender. 

**Como funciona**
- se genera aprenizaje cuando las neuronas se conectan
- Generalmente son tres capas la capa de entrada, capa oculta, capa de salida
- Si no tienes dominio del problemas los Pesos de cada entrada se esocgen de manera aleatoria
- Cada neurona se le llama percetrón
- Internamente solo es una condicional llamada umbral que permite tomar la decisión basada de la cantidad total de entradas
  - Como inciamos:
      - Primero la creamos
      - Segundo la Compilación
      - Tercero la entrenamos
      - Cuarto la Optimizamos
- Flatten es una propiedad que aplasta las imagenes en vectores
- Dense: Nos indica el tipo de la densidad

**Referencias**
- https://www.youtube.com/watch?v=CU24iC3grq8&t=22s
- https://www.youtube.com/watch?v=iX on3VxZzk&t=250s
- https://www.youtube.com/watch?v=CU241C3grq8 https://www.youtube.com/watch?v=uM4u7P2xk08
- https://www.youtube.com/watch?v=ITH4mUc|DVk
- https://colab.research.google.com/drive/1EjxAt OFrdpNgCNmV15XMCE8RI3PF3sD?usp=sharIng#scrollTo=hzkGVPqnSvRE
- https://colab.research.google.com/drive/1GA2GnhpAIVO7|LV88|W1NgvAhflskh8q?hl=es
- https://keras-io.translate.goog/examples/vision/mnist_convnet/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr pto=tc

**Introducción a las Redes Neuronales**

Las redes neuronales son un modelo computacional inspirado en el funcionamiento del cerebro humano. Su bioinspiración radica en cómo las neuronas reciben estímulos, transmiten impulsos nerviosos y se conectan entre sí (sinapsis).

**Características y Ventajas:**

* Son adecuadas para resolver **problemas complejos**.
* El **tiempo de entrenamiento** de las redes neuronales puede ser largo.
* Una vez aprendida la función objetivo, la **evaluación de nuevas instancias es rápida**.
* Se comportan de manera **robusta frente al ruido**, lo que les permite ofrecer buenos resultados incluso si los ejemplos de entrenamiento contienen errores.

**Aprendizaje con Redes Neuronales:**

El objetivo del aprendizaje es ajustar la red neuronal para que, dado un **conjunto de datos de entrenamiento** (pares de entradas y salidas conocidas), las salidas de la red se ajusten lo mejor posible a las salidas esperadas.

Durante la formación de la red, los **pesos sinápticos** se asignan inicialmente de forma aleatoria. La diferencia entre la salida obtenida y la esperada se conoce como **error (o pérdida/costo)**, y este valor se utiliza para ajustar los pesos en cada iteración.

**Componentes clave que determinan el funcionamiento de una red neuronal:**

* **Arquitectura de la red:** Esto incluye el número de capas, el número de neuronas por capa y las conexiones entre neuronas de diferentes capas.
* **Función de activación:** Como la función signo o la función escalón, que determina la salida de una neurona.
* **Algoritmo de aprendizaje:** Principalmente la regla de aprendizaje para ajustar los pesos.

**Tipos de Perceptrones:**

* **Perceptrón simple:** Una unidad básica de una red neuronal que recibe múltiples señales de entrada ($x_1, x_2, \dots, x_n$), las multiplica por pesos sinápticos ($w_1, w_2, \dots, w_n$), suma estos productos y pasa el resultado a través de una función de activación para producir una salida ($y$).
* **Perceptrón multicapa:** Consiste en múltiples capas de neuronas, incluyendo una capa de entrada, una o varias capas intermedias (o capas ocultas) y una capa de salida. Las conexiones van en una dirección, formando una red hacia adelante.

**Cómo crear una Red Neuronal con TensorFlow y Keras en Python (Pasos):**

1.  **Creación (1- creación):**
    * Se importa `datasets`, `Sequential` de `tensorflow.keras` y `Flatten`, `Dense` de `tensorflow.keras.layers`.
    * Se inicializa un modelo secuencial (`modelo = Sequential()`).
    * Se añaden capas al modelo:
        * `Flatten(input_shape=(28,28))`: Aplana la entrada para que sea una única dimensión.
        * `Dense(128, activation = 'relu')`: Una capa densa con 128 neuronas y función de activación ReLU.
        * `Dense(10, activation = 'softmax')`: Una capa de salida con 10 neuronas (probablemente para 10 clases) y función de activación softmax.

2.  **Compilación (2 - compilación):**
    * Se configura el proceso de aprendizaje del modelo.
    * `modelo.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])`:
        * `optimizer='adam'`: El algoritmo de optimización para ajustar los pesos.
        * `loss='categorical_crossentropy'`: La función de pérdida para problemas de clasificación con múltiples clases.
        * `metrics=['accuracy']`: Métrica para evaluar el rendimiento del modelo durante el entrenamiento.

3.  **Entrenamiento (3 - entrenamiento):**
    * Se entrena el modelo con los datos.
    * `modelo.fit(x_train, y_train, epochs=10, verbose=1)`:
        * `x_train`, `y_train`: Datos de entrenamiento y sus etiquetas.
        * `epochs=10`: Número de veces que el modelo recorrerá todo el conjunto de datos de entrenamiento.
        * `verbose=1`: Muestra una barra de progreso durante el entrenamiento.

4.  **Predicción (4 - predicción):**
    * Una vez entrenado, el modelo puede hacer predicciones sobre nuevos datos.
    * `predicciones = modelo.predict(x_test)`: Realiza predicciones sobre el conjunto de datos de prueba (`x_test`).


