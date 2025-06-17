# Técnicas de Inteligencia Artificial

# Temario 1: Introducción a la IA 

## Resumen del Diagrama: Descubrimiento del Conocimiento y Aprendizaje Automático

La imagen presenta un diagrama que ilustra dos conceptos principales interrelacionados: **Descubrimiento del Conocimiento en Bases de Datos (KDD)** y el **Aprendizaje Automático (Machine Learning)**.

**Descubrimiento del Conocimiento en Bases de Datos (KDD):**

## Pasos 
- Paso 1: Recopilamos información 
- Paso 2: 

Este proceso se describe como una secuencia de pasos que transforma datos brutos en conocimiento útil. Las etapas son:

1.  **Datos:** Se inicia con una base de datos (BD) como fuente de información.
2.  **Selección:** Se eligen los datos relevantes para el objetivo del descubrimiento.
3.  **Pre-procesamiento:** Los datos seleccionados se limpian y preparan para el análisis.
4.  **Transformación:** Los datos pre-procesados se transforman a un formato adecuado para la minería de datos.
5.  **Minería de Datos:** Se aplican técnicas de aprendizaje automático para extraer patrones y descubrir conocimiento valioso a partir de grandes cantidades de datos.
6.  **Interpretación y Evaluación de Resultados:** Los patrones descubiertos se interpretan y evalúan para determinar su utilidad y relevancia.
7.  **Conocimiento:** El resultado final es el conocimiento extraído de los datos.

**Aprendizaje Automático (Machine Learning):**

El aprendizaje automático se presenta como un subcampo de la **Inteligencia Artificial (IA)** y el **Aprendizaje Automático (Automático)**.

* **Inteligencia Artificial (IA):** Se define como la ciencia que estudia la creación de agentes computacionales que, basándose en unos estímulos externos y un conocimiento almacenado, producen acciones que maximizan su rendimiento. Se mencionan áreas como la Robótica, Sistemas Expertos y el Procesamiento del Lenguaje Natural.

* **Aprendizaje Automático (Automático):** Se describe como una rama de la IA que se dedica a la construcción de programas computacionales que automáticamente mejoran su rendimiento en una tarea determinada con la experiencia.

    * **Elementos que intervienen en el aprendizaje automático:**
        * **Clase (concepto que se aprende)**
        * **Instancias con sus atributos**
        * **Ejemplos y no ejemplos (datos de entrenamiento)**

    * **Tipos de Aprendizaje Automático:**
        * **Aprendizaje Supervisado:** Se basa en la descripción de un concepto o clase a partir de datos etiquetados. 
        * **Aprendizaje No Supervisado:** Busca la formación de un nuevo concepto (clase desconocida) a partir de datos sin etiquetas.
        * **Aprendizaje Visto como Búsqueda de Hipótesis (bias y sobreajuste):** Se enfoca en la búsqueda del mejor modelo o hipótesis a partir de los datos, considerando el sesgo y el riesgo de sobreajuste.

**Relación entre KDD y Aprendizaje Automático:**

El diagrama muestra que la **Minería de Datos** dentro del proceso de KDD **utiliza** técnicas de **Aprendizaje Automático** para descubrir patrones y extraer conocimiento de los datos. Por lo tanto, el aprendizaje automático es una herramienta fundamental dentro del proceso más amplio de descubrimiento del conocimiento.

## 1.2. Aproximación a los conceptos de inteligencia artificial, aprendizaje automático y minería de datos. Interés y aplicaciones


> Lengua Española de la Real Academia Española podemos
- «Disciplina científica que se ocupa de crear programas informáticos que ejecutan operaciones comparables a las que realiza la mente humana, como el aprendizaje o el razonamiento lógico».

- El objetivo de la IA, desde el punto de vista de la investigación y de la ciencia, es
comprender los principios que hacen posible el comportamiento inteligente en
sistemas artificiales. Para ello, se deben analizar agentes naturales y artificiales,
formular y testear hipótesis sobre lo que implica construir un sistema artificial que
realice tareas que requieren inteligencia, así como diseñar y desarrollar el sistema
inteligente empírico, esto es, experimentando y comprobando las distintas hipótesis
planteadas (Poole & Mackworth, 2010).

- Alan Turing con título «Computing machinery and intelligence» publicado en el año 1950 (Turing, 1950). 
    - Principio : Turing propone un juego de imitación en el que un juez humano debe interrogar a otro humano y a un ordenador remotamente y conseguir adivinar quién es el ordenador de sus dos interlocutores. 



## Inteligencia artificial
Es una rama de la informática que estudia la creación de agentes computacionales que reciben estímulos externos y en base a ellos y a un conocimiento almacenado en dicho agente, producen resultados o acciones que maximizan una medida de rendimiento. El conocimiento almacenado puede ser aprendido por el mismo agente utilizando técnicas de aprendizaje automático o puede ser incorporado por un humano experto en el dominio específico.


## Minería de datos
Es un proceso que utiliza técnicas de inteligencia artificial sobre grandes cantidades de datos con el objetivo de descubrir y describir patrones en los datos, a partir de los cuales se pueda obtener un beneficio.

## Aprendizaje automático, 
Es una rama de la IA, se refiere a la construcción de programas computacionales que automáticamente mejoran su rendimiento en una
tarea determinada con la experiencia.


## 1.3. Definición de aprendizaje, tareas básicas y ejemplos


La siguiente frase define el aprendizaje por parte de un ordenador:
Un programa de ordenador aprende de la experiencia E con respecto a
una clase de tareas T y una medida de rendimiento P, si su rendimiento
en las tareas T, medido en base a la medida P, mejora con la
experiencia E. (Mitchell, 1997).
Para ilustrar esta definición y los elementos E, P y T, se exponen a continuación
algunos ejemplos de tareas de aprendizaje:
Ejemplo 1: Aprender a detectar robos de tarjetas de crédito.
T: detectar robos de tarjetas de crédito.
P: porcentaje de robos detectados.
E: base de datos de hábitos de compra con la tarjeta de crédito.
Ejemplo 2: Aprender a reconocer la escritura manual.
T: reconocer y clasificar palabras escritas en imágenes.
P: porcentaje de palabras correctamente clasificadas.
E: base de datos de imágenes de palabras manuscritas clasificadas.
Ejemplo 3: Aprender a aparcar un coche utilizando sensores de visión.
T: aparcar un coche utilizando sensores de visión.
P: porcentaje de aparcamientos correctos.
E: secuencias de imágenes y comandos de guiados registrados.


