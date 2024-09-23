# Curso Python Básico 



## Tema 1 Introducción 

**Notas Mentales**
- Creado en 1989 
- Creador conocido como el Benevolente dictador Vitalicio, gracias a sus grandes capacidades en la toma de deciciones 
- Creador Guido van Rossum 
- Se fundamenta del lenguaje ABC 
- Inicio en Holanda que ahora es la W3C
- Va por la version 3 estable 
- Anaconda es usando para el analisis de datos ya que viene ya con modulos preinstalados

**Temas de lectura** 

```
Explicación:

Anaconda es una distribución de Python especialmente diseñada para ciencia de datos y machine learning. Viene preinstalada con una gran cantidad de paquetes y librerías populares para estas áreas, como NumPy, Pandas, Matplotlib, Scikit-learn, entre otros. Esto facilita enormemente el inicio de proyectos en estos campos, ya que no es necesario instalar cada paquete individualmente.

La distribución básica de Python (la que se instala desde el sitio web oficial de Python) incluye un conjunto más limitado de módulos, los considerados "estándar". Si necesitas librerías más específicas o avanzadas, deberás instalarlas utilizando herramientas como pip.


Fin de vida de Python 2.7: La versión 2.7 de Python llegó a su fin de vida en enero de 2020. Esto significa que ya no recibe actualizaciones de seguridad ni nuevas funcionalidades. Utilizar una versión obsoleta expone a tu proyecto a vulnerabilidades y limita las posibilidades de desarrollo.

Python 3 es el futuro: Python 3 es la versión actual y activa del lenguaje, con mejoras significativas en cuanto a rendimiento, legibilidad y soporte para nuevas características.
Compatibilidad con librerías: La gran mayoría de las bibliotecas y frameworks modernos están diseñados para funcionar con Python 3 y no son compatibles con versiones anteriores.
-------------------------------------------------------------------------------------

Propósito de Jupyter: Jupyter Notebook está enfocado en la creación y ejecución de código, así como en la exploración interactiva de datos. La generación de PDF suele ser un paso posterior, una vez que el trabajo en el notebook ha finalizado.

El navegador de archivos de Jupyter Notebook está diseñado principalmente para gestionar y organizar los archivos asociados a tus proyectos de Jupyter, como:

Notebooks (.ipynb): Estos son los archivos principales donde se escribe y ejecuta el código Python, además de incluir texto enriquecido, imágenes y otros elementos.

Carpetas: Sirven para organizar tus notebooks y otros archivos relacionados.

Ficheros de Texto: Puedes crear y editar archivos de texto plano (.txt) para almacenar datos o notas.

Aunque Jupyter Notebook no permite crear archivos PDF directamente desde su navegador de archivos, ofrece varias opciones para convertir tus notebooks a este formato una vez que hayas terminado de trabajar en ellos.

Una de las características más destacadas de Jupyter Notebook es su capacidad de ejecutar código en celdas individuales y mostrar los resultados inmediatamente debajo de la celda. Esto significa que:

Ejecución celda a celda: Puedes ejecutar el código contenido en una celda de forma independiente, y el resultado (ya sea texto, una gráfica, un DataFrame de pandas, etc.) se mostrará automáticamente en una celda de salida justo debajo.
Actualización en vivo: Si modificas el código en una celda y la ejecutas nuevamente, la celda de salida se actualizará con el nuevo resultado.
----------------------------------------------------------------------------------------

```


**Examen**

**Python se creó con el objetivo de**

Pregunta 1 

- Ser más potente que otros lenguajes de la época.
- Crear un lenguaje fácil de usar y de aprender. ✔️
- Programar usando interfaces visuales.
- Poder crear aplicaciones de servidor más fácilmente.

**¿Cuál de las siguientes propiedades tiene Python?**
Pregunta 2

- El tipo de las variables se hace de forma dinámica.
- Se pueden programar en diferentes paradigmas como programación orientada a objetos o programación funcional.
- Podemos extender las funcionalidades de Python creando módulos en C++.
- Todas las anteriores. ✔️



