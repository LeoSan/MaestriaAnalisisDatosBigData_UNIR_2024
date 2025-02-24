

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

## Videoclase 2: Respaldo de datos

## Notas: 
- Es copiar el directorio del sistema de ficheros a la nueva ubicación, puede generar problemas si no se detiene el gestor de base de datos. 
- Ser recomienda detener el servidor 
- Herramienta MongoDumb generar copias de seguridad 
- Herramienta MongoRestore se puede restaurar  datos de seguridad por defecto busca el dorectorio dumb
- MongoDumb Ejemplo -> mongodump --host mongoHost.es --port 27017 --out /data/backup/mongodump --collection miColeccion --db miBaseDeDatos
- MongoRestore Ejemplo -> mongorestore --port 27017 /db/backup/mongodump-2013-10-24 
- avanzado -> mongorestore --host mongodbl.example.net --port 3017 --username user password pass /db/backup/mongodump-2013-10-24
- 

- Si el servidor MongoDB está en ejecución durante la copia del sistema de ficheros, existe el riesgo de corrupción de datos, por lo que se recomienda detener el servidor antes de realizar la copia.

- Mongodump es la herramienta utilizada para realizar copias de seguridad de bases de datos completas, colecciones individuales o partes específicas mediante consultas.

- Mongodump es la herramienta utilizada para realizar copias de seguridad de bases de datos completas, colecciones individuales o partes específicas mediante consultas.

- Las versiones recientes de mongodump no son compatibles con versiones anteriores de datos BSON, lo que debe tenerse en cuenta al realizar copias de seguridad y restauraciones.

- Mongorestore busca de manera predeterminada las copias de seguridad en el directorio "dump/" para realizar las restauraciones.

## Videoclase 3: Uso de índices

## Notas:
- si creamos indices opotmizamos los tiempos de consilta si aplicamos indices entres las colecciones 
- Es una estretgia fundamental para mejorar el rendicmiento del sistema 
- Ejemplos de indices 
  - Indices Simples: se genera para un solo atributo ejemplo nombre ->
  - Indice Compuestos: se genera para varios atributos ejemplo nombre, edad
  - Indices de subdocumentos: para atributo dentro de un objeto,  como info.friend
  - Indices Arrays: para claves que contienen arrays como hobnies 
  - Indices 2d: usados para geolocalización se usan coordernadas como x & y 

- Sharding: es una tecnica para distribuir y dividir conjuntos de datos en varios servidores, permite aumentar el rendimiento y la capacidad. 
  - Shard (Fragmentos): Escalabilidad Horizontal, se generan nodos responsables de almacenar datos, cada shard es una replica set que ofrece disponibilidad y consistencia de datos. 
  - Query Routers: Instancias actuan como interfaz entre los clientes y los shard, dirigiendo las consultas al shard apropiado. 
  - Config Servers: es el admin permite que los routers validen sus metadatos para luego dirigirlo al shard que contoiene la informacion 

  - Los índices mejoran el tiempo de ejecución de las consultas al permitir búsquedas más rápidas sobre los atributos indexados, lo que optimiza el rendimiento de las operaciones en la base de datos.
  - Al filtrar comúnmente por el atributo "email", sería eficiente crear un índice sobre este atributo para mejorar el rendimiento de las consultas.
  - El comando createIndex es utilizado en MongoDB para crear índices, con las claves representando los atributos sobre los cuales se va a crear el índice y las opciones como parámetros adicionales.
  - Los índices 2d se utilizan para claves que contienen coordenadas geoespaciales, como "location", y permiten realizar consultas geoespaciales eficientes.
  - Los config servers almacenan metadatos sobre la información de los shards y son consultados por los query routers para determinar en qué shard se encuentran los datos específicos.


## 5.2. Seguridad

- Mongodb por defecto no inicia con autenticación sin embargo podemos crear usuarios y crear ciertos privilegios. 
- Podemos usar el comando db.createUser(<Nombre de usuario>, <Contraseña de usuario>) para crear usuarios. 
- Un usuario puede tener privilegios en diferentes bases de datos. Si necesita que un
usuario tenga privilegios en varias bases de datos, crea un solo usuario con roles
que otorguen los privilegios de base de datos aplicables en lugar de crear el usuario
varias veces en diferentes bases de datos.
- Para autenticarse desde la consola de MongoDB se utiliza el comando db.auth :
db.auth(<Nombre de usuario>, <Contraseña de usuario>)


## Ejemplo 

db.createUser({
 user:"admin",
 pwd: "mipassword“,
 roles:[
 "clusterAdmin",
 "readAnyDatabase",
 "readWriteAnyDatabase",
 "userAdminAnyDatabase",
 "dbAdminAnyDatabase“
 ]
});

## Roles
- read: proporciona la capacidad de leer datos de todas las colecciones que no son
del sistema y de las siguientes colecciones del sistema: system.indexes, system.js y
system.namespaces. 

- readWrite: proporciona todos los privilegios del rol de lectura y la capacidad de
modificar datos de todas las colecciones que no son del sistema y de la colección
system.js .

- Cada base de datos incluye los siguientes roles de administración de base de datos:

- dbadmin: proporciona la capacidad de realizar tareas administrativas, tales como
tareas relacionadas con el esquema, indexación y recopilación de estadísticas. Esta
función no otorga privilegios para la administración de usuarios y roles.

- dbOwner: proporciona la capacidad de realizar cualquier acción administrativa en la
base de datos. Este rol combina los privilegios otorgados por las funciones readWrite,
dbAdmin y userAdmin .

- userAdmin: proporciona la capacidad de crear y modificar roles y usuarios en la
base de datos actual. Dado que el rol userAdmin permite a los usuarios otorgar
cualquier privilegio a cualquier usuario, incluyendo a ellos mismos, el rol también
indirectamente proporciona acceso de superusuario a la base de datos o, si se
extiende a la base de datos de administración, al clúster.

La base de datos admin incluye las siguientes funciones para administrar todo el
sistema en lugar de una base de datos específica:

- clusterAdmin: proporciona el mayor acceso de administración de clústeres. Este rol
combina los privilegios otorgados por las funciones clusterManager, clusterMonitor y
hostManager. Además, la función proporciona la acción dropDatabase .

- clusterManager: proporciona acciones de administración y supervisión en el clúster.
Un usuario con esta función puede acceder a las bases de datos de configuración y
local, que se utilizan en sharding y replicación, respectivamente.

- clusterMonitor: proporciona acceso de solo lectura a las herramientas de
supervisión, como MongoDB Cloud Manager y el agente de supervisión Ops
Manager.

- hostManager: proporciona la capacidad de supervisar y administrar servidores.


La base de datos admin incluye las siguientes funciones para realizar copias de
seguridad y restaurar datos:

- backup: proporciona los privilegios necesarios para realizar copias de seguridad de
los datos. Esta función proporciona suficientes privilegios para utilizar el agente de
copia de seguridad de MongoDB Cloud Manager, el agente de copia de seguridad
de Ops Manager o para utilizar mongodump .

- restore: proporciona los privilegios necesarios para restaurar los datos con
mongorestore sin la opción --oplogReplay o sin los datos de la colección system.profile

Estas funciones en la base de datos de administración se aplican a todas las bases
de datos local y config excepto en una instancia mongod:

- readAnyDatabase: proporciona los mismos permisos de solo lectura, excepto los
que se aplican sobre todas las bases de datos, las locales y el config del clúster. El
rol también proporciona la acción listDatabases en el clúster como un todo.

- readWriteAnyDatabase: proporciona los mismos permisos de lectura y escritura
que readWrite , excepto que se aplica a todas las bases de datos local y config del
clúster. El rol también proporciona la acción listDatabases en el clúster como un todo.

- userAdminAnyDatabase: proporciona el mismo acceso a las operaciones de
administración de usuarios como userAdmin, excepto que se aplica a todas las
bases de datos local y config del clúster. 

- dbAdminAnyDatabase: proporciona el mismo acceso a las operaciones de
administración de bases de datos que dbAdmin , excepto que se aplica a todas las
bases de datos locales y de configuración del clúster. El rol también proporciona la
acción listDatabases en el clúster como un todo.

## 5.3. Respaldo

Existen muchas formas de generar respaldo la mas rudimentaria es copiar el directorio del sistema de ficheros a la nueva
ubicación. Por defecto, los datos de MongoDB se almacenan en la ruta /data/db en
Linux, o C:\data\db en Windows (ruta recomendada). Es importante tener en cuenta
que los datos no se copiarán adecuadamente si el servidor de MongoDB se
está ejecutando en el momento de realizar la copia

Además, MongoDB permite exportar e importar bases de datos mediante dos
herramientas a utilizar desde la línea de comandos: mongodump y mongorestore ,
respectivamente

## ¿Qué es mongodump?

Es una herramienta de línea de comandos que forma parte de la suite de herramientas de MongoDB. Su función principal es realizar copias de seguridad (dumps) de bases de datos o colecciones individuales en formato BSON. Este formato es binario y optimizado para MongoDB, lo que lo hace eficiente para realizar restauraciones posteriores.

## Opciones adicionales:

- gzip: Comprime la copia de seguridad en formato gzip para ahorrar espacio.
- archive: Crea un archivo único que contiene todas las colecciones de la base de datos.
- authenticationDatabase: Especifica la base de datos de autenticación si tu sistema requiere autenticación.
- username y --password: Proporciona las credenciales de autenticación.

## Ejemplo Código básico 

- mongodump -d miBaseDatos -c usuarios -o /var/backups/usuarios.bson

## Ejemplo avanzado 

- mongodump -d miBaseDatos -o backup --gzip --authenticationDatabase admin --username miUsuario --password miContraseña

Nota: las utilidades mongodump y mongorestore funcionan con volcados de datos
BSON y son útiles para crear copias de seguridad de pequeñas implementaciones.


## ¿Qué es mongorestore?

Es una herramienta de línea de comandos de MongoDB que se utiliza para restaurar una base de datos completa o una colección específica a partir de un volcado binario creado previamente con mongodump.

## Opciones adicionales:

mongorestore ofrece muchas opciones adicionales para personalizar la restauración. Algunas de las más comunes incluyen:

- uri: Especifica la cadena de conexión a un clúster MongoDB.
- host: Especifica el host del servidor MongoDB.
- port: Especifica el puerto del servidor MongoDB.
- archive: Indica que la entrada es un archivo de respaldo comprimido.
- drop: Elimina la base de datos de destino antes de restaurar.
- gzip: Descomprime el archivo de respaldo gzip.
- verbose: Muestra información detallada sobre el proceso de restauración.

## Ejemplo Código básico 

- mongorestore --uri mongodb://user:password@host:port/database --archive --gzip /backup/mydatabase.gz

## Ejemplo avanzado 

- mongodump -d miBaseDatos -o backup --gzip --authenticationDatabase admin --username miUsuario --password miContraseña

La replicación es una característica de MongoDB que permite la redundancia de
datos, así como incrementar su disponibilidad. La arquitectura básica de replicación
en MongoDB sigue un modelo Maestro-Esclavo. La instancia maestra recibe
operaciones de escritura y estas son aplicadas en la instancia dependiente para
mantener la consistencia de los repositorios de datos.

## 5.4. Rendimiento

El incremento de rendimiento en el sistema MongoDB puede realizarse a través de
acciones como la creación de índices, los cuales mejoran el tiempo de ejecución de
consultas sobre collections. 

Es recomendable analizar los atributos de un documento sobre los cuales será
beneficioso aplicar un índice. Por ejemplo, si es común filtrar documentos en la
collection usuarios por el atributo email , será conveniente crear un índice sobre dicho
atributo.

- El comando brindado para crear un índice es createIndex y posee el siguiente
formato:
db.<nombre de collection>.createIndex(<claves>, <opciones>)

Ambos argumentos en la llamada a la función son objetos en formato JSON. El
objeto claves indica los atributos sobre los cuales se creará el índice, teniendo como
valor el número 1 si el índice se creará de forma ascendente y -1 si es de forma
descendente.

