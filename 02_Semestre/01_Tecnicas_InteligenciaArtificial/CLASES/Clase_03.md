# Primera Clase 
> 09 Mayo 2025 - Presencial - Grabada 

- Profesora: Adriana Cervantes Castillo 

# Resumen de Clase de IA: Técnica de Reglas 

Los sistemas basados en reglas son una de las metodologías más utilizadas para la representación del conocimiento. Se caracterizan por su capacidad de almacenar y procesar información en forma de reglas "Si-Entonces" (If-Then), lo que los hace ideales para la toma de decisiones y la automatización de procesos lógicos.


**Caracteristicas**
- Estamos hablando que nos topamos a diarios es buscar patrones y asociaciones en distintos 
- Los sistemas basados en reglas son senillos y facil de entender
- Existen reglas de clasifiacion y de asociacion 
- Son modulares ya que nos permiten tomar decisiones de manera facil 
- no todas las reglas son necesariamente son buenas
- quien define si una regla es buena o no lo define el dominio es es el conocimiento que tengas del mismo dominio 
- no se tiene que mezclarse las conjunciones y disyunciones
- Tenemos confianza en las reglas 
- Tenemos Soporte en las reglas 

## Guia de pasos 
- Cuando trabajamos con reglas primero es calcular el soporte 
- Pero tenemos la exepción que iniciar con soporte no nos puede decir mucho ya que necesitamos que la premisa para un soporte este ejecutandose ese patron frecuentemente tener mas mayor coincidencias 
- Calcular la confianza 


**Ventajas clave de los sistemas basados en reglas:**

- Modularidad: Permiten descomponer el conocimiento en reglas individuales y manejables. Esto facilita la adición, modificación o eliminación de reglas sin afectar otras partes del sistema.

- Separación entre control y conocimiento: Distinguen claramente entre el motor de inferencia (el "control" que aplica las reglas) y la base de conocimiento (las "reglas" mismas). Esto mejora la flexibilidad y el mantenimiento del sistema.

- Fácil de entender: La estructura de las reglas (Si [condición] Entonces [acción/conclusión]) es intuitiva y se asemeja al razonamiento humano, lo que las hace comprensibles incluso para no expertos.

- Gestión del conocimiento: Proveen un marco estructurado para organizar, almacenar y recuperar el conocimiento de un dominio específico, facilitando su administración y evolución.

- Toma de decisiones: Son altamente efectivos para modelar procesos de decisión, permitiendo al sistema llegar a conclusiones o ejecutar acciones basadas en las condiciones presentes.

**Como se hace**

Sintaxis básica:
Una regla fundamental se expresa como:
SI <antecedente>
ENTONCES <consecuente>

- Antecedente (Condición): Es la parte de la regla que establece una o más condiciones que deben ser verdaderas para que la regla se dispare. Piensa en esto como la "causa" o la "situación" que se evalúa.

- Consecuente (Acción/Conclusión): Es la parte de la regla que especifica la acción a realizar o la conclusión a la que se llega si el antecedente es verdadero. Es el "efecto" o la "consecuencia".
Ejemplo simple:
SI "hay sol"
ENTONCES "ir a la playa"

Reglas con conjunciones y disyunciones:
Las reglas pueden tener antecedentes más complejos que involucran múltiples condiciones.

- Conjunciones (AND): Significa que todas las condiciones en el antecedente deben ser verdaderas.
SI <antecedente 1>
AND <antecedente 2>
AND <antecedente 3>
ENTONCES <consecuente 1>
<consecuente 2>

En este caso, para que la regla se active y se produzcan los consecuentes 1 y 2, tanto el antecedente 1, como el antecedente 2, como el antecedente 3 deben ser verdaderos.

- Disyunciones (OR): No se muestra explícitamente en la imagen, pero funcionaría así: SI <antecedente A> OR <antecedente B> ENTONCES <consecuente>. Significa que al menos una de las condiciones debe ser verdadera.