**La versión de Python que debemos usar es:**
Pregunta 3 

- Tenemos que usar la versión 3.8 o posterior. ✔️
- Podemos usar cualquier versión de Python, ya que no cambian mucho.
- Tenemos que usar la versión 2.7.
- Depende de las características de nuestro equipo.


**¿Cuál de las siguientes herramientas no podemos usar para programar en Python?**

Pregunta 4

- Editor de texto plano como Atom.
- La consola del sistema.
- Aplicaciones de ofimática como Word.
- Entornos de desarrollo avanzado como PyCharm.


**¿Cómo puedo instalar Jupyter Notebook en mi equipo?**
Pregunta 5

- Instalando la distribución Anaconda o solamente el módulo o paquete Jupyter en Python.✔️
- Instalando la distribución básica de Python.
- Instalando un editor de texto plano.
- A través de una suscripción.

**¿Qué diferencia existe entre las distribuciones de Python?**
Pregunta 6

- La distribución básica de Python incluye más módulo que Anaconda.
- La distribución de Anaconda incluye más módulo que la versión básica. ✔️
- Anaconda no permite instalar más módulos.
- La versión básica de Python no permite instalar más módulos.

¿Qué es Jupyter Notebook?
Pregunta 7

- Un editor de texto plano.
- Un comando de la consola para ejecutar instrucciones de Python.
- Un entorno que permite crear celdas con diferentes funcionalidades (escribir código, documentar, etc.).✔️
- Otra distribución para instalar Python en nuestro equipo.

**¿Qué tipo de celdas podemos usar en Jupyter Notebook?**
Pregunta 8

- Celdas con código de Python.
- Celdas con texto basado en markdown.
- Texto con formato consola.
- Todas las anteriores.✔️

**¿Qué tipo de ficheros no podemos crear con el navegador de archivos de Jupyter Notebook?**
Pregunta 9

- Notebooks.
- Carpetas.
- Ficheros de Texto.
- Ficheros PDF.✔️


**En Jupyter Notebook:**
Pregunta 10

- Las celdas de salida se crean automáticamente. ✔️
- Tenemos que ejecutar las instrucciones en la consola de Python.
- No se pueden exportar los notebooks a otros formatos como PDF o HTML.
- No se puede reiniciar el kernel para borrar la memoria.



## TEMA 2. PRIMEROS CONCEPTOS EN PYTHON

Pregunta 1
**Los identificadores en Python:**
Pueden incluir dígitos siempre que no estén al principio del identificador.

Pregunta 2
¿Cuál de estas afirmaciones no es correcta?
Puedo crear un identificador que se llame and.

Pregunta 3
¿Qué debemos usar para que Python detecte distintos bloques de código?
Sangrías de cuatro espacios según la guía de estilos PEP8.

Pregunta 4
¿Qué tipo de dato devuelve la siguiente operación? 2 / 3
float.

Pregunta 5
Si partimos de una variable var con un valor inicial igual a 10 y queremos multiplicarlo por 3 almacenando el resultado en la misma variable, ¿cuál es la forma más efectiva para conseguirlo?
var *= 3.

Pregunta 6
Tenemos la siguiente cadena de caracteres almacenada en una variable: frase ="Hola, Python!". Si accedemos a las posiciones frase[-7:12], ¿cuál será el resultado?

'Python'.

Pregunta 7

Usando la misma variable que en la pregunta anterior, ejecutamos la siguiente instrucción: frase.replace("Adiós", "Buenos días"). ¿Cuál será el resultado?

'Hola, Python!'.

Pregunta 8
Continuando con la variable anterior, ¿cuál es el resultado de esta sentencia?: len("Hola") <= frase.find(',')

True.

Pregunta 9

¿Cuándo se puede convertir un objeto a una cadena de caracteres?:
Siempre.

Pregunta 10
¿Cuál es el resultado de la siguiente operación booleana?: bool(0) or not(bool())

True.


