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

# Parte  1 Descripción del Dataset

- Nombre del Dataset: 'LifeExpectancyData.csv'.
- Fuente: Se extrajo el dataset de la plataforma Kaggle cuyo enlace publico se consigue en el siguiente enlace público  'https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who/suggestions'

- Hipótesis: Se desea predecir la esperanza de vida de México usando un dataset con información de otros países para el 2030. 

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
