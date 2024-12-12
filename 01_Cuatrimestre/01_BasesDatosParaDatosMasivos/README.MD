

## Tema 1. Métodos de captura de información

## 1.2. Origen y calidad de los datos

**Datos, información y conocimiento**

- En situaciones informales es común usar indiscriminadamente los términos dato,
información y conocimiento. En ámbitos profesionales y académicos, es
conveniente distinguir estos conceptos para evitar malinterpretaciones durante las
distintas fases de la analítica de datos.

- La información puede distinguirse simplemente como un mensaje formado por la
composición de varios datos.

- Los datos deben ser transformados para añadirles valor y convertirlos en
información. 

- Estas transformaciones incluyen métodos como:
    - Contextualización: conocer el propósito del dato obtenido.
    - Categorización: conocer la unidad de medida y los componentes del dato.
    - Cálculo: realizar una operación matemática sobre el dato.
    - Corrección: eliminar errores del dato.
    - Agregación: resumir o minimizar un dato de forma más concisa.

- El conocimiento implica una combinación de experiencias, información contextual y
relevancia sobre cierta información. Así como la información se genera a partir de
datos, el conocimiento surge de la agregación de información. 

**Ejemplos de métodos que generan esta transformación son:**
- Comparación: relación entre información obtenida en distintas experiencias.
- Repercusión: implicación de la información en decisiones y acciones.
- Conexión: relación entre distintos tipos de información.
- Conversación: opinión de otras personas sobre la información.



## 1.3. Organización de los datos

**Ficheros planos* 
Los ficheros planos suelen ser un mecanismo utilizado para el intercambio de
información entre sistemas. Una de sus ventajas es que es posible ver y editar el
contenido del fichero con una herramienta de edición de texto.

Estos ficheros suelen ser mucho más verbosos que los ficheros en formato binario, lo
cual implica que su tamaño en el sistema de ficheros será mayor, así como las
operaciones necesarias para procesar el contenido desde un programa de software.

**Entre los formatos de fichero plano más comunes se pueden mencionar**  
- CSV 
- JSON
- XML. 



**Bases de datos**
Una base de datos es un conjunto de datos persistente utilizado por un sistema de
software. Siguiendo con las definiciones, y tal y como se menciona en la bibliografía,
un sistema de base de datos es un sistema computarizado para el almacenamiento
de registros. Se pueden mencionar cuatro componentes de un sistema de esta
categoría:

- Datos. Los datos en un sistema de base de datos pueden definirse como
integrados, en aquellos casos en que todos los datos se mantienen unificados y
comúnmente serán accedidos por una sola persona, así como compartidos, para
aquellos casos en los que se desea mantener los conjuntos de datos separados y
otorgar privilegios de acceso distintos a varias personas.


- Hardware. Como en otros métodos de almacenamiento, los componentes de
hardware que intervienen en un sistema de base de datos son los volúmenes de
almacenamiento, así como los procesadores y memoria principal.

- Software. La capa de software entre el usuario y la base de datos física se conoce
como DBMS (Database Management System o sistema gestor de la base de datos).
Usuarios. Existen tres clases de usuarios en un sistema de bases de datos:
Programadores: encargados de crear aplicaciones que permitan la interacción con
la base de datos.

- Usuarios finales: utilizan las distintas aplicaciones y herramientas para interactuar
con la base de datos.

- Administrador de base de datos: también conocido como DBA por sus siglas en
inglés, se encarga de gestionar la estructura, disponibilidad y eficiencia del sistema
de base de datos.


## Cuestionario 

1. ¿Cuál es la unidad semántica mínima que puede almacenarse o comunicarse?
A. Dato.
B. Información.
C. Conocimiento.
D. Las respuestas A y B son correctas.
2. ¿Qué métodos pueden utilizarse para la transformación de información a
conocimiento?
A. Contextualización, agregación y cálculo.
B. Repercusión, conexión y conversación.
C. Categorización, corrección y agregación.
D. Análisis, investigación y discusión.
3. ¿Qué métrica de calidad describe la proporción en la que un conjunto de datos
contiene a la población que representa?
A. Precisión.
B. Consistencia.
C. Completitud.
D. Interpretabilidad.
4. ¿Cuál de los siguientes es un ejemplo de método de captura manual?
A. Web scraping.
B. Encuestas.
C. Acceso a bases de datos relacionales.
D. Lectura de termómetro digital.
Test
Bases de Datos para el Big Data
Tema 1. Test
44
5. ¿En qué categoría de captura de datos entra la lectura de información del
acelerómetro y giroscopio de un teléfono móvil?
A. Captura manual.
B. Procesamiento de documentos.
C. Acceso a datos públicos.
D. Sensores.
6. ¿Qué elemento es utilizado para delimitar valores en un fichero CSV?
A. Coma.
B. CRLF.
C. Comillas dobles.
D. Espacio.
7. ¿Sobre qué estructuras se basa el formato JSON?
A. Objetos y diccionarios.
B. Tablas hash.
C. Objetos y arrays.
D. Listas enlazadas.
8. ¿Cuál de las siguientes condiciones sobre XML es verdadera?
A. Un documento solo puede tener un elemento raíz.
B. El contenido de un elemento debe ser otro elemento.
C. Todo elemento debe tener un atributo llamado «id».
D. Los atributos deben de ser de tipo numérico.
Test
Bases de Datos para el Big Data
Tema 1. Test
45
9. ¿Qué nombre recibe un conjunto de datos persistente utilizado por un sistema de
software?
A. Archivo.
B. Base de datos.
C. Registro.
D. Las respuestas A y B son correctas.
10. ¿Cuál es la instrucción de SQL para consultar información?
A. SELECT.
B. INSERT.
C. UPDATE.
D. DELETE.



## Tema 2. NoSQL

## 2.1. Introducción y objetivos


**Concepto** 
>  El término NoSQL se definió en 2009 con el fin de agrupar todas aquellas bases de datos no relacionales que estaban ganando popularidad en ese momento. 
- El término NoSQL hace alusión a métodos de almacenamiento no necesariamente estructurados
- cuyo nombre se refiere al lenguaje de consulta «no es SQL» o «no solo es SQL», «Not only SQL».

