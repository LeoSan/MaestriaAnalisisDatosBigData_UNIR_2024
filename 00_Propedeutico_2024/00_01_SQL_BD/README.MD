# TEMA 1 : APLICACIONES Y PROPÓSITOS DE LOS SISTEMAS DE BASES DE DATOS


## ¿Qué propiedad no se corresponde con las propiedades principales de las bases de datos ACID?

a.
Atomicidad.

b.
Consistencia.

c.
Independencia. ⬅️

d.
Durabilidad.


## Señala la opción correcta. El problema de la redundancia, ¿a qué se refiere?

a.
A la repetición de datos en diferentes lugares.⬅️

b.
La interconexión de datos con otras bases de datos.

c.
A la presencia de los mismos datos en un lugar.

d.
A la prioridad de archivos para almacenar los datos relevantes.

## ¿Qué tipo de empresas fueron pioneras en utilizar las bases de datos por toda la geografía?

a.
Automovilísticas.

b.
Compañías aéreas.⬅️

c.
Logísticas.

d.
Dedicadas al turismo.


## El problema de acceso concurrente ¿en qué consiste?

a.
Los datos no están disponibles cuando se quiere acceder desde distintas operaciones simultáneamente.

b.
Solo puede acceder a la base datos un usuario al mismo tiempo.

c.
Los usuarios pueden actualizar sus datos de una manera simultánea, pero puede existir un problema en la corrección del resultado si no se controla adecuadamente. ⬅️

d.
Los usuarios no pueden actualizar sus datos de una manera simultánea.

## ¿Cuándo una operación es atómica?

a.
Cuando no existen pasos intermedios.

b.
Cuando existen varias transacciones iguales.

c.
Cuando es imposible de describir su formato.

d.
Cuando se ejecutan todos los pasos o ninguno.⬅️

## ¿Qué es un sistema de gestión de base de datos (SGBD)?

a.
Un conjunto de datos estructurados y relacionados entre sí.

b.
Una BD y las herramientas para gestionarlos.⬅️

c.
El lenguaje utilizado para realizar consultas.

d.
Todas las anteriores son correctas.

## Señalar con bandera la pregunta
Texto de la pregunta
Relaciona los siguientes conceptos:
Garantiza la integridad de los datos de la BD.	Respuesta 1
Consistencia.
 
Se realizan todas las operaciones o ninguna.	Respuesta 2
Atomicidad.
 
El resultado de operaciones simultáneas da es el mismo que alguna ejecución secuencial de ellas.	Respuesta 3
Aislamiento.
 
Persistencia de las operaciones.	Respuesta 4
Durabilidad.
 
## ¿Cómo se evitan problemas de integridad?

a.
Mediante reglas que deben cumplir los datos de la BD en todo momento.⬅️

b.
Almacenando pocos datos.

c.
Evitando la presencia de limitaciones o reglas.

d.
Utilización de software de alto rendimiento para evitar estos problemas.

## Una de las ventajas de trabajar con un SGBD es:

a.
Que todos los usuarios tienen acceso a todos los datos.

b.
Que una persona puede suministrar los datos a todos los empleados de forma sencilla.

c.
La posibilidad de gestionar distintos tipos de vistas para distintos tipos de usuarios.⬅️

d.
Que cada usuario puede decidir qué datos quiere ver.

## En relación a las BD, ¿qué supuso el nacimiento de Internet?

a.
Una mejora en la seguridad de las conexiones.

b.
Una disminución de la necesidad de BD.

c.
Un aumento de interacciones entre una persona y las bases de datos.⬅️

d.
La aparición de Internet no tuvo ninguna influencia en las BD.

#TEMA 2: 

## ¿Qué nos permite realizar un lenguaje de manipulación de datos (DML)?

a.
Permite a los usuarios manipular la estructura de la base de datos.

b.
Permite a los usuarios acceder a los datos. ⬅️

c.
Permite realizar cualquier consulta que no modifique los datos.

d.
Permite insertar nuevos usuarios en la base de datos.

