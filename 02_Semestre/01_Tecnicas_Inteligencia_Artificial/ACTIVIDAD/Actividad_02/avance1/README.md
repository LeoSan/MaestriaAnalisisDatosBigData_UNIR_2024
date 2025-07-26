# Pasos para la actividad Avance Version 1 

## Configuracion 
- Creamos nuestro entorno  con el siguiente comandi ´python3 -m venv <nombre>´
- luego activamos ´source ./nombreEntorno/bin/activate´
- Instalamos librerias 
    - pip install pandas
    - pip install seabron
    - pip install scikit-learn
    - pip install tensorflow 


## Iniciamos avance 
    - Buscamos un dataset para aplicar los conocimientos 
    - creamos un archivo llamado main.py que contendra el script 
    - activamos entorno asi -> ´source ./avance2/bin/activate´
    - Ejecutamos así ´python3 main.py´ estando en el directorio -> ~/Documents/Dev/python/maestria


# PARTE TECNICA PARA SOLVENTAR **Actividad de Regresión (Apartado A)**

- Nombre del Dataset: 'LifeExpectancyData.csv'.
- Fuente: Se extrajo el dataset de la plataforma Kaggle cuyo enlace publico se consigue en el siguiente enlace público  '[https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who/suggestions](https://www.kaggle.com/code/qusaybtoush1990/students-adaptability-accuracy-91-4/notebook)'

- Hipótesis: Se desea predecir la esperanza de vida de un conjunto de datos generales,  usando un dataset con información de otros países para el 2030. 

- Contexto: Se tomaran las siguientes variables para validar la hipotesis y aplicar el conocimiento adquirido durante las clases las variables son: 

    - Adult Mortality (Mortalidad Adulta): Es una de las variables más directamente relacionadas con la esperanza de vida Menor mortalidad adulta debería implicar mayor esperanza de vida.

    - infant deaths (Muertes Infantiles): Similar a la mortalidad adulta, una reducción en las muertes infantiles contribuye directamente al aumento de la esperanza de vida de una población.

    - Schooling (Escolaridad): Un mayor nivel de escolaridad suele correlacionarse con una mayor conciencia sobre la salud, mejores trabajos, ingresos y acceso a atención médica, lo que se traduce en mayor esperanza de vida. 

    - GDP (Producto Interno Bruto): Representa la salud económica de un país. Un PIB más alto generalmente implica mejores infraestructuras de salud, nutrición y condiciones de vida.

    - HIV/AIDS (VIH/SIDA): La prevalencia de enfermedades crónicas y pandemias tiene un impacto directo y negativo en la esperanza de vida. Esta variable captura un aspecto importante de la salud pública.

    - Income composition of resources (Composición de los recursos de ingresos): Esta variable suele ser un índice que combina GNI per cápita, años de escolaridad y esperanza de vida. tomamos esta variables como un buen indicador compuesto del desarrollo humano y es probable que tenga una fuerte correlación con la esperanza de vida.

    - Year: Por ultima variables pero no menos importante el año esto nos ayudará en establecer la predicción para años a futuros. 

    - Country (Pais): El total de paises que se realizó el estudio previo. 

    - Status: 

- Variables Clave: (Life expectancy) consideramos esta variable numérica continua y es el objetivo de la predicción, lo que la hace la variable de salida perfecta para un problema de regresión y nos apoya para resolver la problemática de estudio.
 
- Técnicas de Preprocesamiento de Datos: Usaremos 'Codificación One-Hot'
Porque validando las variables nos encontramos con categiorias nominales y el número de categorias no es muy grande y el OneHotEncoder para las variables categóricas, que es lo más adecuado para este caso, y cómo manejar las variables numéricas sin aplicarles codificación inapropiada.Consideramos que el dataset LifeExpectancyData.csv las variables que típicamente serían categóricas y se beneficiarían del One-Hot Encoding son 'Country' y 'Status'. Las demás variables que se mencionan como ('Adult Mortality', 'infant deaths', 'Schooling', 'GDP', 'HIV/AIDS', 'Income composition of resources', 'Year', y 'Life expectancy') son numéricas y deben tratarse como tal, posiblemente con escalado si es necesario para el modelo, pero no con codificación que altere su significado numérico.

## Variables clave que vamos a caracterizar:

- Variable Objetivo (Target): life_expectancy