**Caracteristicas** 
- No es una tecnilogia tan nueva se ideo en los 60 
- El nombre NoSQL fue utilizado por Carlo Strozzi en 1998
- En esa fecha aun seguia siendo una base datos relcional solo era una interfaz SQL por lo que formaba parte del movimiento SQL 
- El término volvió a surgir en 2009
- **Eric Evans** lo utilizo para referirse al continuo aumento de bases de datos no relacionales. 
- Aunque el nombre naciera en 2009, las bases de datos NoSQL se remontan a la época de las bases de datos de red y jerárquicas
- otras tendencias NO SQL como Las bases de datos MultiValue fueron desarrolladas por TRW en 1965.
- En 1966 se desarrolló en el Hospital Mass General un lenguaje de programación que incorpora
una base de datos jerárquica con almacenamiento de árbol B+
- IBM IMS con Rockwell y Caterpillar desarrollaron una base de datos jerárquica para
el programa espacial Apolo en 1966 
- Las bases de datos NoSQL fueron diseñadas precisamente para ser escalables y
distribuidas

## 2.2. Descripción y tipos de bases de datos NoSQL

**Categorías conocidas**

> Las bases de datos NoSQL pueden clasificarse en cuatro grandes categorías:

- Almacenes de clave-valor simples: Como su nombre indica, utilizan una clave
para acceder a un valor en específico. Los valores almacenados se manejan como
arrays de bytes, es decir, sin ningún esquema específico asignado. Su aplicación es
común en sistemas de caché. Uno de los sistemas más conocidos en esta categoría
es memcached, el cual es el sistema de facto para la gestión de caché de datos en
aplicaciones web.

- Almacenes de clave-valor sofisticados: Estos sistemas son un refinamiento de la
categoría anterior con el objetivo de permitir operaciones de lectura y escritura más
complejas, así como un modelo de datos ligeramente más elaborado. Ejemplos de
sistemas en esta categoría son Cassandra, Dynamo, Voldemort y Riak

- Almacenes de documentos: Los sistemas dentro de esta categoría permiten
almacenar estructuras de datos relativamente complejas. Las implementaciones más
conocidas en este grupo son CouchDB y MongoDB

- Almacenes de grafos: Las bases de datos que entran en esta categoría son las que
almacenan la información en estructuras de grafos, cuyos nodos representan la
información y las aristas, sus relaciones. Las bases de datos de grafos brindan la
facilidad de consultar su información aplicando teoría de grafos.

- multimodelo: entro de este tipo de bases de datos se encuentra Redis. Redis es una base de
datos NoSQL multimodelo que permite búsquedas, mensajería, transmisión, grafos y
otras capacidades más allá de las que ofrece un simple almacén de datos

## 2.3. Teorema CAP

**Concepto**
> (que pueda crecer sin mayores contratiempos) y que además trabaje en entornos distribuidos.

´´´El teorema CAP, o también llamado teorema Brewer, indica que todos los sistemas
distribuidos no pueden garantizar a la vez que haya consistencia, disponibilidad y
tolerancia a particione´´´


- Consistencia: sin importar qué servidor reciba la petición, cuando se realiza una
consulta o se hace una inserción, el sistema siempre debe devolver la misma
información de respuesta.

- Disponibilidad: la caída de uno o más nodos no debe ser un impedimento para que
los clientes puedan leer y escribir peticiones.

- Tolerancia a particiones: hace referencia al hecho de que el sistema tiene que
seguir funcionando, aunque existan fallos o caídas parciales que dividan el sistema.
La división por particiones es una característica de los sistemas distribuidos que
permite canalizar grandes flujos de peticiones.

**Según sus capacidades, es posible ver cómo las distintas bases de datos cumplen al
menos dos de los criterios indicados por el teorema CAP.** 


- CA: garantizan la consistencia y la disponibilidad en la base de datos, pero no
suelen ser óptimas al manejar la tolerancia a particiones. Para cubrir esta
deficiencia, lo que suelen hacer es replicar los datos.

- AP: garantizan la disponibilidad y la tolerancia a particiones, pero no suelen ser
buenas tratando la consistencia. Determinados motores logran una consistencia
parcial mediante técnicas de replicación y verificación.

- CP: garantizan la consistencia y la tolerancia a particiones, pero sacrifican la
disponibilidad al replicar los datos entre los distintos nodos con el fin de asegurar la
consistencia

2.4. Elección de base de datos: NoSQL vs. SQL

> Se puede decir que las bases de datos tradicionales son las bases de datos relacionales, que usan un lenguaje estándar para su manipulación y gestión. 
- Su éxito se basa en que es una solución para los problemas de gestión y estructuración de la
información de las organizaciones. 
- Se basa de usar un un fundamento matemático muy fuerte.
- Se apoya en lenguaje estandarizado con metodologías estructuradas para el diseño de los
sistemas de información
- Se rigen por el principios de diseño como la regla ACID (Atómica Consistente Aislada y Durable).

> Las NoSQL son un conjunto de bases de datos que no se ajustan al modelo de base de datos relacional y se caracterizan por no tener esquema, 
- Por no utilizar SQL ni permitir joins, por no garantizar la propiedad ACID, por escalar horizontalmente, 
- Por hacer uso amplio de la memoria principal del ordenador.
- por resolver el problema de los altos volúmenes de información y la inmensa cantidad de consultas y transacciones diarias. 

**Ejemplo**

Una de las características de NoSQL, como ya se ha dicho antes, es la flexibilidad
que proporciona para el uso de modelos de datos, la cual permite tener registros con
modelos diferentes. Se puede disponer de registro en el que el atributo «color»
aparezca o exista y de registros similares que no contengan dicho atributo, y en otros
casos que el atributo sea un array o una cadena de caracteres, sin que ocasione
ningún tipo de error en base de datos.

**Ventajas**
- Responden a la necesidad de escalabilidades horizontal demandada cada vez por más empresas y, además, de manera sencilla.
- No generan cuellos de botella.
- Permiten manejar grandes volúmenes de datos.
- Se pueden tener diferentes bases de datos NoSQL para diferentes proyectos.
- Equipos económicos para la puesta en marcha.

**desventajas**
- No ofrecen tanto soporte y nombre como lo hacen bases de datos como Oracle, IBM o Microsoft. 
- Generalmente un vendedor de código abierto no tiene el alcance global, servicios de soporte y la credibilidad de Oracle o IBM.
- No están lo suficientemente maduras para algunas empresas.
- Limitaciones de inteligencia de negocios. 