Advertencia importante: La imagen menciona que "No es recomendable mezclar conjunciones y disyunciones en una sola regla." Esto se debe a que mezclar AND y OR en el mismo nivel sin paréntesis explícitos puede llevar a ambigüedades y hacer que la lógica de la regla sea difícil de entender y mantener. Es mejor dividir reglas complejas con AND y OR mixtos en reglas más simples o usar paréntesis para clarificar la precedencia, aunque generalmente se prefiere mantener la simplicidad.

## Reglas de Clasificación y de Asociación: Explicación Ampliada
 Dos tipos fundamentales de reglas utilizadas en el ámbito de la minería de datos y el aprendizaje automático: Reglas de Clasificación y Reglas de Asociación. Aunque ambas utilizan la estructura "SI... ENTONCES...", su propósito y aplicación son diferentes.

 1. Reglas de Clasificación
Definición de la imagen: "Las reglas de clasificación predicen la clase."

**Contexto ampliado:**

- Objetivo: El objetivo principal de las reglas de clasificación es asignar una etiqueta de clase predefinida a una nueva observación o dato. Es decir, buscan construir un modelo que pueda predecir a qué categoría o grupo pertenece un elemento.

- Estructura: Típicamente tienen la forma SI [condiciones sobre atributos] ENTONCES [pertenece a la Clase X]. El consecuente (la parte "ENTONCES") es siempre una de las clases posibles en el conjunto de datos.

- Entrenamiento: Se entrenan a partir de un conjunto de datos donde las clases ya son conocidas (datos etiquetados). El algoritmo aprende los patrones en los atributos que conducen a cada clase.

- Aplicaciones comunes:
Diagnóstico médico: SI [síntoma A] AND [síntoma B] ENTONCES [Diagnóstico: Gripe].

    - Clasificación de correos electrónicos: SI [contiene palabras "oferta" OR "gratis"] ENTONCES [Clase: Spam].

    - Aprobación de crédito: SI [ingresos > X] AND [deuda < Y] ENTONCES [Clase: Crédito Aprobado].

    - Evaluación: Su rendimiento se mide por métricas como la precisión, la exhaustividad, la puntuación F1 y la matriz de confusión, que evalúan qué tan bien predicen la clase correcta.

Relación con otros algoritmos: Son el resultado de algoritmos como C4.5, CART, máquinas de vectores de soporte (SVM) cuando se usan para clasificación, o incluso redes neuronales convolucionales (CNN) para clasificación de imágenes. Los árboles de decisión son una fuente muy común de reglas de clasificación.


2. Reglas de Asociación
Las reglas de asociación predicen valores de atributos, combinaciones de valores de atributos, o la propia clase." Y "El interés de las reglas de asociación es descubrir combinaciones de pares atributo-valor que ocurren con frecuencia en un conjunto de datos."

- Objetivo: El objetivo principal de las reglas de asociación es descubrir relaciones o dependencias interesantes y ocultas entre ítems (atributos y sus valores) en grandes conjuntos de datos. No buscan predecir una clase específica, sino encontrar qué ítems tienden a aparecer juntos.
Estructura: También tienen la forma SI [conjunto de ítems] ENTONCES [otro conjunto de ítems]. Los ítems pueden ser cualquier par atributo-valor (por ejemplo, "producto=leche", "día=martes", "método_pago=tarjeta").
Conceptos clave:

- Soporte (Support): Mide la frecuencia con la que aparecen juntos el antecedente y el consecuente en el conjunto de datos. Indica la popularidad de la regla.

- Confianza (Confidence): Mide la probabilidad de que el consecuente ocurra dado que el antecedente ha ocurrido. Indica la fiabilidad de la inferencia de la regla.

- Lift: Mide qué tan relevante es la asociación más allá de lo que se esperaría por azar. Un valor de Lift > 1 indica una asociación positiva.

- Algoritmos comunes: El algoritmo más conocido para generar reglas de asociación es Apriori. Otros incluyen Eclat y FP-Growth.
Aplicaciones comunes (Análisis de Cesta de la Compra - Market Basket Analysis):

- Recomendación de productos: SI [compra pañales] ENTONCES [probablemente compra toallitas húmedas]. (¡El clásico ejemplo de "cerveza y pañales"!)