## ¿Qué nos permite realizar un lenguaje de definición de datos (DDL)?

a.
Definir las diferentes estructuras que almacenarán los datos. ⬅️

b.
Realizar consultas con privilegios de administrador.

c.
Acceder a los datos.

d.
Todas las anteriores son correctas.

## ¿Cómo está formada una tabla?

a.
Por campos.

b.
Por campos y relaciones.

c.
Por un sistema complejo de entidades.

d.
Por registros que están formados por campos o atributos. ⬅️

## ¿Qué lenguaje es un lenguaje anfitrión?

a.
HTML.

b.
PROLOG.

c.
SQL.

d.
JAVA.⬅️


## ¿Qué itinerario sigue el diseño de una base de datos?

a.
Crear el diseño lógico y el diseño físico.

b.
Diseño lógico, especificación de requisitos, diseño físico.

c.
Diseño lógico, diseño físico.

d.
Especificación de requisitos, diseño lógico, diseño físico. ⬅️

## ¿En qué consiste la normalización?

a.
En la creación del esquema entidad-relación.

b.
En diseñar la BD de acuerdo a reglas que permitan hacer un uso eficiente de los datos.⬅️

c.
En establecer un conjunto de reglas que deben cumplir nuestros usuarios.

d.
En crear un diseño físico que se adapte a nuestro problema.

## Uno de los objetivos de la normalización es la supresión de datos redundantes. ¿Por qué es importante?


a.
Porque ocupa espacio innecesariamente.

b.
Porque aumenta la probabilidad de que aparezcan inconsistencias en los datos.

c.
Porque aumenta la necesidad de control sobre las operaciones que implican modificación de datos.

d.
Todas las anteriores son correctas.⬅️


## ¿Qué sucede cuando se ejecuta el comando siguiente?

create table Departamento ( dept_name varchar(20),   building  varchar(15), budget numeric(12, 2) check (budget > 0),primary key (dept_name));


a.
Se produce un error indicando que ya existe otra tabla con los mismos atributos

b.
Se crea una nueva tabla con nombre Departamento⬅️

c.
Se produce un error de sintaxis indicando que el nombre de la tabla es incorrecto

d.
No sucede nada

## ¿Qué sucede cuando se ejecuta el siguiente comando?

insert into department (dept_name, building,budget) values(153,120,230);


a.
La inserción se realiza de manera correcta y el valor 153 es convertido a varchar

b.
Se produce un error debido al tipo de campo dept_name mal 

c.
No se produce un error pero nada de inserta

d.
Se produce un error indicando que no existe el comando Insert

## ¿Qué sucede cuando se ejecuta el comando siguiente?

insert into classroom values('DaVinci',122, 40123);


a.
Se inserta en la tabla classroom la tupla (‘DaVinci’, 122, 40123) 

b.
Se inserta en la tabla classroom la tupla (‘Davinci’, 122, null) 

c.
Se produce un error de valor fuera de rango ⬅️

d.
No sucede nada



# TEMA 3. El modelo relacional: estructura y operaciones

## Una BD relacional es:

a.
Un conjunto de tablas con nombre único.

b.
Un conjunto de relaciones con nombre único.

c.
A y B son correctas. ⬅️

d.
Ninguna de las anteriores.


## El esquema de una relación:

a.
Describe la estructura de la relación especificando los tipos (dominios) de sus campos, así como restricciones aplicadas a ellos. ⬅️

b.
Describe solamente los nombres de las columnas de la tabla.

c.
Permite hacer recuperaciones de datos más eficientes.

d.
No permite ningún tipo de correspondencia.


## La clave primaria:

a.
Es un atributo o un grupo de atributos mínimo que permite identificar unívocamente un registro. ⬅️

b.
Es un único atributo que identifica inequívocamente un registro.

c.
Es el primer atributo de la tabla.

d.
Es un atributo que hace referencia a otra tabla.


## Una clave alternativa es:

a.
Una superclave que ha sido seleccionada como clave primaria.

b.
Un campo que no pertenece al dominio de un atributo.

