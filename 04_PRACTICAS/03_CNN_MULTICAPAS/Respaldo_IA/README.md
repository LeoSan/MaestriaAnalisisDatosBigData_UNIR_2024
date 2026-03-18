# Clasificador de Semáforos (Multiclase)

Este proyecto es una aplicación práctica para aprender sobre la clasificación **multiclase** utilizando Redes Neuronales Convolucionales (CNN) y la función de pérdida `categorical_crossentropy`.

## 1. Teoría y Conceptos Clave

### Clasificación Multiclase vs Binaria
A diferencia de la clasificación binaria (donde solo hay dos salidas posibles, por ejemplo: Perro o Gato, usando `binary_crossentropy` y una función de activación `sigmoid` al final), en la clasificación multiclase tenemos **tres o más categorías mutuamente excluyentes**. 

En nuestro caso, el semáforo solo puede estar en un estado a la vez:
1. Rojo
2. Amarillo
3. Verde
4. Apagado

### categorical_crossentropy
Es la función de pérdida estándar para problemas multiclase. Para usarla correctamente, las etiquetas de nuestro dataset deben estar codificadas en formato **"One-Hot Encoding"**.
- Ejemplo: Si tenemos 4 clases (Rojo, Amarillo, Verde, Apagado), la clase "Rojo" no será el número `0`, sino el arreglo `[1, 0, 0, 0]`. La clase "Verde" podría ser `[0, 0, 1, 0]`.

*(Nota: Si las etiquetas fueran números enteros normales como `0, 1, 2, 3`, se usaría `sparse_categorical_crossentropy` en su lugar).*

### Función de Activación Softmax
En la última capa de nuestro modelo multiclase, usaremos la activación `softmax`. Esta función toma las salidas sin normalizar de la red y las convierte en una **distribución de probabilidades** que suman 1.0. 
- Ejemplo de salida Softmax: `[0.85, 0.05, 0.08, 0.02]`. Esto nos dice que el modelo está 85% seguro de que la imagen pertenece a la primera clase.

---

## 2. Preguntas Frecuentes en Entrevistas (Tips)

**Q: ¿Cuál es la diferencia entre `sigmoid` y `softmax` en la capa de salida?**
**A:** `sigmoid` trata cada neurona de salida de forma independiente, aplastando su valor entre 0 y 1. Es útil para clasificación binaria o multietiqueta (donde una imagen puede tener varios objetos a la vez). `softmax` considera todas las salidas juntas y asegura que la suma de todas las probabilidades sea exactamente 1, lo cual es ideal para clasificación multiclase donde las clases son exclusivas.

**Q: ¿Cuándo usar `categorical_crossentropy` vs `sparse_categorical_crossentropy`?**
**A:** Matemáticamente hacen lo mismo, pero depende del formato de tus etiquetas (labels). Usas `categorical_crossentropy` cuando tus etiquetas están en formato one-hot (ej. `[0, 1, 0, 0]`). Usas `sparse_categorical_crossentropy` cuando tus etiquetas son números enteros (ej. `1`, `2`, `3`).

**Q: En un dataset con `label_mode='categorical'`, ¿cómo obtuve un error "only length-1 arrays can be converted to Python scalars" al graficar y cómo se soluciona?**
**A:** Porque las etiquetas ya no son un solo número (índice), sino un arreglo One-Hot (ej. `[0, 1, 0, 0]`). Al intentar pasar ese arreglo completo como índice válido de un array en Python, genera error. La solución es usar `tf.argmax(etiqueta)` (o `np.argmax()`) para extraer la posición del valor máximo (el 1), que corresponde al índice de la clase original.

**Q: En la construcción del modelo CNN (el cerebro), ¿cuántas capas de "aplanado" (`Flatten`) se necesitan y por qué?**
**A:** Normalmente se necesita **solo una** capa de aplanamiento o `Flatten()`. La función de esta capa es servir de "puente" entre la zona de extracción de características (las capas `Conv2D` y `MaxPooling2D` que trabajan con mapas en 2D/3D) y la zona de clasificación o razonamiento (las capas `Dense` que necesitan recibir los datos en un vector lineal o 1D). Una vez que el dato tridimensional se aplana, ya está listo para todas las capas Densas posteriores.

### Conceptos Fundamentales (Preguntas Extra para Perfiles Junior/Mid)