El objeto opciones puede contener los siguientes atributos, todos opcionales:

- background: valor booleano para indicar si el índice debe crearse sin bloquear otras
actividades en la base de datos. Por defecto es false .
- unique: valor booleano para indicar si un atributo no acepta valores repetidos. Por
defecto es false .
- name: cadena de texto para especificar el nombre del índice
- dropDups: valor booleano que indica la creación de un índice único y la eliminación
de documentos repetidos en la collection. Por defecto es false .
- sparse: valor booleano para indicar que el índice se aplica solamente sobre los
documentos con los atributos indicados en el campo de claves.
- v: indica el número de versión del índice a crear. Antes de la versión 2.0 de
MongoDB este valor es 0, para versiones posteriores el valor es 1.

Un índice puede eliminarse utilizando el comando dropIndex , siguiendo la sintaxis
apropiada:
db.<nombre de collection>.dropIndex(<índice>)


## Algunos ejemplos de indexación pueden ser los siguientes:

- Simple: insertamos un índice en orden ascendente para el atributo name . El
comando para insertar el índice y la búsqueda que lo aplica son los siguientes:

db.users.createIndex( { "name" : 1} )
db.usesr.find({ name: “Fernando Alonso” })

- Compuesto: se pueden usar para consultar uno o varios campos sin incluir todos. El
siguiente ejemplo permitirá optimizar la búsqueda para name , o para name y age .
Si se quiere hacer solo sobre age , habría que crear un índice simple para este
atributo. En el siguiente ejemplo se crea un índice para name y age y se crea la
consulta que se aprovecha de esta optimización:

db.users.createIndex( { "name" : 1, "age":-1 } )
db.usesr.find( {name: “Fernando Alonso”, age:36 })

- Subdocumento: si el atributo pertenece a un objeto, es necesario llegar al nivel
deseado para asegurar el índice. El insertado del índice y la consulta que utiliza la
optimización son las siguientes:

db.users.createIndex( { "info.friend" : 1 } )
db.user.find({ info.friend: “Pedro”})

- Arrays: se pueden crear índices sobre claves que contienen arrays; para ello se
crea un valor en el índice para cada valor del array. Se denominan índices multikey y
no hace falta intimidarlo explícitamente. El insertado del índice y la consulta que
utiliza la optimización son las siguientes:

db.users.createIndex( { "hobbies": 1} )
db.users.find({ hobbies: “motor” })

- 2d: los documentos deben tener una clave que contenga un array de dos
coordenadas. Estos índices son útiles cuando permiten utilizar operadores
especiales como $near . El insertado del índice y la consulta que utiliza la
optimización son las siguientes:

db.users.createIndex( { "location": 2d} )
db.users.find({ location: {$near: [25,32] } }).limit(6)

Nota: a partir de la versión 3.0 de MongoDB, createIndex fue el método que
reemplazó a ensureIndex.

## 5.5. Sharding

Otro mecanismo para incrementar el rendimiento de una base de datos es escalar,
ya sea de forma vertical u horizontal. La escalabilidad vertical consiste en
incrementar o mejorar hardware (CPU y memoria RAM) que utiliza el sistema.

En contraste, la escalabilidad horizontal o sharding consiste en dividir el conjunto de
datos y distribuirlo en varios servidores o shards. Así, el número de operaciones y la
cantidad de datos se reparte entre el conjunto de shards. Si la base de datos crece,
es suficiente con añadir un nuevo shard para poder almacenar más datos en un
nuevo nodo.

Su principal utilidad es aumentar el rendimiento de las consultas distribuyendo la
información entre varias máquinas y permitir añadir nuevas máquinas para poder
aumentar la capacidad de almacenaje de información.

MongoDB brinda sharding a través de la definición de sharded clusters, los cuales
están compuestos por tres tipos de componentes:

- Shards: están a cargo de almacenar la información. Cada shard es un replica set,
por lo que brinda alta disponibilidad y consistencia de datos.

- Query Routers: son instancias del servicio mongo y sirven de interfaz entre los
clientes y los shards.

- Config Servers: almacenan metadatos sobre la información almacenada en cada
shard. Son consultados y modificados por los query routers para saber qué shards
contienen información en específico. Los sharded clusters en un entorno de
producción tienen exactamente tres config servers.


## Cuestionarios 

1. ¿Qué comando de MongoDB permite crear una copia de respaldo de una base
de datos?
A. mongorestore.
B. mongodump. -> Correcto
C. backup.
D. mongod.

2. ¿Qué comando de MongoDB permite recuperar una base de datos a partir de
una copia de seguridad?
A. mongorestore. -> Correcto
B. save.
C. mongos.
D. copydb.

3. ¿Qué elementos de la base de datos mejoran el rendimiento de consultas a
collections?
A. Índices. -> Correcto
B. Replica sets.
C. Query routers.
D. Las respuestas B y C son correctas.

4. ¿Qué característica de MongoDB permite tener redundancia y aumentar la
disponibilidad de los datos?
A. Seguridad.
B. Sharding. -> Correcto 
C. Índices.
D. Replicación.

5. ¿Cuál es el modelo básico de replicación en MongoDB?
A. Sharding.
B. Replica set. -> Correcto
C. Maestro-Esclavo.
D. Shards.


6. ¿Cómo se llama al refinamiento del modelo Maestro-Esclavo implementado en
MongoDB?
A. Result set.
B. Replica set. -> Correcto
C. Sharding.
D. Replicación.

Un Replica Set en MongoDB es el mecanismo fundamental para lograr alta disponibilidad y tolerancia a fallos. Consiste en un conjunto de servidores, donde uno actúa como primario y los demás como secundarios.


7. ¿Cómo se denomina el nodo de un replica set que no almacena datos y
solamente puede votar en las elecciones de nodo primario?
A. Secundario.
B. Árbitro. -> Correcto
C. Shard.
D. Config server.

Un nodo árbitro en un replica set de MongoDB es aquel que no almacena datos y solo participa en las elecciones de nodo primario.

8. ¿Qué otro nombre recibe el método de escalabilidad horizontal, en el que los
datos son separados y distribuidos entre varios servidores?
A. Escalabilidad vertical.
B. Elastic computing.
C. Sharding. -> Correcto 
D. Replicación.

Sharding es un término específico que se refiere a la técnica de dividir una base de datos en múltiples bases de datos más pequeñas, distribuidas en diferentes servidores. Cada una de estas bases de datos más pequeñas se llama shard.

9. ¿Qué nombre reciben los nodos que almacenan datos en un sharded cluster?
A. Data stores.
B. Config servers.
C. Query routers.
D. Shards. -> Correcto 

Shards: En un clúster sharded, los datos se dividen en fragmentos más pequeños llamados shards. Cada shard es almacenado en un nodo específico del clúster. Esta distribución permite escalar el sistema horizontalmente al agregar más nodos y shards a medida que crece la cantidad de datos.


10. ¿Cuántos config servers debe haber en un entorno de producción?
A. Uno.
B. Tres.
C. Un máximo de cinco.
D. Depende del número de servidores disponibles. -> correcto 


## Tema 6. Drivers de conexión

## Videoclase 1. Drivers de Conexión

## Notas:
- Actua como intermediario entre el código y la base de datos. 
- Nos facilita la visualizacion de datos y gestión de big data. 
- Lenguajes Oficiales: c, C++, C#, Java, Node.js, perl, php 
- Lenguajes Soportado Comunidad: Action Script3, C, C#, .NET,   ColdFusion, D, Dart, 
- Los drivers son el vínculo entre la base de datos y el código de la aplicación, permitiendo que los desarrolladores accedan a los datos desde varios lenguajes de programación.
- Para aplicaciones Java que utilizan MongoDB, se recomienda utilizar maven para la gestión de dependencias.
- En la presentación se mencionan lenguajes como Python, Swift y R, pero no se menciona COBOL entre los lenguajes soportados por los drivers de MongoDB.
- La página oficial de MongoDB para consultar la documentación, cursos y ejemplos sobre los drivers es www.mongodb.com/docs/drivers/.
- Para conectar a un host específico de MongoDB en Java, se utiliza el URI de conexión, que permite especificar detalles del servidor y la base de datos.

## Videoclase 2. MongoDB y otros lenguajes

## Notas:
- Solo exlicarón como acceder usando java bueno comandos cortos. 
- MongoDB utiliza BSON, una versión binaria de JSON, para almacenar documentos debido a su mayor eficiencia y compatibilidad con tipos de datos adicionales.
- El primer paso para acceder a una base de datos de MongoDB es conectarse al servidor MongoDB antes de interactuar con la base de datos o sus colecciones
- El comando find() se utiliza para realizar búsquedas de documentos dentro de una colección en MongoDB, permitiendo filtrar los resultados según los criterios especificados.
- La búsqueda de documentos en MongoDB se realiza a través del método find(), que permite obtener los documentos que coinciden con los criterios de búsqueda.
- Los datos en MongoDB se almacenan y manipulan en formato BSON dentro de las colecciones, que representan estructuras similares a documentos JSON, pero optimizadas para el rendimiento.


## Videoclase 3. NodeJS y Python

## Notas:
- Hay que tener bien instaldo mongodb
- ![ejemplo insalacion](../01_BasesDatosParaDatosMasivos/info/info_008.png)
- ![ejemplo insalacion](../01_BasesDatosParaDatosMasivos/info/info_009.png)
- Mongoose es una librería popular en Node.js para interactuar con MongoDB, proporcionando una capa de modelado de datos sobre MongoDB.
- PyMongo es la biblioteca oficial de MongoDB para Python, utilizada para la conexión y manipulación de datos en MongoDB desde aplicaciones Python.
- El método insertOne() es utilizado en Node.js para insertar un único documento en una colección de MongoDB.
- En Python, la conexión a una base de datos MongoDB se realiza utilizando el método connect() proporcionado por la biblioteca PyMongo.
- El ejemplo presentado en la videoclase es la inserción de un documento, lo que es fundamental para entender cómo interactuar con MongoDB en aplicaciones Node.js y Python.


## 6.2. Referencias: dónde consultar cada driver

> MongoDB proporciona una descripción completa de cómo funciona cada uno de los drivers, que tienes disponible en el siguiente enlace. En esta página se pueden encontrar cursos, tutoriales y ejemplos para facilitar la construcción de aplicaciones que precisen de MongoDB para su funcionamiento.

## A continuación, se enumera una lista de los drivers que hay disponibles:
- C
- C++
- C#
- Java
- Node.js
- Perl
- PHP
- Python
- Motor
- Ruby
- Scalar
- Go
- Erlang