c.
Una clave foránea que no ha podido ser seleccionada como clave primaria.

d.
Una clave candidata que no ha podido ser seleccionada como clave primaria. ⬅️


## Un lenguaje de consultas es un lenguaje:

a.
Para que los usuarios puedan utilizarlo para buscar información en la base de datos. ⬅️

b.
Para que los administradores lo utilicen para solicitar información de la base de datos.

c.
Que permite al SGBD trabajar directamente con el sistema operativo.

d.
Para delimitar las operaciones de consulta.


## La operación selección, ¿qué función tiene?

a.
Mostrar al usuario las tablas de la BD que puede ver.

b.
Seleccionar columnas del conjunto total que forma una tabla.

c.
Seleccionar tuplas que satisfacen un predicado. ⬅️

d.
Satisfacer una relación.


## La unión permite:

a.
Combinar datos de dos relaciones.  ⬅️

b.
Elegir los datos que coinciden en dos relaciones.

c.
Combinar datos de dos atributos.

d.
Combinar interrelaciones.

## ¿Qué sentencia del álgebra relacional se corresponde con el comando?:

SELECT ID, name from instructor;


a.
LaTeX: \pi_{ID,name}  (instructor)

b.
LaTeX: \pi  (instructor, ID, name)

c.
Instructor (LaTeX: \pi _{ID,name} ) ⬅️ Falle 

d.
Ninguna de las anteriores


## ¿Qué sentencia del álgebra relacional se corresponde con el siguiente comando?

select salary from instructor where salary < 75000;


a.
σ salary<75000 (π salary(instructor) )

b.
instructor(σ salary<75000)

c.
π salary (σ salary<75000(instructor))

d.
Las opciones A y C son correctas ⬅️


## ¿Qué resultado se obtiene de ejecutar el comando SQL correspondiente a la siguiente consulta?

πID, name, course_id (takes ⋈ student))


a.
Relación con el esquema (ID, name, course_id) de los instructores que asesoran a los estudiantes.

b.
Relación con el esquema (ID, name, course_id) de estudiantes que han tomado cualquier curso en la universidad. ⬅️

c.
No es posible escribir un comando SQL para esa consulta.

d.
Ninguna de las opciones es correcta.






# TEMA 4 : APLICACIONES Y PROPÓSITOS DE LOS SISTEMAS DE BASES DE DATOS



## La clave primaria de una relación:

a.
Especifica el atributo que permite seleccionar una tupla.

b.
Es un conjunto de atributos que identifica una tupla de forma unívoca. ⬅️

c.
Es un conjunto de valores que identifica una tupla de forma unívoca.

d.
Es un conjunto de valores que permite ordenar las tuplas en función de su orden de inserción, desde la primera.



## El comando alter table se utiliza para:

a.
Añadir una relación a la BD.

b.
Añadir atributos a una relación de la BD.⬅️

c.
Añadir atributos a las relaciones y relaciones a la BD.

d.
Reorganizar las tuplas que contiene la tabla.


## ¿Para qué sirve la palabra distinct?

a.
Para considerar cada valor solo una vez.⬅️

b.
Para incluir una marca que permita distinguir las tuplas que tienen valores repetidos.

c.
Para eliminar de la tabla los valores repetidos.

d.
Todas las anteriores son correctas.


## ¿Para qué sirve el operador between?

a.
Para especificar comparaciones fuera de un rango.

b.
Para especificar comparaciones dentro de un rango.⬅️

c.
Para especificar las tablas en las que hay que hacer una reunión natural.

d.
Para sustituir la cláusula WHERE en la consulta.


## ¿Qué son las variables tupla?

a.
Son variables que representan una tupla de la relación donde se definen. ⬅️ falle

b.
Permiten comparar tuplas de la misma relación.

c.
A y B son correctas. ⬅️ falle

d.
Ninguna de las anteriores.⬅️ falle


## ¿Qué consulta debe realizarse para encontrar los títulos de los cursos en el departamento con nombre Comp. Sci que tienen 3 créditos?

