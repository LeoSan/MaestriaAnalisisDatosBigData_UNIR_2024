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