Por el momento, las bases de datos
NoSQL no tienen buena aceptación con las herramientas de BI, lo que origina que
una consulta ad hoc y su análisis implica conocimientos avanzados de
programación. Sin embargo, esta tendencia está cambiando, por ejemplo, Quest
Software ha creado Toad para bases de datos en la nube, que proporciona
capacidades de consulta ad hoc para algunas bases de datos NoSQL.

- La falta de experiencia. Debido a que NoSQL es una tecnología novedosa, no hay
una gran cantidad de desarrolladores y administradores que la dominen

- Problemas de compatibilidad. A diferencia de las bases de datos relacionales, que
comparten ciertos estándares, las bases de datos NoSQL tienen pocas normas en
común. Cada base de datos NoSQL tiene su propia API, las interfaces de consultas
son únicas y tienen peculiaridades. Esta falta de normas hace difícil el cambio de
unos proveedores a otros.

2.5. Bases de datos NoSQL


**Cassandra**
Apache Cassandra es una base de datos NoSQL distribuida de código abierto escrita
en Java. Está basada en un modelo de almacenamiento clave-valor y se caracteriza
en que los nodos que componen el sistema de datos actúan por igual agrupándose
en un anillo o clúster

**Caracteristicas**
Modelo  
- Clave-Valor

Arquitectura 
- Descentralizada 

Sistema de datos 
- Anillos o clouster
- Permite configurar un sistema de replicas 
- Tienes tablas filas y columnas 
- Las filas tienen una clave de aprticiona 
- las columnas tiene un clave valor para interactuar con los datos
- Usa CQL es una simplificacion de sql 
- Usa Shell para accder a los datos



**Neo4j**
Es un sistema de gestión de base de datos basada en grafos, desarrollado por Neo
Technology, Inc en Java lanzada en febrero del 2010. Descrito por sus
desarrolladores como una base de datos transaccional compatible con ACID con
almacenamiento y procesamiento de grafos nativos.

Un grafo se compone de dos elementos: un nodo y una relación. Cada nodo
representa una entidad (una persona, un lugar, una cosa, una categoría u otra pieza
de datos) y cada relación representa cómo se asocian dos nodos. 

Esta estructura de propósito general permite modelar todo tipo de escenarios, desde un sistema de
carreteras hasta una red de dispositivos, la historia médica de una población o
cualquier otra cosa definida por las relaciones.
Una base de datos de grafos es un sistema de gestión

**Caracteristicas**
- Estas BD estan disenadas para operaciones transaccionales
- Usa almacenamiento nativo 
- Rendimiento en mejora significativa en consultas relacionales 
- Flexibilidad se adapta rapidamente  
- Agilidad se integra con desarrollos agiles 
- usado para deteccion de fraudes, Motores de recomendaciones en tiempo real, gestion de datos maestros, gestion de identidad acceso. 
- Tiene software comunitario 


**MongoDB**

MongoDB (que proviene de humongous) es una de las bases de datos NoSQL
orientada a documentos desarrollada bajo el concepto de código abierto. Es una de
las bases de datos NoSQL más utilizadas en todo el mundo.
Es una base de datos ágil, que permite a los esquemas cambiar rápidamente cuando
las aplicaciones evolucionan, proporcionando siempre la funcionalidad que los
desarrolladores esperan de las bases de datos tradicionales, tales como índices
secundarios, un lenguaje completo de búsquedas y consistencia estricta
En MongoDB, los datos se almacenan en forma de un documento, el cual es una
estructura con pares clave-valor, muy similares a los objetos JSON, con la salvedad
de que MongoDB almacena los datos en formato BSON (representación binaria de
JSON). Un documento posee un atributo especial llamado _id, el cual indica el valor
que identifica de forma inequívoca al documento.
A su vez, los documentos se almacenan en collections, formando así un conjunto
de documentos con atributos similares. Podría decirse que una collection equivale a
una tabla en una base de datos relacional. Así, se puede definir una base de datos
en MongoDB como un conjunto de collections.

**Caracteristicas**


**Patrones de diseño en MongoDB**
Los patrones de diseño en MongoDB pueden agruparse en dos categorías. La
primera incluye aquellos patrones que soportan relaciones entre documentos:

Patrón de relación uno-a-uno con documentos embebidos: en este patrón se
embebe un documento dentro de otro con el cual tiene relación. Por ejemplo, se
puede contar con un documento de información de un usuario y embeber un
subdocumento con información de la dirección del usuario:
{ _id: "1", nombre: "Juan", direccion: { ciudad: "Madrid" } }

Patrón de relación uno-a-muchos con documentos embebidos: en este patrón
se embebe a varios documentos dentro de otro con el cual tiene relación. Siguiendo
con el ejemplo anterior, es probable que el usuario tenga más de una dirección, por
lo que se tiene una relación de uno (usuario) a varios (direcciones).
{ _id: "1", nombre: "Juan", direcciones: [ { ciudad: "Madrid" }, { ciudad:
"Toledo" } ] }

Patrón de relación uno-a-muchos con documentos referidos: este patrón se
suele utilizar para evitar repetición en aquellos casos en que un mismo documento
se desee embeber en otros varios. Un ejemplo de su aplicación es el siguiente:
{ _id: address1, ciudad: "Madrid" }, 
{ _id: address2 ciudad: "Toledo" }, 
{ _id:"1", nombre: "Juan", direcciones: [address1, address2] }

Patrón de relación uno-a-uno con documentos referidos: igual que el anterior,
pero solo a un documento. No es aconsejable su utilización, debido a que es más útil
utilizar documentos embebidos.
{ _id: address ciudad: "Toledo" }, 
{ _id: "1", nombre: "Juan", direcciones:address }

Patrón de modelo de estructura de árbol con referencias al nodo padre . Tal
como indica el nombre, se mantiene un atributo que almacena el _id del nodo padre.
A continuación, se muestra un ejemplo con documentos representando carpetas de
un sistema de ficheros.
{ _id: folder1, nombre: "Raíz", parent: null }, 
{ _id: folder2, nombre: "Folder 2", parent: folder1 } 
{ _id: folder3, nombre: "Folder 3", parent: folder1 }

El modelo de estructura de árbol con referencia a nodo hijo. Como indica el
nombre, implica una aproximación inversa al caso de referencias al nodo padre. El
ejemplo anterior se vería representado de la siguiente manera.
{ _id: folder1, nombre: "Raíz", children: [folder2, folder3] }
, { _id: folder2, nombre: "Folder 2", children: [ ] } 
, { _id: folder3, nombre: "Folder 3",children: [ ] }

