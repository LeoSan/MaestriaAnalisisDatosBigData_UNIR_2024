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
