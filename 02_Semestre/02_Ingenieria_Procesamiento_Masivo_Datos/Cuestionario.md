# Tema 1. Introducción a las tecnologías big data

1. En la sociedad actual, la mayoría de los datos que se generan a diario son…
A. Datos no estructurados generados por las personas. -> **correcto**
B. Datos estructurados generados por máquinas.
C. Datos estructurados generados por las personas.


2. ¿Qué retos presentan los datos generados por personas en una red social?
A. Son datos no estructurados (imágenes, vídeos), más difíciles de procesar.
B. Son datos masivos.
C. Las dos respuestas anteriores son correctas. -> **Correcto**

3. El término commodity hardware se refiere a…
A. Máquinas remotas que se alquilan a un proveedor de cloud como Amazon.
B. Máquinas muy potentes que suelen adquirir las grandes empresas.
C. Máquinas de potencia y coste normales, conectadas entre sí para formar un clúster más potente. -> **Correcto**

4. Un proyecto se denomina big data cuando…
A. Solo se puede resolver gracias a las tecnologías big data.
B. La forma más eficaz y directa de abordarlo implica tecnologías big data.-> **Correcto**
C. El problema que resuelve contiene simultáneamente las tres «v». 

5. Las tres «v» del big data se refieren a:
A. Volumen, velocidad y variedad. -> **Correcto**
B. Voracidad, volumen y velocidad.
C. Ninguna de las respuestas anteriores es correcta.

6. Lo mejor, si necesitamos más potencia de cómputo en un clúster big data, es…
A. Reemplazar algunas máquinas del clúster por otras más potentes.
B. Aumentar el ancho de banda de la red.
C. Añadir más máquinas al clúster y aprovechar todas las que ya había. -> **Correcto**

7. El sistema de ficheros precursor de HDFS fue…
A. GFS. -> **Correcto**
B. Apache Hadoop.
C. Apache MapReduce.

8. Una distribución de Hadoop es…
A. Un software con licencia comercial para clústeres, difundido por Microsoft.
B. Un conjunto de aplicaciones del ecosistema Hadoop, con versiones
interoperables entre sí y listas para usarse. -> **correcto**
C. Ninguna de las opciones anteriores es correcta.

9. ¿Qué compañías fueron precursoras de HDFS y MapReduce?
A. Google y Microsoft, respectivamente.
B. Google, en los dos casos. -> **correcto**
C. Google y Apache, respectivamente. 

10. Definimos big data como…
A. Todos aquellos algoritmos que se pueden ejecutar sobre un clúster de
ordenadores.
B. Las tecnologías distribuidas de Internet que posibilitan una sociedad
interconectada por las redes sociales.
C. Las tecnologías que permiten almacenar, mover, procesar y analizar
cantidades inmensas de datos heterogéneos. -> **correcto**

## Videoclase 1. Sociedad de la información

- ¿Cuál es uno de los desafíos principales en la era de la sociedad interconectada? 
- La capacidad de asimilar y almacenar el flujo constante de datos en tiempo real.

- ¿Qué permite la utilización de tecnologías de Big Data en las empresas? 
- Almacenar y procesar grandes volúmenes de datos para tomar decisiones informadas.

- ¿Cuál es un beneficio significativo de la interacción humano-máquina?
- Mejora de la accesibilidad para personas con discapacidades.

- ¿Cuál es un impacto positivo del uso de Big Data en la atención médica? 
- Personalización del tratamiento según el perfil del paciente.

- ¿Qué rol juega el Smart Data en la Industria 4.0?
- Permite la optimización de procesos y la mejora de la calidad.


## Videoclase 2. Tecnologías big data

- ¿Qué caracteriza al volumen en el contexto de Big Data? 
- La cantidad masiva de datos generados y recopilados.

- ¿Qué implica la velocidad en Big Data? 
- La rapidez con la que se generan, recopilan y procesan los datos.

- ¿Qué se entiende por variedad en el contexto de Big Data? 
- Los diferentes tipos de datos que se generan y recopilan.

- ¿Por qué es importante la veracidad en Big Data?
- Para asegurar que los datos sean precisos y confiables.

- ¿Qué se busca al extraer valor de los datos en Big Data? 
- Transformar datos brutos en insights accionables.