**Notas Mongo DB** 
se compara como es mongo vs BD relacional 
![Ejemplo](../01_BasesDatosParaDatosMasivos/info/info_001.png)

**Capsulas**
- https://unir.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=b93f2fb1-390b-496b-9124-aca70108f754



![Ejemplo](../01_BasesDatosParaDatosMasivos/info/info_002.png)


## Cuestionario 

1. ¿Qué tipo de base de datos NoSQL se caracteriza por operaciones de lectura y
escritura básicas, además de ser apropiados para entornos de gestión de caché?
A. Almacén clave-valor simple.
B. Almacén clave-valor sofisticado.
C. Base de datos relacional.
D. Almacén de documentos.
2. ¿En qué categoría de base de datos NoSQL se clasifica a MongoDB?
A. Almacén clave-valor simple.
B. Almacén clave-valor sofisticado.
C. Base de datos relacional.
D. Almacén de documentos.
3. ¿Cuál de las siguientes afirmaciones es correcta?
A. Cassandra se caracteriza porque todos sus nodos actúan por igual y se
agrupan en anillo.
B. Cassandra y Neo4j están desarrolladas en Java.
C. Neo4j es una base de datos transaccional compatible con ACID y que
almacena y procesa grafos nativos.
D. Todas las afirmaciones anteriores son correctas.
4. ¿Cuál es el equivalente a un registro en MongoDB?
A. Base de datos.
B. Collection.
C. Tabla.
D. Documento.
Test
Bases de Datos para el Big Data
Tema 2. Test
35
5. ¿Cuál es el término equivalente a una tabla en MongoDB?
A. Base de datos.
B. Collection.
C. Registro.
D. Documento.
6. ¿Cuándo se detalla el uso de la primera base de datos NoSQL?
A. En 2007, cuando Amazon liberó DynamoDB.
B. Con Carlo Strozzi en 1998.
C. En 1965 con MultiValue.
D. Eric Evans en 2009.
7. ¿Cuál de las siguientes es una ventaja de las bases de datos NoSQL?
A. No generan cuellos de botella.
B. Tecnología madura.
C. Responden a la necesidad de escalabilidades horizontal demandada cada
vez por más empresas y, además, de manera sencilla.
D. Las respuestas A y C son correctas.
8. ¿Cuál de las siguientes afirmaciones es correcta?
A. Todo sistema distribuido no puede garantizar a la vez que haya
consistencia, disponibilidad y tolerancia a particiones.
B. Un sistema distribuido garantiza al menos disponibilidad y consistencia.
C. Un sistema distribuido que garantiza la consistencia y la tolerancia a
particiones no sacrifica por ello la disponibilidad.
D. Todas las afirmaciones anteriores son correctas
Test
Bases de Datos para el Big Data
Tema 2. Test
36
9. ¿Qué patrón de diseño de MongoDB permite incluir un documento dentro de
otro?
A. Uno-a-uno con documentos embebidos.
B. Uno-a-uno con documentos referidos.
C. Uno-a-varios con documentos referidos.
D. Las respuestas B y C son correctas.
10. ¿Qué patrón de diseño de MongoDB permite incluir una lista de referencias a
otros documentos dentro de un documento principal?
A. Uno-a-uno con documentos embebidos.
B. Uno-a-uno con documentos referidos.
C. Uno-a-varios con documentos referidos.
D. Las respuestas B y C son correctas.


## Tema 3. MongoDB

## 3.2. Descarga e instalación

## La instalación de MongoDB puede realizarse en el sistema operativo Windows mediante los siguientes pasos:

- Paso 1: descarga el fichero de instalación, en formato zip o msi, desde la siguiente
dirección web: http://www.mongodb.org/downloads

- Paso 2: en la pestaña Community Server habrá que descargar el archivo msi de
instalación. Si el sistema operativo que va a soportar la instalación es de 64 bits, se
recomienda elegir la versión de Windows. Esta versión funciona en casi todas las
versiones de Windows de 64 bits.

- Paso 3: en el caso de no tener un sistema operativo de 64 bits o querer una versión
anterior, en el enlace All Version Binaries se pueden encontrar todas las versiones
de la base de datos.

- Paso 4: instalar la aplicación siguiendo los pasos. Es recomendable utilizar un
directorio de instalación conocido, por ejemplo, C:/MongoDB/

- Paso 5: inicia el servidor de MongoDB ejecutando el programa mongod.exe, ubicado
en la subcarpeta bin.
Ten presente: a partir de la versión 3.x.x de MongoDB, el instalador sobre Windows
crea el servicio y lo incluye en la lista de procesos o servicios que ejecutará el
sistema operativo.

## La instalación de MongoDB puede realizarse en el sistema operativo MAC mediante los siguientes pasos:

- Paso 1: Me toco decsrgar el COMPASS GUI para gestionar datos en mongoDB y con mi cuenta online de Mongo para usar la herramienta en mac
- Paso 2: Descargra e instalar Compass GUI -> https://www.mongodb.com/try/download/compass 
- Paso 3: Me gusta usar la version Mongo enlinea por lo que tengo un clouster activo para mis ejemplos. 

## Directorios de la instalación
Una vez instalado, en el directorio de instalación podréis encontrar los siguientes
subdirectorios:
- bin: todos los programas que necesita Mongo para ejecutarse.
- data: el directorio donde por defecto se crearán las bases de datos.
- log: un fichero con todas las trazas de log del motor y de los accesos al servidor
mondodb.
- snmp: ficheros de configuración para una instancia de mongod como un subagente
SNMP. Esto es útil en la versión Enterprise.


a. mongod: Este es el demonio principal de MongoDB, encargado de gestionar la base de datos. Es esencial para el funcionamiento de cualquier instancia de MongoDB.

b. mongos: Este es el proceso que actúa como router en una configuración de sharding (particionamiento) de MongoDB. Coordina las solicitudes de lectura y escritura entre los diferentes shards.

c. mongostat: Esta es una herramienta de línea de comandos que proporciona estadísticas en tiempo real sobre el rendimiento de una instancia de MongoDB. Es muy útil para monitorear la salud y el desempeño de tu base de datos.