**Q: En la fase de preparación de datos, usamos `Rescaling(1./255)`. ¿Por qué es estrictamente necesario "normalizar" los píxeles de una imagen antes de dárselos a una Red Neuronal?**
**A:** Los colores de un píxel originalmente van de 0 a 255. Si metemos números tan grandes a una red neuronal, los cálculos matemáticos (multiplicación de matrices) explotan rápidamente, causando un error fatal llamado *Exploding Gradients* que impide aprender al modelo. Al dividir entre 255, aplastamos todos los valores a un rango de 0.0 a 1.0 (Normalización). Las redes neuronales, por su matemática interna, trabajan mil veces mejor, más rápido y más estable con números pequeños y consistentes.

**Q: Al cargar mis imágenes con Keras, le obligo a convertirlas todas a un `image_size=(128, 128)`. ¿Qué pasaría si le paso imágenes de distintos tamaños a mi modelo durante el entrenamiento?**
**A:** El modelo colapsaría con un error de dimensiones matematicas. Las capas Densas (`Dense`) al final de la red requieren estrictamente recibir un vector de un tamaño exacto y precalculado. Si las imágenes de entrada tienen tamaños diferentes (ej. una de 200x200 y otra de 50x50), el mapa aplanado resultante (`Flatten`) cambiaría de tamaño en cada foto, rompiendo la arquitectura matemática estática de la red. Una CNN estándar exige que todas las fotos tengan el mismo input_shape.

**Q: En palabras sencillas, ¿qué es exactamente lo que "aprende" la primera capa `Conv2D` a diferencia de las últimas capas `Conv2D` de una red profunda?**
**A:** Las capas convolucionales actúan como una "lupa" jerárquica. Las **primeras capas Conv2D** (cercanas a la imagen) aprenden a reconocer características sumamente básicas y locales: líneas rectas, curvas simples y bordes de contraste luz-oscuridad. En cambio, las **últimas capas Conv2D** (profundas en la red) toman esos "bordes" de las capas anteriores y los unen para reconocer conceptos complejos: una rueda, una cara completa o, en nuestro caso, el caparazón protector alrededor del círculo de un semáforo.

**Q: Después de una capa convolucional, normalmente ponemos una capa `MaxPooling2D`. ¿Cuál es su utilidad vital en la arquitectura?**
**A:** Tiene dos misiones críticas. 1) **Ahorrar Memoria (Downsampling):** Reduce el tamaño espacial de la imagen a la mitad reteniendo solo los píxeles "más brillantes o importantes" (el valor máximo), mitigando drásticamente el costo computacional para las siguientes capas. 2) **Invarianza a la Traslación:** Le enseña al modelo que un semáforo "rojo" sigue siendo rojo sin importar si el círculo luminoso está un centímetro más arriba, más abajo, a la izquierda o derecha dentro de la foto.

**Q: Finalmente, cuando ejecutamos `modelo.save('mi_modelo.keras')`, ¿qué es exactamente lo que se guarda dentro de ese archivo mágico que pesa varios megas?**
**A:** Ese archivo guarda tres cosas esenciales para evitar que un modelo en producción tenga que entrenarse de cero:
1. **La Arquitectura (El Plano):** Cuántas capas hay, cuántas neuronas y de qué tipo (Conv2D, Dense, etc.).
2. **Los Pesos y Sesgos (El Cerebro/Recuerdos):** Los miles (o millones) de numeritos flotantes que la red ajustó internamente en cada época tras equivocarse y autocorregirse para aprender qué es un semáforo.
3. **El Estado del Optimizador (La Memoria de Cómputo):** Guarda con qué *Learning Rate* (velocidad de aprendizaje) se quedó el optimizador (ej. Adam), por si el día de mañana decides cargar el modelo y seguir entrenándolo con nuevas imágenes desde donde lo dejaste.

### Sobre One-Hot Encoding (OHE)

**Q: ¿Qué es exactamente el "One-Hot Encoding" en el contexto de las redes neuronales?**
**A:** Es una técnica para convertir datos categóricos (como colores, tipos de animales, nombres de frutas) en un formato numérico que el modelo pueda procesar matemáticamente sin asumir un orden. En nuestro caso, en lugar de decirle al modelo que "Apagado" es `0` y "Rojo" es `1` (lo que haría creer al modelo equivocadamente que "Rojo" es matemáticamente mayor o el doble que "Apagado"), se usa un arreglo de ceros donde solo la posición que representa la clase real contiene un `1` (ej. `[1, 0, 0, 0]`).