## Videoclase 3. Origen de las tecnologías big data
- ¿Cuál es una de las características clave de los datacenters utilizados para Big Data? 
- Escalabilidad

- ¿Qué mide el término FLOPS en el contexto del procesamiento de Big Data? 
- Las operaciones de punto flotante por segundo. 

- ¿Cuál es una diferencia clave entre la computación paralela y la computación distribuida? 
- La computación paralela se centra en la ejecución simultánea de tareas dentro de una máquina

- ¿Cuál es el enfoque principal de High-Throughput Computing (HTC)?
- Realizar cálculos científicos complejos. => HTC (High-Throughput Computing) se enfoca en la capacidad de manejar y procesar un gran número de trabajos computacionales independientes en paralelo.

- ¿Cuál es una ventaja de implementar soluciones de Big Data en la nube? 
- Escalabilidad fácil y flexible.

# Tema 2. HDFS y MapReduce

1. ¿Cuánto ocupa en total un archivo de 500 MB almacenado en HDFS, sin
replicación, si se asume el tamaño de bloque por defecto?
A. Ocupará 500 MB. -> **correcto**
B. Ocupará 512 MB, que son 4 bloques de 128 MB, y hay 12 MB
desperdiciados.
C. Ocupará lo que resulte de multiplicar 500 MB por el número de datanodes
del clúster.


2. ¿Cuál de las siguientes afirmaciones respecto a HDFS es cierta?
A. El tamaño de bloque debe ser siempre pequeño para no desperdiciar espacio.
B. El factor de replicación es configurable por fichero y su valor, por defecto, es 3. -> **correcto**
C. Las dos respuestas anteriores son correctas.

3. ¿Qué afirmación es cierta sobre el proceso de escritura en HDFS?
A. El cliente manda al namenode el fichero, que, a su vez, se encarga de escribirlo en los diferentes datanodes.
B. El cliente escribe los bloques en todos los datanodes que le ha especificado el namenode. -> **correcto**
C. El cliente escribe los bloques en un datanode y este envía la orden de escritura a los demás.

4. En un clúster de varios nodos donde no hemos configurado la topología…
A. Es imposible que dos réplicas del mismo bloque caigan en el mismo nodo.
B. Es imposible que dos réplicas del mismo bloque caigan en el mismo rack. -> **correcto**
C. Las dos respuestas anteriores son falsas.

5. Cuando usamos namenodes federados…
A. Cada datanode puede albergar datos de uno de los subárboles. -> **correcto**
B. La caída de un namenode no tiene ningún efecto en el clúster.
C. Ninguna de las respuestas anteriores es correcta.

6. ¿Por qué se dice que HDFS es un sistema escalable?
A. Porque reemplazar un nodo por otro más potente no afecta a los namenodes.
B. Porque un clúster es capaz de almacenar datos a gran escala.
C. Porque se puede aumentar la capacidad del clúster añadiendo más nodos. -> **correcto**

7. ¿Qué tipo de uso suele darse a los ficheros de HDFS?
A. Ficheros de cualquier tamaño que se almacenan temporalmente.
B. Ficheros de gran tamaño que se crean, no se modifican, y sobre los que se realizan frecuentes lecturas. -> **correcto**
C. Ficheros de gran tamaño que suelen modificarse constantemente.

8. La alta disponibilidad de los namenodes de HDFS implica que…
A. La caída de un namenode apenas deja sin servicio al sistema de ficheros durante un minuto antes de que otro entre en acción. -> **correcto**
B. Es posible escalar los namenodes añadiendo más nodos.
C. La caída de un datanode deja sin servicio al sistema durante unos pocos segundos hasta que este es sustituido.

9. El comando de HDFS para moverse a la carpeta /mydata es…
A. hdfs dfs –cd /mydata.
B. hdfs dfs –ls /mydata.
C. No existe ningún comando equivalente en HDFS. -> **correcto**

10. ¿Qué inconveniente presenta MapReduce?
A. No es capaz de procesar datos distribuidos cuando son demasiado grandes.
B. Entre las fases map y reduce , siempre lleva a cabo escrituras a disco y movimiento de datos entre máquinas. -> **correcto**
C. Es una tecnología propietaria y no es código abierto.