d. mongored: ¡Este es el que no existe! No hay ningún comando o ejecutable de MongoDB llamado "mongored". Es probable que haya sido una opción creada para confundir en una prueba o ejercicio.




## 3.3. Software de apoyo

## MongoBooster
MongoBooster es una herramienta GUI multiplataforma basada en shell para
MongoDB a partir de la versión 2.4, que permite la construcción de consultas fluidas,
soporte de sintaxis ES6, una experiencia IntelliSense y un gran número de
herramientas útiles para el manejo de la base de datos.

## MongoDB Compass
MongoDB también posee un software propio para la manipulación externa de su
base de datos a través de una GUI. Esta aplicación permite ejecutar consultas ad
hoc en segundos, interactuar con sus datos con funcionalidad CRUD completa y ver
y optimizar el rendimiento de la consulta. Está disponible para la mayoría de los
sistemas operativos. Compass permite tomar decisiones más inteligentes sobre la
indexación, la validación de documentos y mucho más.

## 3.4. Flexibilidad del modelo de datos

MongoDB tiene un esquema flexible, donde no es necesario que las colecciones
tengan una estructura idéntica para todos los documentos. Esto significa que los
documentos de la misma colección no necesitan tener el mismo número de campos
o estructura. Cada documento solo necesita contener un número relevante de
campos de la entidad u objeto que el documento representa.

## 3.5. Inserción de datos

Por ejemplo, si se desea crear un nuevo documento con información sobre un
producto en específico, dentro de la collection llamada productos, el comando sería
el
´´´
// Create a new database.
use(database);

// Create a new collection.
db.createCollection(productos);

//Insert 
db.productos.insert({nombre: “Jabón líquido”, precio: 5.50})
db.productos.save({nombre: "Mantequilla", precio: 3.50}) 

//Ten en cuenta que, a partir de MongoDB 4.2, el método db.collection.save() está en
//desuso, en versiones inferiores sí podrás seguir utilizándolo.

db.productos.find()
´´´


## 3.6. Lectura de datos

El comando utilizado en MongoDB para realizar consultas es find , con la siguiente
sintaxis:
´´´
db.<nombre de Collection>.find(<criterios de búsqueda>, <proyección>)
´´´
**Caracteristicas**
- Ambos argumentos son opcionales y, en caso de definirlos, deben seguir el formato
JSON. 
- Los criterios de búsqueda son las condiciones, que los documentos
resultantes deben cumplir. 
- Las condiciones se estructuran en pares clave-valor, donde el valor puede ser de tipo primitivo (número, cadena de texto, etc.) o un objeto para el uso de tres operadores de comparación:
- $gt, $gte, $lt, $lte, $ne: para la evaluación de condiciones «mayor que», «mayor o
igual que», «menor que», «menor o igual que» y «es diferente a».
- $in, $nin: evalúan la pertenencia y ausencia respectivamente de un atributo en un
array dado.
- $exists: evalúa que exista el atributo indicado.
- $type: evalúa que el campo sea de un tipo específico.
- $all: evalúa arrays que coincidan completamente con el parámetro dado.
- $elemMatch: permite evaluar arrays a nivel de elementos, de forma muy específica.
- Además, pueden utilizarse los operadores lógicos $or, $and, $not y $nor, los cuales
reciben un array de expresiones a evaluar en conjunto. MongoDB también brinda operadores para búsquedas de información geoespacial.
- Los resultados obtenidos a partir de una consulta pueden transformarse mediante
cualquier combinación de tres operaciones:
  - limit: indica la cantidad máxima de documentos a mostrar. 
  - skip: indica la cantidad de documentos a omitir al inicio en un inicio.
  - sort: indica, a través de pares clave-valor donde la clave es el atributo sobre el que se ordenará y el valor es 1 para un orden ascendente y -1 para un orden
descendente

En resumen:

Las llaves y corchetes son fundamentales en MongoDB para estructurar los documentos y las consultas. Comprender su uso te permitirá escribir consultas más complejas y eficientes para manipular tus datos.

Notas: 
- Recuerda usamos las llaves para muchas cosas pero la razon principal es exponer el objeto json que se desea encontrar 
Ejemplo
´´´
db.getCollection('books').aggregate(
  [
    {
      $group: {
        _id: {
          hasPages: {
            $cond: [
              { $eq: ['$pageCount', 0] },
              'Libros 0 páginas',
              'Libros con páginas'
            ]
          }
        }, // creo un elemento llamado hasPages
        count: { $sum: 1 } // creo un elemento llamado count
      }
    }
  ]
);
´´´
- los corchetes lo podemos usar para las operacion del documento y llegar al atributo del documento ejemplo ['$pageCount']
- El simbolo $ es para indicar que deseamos ese atributo del documento en alguna operacion 

Ejemplo 

´´´
db.productos.find()
db.productos.find({precio:1})
db.productos.find({precio: {$lte: 1} })
db.productos.find({precio: {$gt: 1, $lt: 2} })
db.productos.find({ $and: [{precio: {$gt: 1}}, {precio: {$lt: 2}} ]})
db.productos.find({ $and: [{precio: {$gt: 1}}, {precio: {$lt: 2}} ]},{_id: 0, nombre: 1})
db.productos.find().sort({precio: -1}).limit(2)
´´´

## 3.7. Actualización de datos

Los criterios de búsqueda del comando update siguen las reglas indicadas para el
comando find. 

Por defecto, el documento que cumpla con esos criterios se reemplaza por el documento enviado como segundo argumento. 
Si lo deseado es realizar un cambio específico, se pueden utilizar los siguientes operadores:

- $set: permite crear o cambiar un atributo en específico.
- $unset: permite eliminar un atributo.
- $inc: incrementa un número.
- $rename: cambia el nombre de un atributo.

Las opciones de modificación pueden ser dos:
- multi: por defecto, update solamente modifica un documento. Si el modificador
multi tiene el valor true , se modificarán todos los documentos que cumplan con las
condiciones de búsqueda.
- upsert: si ningún documento cumple con las condiciones de búsqueda y upsert se
define con el valor true , el comando update creará un documento.


´´´
db.productos.update({ precio: { $gte: 2}}, {$set: {precio: 3}}, {multi:true})
db.productos.updateMany({ precio: { $gte: 2}}, {$set: {precio: 7.5}})
db.productos.updateOne({ precio: { $gte: 7}}, {$set: {precio: 8.555}})
db.productos.find() 

db.inventario.deleteMany({ estado : "B" })

