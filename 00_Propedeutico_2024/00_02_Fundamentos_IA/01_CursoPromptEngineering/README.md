# Curso de Prompt Engineering

## Clase 1: Conceptos Clave para Entender los LLMs en Prompt Engineering

¿Qué es exactamente un LLM?
Imagínate una biblioteca gigantesca que contiene absolutamente todo lo que se ha escrito en la humanidad. Ahora imagina esta biblioteca con una mente propia, capaz de entender significativamente el contenido. Esto es precisamente un LLM o modelo grande de lenguaje, una herramienta que aunque no tiene conciencia, posee la impresionante habilidad de predecir la siguiente palabra o frase con gran precisión.


## Clase 2:  Vectores y Embeddings en Modelos de Lenguaje

- Comprensión de LLMs
    - Comparación con buscar un libro en una biblioteca
    - Transformación de palabras en relaciones y características
- Ejemplo de la palabra "motivar"
    - Contexto deportivo y su clasificación
    - Análisis de sentimientos y usos
- Concepto de vectores
    - Definición y aplicación en diversas dimensiones
    - Ejemplos en la vida diaria
- Embeddings y dimensiones n-dimensionales
    - Dificultad de imaginar más de tres dimensiones
    - Ejemplos de evaluaciones en restaurantes y direcciones
- Similitud semántica y su rol en LLMs
    - Ejemplo con "aguacate" y "avocado"
    - Importancia de la elección de palabras

## Clase 4: Atención y Contexto en Modelos de Lenguaje Natural 

🧪 Ejercicio de Priming

🧠 Activación automática e inconsciente por estímulos previos
🎯 Ejemplo: pensar en un vegetal tras operaciones matemáticas
🤖 Atención en modelos LLM

🔍 Asigna pesos a palabras
📏 Predice respuestas considerando relevancia contextual
📱 Diferencias con autocorrectores

📲 Autocorrector: solo considera la palabra anterior
🤯 LLM: considera todo el contexto (tus palabras y las del modelo)
🪟 Ventana de contexto

📚 Capacidad de procesar hasta 128,000 tokens (~160 páginas)
🔄 El modelo puede priorizar partes recientes de la conversación
🧭 Relevancia de las palabras

🐱 Ejemplo: “gato” tiene más contexto que “el”
🧩 Ayuda a predecir de forma más precisa
🎯 Técnicas de prompting (en futuras clases)

🧲 Redirigir la atención del modelo
🛠️ Personalizar y mejorar respuestas

## El Mecanismo de Atención 
Es la capacidad del modelo de enfocarse en los tokens/embeddings más relevantes del input, lograda mediante la comparación matemática de sus vectores (Embeddings) dentro del Espacio N-Dimensional. Esto le permite entender el contexto y es fundamental para su funcionamiento y aparente "razonamiento".

## ¿Cómo se relaciona con los conceptos anteriores (Tokens, Embeddings, Espacio N-Dimensional)?

- Opera sobre Tokens y sus Embeddings: El mecanismo de atención no trabaja directamente con las palabras o el texto crudo. Trabaja con las representaciones numéricas de los tokens: ¡los Embeddings (Vectores)!

- Compara Embeddings en el Espacio N-Dimensional: El "prestar atención" del modelo se logra comparando los Embeddings de los diferentes tokens en el ``Espacio N-Dimensional. El mecanismo calcula una especie de "puntuación de relevancia" o "similitud" entre el embedding del token actual que está procesando y los embeddings de todos los otros tokens en la ventana de contexto. Estas puntuaciones se derivan de operaciones matemáticas realizadas con los vectores en el espacio N-dimensional (como calcular cuán "alineados" están).

El Resultado Ayuda a Entender el Contexto (Llevando a Embeddings Contextualizados): Basándose en estas puntuaciones de relevancia, el mecanismo de atención pesa la importancia de los embeddings de los otros tokens. El resultado final de este proceso de atención**** es una nueva representación (a menudo, un tipo de embedding contextualizado) para el token actual, que ahora incluye información combinada de los tokens más relevantes de su contexto.

Pensemos en la Analogía del Cocinero de nuevo:
Ahora el cocinero no solo corta bien los ingredientes (Tokenización) y sabe qué "sabor" tiene cada uno individualmente (Embeddings base), sino que también sabe que para hacer un buen plato, debe prestarle más atención a cómo interactúan ciertos sabores (el Mecanismo de Atención prestando atención a cómo interactúan ciertos embeddings/tokens). Sabe que la cebolla y el ajo son muy relevantes para el sabor de la mayoría de los sofritos, y les presta más "atención" al combinarlos.