a.
La relación department no tiene el atributo name

b.
select title from course where dept_name = ’Comp. Sci.’ and credits = 3;⬅️

c.
select title from department where dept_name = ’Comp. Sci.’ and credits =3;

d.
select title from course where AND(dept_name =’Comp. Sci.’ credits= 3);

## Considerando que la cardinalidad de la relación instructor es 12 y la cardinalidad de la relación student es 13 , ¿cuál es el resultado al ejecutar el comando siguiente?

select count(*) from instructor, student;


a.
Se produce un error por sintaxis errónea de la función de agregación count

b.
55

c.
144 

d.
Ninguna de las anteriores⬅️


## ¿Qué consulta debe realizarse para encontrar a todos los instructores que ganan el salario más alto?

a.
select ID, name from instructor where salary = (select max(salary) from instructor); ⬅️

b.
select max(salary) from instructor;

c.
select * from instructor where salary = (select max(salary) from instructor);

d.
select ID, name from instructor where salary > max(salary);



## ¿Qué consulta debe realizar para obtener los nombres de los estudiantes que comienzan con la letra A o la letra a o que terminan con la letra s?

a.
select name from student where lower(name) like 'a%' or name like '%s';

b.
select name from student where name like ‘a%s’;

c.
select name from student where lower(name) like ‘a%’ or lower(name) like ‘%s’;

d.
Las opciones A y C son correctas ⬅️


## Marque la consulta correcta para obtener las tuplas (instructor.name, student.name) que indiquen los estudiantes que son asesorados (advised) por cada instructor

a.
select instructor.name, student.name from instructor inner join advisor on instructor.ID = advisor.i_ID inner join student on advisor.s_ID = student.ID;

b.
select instructor.name, student.name from instructor, advisor, student where advisor.s_ID = student.ID AND instructor.ID = advisor.i_ID;

c.
select instructor.name, student.name from instructor join advisor on instructor.ID = advisor.i_ID join student on advisor.s_ID = student.ID;

d.
Todas las opciones son correctas ⬅️






# TEMA 5. ORGANIZACIÓN DEL CÓDIGO



## ¿Qué diferencia existe entre union all y union?

a.
union all selecciona de todas las tablas que sean compatibles con la lista de atributos dada.

b.
union muestra todos los valores y union all solo los valores distintos.

c.
union solo muestra valores distintos y union all muestra todos los valores.⬅️

d.
union all selecciona solo los valores que no se repiten.




## El comando intersect se utiliza para:

a.
Establecer un rango o sección donde se ubican los valores que buscamos.

b.
Mostrar todas las tuplas que surgen como resultado de una operación de intersección.

c.
Mostrar las tuplas que surgen como resultado de una operación de intersección, eliminando duplicados.⬅️

d.
Mostrar las tuplas que no tienen duplicado cuando se hace una operación de intersección.



## ¿Para qué sirve la palabra except?

a.
Fuerza la eliminación de valores duplicados en el resultado de una consulta.

b.
Muestra las tuplas de la primera consulta que no aparecen en la segunda. ⬅️

c.
Muestra las tuplas de la segunda consulta que no aparecen en la primera.

d.
No elimina los valores duplicados automáticamente.


## ¿Qué diferencia existe entre except all y except?

a.
except elimina los valores duplicados automáticamente, para conservar todos los valores duplicados se utiliza except all. ⬅️

b.
except all elimina todos los valores duplicados automáticamente, si se desea conservar todos los valores duplicados se utiliza except.

c.
except all permite listar los atributos que se quieren mostrar.

d.
except permite listar los atributos que se quieren mostrar.


## La cláusula group by:

a.
Permite determinar el atributo sobre el que se va a ejecutar una operación de agregación.

b.
Permite agrupar las tuplas sobre las que se va a ejecutar una operación de agregación.⬅️

c.
Permite mostrar los resultados ordenados.

d.
Permite establecer condiciones sobre los resultados de una operación de agregación.


## La cláusula having:

a.
Se coloca en la cláusula FROM y permite establecer condiciones sobre el producto cartesiano que se realiza en las tablas que se listan a continuación.