´´´


## 3.8. Caso práctico

Nota: Podemos usar la IA  de mongo DB para generar consultas un ejemplo puede ser 
- I want to get How many books have 0 pages and how many do not from the books collection

db.getCollection('books').find({longDescription: {$gte: "A", $lt: "B"}}, {title: 1, longDescription: 1})

db.getCollection('books').find({status: "PUBLISH"}, {title: 1, longDescription: 1, status:1, authors:1})


## MongoDB y sus IDEs

> MongoBooster

MongoBooster es una herramienta GUI multiplataforma basada en shell para MongoDB a partir de la versión 2.4.

**Características:**

- Construcción de consultas fluidas.
- Soporte de sintaxis ES6.
- Experiencia IntelliSense para autocompletar.
- Lector Shell integrado.
- Utilidad para crear colecciones aleatorias.
- Herramientas de monitorización y estadísticas.
- Schema Analyzer para describir el esquema de las colecciones. 
- Versiones: Dispone de una versión gratuita con ciertas limitaciones después de los 60 días de prueba.

## MongoDB Compass

> MongoDB 
Compass es el software de MongoDB para la manipulación externa de la base de datos a través de una GUI.

**Funcionalidades:**

- Ejecución de consultas ad hoc.
- Funcionalidad CRUD completa.
- Análisis y optimización del rendimiento de las consultas.
- Visualización intuitiva de la estructura de los documentos.
- Estadísticas del servidor en tiempo real.
- Exploración de operaciones de la base de datos.
- Construcción de consultas complejas de manera sencilla.
- Modificación, inserción y borrado de documentos mediante un editor visual.
- Creación y modificación de reglas de validación de datos.
- Utilidad: Facilita la comprensión y manipulación de los datos almacenados en MongoDB a través de una interfaz gráfica intuitiva.


## Recordar

- Comando insert: utilizado para crear documentos en una colección.
  - Sintaxis: db.<nombre de Collection>.insert(<documento a almacenar>).
- Atributo _id: MongoDB genera automáticamente un _id de tipo Objectld para garantizar la unicidad de los documentos.
- Inserción Múltiple: Utiliza insertMany([...]) con un array de documentos como argumento.
- Comando save:
  - Sintaxis: db.<nombre de Collection>.save(<documento a almacenar>).
  - Similar a insert, pero reemplaza el documento existente si el_id coincide.

## Observaciones:
- Uso de try-catch para manejar errores.
´´´
try {
db.productos.insertMany( [
...
] );
} catch (e) {
print (e);
}
´´´
- Consulta de documentos con db.productos.find().
- Modificación y reemplazo de documentos existentes.
- Uso de_id para identificar documentos existentes.
  - Desuso de save:
    - A partir de MongoDB 4.2, el método db.collection.save() está en desuso.
- Interacción con la audiencia:
  - Se fomenta la participación y comentarios en el foro sobre los resultados de las operaciones.




## MongoDB y Las operaciones de lectura y actualización

> Lectura de datos en MongoDB
- Comando find:
  - Utilizado para leer u obtener datos de una colección.
  - Sintaxis: db.<nombre de Collection>.find(<criterios de búsqueda>, <proyección>).

- Criterios de búsqueda:
  - Condiciones que los documentos deben cumplir.
  - Operadores de comparación como $gt, $It, $gte, $lte, etc.
  - Operadores lógicos como $or, $and, $not, etc.
  - Operadores para búsquedas geoespaciales.

- Proyección:
  - Indica qué atributos mostrar u ocultar en los resultados. Formato: lista de pares clave-valor.
  - Uso del operador punto para atributos de subdocumentos.

- Transformación de resultados:
  - limit: indica la cantidad de documentos que deseamos ver -> db.usuarios.find().sort({ edad: -1 }).limit(5)
  - skip : lo usamos para omitir la cantidad de docummentos al principio de la consulta ->  db.usuarios.find().skip(10).limit(10) -> Si tienes una colección de usuarios y quieres obtener los usuarios del 11 al 20, sin importar el orden, podrías usa
  - Sort: lo usamos para ordenar los documentos 1 = ASC -1 = DESC 

- Comando findOne:
  - Utilizado para encontrar un solo documento. Argumentos similares al comando find.
  - Interacción con la audiencia:
  - Se fomenta la participación y comentarios sobre los ejemplos y resultados de las consultas.
  - Se pueden realizar ejercicios prácticos para reforzar el entendimiento de los comandos.

- Comando Update:
  - Utilizado para modificar documentos que coinciden con un criterio de búsqueda.
  - Sintaxis antes de la versión 2.2 y a partir de la misma.

´´´
db.Employee.update
(
	{
		Employeeid : 1
	},
	{
		$set :
		{
			"EmployeeName" : "NewMartin",
			"Employeeid" : 22
		}
	}
)

# Comando para indicar Join equivalente al SQL

db.users.aggregate([
  {
    $lookup: {
      from: "orders", // Colección a unir
      localField: "_id", // Campo de la colección actual
      foreignField: "userId", // Campo de la colección a unir
      as: "orders" // Nombre del campo en el resultado
    }
  }
])
´´´


- Operadores de Modificación:
  - $set, Sunset, $inc, $rename.
  - Permite crear, modificar o eliminar atributos específicos.

- Opciones de Modificación:
  - multi: modifica uno o varios documentos.
  - upsert: crea un nuevo documento si no hay coincidencias.


- Comandos de eliminación:
  - remove, delete Many y deleteOne.
´´´
db.usuarios.remove({});// Elimina a todos
db.usuarios.remove({ edad: { $gt: 30 } }); // Elimina los mayores a 30 


´´´
  - Elimina documentos basados en criterios de búsqueda. Argumento adicional para eliminar solo un documento.

- Interacción con la audiencia:
  - Se fomenta la comprensión de cuándo es más conveniente utilizar cada comando.
  - Se realizan ejemplos prácticos y se invita a comentarios sobre su aplicación y utilidad.


  ´´´
  Hemos visto en conceptos anteriores que podemos eliminar todos los documentos de una colección mediante el método deleteMany y pasando un objeto literal vacío:

db.libros.deleteMany({})
Aprendimos también a recuperar algunos documentos con el método find empleando una serie de operadores relacionales, dichos operadores se pueden emplear en forma idéntica con los métodos deleteMany y deleteOne.

Hay dos métodos para eliminar documentos:

deleteMany: Borra todos los documentos que cumplen la condición que le enviamos.
deleteOne: Borra el primer documento que cumple la condición que le pasamos.
Almacenaremos una serie de documentos en una colección llamada libros y luego borraremos algunos de sus documentos:

use base1
db.libros.drop()

db.libros.insertOne(
  {
    _id: 1,  
    titulo: 'El aleph',
    autor: 'Borges',
    editorial: ['Siglo XXI','Planeta'],
    precio: 20,
    cantidad: 50 
  }
)
db.libros.insertOne(
  {
    _id: 2,  
    titulo: 'Martin Fierro',
    autor: 'Jose Hernandez',
    editorial: ['Siglo XXI'],
    precio: 50,
    cantidad: 12
  }
)
db.libros.insertOne(
  {
    _id: 3,  
    titulo: 'Aprenda PHP',
    autor: 'Mario Molina',
    editorial: ['Siglo XXI','Planeta'],
    precio: 50,
    cantidad: 20
  }
)
db.libros.insertOne(
  {
    _id: 4,  
    titulo: 'Java en 10 minutos',
    editorial: ['Siglo XXI'],
    precio: 45,
    cantidad: 1 
  }
)

db.libros.find()

db.libros.deleteOne({_id: 1})

db.libros.find()

db.libros.deleteMany({precio : {$gte : 50 }})

db.libros.find()
Si queremos eliminar el documento que almacena en el campo el _id con valor 1 luego podemos utilizar la sintaxis:

db.libros.deleteOne({_id: 1})
Lo más conveniente es utilizar el método 'deleteOne' ya que solo uno puede cumplir esa condición al ser la clave primaria del documento.

Recordemos que la sintaxis alternativa para eliminar el documento con _id con valor 1 es:

db.libros.deleteOne({_id: { $eq : 1}})
La sintaxis anterior es buena recordar ya que los otros operadores relacionales hay que utilizarlos en forma obligatoria y no tienen una sintaxis alternativa como el $eq.

Para borrar todos los libros que tienen un precio mayor o igual a 50 tenemos:

db.libros.deleteMany({precio : {$gte : 50 }})

´´´

## Cuestionario 
1. ¿Qué comando de la consola de MongoDB se utiliza para indicar la base de
datos con la que se trabajará?
A. select.
B. find.
C. use.
D. Las respuestas A y C son correctas.
2. ¿Cuál de las siguientes afirmaciones es correcta?
A. MongoBooster es una herramienta GUI multiplataforma que facilita la
construcción de consultas.
B. MongoDB Compass es una herramienta no propietaria para la
manipulación externa de bases de datos MongoDB.
C. MongoBooster y MongoDB Compass proporcionan información estadística
y de rendimiento de una base de datos MongoDB.
D. Todas las afirmaciones anteriores son correctas.
3. ¿Cuál será el resultado al insertar un documento que posee un atributo más al
resto de atributos de la colección?
A. Dará un fallo al insertar los datos porque el modelo de datos es diferente.
B. Insertará los datos a la colección.
C. Insertará los datos a la colección y creará el nuevo atributo vacío en el
resto de documentos.
D. Insertará los datos a la colección, pero sin el nuevo atributo para cumplir
con el modelo.
Test
Bases de Datos para el Big Data
Tema 3. Test
52
4. ¿Qué comando puede utilizarse en MongoDB para la creación de un nuevo
documento dentro de una collection?
A. save.
B. insert.
C. create.
D. Las respuestas A y B son correctas.
5. ¿Cuál es el nombre del atributo especial en las collections de MongoDB que
ayuda a identificar de manera única a cada documento?
A. _id.
B. ID.
C. Primary key.
D. Identifier.
6. ¿Qué método permite modificar los datos de un documento sin tener que incluir
el documento completo como argumento?
A. save.
B. store.
C. update.
D. set.
7. La operación MongoDB equivalente a JOIN en SQL es:
A. Se puede conseguir concatenando sentencias find en la misma operación.
B. El aggregation framework.
C. MongoDB no tiene operación equivalente a JOIN hasta su versión 3.2.
D. Ninguna de las anteriores es cierta.
Test
Bases de Datos para el Big Data
Tema 3. Test
53
8. ¿Qué situación tiene que darse para que el comando save actualice un
documento?
A. Que el argumento contenga un identificador existente en la collection.
B. Que el segundo argumento en el comando sea el valor true.
C. Que el argumento se parezca en más de un 50 % a un documento en la
collection.
D. save no puede utilizarse para actualizar documentos.
9. ¿Qué comando se utiliza en MongoDB para eliminar un conjunto de
documentos?
A. save.
B. delete.
C. remove.
D. unset.
10. ¿Qué comando puede aplicarse sobre el resultado de una consulta en
MongoDB para restringir el número de documentos retornados?
A. limit.
B. restrict.
C. skip.
D. sort.


## Tema 4 Agregación

## Videoclase 1. Framework de Agregación

- Conceptos Basicos de agregacion de MongoDB 
  - Se usa para consultar datos agrupados y obtener un resultado 
  - Ejemplo: Suma total de ventas por años 
- MongoDB Ofrece tres metodos: 
  - Map-Reduce: Es mas potente pero complejo de usar 
    - Map: permite filtrar los datos 
    - Reduce: permite agregar reglas de operacion sobre los datos.

´´´
Map-Reduce utiliza funciones de JavaScript personalizadas para
realizar el map y el reduce de las operaciones, así como la operación de
finalización opcional. El uso de JavaScript proporciona una gran
flexibilidad en comparación con las pipelines, pero Map-Reduce es
menos eficiente y más complejo.
´´´

## Muestras: 

![ejemplo reduce](../01_BasesDatosParaDatosMasivos/info/info_003.png)

![ejemplo reduce](../01_BasesDatosParaDatosMasivos/info/info_004.png)

![ejemplo reduce](../01_BasesDatosParaDatosMasivos/info/info_005.png)


  - Aggregation Framework: Permite obtener operaciones parecidos a SQL, facil y optimizada, mejora los tiempos de consultas mas cortos, puedes usar count(), distinct() atributos unicos, podemos usar consultas avanzadas. 
  - Operaciones Simples: count, distinct, sum, average 


  NOTA: DEBES HACER LOS EJERCICIOS DEL TEMA 4 PARA PRACTICAR 

## Videoclase 2. Map-Reduce