-   Optimización de distribución en tiendas: Identificar qué productos deberían estar cerca unos de otros.

- Detección de fraudes: SI [transacción en país X] AND [cantidad > Y] ENTONCES [posiblemente fraudulento]. (Aquí la "clase" fraudulento podría ser el consecuente, mostrando cómo pueden superponerse en la predicción de clases).

- Análisis web: SI [visita página A] AND [visita página B] ENTONCES [probablemente visita página C].

- Enfoque: Se centran en encontrar patrones frecuentes y relaciones de co-ocurrencia, no necesariamente en predecir un resultado específico predefinido.


Estas dos métricas son fundamentales en el ámbito de las reglas de asociación (y a veces también en clasificación, aunque con matices) para determinar la "relevancia" y el "interés" de una regla descubierta en un conjunto de datos. No basta con que una regla sea lógicamente válida; debe ser estadísticamente significativa.

1. Confianza (Confidence)
"La confianza es la probabilidad condicional de que dado un evento A se produzca un evento B."

Fórmula (notación probabilística): Confianza(A→B)=P(B∣A)= 
P(A)P(A∩B)
​Donde:
A→B representa la regla "SI A ENTONCES B".
P(B∣A) es la probabilidad de que B ocurra dado que A ha ocurrido.
P(A∩B) es la probabilidad de que A y B ocurran juntos (la intersección).
P(A) es la probabilidad de que A ocurra.

Explicación en el contexto de reglas: "Al hablar de reglas, la confianza se puede expresar como el porcentaje de ejemplos que satisfacen el antecedente y consecuente de la regla entre aquellos que satisfacen el antecedente."

Imagina que tienes una regla: SI (compra Pan) ENTONCES (compra Leche).
Para calcular la confianza, contarías:
El número de transacciones donde se compra Pan Y Leche (esto es A∩B).
El número de transacciones donde solo se compra Pan (esto es A).
La confianza sería:  Número de transacciones con Pan Numero de transacciones con Pan y Leche
​
¿Qué mide? La confianza mide la fiabilidad o la precisión predictiva de la regla. Indica qué tan probable es que el consecuente sea verdadero si el antecedente es verdadero. Un valor de confianza alto sugiere que la implicación de la regla es fuerte. Por ejemplo, una confianza del 80% significa que en el 80% de los casos donde se cumple el antecedente, también se cumple el consecuente.

2. Soporte (Support)
"El soporte se refiere al cociente del número de ejemplos que cumplen el antecedente y el consecuente de la regla entre el número total de ejemplos."

Fórmula (notación probabilística): Soporte(A→B)=P(A∪B) (Nota: la imagen tiene un error aquí, debería ser P(A∩B), no P(A∪B))

Corrección: El soporte para una regla A→B se define como la probabilidad de que ambos el antecedente (A) y el consecuente (B) ocurran juntos en el conjunto de datos. Es decir, la frecuencia con la que la regla entera se cumple en todo el dataset.
La fórmula correcta debería ser: Soporte(A→B)=P(A∩B).

Explicación en el contexto de reglas:
Usando el mismo ejemplo SI (compra Pan) ENTONCES (compra Leche).
Para calcular el soporte, contarías:
El número de transacciones donde se compra Pan Y Leche (esto es A∩B).
El número total de transacciones en tu conjunto de datos.
El soporte sería:   Numero total de transacciones 
                    Numero de transacciones con Pan y Leche
​
 
¿Qué mide? El soporte mide la frecuencia o la popularidad de la regla en el conjunto de datos. Un soporte alto indica que la combinación de ítems en la regla (antecedente y consecuente juntos) aparece con mucha frecuencia en el dataset. Esto es crucial porque una regla con alta confianza pero bajo soporte podría ser estadísticamente insignificante (se cumple muy bien, pero en muy pocos casos).

Importancia conjunta de Confianza y Soporte
La última frase de la imagen es clave:

"Detectar aquellas reglas que, aunque se cumplen en algún caso y aunque puedan tener alta confianza, no son relevantes porque cubren casos poco frecuentes."

¿Por qué ambos son necesarios?

