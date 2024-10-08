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


## TEMA 3. PROGRAMACION BASICA 

Pregunta 1
Correcta
¿Cuál de estas afirmaciones no es correcta?
Los elementos de una lista solo pueden ser del mismo tipo.


Pregunta 2
Correcta
Para acceder al valor de un elemento de un diccionario necesitamos saber:
La clave que se ha asignado al elemento.

Pregunta 3
Correcta
Los conjuntos son:
Colecciones de elementos no ordenadas y sin repeticiones

Pregunta 4
Correcta
En una ejecución condicional, un bloque de código tras una sentencia else se ejecuta:
Si las expresiones de las sentencias if y elif han dado como resultado False.


Pregunta 5
Correcta
En un bucle while, un bloque de código tras una sentencia else se ejecuta:
Siempre, una vez se salga del bucle normalmente.

Pregunta 6
Correcta
¿Cuántas veces se va a imprimir el mensaje en este código?

for i in range(1, 9):
    print(i)

8.


Pregunta 7
Correcta
¿Qué números no se imprimirán en este código?


for i in range (1,10):
if i % 3 !=0:
print(i)
else:
continue

3, 6, 9.


Pregunta 8
Correcta
¿Cuál de las siguientes opciones nos devolvería los números pares de 0 a 19?
Pregunta 8Respuesta


range(0, 20, 2).

Pregunta 9
Correcta
¿Cuál será el resultado de ejecutar este código?

lista =['a', 5, 7]

iterador =iter(lista)

next(iterador) * 10


'aaaaaaaaaa'.

## TEMA 4. FUNCIONES 

Pregunta 1
¿Cuántos argumentos puede recibir la siguiente función y cómo se deben poner? 

Se recomienda no realizar copy and paste de la variable.

def ejemplo(*args):

    print(args)

Todos los que se quieran, y se colocarán por posición.


Pregunta 2
¿Cuál es el resultado de ejecutar la siguiente función? 

def calculo(numero_1, numero_2 = 3):

    return numero_1 / numero_2

calculo(10)

3.33.


Pregunta 3
La sentencia return de una función permite:
Devolver más de un resultado, pero se devolverán como una tupla.

Pregunta 4
¿Qué función del sistema Python se puede utilizar para obtener la parte entera de un número?

math.trunc().

Pregunta 5
¿Cuál es la funcionalidad de la variable sys.argv?

Almacenar los argumentos que se han introducido en la consola al ejecutar el script.

Pregunta 6

Queremos comprobar si el fichero '/Carpeta/fichero.py' existe en el sistema. ¿Cómo se podría hacer de la forma más sencilla?

Usando la función os.path.exists().

Pregunta 7

¿Qué devuelve la siguiente función?

def test():

    lista =[2, 6, ?Hola?, 10, 7]

    return random.choice(lista)



Un elemento de la lista elegido aleatoriamente.

Pregunta 8

Debe tener una única expresión, sin importar el tipo de esa expresión.


Pregunta 9
¿Qué devuelve la siguiente función?

funcion =lambda x: x >=5 and x < 10