## ¿Qué contenidos se pueden aprender?
De acuerdo con la teoría de instrucción de Merril denominada «Teoría de
presentación de componentes», «Component display theory» (Merril et al., 1994), las
personas pueden aprender cuatro tipos de contenido:

- Hechos: simples afirmaciones de una verdad, que puede ser una asociación entre
una fecha y un hecho, o un nombre y un objeto.

- Conceptos: conjunto de objetos, símbolos o eventos agrupados porque comparten
ciertas características y que pueden ser referenciados por un nombre en particular o
un símbolo. Los objetos existen en el espacio y tiempo como puede ser una persona,
una mesa; los símbolos se refieren a tipos de palabras, números, marcas, como
puede ser un predicado o una fracción; los eventos son interacciones específicas de
objetos en un periodo de tiempo como puede ser la digestión o la fotosíntesis.

- Procedimientos: conjunto de acciones realizadas en pasos consecutivos para
alcanzar un objetivo.

- Principios: relaciones causa-efecto, verdades generales o leyes básicas para
afirmar otras verdades.

## ¿Qué elementos intervienen en el aprendizaje de un concepto?

Una instancia es una ilustración específica de un objeto, símbolo, evento, proceso o
procedimiento

## ¿En qué consiste aprender un concepto?

página 19 


# Aprendizaje Supervizado
- Tiene etiquetas
    - Regresión 
    - Clasificación 

# Aprendizaje NO Supervizado
- NO Tiene etiquetas
    - Agrupación  
    - Detención de anomalías  
    
## 1.4. Etapas en el descubrimiento de conocimiento

# Temario 2: Python para la implementación de técnicas de inteligencia artificial

## 2.3. El lenguaje Python: conceptos básicos e instalación
 - Fue creado por Guido van Rossum
 - Lanzado en 1991 
 - Tiene su nombre por un comediante Monty Python
 - Multiplataforma 
 - Es un lenguaje interpretado no compilado 
 - Multiparadigma
    - Programación orientada a objetos,
    - Programación imperativa
    - programación procedural,
    - Programación funcional, basado en el cálculo lambda
- Maneja dos tipos de tipado
    - Fuertemente tipado
    - De tipado dinámico

## Instalación 
-  con estos comando en Linux podemos instalarlo 
```bash
sudo apt-get update
sudo apt-get install python
sudo apt-get install pip
```


## 2.4. La sintaxis de Python

## Indentación y comentarios
> A diferencia de otros lenguajes, en los cuales no es importante y solo se hace por legibilidad del código, en Python es importante el sangrado (indentación) a la hora de definir los distintos bloques de ejecución. Hemos de usar siempre el mismo nivel de sangrado para cada bloque y el deshacerlo hace que se cierre dicho bloque.

## Variables, tipos de datos y casting
- En Python no es necesario declarar una variable (a diferencia de lenguajes de tipado
estático como C/C++)
- Esta se crea en el momento de utilizarla por primera vez,
momento en el cual se define su tipo, que además puede cambiar con el tiempo con
una nueva asignación de la variable a un tipo nuevo
- Python son case-sensitive (debemos respetar uso de mayúsculas y minúsculas)
- pueden contener letras, números y el carácter de subrayado, pero no pueden comenzar por un número
- Por defecto, una variable definida fuera de una función es global, y cuando es
definida dentro de una función es local, a no ser que utilicemos la palabra clave global
 para modificar este comportamiento. Una variable global puede ser empleada desde
cualquier punto del programa, pero una variable local solo puede ser empleada
dentro de la función que la define.

## Tipos de Variables 
- Texto      -> str 
- Númericos  -> int, float, complex
- Secuencias -> list, tuple, range
- Mapas      -> dict 
- Conjuntos  -> set, frozenset
- Booleanos  -> bool 
- Binarios   -> bytes, bytarray, memoryview 

## Cadenas

- Las cadenas funcionan como el resto de los arrays en cuanto a que son iterables y
cada elemento es accesible mediante el uso de corchetes. Cada elemento es un
carácter Unicode, pero no existe un tipo char como en otros lenguajes. Un carácter
es una cadena de tamaño 1. 

- Podemos acceder a los elementos de la cadena de forma selectiva. 

## Operadores
> En Python existen los siguientes tipos de operadores (que nos interesen):
- Aritméticos.
- Asignación.
- Comparación.
- Lógicos.
- Identidad.
- Membresía.


## 2.5. Listas, tuplas, conjuntos y diccionarios

## Listas
- Las listas son colecciones de objetos ordenadas y modificables. 
- Se escriben utilizando corchetes con los elementos separados por comas. 
- Podemos acceder a los diferentes elementos empleando el operador corchete y acceder a un rango de
elementos, al igual que hacíamos con las cadenas. 
- Asimismo, podemos utilizar la función len() y el método append() para añadir nuevos elementos.


## Tuplas
- Las tuplas son colecciones ordenadas pero inmutables, es decir, no podemos alterar
su valor. 
- Las tuplas funcionan de forma muy similar a las listas a la hora de acceder a
sus elementos, iterarlas, comprobar si un elemento se encuentra en ellas, etc. 
- Sin embargo, no podemos añadir o eliminar elementos o modificar el valor de uno de sus
elementos. 
- Para hacer esto, tendríamos que copiar su valore en una lista, realizar las
modificaciones y asignar su contenido completo a la tupla original.

## Conjuntos
- Los conjuntos (set) son colecciones de datos no ordenadas y que no permiten
elementos duplicados. 
- Es decir, no podemos predecir en qué orden se mostrarán
(print) o iterarán sus elementos (for … in). 
- De hecho, cada vez que realicemos una ejecución de este tipo el orden puede ser distinto. 
- Tampoco podemos utilizar el operador corchete para acceder a un elemento determinado, puesto que no tienen orden alguno. 
- No pueden contener dos elementos con el mismo valor.
- Una vez que creamos un conjunto, no podemos alterar el valor de uno de sus
elementos. Lo que sí podemos hacer es añadir nuevos elementos o eliminar los
existentes

## Diccionarios
- Los diccionarios son el equivalente a mapas o hashes en otros lenguajes de
programación. 
- Son un conjunto de elementos clave-valor sin orden y en los cuales se
puede modificar el contenido de los elementos. 
- Son también similares a los objetos nativos de JavaScript que pueden ser convertidos a y desde JSON. Sin embargo son mucho más flexibles y una clave no tiene por qué ser sólo de tipo cadena, sino que puede ser cualquier objeto, incluso un entero, un flotante o un complejo, por