Imagina una regla SI (compra oro y diamantes) ENTONCES (compra yate). Podría tener una confianza del 100% (cada vez que alguien compra oro y diamantes, también compra un yate en tus datos). Sin embargo, si solo ha habido 2 transacciones en tu historial de miles donde alguien compró oro y diamantes, el soporte sería bajísimo. Esta regla es "confiable" pero no "relevante" porque se basa en una muestra minúscula y no representa un patrón generalizado.

Por otro lado, una regla con alto soporte pero baja confianza tampoco es útil. Por ejemplo, SI (compra pan) ENTONCES (compra cualquier cosa). El soporte de "pan y cualquier cosa" podría ser alto, pero la confianza sería baja si comprar pan no lleva de forma consistente a comprar algo específico.

Umbrales: En la minería de reglas de asociación (como con el algoritmo Apriori), se suelen definir umbrales mínimos de soporte y confianza para filtrar las reglas. Solo las reglas que superen ambos umbrales se consideran "interesantes" o "relevantes".


##  Que es el LIFT explicado con mis propias palabras 

- Es una tecnica que nos permite medir la relación entre un atencedente y un consecuente usando probabilidad, permite validar nuestras reglas su nivel de confianza o relación. 

**Validación LIFT**
1. Si Lift=1: El hecho A es independiente del hecho B, quiere decir que no impacta la información nueva tanto un antecendente como una consecuencia no tiene un impacto en la regla generada, 

2. Si Lift>1: Existe correlación positiva entre A y B. A y B tienden a ocurrir juntos. Es un caso de exito ya que es una relación util por lo que el hecho A aumenta en mucho que suceda el hecho B. 

3. Si Lift<1: Existe correlación negativa entre A y B. 
            A y B se comportan de forma opuesta, o A disminuye la probabilidad de B


## Algoritmo Apriori 
> Es una tecnica que podemos usar para generar reglas ya que genera conjuntos de item-set que podemos usar como un método de aprendizaje de reglas de asociación.


El algoritmo Apriori es un método de dos pasos para encontrar patrones interesantes en los datos, específicamente en forma de reglas de asociación:

- Primero: Encuentra los conjuntos de ítems que aparecen juntos con suficiente frecuencia (fase de ítem-sets frecuentes o "minería de conjuntos frecuentes").

- Segundo: A partir de esos conjuntos frecuentes, deriva reglas de tipo "SI... ENTONCES..." que son suficientemente fiables y potencialmente interesantes (fase de generación de reglas).

## Para que las usamos 
- Asociaciones entre artículos de la cesta de la compra
- Análisis de sentimiento en texto
- Diagnóstico médico a través de síntomas
- Conocer los hábitos de usuarios de un gran centro deportivo
- Asociaciones entre lugares visitados por turistas

## como hacemos esto Python 

# Pasos 

- Paso 1: 
> El algoritmo Apriori espera que los datos de entrada estén en un formato de codificación One-Hot (también conocido como formato "boolean sparse" o "dataframe disperso booleano"). Esto significa que cada columna representa un ítem único, y cada fila es una transacción.

- Paso 2: pip install mlxtend pandas

- Paso 3: Análisis Ejemplo 

Imagina que tienes una lista de listas, donde cada sublista representa una transacción y contiene los ítems comprados:

```Python
transactions = [
    ['leche', 'pan', 'mantequilla'],
    ['pan', 'mantequilla', 'cerveza', 'pañales'],
    ['leche', 'pan', 'cerveza', 'coca-cola'],
    ['leche', 'mantequilla', 'coca-cola'],
    ['pan', 'cerveza', 'pañales']
]
```

Transformar los datos a formato One-Hot