list(filter(funcion, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

[5, 6, 7, 8, 9].

Pregunta 10

¿Qué devuelven las siguientes líneas de código?

 funcion =lambda x: str(x)
 list(map(funcion, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
Pregunta 10Respuesta

Una lista con todos los elementos convertidos a cadena de caracteres.



## Tema 5.  Organización del código 

Respuesta a la pregunta sobre herencia y polimorfismo
La respuesta correcta es: «Hola, soy la clase hija».

Explicación detallada
Cuando creamos un objeto de la clase ClaseHija, este hereda todas las propiedades y métodos de su clase padre ClasePadre. Sin embargo, al tener un método imprimir definido en ambas clases, se produce un fenómeno conocido como polimorfismo.

¿Qué es el polimorfismo? Es la capacidad de que un mismo método se comporte de manera diferente dependiendo del objeto que lo invoque. En este caso, al llamar al método imprimir sobre el objeto objeto (que es de tipo ClaseHija), se ejecutará la versión del método definida en ClaseHija.

¿Por qué se ejecuta la versión de la clase hija? Esto se debe a que Python busca siempre la implementación más específica del método. Como objeto es de tipo ClaseHija, Python encuentra primero la implementación en ClaseHija y la ejecuta, ignorando la versión de ClasePadre.

Descartando las demás opciones:

Mostrará un error al no saber a qué método nos referimos: No se producirá un error, ya que Python resuelve la ambigüedad gracias al polimorfismo.
«Hola, soy la clase padre». Solo se ejecutaría esta versión si el objeto fuera de tipo ClasePadre y no hubiera una implementación más específica en una subclase.
No se puede imprimir porque no le hemos pasado el argumento self. El argumento self se pasa automáticamente al llamar a un método de una instancia de una clase, por lo que no es necesario pasarlo explícitamente.
En resumen:

Gracias a la herencia y al polimorfismo, el código se vuelve más flexible y reutilizable. Al llamar a un método sobre un objeto, se ejecuta la versión más específica de ese método según el tipo de objeto, sin necesidad de escribir código adicional para cada caso.




Pregunta 1
Correcta

¿Cuál es la principal característica de los módulos?


Organizar el código de manera que podamos agrupar los diferentes elementos que desarrollemos.

Pregunta 2
¿Qué utilidad tiene el alias a la hora de importar un módulo?

El alias permite asignar otro identificador a dicho módulo.


Pregunta 3
¿Cómo debemos crear un paquete en Python?


Creando una carpeta donde exista un fichero llamado __init__.py.


Pregunta 4

En la siguiente importación de un paquete, ¿cómo debemos acceder a la función test() del módulo mi_modulo?

from paquete import mi_modulo as mod

mod.test().


Pregunta 5
¿Qué es un objeto?


Una abstracción de los datos que tiene un estado, un comportamiento y una identidad.

Pregunta 6
Cuando implementamos un método en una clase, ¿para qué sirve el parámetro self?

Para dar al método la instancia del objeto que va a utilizar.


Pregunta 7
Para la siguiente clase, ¿cómo podríamos crear una instancia?

class MiClase:

    def __init__(self, nombre, puntuacion=0.0):

        self.nombre = nombre

        self.puntuacion = puntuacion

Pregunta 7Respuesta

objeto = MiClase(?Hola?).


Pregunta 8

Cuando implementamos una clase que es una herencia de otra clase, ¿a qué elementos de la clase padre podemos acceder desde la clase hija?



A los atributos y métodos de la clase padre.


Pregunta 9

Supongamos que hemos implementado las siguientes clases. ¿Qué se mostrará en la consola si ejecutamos el método imprimir del objeto?

class ClasePadre:

    def imprimir(self):

        print("Hola, soy la clase padre")

class ClaseHija(ClasePadre):

    def imprimir(self):

        print("Hola, soy la clase hija")

objeto =ClaseHija()


«Hola, soy la clase hija».

Pregunta 10
¿Para qué sirven los docstring?

Para escribir documentación que luego puede ser consultada por la instrucción help().


## Tema 6: Aspectos avanzados

Pregunta 1
Ejecutando el siguiente código, ¿qué resultado se mostrará al final de la ejecución? 

import re 
 
mensaje = 'Hola, me gusta estudiar Python' 
re.sub('\w{4},', 'Buenos días', mensaje) 


Pregunta 1Respuesta

«Buenos días me gusta estudiar Python».


Pregunta 2
En el siguiente ejemplo, ¿qué patrón se está buscando? 

string ='Hoy hemos comido 10 personas un menú de 12 euros. y 2 niños 2 bocadillos de 4 euros. En total pagamos 128 euros.'

result =re.findall('\d+', string)

   print(result)


Todos los números que hay en la cadena de caracteres, es decir, ['10', '12', '2', '2', '4', '128'].

Pregunta 3

¿Qué devuelve la función match() cuando no ha encontrado ningún resultado en la cadena de caracteres?

None.

Pregunta 4
¿Qué es una excepción?

Un bloque de código que permite continuar la ejecución de un programa cuando se ha detectado un error.

Pregunta 5
¿Cuándo se ejecuta el bloque else en las sentencias try-except?


Se ejecuta cuando no ha habido ningún error en el bloque try.

Pregunta 6

¿Cuándo se ejecuta el bloque finally en las sentencias try-except?


Se ejecuta siempre, se produzca o no se produzca un error.

Pregunta 7
¿Qué resultado devolverá la ejecución del siguiente código?

try:

    'hola'+ 5

except ValueError:

    print('Error 1')

except TypeError:

    print('Error 2')

except:

    print('Error 3')

Pregunta 7Respuesta

Error 2.

Pregunta 8
¿Qué lista devolverá el siguiente bloque de instrucciones?
lista =list(range(1,10)) [x / 2 for x in lista if x * 4 < 15]


[0.5, 1.0, 1.5].

Pregunta 9
¿Qué estructuras de datos se pueden crear con la técnica de compresión?


Listas, conjuntos y diccionarios.


Pregunta 10

Texto de la pregunta
A partir de la siguiente lista, queremos crear un diccionario donde, por cada elemento, la clave sea el nombre del usuario y el valor, la edad. En el diccionario solo guardaremos aquellos usuarios menores de 35 años. ¿Cuál de las siguientes sentencias se debería utilizar? 

usuarios =[['Juan', 33], ['Alicia', 28], ['Rebeca', 56]]

Pregunta 10Respuesta


{item[0]: item[1] for item in usuarios if item[1] < 35}.

## Tema 7: analisis de datos - Numpy y pandas 

Pregunta 1

¿Cómo se puede crear una matriz con 3 filas y 3 columnas usando numpy?
Pregunta 1Respuesta

np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).

Pregunta 2
numpy es una librería útil para:

Cálculo de vectores y matrices.

Pregunta 3
pandas es:

Una librería para facilitar el tratamiento de datos.

Pregunta 4
Para obtener con pandas la información estadística de la estructura e información contenida en un dataframe llamamos a la función:
Pregunta 4Respuesta


describe().


Pregunta 5
La función iloc de pandas:

Nos permite acceder a los valores a través de la posición del índice.


Pregunta 6
La sentencia df[df.A>0]:

Muestra solo las filas de df que en su columna A tienen un valor mayor que cero.


Pregunta 7

¿Qué hace la función groupby() en pandas?
Pregunta 7Respuesta

Permite agrupar los datos según los valores de las columnas especificadas por el argumento by=.

Pregunta 8

¿Qué hace la función substract() en numpy?
Pregunta 8Respuesta

Resta los valores de dos arrays elemento por elemento.


Pregunta 9

¿Qué función nos permite ordenar un dataframe por su índice?
Pregunta 9Respuesta


sort_index().



Pregunta 10

¿Cómo tengo que llamar a la función read_csv() para leer un fichero prueba.csv donde los valores están separados por punto y coma (;)?
Pregunta 10Respuesta


read_csv('prueba.csv', sep=';').