[Drivers Documentación](https://www.mongodb.com/docs/drivers/)

También MongoDB proporciona un conector para Hadoop. Este conector es un
plugin que permite utilizar MongoDB como fuente de entrada y/o salida destino.

Hadoop: Una plataforma para procesar grandes volúmenes de datos

Hadoop es una plataforma de código abierto diseñada para almacenar y procesar grandes conjuntos de datos de forma distribuida y eficiente. Imagina que tienes una cantidad masiva de información, como los registros de todas las búsquedas en un motor de búsqueda o los datos de sensores de una ciudad inteligente. Hadoop te permite:

Almacenar: Guardar estos datos en un sistema de archivos distribuido (HDFS) que puede manejar grandes cantidades de información en múltiples servidores.
Procesar: Analizar y transformar estos datos utilizando un modelo de programación llamado MapReduce. MapReduce divide el trabajo en pequeñas tareas que se ejecutan en paralelo en múltiples máquinas, lo que permite procesar datos muy grandes de manera rápida

## 6.3. Ejemplos de uso

## Cuestionario

1. ¿Cuál es el objetivo de un driver?
A. «Traducir» las llamadas que se hacen desde un lenguaje de programación
a un «lenguaje» que entienda la base de datos.
B. Proporcionar un objeto de conexión.
C. Proporcionar una serie de «funciones» que permitan al programador
interactuar con la base de datos.
D. Todas las anteriores son correctas. -> Correcto 

2. ¿Dónde se debería acudir si se quiere desarrollar una aplicación con base de
datos MongoDB pare gestionar una conexión?
A. A la página oficial del lenguaje de programación con el que estamos
desarrollando.
B. A la página de documentación oficial de MongoDB, en el apartado de
drivers. -> Correcto 
C. A la página oficial del sistema operativo donde estemos desarrollando.
D. Todas las anteriores son correctas.

3. ¿Cuál de los siguientes lenguajes de programación soporta MongoDB?
A. C.
B. Java.
C. PHP.
D. Todos los anteriores son correctos. -> correcto 

4. ¿Cuál es la mejor forma de descargar el driver de Java?
A. Utilizando Maven. -> Correcto 
B. Buscando en Google.
C. Repositorio.
D. Las respuestas A y C son correctas.


5. Si no se especifica en el driver ningún parámetro, ¿dónde se realiza la conexión?
A. localhost y puerto 27017. -> Correcto 
B. Puerto 27017.
C. Localhost.
D. Es obligatorio definir un servidor y un puerto.

6. ¿Cuál es el formato de documentos utilizado por el driver de Java?
A. BSON.
B. JSON.
C. CSV.
D. XML. -> Correcto 

7. ¿Cuál es la mejor forma de instalar el driver de Node.js?
A. Usando Maven.
B. Buscando en Google.
C. Usando NPM.      -> Correcto 
D. Todas las anteriores son correctas.

8. ¿Qué es PyMongo?
A. Una base de datos NoSQL.
B. El driver de MongoDB para Python. -> Correcto 
C. Una base de datos SQL.
D. El driver de lenguaje de programación Py.

9. ¿Cómo podemos descargar el driver de Python para Mongo?
A. Utilizando NPM.
B. Utilizando Maven.
C. Buscando en Google.
D. Utilizando PIP. -> Corrceto 


10. ¿Cuál de estos comandos son válidos para acceder a una colección de mongo?
A. db.myCollection
B. db['myCollection']
C. db.getCollection('myCollection')
D. Todas son correctas -> Correcto 


## Tema 7: Cassandra

## 7.2. Descarga e instalación

- Paso 1: brew install cassandra 
- Paso 2: brew services start cassandra
- Paso 3: sudo cqlsh 
- Paso 4: descargue TablePlus como medio visual  


**Usando Docker**
- Paso 1: docker pull cassandra:latest
- Paso 2: docker network create cassandra
- Paso 3: docker run --rm -d --name cassandra --hostname cassandra --network cassandra cassandra
- Paso 000 : docker kill cassandra docker network rm cassandra

- Fuente : https://cassandra.apache.org/_/quickstart.html


## 7.3. Conceptos generales
- En el año 2008 Cassandra fue desarrollada en Facebook
-  Surgió como una mezcla del almacén de datos BigTable
- Con esta base de datos se quería resolver el problema de búsqueda en la bandeja
de entrada de Facebook.
- Cassandra es una base de datos de tipo clave-valor
- Los datos se almacenan como tablas y columnas
- Cada tabla tiene una clave principal.
- Aunque permite lecturas y escrituras muy rápidas, tiene una interfaz SQL limitada
debido a su propia estructura.


## Arquitectura

- Cassandra se diseñó para trabajar en entornos big data sobre múltiples nodos.
- cuenta con un sistema distribuido de igual a igual en todos sus nodos, donde los datos se distribuyen entre todo el clúster. 
- Arquitectura Apache Cassandra. 

## Los principales componentes de Cassandra son:
- Nodo: un lugar donde se almacenan los datos.
- Centro de datos: es una colección de nodos relacionados.
- Clúster: es un componente que contiene uno o más centros de datos.
- Registro de confirmación: mecanismo de recuperación de fallos. Todas las operaciones de escritura se escriben en este registro de confirmación.
- Mem-table: es una estructura de datos residente en memoria. Después del registro
de confirmación, los datos pasan a la tabla en memoria. Es normal que para una
familia de una sola columna existan varias mem-tables.
- SSTable: archivo de disco al que se vacían los datos de la tabla de memoria,
cuando su contenido alcanza un valor umbral.
- Filtro Bloom: conjunto de algoritmos no deterministas muy rápidos, utilizados para
probar si un elemento es miembro de un conjunto. Comprende el uso de tipo
especial de caché al que se accede después de cada consulta.


**Sistema de replicación**
- Los nodos de un clúster en Cassandra actúan como réplicas de un dato específico.
- Si la respuesta a algún nodo incluye un valor desactualizado, Cassandra se
encargará de devolver al usuario el valor más reciente. 
- Después de atender al usuario, Cassandra repara la lectura en segundo plano para actualizar los valores que se encontraron obsoletos.

**Operaciones de escritura**
- Los registros de confirmación que residen en los nodos capturan toda actividad de
escritura de los mismos nodos. 
- El objetivo es que dichos datos sean almacenados en la tabla de memorias siempre que esta esté libre. 
- En el caso de que la tabla de memorias esté llena, los datos se escribirán en el archivo de datos SStable.

**Operaciones de lectura**
- Para leer los datos, Cassandra consulta los valores de la tabla de memorias y
establece la forma de ubicar la tabla SST que contenga los datos solicitados
- El primer paso es enviar una solicitud directa a una de las réplicas. 
- Luego, el coordinador envía la solicitud de resumen a la cantidad de réplicas especificadas para garantizar el nivel de coherencia y, finalmente, comprueba que los datos
devueltos están actualizados.

**Lenguaje de consulta en Cassandra**
- Es necesario conocer también Cassandra Query Language (CQL), el lenguaje de
consulta utilizado para acceder a Cassandra a través de sus nodos. 
- La principal característica del lenguaje es que CQL utiliza la base de datos como un contenedor de tablas, las cuales representan espacio de claves. 
- Los programadores pueden utilizar cqlsh en modo consola para trabajar con CQL o emplear controladores de otras aplicaciones independientes.

## Resumen 

**¿Qué se puede destacar de Cassandra?**
- Es una base de datos orientada a columnas.
- Es escalable, consistente y tolerante a fallas.
- El diseño de distribución de Cassandra se basa en Dynamo de Amazon y su modelo de datos en Bigtable de Google.
- Se puede decir que Facebook es el creador de Cassandra.
- Como motor de base de datos, es totalmente diferente de los sistemas de
administración de bases de datos relacionales.
- El modelo de replicación es del estilo de Dynamo y el concepto de modelo de datos «familia de columnas» es el más robusto.

**¿Se usa?** 
- Sí. Algunas de las empresas más grandes como Facebook, Twitter, Cisco, Rackspace, eBay, Twitter y Netflix, entre otros, lo emplean dentro de sus arquitecturas.

**Los objetivos que se abordan en este tema son los siguientes:**
- Entender los conceptos generales que caracterizan a Cassandra.
- Conocer la arquitectura básica de esta base de datos NoSQL y los elementos que la componen.
- Aprender a usar los principales tipos de datos, incluidos los tipos de datos definidos por el usuario.
- Entender el uso de las colecciones set, list y map.
- Poner en práctica la instalación de esta base de datos en un entorno de pruebas

## 7.4. Modelo de datos y relaciones

> Cassandra divide los datos en los nodos de almacenamiento, utilizando una variante de hash consistente para la distribución de datos.

-  El hash es una técnica que se utiliza para mapear datos con la que, dada una clave, una función hash genera un valor hash (o simplemente un hash) que se almacena en una tabla hash. 
- Una clave de partición se genera a partir del primer campo de una clave primaria
- Los datos divididos en tablas hash mediante claves de partición proporcionan una
búsqueda rápida.

**Espacios de claves** 
- El modelo de datos de Cassandra consta de espacios de claves al más alto nivel.
- Los espacios de claves son los contenedores de datos, similares al esquema o la base de datos en una base de datos relacional. Normalmente, los espacios de claves
contienen muchas tablas.

**Tablas**
- Dentro de los espacios de claves, se definen o crean las tablas. 
- Estas también se conocen como «familias de columnas» en las versiones anteriores de Cassandra.
- Las tablas contienen un conjunto de columnas y una clave principal, y almacenan los datos en un conjunto de filas.

**Columnas**
- Las columnas definen la estructura de los datos en una tabla. 
- Cada columna tiene un tipo asociado, como entero, texto, doble y booleano
- En la primera columna de la tabla anterior, la clave de partición se genera a partir de la clave principal id para la distribución de datos entre los nodos de un clúster. 
- En la segunda columna de la tabla, se asigna una clave primaria compuesta, el primer campo id se usa para generar la clave de partición y el segundo campo name es la clave de agrupamiento usada para ordenar dentro de una partición.

**Relaciones**
- Cuando se quiere crear una aplicación basada en datos que utilizarán una base de datos relacional, es posible comenzar a modelar el dominio como un conjunto de tablas normalizadas correctamente y utilizar claves externas para hacer referencia a datos relacionados en otras tablas. 


## 7.5. CQL3

## Tipos de datos

- Contadores: Son tipos de columnas que funcionan como contadores, cuyas únicas operaciones
permitidas son incrementar y decrementar. El valor de la columna no se establece,
- Timestamp: Son valores codificados como enteros de 64 bits con signo. Se ingresan usando el tipo integer o string para representar, por ejemplo, una fecha ISO 8601. Estos son ejemplos de valores válidos como timestamp:
- Date: Al igual que los timestamp, se puede representar como integer o string. En el caso
de string se debe utilizar el formato convencional yyyy-mm-dd. 
- Duraciones: Los valores del duration se codifican como números enteros con 3 signos de
longitudes variables. El primer número entero representa el número de meses, el
segundo el número, de días y el tercero, el número de nanosegundos. La forma de
establecer su valor es (quantity unit)+, de la forma 12h30m. 
- Colecciones: Los tres tipos de colecciones que admite CQL son map, set y list 
  - Map: INSERT INTO clients (id, name, type) VALUES ('client001', 'Andres Luna', {
'bill' : 'ordinary', 'payment' : 'cash' });
  - Set: INSERT INTO clients (id, name, type) VALUES ('client002', 'Manuel Faena',
{'A', 'B', 'C'});
  - List:  INSERT INTO products (id, name, order, pos) VALUES ('Table01', 'Table
Reduce', 3, [10, 11, 12]);
  - Tuple :INSERT INTO users (user, phones) VALUES ('Pepe Navarro', ('home', '(34)
666-666-666'));
- Tipos definidos por el usuario (UDT): Los usuarios pueden crear sus propios tipos de datos. Para ello se emplea la instrucción CREATE TYPE.
- Keyspace Es un objeto que contiene las familias de columnas, los índices, los UDT, el conocimiento del centro de datos, la estrategia utilizada en el espacio de claves, el
factor de replicación, etc. En Cassandra, se puede considerar el keyspace como algo
similar a la base de datos en un RDBMS

## Tipo de estrategia: 
- Estrategia simple (SimpleStrategy): se utiliza cuando solo tiene un centro de
datos. En esta estrategia, la primera réplica se coloca en el nodo seleccionado por el
particionador. Los nodos restantes se colocan en el sentido de las agujas del reloj en
el anillo sin tener en cuenta la ubicación del rack o del nodo

- Estrategia de topología de red (NetworktopologyStrategy): se utiliza cuando
tiene más de un centro de datos. En esta estrategia, se debe proporcionar un factor
de replicación para cada centro de datos por separado.

- Factor de replicación (ReplicationFactor): es el número de réplicas de datos
colocadas en diferentes nodos. Para que no haya fallas, 3 es un buen factor de
replicación. Más de dos factores de replicación garantizan que no haya un solo
punto de falla.


## Ten en cuenta los siguientes aspectos sobre el keyspace:
- Nombre del keyspace: no se puede modificar en Cassandra.
- Nombre de la estrategia: se puede modificar especificando un nuevo nombre de
estrategia.
- Factor de replicación: se puede modificar especificando un nuevo factor de
replicación.
- DURABLE_WRITES : el valor DURABLE_WRITES se puede modificar especificando su
valor verdadero o falso. Por defecto, es true . Si se establece en false , no se
escribirán actualizaciones en el registro de confirmación y viceversa

## INSERT: insertando datos

INSERT INTO Products.users (user, phones) VALUES ('Pepe Navarro', ('home',
'(34) 666-666-666'));

Ten en cuenta que Cassandra insertará una fila si no existe la clave
principal indicada; de lo contrario, si la clave principal existe, actualizará
esa fila.

## UPDATE: actualizando datos

El comando UPDATE se emplea para actualizar los datos en la tabla Cassandra. Si
no se devuelven resultados después de actualizar los datos, significa que los datos
se actualizaron correctamente; de lo contrario, se devolverá un error

UPDATE Products.users Set phone = '(34) 666-666-666' WHERE user = 'Pepe
Lopez';

## DELETE: borrando datos

El comando DELETE elimina una fila completa o algunas columnas de la tabla
indicada. Cuando se eliminan datos, no se eliminan de la tabla inmediatamente. En
su lugar, los datos eliminados se marcan con una lápida y se eliminan después de la
compactación. 

DELETE from Products.users WHERE user = 'Pepe Lopez';

## Limitaciones en CQL
▸ No admite consultas de agregación como max, min, avg
▸ No admite ni group by ni having.
▸ No admite joins.
▸ No admite consultas OR.
▸ No admite consultas con comodines.
▸ No admite consultas de unión e intersección.
▸ Las columnas de la tabla no se pueden filtrar sin crear el índice.
▸ La consulta mayor que (>) y menor que (<) solo se admite en la columna de
agrupación.
▸ CQL no es adecuado para realizar análisis porque presenta muchas limitaciones.

## 7.6. TTL y WriteTime
> Cassandra puede hacer que los datos expiren de forma automática. Durante lainserción de datos, por ejemplo, se debe especificar el valor TTL en segundos. Dicho valor TTL es el tiempo de vida de los datos. Después que pase ese período en concreto, los datos se eliminarán automáticamente.

## TTL: 
- Supón que quieres insertar un registro y que este exista solo durante los primeros
200 segundos. Al insertar, si indicas el TTL 200 , los registros se eliminarán
automáticamente después de los 200 segundos.
INSERT INTO keyspaceName.TableName (ColumnNames) values (ColumnValues)
using TTL TimeInSeconds;
## Ejemplo
INSERT INTO Products.users (user, phones) VALUES ('Pepe Navarro', ('home',
'(34) 666-666')) using TTL 100;



## WriteTime: 
- es muy útil en CQL para recuperar la fecha y
hora de los insert en las columnas. Es posible usar la función WRITETIME junto con la
instrucción select seguida de la columna sin particiones entre paréntesis.
## Ejemplo
CREATE TABLE ftest (
Id int,
Name text,
Address text,
PRIMARY KEY(Id)
);
INSERT INTO ftest (Id, Name, Address) VALUES (201, 'Ashish', 'Delhi');
INSERT INTO ftest (Id, Name, Address) VALUES (202, 'Rana', 'Mumbai');
INSERT INTO ftest (Id, Name, Address) VALUES (203, 'Abi', 'Noida');
SELECT * FROM ftest;
SELECT WRITETIME (Address) FROM ftest;


## 7.7. Índices
## 7.8. Ejercicio práctico: instalación con Docker

## Ejemplo Cassandra 

-- Create a keyspace -> Crear Base de Datos
CREATE KEYSPACE IF NOT EXISTS store WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '1' };

-- Create a table
CREATE TABLE IF NOT EXISTS store.shopping_cart (
userid text PRIMARY KEY,
item_count int,
last_update_timestamp timestamp
);

-- Insert some data
INSERT INTO store.shopping_cart
(userid, item_count, last_update_timestamp)
VALUES ('9876', 2, toTimeStamp(now()));
INSERT INTO store.shopping_cart
(userid, item_count, last_update_timestamp)
VALUES ('1234', 5, toTimeStamp(now()));


## Instalar Cassandra en Windows 

- https://phoenixnap.com/kb/install-cassandra-on-windows


## Videoclase 1. Cassandra
## Notas:

- ¿Cuál fue el objetivo inicial de Cassandra cuando se desarrolló en Facebook?
  - Resolver problemas de búsqueda en la bandeja de entrada.
- ¿Cuál de las siguientes es una característica clave de Cassandra?
  - Almacenamiento de datos en tablas y columnas.
- ¿Qué componente en la arquitectura de Cassandra actúa como archivo de disco cuando la Mem-table se llena?
  - SSTable.
- ¿Qué característica distingue la arquitectura distribuida de Cassandra?
  - Sistema distribuido de igual a igual sin puntos de fallo únicos.
- ¿Qué algoritmo utiliza Cassandra para verificar la pertenencia de elementos en un conjunto?
  - Filtro Bloom -> Cassandra utiliza el Filtro Bloom para verificar eficientemente la pertenencia de elementos en un conjunto, ayudando a reducir la carga en las consultas de datos.


## Videoclase 2. Componentes de Cassandra
## Notas:
- ¿Cuál es la función principal del sistema de replicación en Cassandra?
  - Actualizar automáticamente valores desactualizados. -> El sistema de replicación de Cassandra garantiza que los valores desactualizados se actualicen automáticamente y que los datos se mantengan consistentes en todos los nodos del clúster.
- ¿Cómo distribuye Cassandra los datos entre los nodos del clúster?
  - Mediante hash consistente basado en la clave de partición.
- ¿Qué mejora el rendimiento de lectura en Cassandra según su enfoque de modelado?
  - Desnormalización de datos duplicados en varias tablas.
- ¿Qué similitud existe entre los espacios de claves en Cassandra y los esquemas en bases de datos relacionales?
  - Ambos actúan como contenedores de datos.
- ¿Cuál es el lenguaje de consultas utilizado en Cassandra para manipular datos?
  - CQL3.

## Videoclase 3. Operaciones básicas con CQL
## Notas:
- ¿Qué operación se utiliza en Cassandra para insertar datos en una tabla?
  - INSERT.
- ¿Cómo se eliminan datos de una tabla en Cassandra?
  - DELETE
- ¿Qué permite hacer la función TTL en Cassandra?
  - Establecer un tiempo de vida para los datos, después del cual expiran.
- ¿Qué limita el uso de índices secundarios en Cassandra?
  - No se pueden crear índices sobre claves principales ni colecciones 
- ¿Qué permite la función WriteTime en Cassandra?
  - Recuperar la fecha y hora exacta en que los datos fueron escritos.

## Cuestionario 

1. Cassandra:
A. Es un sistema de almacenamiento de datos NoSQL desarrollado por Facebook.
B. Es un sistema de almacenamiento en tiempo real para aplicaciones en línea.
C. Está diseñado para manejar cargas de trabajo en múltiples nodos.
D. Todas las afirmaciones anteriores son correctas. -> Correcta 

2. ¿Cuáles son los componentes principales de Cassandra?
A. Cluster, keyspace, column y column & family.
B. Columna name, tables y keyspace.
C. Mem-Table, SSTable y Bloom Filter.
D. Las respuestas A y C son correctas. -> Correcta

3. ¿Cuáles son las colecciones en CQL Cassandra?
A. Tupple, list y timestamp.
B. Map, list y set.   -> Correcta 
C. Counter, duration y date.
D. Ninguna respuesta anterior es correcta.

4. ¿Cuál es la principal característica de la colección list?
A. Almacenar datos de forma aleatoria.
B. Almacenar datos de forma ordenada y que se puedan repetir. -> Correcto 
C. Almacenar elementos clave-valor.
D. Almacenar elementos para usarlos en un orden concreto

5. ¿Qué pasa con los datos eliminados en Cassandra?
A. Se borran inmediatamente de la base de datos.
B. Se almacenan temporalmente en la papelera de reciclaje de Cassandra.
C. Son marcados con una lápida. -> Correcto 
D. Nunca se borran, están inactivos hasta que el usuario los vuelva a activar.

6. ¿Cuál de las siguientes afirmaciones es verdadera?
A. Cassandra escribe los datos en una caché clave-valor llamada Mem-Table.
B. Los datos en Mem-Table se ordenan por clave.
C. Existe una Mem-Table por cada ColumnFamily y de ella se recuperan los catos por la columna clave.
D. Todas las afirmaciones anteriores son correctas. -> Correcto 

7. La instrucción ALTER KEYSPACE se puede utilizar para:
A. Definir un esquema.
B. Crear una tabla.
C. Ejecutar una consulta.
D. Modificar un keyspace. -> Correcto 

8. Al intentar borrar un elemento que no existe en una colección set, se produce:
A. La inserción de un nuevo elemento con dicho valor.
B. Un error en la operación de borrado.
C. Una operación que no se lleva a cabo y que tampoco genera error alguno. -> Correcto 
D. Una mutación de la colección.

9. ¿Qué es una UDT?
A. Un tipo de datos primitivo.
B. Un objeto con funciones especiales en Cassandra.
C. Un tipo de datos definido por el usuario. -> Correcto
D. Un proceso de carga de datos.

10. ¿Cuál de las siguientes instrucciones es correcta?
A. select * from client.agent where dept='AB';
B. drop index IF EXISTS clients.DeptIndex;
C. insert into University.Teacher(id,Name,Email,Description) values ( 2,'Hamilton', {'hamilton@hotmail.com'}, ['Data Science']);
D. Todas las instrucciones anteriores son correctas. -> Correcto 

## Tema 8: Neo4j
## 8.2. Descarga e instalación

- Paso 1: descarga la versión Community de Neo4j.
Figura 1. Web de descarga de MongoDB.
- Paso 2: si no tienes instalado Java en tu ordenador, descarga la versión OpenJDK 8
u Oracle Java 8. Esta versión es la recomendada para Neo4j 3.0.x. Si por alguna
razón debes usar una versión de Neo4j inferior a 2.3.0, es recomendable usar la
versión 7 de Java. Consulta el apartado «Instalar Java 8 y crear variable de
entorno» de este documento.
- Paso 3: el archivo que has descargado en el Paso 1 es un zip que contiene los
ficheros de Neo4j. Localiza dicho fichero y extrae su contenido dentro de un
directorio conocido, por ejemplo: D:\Neo4j\.
- Paso 4: el ordenador donde se instala Neo4j hará las veces de servidor. Es
recomendable crear la variable de entorno NEO4J_HOME para señalar el
directorio del Paso 3. En dicho servidor, es posible ejecutar una instancia de la
consola de Neo4j para trabajar (Paso 5.1), pero también es posible crear un
servicio en Windows que permita levantar la base de datos de forma permanente, 


- Paso 5.1: para ejecutar una instancia de Neo4j, desde la consola de Windows
PowerShell, ubícate en la ruta y ejecuta neo4j console
(<NEO4J_HOME>\bin\neo4j console). Ten en cuenta que al descomprimir el
fichero ZIP, este crea otro directorio llamando /neo4j-community-4.x.x. Se asume
que su contenido es lo que has copiado en el directorio recomendado en el Paso 3.
Si lo que copias es el directorio completo, entonces ten en cuenta este nuevo
directorio en la ruta propuesta.

- Paso 5.2: para instalar Neo4j como servicio, utiliza la instrucción
<NEO4J_HOME>\bin\neo4j install-service.
- Paso 6: si todo ha ido bien, accede a la URL http://localhost:7474 desde el
navegador web que usas frecuentemente. Utiliza el usuario neo4j con la
contraseña predeterminada neo4j. De inmediato te pedirá que cambies la
contraseña para mayor seguridad.

Observa cómo cada base de datos utiliza un puerto por defecto en las
instalaciones por defecto: MySQL utiliza el puerto 3306, MongoDB el puerto
27017, Neo4j el puerto 7474… Lo más probable y seguro es que los
administradores de bases de datos asignen puertos menos comunes.

## Instalar Java y crear variable de entorno
- Paso 1: descarga Java 8 o superior del sitio oficial de Oracle (intenta en la siguiente
URL: https://www.oracle.com/java/technologies/javase/javase-jdk8-
downloads.html). Si falla la URL anterior Si falla la URL anterior (es Oracle y cada vez que innovan mueven
cosas de su sitio web), busca en Google «Instalar Java 8

- Paso 2: ejecuta el ejecutable que has descargado e instala Java en la ruta
D:\Java\jdk1.8.0 (D es una unidad de ejemplo, puedes usar otra que consideres más
oportuna).

- Paso 3: desde Windows crea la variable JAVA_HOME, para ello da clic derecho en Equipo
o Este Equipo en el Explorador de archivos de Windows.

- Paso 4: selecciona la opción Propiedades y luego accede a Configuración avanzada del
sistema > Variables de entorno.

- Paso 5: en el recuadro Variables del sistema crea una «Nueva…» variable del sistema
cuyo nombre debe ser JAVA_HOME. A dicha variable ponle como valor de la variable la
ruta de instalación de Java, es decir, D:\Java\jdk1.8.0. Acepta todas y cada de las
ventanas abiertas (son unas cuantas).

- Paso 6: comprueba que todo está correcto. Para ello, abre una consola de Windows
y escribe las instrucciones SET JAVA_HOME para comprobar la ruta y luego java –
versión para mostrar la versión que acabas de instalar de Java.

## Instalar Neo4j como servicio en Windows
Para instalar Neo4j como servicio, basta con seguir dos pasos:
- Paso 1: desde la ruta de instalación ejecuta lo siguiente: <NEO4J_HOME>\bin\neo4j
install-service.
Figura 5. Instalar servicio de Neo4j desde la consola de Windows.
- Paso 2: comprueba que el servicio está funcionando.
Figura 6. Lista de servicios en Windows.


## 8.3. Conceptos generales
## Concepto 
- Neo4Js es una base de datos NoSQL de código abierto 
- Esta desarrollado en Java, es un tipo de base de datos se basa en la reprsentación gráfica de nodos
- Hay dos elementos claves en Neo4j: los nodos (vértices) y las relaciones (bordes). 
- En el grafo los nodos representan las entidades, mientras que las relaciones indican la asociación que hay entre los nodos. 
- Las relaciones también tienen múltiples propiedades, las cuales permiten organizar la información asociada a los nodos. 
- pero si se quisiera indicar bidireccionalidad, es necesario crear dos relaciones en sentidos opuestos.
- Toda relación siempre tendrá una dirección. La dirección que se tome en cuenta será la que sea útil para el análisis que se quiere hacer
- Esto significa que no es necesario agregar relaciones duplicadas en la dirección opuesta a menos que sea necesario para describir correctamente un caso de uso
- Se ha dicho previamente que tanto nodos como relaciones poseen propiedades
- Las propiedades son pares de nombre-valor utilizados para agregar cualidades a los nodos y las relaciones.
- El valor de la propiedad puede contener diferentes tipos de datos tales como números, cadenas y booleanos
- Recorrer los nodos en función de sus relaciones es lo que se conoce como recorrido
- En Neo4j el esquema hace referencia a los índices y restricciones que componen la base de datos.
- En Neo4j el esquema es opcional,
- Los índices permiten aumentar el rendimiento de las consultas a las bases de datos. 
- Las restricciones permiten asegurar que los datos cumplan con las reglas del dominio establecido para garantizar coherencia en el modelo. 
- En lo que respecta a las etiquetas de nodo, los tipos de relación y las propiedades, al igual que Java, son sensibles al uso de mayúsculas y minúsculas. 
- Neo4j utiliza Native GPE (motor de procesamiento de grafos) para trabajar con su formato de almacenamiento de grafos nativo 

## Recomendaciones de nombres
- Entidades -> Etiqueta del nodo  -> Comenzar con un carácter en mayúscula. -> ejemplo -> :PropietarioVehiculo
- Entidades -> Tipo de relaciones -> Todo en mayúsculas usando guion bajo. -> ejemplo -> :ACTUO_EN
- Entidades -> Propiedades -> Iniciar en minúscula y añadir mayúscula al principio de las siguientes palabas. -> ejemplo -> firstName

## 8.4. Graph Data Modelling
- El modelo de datos se representa con nodos (círculos), relaciones (flechas) y propiedades.
- Tanto los nodos como las relaciones contienen propiedades
- Las propiedades también se representan como pares clave-valor
- Las relaciones tienen direcciones unidireccionales y bidireccionales
- En una relación siempre hay un «nodo de inicio» o «nodo desde» y un «nodo hasta» o «nodo final»
- Una relación conecta dos nodos
- 

## 8.5. Interfaz Neo4j
## 8.6. CQL
- El lenguaje de consulta utilizado en Neo4j es CQL o Cypher Query Language. 
- Es un lenguaje declarativo, que permite buscar coincidencia de patrones
- CQL emplea comandos o instrucciones para manipular sus bases de datos
- Admite muchas cláusulas como WHERE y ORDER BY
- También permite usar funciones como string, aggregation, así como algunas funciones de relación.

## Tipos de datos 
- Boolean True/False
- byte Enteros de 8 bit
- short Enteros de 16 bit
- int Enteros de 32 bit
- long Enteros de 64 bit
- float Números de 32 bit con punto flotante
- doublé Números de 64 bit con punto flotante
- char Caracteres de 16 bit
- string String

## Cláusulas de CQL

**Lectura de datos**
- MATCH Especificar un patrón.
- OPTIONAL MATCH Especificar un patrón donde además es posible usar nulos en caso de que el patrón carezca de partes.
- WHERE Añadir contenido a las consultas CQL.
- START Se utiliza para encontrar los puntos de partida a través de los índices heredados.
- LOAD CSV Se usa para cargar datos desde un fichero CSV.

**Escritura de datos**
- CREATE Permite crear nodos, relaciones y propiedades.
- MERGE Comprueba si un patrón especificado existe en el grafo; en caso de que no, crea el patrón.
- SET Permite actualizar etiquetas de nodos, relaciones y propiedades.
- DELETE Permite borrar nodos, relaciones o rutas en el grafo.
- CREATE UNIQUE Mediante las cláusulas CREATE y MATCH, es posible obtener un patrón único al hacer coincidir el patrón existente y crear el que falta.
- REMOVE Permite borrar propiedades de los nodos y relaciones.
- FOREACH Permite actualizar los datos dentro de una lista (recorre la lista).

**Otras cláusulas**
- LIMIT Limita el resultado a un número de valores concreto.
- SKIP Se utiliza para establecer desde qué fila comenzar a incluir las filas en la salida.
- WITH Se utiliza para encadenar las partes de la consulta.
- RETURN Se utiliza para definir qué incluir en el conjunto de resultados de la consulta.
- ORDER BY Se utiliza junto con las cláusulas RETURN o WITH y permite organizar la salida de una consulta en orden.
- UNWIND Permite expandir una lista en una secuencia de filas.
- UNION Permite unir el resultado de múltiples consultas.
- CALL Permite llamar 

**Cláusula Match**
- MATCH (n) RETURN n: consulta todos los nodos.
- MATCH (n:Persona) RETURN n: consulta todos los nodos con la etiqueta Persona.
- MATCH (Pepe:Persona{name: "Pepe Rueda"})<-[: AMIGO_DE]-(n) RETURN n.name: retorna la lista de nodos cuya relación con Pepe:Persona es AMIGO_DE.
- MATCH (n) detach delete n: borra todos los nodos existentes.

**Otras cláusulas**
- MATCH (n) RETURN n.name, n.age ORDER BY n.age ASC LIMIT 10
- MATCH (n) RETURN n.name, n.age ORDER BY n.age ASC LIMIT toInt(3 *rand())+ 1: uso de funciones dentro de las consultas.
- MATCH (n) RETURN n.name, n.age ORDER BY n.age ASC SKIP 2
- MATCH (n) WITH n ORDER BY n.name ASC LIMIT 5 RETURN collect(n.name): devuelve el resultado de la consulta en forma de colección.
- MATCH (Pepe:Persona{name: "Pepe Rueda"}) REMOVE Pepe.nacionality RETURN Pepe: remover una propiedad (age) del nodo.
- MATCH (Pepe:Persona{name: "Pepe Rueda"}) REMOVE Pepe:Persona RETURN Pepe: borrar la etiqueta de un nodo. Puede añadir más de una etiqueta separándolas con dos puntos (:).
- MATCH (Persona) WHERE Persona.age = 25 RETURN Persona: la cláusula WHERE permite acotar la consulta añadiendo condiciones.
- MATCH (Persona) WHERE Persona.age > 18 AND Persona.age < 30 RETURN Persona
- Importante: MATCH (n) WHERE (n)-[: AMIGO_DE]->( {name: "Po"}) RETURN n: consultar los amigos de Po (Persona).

**comandos**
- Neo4j, viene con una base de datos ejemplo instalada por defectos es cobre peliculas 
- $ :play movie graph : De inmediato se desplegarán las instrucciones para cargar la base de datos
- $ :play northwind graph ; 
- 
## 8.7. Visualización de grafos
- La principal característica de Neo4j es su modo de visualizar los datos y las relaciones que existen entre ellos

## Formatos del grafo
- Hay una variedad de formatos a la hora de visualizar los datos en Neo4j. 
- Los resultados de una consulta se pueden guardar como JSON, XML, formatos tabulares y formato visual.
- Neo4j: Neo4j Browser y Neo4j Bloom -> dos herramientas visuales 


## 8.8. Caso práctico



## Videoclase 1. Neo4J
## Notas:
- ¿Cuál es el principal enfoque de Neo4j como base de datos?
  - Representación de datos en forma de grafos.
- ¿Qué versión de Neo4j se recomienda para entornos de desarrollo?
  - Community
- ¿Cuál es un requisito previo esencial para instalar Neo4j?
  - Instalar Java (OpenJDK 8 u Oracle Java 8)
- ¿Cómo se accede a la interfaz web de Neo4j una vez instalado?
  - Accediendo a la URL http://localhost:7474.
- ¿Qué variable de entorno debe configurarse para ejecutar Neo4j desde la consola?
  - NEO4J_HOME

## Videoclase 2. 
## Notas:
- ¿Qué representan los nodos en un grafo de Neo4j?
  - Entidades con propiedades.->En Neo4j, los nodos representan entidades con propiedades que permiten describir cualidades o características de esas entidades.
- ¿Qué característica es obligatoria en una relación en Neo4j?
  - Debe tener una dirección definida -> Las relaciones en Neo4j siempre deben tener una dirección clara, especificando el nodo de inicio y el nodo final
- ¿Cuál de los siguientes tipos de dato no es soportado por las propiedades en los nodos y relaciones de Neo4j?
  - Arrays -> Neo4j soporta tipos de datos como números, cadenas y booleanos para las propiedades de los nodos y relaciones, pero no menciona arrays en este contexto
- ¿Qué permite el uso de índices en Neo4j?
  - Mejorar el rendimiento de las consultas -> os índices en Neo4j mejoran el rendimiento de las consultas, permitiendo un acceso más rápido a los nodos y relaciones.
- ¿Qué función cumple el Native GPE en Neo4j?
  - Almacena grafos en formato nativo -> Neo4j utiliza el Native GPE para almacenar los datos en formato nativo de grafos, sin necesidad de utilizar una base de datos SQL o NoSQL adicional.

## Videoclase 3. Introducción a CQL
## Notas:
- ¿Qué significa CQL en Neo4j?
  - Cypher Query Language.
- ¿Qué operador lógico se utiliza en CQL para combinar varias condiciones en una consulta?
  - AND
- ¿Qué cláusula en CQL se utiliza para limitar el número de resultados devueltos por una consulta?
  - LIMIT
- ¿Cuál es la función principal de la herramienta Neo4j Bloom?
  - Permitir a los usuarios explorar patrones y clústeres usando lenguaje natural.
- ¿En qué formatos se pueden guardar los resultados de las consultas en Neo4j?
  - En JSON, XML, tabular y formato visual.


## Cuestionario 
1. ¿Cuáles son los principales componentes de un grafo?
A. El esquema, los nodos, las relaciones y las propiedades.
B. Nodos, relaciones y propiedades. -> Correcto 
C. Nodos y relaciones, las propiedades están implícitas en cada uno.
D. Ninguna de las anteriores es correcta.

2. ¿Qué afirmación define las características principales del modelo de grafos?
A. El modelo representa datos en nodos, relaciones y propiedades.
B. Las propiedades son pares clave-valor.
C. Las relaciones conectan los nodos.
D. Todas las anteriores son correctas. -> Correcto 

3. ¿Qué es CQL?
A. El lenguaje de consulta para Neo4j Graph Database.
B. Un lenguaje para insertar y borrar nodos y relaciones.
C. Un lenguaje enfocado a encontrar solo nodos dentro de un grafo.
D. Todas las afirmaciones anteriores son correctas. -> Correcto 

4. ¿Qué hace la siguiente instrucción: MATCH ( n ) DETACH DELETE n?
A. Limpia la base de datos.
B. Borra todos los nodos y relaciones de la base de datos. -> Correcto 
C. Borra solo los nodos existentes.
D. Borra los nodos y sus propiedades.

5.- La cláusula que borra etiquetas y propiedades es:
A. DELETE.
B. UNWIND.
C. REMOVE. -> Corrrecto -> REMOVE permite eliminar tanto las etiquetas como las propiedades de nodos y relaciones
D. DROP

6. ¿Qué significa n en la siguiente instrucción: MATCH ( n ) RETURN n.name, n.runs ORDER BY n.runs?
A. Cualquier nodo y relación.
B. Cualquier nodo. -> Correcto 
C. Cualquier relación con las propiedades name y runs.
D. Los nodos cuya propiedad name tiene un valor.

7. ¿La instruction MATCH ( n ) RETURN n.name order by n.name qué retorna?
A. Un grafo con los nodos n.
B. Un listado.
C. Un listado y un grafo.
D. Una lista ordenada de las propiedades nombre de todos los nodos.-> correcto 

8. ¿La instrucción CREATE (Pepe)-[r:CANTA_EN{name='Padro'}]-(Concierto) genera algún tipo de error al ser ejecutada?
A. No, crea los nodos Pepe y Concierto y su relación CANTA_EN.
B. Sí, la propiedad de la relación es incorrecta.-> Correcto 
C. Sí, no se indica una dirección o sentido de la relación. 
D. Todas las respuestas anteriores son correctas.

9. La instrucción CREATE (Juan)-[r:HIJO_DE]->(Alma) crea:
A. Los nodos Juan y Alma y una relación entre ellos llamada HIJO_DE. -> Correcto
B. Una relación entre los nodos Juan y Alma llamada HIJO_DE. 
C. Una relación saliente de Juan hacia Ana llamada HIJO_DE.
D. Ninguna de las anteriores es correcta


10. Indica qué hace la siguiente instrucción: MATCH (a:Jugador), (b:Juego) WHERE a.name = "Rabino" AND b.name = "Casino" CREATE (a)-[r:TRABAJA_EN {partida:1, victorias:5}]->(b) RETURN a,b
A. Crea los nodos a y b y asigna la relación TRABAJA_EN.
B. Crea la relación TRABAJA_EN sobre los nodos a y b.
C. Busca los nodos a y b que cumplan la condición del WHERE y luego asigna la
relación TRABAJA_EN entre ellos. -> correcto 
D. Todas las respuestas anteriores son correctas.


## Tema 9: Redis


## 9.2. Conceptos generales

- Redis surgió como un simple diccionario remoto (REmote DIctionary Server).
- Actualmente se define como una base de datos multimodelo que permite búsquedas,
mensajería, transmisión, gráficos 
- Es parte del gran número de bases de datos NoSQL 
- Redis es una de las más populares y más utilizada dentro de la tipología de bases de datos clave-valor. 
- Es una base de datos altamente veloz. 
- Trabaja con la información en memoria.
- Usa  tipología (clave-valor)

**Características de Redis**
- Las estructuras de datos son la clave principal de Redis
- Redis permite pensar en casos concretos ahí radica la estrategia del uso de estructuras de datos. 
- Soporta las siguientes estructura de datos: 
  - String.
  - Lists.
  - Sets.
  - Sorted sets.
  - Hashes.
  - Bit arrays.
  - Streams.
  - HyperLogLogs

![Ejemplo](../01_BasesDatosParaDatosMasivos/info/info_010.png)

![Ejemplo](../01_BasesDatosParaDatosMasivos/info/info_011.png)

- Soporta el patrón publicar/suscribir (pub/sub).
-  Se ejecuta del lado del servidor, principalmente en los sistemas operativos basados
en Unix como Linux y Mac, y también como un contenedor Docker en Microsoft
Windows.
-  La instalación de Redis es sencilla y su disponibilidad es casi inmediata una vez es
público. 
- El servidor espera las conexiones de los clientes, bien sea de forma programática o a través de la interfaz de línea de comandos(CLI).
- Como toda base de datos NoSQL, no es necesario definir un modelo de datos para
poder trabajar con Redis. 
- El comando SET se utiliza para crear datos dentro de la base de datos actual, sin la
necesidad de definir una estructura previa.  


**Flexibilidad de Redis y uso de memoria**
- Por su flexibilidad no se necesita un modelo de datos previo. 
- Redis almacena los datos en memoria RAM y en memoria flash en caso se que los datos se incrementen.
- Algo que radica su flexibilidad es su adminitración de la memoria cuando usa datos de manera recurrente este lo almacena en RAM si no se usa tanto en memoria Flash 
- LRU (Least Recently Used) -> Usado Menos Recientemente   
- Redis emplea diferentes métodos para cumplir con las propiedades ACID (Atomicity,Consistency, Isolation y Durability).


## 9.3. Modelo de datos, estructura y módulos
- Redis es una base de datos que soporta múltiples modelos de datos para
que estos se representen de múltiples formas, permitiendo así representar varios casos
de uso simultáneamente.
- Una base de datos de cualquier tipo obliga a pensar y decidir
sobre la forma de representar los datos dentro del almacén de datos. La forma que se
decida es la que luego definirá cómo se insertarán los datos y cómo se leerán.
- Redis almacena los datos mediante claves, las cuales pueden ser de cualquier tipo
porque realmente son elementos binarios. 
- Una imagen puede ser usada como clave dentro de la base de datos. Aunque existe esta posibilidad,
por lo general las claves son cadenas simples.
- Los bitmaps, por su parte, son una forma de almacenamiento de cadenas donde se
pueden representar muchos elementos de datos que posean, por ejemplo, un estado
determinado activado (1) o desactivado (0).
- En un escenario donde solo se quiere saber estos estados, Redis es útil por el rápido
acceso y manipulación de dichos valores.
- SETBIT y GETBIT son comandos específicos para trabajar con tipos bitmaps. Se utilizan
para crear o cambiar un valor y recuperar un valor, respectivamente. Otros comandos
son BITOP y BITFIELD.


## Lists
En determinados escenarios una lista puede ser una matriz, pero Redis la utiliza como
lista vinculada que permite operaciones de escrituras muy rápidas. Se usan para
almacenar datos con algún tipo de relación.

## Sets
Los sets son parecidos a las lists, pero se diferencian en dos aspectos:
1. En la forma de almacenar los valores porque utiliza una sola clave para almacenar varios valores.
2. En la forma de recuperar los valores; no se usa índice de posición y tampoco se ordenan.

## Hashes
Se emplean para almacenar colecciones de pares clave-valor. Un hash tiene una
clave, pero dentro de su estructura hay espacio para más campos y valores. El estado
actual de una aplicación es algo que se suele almacenar en un hash.  

El comando para crear el hash es HSET. Este permite recuperar valores concretos en
un hash concreto.

## Sets ordenados
Una variante de sets es su versión ordenada de los valores. Este tipo de datos se
utiliza cuando se quiere almacenar datos que deben estar clasificados. Al igual que
hash, una sola clave puede almacenar varios elementos. Cada valor está puntuado
con un número.

## HyperLogLog
Este es un tipo de datos especializado muy útil en Redis. Se utiliza para mantener un
recuento estimado de elementos únicos. Un caso de uso común es emplearlo para
llevar a cabo un seguimiento de un recuento general de visitantes únicos al aula
virtual. 

## Estructuras
Una funcionalidad interesante de Redis es el patrón publisher/subscriber (pub/sub)
el cual actúa como un mecanismo para intercambiar mensajes. Al usarlo, un
publicador crea un par clave-valor y otros clientes se suscriben a él para recibir dicho
mensaje (el par clave-valor creado).

## Geoespacial
La indexación geoespacial es un patrón común utilizado para codificar datos basados
en la latitud y la longitud, la cual facilita y agiliza el trabajo con datos espaciales. 

## 9.4. Arquitectura y topología

- Redis separa la administración del clúster de la arquitectura para que las solicitudes sean
atendidas tan rápido como lo serían si el servidor no se estuviera ejecutando en un clúster 
- Un servidor dentro de un clúster se denomina nodo en Redis. Los nodos podrán ser primarios o secundarios.

- El clúster de Redis Enterprise consta de los siguientes componentes:
- Capa de datos: en esta capa los datos se almacenan y administran, haciendo parte del
mismo núcleo como si se tratase de una única instancia de Redis (open source).
- Administrador de clústeres: se encarga del estado general del clúster, su supervisión,
el reequilibrio, la compartición, el aprovisionamiento y el desaprovisionamiento de
nodos, entre otras tareas.
- Proxy de latencia cero: los nodos del clúster utilizan un proxy para proporcionar
comunicación sin estado y multiproceso entre el cliente y el nodo.
- API REST: se utiliza para la gestión del clúster


**Alta disponibilidad**
Es importante en este punto volver a diferenciar las dos versiones que ofrece Redis para
trabajar. Por un lado, está Redis Open Source y, por otra parte, está Redis Enterprise.
Cuando se quiere conseguir una alta disponibilidad, con Redis Open Source el gasto en
RAM dificulta las réplicas del dato de forma simultánea.

## 9.5. Despliegue en Docker

Para que puedas poner en marcha un servidor de Redis, en este apartado se propone
una instalación basada en Docker que permita de forma rápida acceder a Redis y realizar
las pruebas de los comandos antes vistos. A continuación, se indican los pasos de
instalación

## 9.6. Drivers
Redis se integra con muchos lenguajes de programación conocidos. De forma
programática, desde estos lenguajes, es necesario crear los mecanismos para realizar
dicha conexión. Los clientes y controladores generalmente se comparten bajo una
licencia de código abierto, aunque la licencia varía según el proyecto. 

## Cuestionario 

1. Las siguientes son estructuras de Redis:
A. String, integer, float, sets y lists.
B. Lists, sets, hashes, stream y bit arrays. -> Correcto 
C. HyperLogsLogs, hashes, sets, string y float.
D. Ninguna de las anteriores es correcta.

2. ¿Cuál de estas afirmaciones es verdadera?
A. No es necesario definir previamente un modelo de datos antes de usar o guardar datos en Redis.
B. Redis se caracteriza por el tratamiento de distintos tipos de datos, los cuales se pueden aplicar en distintos casos de uso.
C. Redis es una base de datos clave-valor.
D. Todas las anteriores son correctas. -> Correcto 

3. ¿Cómo se llama el cliente de Redis?
A. Cliente Redis Long.
B. redis-cli. -> Correcto 
C. cli-rediss.
D. Ninguna de las anteriores es correcta.

4. ¿Cuál de estas instrucciones muestra todos los elementos de una lista llamada clientes?
A. LINDEX clientes 0.
B. LRANGE clientes 0 -1. -> Correcto 
C. LRANGE clientes 0 *.
D. GET clientes 1.

5. ¿Cuál de estas instrucciones permite añadir un elemento a la colección llamada frutas?
A. SADD frutas mango. -> Correcto 
B. SADD mango frutas.
C. SMEMBERS frutas mango.
D. SISMEMBERS frutas mango.

6. ¿Qué hace la siguiente instrucción: SET user pep?
A. Establece un usuario en pep.
B. Crea un elemento llamado user con el valor pep. -> Correcto 
C. Muestra el valor de user y pep.
D. Guarda el valor user en pep.

7. ¿Qué son las colecciones ordenadas?
A. Una colección cuyos elementos se ordenan por la clave.
B. Una colección cuyos elementos se ordenan por el orden en que se añaden
los valores.
C. Una colección cuyos elementos se ordenan por los valores.  -> Correcto 
D. Ninguna de las anteriores es correcta.


8. El patrón pub/sub permite:
A. Publicar datos cada cierto tiempo en un puerto concreto.
B. Crea un canal para que los clientes se suscriban y reciban los valores emitidos. ->  Correcto 
C. Publicar datos en stream para ser consumido.
D. Todas las anteriores son correctas.


9. Redis es una base de datos clave-valor que utiliza:
A. RAM y memoria flash. 
B. Solo RAM. -> Correcto 
C. RAM y memoria caché.
D. RAM SSD y Sweap.


10. ¿Qué afirmación es verdadera?
A. Dentro de un clúster de Redis, un servidor determinado se denomina cliente.
B. Cada nodo puede ser un nodo primario (maestro), pero no un nodo secundario (esclavo).
C. La administración del clúster se realiza en una capa de la arquitectura del clúster de Redis. -> Correcto 
D. El almacenamiento de datos de series de tiempo es otra tarea común en Redis.


## Videoclase 1. 
## Notas:
- ¿Cuál es la principal característica que distingue a Redis de otras bases de datos NoSQL?
  - Funciona en memoria para accesos rápidos a datos.
- ¿Qué tipo de estructuras de datos admite Redis además de strings?
  - Listas, sets y hashes.
- ¿Cuál de los siguientes comandos se utiliza en Redis para almacenar un valor asociado a una clave?
  - SET
- ¿En qué contexto es más útil Redis?
  - Acceso inmediato a datos en aplicaciones en tiempo real.
- ¿Qué características ofrece la versión Enterprise de Redis en comparación con la versión estándar?
  - Almacenamiento en memoria flash.

## Videoclase 2. Tipos de datos en Redis
## Notas:
- ¿Cuál de los siguientes tipos de datos no es compatible con Redis?
  - Tablas relacionales.
- ¿Qué módulo de Redis se utiliza para trabajar con datos de grafos?
  - RedisGraph.
- ¿Qué característica principal ofrece Redis Enterprise para garantizar alta disponibilidad?
  - Agrupamiento en clústeres y fragmentación.
- ¿Cómo Redis Enterprise optimiza la gestión de la replicación en RAM sin necesidad de una tercera réplica costosa?
  - Usando un tercer servidor para la resolución del quorum.
- ¿Cuál es el propósito de RedisSearch como módulo adicional en Redis?
  - Proporcionar búsqueda de texto completo.

## Videoclase 3. 
## Notas:
- ¿Qué puerto se utiliza para las conexiones HTTPS en Redis desplegado con Docker?
  - 8443
- ¿Qué comando se utiliza para iniciar un contenedor de Redis en Docker?
  - docker run -d --cap-add sys_resource --name rp -p 8443:8443 -p 9443:9443.
- ¿Qué cliente de Redis es recomendado para Node.js?
  - node_redis
- ¿Qué comando se utiliza para conectarse a Redis desde Docker usando redis-cli?
  - redis-cli -p 9443.
- ¿Qué cliente de Redis es más recomendado para trabajar con Python?
  - redis-py.


## Tema 10: Datos en el cloud

**Conceptos**
El uso del cloud implica, por un lado, confiar en la infraestructura de otros
proveedores y, por otra parte, usar y explotar nuestra información siguiendo
determinados protocolos. Existen proveedores que cuentan con sus propias
infraestructuras en el cloud. En otros casos, algunos dependen de otros proveedores
del cloud para proporcionar los mismos servicios. 

Oracle define el cloud computing como la capacidad de alquilar sus tecnologías de la
información, en lugar de comprarlas. En lugar de invertir mucho en bases de datos,
software y equipos, las empresas optan por acceder a la potencia de cálculo a través de
Internet y pagar por lo que consumen 


**Entre los beneficios más destacados que ofrece el cloud computing se mencionan los
siguientes:**

- Escalabilidad horizontal y vertical: cuando aumentan las necesidades de las
compañías debido a su propio negocio, el cloud se adapta y crece en función de la
demanda de recursos.

- Migraciones flexibles: las empresas pueden migrar ciertos recursos hacia o desde
la nube, o hacia diferentes proveedores de nube, según lo deseen, o
automáticamente para obtener mejores ahorros de costos, un mejor rendimiento
o para usar nuevos servicios a medida que surgen.

- Infraestructura: los clientes pueden estimar y calcular los recursos para los
distintos elementos de la infraestructura. Aunque suene negativo, los
administradores de TI no tienen la tarea de estimar y gestionar directamente los
recursos de la compañía.

- Resistencia cargas de trabajo: el servicio en la nube provee el almacenamiento
constante de los datos en distintas ubicaciones en todo el mundo.

- Pago por uso: los costes se aplican por unidades concretas de recursos usados, sin
recargos y con una facturación de servicios muy transparente.

- Protección antidesastres: el cloud elimina la necesidad de invertir en hardware para
copias de seguridad. Los servidores son globales y la gestión de copias la lleva
directamente el proveedor a nivel mundial.

- Actualizaciones automáticas, trabajo remoto y aumento de la capacidad de
colaboración: no es necesario llevar a cabo procesos de actualización de hardware o
software. los servicios de cara al usuario operan independientemente de la
infraestructura, todo lo que el cliente necesita es un mecanismo de conexión a través
de Internet.

- Seguridad: el cloud brinda los mejores estándares de seguridad disponibles en el
mercado. El cliente, las aplicaciones, los datos y el código están protegidos y
monitorizados las 24 horas.

## 10.3. Modelos de cloud computing
- Cloud privado: como su nombre indica, son servicios cloud creados para una
organización específica y solo para ella. 
  - OpenStack: https://www.openstack.org
  - CloudStack: https://cloudstack.apache.org
  - VMware: https://cloud.vmware.com

- Cloud público: Las empresas en este caso acceden a servicios del cloud a través de
Internet. Estos servicios se ajustan a la demanda del servicio y se miden (a efectos de
costes y facturación) con la demanda del servicio por minutos u horas. Las
suscripciones son otra forma de prolongar el contrato y los servicios.
  - Microsoft Azure: https://azure.microsoft.com
  - Google Cloud Platform (GPC): https://cloud.google.com
  - Servicios web de Amazon: https://aws.amazon.com
  - IBM: https://www.ibm.com/cloud

- Cloud híbrido: es una fusión de servicios de cloud público (GCP, AWS o Azure) y un
cloud privado local. Las soluciones en local se usarán más para aplicaciones críticas
dentro de la compañía, mientras que el cloud público abordará las demandas del
servicio

  - IBM: https://www.ibm.com/it-infrastructure/z/capabilities/hybrid-cloud
  - AWS: https://aws.amazon.com/enterprise/hybrid


## 10.4. Tipos de servicios cloud
Software as a Service (SaaS)
En este tipo de servicios, el proveedor del cloud centra su servicio en alojar e
implementar software del cliente en su entorno

Platform as a Service (PaaS)
Este tipo de servicio ofrece acceso a herramientas y plataformas adecuadas para
cubrir las necesidades de entornos de desarrollo para crear y gestionar aplicaciones
web, móviles o de proceso.

Infrastructure as a service (IaaS)
También llamado HaaS o Hardware as a Service. En este otro tipo, el servicio se
enfoca en ofrecer infraestructura como servicio para que el cliente haga uso del
mismo a demanda. Los clientes solo tienen que preocuparse de sus procesos y
análisis, delegando a los proveedores del servicio los componentes de infraestructura
con capacidad de cómputo, almacenamiento y de red para ejecutar los procesos del
cliente.

En IaaS el proveedor dispone de infraestructura para proveer de máquinas virtuales
a sus clientes. Con ellas se abstraen los recursos de un ordenador con un hypervisor
o VMM (Virtual Machine Monitor), el cual crea capas entre máquina host y el sistema
operativo virtualizado

Function as a Service (FaaS)
Otro de los servicios que se ofrecen sobre el cloud son funciones como servicio. Este
servicio lo utilizan desarrolladores para implementar la lógica de back-end sin la
necesidad de configurar y levantar un servidor.


Container as a Service (CaaS)
Es un modelo de servicio en la nube que permite a los usuarios cargar, organizar,
iniciar, detener, escalar y administrar contenedores, aplicaciones y clústeres. La base
de este servicio es la virtualización basada en contenedores, una interfaz de
programación de aplicaciones (API) y una interfaz de portal web.


Enfoque del servicio
Estos servicios brindan varios niveles de abstracción sobre las máquinas que
finalmente ejecutan dichos servicios. Cada servicio opera sobre un nivel diferente de
responsabilidad dentro del entorno del proveedo

![alt text](../01_BasesDatosParaDatosMasivos/info/info_012.png)

![alt text](../01_BasesDatosParaDatosMasivos/info/info_013.png)


## 10.5. Virtualización

La virtualización permite crear entornos virtuales simulando un entorno físico. El
entorno virtual por lo general incluye características y versiones del hardware que
representa, de los sistemas operativos que ejecuta, de los dispositivos de
almacenamiento configurados, de la memoria RAM empleada, etc 

Con la virtualización es posible convertir un único equipo físico o servidor en varias
máquinas virtuales. En él, cada máquina virtual puede interactuar
independientemente y levantar sistemas operativos o aplicaciones diferentes
mientras comparten los recursos de la máquina host. 

Los IaaS utilizan con frecuencia la virtualización de servidores para ofrecer sus
servicios. Mediante un software de virtualización crean sobre un servidor físico
máquinas virtuales que luego se ofrecen a los clientes para su uso


## Hipervisores
Los hipervisores son software que se encargan de separar los recursos físicos de los
entornos virtuales. Estos se pueden instalar en un hardware concreto como servidor
o hacer parte de un sistema operativo existente. En el primer caso, es el mecanismo
que utilizan las grandes empresas dedicadas a la virtualización. En el segundo caso,
se refiere a lo que se suele hacer a la hora de virtualizar algún sistema operativo sobre
un ordenador con sistema operativo funcionando

El hipervisor gestiona los recursos físicos y los divide de tal forma que todos los
entornos virtuales puedan usarlos. Estos recursos se comparten según las demandas
de cada virtualización y del propio entorno físico donde están alojadas. Cuando un
usuario interactúa con una virtualización, lo hace dentro del entorno virtual conocido
comúnmente como máquina de guest o máquina virtual


## Tipología de la virtualización

**Virtualización de escritorio:**
Permite que un servidor centralizado ofrezca y
administre escritorios de forma individual. 

Es común confundirla con la
virtualización de los sistemas operativos. Sin embargo, en la virtualización de los
escritorios existe la figura de administrador o herramienta de administración
automatizada que configura los entornos simulados de escritorio en cientos de
máquinas físicas al mismo tiempo. 

**Virtualización de red:**

se caracteriza porque divide el ancho de banda de una red
en canales independientes que se asignan a servidores o dispositivos específicos.

La virtualización de las funciones de red (NFV) permite separar las funciones de
una red para luego distribuirlas entre los entornos correspondientes. Esta
virtualización reduce la cantidad de componentes físicos tales como
conmutadores, enrutadores, servidores, cables, centrales, entre otros, necesarios
para crear redes independientes.


**Virtualización de datos o almacenamiento:** 
Combina recursos de almacenamiento
en red y los muestra como un solo dispositivo de almacenamiento accesible para
varios usuarios. La virtualización de datos permite a las empresas aplicar sobre
ellos capacidad de procesamiento, reuniéndolos desde varias fuentes y facilitando
la integración de nuevos orígenes de datos. 

## 10.6. Docker

Docker es un motor de código abierto cuya función principal es facilitar la
implementación de aplicaciones en contenedores. Su creador es Docker Inc,
conocidos en fechas pasadas como dotCloud Inc

Docker propone un sistema de implementación de aplicaciones sobre un entorno de
ejecución de contenedores virtualizado

Su entorno se caracteriza por ser rápido,
ligero y por facilitar la ejecución de su código. 

Docker se diferencia de una máquina virtual por su sencillez y requerimientos
mínimos para ejecutar un host


## Cómo funciona Docker
En un principio Docker usaba LinuX Containers (LXC) para crear sus contenedores,
pero posteriormente cambió a runC (libcontainer). Este último se ejecuta en el mismo
sistema operativo que su host, permitiendo compartir los recursos del sistema
operativo del host. El sistema de archivos que utiliza se basa en capas (AuFS) y
permite gestionar las redes del mismo 

AuFS es un sistema de archivos basado en capas, lo cual permite que se fusionen
capas de solo lectura y capas de escritura.


## Máquinas virtuales vs. Docker
Una máquina virtual completa utiliza su propio conjunto de recursos asignados y
comparte los mínimos recursos posibles. Está mucho más aislada y por ello es muy
pesada (requiere más recursos propios). Docker ofrece menos aislamiento, pero sus
contenedores son más livianos (requieren menos recursos).

Esto último permite que se ejecuten muchos contenedores en un mismo host sin destrozarlo.


![alt text](../01_BasesDatosParaDatosMasivos/info/info_014.png)

En el caso de máquinas virtuales completas, en un host es probable que el número
de máquinas ejecutándose a la vez sea muy limitado. Por otro lado, una máquina
virtual suele tardar unos minutos en iniciarse (como cualquier sistema operativo
común), mientras que los contenedores Docker/LXC/runC tardan unos pocos
segundos.

Existen pros y contras para cada tipo de virtualización. Si se necesita un aislamiento
total con recursos garantizados, una máquina virtual completa es la mejor opción. Si
por el contrario solo desea aislar procesos concretos entre sí y desea ejecutar muchos
de ellos en un único host de tamaño razonable, Docker/LXC/runC podría ser de
mucha utilidad.


Los componentes centrales que constituyen Docker son:
- El cliente y el servidor de Docker: 
Docker es una aplicación cliente-servidor. El cliente se comunica con el servidor o
demonio de Docker, que es quien hace todo el trabajo. Docker incluye cliente
mediante línea de comandos, el cual implementa una API RESTful completa

- Imágenes.

Las imágenes son los componentes básicos de Docker. Los contenedores se ejecutan
a partir de imágenes concretas. Las imágenes definen el ciclo de vida de Docker y se
basan en un formato en capas


- Registros.

Existen dos tipos de registro: públicos y privados. Docker almacena las imágenes que
crea en registros. Docker, Inc., utiliza un registro público de imágenes, llamado
Docker Hub. Es recomendable crear una cuenta en Docker Hub y usarla para
compartir y almacenar tus propias imágenes

- Contenedores

Docker permite crear e implementar contenedores donde luego empaqueta
aplicaciones y servicios. A partir de las imágenes, los contenedores se lanzan con uno
más proceso en ejecución

## Cuestionario 
1. ¿Cuáles son los beneficios del cloud computing?
A. Escalabilidad, flexibilidad, seguridad, pago por uso… -> Correcto 
B. Flexibilidad, pago por uso y seguridad.
C. Escalabilidad y portabilidad.
D. Ninguno de los anteriores.



2. ¿Cuántos modelos de cloud existen?
A. Dos: público y privado.
B. Tres: público, privado y de pago.
C. Tres: público, privado e híbrido. -> Correcto 
D. Ninguno de los anteriores.

3. Una afirmación verdadera sobre SaaS:
A. SaaS es ofrecer servicios de sistemas operativos virtualizados.
B. Se centra en alojar e implementar software del cliente en el cloud para que
este luego lo use a demanda.
C. Significa Software como Servicio y ofrece al cliente licencia de todo tipo de
software. -> Correcto 
D. El cliente usa este servicio como repositorio para guardar todo el software
que compra la compañía y así no instalarlo en sus servidores principales.


4. ¿En qué se parecen PaaS e IaaS?
A. En nada, cada uno ofrece servicios totalmente diferentes.
B. PaaS ofrece determinados servicios como parte de un contexto de
plataforma; IaaS, por su parte, puede que ofrezca servicios similares, pero de
forma independiente. -> Correcto 
C. Ambos ofrecen servicios parecidos, solo que uno le da un enfoque más
corporativo y el otro se centra más en resolver problemas puntuales del cliente.
D. Ninguna de las anteriores es correcta.

Tal y como se indica, los servicios podrán ser similares en ciertos casos, pero el
enfoque del primero va orientado a que el cliente disfrute de las ventajas de toda una
plataforma de trabajo y no de servicios individualizados.


5. ¿Qué clase de servicio se podría considerar Google Docs?
A. IaaS.
B. PaaS.
C. SaaS.-> correcto 
D. PaaS y SaaS.


Google Docs ofrece software a sus clientes mediante el cloud, por ende, el modelo
de servicio que más se ajusta es SaaS.

6. El encargado de gestionar los recursos físicos y distribuirlos de forma equitativa
para que las virtualizaciones hagan uso de ellos es:
A. Docker.
B. Cloud computing.
C. SaaS.
D. Hipervisor. -> Correcto 
Esta es la responsabilidad del hipervisor. Docker incorpora un hipervisor, pero existen
otros que utilizan otros mecanismos y configuraciones

7. Los componentes de Docker son:
A. Los registros.
B. Las imágenes.
C. Los contenedores.
D. Todos los anteriores son correctos. -> Correcto 


8. Para trabajar con contenedores en Docker, ¿qué es lo primero que debemos
descargar?
A. El propio contenedor.
B. Imágenes. -> Correcto 
C. Registros.
D. Ninguno de los anteriores.

La imagen posee el kernel del sistema operativo sobre el cual se creará el contenedor.
Por lo tanto, es lo primero que debemos descargar.


9. ¿Qué hace el comando docker rm id_contenedor?
A. Borra todos los contenedores que se hayan creado previamente.
B. Borra el contenedor y limpia la imagen para crear nuevos contenedores.
C. Borra el contenedor cuyo id corresponde con el descrito siempre que esté
detenido. -> Correcto 
D. Borra un contenedor cuyo id es id_contenedor.

Docker no permite borrar contenedores que se estén ejecutando, por ello,
previamente debemos detener el contenedor y luego borrarlo con esta instrucción.
Es necesario también usar el id del contenedor que se quiere borrar.


10. ¿Qué hace el comando docker images?
A. Muestra la lista de imágenes creadas o existentes. -> Correcto 
B. Muestra las imágenes con sus correspondientes contenedores asociados.
C. Muestra las imágenes que se están ejecutando.
D. Ninguna de las anteriores.
Este comando permite visualizar todas las imágenes creadas hasta el momento en
Docker. Con él podrás conocer el repositorio de cada máquina, su etiqueta y el
tamaño del espacio ocupado.


## Videoclase 1. 
## Notas:
- ¿Cuál es uno de los beneficios clave de la computación en la nube?
  - Escalabilidad horizontal y vertical según la demanda. -> no de los beneficios clave del cloud computing es la escalabilidad horizontal y vertical, lo que permite ajustar los recursos de manera flexible según las necesidades de las cargas de trabajo
  
- ¿Qué modelo de servicio en la nube permite alquilar infraestructura física completa para el desarrollo y despliegue de aplicaciones?
  - IaaS. -> El modelo IaaS (Infraestructura como Servicio) permite a las empresas alquilar infraestructura física para desarrollar y desplegar sus aplicaciones.


- ¿Qué tipo de cloud es exclusivo para una sola organización y permite una mayor personalización de hardware y software?
  - Cloud privado.-> El cloud privado es exclusivo para una organización, lo que permite personalizar el hardware, software y almacenamiento, ofreciendo mayor control y seguridad.


- ¿Qué beneficio ofrece la computación en la nube en términos de protección contra desastres?
  - Gestión global de copias y recuperación antidesastres.


- ¿Cuál de los siguientes es un proveedor de cloud público?
  - AWS.-> WS (Amazon Web Services) es uno de los proveedores de cloud público mencionados, junto con Microsoft Azure y Google Cloud Platform.

## Videoclase 2. Tipos de Servicios en el Cloud
## Notas:
- ¿Qué característica define a Software as a Service (SaaS?
  - Acceso a aplicaciones a través de Internet.

En SaaS, las aplicaciones se alojan e implementan por el proveedor y son accesibles a través de Internet, con un modelo de pago por uso.


- ¿Cuál es la principal diferencia entre IaaS y FaaS en los servicios cloud?
  - IaaS proporciona infraestructura virtual, mientras que FaaS se enfoca en la lógica de back-end sin servidor.

IaaS proporciona infraestructura virtual a demanda, mientras que FaaS permite implementar la lógica de back-end sin necesidad de servidores, centrándose en el código.


- ¿Qué permite la virtualización en el cloud computing?
  - Ejecutar múltiples máquinas virtuales en un solo servidor físico.

La virtualización permite crear múltiples máquinas virtuales en un solo servidor físico, optimizando el uso de recursos y mejorando la escalabilidad.

- ¿Cuál es la principal diferencia entre Docker y las máquinas virtuales tradicionales?
  - Docker es más ligero y rápido que las máquinas virtuales.

Docker es más ligero y rápido que las máquinas virtuales tradicionales, ya que utiliza contenedores que comparten el mismo sistema operativo, lo que lo hace más eficiente en términos de recursos.

- ¿Qué es Docker Hub?
  - Un registro público de imágenes de Docker.

Docker Hub es un registro público donde se almacenan y comparten imágenes de Docker, facilitando el acceso a componentes para la creación de contenedores.

## Videoclase 3. Uso de Docker
## Notas:
- ¿Qué opción se debe habilitar durante la instalación de Docker Desktop en Windows?
  - Enable Hyper-V Windows Features.

Durante la instalación de Docker Desktop en Windows, es necesario habilitar la opción Enable Hyper-V Windows Features para permitir que Docker funcione correctamente en Windows.


- ¿Qué comando se utiliza para descargar la imagen de MongoDB en Docker?
  - docker pull mongo.

El comando docker pull mongo se utiliza para descargar la imagen de MongoDB en Docker.


- ¿Qué comando se utiliza para descargar la imagen de MongoDB en Docker?
  - docker run -it -v e:/MongoDB/mongodata:/data/db --name mongodb -d mongo.

El comando docker run -it -v e:/MongoDB/mongodata:/data/db --name mongodb -d mongo se utiliza para iniciar un contenedor de MongoDB en Docker con un volumen que mapea un directorio local al almacenamiento de la base de datos.


- ¿Qué comando se utiliza para ver los contenedores activos en Docker?
  - docker ps.

El comando docker ps se utiliza para ver los contenedores activos en Docker.


- ¿Cómo se pueden gestionar los contenedores de MongoDB en Docker (detener, iniciar, eliminar)?
  - docker stop/start/rm.





















## Videoclase 1. 
## Notas:
- 
  - 
- 
  - 
- 
  - 
- 
  - 
- 
  - 

## Videoclase 2. 
## Notas:
- 
  - 
- 
  - 
- 
  - 
- 
  - 
- 
  - 

## Videoclase 3. 
## Notas:
- 
  - 
- 
  - 
- 
  - 
- 
  - 
- 
  - 


## Cuestionario 

