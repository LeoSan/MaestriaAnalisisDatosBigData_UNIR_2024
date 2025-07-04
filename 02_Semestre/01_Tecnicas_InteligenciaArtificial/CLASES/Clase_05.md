# Primera Clase 
> 30 Junio 2025 - Presencial 

- Profesora: Adriana Cervantes Castillo

Claro que sí. La imagen muestra una tabla de contenido con cinco tipos de redes neuronales. Te explicaré cada una de ellas de una manera sencilla para que las recuerdes fácilmente:

---

## Contenido: Tipos de Redes Neuronales

### 1. Redes Prealimentadas (Feedforward Neural Networks)

* **Imagina un camino de una sola dirección:** Piensa en la información como un río que fluye desde una fuente (la entrada) hacia un destino final (la salida). En las redes prealimentadas, los datos viajan en una única dirección, sin retroceder ni formar ciclos.
* **Capas de información:** El río pasa por diferentes "estaciones de peaje" (capas ocultas) antes de llegar a su destino. Cada estación procesa la información y la pasa a la siguiente.
* **¿Para qué sirven?** Son las redes neuronales más básicas y se usan para tareas como:
    * **Clasificación:** Decidir si una imagen es de un perro o un gato.
    * **Regresión:** Predecir el precio de una casa.
* **Recuerdo fácil:** "Prealimentadas" porque la información se **pre-alimenta** hacia adelante.

### 2. Redes Neuronales Recurrentes (Recurrent Neural Networks - RNNs)

* **Imagina un cerebro con memoria:** A diferencia del río de una sola dirección, las RNNs tienen la capacidad de recordar lo que ha pasado antes. Piensa en alguien que está leyendo un libro; para entender la frase actual, necesita recordar las frases anteriores.
* **Bucles internos:** Tienen un "bucle de memoria" que les permite tomar decisiones basadas no solo en la entrada actual, sino también en las entradas pasadas.
* **¿Para qué sirven?** Son ideales para datos secuenciales, donde el orden importa:
    * **Procesamiento de Lenguaje Natural (PLN):** Traducir idiomas, completar texto (como tu teclado).
    * **Reconocimiento de voz:** Entender lo que dices.
    * **Generación de música:** Crear secuencias musicales.
* **Recuerdo fácil:** "Recurrentes" porque la información **re-circula** dentro de la red, como un recuerdo.

### 3. Redes Autoencoders (Autoencoders)

* **Imagina un "artista" que comprime y descomprime:** Piensa en un autoencoder como un artista que primero toma una imagen y la reduce a su "esencia" o las características más importantes (codificación), y luego intenta reconstruirla lo más parecido posible a la original a partir de esa esencia (decodificación).
* **Dos partes principales:**
    * **Codificador:** Comprime la información de entrada en una representación más pequeña y densa.
    * **Decodificador:** Descomprime esa representación para recrear la entrada original.
* **¿Para qué sirven?** Principalmente para:
    * **Reducción de dimensionalidad:** Simplificar datos complejos.
    * **Detección de anomalías:** Encontrar cosas "raras" o fuera de lo común (como un billete falso).
    * **Eliminación de ruido en imágenes:** Limpiar fotos borrosas.
* **Recuerdo fácil:** "Autoencoder" porque se **auto-codifican** y **auto-decodifican** a sí mismas.

### 4. Redes Neuronales Convolucionales (Convolutional Neural Networks - CNNs)

* **Imagina un "ojo" que busca patrones específicos:** Piensa en las CNNs como un detective con una lupa, que busca características específicas en una imagen (bordes, texturas, formas). No ven la imagen completa de una vez, sino que se enfocan en pequeñas partes.
* **Filtros (convoluciones):** Usan "filtros" o "máscaras" que se deslizan sobre la imagen para detectar estos patrones. Cada filtro es como un pequeño detector de una característica particular.
* **¿Para qué sirven?** Son el "rey" para el procesamiento de imágenes:
    * **Reconocimiento de imágenes:** Identificar objetos, personas o escenas en fotos.
    * **Clasificación de imágenes:** Decir si una imagen es de un perro, un gato, etc.
    * **Visión por computadora:** En coches autónomos, reconocimiento facial.
* **Recuerdo fácil:** "Convolucionales" porque usan **convoluciones** (esos filtros deslizantes) para ver la imagen.

### 5. Redes Generativas Antagónicas (Generative Adversarial Networks - GANs)

* **Imagina dos artistas rivales:** Piensa en dos artistas:
    * **El Generador (falsificador):** Intenta crear algo tan real que engañe al otro artista (por ejemplo, una imagen de una persona que no existe).
    * **El Discriminador (detective):** Intenta distinguir entre lo que es real y lo que el Generador creó (lo "falso").
* **Juego de "gato y ratón":** Ambos se entrenan al mismo tiempo. El Generador mejora para crear cosas más realistas, y el Discriminador mejora para detectar mejor las falsificaciones.
* **¿Para qué sirven?** Son asombrosas para generar contenido nuevo y realista:
    * **Creación de imágenes realistas:** Rostros de personas que no existen, paisajes, objetos.
    * **Transferencia de estilo:** Hacer que una foto parezca una pintura de Van Gogh.
    * **Generación de datos sintéticos:** Crear datos para entrenar otros modelos.
* **Recuerdo fácil:** "Generativas" porque **generan** cosas nuevas. "Antagónicas" porque hay una **antagonía** (rivalidad) entre el generador y el discriminador.