## Videoclase 1. Hadoop 
- ¿Qué componente de Hadoop se encarga de almacenar grandes cantidades de datos distribuidos en diferentes nodos?
- HDFS. =>  HDFS (hadoop distributed file system), es el sistema de ficheros distribuido de Hadoop que permite almacenar grandes cantidades de datos en la computación distribuida (nodos de un cluster).

- ¿Cuál de los siguientes componentes gestiona los recursos y la ejecución de tareas en un clúster Hadoop? 
- YARN =>  YARN Hadoop es uno de los principales componentes del framework de la herramienta Apache Hadoop. Significa “Yet Another Resource Negotiator” y es el encargado de administrar los recursos que forman el ecosistema de Apache Hadoop. 

- ¿Cuál es el nombre del nodo principal responsable de almacenar los metadatos del sistema de archivos en HDFS? 
- NameNode => El NameNode (NN) es el maestro o nodo principal del sistema. No se encarga de almacenar los datos en sí, sino de gestionar su acceso y almacenar sus metadatos

- En la arquitectura HDFS, ¿qué componente almacena efectivamente los bloques de datos?
- DataNode => Los DataNodes (DN) se corresponden con los nodos del clúster que almacenan los datos. Se encarga de gestionar el almacenamiento del nodo.


- ¿Qué función realiza el Secondary NameNode en Hadoop? 
- Ayuda a evitar la pérdida de datos del NameNode. => Ejecuta los trabajos de MapReduce.

## Videoclase 2. HDFS
- ¿Qué rol desempeña el NameNode en HDFS?
- Mantiene y gestiona los metadatos del sistema de archivos. => (NN). Este componente es único nodo que conoce la lista de ficheros y directorios del clúster. El sistema de ficheros no se puede usar sin el NameNode.

- ¿Cuál de las siguientes afirmaciones describe mejor la función de los DataNodes en HDFS? 
-  Almacenan los bloques reales de datos. => Almacenan los bloques reales de datos, debido a que se asemeja a una tabla de contenidos, en la que se asignan bloques de datos a DataNodes. Debido a esto, necesita menos espacio de disco, pero más recursos computacionales (memoria y CPU) que los DataNodes.

- ¿Qué sucede si el NameNode falla en un clúster Hadoop sin alta disponibilidad configurada? 
- El clúster HDFS se detiene y no puede procesar nuevas peticiones. => Para que el cluster HDFS no se detenga, se puede configurar para que exista un NameNode primario activo y un NameNode secundario en espera (o más de uno a partir de Hadoop 3) que actúa como esclavo. Este último toma el control y responde a las peticiones de los clientes si se detecta algún fallo o el nodo primario deja de estar disponible. Estos nodos deben estar sincronizados y tener los mismos metadatos almacenados. Existen dos mecanismos para conseguir esta sincronización. 

- ¿Qué mecanismo utiliza HDFS para asegurar la disponibilidad de los datos almacenados en los DataNodes? 
-  Replicación de datos en múltiples DataNodes. => Replicación de datos en múltiples DataNodes, en Hadoop 2 se introduce el concepto de alta disponibilidad, evitando que exista un único punto de fallo en el sistema.

- ¿Qué componente de HDFS se encarga de notificar al NameNode sobre la salud y la disponibilidad de los DataNodes?
-  Heartbeat. => Para garantizar la tolerancia a fallos, si un datanode deja de estar disponible, el namenode lo detecta mediante un proceso de heartbeat y vuelve a replicar los bloques perdidos en otras máquinas que sí estén disponibles.

## Videoclase 3. MAP- Reduce
- En la arquitectura de MapReduce, ¿qué hace la fase de «Map»?
- Divide los datos de entrada en pares clave-valor intermedios. => Divide los datos de entrada en pares clave-valor intermedios, cada nodo esclavo (worker) aplica la función map a los datos locales, y escribe la salida en un almacenamiento temporal. Un nodo maestro garantiza que sólo se procese una copia de los datos de entrada redundantes.

- ¿Cuál es el propósito de la fase de «Reduce» en un trabajo de MapReduce? 
- Combinar y procesar los pares clave-valor intermedios generados por los mappers. => los nodos trabajadores procesan cada grupo de datos de salida, por clave, en paralelo.

