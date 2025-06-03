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

## 2.8. Importación de datos

## 2.9. Introducción a Machine Learning con librerías en Python