b.
Se coloca en la cláusula FROM e indica que las tablas que se listan a continuación deben operarse con la operación reunión natural.

c.
Permite definir operaciones de agregación sobre conjuntos de tuplas.

d.
Permite establecer condiciones sobre los resultados de una operación de agregación.⬅️


## ¿Qué devuelve la expresión null or true?

a.
True.⬅️

b.
False.

c.
Null.

d.
Unknown 





## ¿Cambia el resultado si se aplica distinct en las funciones de agregación max y min?

a.
Sí, porque el conjunto sobre el que se aplican es menor.

b.
Solo en min.

c.
Solo en max.

d.
No cambia. ⬅️



## Para generar una tabla con los valores máximo, mínimo, promedio y desviación estándar de los créditos de los estudiantes utilizamos:

a.
select max(tot_cred) as MAX, min(tot_cred) as MIN, round(avg(tot_cred)) as AVG, round(std(tot_cred)) as STDEV from student;

b.
select max(tot_cred) as MAX, min(tot_cred) as MIN, avg(tot_cred) as AVG, std(tot_cred) as STDEV from student; ⬅️ fallo

c.
select max(tot_cred) as MAX, min(tot_cred) as MIN, ceil(avg(tot_cred)) as AVG, ceil(std(tot_cred)) as STDEV from student;

d.
Todas las opciones son correctas


## Marque la respuesta correcta al ejecutar la siguiente consulta:

select sum(tot_cred) DIV count(*), ceil (avg(tot_cred)) from student;


a.
Se genera una tabla con dos columnas y dos filas con valores numéricos en cada fila.

b.
Los valores de las columnas en la fila resultante siempre son iguales.

c.
Los valores de las columnas en la fila resultante pueden ser diferentes.⬅️

d.
Las opciones B y C son correctas


## TEMA 6. SQL: consultas complejas y vistas


## Una subconsulta es:

a.
Una consulta que se define sobre una parte una tabla.

b.
Una consulta que se define sobre una parte de la BD.

c.
Una consulta que se utiliza para comparar el resultado de otra consulta.⬅️

d.
Una consulta que no contiene todos los elementos que pueden aparecer en la estructura sintáctica de una consulta SQL.


## Dentro de una subconsulta, ¿para qué sirve la conectiva in? 


a.
Para comprobar la pertenencia a un conjunto.⬅️

b.
Para comparar conjuntos.

c.
Para comprobar relaciones vacías.

d.
Depende del caso.


## Dentro de una subconsulta, ¿para qué sirve la conectiva some?

a.
Para comprobar la pertenencia a un conjunto.⬅️ falla 

b.
Para comparar conjuntos.

c.
Para comprobar relaciones vacías.

d.
Depende del caso.



## Dentro de una subconsulta, ¿para qué sirve la conectiva exists?

a.
Para comprobar la pertenencia a un conjunto.

b.
Para comparar conjuntos.

c.
Para comprobar relaciones vacías.⬅️

d.
Depende del caso.

## ¿Se pueden utilizar vistas en las expresiones que definen otras vistas?

a.
Sí. ⬅️

b.
No.

c.
Según sea la condición.

d.
Solo en algunas relaciones.



## ¿Qué consulta es correcta para obtener los nombres de los instructores que han impartido cursos, el id de sus cursos y la cantidad?

a.
select name, course_id, count(name) as 'N' from instructor right outer join teaches on instructor.ID = teaches.ID group by teaches.ID, name;

b.
select name, course_id, count(name) as 'N' from instructor left outer join teaches on instructor.ID = teaches.ID group by instructor.ID, name;

c.
select name, course_id, count(name) as 'N' from instructor join teaches on instructor.ID = teaches.ID group by instructor.ID, name;

d.
Las opciones A y C son correctas ⬅️


## Marque la opción correcta para que un empleado pueda obtener la información de los instructores sin tener acceso a sus salarios:

a.
create view profesores as select university.instructor.ID AS ID, university.instructor.name AS name, university.instructor.dept_name AS dept_name from university.instructor where True;

b.
create view profesores as select instructor.ID AS ID, instructor.name AS name, instructor.dept_name AS dept_name from instructor; ⬅️ falla falla 

c.
select ID, name, dept_name from instructor;

d.
Todas las opciones son correctas


## ¿Qué realiza la siguiente consulta?

select sum(enrollment) from (select count(ID) as enrollment from section natural join takes where semester = 'Spring' and year = 2009   group by course_id, sec_id) as ste;


a.
La sintaxis de la consulta es errónea. “as ste” no es parte de ella.

b.
La sintaxis de la consulta es errónea. No se puede agrupar por dos campos.

c.
Devuelve el total de estudiantes enrolados en el semestre Spring 2009. ⬅️

d.
Devuelve el máximo de estudiantes enrolados en el semestre Spring 2009


## ¿Qué consulta es válida para saber el ID de los instructores que son asesores (advisors) de algun(os) estudiante(s)?

a.
select ID from instructor where ID in (select i_ID from advisor);

b.
select ID from instructor left outer join advisor on ID =i_ID;

c.
select distinct ID from instructor join advisor on ID =i_ID;

d.
Las opciones A y C son correctas  ⬅️



¿Qué consulta es válida para saber el ID de los instructores que no son asesores (advisors) de algun(os) estudiante(s)?

a.
select ID from instructor where ID not in (select i_ID from advisor);

b.
select ID from instructor left outer join advisor on ID != i_ID;

c.
select ID from instructor right outer join advisor on ID != i_ID;

d.
Las opciones A y B son correctas ⬅️ falla 


# Tema 9: Diseño de bases de datos relacionales: características y dominios

## Las decisiones de diseño sobre BD deben:

a.
Minimizar el número de reuniones naturales.

b.
Evitar redundancia de información.

c.
Ser eficientes en la recuperación de datos.

d.
Todas las anteriores son correctas. ⬅️ 


## ¿Cuándo un dominio es atómico?

a.
Cuando los elementos del dominio se presentan como unidades indivisibles.

b.
Cuando no se tienen varios valores para dicho atributo en la misma tupla.

c.
Cuando los caracteres que forman parte del valor no tienen significados parciales.

d.
Todas las anteriores son correctas.⬅️


## Las dependencias funcionales son:

a.
Sinónimos de las claves primarias.

b.
Conceptos más amplios que las claves, que permiten establecer relaciones ente valores de atributos aunque éstos no sean clave. ⬅️

c.
Sinónimos de claves externas.

d.
Ninguna de las anteriores es correcta.


## Una dependencia funcional puede ser:

a.
Trivial, si se cumple en todas las relaciones.

b.
Completa, si la dependencia se establece en relación a un conjunto de valores en el antecedente y no a un subconjunto de ellos.

c.
Transitiva, si sigue la misma norma que el concepto matemático que ya conocemos.

d.
Todas las anteriores son correctas. ⬅️


## Normalizar es:

a.
Simplificar el diseño para que pueda ser entendido por el cliente.

b.
Evitar que se repita cualquier dato en la BD.⬅️

c.
Eliminar las redundancias en la BD.

d.
Todas las anteriores son correctas.

##  La primera forma normal (1FN) hace referencia a:

a.
Dominios atómicos. ⬅️

b.
Eliminación de dependencias transitivas.

c.
Eliminación de atributos multivalorados.

d.
Todas las anteriores son correctas.

## La segunda forma normal hace referencia a:

a.
Dominios atómicos.

b.
Eliminación de dependencias parciales de la clave primaria. ⬅️

c.
Eliminación de atributos multivalorados.

d.
Eliminación de dependencias transitivas.


La tercera forma normal hace referencia a:

a.
Dominios atómicos.

b.
Eliminación de dependencias parciales de la clave primaria.

c.
Eliminación de atributos multivalorados.

d.
Eliminación de dependencias transitivas. ⬅️ 

## La FNBC:

a.
Relaja las restricciones de la 3FN.