```Python

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

# Tus datos de transacciones
transactions = [
    ['leche', 'pan', 'mantequilla'],
    ['pan', 'mantequilla', 'cerveza', 'pañales'],
    ['leche', 'pan', 'cerveza', 'coca-cola'],
    ['leche', 'mantequilla', 'coca-cola'],
    ['pan', 'cerveza', 'pañales']
]

# Inicializar y ajustar el TransactionEncoder
te = TransactionEncoder()
te_array = te.fit(transactions).transform(transactions)

# Convertir el array resultante en un DataFrame de pandas
df_encoded = pd.DataFrame(te_array, columns=te.columns_)

print("DataFrame en formato One-Hot:")
print(df_encoded)


Salida del df_encoded:

DataFrame en formato One-Hot:
      cerveza  coca-cola   leche  mantequilla    pan  pañales
0     False      False    True         True   True    False
1      True      False   False         True   True     True
2      True       True    True        False   True    False
3     False       True    True         True  False    False
4      True      False   False        False   True     True

```
- Paso 3: Aplicar el algoritmo Apriori (Fase 1: Encontrar Itemsets Frecuentes)
> Ahora que los datos están en el formato correcto, puedes usar la función apriori de mlxtend. Necesitas especificar un min_support (soporte mínimo) como umbral.
```Python

from mlxtend.frequent_patterns import apriori

# Aplicar el algoritmo Apriori
# min_support: el umbral de soporte mínimo (ej. 0.5 significa que el itemset debe aparecer en al menos el 50% de las transacciones)
# use_colnames=True: para que el resultado use los nombres de los ítems en lugar de índices de columna
frequent_itemsets = apriori(df_encoded, min_support=0.5, use_colnames=True)

print("\nItemsets Frecuentes:")
print(frequent_itemsets)

Salida del frequent_itemsets:

Itemsets Frecuentes:
   support                 itemsets
0      0.6                 (cerveza)
1      0.6                   (leche)
2      0.6             (mantequilla)
3      0.8                     (pan)
4      0.6      (cerveza, pan)
5      0.6       (leche, mantequilla)

En este resultado:

support: Es el soporte del ítem-set (su frecuencia en las transacciones).
itemsets: Es el ítem-set en sí (un frozenset de Python).
```

- Paso 4: Generar Reglas de Asociación (Fase 2: Crear Reglas)
> Una vez que tienes los ítem-sets frecuentes, puedes usar la función association_rules de mlxtend para generar las reglas de asociación. Aquí necesitas especificar una métrica (por ejemplo, "confidence" o "lift") y un min_threshold (umbral mínimo para esa métrica).

```Python
from mlxtend.frequent_patterns import association_rules

# Generar reglas de asociación
# metric="confidence": Usaremos la confianza como métrica principal para filtrar reglas
# min_threshold=0.7: Solo reglas con una confianza del 70% o más
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

print("\nReglas de Asociación (basadas en confianza):")
print(rules)

Salida de las rules (ejemplo):

Reglas de Asociación (basadas en confianza):
  antecedents consequents  antecedent support  consequent support  support  confidence      lift  leverage  conviction
0   (cerveza)        (pan)                0.6                 0.8      0.6         1.0  1.250000       0.12        inf
1  (mantequilla)    (leche)                0.6                 0.6      0.6         1.0  1.666667       0.24        inf


Explicación de las columnas en el DataFrame de reglas:

antecedents: Los ítems en el "SI" de la regla.
consequents: Los ítems en el "ENTONCES" de la regla.
antecedent support: El soporte del antecedente (frecuencia de los ítems en el "SI").
consequent support: El soporte del consecuente (frecuencia de los ítems en el "ENTONCES").
support: El soporte de la regla completa (A∩B).
confidence: La confianza de la regla (P(B∣A)).
lift: El Lift de la regla (correlación).
leverage: Otra métrica que mide la diferencia entre la frecuencia observada de A y B juntos y la que se esperaría si fueran independientes. Un valor de 0 indica independencia.
conviction: Otra métrica que compara la probabilidad de que A aparezca sin B, si A y B fueran independientes.
```

- Paso 5: Filtrar y ordenar reglas
> Puedes filtrar y ordenar las reglas para encontrar las más interesantes. Por ejemplo, reglas con un alto lift (mayor que 1) y una alta confidence
```Python
# Filtrar reglas con lift > 1 y confianza > 0.8
strong_rules = rules[(rules['lift'] > 1) & (rules['confidence'] > 0.8)]

print("\nReglas de Asociación Fuertes (Lift > 1, Confianza > 0.8):")
print(strong_rules.sort_values(by="lift", ascending=False))

```