**Q: ¿Por qué NO es buena idea usar números enteros (1, 2, 3...) para clasificar clases independientes como rojo, amarillo y verde?**
**A:** Porque las redes neuronales son optimizadores matemáticos. Si usas valores ordinales (enteros regulares) para categorías nominales (sin orden jerárquico real), el modelo intentará encontrar relaciones matemáticas donde no existen. Podría llegar a la conclusión errónea de que la clase `2` (Verde) está "en medio" de la clase `1` y la clase `3`, o calcular un promedio y predecir `1.5` que no representa ninguna clase. El One-Hot Encoding soluciona esto aislando cada clase en su propia "dimensión" (columna).

**Q: Si tengo 10 clases diferentes en mi proyecto en lugar de 4, ¿cómo afectaría esto al tamaño de mi representación One-Hot y a la capa final de mi red?**
**A:** Tu arreglo One-Hot ya no tendría 4 elementos, sino 10 (nueve ceros y un uno). En consecuencia directa, la última capa `Dense` de tu modelo necesitaría obligatoriamente configurarse con **10 neuronas** `layers.Dense(10, activation='softmax')`, para que cada neurona especializada arroje la probabilidad individual correspondiente a esa posición específica del arreglo OHE.

### Sobre la Compilación del Modelo (`model.compile`)

**Q: En la configuración `optimizer='adam'`, ¿qué función cumple exactamente el optimizador en el entrenamiento neuronal y por qué *Adam* es tan popular?**
**A:** El optimizador es el motor del aprendizaje. Su trabajo es ajustar los "pesos" y "sesgos" (las conexiones) de las neuronas basándose en el error que calcula la función de pérdida (`loss`). *Adam* (Adaptive Moment Estimation) es muy popular en entrevistas y proyectos porque es un optimizador inteligente: ajusta automáticamente el tamaño del paso (learning rate) para cada parámetro individualmente, lo que hace que el modelo converja (aprenda) mucho más rápido y de manera más estable que con optimizadores tradicionales como SGD.

**Q: ¿Por qué es necesario definir `metrics=['accuracy']` si ya le dijimos al modelo que evalúe su error usando `loss='categorical_crossentropy'`?**
**A:** Es una excelente pregunta para diferenciar conceptos. La función de pérdida (`loss`) es el valor matemático complejo que el Optimizador usa para ajustar la red internamente (el gradiente), suele ser un número difícil de interpretar humanamente (ej. 0.345). En cambio, la métrica (`accuracy`) es **solo para que nosotros (los humanos) evaluemos** el rendimiento de manera intuitiva. Al optimizador NO le importa el accuracy, solo le importa reducir el loss. El accuracy nos dice simplemente: "de 100 fotos, le atinó a 95" (95%).

**Q: Si fueras a cambiar este código que hace "Clasificación Multiclase" para que haga un proyecto de "Regresión" (por ejemplo, predecir el precio en dólares de una casa), ¿qué cambiarías en el `model.compile(...)`?**
**A:** ¡Esa es la pregunta de oro! Cambiaría todo el bloque: 
1. La función de pérdida ya no puede ser `categorical_crossentropy` (eso cuenta categorías). Para predecir un valor continuo se usa `loss='mse'` (Error Cuadrático Medio). 
2. La métrica ya no sería `accuracy` (precisión), ya que es casi imposible "atinar" al centavo exacto del precio. Usaría métricas como `mae` (Error Absoluto Medio) para saber por cuántos dólares en promedio se equivoca el modelo.

### Sobre el Entrenamiento del Modelo (`model.fit`)

**Q: En la función `model.fit`, ¿cuál es la diferencia conceptual entre `epochs` y `batch_size`?**
**A:** Un `epoch` (época) es un ciclo completo donde la red neuronal logra ver **absolutamente todas las imágenes** del dataset de entrenamiento al menos una vez. Sin embargo, procesar todas las imágenes al mismo tiempo saturaría la memoria de la tarjeta de video (GPU). Para evitarlo, usamos el `batch_size` (ej. 32), que define cuántas imágenes se procesan a la vez antes de que el Optimizador actualice temporalmente los "pesos". Si tienes 320 imágenes dadas a la IA en 1 época, ocurren 10 "mini-actualizaciones" consecutivas de 32 imágenes cada una.