b.
Relaja las restricciones de la 2FN.

c.
Es más estricta que la 3FN. ⬅️ 

d.
Ninguna de las anteriores es correcta.


## Si tenemos libro (titulo,ejemplar, precio, f_edicion,autor):

a.
titulo→ autor sí es una dependencia funcional. ⬅️

b.
precio → f_edicion sí es una dependencia funcional.

c.
precio → f_edicion alguna veces es una dependencia funcional.

d.
titulo → autor no es una dependencia funcional.

# Tema 10:  Diseño de bases de datos relacionales: dependencias funcionales y descomposición


## El grafo de dependencias funcionales:

a.
Permite representar, de forma visual, el conjunto de dependencias que representa el contexto semántico del entorno que estamos modelando.

b.
Se construye colocando los atributos como nodos y las dependencias como arcos. No están permitidos multivalores en los nodos.

c.
Las respuestas A y B son correctas. mal 

d.
Ninguna de las anteriores es correcta.


## El cierre de un conjunto de dependencias funcionales:

a.
Está formado por las dependencias funcionales indicadas por el diseñador al modelar el problema.

b.
Está formado por las dependencias funcionales indicadas por el diseñador al modelar el problema y por aquellas que se derivan de la revisión con el cliente.

c.
Está formado por las dependencias funcionales indicadas por el diseñador y las que se pueden deducir a partir de ellas.   ⬅️

d.
Determina el conjunto que el diseñador establece como necesario para el sistema que está modelando.


## Dos conjuntos de dependencias funcionales:

a.
Permiten completar las restricciones de una relación cuando surgen nuevos requerimientos. MAL

b.
Son equivalentes si tienen el mismo cierre.

c.
Pueden representarse en el mismo grafo si incluyen los mismos atributos.

d.
Todas las anteriores son correctas.

## Los axiomas de Armstrong:

a.
Permiten derivar dependencias funcionales implicadas lógicamente a partir de un conjunto de dependencias dado.

b.
Permiten calcular el cierre del conjunto de dependencias dado.

c.
Comprende un grupo de axiomas básico y otros adicionales para facilitar su aplicación.

d.
Todas las anteriores son correctas. ⬅️


## Los axiomas de Armstrong son:

a.
Reflexividad, aumentatividad y transitividad.

b.
Unión, descomposición y pseudotransitividad.

c.
A y B son correctas. ⬅️

d.
Ninguna de las anteriores es correcta.



## La descomposición sin pérdida implica que:

a.
La intersección de las descomposiciones es superclave de la primera descomposición indicada.

b.
La intersección de las descomposiciones es superclave de la segunda descomposición indicada.

c.
La intersección de las descomposiciones es superclave de las dos descomposiciones generadas. ⬅️

d.
La intersección de las descomposiciones es superclave de alguna de las descomposiciones implicadas.


## Una descomposición con pérdida:

a.
Es signo de un buen diseño.

b.
Es signo de un mal diseño. ⬅️

c.
Explica que las dependencias funcionales están mal especificadas.

d.
Explica que el cierre de las dependencias funcionales no está completo.


## El cierre de un atributo:

a.
Es sinónimo del cierre de una dependencia funcional.

b.
Permite determinar si el atributo es superclave de la relación. ⬅️

c.
Es el paso previo al cálculo del cierre de dependencias funcionales.

d.
Todas las anteriores son correctas.


## El recubrimiento canónico de un conjunto de dependencias:

a.
Facilita la comprobación de la legalidad de una relación en cada actualización.

b.
Es un conjunto simplificado de dependencias funcionales que tiene el mismo cierre que el conjunto inicial.

c.
Implica lógicamente todas las dependencias del conjunto inicial.

d.
Todas las anteriores son correctas. ⬅️

## La 4FN:

a.
Está relacionada con las dependencias funcionales transitivas.

b.
Está relacionada con los atributos raros.

c.
Está relacionada con las dependencias multivaloradas. ⬅️

d.
Está relacionada con las dependencias funcionales pseudotransitivas.