# Tabla Comparativa de Técnicas de Preprocesamiento de Datos

| Técnica                                 | Concepto                                                                                                         | ¿Cuándo usar?                                                                                                                                                                                                                                                                                                         | Ventajas                                                                                                  | Desventajas                                                                                                                                                                                                                                                                                                     |
| :-------------------------------------- | :--------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **I. Técnicas de Codificación de Variables Categóricas** |                                                                                                                  |                                                                                                                                                                                                                                                                                                                       |                                                                                                           |                                                                                                                                                                                                                                                                                                                   |
| **1. Codificación One-Hot** | Crea una nueva columna binaria (0 o 1) para cada categoría única en la variable original.                       | Cuando las categorías son **nominales** (sin orden) y el número de categorías no es excesivamente grande. Ideal para algoritmos que asumen independencia de características (ej., regresión lineal, SVM).                                                                                                              | Evita asumir un orden o relación numérica artificial. Fácil de entender. Compatible con la mayoría de los algoritmos. | Puede generar un gran número de columnas (alta dimensionalidad) si hay muchas categorías. Aumenta la complejidad computacional y de almacenamiento. |
| **2. Codificación Dummy** | Similar a One-Hot, pero crea `N-1` columnas para `N` categorías. Una categoría es la de referencia (inferida).  | Para evitar la **multicolinealidad perfecta** en modelos sensibles como la regresión lineal o logística, mientras se manejan categorías nominales.                                                                                                                                                                      | Resuelve el problema de multicolinealidad. Mantiene las ventajas de One-Hot para categorías nominales.   | Aún puede generar muchas columnas.                                                                                                                                                                                                                                                                    |
| **3. Codificación Ordinal** | Asigna un número entero a cada categoría basado en un orden predefinido por el usuario.                         | Cuando las categorías tienen un **orden intrínseco o jerarquía** (variables ordinales).                                                                                                                                                                                                                               | Reduce la dimensionalidad a una sola columna. Mantiene la información del orden si es significativo.    | Si las categorías no tienen un orden real, impone uno artificial que puede confundir al modelo (implicando distancias numéricas arbitrarias). |
| **4. LabelEncoder** | Asigna un valor numérico entero secuencial único a cada categoría única en la variable. (Es una forma de Codificación Ordinal arbitraria). | Principalmente para codificar la **variable objetivo (y)** en clasificación. También para características (X) si el número de categorías es pequeño y el algoritmo puede manejar el orden artificial (ej., árboles de decisión, Random Forest, GBT) o si hay un orden real. | Simple y fácil de usar. Reduce la dimensionalidad a una sola columna.                                     | Impone un orden numérico arbitrario a las categorías, lo que puede ser problemático para algoritmos que interpretan distancias (ej., K-NN, SVM, regresión lineal).                                                                                                                                     |
| **5. Codificación por Frecuencia/Conteo** | Reemplaza cada categoría con la frecuencia (o el conteo) de su aparición en el conjunto de datos.                  | Cuando la frecuencia de una categoría es un predictor potencialmente importante para el modelo. Para variables categóricas con alta cardinalidad.                                                                                                                                                              | Reduce la dimensionalidad a una sola columna. Captura información sobre la popularidad de la categoría.   | Categorías con la misma frecuencia reciben el mismo valor, perdiendo su distinción. No es útil si la frecuencia no es relevante para la predicción. |
| **6. Codificación por Media/Objetivo** | Reemplaza cada categoría con la media de la variable objetivo (o alguna otra estadística) para esa categoría.       | Para variables categóricas con **alta cardinalidad** en problemas de regresión o clasificación.                                                                                                                                                                                                                       | Reduce la dimensionalidad drásticamente. Captura información predictiva directamente de la variable objetivo. | Puede introducir *data leakage* (fuga de datos) si no se implementa cuidadosamente (usar solo datos de entrenamiento). Susceptible a *overfitting* en categorías con pocos ejemplos. Necesita técnicas de suavizado. |
| **7. Codificación Hash** | Transforma categorías en un espacio de dimensiones más bajas usando una función hash, mapeando a un índice fijo.     | Para variables con **cardinalidad muy alta** donde One-Hot no es factible. En escenarios donde la eficiencia computacional y de memoria son críticas.                                                                                                                                                            | Dimensionalidad fija y controlable. No requiere almacenar el mapeo. Puede manejar categorías nuevas.       | Posibilidad de **colisiones** (diferentes categorías mapeadas al mismo índice), lo que puede reducir el rendimiento. No es reversible.                                                                                                                                              |
| **8. Codificación Binaria** | Convierte categorías a números enteros, luego esos enteros a su representación binaria, creando una columna para cada bit. | Cuando el número de categorías es grande, pero no tan extremo como para necesitar hashing, buscando un compromiso entre One-Hot y Ordinal.                                                                                                                                                                    | Reduce la dimensionalidad en comparación con One-Hot.                                                     | Las nuevas columnas tienen una relación artificial que el modelo debe aprender. Menos interpretable que One-Hot.                                                                                                                                                                    |
| **II. Otras Técnicas de Preprocesamiento de Datos Relevantes** |                                                                                                                  |                                                                                                                                                                                                                                                                                                                       |                                                                                                           |                                                                                                                                                                                                                                                                                                                   |
| **1. Escalado de Características** | Ajusta la escala de las características numéricas para que tengan un rango similar.                                | Para algoritmos sensibles a la escala de las características (ej., K-NN, SVM, redes neuronales, regresión, clustering basado en distancia).                                                                                                                                                                          | Mejora el rendimiento y la estabilidad de muchos algoritmos. Acelera la convergencia de algoritmos basados en gradientes. | Puede dificultar la interpretabilidad directa de las características originales.                                                                                                                                                                                                    |
| **2. Manejo de Valores Faltantes** | Rellena los valores ausentes (NaN) en el conjunto de datos.                                                    | Siempre que haya valores faltantes en el dataset, ya que la mayoría de los algoritmos no pueden procesarlos directamente.                                                                                                                                                                                             | Permite usar el dataset completo sin eliminar filas o columnas.                                           | Una imputación incorrecta puede introducir sesgos o distorsiones en los datos. La elección del método de imputación es crucial.                                                                                                                                              |
| **3. Discretización / Binning** | Convierte variables numéricas continuas en categorías o "bins" (intervalos).                                      | Para algoritmos que prefieren datos categóricos o rangos (ej., algunas implementaciones de árboles de decisión, reglas de asociación para datos numéricos). Para reducir el ruido en datos continuos.                                                                                                             | Puede mejorar la robustez a los outliers. Permite usar técnicas de minería de reglas en datos continuos.   | Pérdida de información detallada de la variable numérica. La elección de los límites de los bins puede ser arbitrante o crítica.                                                                                                                                          |
| **4. Reducción de Dimensionalidad** | Reduce el número de características (columnas), conservando la mayor cantidad de información posible.             | Cuando hay un número excesivo de características (especialmente después de One-Hot Encoding), para combatir la "maldición de la dimensionalidad", reducir el tiempo de entrenamiento y mejorar el rendimiento.                                                                                                | Reduce la complejidad del modelo. Acelera el entrenamiento. Puede mejorar la interpretabilidad (si las componentes son claras). | Puede llevar a una pérdida de información (aunque se busca minimizarla). Las nuevas características (componentes) a menudo son menos interpretables que las originales.                                                                                                     |
| **5. Generación de Características (Feature Engineering)** | Crea nuevas características a partir de las existentes que pueden ayudar al modelo a aprender patrones.                      | Siempre que se pueda extraer información adicional relevante de los datos brutos que no sea directamente evidente para el modelo.                                                                                                                                                                           | Puede mejorar significativamente el rendimiento del modelo. Aporta conocimiento de dominio al proceso.   | Requiere creatividad, conocimiento del dominio y a menudo es un proceso iterativo y que consume mucho tiempo. Puede introducir *overfitting* si no se valida bien.                                                                                                        |


