# Técnicas de Inteligencia Artificial

## Temario 1: Introducción a la IA 

## Resumen del Diagrama: Descubrimiento del Conocimiento y Aprendizaje Automático

La imagen presenta un diagrama que ilustra dos conceptos principales interrelacionados: **Descubrimiento del Conocimiento en Bases de Datos (KDD)** y el **Aprendizaje Automático (Machine Learning)**.

**Descubrimiento del Conocimiento en Bases de Datos (KDD):**

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
        * **Aprendizaje Supervisado:** Se basa en la descripción de un concepto o clase a partir de datos etiquetados (ejemplos y no ejemplos).
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
Es una rama de la informática que estudia la creación de agentes computacionales que reciben estímulos externos y, en base a ellos y a un conocimiento almacenado en dicho agente, producen resultados o acciones que maximizan una medida de rendimiento. El conocimiento almacenado puede ser aprendido por el mismo agente utilizando técnicas de aprendizaje automático o puede ser incorporado por un humano experto en el dominio específico.


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