- ¿Qué componente de Hadoop gestiona la ejecución de trabajos de MapReduce? 
- JobTracker. => obTracker (Nota: En versiones más recientes de Hadoop, YARN gestiona los recursos y el JobTracker ha sido reemplazado por el ResourceManager y el ApplicationMaster)

- ¿Qué es un «Split» en el contexto de MapReduce? 
- Una división lógica de los datos de entrada que se procesa por un solo mapper. => Una división lógica de los datos de entrada que se procesa por un solo mapper, son los datos que van a ser procesados por el Mapper. Se corresponden con un un bloque del fichero.

- ¿Qué sucede si un DataNode falla durante la ejecución de un trabajo de MapReduce? 
- El NameNode reasigna las tareas a otros DataNodes. => El NameNode reasigna las tareas a otros DataNodes. De forma predeterminada, los DataNodes están configurados para escribir en discos de una manera circular. Si se utilizan discos de diferentes capacidades, o si los discos fallan y se reemplazan, el algoritmo de escritura de turnos continuos continúa escribiendo en cada disco a la vez, lo que resulta en un porcentaje diferente de capacidad utilizada en cada disco.

# Tema 3. Spark I

1. ¿Cuál es la principal fortaleza de Spark?
A. Opera en memoria principal, lo que hace que los cálculos sean mucho más rápidos.  -> **correcto**
B. Nunca da lugar a movimiento de datos entre máquinas (shuffle).
C. Las respuestas A y B son correctas.
D. Las respuestas A y B son incorrectas.

2. ¿Qué tipo de procesos se benefician especialmente de Spark?
A. Los procesos en modo batch, como, por ejemplo, una consulta SQL.
B. Los proceso aplicados a datos no demasiado grandes.
C. Los algoritmos de aprendizaje automático que dan varias pasadas sobre los mismos datos.  -> **correcto**
D. Las respuestas A, B y C son correctas.

3. ¿Cuál es la estructura de datos fundamental en Spark?
A. RDD. -> **correcto**
B. DataFrame.
C. SparkSession.
D. SparkContext

4. En una operación de Spark en la que sea necesario movimiento de datos…
A. Siempre debemos escribirlos primero en el disco local del nodo emisor.
B. No hay acceso al disco local, puesto que Spark opera siempre en memoria.
C. Spark nunca provoca movimiento de datos, a diferencia de MapReduce.
D. Las respuestas A, B y C son incorrectas. -> **correcto**

5. Elige la respuesta correcta: Cuando se ejecuta una transformación en Spark sobre un RDD…
A. Se crea inmediatamente un RDD con el resultado de la transformación.
B. Se modifica inmediatamente el RDD con el resultado de la transformación.
C. Se añade la transformación al DAG, que creará un RDD con el resultado de la transformación cuando se materialice el RDD resultante. -> **correcto**
D. Se añade la transformación al DAG, que modificará el RDD original con el resultado de la transformación cuando se materialice el RDD resultante.

6. Elige la respuesta correcta: La acción collect de Spark…
A. No existe como acción; es una transformación.
B. Aplica una función a cada fila del RDD de entrada y devuelve otro RDD.
C. Lleva todo el contenido del RDD al driver y podría provocar una excepción. -> **correcto**
D. Lleva algunos registros del RDD al driver.

7. Elige la respuesta incorrecta: Un PairRDD…
A. Es un tipo de RDD que permite realizar tareas de agregación y joins.
B. Es un tipo de RDD que contiene una tupla con un número variable de componentes. -> **correcto**
C. Es un tipo de RDD cuyo primer componente se considera la clave y el segundo, el valor.
D. Se define como cualquier otro RDD, pero con un formato concreto.

8. ¿Qué es un executor de Spark?
A. Cada uno de los nodos del clúster de Spark.
B. Un proceso creado en los nodos del clúster, preparado para recibir trabajos de Spark. -> **correcto**
C. Un nodo concreto del clúster que orquesta los trabajos ejecutados en él.
D. Ninguna de las definiciones anteriores es correcta.

9. La acción map de Spark…
A. No existe como acción; es una transformación. -> **correcto**
B. Aplica una función a cada fila del RDD de entrada y devuelve otro RDD.
C. Lleva todo el contenido del RDD al driver y podría provocar una excepción.
D. Lleva ciertos registros del RDD al driver.