**Q: ¿Por qué le pasamos a la función `fit` explícitamente el parámetro `validation_data` en lugar de dejar que el modelo entrene y evaluar todo al final?**
**A:** Porque queremos "monitorear" el aprendizaje de la IA en tiempo real, de época en época, simulando exámenes que la IA nunca ha visto para detectar problemas *antes* de que termine el entrenamiento completo. Le pasamos `validation_data` para que nos arroje un `val_loss` y `val_accuracy` periódico. Esto nos permite detectar el famoso **Overfitting** en el acto (ej. detectamos que en la época 5 el error de validación empezó a subir en lugar de bajar).

**Q: ¿Qué guarda exactamente la variable `historial = model.fit(...)` y para qué sirve en un entorno profesional?**
**A:** La variable `historial` *no* guarda la red neuronal inteligente (el "cerebro" actualizado ya vive en tu variable `modelo`). Lo que guarda es un objeto tipo diccionario (accesible usando `historial.history`) que contiene el registro épico-por-épico de cómo evolucionaron tus métricas (loss, accuracy, val_loss, val_accuracy). En un entorno profesional, este historial se usa con librerías como `Matplotlib` para **graficar curvas de aprendizaje**, las cuales son cruciales en reportes de ciencia de datos para demostrar visualmente si el modelo realmente aprendió o si necesita arquitecturas diferentes.

### Sobre la Evaluación del Modelo (`model.evaluate`)

**Q: ¿Para qué sirve exactamente `modelo.evaluate()` si el modelo ya nos dio un `val_accuracy` y un `val_loss` durante el entrenamiento (`model.fit`)?**
**A:** En proyectos simples o de práctica (como nuestro script actual), usar `dataset_validacion` tanto en el `fit()` como en el `evaluate()` es una forma rápida de ver el resultado final por pantalla. Sin embargo, en el mundo real profesional, **esto es una mala práctica**. El `evaluate()` debe usarse EXCLUSIVAMENTE con un tercer conjunto de datos llamado **Test Set** (Conjunto de Prueba), el cual la IA jamás ha visto, ni siquiera para calcular el `val_loss` durante el entrenamiento. `evaluate()` es el "Examen Final Definitivo" que dictamina si tu modelo sirve para salir a producción web o no.

**Q: ¿Qué valores devuelve la función `modelo.evaluate()` y en qué orden lo hace?**
**A:** Devuelve una lista de números. El primer valor SIEMPRE es el valor escalar de la función de pérdida matemática (`loss`, en nuestro caso *categorical_crossentropy*). Los valores que le siguen corresponden exactamente a las métricas humanas que le definiste previamente en `model.compile(metrics=[...])` (en nuestro caso, solo pusimos *accuracy*). Por eso podemos desempaquetar la tupla limpiamente haciendo: `perdida, precision = modelo.evaluate(...)`.

**Q: Si obtengo un alto `accuracy` en el entrenamiento (`model.fit`), pero `modelo.evaluate(dataset_test_nuevo)` arroja un `precision` bajísimo, ¿cómo llamamos médicamente a este problema en IA?**
**A:** Se diagnostica como un caso clásico y terminal de **Overfitting**. Tu modelo aprendió a memorizar el dataset de entrenamiento (se hizo "experto local"), pero no entendió las características universales de los semáforos, volviéndose inútil frente a fotos que ligeramente escapan a su set de memoria.

### Sobre Overfitting y Resultados (Evaluación)

**Q: Al terminar de entrenar obtuve un `accuracy` de 1.0000 (100%) pero un `val_accuracy` de 0.7500 (75%) y, peor aún, mi `loss` bajó casi a 0 pero mi `val_loss` subió muchísimo (ej. 2.84). ¿Qué significa esto?**
**A:** Significa que tu modelo sufrió de **Overfitting (Sobreajuste)** severo. El modelo se "memorizó" perfectamente las imágenes de estudio (por eso el acierto perfecto del 100% en `accuracy`) pero no aprendió a generalizar los conceptos subyacentes. Cuando se enfrentó a imágenes nuevas en el examen sorpresa (`val_accuracy`), falló en 1 de cada 4 fotos, y su "inseguridad" o error matemático al intentar predecirlas (`val_loss`) se disparó.