## Conceptos: 
  - Es un paradigma que se tiene en muchas herramientas de desarrollo 
  - El objetivo es analizar grandes volumes de datos 
  - En mongoDB aun sigue existiendo pero ya esta obsoleto "predecado"
  - Estan apostando mas por el framework de agregations 
  - Es complejo ya que tienes que saber programar 
  
## Como Funciona

  - Paso 1: Pasa por la función map que permite validar cada documento y emite parea clave-valor
  - Paso 2: la funcion reduce recibe la clave y el array de los valores para realizar operaciones de agregacion 
  - paso 3: permite recibir parametros como: 
      - out: 
      - querry:
      - sort: 
      - limit:
      - finalize:
      - scope: 
      - JsMode:
      - verbose:  

## Ejemplo Código 

´´´
# JavaScript
var map = function() {
  emit(this.producto, this.cantidad * this.precio);
};

var reduce = function(key, values) {
  var total = 0;
  for (var i = 0; i < values.length; i++) {
    total += values[i];
  }
  return total;
};


db.ventas.mapReduce(
  map, 
  reduce, 
  { 
    out: "resultados_ventas" 
  }
);
´´´

## Videoclase 3. Operaciones de Agregación

## Concpetos
- Es modelado en concpetos de tuberias "pipeline" -> los documentos entran a una tuberias de varias etapas que transforman los documentos en un resultado agregado. 
- proporciona la capacidad de "sharing" -> 
- Se puede usar el indice para mejorar el rendimiento. 
- El Aggregation Framework de MongoDB funciona como tuberías de procesamiento de datos.
- Los documentos atraviesan varias etapas que transforman los datos en un resultado agregado.
- Las etapas básicas proporcionan filtros y transformaciones de documentos.
- Otras etapas permiten agrupar, clasificar y agregar contenido de arrays, entre otras operaciones.

![ejemplo agregacion](../01_BasesDatosParaDatosMasivos/info/info_006.png)
![ejemplo agregacion](../01_BasesDatosParaDatosMasivos/info/info_007.png)

## Notas 
- El Aggregation Framework permite realizar operaciones complejas como el cálculo de promedios y la concatenación de cadenas mediante operadores
- La etapa $unwind en el Aggregation Framework se utiliza para descomponer arrays en documentos individuales, permitiendo realizar operaciones sobre los elementos de un array.
- El Aggregation Framework tiene una fase de optimización interna que mejora el rendimiento, lo que lo hace más eficiente que Map-Reduce en muchas operaciones.
- El Aggregation Framework mejora el rendimiento al utilizar índices y aprovechar la capacidad de sharding de MongoDB, lo que permite distribuir el procesamiento de datos en diferentes nodos. 
- El operador $lookup se utiliza para realizar una combinación de documentos de diferentes colecciones, lo que permite trabajar con datos relacionados en el Aggregation Framework.


## 4.2. Conceptos
## 4.3. Map-Reduce
## 4.4. Aggregation Framework
## 4.5. Casos prácticos

## Cuestionario 

1. ¿Para qué son útiles las funciones de agregación?
  A. Para agrupar datos.
  B. Para realizar cálculos.
  C. Para crear nuevas colecciones.
  D. Todas las anteriores son correctas. -> Correcto 

2. ¿Qué método puede utilizarse en MongoDB para agregar información de
documentos en una collection?
  A. sum.
  B. Aggregate, a partir de la versión 2.2.
  C. Map-Reduce.
  D. Las respuestas B y C son correctas. -> Correcta 

3. ¿Cuál de las siguientes son operaciones específicas de agregación?
  A. sum.
  B. Map-Reduce.
  C. count.
  D. Las respuestas A y C son correctas. -> Correcta

4. ¿Cuál es el objetivo principal de la función map?
  A. Generar los pares clave-valor.
  B. Realizar operaciones con los atributos de la colección.
  C. Operar sobre los pares clave-valor.
  D. Crear una nueva colección. -> Duda


5. ¿Cuál es el objetivo principal de la función reduce?
  A. Generar los pares clave-valor.
  B. Realizar operaciones con los atributos de la colección.
  C. Operar sobre los pares clave-valor. -> Correcto 
  D. Crear una nueva colección.

6. ¿Qué comando se utiliza en una función map para generar el par clave-valor que
será procesado posteriormente?
  A. generate.
  B. return. -> Duda
  C. emit. -> emitir notificaciones sincronicas entre la BD y la Aplicacion 
  D. yield.

7. ¿Cuál de las siguientes es una ventaja de framework de agregación de
MongoDB?
  A. Rendimiento.
  B. Potencia.
  C. Simplicidad.
  D. Las respuestas A y C son correctas. -> Correcto

8. ¿En qué está modelado el framework de agregación?
  A. Funciones.
  B. Etapas. -> Correcto 
  C. Sentencias SQL.
  D. Agrupaciones.

9. ¿Qué campo es obligatorio especificar en framework de agregación?
  A. _id. -> Correcto 
  B. Object.
  C. $sum.
  D. $group.

10. ¿Cuál de los siguientes es un operador del framework de agregación?
  A. $gt.-> Correcta 
  B. $map.
  C. $year.
  D. Todos los anteriores son correctos.


## Tema 5. Gestión de MongoDB

## Videoclase 1. Gestión de MongoDB

## Notas:
- En entornos de producción, garantizar la seguridad de los datos es crucial, por lo que MongoDB implementa medidas para proteger la integridad y confidencialidad de la información mediante autenticación de usuarios y restricciones de acceso.

- El usuario administrador tiene privilegios esenciales para gestionar otros usuarios y acceder a todas las bases de datos en el sistema, lo que es clave para la administración segura de MongoDB.

- La creación de usuarios con los privilegios adecuados y la autenticación de estos son pasos fundamentales en la configuración de la seguridad en MongoDB.

-  La asignación correcta de roles y funciones asegura que los usuarios tengan acceso solo a las operaciones y datos que les corresponden, lo que contribuye a la seguridad e integridad de la base de datos.

- Sharding es el proceso que permite repartir la carga de la base de datos en diferentes servidores, optimizando el rendimiento y la escalabilidad del sistema MongoDB.

## Videoclase 2. 

## Notas: 


## Videoclase 3. 

## Notas: 



## 5.2. Seguridad

## 5.3. Respaldo

## 5.4. Rendimiento

## 5.5. Sharding