10. Cuando Spark ejecuta una acción…
A. Se materializan en la memoria RAM de los workers todos los RDD intermedios necesarios para calcular el resultado de la acción y después se liberan todos.
B. Se añade la acción al DAG y no hace nada en ese momento.
C. Se materializan los RDD intermedios necesarios que no estuviesen ya materializados, se calcula el resultado de la acción y se liberan los no cacheados. -> **correcto**
D. Ninguna de las respuestas anteriores es correcta.


## Videoclase 1. Spark 

- ¿Cuál es la principal ventaja de Apache Spark sobre Hadoop MapReduce? 
- Procesamiento de datos en memoria, lo que aumenta la velocidad. 

- ¿Qué componente de Apache Spark es responsable de gestionar la distribución de tareas y recursos en un clúster?
- ClusterManager => El administrador de clúster o Clúster Manager en Spark hace referencia a la comunicación del driver con el backend para adquirir recursos físicos y poder ejecutar los executors.

- ¿Cuál de los siguientes lenguajes de programación no es soportado de manera nativa por Apache Spark? 
- Ruby.

- ¿Qué es un RDD (Resilient Distributed Dataset) en Apache Spark? 
- Una estructura de datos fundamental que permite el procesamiento distribuido tolerante a fallos.

- ¿Qué operación en Apache Spark se utiliza para aplicar una función a cada elemento de un RDD y devolver un nuevo RDD? 
-  Map => Esta función se utiliza para aplicar una transformación a cada elemento de un RDD (Resilient Distributed Dataset). Toma una función como argumento y aplica esa función a cada elemento del RDD, devolviendo un nuevo RDD con los resultados.



## Videoclase 2. Spark Arquitectura 

- ¿Cuál es la estructura de datos fundamental en Apache Spark que permite el procesamiento distribuido y tolerante a fallos? 
- RDD (Resilient Distributed Dataset). => RDD (Resilient Distributed Dataset): Es la principal abstracción de datos, el tipo de dato básico que tiene Apache Spark.  Los RDD están particionados en los distintos nodos del clúster, ya que Apache Spark se suele instalar en un clúster o conjunto de máquinas, por lo que esos RRDs se encuentran distribuidos sobre esas máquinas. Con ello se consigue la tolerancia a fallos, porque si falla una máquina tenemos el fichero en otras máquinas.

- ¿Qué componente de Apache Spark gestiona los recursos del clúster y asigna recursos para las aplicaciones? 
- ClusterManager. => ClusterManager: El administrador de clúster o Clúster Manager en Spark hace referencia a la comunicación del driver con el backend para adquirir recursos físicos y poder ejecutar los executors.

- ¿Cuál es la diferencia principal entre un DataFrame y un RDD en Apache Spark? 
- Los DataFrames proporcionan una API optimizada y utilizan un planificador de consultas, mientras que los RDDs son colecciones distribuidas de objetos. => Tanto los RDD como los conjuntos de datos proporcionan una API de estilo OOP, mientras que los DataFrames proporcionan una API de estilo SQL. En los RDD, le especificamos al motor Spark cómo realizar una determinada tarea, mientras que, con los DataFrames y los conjuntos de datos, especificamos qué hacer y el motor Spark se encarga del resto.

- ¿En qué modo de despliegue de Apache Spark el Driver Program corre en el mismo proceso que la aplicación? 
- Local Mode.=>En modo local toda la infraestructura de Spark se aloja en una sola JVM dentro de una sola computadora, el driver y el resource manager tambien se encuentran alojados.

- ¿Qué componente en Apache Spark es responsable de ejecutar una serie de transformaciones y acciones en un RDD? 
- Executor. => Executor: Los executors en Spark hacen referencia al proceso en el que estos realizan la carga de trabajo. De manera que los executors obtienen sus tareas desde el driver y llevan a cabo la carga, la transformación y el almacenamiento de los datos.




##  Videoclase 3. Spark Transformaciones 