- Variables Numéricas (Features): adult_mortality, infant_deaths, alcohol, percentage_expenditure, hepatitis_b, measles, bmi, under_five_deaths, polio, total_expenditure, diphtheria, hiv/aids, gdp, population, thinness__1_19_years, thinness_5_9_years, income_composition_of_resources, schooling, year.

- Variables Categóricas (Features): country, status

## Definición de Graficas 
Se discución con el equipo y se usó las siguientes graficas por su amplia demostración de los datos: 

a) Histogramas para Variables Numéricas:
Muestran la distribución de una sola variable. Nos ayudó a ver si la distribución es normal, sesgada, bimodal, Para life_expectancy entre otras características numéricas importantes: GDP, Schooling, Adult Mortality, HIV/AIDS, etc.

b) Diagramas de Dispersión (Scatter Plots) para Relaciones  Numéricas:
Nos mostró la visualización y la relación entre dos variables numéricas. fue excelente ya que nos permitió identificar correlaciones, tendencias y posibles valores atípicos.

Comparación 
- life_expectancy vs. GDP: ¿Mayor PIB significa mayor esperanza de vida?
- life_expectancy vs. Schooling: ¿Más años de escolaridad se relacionan con mayor esperanza de vida?
- life_expectancy vs. Adult Mortality: ¿Mayor mortalidad adulta se relaciona con menor esperanza de vida? (esperaríamos una correlación negativa).
- life_expectancy vs. HIV/AIDS: ¿Relación con la prevalencia de VIH/SIDA?

c) Diagramas de Cajas y Bigotes (Box Plots):
Nos permitió visualizar la distribución de una variable numérica en función de una variable categórica. Muestra la mediana, los cuartiles y la presencia de valores atípicos.

Comparación 
- life_expectancy por Status (Developing/Developed): ¿Hay diferencias claras en la esperanza de vida entre países desarrollados y en desarrollo?

d) Mapa de Calor de Correlación (Heatmap):
Nos permitió ver la representación visual de la matriz de correlación, haciendo que sea muy fácil identificar relaciones fuertes (positivas o negativas) en un par de vistazos.

Consideramos estas como las mas utiles y faciles de comprender y de desarrollar, sabemos que existe una gran variedad de graficas y de extender mas la comprensión de la data, debemos nosotros como futuros analistas ampliar nuestra experiencia y adquirir mas criterios de analisis y de curiosidad para mejorar en este mundo de la big data. 

## Modelo de Regresión No Neuronal:

Para este caso usaremos el random forest regression por ser muy robusto y versátil para tareas de regresión, tomando en cuenta sus ventajas muy claras como **Alta Precisión**, Tiende a producir resultados muy precisos, especialmente en datasets complejos con relaciones no lineales. **Manejo de Multicolinealidad**  nos permite tener menos sensibilidad a la multicolinealidad entre características en comparación con la regresión lineal, **Robustez a Outliers** es bastante robusto a los valores atípicos (outliers) y al ruido en los datos, **Manejo de Datos Faltantes** lo bueno de esta ventaja es que si tenemos una gestión para datos imputados, los árboles de decisión que componen el **Random Forest** pueden manejar bien algunos tipos de datos con patrones de valores faltantes, aunque ya los estemos imputamos, es una ventaja general del método. 


## Modelo de Red Neuronal Secuencial usando Keras tensior Flow:


Para este caso usaremos un modelo **Sequential** ya que Es el tipo de modelo más simple de Keras, donde las capas se apilan una tras otra.
se describe a continuación la composición de los parametros de entrada para el modelo: 
- keras.Input(shape=input_shape): Define la forma esperada de los datos de entrada. input_shape se calcula automáticamente como (X_train_final.shape[1],), lo que significa el número de columnas (características) de tus datos preprocesados.
- layers.Dense(64, activation='relu', name='hidden_layer_1'): La primera capa densa (fully connected) con 64 neuronas. relu es la función de activación. 
- layers.Dense(32, activation='relu', name='hidden_layer_2'): La segunda capa densa con 32 neuronas, también usando relu.
- layers.Dense(1, activation='linear', name='output_layer'): La capa de salida. Tiene 1 neurona (porque es una regresión de una sola salida) y linear como función de activación, permitiendo cualquier valor real como predicción.

Para su complilación se usaron los siguientes valores: 

- optimizer='adam': Es el algoritmo que nos permite una optimización que ajustará los pesos de la red. Adam es un optimizador eficiente y popular que se adapta bien a diferentes problemas por eso fue escogido. 