## 2.6. Librerías útiles para el análisis de datos
> NumPy 
Es una librería muy popular para el procesamiento de grandes matrices y
matrices multidimensionales, con la ayuda de una gran colección de funciones
matemáticas de alto nivel. Es muy útil para los cálculos científicos fundamentales en
machine learning. Es particularmente útil para el álgebra lineal, la transformación de
Fourier y las capacidades de números aleatorios. Otras librerías de alto nivel como
TensorFlow utilizan NumPy internamente para la manipulación de tensores

> SciPy
Es una biblioteca muy popular entre los ingenieros de machine learning, ya que
contiene diferentes módulos para la optimización, el álgebra lineal, la integración y la
estadística. Hay una diferencia entre la biblioteca de SciPy y la pila de SciPy (SciPy
stack). La librería SciPy es uno de los paquetes centrales que componen la pila de
SciPy. SciPy también es muy útil para la manipulación de imágenes.

> Scikit-learn.
Es una de las librerías de machine learning más populares para los
algoritmos de machine learning clásico. Está construida sobre dos bibliotecas
básicas de Python, NumPy y SciPy. Scikit-learn soporta la mayoría de los algoritmos
de aprendizaje supervisado y no supervisado

> Theano.
El machine learning es básicamente matemáticas y estadística. Theano es una
popular librería que se utiliza para definir, evaluar y optimizar las expresiones
matemáticas que implican conjuntos multidimensionales de manera eficiente. 

Se consigue optimizando la utilización de la CPU y la GPU. Se utiliza ampliamente para
pruebas unitarias y autoverificación para detectar y diagnosticar diferentes tipos de
errores. Theano es una biblioteca muy potente que se ha utilizado en proyectos
científicos de gran escala e intensivos en computación durante mucho tiempo, pero
es lo suficientemente sencilla y accesible para que pequeños desarrolladores la
utilicen en sus propios proyectos.

> Keras.
Es una de las librerías de Machine Learning más populares para Python. Es
una API de redes neuronales de alto nivel capaz de funcionar sobre TensorFlow,
CNTK, o Theano. Puede funcionar sin problemas en la CPU y la GPU. Keras permite
que sea realmente sencillo construir y diseñar redes neuronales para los
principiantes en el machine learning. Una de las mejores características de Keras es
que permite la creación de prototipos de forma fácil y rápida.

> TensorFlow.
TensorFlow es una biblioteca de código abierto muy popular para el cálculo numérico
de alto rendimiento, desarrollada por el equipo de Google Brain en Google. Como su
nombre lo sugiere, TensorFlow es un marco de trabajo que implica la definición y ejecución de cálculos que implican tensores.

> PyTorch
Es otra de las librerías más populares de machine learning de código abierto
para Python basada en Torch, que es una biblioteca de machine learning de código
abierto que se implementa en C con un wrapper en Lua. Tiene una extensa selección
de herramientas y librerías que incluye visión artificial (Computer Vision) o
Procesamiento de Lenguaje Natural (NLP), entre otros. Permite a los desarrolladores
realizar cálculos tensoriales con aceleración en la GPU y también es de ayuda en la

> Pandas.
Pandas es una popular librería de Python para el análisis de datos. No está
directamente relacionada con el machine learning. Como sabemos, los dataset han
ser preparados antes del entrenamiento. En este caso, Pandas es muy útil, ya que
fue desarrollada específicamente para la extracción y preparación de datos.
Proporciona estructuras de datos de alto nivel y una amplia variedad de herramientas
para el análisis de datos. Asimismo, proporciona muchos métodos incorporados para
tantear, combinar y filtrar datos. 

> Matplotlib.
Es una biblioteca de Python muy popular para la visualización de datos. Al
igual que Pandas, no está directamente relacionada con el machine learning. Es
particularmente útil cuando un programador quiere visualizar los patrones de los
datos. Es una librería de ploteo en 2D usada para crear gráficos y diagramas en 2D.


## 2.7. La librería NumPy para el manejo de datos

## Conceptos básicos y arrays en NumPy

Tal y como hemos visto, la librería NumPy nos permite trabajar con arrays de forma
muy eficiente, así como álgebra lineal, transformadas de Fourier y matrices. Aunque
Python dispone de listas que permiten trabajar con arrays, estas son muy lentas.

NumPy proporciona arrays 50 veces más rápidos, en parte porque los elementos
están todos almacenados en posiciones contiguas de memoria y en parte porque
parte de NumPy está escrita en C/C++

Podemos trabajar con escalares, vectores, matrices, arrays tridimensionales o
cualquier otra dimensión diferente. El método ndim nos permite obtener la dimensión
del array, mientras que con el operador corchete podemos acceder a los diferentes
elementos según los índices en cada dimensión

## Array Slicing

Al igual que con los tipos built-in datos (cadenas, listas, etc.), en los arrays NumPy se
puede hacer un slicing de los arrays utilizando notación de corchetes y dos puntos,
pero, con mucha mayor flexibilidad:

## Tipos de datos en NumPy
NumPy nos permite especificar con mucho mayor detalle los tipos de datos de los
elementos en nuestros arrays:
- i – integer
- b – boolean
- u - unsigned integer
- f – float
- c - complex float
- m – timedelta
- M – datetime
- O – object
- S – string
- U - unicode string
- V - chunk o trozo de memoria para otro tipo de dato ( void )

- En los tipos de datos i, u, f, S, U podemos especificar el tamaño en bytes, además.
- Esto se especifica con la propiedad dtype:
- Si un valor no puede ser convertido, se lanzará una excepción de tipo ValueError.
- Si queremos convertir el tipo de datos de un array existente, usaremos el método 

## Copy y view
La principal diferencia entre una copia (obtenida con el método copy() ) y una vista
(obtenida con el método view() ) de un array NumPy es que la copia es un nuevo
array, mientras que la vista es una vista, valga la redundancia, del array original. Es similar al concepto de asignación por referencia o de clonado de los datos en Python

## La forma (shape) de un array
Con el atributo shape podemos obtener una tupla indicando en cada índica el
número de elementos en cada dimensión. Si hemos definido una dimensión mínima
con ndmin en la creación del array, esta será una forma de visualizarlo. El método
reshape() nos permite redimensionar un array (cambios entre 1-D y 2-D o 3D). Dicho
método devuelve una vista, no una copia. Con reshape(-1) podemos aplanar un
array multidimensional en un array unidimensiona

## Operaciones con varios arrays
Podemos concatenar arrays uno a continuación del otro con concatenate(),
especificando sobre qué eje (si no se especifica, se considerará el eje 0):

## Búsquedas en arrays
Podemos utilizar el método where() para realizar búsquedas de los elementos que
cumplan con una condición pasado como argumento a dicho método. Algunos
sencillos ejemplos de su uso incluyen la búsqueda de un valor específico o buscar
todos los elementos pares del array:

## Ordenando arrays
Con el método sort() obtenemos una copia del array, manteniendo el original
inalterado. Si ordenamos un array 2-D, el orden se hará fila a fila:

## Filtrado de arrays
Para ello, se usa un array de booleanos que permiten indicar mediante valores True o
False si el elemento correspondiente se mantendrá o no tras el filtrado.

## 2.8. Importación de datos

Aunque ya hemos visto algunas en los ejemplos en la sección de librerías, vamos a
ver las diferentes formas que tenemos para importar datos en Python a la hora de
aplicar métodos machine learning 


- Importación de archivos en formato .txt.
- Importación de archivos planos CSV mediante la librería estándar de Python.
- Importación de archivos planos CSV mediante NumPy.
- Importación de archivos planos CSV mediante Pandas.
- Importación desde una URL.
- Importación desde otras librerías (toy datasets).

## Importación de archivos en formato .txt
- En todos los casos en los que manejemos ficheros, nos interesa asegurarnos
primero de que estamos en el directorio correcto, a no ser que queramos utilizar una
ruta absoluta

## Importación de archivos planos CSV mediante la librería estándar de Python
- En el caso de que trabajemos con archivos CSV, hemos de tener en cuenta, no solo
la ubicación, sino detalles como:
- Si tiene cabecera (header).
- Si tiene comentarios (incluidos con #).
- Qué tipo de delimitador utiliza el fichero (coma, punto y coma, espacios en blanco,
etc.)

## Importación de archivos planos CSV mediante Pandas

- Esta forma es muy popular dadas las ventajas que ofrece Pandas en este sentido.
- Usaremos la función readcsv() para la carga, la cual nos ofrece una gran versatilidad
a la hora de importar los datos. Con una única línea permite:

- Detectar automáticamente los headers sin que se lo tengamos que especificar.
Saltar líneas con el modificador skiprow.

- Detectar automáticamente el tipo de datos (entero, flotante, cadenas, etc.)
- Identificar campos erróneos o vacíos.
- Convertir los datos CSV en un dataframe de Pandas, que son estructuras de datos
especialmente diseñadas para aplicar técnicas de ciencia de datos, siendo posible
su uso como tablas o series temporales.
- Emplear la opción chunksize para cargar los datos en fragmentos de tamaño
configurable en lugar de cargar todos los datos en un único espacio de memoria. De
este modo, se mejora la eficiencia.

## Importación desde una URL
- También podemos cargar directamente los datos desde una URL usando Pandas:


## Importación desde otras librerías
(toy datasets)
Como ya hemos visto con anterioridad, existen datasets que vienen incluidos «de
serie» en las librerías de machine learning. Lo hemos visto en los ejemplos de scikitlearn, pero también los hay incluidos en paquetes como statsmodels o seaborn. Este
tipo de conjuntos de datos para hacer pruebas se conocen como «toy datasets»


## 2.9. Introducción a Machine Learning con librerías en Python

## Medias, medianas, modas, desviación estándar, varianza y percentiles
Como hemos visto con anterioridad, podemos dividir los tipos de datos de nuestro
dataset en:

Medidas de Tendencia Central
Estas medidas nos dicen dónde está el "centro" o el valor más típico de un conjunto de datos.

## Media (Promedio)
La media es lo que comúnmente conocemos como promedio. Se calcula sumando todos los valores de un conjunto de datos y dividiendo el resultado entre el número total de valores.

¿Cómo recordarla? Piensa en tu promedio de calificaciones. Sumas todas tus notas y divides entre el número de materias.
Ejemplo: Si tus edades son 10, 12, 11, 13, 14. La media es (10+12+11+13+14)/5=60/5=12. La edad promedio es 12 años.

## Mediana
La mediana es el valor que se encuentra justo en el medio de un conjunto de datos cuando estos están ordenados de menor a mayor (o de mayor a menor). Si hay un número par de datos, la mediana es el promedio de los dos valores centrales.

¿Cómo recordarla? Piensa en la "línea media" de una carretera; es el punto central.
Ejemplo:
Datos impares: 10, 11, 12, 13, 14. La mediana es 12.
Datos pares: 10, 11, 12, 13, 14, 15. La mediana es (12+13)/2=12.5.

### Moda
La moda es el valor que aparece con mayor frecuencia en un conjunto de datos. Puede haber una moda (unimodal), varias modas (multimodal) o ninguna moda si todos los valores son únicos.

¿Cómo recordarla? Piensa en la "moda" en la ropa; es lo que "más se usa" o "más se repite".
Ejemplo:
10, 11, 12, 13, 12, 14. La moda es 12.
10, 11, 12, 13, 14. No hay moda.


## Medidas de Dispersión
Estas medidas nos dicen qué tan dispersos o separados están los datos entre sí.

## Desviación Estándar
La desviación estándar mide el promedio de qué tan lejos están los datos de la media. Un valor bajo indica que los datos están cerca de la media, mientras que un valor alto indica que están más dispersos.

¿Cómo recordarla? Piensa que te dice qué tan "desviados" o "apartados" están los datos de su centro (la media) en promedio. Es una medida clave de la "variabilidad" de los datos.
Concepto clave: Es la raíz cuadrada de la varianza.

## Varianza
La varianza mide la dispersión total de los datos alrededor de la media. Es el promedio de los cuadrados de las diferencias de cada dato con la media. Se usa para calcular la desviación estándar.

¿Cómo recordarla? Piensa que te dice qué tanta "variación" o "diferencia" hay en tus datos con respecto a la media. Es el paso previo a la desviación estándar.
Concepto clave: La varianza está en unidades cuadradas de los datos originales, por eso se le saca raíz cuadrada para obtener la desviación estándar y que esté en las mismas unidades que los datos.

## Medidas de Posición
Estas medidas nos dicen la posición de un valor específico dentro de un conjunto de datos ordenado.

## Percentiles
Los percentiles dividen un conjunto de datos ordenado en 100 partes iguales. Un percentil indica el porcentaje de datos que caen por debajo de un valor específico. Por ejemplo, si sacaste 85 en un examen y eso te pone en el percentil 90, significa que el 90% de los estudiantes sacaron menos de 85.

¿Cómo recordarlos? Piensa en "por ciento" (parte de cien). Te dice qué porcentaje de los datos están por debajo de un valor.
Ejemplo: El percentil 25 (P25) es el valor por debajo del cual cae el 25% de los datos. El percentil 50 (P50) es la mediana, ya que el 50% de los datos están por debajo de este valor.

## Resumen para memorizar:
- Media: Promedio, el "centro" aritmético.
- Mediana: El valor de en medio cuando los datos están ordenados.
- Moda: El valor que más se repite (el que está de "moda").
- Desviación Estándar: Qué tan alejados están los datos de la media, en promedio (en las mismas unidades que los datos).
- Varianza: La dispersión total de los datos respecto a la media (la desviación estándar al cuadrado).
- Percentiles: Dividen los datos en 100 partes, indicando el porcentaje de datos por debajo de un valor.


- Numéricos:
    - Discretos (el número de hijos por mujer).
    - Continuos (la longitud del pétalo de una flor).
- Categóricos (perro, gato, loro).
- Ordinales (suspenso, aprobado, notable, sobresaliente).

NumPy y SciPy nos ofrecen métodos rápidos para calcular diferentes medidas de un
conjunto de datos, como la media, la mediana, la moda, la desviación estándar, la
varianza y determinados percentiles, por ejemplo, el percentil 75:

## Distribución de los datos
Podemos generar una gran cantidad de datos aleatorios con NumPy y mostrar el
histograma representando la distribución de los datos usando Matplotlib.

## Regresiones
Una forma clásica de aprendizaje supervisado cuando se tienen datos continuos es
la regresión, que puede ser lineal o polinómica, además de otros muchos más tipos
más complejos

## TensorFlow 2.0 Crash Course
 2  horas de tensorFlow 
https://www.youtube.com/watch?v=6g4O5UOH304&ab_channel=freeCodeCamp.org 

Fundamentos de Machine Learning
1. Regresión Lineal con Python
🔗 https://youtu.be/1CGbP0l0iqo?si=DZnQW4ClqyZaOJhJ
📌 Explicación de la regresión lineal y su implementación en Python.

2. Codificación de Datos Categóricos
https://youtu.be/KUEsLv8EaVY?si=ER1EN3ZutSwN9kCx
📌 Métodos para transformar variables categóricas en datos numéricos para modelos de ML.

3. Escalamiento, Normalización y Estandarización de Datos
https://youtu.be/-VuR14Qyl7E?si=sfjLg1Zg4rlXXn6q
📌 Técnicas para preparar datos antes de alimentar un modelo de aprendizaje automático.


Algoritmos de Aprendizaje Automático
4. Random Forest (Bosque Aleatorio
https://youtu.be/yOCJQLf_YFI?si=qj_tImJhBxBLxHI1
📌 Explicación de este método de ensamblado basado en árboles de decisión.

5. Entropía en Árboles de Decisión
https://youtu.be/GWX2YcnaELg?si=KrWBYM5uRI1EHKyk
📌 Concepto clave en la división de nodos dentro de árboles de decisión.

6. Impureza GINI en Árboles de Decisión
https://youtu.be/PFn31_hzQ2Y?si=ZUOD5-ejUK3zICWB
📌 Otro criterio fundamental en la construcción de árboles de decisión.

Evaluación y Optimización de Modelos
7. Matriz de Confusión: Precisión, Accuracy, Recall y F1-Score
https://youtu.be/uaGMk43XTOw?si=EdxWX8czQOzQpaQR
📌 Cómo evaluar el rendimiento de los modelos de clasificación.

8. Curva ROC y AUC
https://youtu.be/Uyfcqn3Nidc?si=1ubow-pNmcaQlEB5
📌 Análisis de la capacidad discriminativa de un modelo de clasificación.

9. Optimización de Modelos: Hiperparámetros
https://youtu.be/YAfS8-BXp8Q?si=wmuqpBY0sCIkGfqD
📌 Técnicas para mejorar el rendimiento de los modelos de ML mediante el ajuste de hiperparámetros.



# Tema 3. Árboles de decisión

## 3.3. Descripción de la tarea de inducción

### Resumen: Descripción de la tarea de inducción en árboles de decisión

El objetivo de la **inducción** en el aprendizaje automático es tomar información específica (observaciones, experiencias) y usarla para encontrar conocimiento general o patrones ocultos. En el caso de los **árboles de decisión**, esto significa construir un árbol que pueda clasificar nuevos datos basándose en ejemplos que ya han sido clasificados.

#### ¿Cómo se construye un árbol de decisión?

Un árbol de decisión se construye **seleccionando atributos** que ayuden a dividir los datos en grupos cada vez más homogéneos (es decir, que contengan ejemplos de la misma clase).

* **Selección del atributo**: Este es un paso crucial. El algoritmo elige el "mejor" atributo para hacer la primera división. Por ejemplo, si estamos clasificando si se puede jugar al tenis, podría ser el "ambiente".
* **Creación de ramas**: Una vez que se selecciona un atributo, se crean ramas a partir de ese punto.
    * Si el atributo tiene valores **discretos** (como "soleado", "nublado", "lluvioso"), se crea una rama para cada valor.
    * Si el atributo es **numérico** (como la temperatura), se establece un punto de corte (por ejemplo, si la temperatura es "mayor a X" o "menor a X").
* **Proceso iterativo**: Este proceso de seleccionar un atributo y ramificar el árbol se repite para cada subconjunto de datos hasta que se cumplen ciertas condiciones:
    * Todos los ejemplos en un nodo pertenecen a la misma clase (¡éxito, llegamos a una "hoja" del árbol!).
    * No quedan más atributos para dividir los datos. En este caso, el nodo se convierte en una hoja y se etiqueta con la clase más común entre los ejemplos que llegaron a ese punto.
    * No hay ejemplos para una rama (lo que se maneja etiquetando la hoja con la clase mayoritaria del conjunto original de datos).

#### Ejemplo práctico: ¿Se puede jugar al aire libre?

El texto usa un ejemplo clásico para ilustrar esto: clasificar si es un buen día para jugar al aire libre (como al tenis) basándose en factores como el ambiente, la temperatura, la humedad y el viento. El algoritmo "aprende" de ejemplos pasados para decidir, por ejemplo, que si el "Ambiente" es "nublado", ¡siempre se puede jugar!

#### Es un algoritmo "Divide y Vencerás" (y "Codicioso")

Este tipo de algoritmo se conoce como **"divide y vencerás"** porque rompe un problema grande en problemas más pequeños y manejables. También se le llama **"codicioso"** (greedy) porque en cada paso toma la mejor decisión en ese momento sin "mirar hacia atrás" para ver si una decisión anterior podría haberse mejorado.

En resumen, los árboles de decisión aprenden a clasificar datos construyendo una serie de "preguntas" (basadas en atributos) que, al seguir las respuestas, te llevan a una clasificación final.


## 3.4. Algoritmo básico de aprendizaje de árboles de decisión: ID3

## Algoritmo ID3: Cómo los árboles de decisión aprenden a clasificar

El **algoritmo ID3** es una forma específica y popular de construir un **árbol de decisión**. Imagina que estás construyendo un árbol genealógico, pero en lugar de personas, son decisiones. ID3 hace esto de **arriba hacia abajo**, empezando por la "raíz" y ramificándose.

### La clave: La ganancia de información

ID3 tiene un truco principal para decidir qué atributo usar en cada "ramificación" del árbol: la **ganancia de información**. Este concepto viene de la **teoría de la información** y básicamente busca el atributo que nos dé la *mayor claridad* o *la mejor pista* para clasificar los ejemplos.

Piensa así: si tienes un montón de datos mezclados (algunos "sí", algunos "no"), la ganancia de información te dice qué pregunta (qué atributo) te va a ayudar a separar esos datos de la forma más efectiva, haciendo que los grupos resultantes sean lo más "puros" posible (es decir, que todos en un grupo sean "sí" o todos sean "no").

### ¿Cómo mide ID3 esta "claridad" o "pureza"?

Para entender la ganancia de información, primero necesitamos entender la **entropía**:

* **Entropía**: Es una medida de la **heterogeneidad** o **mezcla** de un conjunto de ejemplos.
    * Si todos los ejemplos en un grupo son de la misma clase (por ejemplo, todos son "sí"), la entropía es **cero (0)**. ¡Perfecta pureza!
    * Si los ejemplos están perfectamente mezclados (por ejemplo, la mitad son "sí" y la mitad son "no" en una clasificación de dos clases), la entropía es **uno (1)**. ¡Máxima mezcla!
    * Si están parcialmente mezclados, el valor de la entropía estará entre 0 y 1.

    Matemáticamente, la entropía ($H(E)$) se calcula con la siguiente fórmula:
    $$H(E) = - \sum_{i=1}^{n} p_i \log_2(p_i)$$
    donde $p_i$ es la proporción de ejemplos que pertenecen a la clase $i$.

* **Ganancia de Información (Gain)**: Una vez que entendemos la entropía, la ganancia de información se vuelve sencilla. Mide **cuánto se reduce la entropía** si dividimos los ejemplos usando un atributo específico. Es decir, qué tan efectivo es ese atributo para "limpiar" la mezcla.

    La fórmula para calcular la ganancia de información de un atributo A en un conjunto de ejemplos E es:
    $$Gain(E, A) = H(E) - \sum_{v \in Values(A)} \frac{|E_v|}{|E|} H(E_v)$$
    donde:
    * $H(E)$ es la entropía del conjunto original.
    * $Values(A)$ son los posibles valores del atributo A.
    * $E_v$ es el subconjunto de ejemplos donde el atributo A toma el valor $v$.
    * $|E_v|$ y $|E|$ son el número de ejemplos en los subconjuntos.

### Pasos del Algoritmo ID3 en acción

1.  **Inicio**: Se empieza con todos los datos en la "raíz" del árbol.
2.  **Calcular Ganancia**: Para cada atributo disponible, ID3 calcula su ganancia de información.
3.  **Seleccionar el Mejor Atributo**: Se elige el atributo que tiene la **mayor ganancia de información**. Este será el que mejor "clasifique" o separe los ejemplos.
4.  **Ramificar**: Se crea una rama por cada posible valor de ese atributo. Los ejemplos se distribuyen por estas ramas según el valor de ese atributo que tengan.
5.  **Repetir**: Este proceso se repite para cada rama (cada "nodo hijo") con los ejemplos que llegaron a esa rama, y con los atributos que aún no se han utilizado en ese camino del árbol.
6.  **Parada**: El proceso se detiene en una rama cuando:
    * Todos los ejemplos en esa rama pertenecen a la misma clase (¡Ya se clasificaron!).
    * Ya no quedan atributos para dividir (en este caso, el nodo se convierte en una hoja y se etiqueta con la clase más común entre los ejemplos que llegaron allí).
    * No hay ejemplos en una rama específica.

### Ejemplo del "Problema del Tiempo"

El texto menciona que, para el problema de si jugar al aire libre, el algoritmo ID3 probablemente seleccionaría el atributo "**ambiente**" como el primero para ramificar el árbol. Esto se debe a que, al calcular la ganancia de información, "ambiente" es el que ofrece la mayor reducción de entropía. Por ejemplo, todos los días "nublados" resultan en "sí" (jugar al aire libre), lo que hace que esa rama sea pura y se convierta en una hoja de inmediato.

En esencia, ID3 es un método **"codicioso"** (greedy) que siempre busca el mejor atributo en el momento actual para dividir los datos, construyendo el árbol paso a paso sin retroceder.

## 3.5. Espacio de búsqueda y bias inductivo

### La Búsqueda de ID3 en el Espacio de Posibles Soluciones

Imagina que existen muchísimos árboles de decisión posibles que podrían explicar tus datos. El **ID3** tiene la tarea de encontrar el árbol "correcto" que se ajuste a tus **ejemplos de entrenamiento** (los datos que ya conoces y están clasificados).

* **Búsqueda en Escalada (Hill Climbing)**: ID3 busca esta solución subiendo una "colina". Empieza con árboles sencillos y va construyendo árboles más complejos paso a paso. Se guía por la **ganancia de información**; cada paso que da es hacia el árbol que, hasta ese momento, clasifica mejor los datos.
* **Espacio de Hipótesis Completo**: Una gran ventaja de ID3 es que explora un conjunto **completo** de posibles árboles. Esto significa que **nunca se quedará sin una solución** dentro del rango de lo que puede construir.
* **Un Camino a la Vez**: Sin embargo, ID3 solo se concentra en **una única solución posible** a la vez. No compara múltiples árboles "buenos" simultáneamente. Esto es como tener solo un camino en la colina; si ese camino te lleva a una cima que no es la más alta de todas (una **óptima local**), te quedarás ahí sin saber que hay una mejor cima en otro lugar.
* **Sin Marcha Atrás (Greedy)**: Una vez que ID3 toma una decisión (elegir un atributo para un nodo), **no retrocede** para reconsiderar esa elección. Esta es la naturaleza "codiciosa" (greedy) del algoritmo. Puede llevar a construir un árbol que funciona bien para los datos de entrenamiento, pero que quizás no sea el mejor árbol posible a nivel global.
* **Robusto a Errores y Coste Computacional**: ID3 es bueno para manejar datos con errores porque usa **todos los ejemplos** en cada cálculo de ganancia de información. Esto lo hace robusto, pero también significa que puede ser **computacionalmente más costoso** que otros métodos que solo usan una parte de los ejemplos en cada paso.

---

### El "Bias" (Sesgo) Inductivo de ID3: ¿Por qué elige ciertos árboles?

El **bias inductivo** de un algoritmo se refiere a los **criterios o preferencias** que usa para seleccionar una solución (una hipótesis) entre muchas posibles. En el caso de ID3, su sesgo se basa en dos premisas principales:

1.  **Preferencia por Árboles Cortos**: ID3 tiende a preferir los **árboles más cortos** (con menos nodos y ramas) sobre los árboles más largos. Aunque no siempre garantiza que encontrará el árbol más corto *absoluto* (porque no hace una búsqueda exhaustiva de todos los posibles árboles), su enfoque de "búsqueda en escalada" y "codicioso" lo inclina hacia la simplicidad.

2.  **Atributos con Mayor Ganancia de Información Cerca de la Raíz**: ID3 siempre colocará los atributos que proporcionan la **mayor ganancia de información** (los que mejor dividen los datos) **más cerca de la raíz** del árbol. Esto tiene sentido, ya que si un atributo es muy bueno para clasificar, es lógico usarlo al principio para hacer las divisiones más importantes.

#### ¿Por qué es importante preferir árboles cortos?

Preferir árboles cortos es crucial para la **generalización**. Un árbol más corto y simple a menudo puede **clasificar correctamente nuevos datos** (instancias que no se usaron para entrenar el árbol) de manera más efectiva. Los árboles muy complejos pueden "memorizar" los datos de entrenamiento perfectamente, pero luego fallan al aplicarse a datos nuevos que nunca han visto. Esto se conoce como **sobreajuste (overfitting)**, y preferir árboles cortos es una estrategia para evitarlo.

En resumen, ID3 busca un árbol que clasifique bien los datos de entrenamiento, guiándose por la ganancia de información. Su "prejuicio" lo lleva a favorecer árboles más simples y a usar los atributos más informativos al principio, lo cual es beneficioso para que el árbol funcione bien no solo con los datos que ya conoce, sino también con datos completamente nuevos.

## 3.6. Métodos de selección de atributos

## Métodos de Selección de Atributos: Diferentes Formas de Ramificar un Árbol

Cuando construyes un árbol de decisión, una de las decisiones más importantes es **qué atributo usar** para dividir tus datos en cada paso. Hay varios "métodos de selección de atributos" que los algoritmos de árboles de decisión pueden emplear para tomar esta decisión crucial. La elección del método dependerá del algoritmo que uses, de tus datos, y de lo que esperas del árbol final.

### 1. Ganancia de Información (ID3)

Como ya vimos, el algoritmo **ID3** utiliza la **ganancia de información**. Esta mide cuánto "clarifica" un atributo la clasificación de tus datos al reducir la **entropía** (la mezcla o impureza de las clases). El atributo con la mayor ganancia de información es el elegido para la división.

### 2. Índice Gini (CART)

Otro método popular es el **índice Gini**, típicamente usado en algoritmos **CART (Classification and Regression Trees)**. A diferencia de la entropía, que mide la incertidumbre, el índice Gini mide la **impureza** de un conjunto de datos.

* **¿Cómo se calcula?** Se basa en la proporción de cada clase en un conjunto de ejemplos ($p_i$). La fórmula es:
    $$Gini(E) = 1 - \sum_{i=1}^{n} p_i^2$$
    Donde $n$ es el número de clases y $p_i$ es la proporción de ejemplos que pertenecen a la clase $i$.

* **¿Cómo se usa?** El objetivo es **minimizar el índice Gini**. Esto significa que el atributo que produce los subconjuntos con el Gini más bajo (menos impureza) es el que se selecciona para la división. Es decir, buscas la mayor **reducción de impureza**.

### 3. Proporción de Ganancia (C4.5)

El algoritmo **C4.5** (una mejora de ID3) utiliza la **proporción de ganancia**. Este método es una adaptación de la ganancia de información y es especialmente útil cuando tienes atributos con **muchos valores diferentes**.

* **El Problema de la Ganancia de Información:** La ganancia de información tiende a favorecer atributos que tienen un gran número de valores únicos. Por ejemplo, si tienes un atributo que es un "número de identificación" (ID), cada ejemplo tendrá un ID único. La ganancia de información de este atributo sería altísima porque lo divide perfectamente, pero no sería útil para clasificar nuevas instancias porque un nuevo ID no estaría en el árbol.

* **La Solución de la Proporción de Ganancia:** La proporción de ganancia compensa esto. Toma la **ganancia de información** y la **divide** por una medida llamada **información de la división**. La información de la división castiga a los atributos que distribuyen los ejemplos de manera muy uniforme entre muchos valores. La fórmula es:
    $$SplitInformation(E, A) = - \sum_{v \in Values(A)} \frac{|E_v|}{|E|} \log_2(\frac{|E_v|}{|E|})$$
    Y luego la proporción de ganancia se calcula como:
    $$GainRatio(E, A) = \frac{Gain(E, A)}{SplitInformation(E, A)}$$
    Al dividir por la información de la división, se penaliza a los atributos que generan muchas ramas, haciendo que los atributos con menos valores o con valores más concentrados sean más atractivos si su ganancia de información sigue siendo alta.

### 4. Longitud de Descripción Mínima (MDL - Minimum Description Length)

El método MDL es un principio más general que se puede aplicar a la construcción de árboles. Busca el árbol de decisión que es más **simple** de describir.

* **La Idea:** Considera el "mejor" árbol como aquel que requiere el menor número de "bits" (información) para codificar dos cosas:
    1.  El propio árbol de decisión (su estructura y reglas).
    2.  Los errores de clasificación que comete el árbol (casos que el árbol no clasifica correctamente).
* **El Objetivo:** La meta es encontrar la opción más simple y concisa que explique los datos.

### Consideraciones Clave

* **"Bias" o Sesgo:** Cada uno de estos métodos tiene su propio **sesgo inductivo** (como vimos antes). Por ejemplo, ID3 prefiere árboles cortos y atributos informativos cerca de la raíz. CART, con el índice Gini, también busca la simplicidad.

* **Complejidad vs. Precisión:** Hay un equilibrio. Un árbol más profundo y complejo puede ser muy preciso en los datos de entrenamiento (potencialmente sobreajustándose), pero puede cometer más errores en datos nuevos. Los árboles más cortos son a menudo mejores para **generalizar**, aunque podrían no ser perfectos en los datos de entrenamiento.

* **No Hay un "Mejor" Método Universal:** No existe un método de selección de atributos que sea universalmente superior a todos los demás. La elección depende del contexto, los datos y los objetivos específicos del problema de clasificación.


## 3.7. Sobreajuste y poda de árboles

¡Perfecto! Este es un tema crucial en el aprendizaje automático. Comprender el **sobreajuste** y cómo **podar árboles** es fundamental para construir modelos útiles y no solo "memoriones".

## Sobreajuste y Poda de Árboles de Decisión: Evitando el "Memorión"

Como ya vimos, el algoritmo **ID3** (y otros similares) tienen como objetivo clasificar los datos de entrenamiento a la perfección. Sin embargo, esto puede ser contraproducente. Cuando un modelo clasifica **demasiado bien** los datos de entrenamiento, a menudo significa que se ha vuelto excesivamente complejo, ha "memorizado" cada detalle (incluido el ruido o las particularidades de la muestra) y, por lo tanto, no es bueno para **generalizar** con datos nuevos. Esto es lo que llamamos **sobreajuste (overfitting)**.

### ¿Qué es exactamente el Sobreajuste?

El sobreajuste ocurre cuando un árbol de decisión (o cualquier modelo) es **demasiado complejo** y se ajusta muy bien a los **datos de entrenamiento**, pero falla al aplicarse a **nuevas instancias** (datos que no ha visto antes). Es como un estudiante que memoriza cada palabra del libro, pero no entiende los conceptos, por lo que le va mal en el examen si las preguntas cambian un poco.

* **Ejemplo del problema del tiempo:** Si un dato en tu tabla de entrenamiento (como el Ejemplo 7) está mal clasificado, ID3 intentará aprender a clasificarlo correctamente. Esto podría llevar a que el árbol se ramifique más y se vuelva más complejo de lo necesario solo para "explicar" ese dato erróneo, en lugar de generar un nodo hoja simple. El resultado es un árbol que es perfecto para tus datos actuales, pero que es muy probable que cometa errores con datos futuros.

### Estrategias para Evitar el Sobreajuste: La Poda del Árbol

El sobreajuste es un problema común, y se necesitan estrategias para **mitigarlo**. La más importante en los árboles de decisión es la **poda**. Podar un árbol es como cortar las ramas que no son realmente útiles o que hacen que el árbol sea demasiado complicado.

Existen dos enfoques principales para la poda:

1.  **Poda Directa del Árbol:**
    * Después de que el árbol se ha generado completamente, se evalúan sus ramas.
    * Se eliminan las ramificaciones que parecen ser menos fiables o que no aportan una mejora significativa a la clasificación.
    * Cuando se poda un nodo, se convierte en una **hoja** y se le asigna la clase mayoritaria de los ejemplos que caían en ese nodo antes de la poda.
    * Es difícil saber cuándo parar de podar, pero la idea es simplificar el árbol para mejorar su capacidad de generalización.

2.  **Poda Basada en Reglas (Mapeado a Reglas):**
    * Primero, se construye el árbol de decisión a partir de los datos de entrenamiento.
    * Luego, cada camino desde la raíz hasta una hoja del árbol se convierte en una **regla**. Por ejemplo: `SI (Ambiente = Soleado) Y (Humedad = Alta) ENTONCES (Clase = No Jugar)`.
    * **Poda de cada regla:** Se revisa cada regla individualmente. Si eliminar una condición (una parte del `AND`) en la regla mejora la precisión de la clasificación, esa condición se elimina.
    * Finalmente, las reglas se ordenan por su precisión, y cuando se clasifica un nuevo ejemplo, se usan las reglas en ese orden.
    * **Ventaja:** Este método permite podar decisiones de forma más **aislada** porque trabajas con reglas individuales, no con nodos que pueden afectar a múltiples reglas. No importa si la condición está cerca de la raíz o de la hoja; la poda se hace por regla.

### ¿Cómo Saber el Tamaño Adecuado del Árbol? (Validación Cruzada)

Determinar el tamaño óptimo de un árbol (cuándo dejar de crecerlo o hasta dónde podarlo) es complicado. Una técnica fundamental para hacer esto es la **validación cruzada (cross-validation)**.

La validación cruzada te permite estimar qué tan bien funcionaría tu modelo con **datos nuevos** (datos de prueba) cuando no tienes un conjunto de datos de prueba separado.

* **Proceso Básico:**
    1.  **Dividir los Datos:** Tomas tu conjunto de datos disponible y lo divides en dos partes:
        * **Datos de Entrenamiento:** Se usan para construir el árbol de decisión. (Ej. 2/3 de los datos).
        * **Datos de Validación:** Se usan para **evaluar la precisión** del árbol podado o en crecimiento, simulando cómo clasificaría datos futuros. (Ej. 1/3 de los datos).
    2.  **Evaluar la Poda:** Mientras podas el árbol (o decides cuándo detener su crecimiento), usas los datos de validación para ver si el árbol resultante mejora o mantiene su precisión. Si podar un nodo mejora la clasificación en los datos de validación, ¡lo podas! Esto ayuda a eliminar las ramas que se crearon por el ruido en los datos de entrenamiento.
    3.  **Desventaja:** Necesitas suficientes datos para que tanto el conjunto de entrenamiento como el de validación sean estadísticamente significativos.

* **Validación Cruzada de K-Iteraciones (K-fold Cross-Validation):**
    * Cuando no tienes muchos datos, esta técnica es muy útil.
    * **División:** Tus datos se dividen en "k" subconjuntos (o "folds") de igual tamaño.
    * **Iteraciones:** El proceso se repite "k" veces. En cada repetición:
        * Un subconjunto se usa como **datos de validación (prueba)**.
        * Los **"k-1" subconjuntos restantes** se usan como **datos de entrenamiento**.
    * **Resultado Final:** Al final, se promedian los resultados obtenidos en cada una de las "k" iteraciones para tener una estimación más robusta del rendimiento del modelo.
    * **Común:** Un valor común para "k" es 10 (validación cruzada de 10 iteraciones) ya que suele dar buenos resultados.

En resumen, el sobreajuste es un problema de "memorización" que hace que el árbol sea inútil con datos nuevos. La **poda** es la solución, simplificando el árbol para que **generalice** mejor. La **validación cruzada** es la herramienta clave para saber cuándo y cuánto podar, ayudándonos a encontrar el equilibrio perfecto entre un modelo que aprende bien y uno que funciona bien en el mundo real.



## 3.8. Medidas de la precisión de la clasificación. Curva ROC
## 3.9. Simplificación de árboles de decisión mediante poda: algoritmo C4.5
## 3.10. Ensemble Learning y Random Forest
## 3.11. Aplicaciones y ejemplos de implementación



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