- ¿Cuál es la característica principal de las transformaciones en Spark? 
- Son perezosas y construyen un plan de ejecución que se ejecuta cuando se llama a una acción. => Transformaciones Lazy: Las transformaciones en RDD son «lazy» (perezosas), lo que significa que no se ejecutan de inmediato. En su lugar, se registran y se ejecutan solamente cuando se realiza una acción. Esto permite la optimización y la ejecución eficiente de las operaciones.

- ¿Qué transformación en Apache Spark devuelve un nuevo RDD que solo contiene los elementos del RDD original que satisfacen una función predicada?
- Filter => En Spark, la función Filtro devuelve un nuevo conjunto de datos formado al seleccionar aquellos elementos de la fuente en los que la función devuelve verdadero. Por lo tanto, recupera sólo los elementos que satisfacen la condición dada.. 

- ¿Cuál transformación en Apache Spark combina múltiples RDDs en un solo RDD? 
- Union => Nos devuelve la unión de dos o más RDDs

- ¿Qué transformación en Apache Spark agrupa los elementos de un RDD según una clave y devuelve un RDD de pares clave-valor? 
- GroupByKey =>  Agrupa los valores de cada clave en el RDD en una única secuencia Hash particiona el RDD resultante con particiones numPartitions.

- ¿Qué transformación en Apache Spark une dos RDDs de pares clave-valor por sus claves y devuelve un nuevo RDD de pares clave y tuplas de valores? 
- Join => Devuelve un RDD que contiene todos los pares de elementos con claves coincidentes en self y other. Cada par de elementos se devolverá como una tupla (k, (v1, v2)), donde (k, v1) está en uno mismo y (k, v2) está en otro.Realiza una unión hash en todo el clúster.



# TEMA 4: Spark II

1. Elige la respuesta correcta respecto a los DataFrames de Spark:
A. Un RDD es una envoltura de un DataFrame de objetos de tipo Row.
B. Un DataFrame es una envoltura de un RDD de objetos de tipo Row. -> **correcto**
C. Un DataFrame es una envoltura de un objeto de tipo Row que contiene RDD.
D. Ninguna de las respuestas anteriores es correcta.

2. Elige la respuesta correcta sobre los DataFrames de Spark:
A. Puesto que representan una estructura de datos más compleja que un RDD, no es posible distribuirlos en memoria.
B. Puesto que son un envoltorio de un RDD, suponen una estructura de datos que sigue estando distribuida en memoria. -> **correcto**
C. Son una estructura de datos no distribuida en memoria, al igual que los DataFrames de Python o los data.frames de R.
D. Son una estructura de datos distribuida en disco.

3. ¿Qué mecanismo ofrece la API estructurada de DataFrames para leer datos?
A. Método read de la Spark Session. -> **correcto**
B. Método read del Spark Context.
C. No ofrece ningún método, sino que se utiliza la API de RDD para leer datos.
D. Método ingest de la Spark Session.

4. ¿Es obligatorio especificar explícitamente el esquema del DataFrame cuando se
leen datos de fichero?
A. No, porque solo se pueden leer ficheros estructurados como Parquet, que
ya contienen información sobre su esquema.
B. Sí, porque, si no se indica el esquema, Spark no es capaz de leer ficheros
CSV, ya que no sabe con qué tipo almacenar cada campo.
C. No, porque, si no se indica el esquema, Spark guardará todos los campos
de los que no sepa su tipo como strings.  -> **correcto**
D. No, porque, si no se indica el esquema y se intenta leer ficheros sin
esquema implícito, Spark lanzará un error.

5. Seleccione la respuesta incorrecta: ¿Por qué es aconsejable utilizar DataFrames
en Spark en lugar de RDD?
A. Porque son más intuitivos y fáciles de manejar a alto nivel.
B. Porque son más rápidos, debido a optimizaciones realizadas por Catalyst.
C. Porque los DataFrames ocupan menos en disco. -> **correcto**
D. Las respuestas A y B son correctas.

6. Tras ejecutar la operación b = df.withColumn(“nueva”, 2*col(“calif”)):
A. El DataFrame contenido en df tendrá una nueva columna, llamada nueva.
B. Llevaremos al driver el resultado de multiplicar 2 por la columna calif.
C. El DataFrame contenido en b tendrá una columna más que df. -> **correcto**
D. El DataFrame contenido en b tendrá una única columna llamada nueva

7. ¿Cuál es la operación con la que nos quedamos con el subconjunto de filas de un DataFrame que cumplen una determinada condición?
A. sample.
B. filter. -> **correcto**
C. map.
D. show.

8. Las API estructuradas de DataFrames y Spark SQL…
A. Son API que no se pueden combinar: una vez que se empieza a usar una de ellas, se tienen que hacer todas las tareas con la misma API.
B. Se pueden aplicar funciones de la API de DataFrames sobre el resultado de consultas de Spark SQL. -> **correcto**
C. Se pueden aplicar el método s q l para lanzar consultas SQL sobre DataFrames sin registrar.
D. Ninguna de las opciones anteriores es correcta.

9. La transformación map de Spark…
A. No se puede aplicar a un DataFrame porque pertenece a la API de RDD.
B. Se puede aplicar a un DataFrame porque pertenece a la API estructurada de DataFrames.
C. Se puede aplicar a un DataFrame porque envuelve un RDD al que se puede acceder mediante el atributo rdd . -> **correcto**
D. No existe en Spark; map es una acción


# 

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

# 

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


# 

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




# Tema 5. Spark III 


1. ¿Qué diferencia Spark MLlib de Spark ML?
A. Spark MLlib ofrece interfaz para DataFrames en todos sus componentes, mientras que Spark ML sigue utilizando RDD y ha quedado obsoleta. 
B. Spark MLlib no permite cachear los resultados de los modelos, mientras que Spark ML sí.
C. Spark MLlib es más rápida entrenando modelos que Spark ML.
D. Ninguna de las respuestas anteriores es correcta.

2. ¿Qué tipo de componentes ofrece Spark ML?
A. Estimadores y transformadores para ingeniería de variables y para normalizar datos.
B. Estimadores y transformadores para preparar los datos para el formato requerido por los algoritmos de aprendizaje automático de Spark.
C. Solo pipelines que no dan acceso a los estimadores internos.
D. Las respuestas A y B anteriores son correctas.


3. ¿Cuál es el método principal de un estimator de Spark ML?
A. El método fit.
B. El método transform.
C. El método estimate.
D. El método describe.


4. ¿A qué interfaz pertenecen los algoritmos de machine learning de Spark cuando
aún no han sido entrenados?
A. Transformer.
B. Estimator.
C. Pipeline.
D. DataFrame.

5. ¿A qué interfaz pertenecen los modelos de Spark ML cuando ya han sido
entrenados con datos?
A. Transformer.
B. Estimator.
C. Pipeline.
D. DataFrame.


6. ¿Qué ocurre si creamos un StringIndexer para codificar las etiquetas de una variable en el dataset de entrenamiento y después creamos otro StringIndexer para codificar los datos de test en el momento de elaborar predicciones?
A. Obtendremos la misma codificación en los dos.
B. Da un error, porque un mismo StringIndexer no puede añadirse a dos pipelines.
C. Podríamos obtener codificaciones distintas de la misma etiqueta en los datos de entrenamiento y en los de test, lo que falsearía los resultados de las predicciones.
D. Ninguna de las respuestas anteriores es correcta.


7. ¿Cuál es la estructura principal que maneja Spark Structured Streaming?
A. DStreams.
B. DStreams DataFrames.
C. Streaming DataFrames.
D. Streaming RDD.

8. Spark Streaming permite leer flujos de datos:
A. Solo desde tecnologías de ingesta de datos como Apache Kafka.
B. Desde cualquier fuente de datos, siempre que contenga un esquema, como, por ejemplo, una base de datos.
C. Desde fuentes como Apache Kafka y HDFS, si activamos la inferencia de esquema.
D. Las respuestas A, B y C son incorrectas.

9. En Spark Streaming, una vez se ejecuta la acción start:
A. El driver espera automáticamente a que concluya la recepción de flujo para
finalizar su ejecución.
B. Hay que ejecutar un método para indicar al driver que no finalice
automáticamente y que espere a que concluya la recepción del flujo.
C. Un flujo de datos no tiene fin y, por tanto, el driver nunca puede finalizar.
D. Ninguna de las opciones anteriores es correcta.

10. ¿Qué acciones pueden realizarse en Spark Structured Streaming?
A. take.
B. show.
C. start.
D. collect.





# 

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




