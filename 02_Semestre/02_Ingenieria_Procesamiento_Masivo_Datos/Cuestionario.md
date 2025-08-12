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
A. Ocupará 500 MB.
B. Ocupará 512 MB, que son 4 bloques de 128 MB, y hay 12 MB
desperdiciados.
C. Ocupará lo que resulte de multiplicar 500 MB por el número de datanodes
del clúster.


2. ¿Cuál de las siguientes afirmaciones respecto a HDFS es cierta?
A. El tamaño de bloque debe ser siempre pequeño para no desperdiciar
espacio.
B. El factor de replicación es configurable por fichero y su valor, por defecto,
es 3.
C. Las dos respuestas anteriores son correctas.

3. ¿Qué afirmación es cierta sobre el proceso de escritura en HDFS?
A. El cliente manda al namenode el fichero, que, a su vez, se encarga de
escribirlo en los diferentes datanodes.
B. El cliente escribe los bloques en todos los datanodes que le ha
especificado el namenode.
C. El cliente escribe los bloques en un datanode y este envía la orden de
escritura a los demás.

4. En un clúster de varios nodos donde no hemos configurado la topología…
A. Es imposible que dos réplicas del mismo bloque caigan en el mismo nodo.
B. Es imposible que dos réplicas del mismo bloque caigan en el mismo rack.
C. Las dos respuestas anteriores son falsas.

5. Cuando usamos namenodes federados…
A. Cada datanode puede albergar datos de uno de los subárboles.
B. La caída de un namenode no tiene ningún efecto en el clúster.
C. Ninguna de las respuestas anteriores es correcta.

6. ¿Por qué se dice que HDFS es un sistema escalable?
A. Porque reemplazar un nodo por otro más potente no afecta a los
namenodes.
B. Porque un clúster es capaz de almacenar datos a gran escala.
C. Porque se puede aumentar la capacidad del clúster añadiendo más nodos.

7. ¿Qué tipo de uso suele darse a los ficheros de HDFS?
A. Ficheros de cualquier tamaño que se almacenan temporalmente.
B. Ficheros de gran tamaño que se crean, no se modifican, y sobre los que se
realizan frecuentes lecturas.
C. Ficheros de gran tamaño que suelen modificarse constantemente.

8. La alta disponibilidad de los namenodes de HDFS implica que…
A. La caída de un namenode apenas deja sin servicio al sistema de ficheros
durante un minuto antes de que otro entre en acción.
B. Es posible escalar los namenodes añadiendo más nodos.
C. La caída de un datanode deja sin servicio al sistema durante unos pocos
segundos hasta que este es sustituido.

9. El comando de HDFS para moverse a la carpeta /mydata es…
A. hdfs dfs –cd /mydata.
B. hdfs dfs –ls /mydata.
C. No existe ningún comando equivalente en HDFS.

10. ¿Qué inconveniente presenta MapReduce?
A. No es capaz de procesar datos distribuidos cuando son demasiado
grandes.
B. Entre las fases map y reduce , siempre lleva a cabo escrituras a disco y
movimiento de datos entre máquinas.
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