**Q: ¿Cómo se puede combatir el Overfitting en una CNN para evitar que el `val_loss` se dispare?**
**A:** Hay varias estrategias clásicas:
1. **Data Augmentation:** Rotar, hacer zoom o voltear ligeramente las imágenes de entrenamiento para que el modelo nunca vea la misma imagen exacta dos veces.
2. **Dropout:** "Apagar" aleatoriamente un porcentaje de neuronas durante el entrenamiento (ej. `layers.Dropout(0.5)`) para obligar al resto a aprender características más robustas y no volverse perezosas o codependientes.
3. **Early Stopping:** Programar a TensorFlow para que detenga el entrenamiento automáticamente en cuanto el `val_loss` empiece a subir en lugar de bajar.
4. **Más datos:** Simplemente, ¡conseguir más fotos de semáforos!

### Sobre los Límites del Dataset y Transfer Learning

**Q: Si implementé *Data Augmentation* (rotación, flip horizontal, zoom) y mi modelo aún falla estrepitosamente al ver un semáforo con un fondo distinto al de mi dataset (ej. un cielo azul de día en vez de una estructura de noche), ¿es un problema de código?**
**A:** No, es el "Muro de la Escasez de Datos". El Data Augmentation es increíble para exprimir un dataset mediano, pero no es magia generativa. Si tu modelo aprendió a identificar semáforos *exclusivamente* con fondos nocturnos oscuros (porque así eran todas tus 40 fotos originales), por más que TensorFlow rote o haga zoom a esas 40 fotos oscuras en la memoria, el modelo **nunca** aprenderá a reconocer y abstraer un cielo azul radiante al mediodía. Su limitado "mundo" de entrenamiento nunca incluyó ese concepto.

**Q: En el mundo real profesional, ¿qué hacemos si solo tenemos 100 fotos disponibles pero necesitamos que un modelo clasifique imágenes complejas sin sobreajustarse?**
**A:** Usamos la técnica suprema: **Transfer Learning** (Aprendizaje de Transferencia). En lugar de empezar a entrenar nuestro pequeño "cerebro" (CNN) desde cero (pesos aleatorios ciegos), descargamos el cerebro de un modelo titánico hiper-entrenado y famoso (como ResNet50, MobileNet, VGG16) creado por Google o Microsoft.

**Q: ¿Cómo funciona exactamente el Transfer Learning a nivel código y arquitectura?**
**A:** Las CNN grandes están entrenadas con millones de fotos durante semanas (el famoso dataset ImageNet de 1,000 categorías). Ese modelo ya "sabe" identificar bordes, el concepto de "cielo azul", texturas metálicas, autos y perros. En Transfer Learning, tomamos ese modelo gigante y **le congelamos todas sus capas** (los "ojos"). Luego le **cortamos su última capa original** (la que predecía 1,000 cosas) y le insertamos nuestra propia y pequeña capa "Dense(4, activation='softmax')" para nuestros 4 semáforos. De esta manera, solo entrenamos esa última capa que se aprovecha de la tremenda capacidad visual que ya trae el modelo grande. Con apenas 100 fotos, podemos lograr precisiones superiores al 95%.

---

## 3. Pasos del Proyecto (El Recetario)

*Iremos marcando y documentando los pasos conforme avancemos.*

1. [x] **Preparación del Dataset**: Cargar las imágenes desde las carpetas y dividirlas en entrenamiento y validación.
2. [x] **Construcción del Modelo**: Crear la arquitectura CNN usando activaciones y funciones de pérdida adecuadas para multiclase.
3. [x] **Entrenamiento y Evaluación**: Entrenar el modelo y verificar que no haya *overfitting*.
4. [x] **Interfaz con Gradio**: Crear la mini-app para subir imágenes y ver la predicción en tiempo real.


## Comandos MAC y mentales 
- sudo powermetrics --samplers gpu_power
- top -o cpu | grep -i "python"
- ls -lsh : visualiza el tamaño de los archivos
- lsof -i -P | grep LISTEN
- pip install -r requirements.txt
- zip -r Respaldo_IA.zip . -x "venv/*" : Crea un archivo comprimido de todo el directorio ignorando la pesada carpeta del entorno virtual.

- python 001_Entrenamiento.py  => Entrenamiento 
- python 002_Mini_App.py => App con Gradio vemos la ejecución en el navegador