- loss='mse': La función que nos permite evaluar la pérdida para la regresión, nos permite medir el error Cuadrático Medio (MSE) es el  estándar por lo que NO necesitamos reinventar la rueda el objetivo es simple es minimizar esta pérdida durante el entrenamiento.

- metrics=['mae']: Se señade una métrica adicional para observar durante el entrenamiento. El Error Absoluto Medio (MAE) es más fácil de interpretar que el MSE permitieno crear una evaluación y seguimiento ams detallado.

Para su entrenamiento usaremos lo siguiente: 

- X_train_final, y_train: Los datos que el modelo se usó paso por las normalizaciones recurentes durante la preparación del modelo no neuronal, ya que para las redes neuronales, es altamente recomendable escalar las características numéricas para que todas estén en un rango similar (ej. entre 0 y 1, o con media 0 y desviación estándar 1). Esto ayuda al proceso de optimización de la red y previene que características con rangos más grandes dominen el cálculo de la pérdida, duanrente el **preprocessor_model** se uso **passthrough** para lograr que los datos numéricos esten estandarizados (media 0, varianza 1) antes de entrar a la red neuronal.

- epochs=100: El número de pasadas completas a través del conjunto de datos de entrenamiento. Más épocas pueden mejorar el modelo, pero también pueden llevar a sobreajuste si son demasiadas se uso el valor de 100 considerando que es lo mas aproiado. 

- batch_size=32: El número de muestras que se usarán para calcular el gradiente y actualizar los pesos del modelo en cada iteración.

- validation_split=0.2: Keras separará el 20% de X_train_final y y_train para usarlos como un conjunto de validación. Esto es crucial para monitorear el rendimiento del modelo en datos "no vistos" durante el entrenamiento y detectar si está sobreajustando el conjunto de entrenamiento.

 Evaluación del Modelo 

Para la evalución de nuestro modelo de red neuronal comienza utilizando el método **model_nn.evaluate()** sobre el conjunto de datos de prueba **(X_test_final y y_test)** Esta función nos proporciona rápidamente dos métricas clave **uno** la pérdida del modelo (en este caso, el Error Cuadrático Medio o MSE) y el Error Absoluto Medio (MAE). Estos valores nos dan una indicación directa del rendimiento del modelo en datos que nunca se ha visto, ayudándonos a comprender cuán precisas son sus predicciones en promedio.

Ahora para obtener métricas adicionales como el **R2 Score y el RMSE**, es necesario primero generar las predicciones del modelo sobre el conjunto de prueba. Esto se logra con **model_nn.predict(X_test_final)**. Es importante destacar que la salida de **predict()** es un array 2D con una sola columna **(n_samples, 1),** por lo que aplicamos **.flatten()** para convertirlo en un array 1D. Esta conversión es fundamental, ya que funciones de métricas como r2_score esperan que tanto los valores reales (y_test) como las predicciones (y_pred_nn) tengan la misma forma unidimensional.

Por ultimo las predicciones transformadas y los valores reales del conjunto de prueba, se calcularón manualmente el **R2 Score y el RMSE**. Estas métricas complementan el MSE y el MAE, ofreciendo una visión más completa del desempeño del modelo. El R2 Score, en particular, nos indica qué proporción de la varianza en la esperanza de vida es explicada por nuestro modelo, mientras que el RMSE nos da una medida del error en la misma escala que la variable objetivo, permitiendo una comparación directa con los resultados obtenidos del modelo Random Forest.


# PARTE TECNICA PARA SOLVENTAR **Actividad de Clasificación (Apartado B)**

- Nombre del Dataset: 'students_adaptability_level_online_education.csv'.
- Fuente: Se extrajo el dataset de la plataforma Kaggle cuyo enlace publico se consigue en el siguiente enlace público  'https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who/suggestions'

- Hipótesis: Es una dataset para iniciar en este campo del modelado y entrenamientos de analisis de datos  partiremos de esta hipotesis
  - "¿Es posible predecir el nivel de adaptabilidad de un estudiante al aprendizaje online (Bajo, Moderado, Alto) basándose en sus características demográficas, educativas, económicas y tecnológicas?" 

- Context:  Se tomaran las siguientes variables para validar la hipotesis y aplicar el conocimiento adquirido durante las clases las variables son:



