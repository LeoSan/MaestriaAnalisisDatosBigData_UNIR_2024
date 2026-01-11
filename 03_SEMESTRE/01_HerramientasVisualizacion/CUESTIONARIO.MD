# Herramientas de Visualización

# Tema 1. Introducción a las herramientas de visualización

1. Para explicar una historia basada en datos debemos:
- A. Entender los datos disponibles.
- B. Ser capaz de representarlos gráficamente con las herramientas adecuadas.
- C. Comprobar que los destinatarios entiendan el mismo mensaje que pretendes explicar.
- D. Todas las anteriores. **CORRECTA**

2. Los datos y sus relaciones no son siempre algo fácil de entender:
- A. Correcto y por ello las herramientas de visualización nos pueden ayudar a tratar con información compleja. **CORRECTA**
- B. Correcto porque los datos siempre requieren simplificar su complejidad.
- C. Incorrecto si estamos tratando con datos de carácter personal.
- D. Incorrecto si estamos tratando con datos numéricos.

3. Todas las herramientas de visualización requieren de conocimientos de programación:
- A. Incorrecto. **CORRECTA**
- B. Correcto. Tableau es un ejemplo de ello.
- C. Correcto. Google Chart es un ejemplo de ello.
- D. Correcto. D3.js y Carto son un ejemplo de ello.

4. ¿Cuáles de estas herramientas están orientadas a usuarios no desarrolladores?
- A. Tableau.
- B. Qlik.
- C. Carto.
- D. Todas las anteriores. **CORRECTA**

5. ¿Cuáles de estas herramientas están orientadas a usuarios desarrolladores?
- A. Google Chart. **CORRECTA**
- B. Carto.
- C. Qlik.
- D. Todas las anteriores. 

6. En la actualidad las principales plataformas modernas de analítica e inteligencia de negocio...
- A. Se diferencian especialmente por sus capacidades en la visualización de datos.
- B. Ya no se diferencian especialmente por sus capacidades en la visualización de datos. **CORRECTA**
- C. Requieren de usuarios avanzados en programación 

7. Enumera, según Gartner, 3 características de las herramientas modernas de visualización de datos la actualidad:
- A. Análisis avanzado, insights automatizados y catálogo automático.
- B. Seguridad, cloud y conectividad a fuentes de datos.
- C. Seguridad, soporte a la preparación de los datos y consulta mediante búsquedas en lenguaje natural.
- D. Todas son correctas. **CORRECTA**

```
Seguridad: capacidades que permiten la seguridad de la plataforma, la
administración de los usuarios, la auditoría del acceso a la plataforma y la
autenticación.
Capacidad de gestión: capacidades para rastrear el uso, gestionar cómo se
comparte la información y por quién, realizar análisis de impacto y trabajar con
aplicaciones de terceros.
Cloud: la capacidad de apoyar la construcción, despliegue y gestión de análisis y
aplicaciones analíticas en la nube.
Conectividad de la fuente de datos: capacidades que permiten a los usuarios
conectarse e ingerir datos, estructurados y no estructurados, contenidos en varios
tipos de plataformas de almacenamiento.
Preparación de datos: soporte para la combinación de datos de diferentes fuentes,
por medio de arrastrar y soltar, y realizable por los usuarios de negocio, así como la
propia creación de modelos analíticos.
Complejidad del modelo: soporte para modelos de datos complejos, incluyendo la
capacidad de manejar múltiples tablas e interoperar con otras plataformas analíticas.
Catálogo: la capacidad de generar y agregar automáticamente un catálogo que
permita la búsqueda de los objetos creados y utilizados por la plataforma.
Insights automatizados: un atributo fundamental de la analítica aumentada es la
capacidad de aplicar técnicas de machine learning e inteligencia artificial para
generar automáticamente conocimientos para los usuarios finales (por ejemplo,
identificando los atributos más importantes de un conjunto de datos).
```


8. Una página web se construye con base en los siguientes niveles:
- A. HTML y CSS.
- B. HTML y editores de código.
- C. Captura de datos y visualización.
- D. Estructura, contenido, apariencia y comportamiento **CORRECTA**

9. Se dice que HTML es un lenguaje de marcas porque:
- A. Permite las llamadas a APIS o servicios externos de terceros.
- B. Señaliza todas las líneas de código haciéndolas más legibles. 
- C. Es compatible con otros lenguajes como JavaScript.
- D. Codifica con base en etiquetas. **CORRECTA**

10. Brackets es un editor de código:
- A. Compatible con HTML, CSS y JavaScript
- B. Que incorpora un servidor web local.
- C. Que permite ver en tiempo real las modificaciones que realicemos en el código fuente.
- D. Todas son correctas. **CORRECTA**

--- 
## Videoclase 1. Generalidades

- ¿Cuál de las siguientes opciones es un objetivo principal de las herramientas de visualización de datos?
 - Simplificar la complejidad de los datos y destacar información relevante. => Las herramientas de visualización buscan simplificar datos complejos, resaltando la información más relevante y permitiendo identificar patrones que no serían evidentes de otra manera.


- Entre las herramientas de visualización para usuarios no desarrolladores, ¿cuál permite integrar datos tabulares con mapas de forma sencilla?
  - Carto. => Carto es ideal para trabajar con datos tabulares y convertirlos en mapas interactivos, ofreciendo una experiencia intuitiva para usuarios no desarrolladores.

- ¿Qué característica distingue a las herramientas de visualización para usuarios desarrolladores?
  - Altas capacidades de personalización de gráficos. => Las herramientas para desarrolladores permiten un control detallado y una personalización avanzada de las visualizaciones, aunque requieren conocimientos en programación

- ¿Cuál es una característica clave de la analítica aumentada en herramientas ABI según Gartner?
  - Generación automática de insights utilizando inteligencia artificial. => La analítica aumentada utiliza inteligencia artificial para identificar patrones automáticamente, lo que facilita el descubrimiento de insights sin intervención manual.

- ¿Cuál de las siguientes librerías utiliza HTML, CSS y JavaScript para crear gráficos avanzados con datos complejos?
  - D3.js. => D3.js es una poderosa librería que utiliza HTML, CSS y JavaScript para crear visualizaciones avanzadas y personalizables, especialmente útiles para gráficos vectoriales en formato SVG.

--- 
## Videoclase 2. Herramientas y librerías para la visualización de datos

- Cuál de las siguientes opciones describe correctamente la estructura de un documento HTML básico?
  - <body> contiene el contenido visible, y <head> contiene los metadatos y enlaces externos.

- ¿Cuál de las siguientes opciones utiliza correctamente un selector de clase en CSS?
  - .highlight { background-color: yellow; } => Falto el punto .

- ¿Qué hace el siguiente código JavaScript? 
document.getElementById(‘demo’).innerHTML = ‘Hola, Mundo!’;
  - Reemplaza el contenido HTML del elemento con id demo por el texto «Hola, Mundo!».

- ¿Cuál de los siguientes es un ejemplo de selector de ID en CSS?
  - #menu { font-size: 14px; }

- ¿Cómo se conecta un archivo CSS externo a un documento HTML?
  - <link rel="stylesheet" type="text/css" href="styles.css">

--- 

## Videoclase 3. Brackets: editor especializado para desarrollo web frontend

- ¿Cuál es una característica clave que distingue a Brackets de otros editores de código?
  - La vista previa en vivo que refleja los cambios en tiempo real. => La vista previa en vivo es una de las características más destacadas de Brackets. Permite a los desarrolladores ver cambios en HTML, CSS y JavaScript en tiempo real, lo que mejora la eficiencia en el desarrollo front-end.

- ¿Qué sucede en Brackets si una etiqueta HTML no está bien cerrada?
  - Se marca en rojo junto con las etiquetas posteriores afectadas.

- ¿Cómo se puede editar un estilo CSS asociado a una etiqueta HTML en Brackets sin abrir el archivo CSS correspondiente?
  - Presionando «Ctrl» + «E» sobre la etiqueta para desplegar el estilo asociado.

- ¿Qué lenguaje de programación no está orientado al uso principal de Brackets?
  - Python.

- ¿Cuál es una ventaja de la interfaz de Brackets según la descripción?
  - Utiliza una interfaz sencilla con ayudas en la escritura y organización del proyecto.


# Tema 2. Historia de la visualización de datos

1. Necesita ser instanciada con un new para crear un objeto:
- A. Sí. **CORRECTA**
- B. No, solo cuando le asignas valores directamente.
- C. No, solo cuando trabajas la primera vez con la gráfica.
- D. No.


2. ¿Qué función tiene?
- A. Carga el propio cargador de librerías. **CORRECTA**
- B. Importa la librería jQuery.
- C. Carga los diferentes paquetes de la librería.
- D. Carga la última versión de Google Charts.

3. La primera variable que recibe la función de JQuery es:
- A. La URL a la que se dirige la petición.  **CORRECTA**
- B. El evento que ha generado la visualización.
- C. El nombre de función destino donde se pasan los valores.
- D. El array de datos a visualizar.

````javascript 
$.get("https://docs.google.com/spreadsheet/pub?
key=0AhNdznUnSazTdElCVTRT
YzF6Zm9DSmlUQkx1NE5DY1E&output=csv", function(csvString) {
// transform the CSV string into a 2-dimensional array
var arrayData = $.csv.toArrays(csvString, {onParseValue:
$.csv.hooks.castToScalar});
...
});

//En cierta manera, cuando vemos el símbolo $ es equivalente al de JavaScript
// estándar. Quiere decir que vamos a hacer algo con el documento HTML.
````

4. añade una columna a nuestra tabla de datos:
- A. Sí, tantas veces como aparezca esta línea de código.
- B. Sí, aunque no admite valores iguales.
- C. No, porque la tabla ya viene con las columnas definidas.
- D. No.

5. Existen librerías en JQuery que nos facilitan la transformación de archivos CSV a datos comprensibles por la librería de Google Charts:
- A. Sí.
- B. No, porque jQuery no incorpora dichas funciones.
- C. No, porque CSV no es un formato compatible con Google Chart.
- D. Sí, aunque depende de que las versiones sean compatibles.  **CORRECTA**

6. nos dibujará bar charts verticales:
- A. Sí, admite tanto barras verticales como horizontales. **CORRECTA**
- B. Sí, hace lo mismo que colum chart.
- C. Sí, tanto barras independientes como apiladas.
- D. No.

7. ¿Qué hace el código cuando contiene ?
- A. Comprueba si el evento generado por otra visualización tiene el formato correcto.
- B. Comprueba si ha habido algún error con la petición http.
- C. Comprueba si ha habido algún problema en la generación de la visualización.
- D. Comprueba si los datos del archivo son coherentes

8. se utiliza para escuchar eventos que generan las visualizaciones:
- A. Sí. **CORRECTA**
- B. No, solo aplica los eventos del ratón.
- C. No, se encarga de los eventos del sistema operativo.
- D. No

9. Todas las visualizaciones de Google Chart generan los mismos tipos de eventos:
- A. Sí, porque todas funcionan de la misma forma.
- B. Sí, porque de esta forma el código es escalable.
- C. Sí, porque ello permite cambiar la gráfica sin tener que cambiar los eventos.
- D. No. **CORRECTA**


10. ¿Incluiremos el paquete para visualizar un mapa?
- A. Sí, para mostrar un país, un continente o una región. **CORRECTA**
- B. Sí, para mostrar incluso direcciones de calles.
- C. No, porque no existe dicha librería.
- D. No

--- 
## Videoclase 1. Funcionalidades principales

- ¿Cuál es la principal función de google.charts.load() en el código de Google Charts?
  - Cargar la librería de Google Charts y sus paquetes específicos. => a función google.charts.load() es crucial porque carga la librería de Google Charts junto con los paquetes específicos necesarios, como ‘corechart’ o ‘geochart’. Sin esta línea, las funciones de la librería no estarían disponibles.

- ¿Cuál es el propósito de la estructura google.visualization.DataTable()?
  - Proveer una estructura de datos estándar para almacenar las entradas del gráfico. => La estructura DataTable se utiliza para organizar y almacenar datos en un formato compatible con Google Charts, lo que permite que el gráfico pueda leerlos y representarlos visualmente.

- ¿Qué sucede si la función drawChart() se ejecuta antes de que la librería esté completamente cargada?
  - Se lanza un error porque los paquetes no están disponibles aún. =>  La ejecución prematura de drawChart() genera un error porque los paquetes de la librería aún no están disponibles. Por eso es importante usar google.charts.setOnLoadCallback(drawChart).

- ¿Cómo se personalizan los colores de un gráfico circular en Google Charts?
  - Especificando una lista de colores en la opción colors. => La opción colors permite asignar colores específicos a cada sección del gráfico, lo que es útil para mejorar la estética y la claridad de la visualización.
 
- ¿Cuál es la diferencia principal entre un gráfico tipo GeoChart y un PieChart?
  - GeoChart utiliza ubicaciones geográficas para visualizar datos mientras que PieChart representa proporciones. => GeoChart está diseñado para mostrar datos en un mapa basado en ubicaciones geográficas (como países o regiones), mientras que PieChart representa datos en forma de proporciones o secciones circulares.


--- 
## Videoclase 2. Integración de Google Chart con Spreadsheets y CSV

- ¿Qué paso es necesario para usar una hoja de Google Spreadsheet como fuente de datos en una visualización?
  - Asignar permisos de lectura públicos o para cualquier persona con el enlace. => Para conectar una visualización con Google Spreadsheets, es necesario asegurarse de que la hoja tenga permisos de lectura adecuados. Esto permite que el archivo sea accesible desde el código, sin necesidad de modificar constantemente el JavaScript.

- ¿Qué sucede si se utiliza una URL incorrecta de Google Spreadsheet en el código?
  - Aparece un error reportado por la función handleQueryResponse. => La función handleQueryResponse gestiona los errores y si la URL es incorrecta, reporta el problema mediante un mensaje de error que indica la causa específica. Esto ayuda a depurar el código.

- ¿Qué método de jQuery se utiliza para obtener el contenido de un archivo CSV?
  - $.get() => El método $.get() realiza una solicitud HTTP para obtener el contenido del archivo CSV desde una URL. Es un formato común para manejar datos externos con jQuery.

- ¿Qué parámetros son necesarios al llamar a la función google.visualization.Query?
  - headers y gid => Al usar google.visualization.Query, los parámetros headers (para indicar cuántas filas son cabecera) y gid (para identificar la hoja de trabajo específica) son esenciales para una configuración precisa del gráfico.

- ¿Cuál es el propósito de la función $.csv.toArrays al trabajar con un archivo CSV?
  - Transformar el contenido del archivo CSV en un array bidimensional. => La función $.csv.toArrays convierte el contenido del archivo CSV en un array bidimensional que puede ser interpretado fácilmente por bibliotecas como Google Charts. Esto facilita la manipulación de los datos para visualizaciones.

--- 

## Videoclase 3. Manejo de fuentes de datos y eventos en Google Chart
- ¿Qué función de Google Charts se utiliza para escuchar y gestionar eventos generados por las visualizaciones?
  - google.visualization.events.addListener => La función google.visualization.events.addListener permite registrar un evento en una visualización, ejecutando una función cuando dicho evento ocurre. Por ejemplo, en el código de muestra se utiliza para detectar cuando un usuario ordena una tabla.

- ¿Qué ocurre cuando el evento sort de una tabla es detectado por el listener en el ejemplo de código?
  - Se ordenan los datos en el objeto data y se actualiza el gráfico de barras. => En el ejemplo proporcionado, cuando el evento sort es detectado, se ejecuta el método data.sort para reordenar los datos. Posteriormente, se llama al método chart.draw para actualizar el gráfico de barras con el nuevo orden.

- ¿Cuál es el propósito del método google.visualization.DataView en el ejemplo de código?
  - Filtrar y seleccionar las columnas que se mostrarán en las visualizaciones. => 

- ¿Qué efecto tiene aplicar el método formatter.format(data, 1) al objeto de datos?
  - Aplica un prefijo de formato a la columna especificada, como $. => l método formatter.format aplica un formato específico a una columna del objeto DataTable. En este caso, añade el prefijo $ a los valores de la columna de salarios (columna 1).

- ¿Qué función es responsable de actualizar el gráfico de barras cuando se ordenan los datos de la tabla?
  - chart.draw. => La función chart.draw(view) es la encargada de redibujar el gráfico de barras después de que los datos de la tabla se hayan ordenado. Esto ocurre dentro del listener que detecta el evento sort. El gráfico se actualiza con la nueva visualización de los datos ordenados.


# Tema 3. D3.js. Introducción y funcionalidades

1. ¿Qué significa el concepto chaining en D3?
- A. Las funciones se pueden concatenar una detrás de otra separándolas con un punto.  **CORRECTA**
- B. Las funciones dependen unas de otras, y solo puedes llamarlas de una manera seguida.
- C. Las funciones permiten crear elementos HTML.
- D. Ninguna de las anteriores.

2. Si ejecutamos la sentencia :
- A. Seleccionamos el elemento p con identificador target en el HTML y añadimos el texto indicado entre comillas.
- B. Seleccionamos el elemento p con identificador target en el HTML y reemplazamos el texto existente con el indicado entre comillas.
- C. Seleccionamos el elemento target con identificador p.
- D. Ninguna de las anteriores.

3. Si ejecutamos la sentencia
- A. Seleccionamos el elemento del HTML, añadimos un elemento p y le asignamos el texto entre comillas.
- B. Seleccionamos el elemento del HTML, con identificador y le asignamos el texto entre comillas.
- C. No tiene una sintaxis correcta y no funciona.
- D. Ninguna de las anteriores.

4. Con D3, ¿podemos modificar las clases CSS de los elementos HTML?
- A. Sí.**CORRECTA**
- B. No, porque figuran un fichero independiente.
- C. No, porque D3 solo me permite trabajar con los datos.
- D. No, porque solo puedo modificar el código HTML

5. Con D3, ¿podemos modificar el estilo de un elemento HTML como, por ejemplo, el tamaño de la fuente, con una sentencia tipo ?
- A. Sí.**CORRECTA**
- B. No, porque las características de los objetos residen en las hojas de estilo.
- C. No, porque no existe una forma de modificar solo un identificador de estilo.
- D. No, porque los elementos de las hojas de estilo no son accesibles por D3.

6. ¿Qué hace la siguiente sentencia: ?
- A. Devuelve todos los elementos div del HTML con el atributo clase que contenga .
- B. Asigna a todos los elementos div del HTML la clase .
- C. Asigna a un elemento div del HTML la clase .
- D. Ninguna de las anteriores.

7. D3 permite trabajar tanto con los datos a visualizar como con elementos HTML:
- A. No, solo con datos.
- B. No, solo con elementos HTML.
- C. No, porque los elementos u objetos HTML deben codificarse antes de su visualización por el navegador.
- D. Sí. Es una de sus principales ventajas como herramienta de visualización **CORRECTA**

8. ¿Qué hace la siguiente sentencia: ?
- A. Itera por todos los elementos y les añade un elemento con el texto , donde es el contador de la iteración.
- B. Itera por todos los elementos y les añade un elemento con el texto , donde es el texto que el elemento HTML contiene.
- C. Itera por todos los elementos y les añade un elemento con el texto , donde es una constante fija previamente definida.
- D. Ninguna de las anteriores


9. Identifica si obtenemos el mismo resultado con la sentencia que con el siguiente código:

![alt text](image-2.png)

- A. Sí.
- B. No, porque la primera sentencia no es correcta.
- C. No, porque aunque la primera sentencia es correcta, el código siguiente no lo es.
- D. No, porque tanto la línea de código individual como el grupo de código son incorrectos.

10. ¿Qué hace la sentencia d ?
- A. Le asigna vacío al elemento con identificador .
- B. Devuelve el contenido del elemento con identificador .
- C. Devuelve el contenido del elemento , siendo este de formato texto.
- D. Le asigna un texto al elemento .
---
## Videoclase 1. Introducción a D3.js

- ¿Cuál de las siguientes afirmaciones sobre D3.js es incorrecta?
  -  D3.js se limita a crear gráficos estáticos y no soporta interactividad. => 

- ¿Cuál de los siguientes conceptos es central en D3.js y se refiere a la vinculación de datos a elementos del DOM?
  - Binding. => El binding es el proceso fundamental en D3.js que conecta los datos a elementos visuales en el DOM, permitiendo que la visualización se actualice automáticamente cuando cambian los datos

- ¿Cuál de las siguientes opciones no es una ventaja de utilizar D3.js para crear visualizaciones de datos?
  - Facilidad de uso para principiantes. => Si bien D3.js es una herramienta muy poderosa, su curva de aprendizaje puede ser más pronunciada que otras bibliotecas, lo que la hace menos amigable para principiantes.

- ¿Cuál de las siguientes afirmaciones sobre SVG es falsa en el contexto de D3.js?
  - SVG es la única opción para renderizar gráficos en D3.js. => Aunque SVG es el formato más común utilizado por D3.js, también es posible utilizar Canvas para renderizar gráficos.

- ¿Cuál de las siguientes opciones describe mejor el concepto de data-driven documents en D3.js?
  - La vinculación de datos a elementos del DOM para generar visualizaciones dinámicas. => La definición más precisa de data-driven documents es la vinculación de datos a elementos del DOM, lo que permite que la visualización se actualice dinámicamente en respuesta a cambios en los datos.

## Videoclase 2. Manipulación y mejores prácticas en D3.js y HTML

- ¿Cuál de las siguientes no es una ventaja de utilizar D3.js para la visualización de datos?
  - Facilidad de uso para principiantes sin conocimientos de programación. => Si bien D3.js es una herramienta poderosa, requiere un sólido conocimiento de iiJavaScript y programación en general para aprovechar al máximo sus capacidades. La curva de aprendizaje puede ser relativamente empinada para aquellos sin experiencia previa en programación.

- ¿Cuál es el concepto clave que permite enlazar datos a elementos HTML en D3.js y crear visualizaciones dinámicas?
  - Binding. => El binding es el concepto central en D3.js que permite vincular datos a elementos HTML, creando una conexión entre los datos y la visualización. Esto es lo que hace que las visualizaciones sean dinámicas y responsivas a los cambios en los datos.

- ¿Qué función de D3.js se utiliza para añadir un nuevo elemento HTML a un elemento existente?
  - append(). => La función append() en D3.js se utiliza específicamente para añadir nuevos elementos a un elemento existente en el DOM.

- ¿Cuál de las siguientes afirmaciones sobre D3.js es incorrecta?
  - D3.js requiere de plugins adicionales para funcionar en diferentes navegadores. => D3.js utiliza estándares web como HTML, CSS y SVG, por lo que funciona de forma nativa en la mayoría de los navegadores modernos sin necesidad de plugins adicionales.

- ¿Cuál es la principal razón por la que el siguiente código crea un nuevo párrafo con el texto «Párrafo nuevo» dentro del elemento <body>? 
<d3.select(“body”).append(“p”).text(“Párrafo nuevo”);>
  - La función select() selecciona el elemento body y la función append() añade un párrafo. => Este es el flujo correcto del código. Primero se selecciona el elemento body del documento HTML, luego se utiliza append() para agregar un nuevo elemento p (párrafo) como hijo del elemento body y, finalmente, se establece el texto del párrafo utilizando text().



## Videoclase 3. Integración de HTML con D3.js para visualizaciones dinámicas

- ¿Cuál de las siguientes funciones de D3.js se utiliza principalmente para seleccionar múltiples elementos HTML?
  - d3.selectAll().

- ¿Qué hace la función each() en D3.js?
  - Itera sobre cada elemento de una selección y ejecuta una función.

- ¿Cuál es la función de d3.style() en el siguiente código: d3.select(“p#target”).style(“font-size”, “40px”);?
  - Establece el tamaño de la fuente.

- ¿Cuál de las siguientes opciones es la forma correcta de seleccionar un elemento div dentro de un elemento section con ID “section1”?
  - d3.select(“#section1 > div”).

- ¿Qué hace el siguiente código?
```
d3.selectAll("div")

  .attr("class", "red box")

  .each(function(d, i) {

    d3.select(this).append("h1").text(i);

  });
```
  - Selecciona todos los elementos div, les asigna la clase red box y añade un encabezado h1 con el índice de cada elemento.



# Tema 4. D3.js. Datos, SVG y gráficas

1. ¿Podemos utilizar clases CSS en SVG?
- A. Sí. => **CORRECTO**
- B. No, no son compatibles con HTML.
- C. No, no son necesarias.
- D. No, porque D3 no incorpora clases CSS.

2. Si queremos dibujar una elipse, ¿debemos utilizar el SVG elemento de e indicar que el radio es variante?
- A. Sí.
- B. No, requiere el elemento y cuatro parámetros: cx, cy, rx, ry. => **CORRECTO**
- C. No, requiere el elemento y dos parámetros: cx, cy.
- D. No, requiere el elemento y tres parámetros: cx, cy, r.

3. Para dibujar una línea debemos definir los puntos de partida y de fin, y qué tipo de línea queremos que les una:
- A. Sí. => **CORRECTO**
- B. No.
- C. No porque depende de si queremos líneas continuas o a trazos.
- D. No existen líneas en D3.

4. Si ponemos el valor de la altura en negativo cuando vamos a dibujar un rectángulo, ¿el rectángulo se dibujará hacia arriba?

- A. Sí, porque valores positivos apuntan hacia abajo y negativos hacia arriba.
- B. No. => **CORRECTO**
- C. Sí, porque las coordenadas empiezan en 0,0.
- D. Sí, porque las coordenadas tienen su origen en el margen superior izquierda


5. Cuando dibujamos con SVG, ¿qué diferencia hay entre cx y x?
- A. cx indica el centro del círculo y x indica el comienzo a dibujar, por ejemplo, en un rectángulo la esquina superior izquierda. => **CORRECTO**
- B. cx indica el comienzo a dibujar, por ejemplo, en un rectángulo la esquina superior izquierda, y x indica el centro del círculo.
- C. Ninguna.
- D. No existen el parámetro x

6. ¿Qué función hemos de utilizar para cargar un archivo CSV?
- d3.csv("nombre_archivo.csv", function(data) { ... })

7. ¿Qué función hemos de utilizar para cargar un archivo JSON?
- d3.json("nombre_archivo.json", function(data) { ... })

8. ¿Qué es lo que hace este código?
var dataset = [];
for (var i = 0; i < 50; i++) {
var newNumber = Math.random() * 30;
dataset.push(newNumber);
}
- A. Nos genera un array de 50 números del 0 al 30.
- B. Nos genera un array de 30 números del 0 al 50.
- C. Dibuja 50 números al azar. => **CORRECTO**
- D. Dibuja 30 números del 0 al 50


9. ¿Qué nos dibujará el siguiente código?
var dataset = [ 5, 10, 15, 20, 25 ];
svg.selectAll("rect")
.data(dataset)
.enter()
.append("rect")
.attr("x", function(d, i) {
return i * (w / dataset.length);
})
.attr("y", function(d) {
return h - d;
})
.attr("width", w / dataset.length - 1)
.attr("height", function(d) {
return d;
});
- A. Cinco barras con color gradiente azul con el texto encima de las barras.
- B. Diez barras con color gradiente azul con el texto encima de las barras.
- C. Cinco barras con la dirección invertida.
- D. Ninguna de las anteriores => **CORRECTO**

10. ¿Qué nos dibujará el siguiente código?
var dataset = [
[5, 20], [480, 90], [250, 50], [100, 33], [330, 95],
[410, 12], [475, 44], [25, 67], [85, 21], [220, 88]
]
svg.selectAll("circle")
.data(dataset)
.enter()
.append("circle")
.attr("cx", function(d) {
return d[0];
})
.attr("cy", function(d) {
return d[1];
})
.attr("r", 5);
- A. Diez círculos con radio 5 en posición random en nuestro SVG. => **CORRECTO**
- B. Nueve círculos con radio 5 en posición definida por el dataset.
- C. Una gráfica Scatter Plot con diez barras definidas por el dataset.
- D. Ninguna de las anteriores


## Videoclase 1. Manejo de estructuras de datos en D3.js 

- ¿Cuál de las siguientes afirmaciones sobre SVG es incorrecta en el contexto de D3.js?
  - Los elementos SVG son estáticos y no pueden ser manipulados con JavaScript.

- Considerando el código CSV proporcionado, ¿qué función cumple la línea d3.select(“body”).append(“p”).text(d.Comida + ” ” + d.Preferencia);?
  -  Crea un elemento HTML para cada fila del CSV y muestra el nombre de la comida y su preferencia.

- ¿Cuál es la principal diferencia entre trabajar con datos en formato CSV y JSON en D3.js?
  - La estructura de los datos es diferente, CSV utiliza comas para separar valores y JSON utiliza llaves y corchetes.

- ¿Cuál de las siguientes funciones de D3.js se utiliza típicamente para crear un gráfico de barras?
  - d3.rect().

- Imagina que quieres crear un gráfico de dispersión donde cada punto represente una ciudad y su temperatura promedio. ¿Qué propiedades de los objetos JSON serían más relevantes para esta visualización?
  - Latitude, longitude y temperature.

## Videoclase 2. Creación de gráficos vectoriales escalables

- ¿Cuál de las siguientes afirmaciones sobre SVG es correcta?
  - SVG es un formato vectorial que permite crear gráficos escalables y altamente personalizables. => SVG es un formato vectorial, lo que significa que los gráficos pueden ser escalados sin pérdida de calidad. Además, ofrece una gran flexibilidad para crear gráficos interactivos y personalizados.

- ¿Qué representan las coordenadas cx y cy en un elemento <circle> de SVG?
  - Las coordenadas del centro del círculo. => Cx y cy especifican las coordenadas X e Y del centro del círculo, respectivamente.

- ¿Cuál es la principal ventaja de utilizar SVG sobre otros formatos de imagen para crear gráficos web?
  - Todas las anteriores.

- ¿Cómo se puede lograr un efecto de superposición entre diferentes elementos SVG?
  - Cambiando el orden en que se declaran los elementos.

- ¿Cuál es la función de la propiedad stroke-width en un elemento SVG?
  - Define el ancho del borde del elemento => Stroke-width especifica el ancho de la línea que rodea el elemento, es decir, el grosor del borde.

## Videoclase 3. Construcción de gráficas interactivas con D3.js

- ¿Qué propiedad en CSS asegura que las barras en un gráfico de barras creado con div se alineen horizontalmente?
  - display: inline-block

- ¿Cuál es el propósito principal de la función .style(“height”, function(d) { return d + “px”; }) en un gráfico de barras creado con D3.js?
  - Ajustar dinámicamente la altura de las barras según los datos.

- Al crear un gráfico de barras con SVG, ¿qué cambio en el atributo y asegura que las barras se dibujen desde el fondo hacia arriba?
  - y: h - d.

- ¿Qué propiedad define la posición horizontal de cada barra en un gráfico de barras utilizando SVG?
  - .attr(“x”, function(d, i) { return i * (w / dataset.length); }).

- En un Scatter Plot, ¿qué atributo determina el radio de los círculos que representan los puntos?
  - r.

# Tema 5. D3.js. Escalando y dibujando ejes de un gráfico


1. ¿Qué es el input domain?
  - A. Es el rango de valores que nos da nuestra fuente de datos. => **Correcto**
  - B. Es el dominio de datos que utilizamos para definir el título de una gráfica.
  - C. Es el rango de valores que definimos para nuestra escala.
  - D. Ninguna de las anteriores.

2. ¿Qué es el output range?
  - A. Es la leyenda de nuestra gráfica.
  - B. Es la escala que utilizaremos en nuestra gráfica.
  - C. Es el rango de valores que nos da nuestra fuente de datos.
  - D. Ninguna de las anteriores => **Correcto**

3. ¿Cuál es el resultado al ejecutar estas sentencias? var scale = d3.scale.linear(); scale(20)
  - A. 20. => **Correcto** Con Dudas 
  - B. 2.
  - C. 0,2.
  - D. 0,02

4. ¿Cuál es el resultado al ejecutar este código? var scale = d3.scale.linear()
.domain([100, 500])
.range([10, 350]);
scale (100);

  - A. 100.
  - B. 10 => **Correcto**
  - C. 500
  - D. 350


5. ¿Cuál es el resultado al ejecutar este código?
var dataset = [
[5, 20], [480, 90], [250, 50], [100, 33], [330, 95],
[410, 12], [475, 44], [25, 67], [85, 21], [220, 88]
];
d3.max(dataset, function(d) {
return d[0]; //References first value in each sub-array
});
  - A. 480. => **Correcto**
  - B. 495.
  - C. 95.
  - D. 12


6. ¿Cuál es el resultado al ejecutar este código?
  var dataset = [
  [5, 20], [480, 90], [250, 50], [100, 33], [330, 95],
  [410, 12], [475, 44], [25, 67], [85, 21], [220, 88]
  ];
  d3.max(dataset, function(d) {
  return d[1]; //References first value in each sub-array
  });
  - A. 480.
  - B. 495.
  - C. 95. => **Correcto**
  - D. 12.

7. ¿Qué es lo que hace "left" en el siguiente código?
var yAxis = d3.svg.axis()
.scale(yScale)
.orient("left")
.ticks(5);

  - A. Orienta el eje a la izquierda del eje Y.
  - B. Orienta los números del eje a la izquierda de la escala. => **Correcto**
  - C. Orienta el eje a la izquierda del gráfico.
  - D. Orienta los números del eje a la izquierda

8. ¿Qué es lo que hace este código?
  var xAxis = d3.svg.axis()
  .scale(xScale)
  .orient("bottom")
  .ticks(5); //Set rough # of ticks
  - A. Crea cinco divisiones en el eje X. => **Correcto**
  - B. Crea seis divisiones en el eje X porque empiezan a contar desde 0.
  - C. Crea cinco divisiones aplicándolos a la escala.
  - D. Ninguna de las anteriores.


9. ¿Qué es lo que hace este código?
svg.append("g")
.attr("class", "axis")
.call(xAxis);

  - A. Asignar el atributo axis al elemento class.
  - B. Asignar el atributo axis al elemento xAxis.
  - C. Asignar el atributo class al elemento axis.
  - D. Asignar el atributo class al elemento g => **Correcto**

10. ¿Qué nos dibujará el siguiente código?
var yAxis = d3.svg.axis()
.scale(yScale)
.orient("left")
.ticks(5);
svg.append("g")
.attr("class", "axis")
.attr("transform", "translate(" + padding + ",0)")
.call(yAxis);
  
  - A. Un gráfica tipo scatter plot.
  - B. Los ejes X e Y de la gráfica.
  - C. Un gráfica con el eje Y.
  - D. El eje Y con las etiquetas orientadas a la izquierda => **Correcto** 

## ◄ Videoclase 1. Uso de escalas numéricas en D3.js

- ¿Qué describe mejor la funcionalidad de las escalas en D3.js?
  - Una forma de conectar un dominio de entrada con un rango de salida.

- En el siguiente código de D3.js, ¿qué representa el argumento de la función d3.max()? d3.max(dataset, function(d) { return d[1]; });
  - El valor máximo del segundo elemento en cada sub-array del dataset.

- ¿Por qué el rango del eje Y se define de la forma range([h, 0]) en lugar de [0, h]?
  - Para invertir el orden de los valores y alinear con las coordenadas del SVG.

- ¿Qué resultado se espera al ejecutar el siguiente código en D3.js?

```JAVASCRIPT
var scale = d3.scale.linear()

              .domain([100, 500])

              .range([10, 350]);

scale(300);
``` 
- 180 



- ¿Cuál es la principal ventaja de usar d3.min() y d3.max() para definir el dominio de una escala?
  - Permite calcular automáticamente los valores mínimos y máximos del dominio basado en los datos.

## Videoclase 2. Creación y personalización de ejes en D3.js

- ¿Cómo se puede mover el eje X al borde inferior del gráfico?
```JAVASCRIPT
var padding = 30;

var xAxis = d3.svg.axis()

              .scale(xScale)

              .orient("bottom");

 

svg.append("g")

   .attr("class", "axis")

   .call(xAxis);
```
  - Añadiendo .attr(“transform”, “translate(0,” + (h - padding) + “)”). => ajusta la posición del grupo () que contiene el eje, moviéndolo hacia abajo mediante la transformación en el eje Y.



- ¿Qué propiedad del eje se debe ajustar para limitar el número de divisiones visibles?
```JAVASCRIPT
var xAxis = d3.svg.axis()

              .scale(xScale)

              .orient("bottom")
```
  - .ticks(5). => La propiedad .ticks[n] define el número aproximado de divisiones visibles en el eje, en este caso 5.



- ¿Cómo se pueden aplicar estilos personalizados al eje utilizando CSS?
```JAVASCRIPT
svg.append("g")

   .attr("class", "axis") // Clase que será utilizada en el CSS

   .call(xAxis);
```
  - Definiendo la clase CSS .axis con propiedades específicas para SVG, como stroke

- ¿Qué función mueve el eje Y hacia el borde izquierdo del gráfico?
```JAVASCRIPT
var padding = 30;

var yAxis = d3.svg.axis()

              .scale(yScale)

              .orient("left");

 

svg.append("g")

   .attr("class", "axis")

   .call(yAxis);
  
  .attr(“transform”, “translate(” + padding + “,0)”). => La transformación .attr(“transform”, “translate(” + padding + “,0)”) 
```
  - mueve el grupo que contiene el eje Y hacia la derecha por un valor definido por padding, posicionándolo correctamente.

- ¿Cuál sería el resultado de aplicar el siguiente CSS al eje? 
```CSS
.axis path,

.axis line {

  fill: none;

  stroke: black;

  stroke-width: 2;

  shape-rendering: crispEdges;

}

 

.axis text {

  font-family: sans-serif;

  font-size: 11px;

}

 

JavaScript:

svg.append("g")

   .attr("class", "axis")

   .call(xAxis);
```
  - Las líneas del eje serán negras, de 2 píxeles de grosor y el texto será sans-serif de 11px.

## ◄ Videoclase 3. Implementación de escalas ordinales en D3.js

- ¿Cuál es la principal diferencia entre una escala lineal y una escala ordinal en D3? 
  - Las escalas ordinales dividen los datos en bandas discretas, mientras que las lineales utilizan valores continuos.

- ¿Qué hace el parámetro 0.05 en .rangeRoundBands([0, w], 0.05)?
  - Establece el espacio entre las bandas para una separación visual clara.

- Dado el siguiente código: .attr(“width”, xScale.rangeBand()), ¿qué propósito tiene el uso de xScale.rangeBand()?
  - Define el ancho constante de las barras basado en el rango de la escala ordinal.

- Si eliminas el parámetro 0.05 de .rangeRoundBands([0, w], 0.05), ¿qué ocurre?
  - Las barras ocuparán el rango total sin espacio entre ellas.

- ¿Qué logra el siguiente código al trabajar con una escala ordinal? .domain(d3.range(dataset.length))
  - Genera un dominio discreto con índices numéricos para cada elemento del dataset.

# Tema 06. Force Layout, transiciones, movimiento e interacción

1. ¿Cuánto tardará la transición en este código?
```javascript
svg.selectAll("text")
.data(dataset)
.text(function(d) {
return d;
})
.attr("x", function(d, i) {
return xScale(i) + xScale.rangeBand() / 2;
})
.attr("y", function(d) {
return h - yScale(d) + 14;
});
```
A. 1 seg.
B. 2 seg.
C. Depende del número de barras del gráfico.
D. No hay transición => **CORRECTO**


2. ¿Cuánto tardará la transición en este código?
```javascript
svg.selectAll("text")
.data(dataset)
.text(function(d) {
return d;
})
.transition()
.delay(1000)
.attr("x", function(d, i) {
return xScale(i) + xScale.rangeBand() / 2;
})
.attr("y", function(d) {
return h - yScale(d) + 14;
});
```
A. 1 seg. => **CORRECTO**
B. 2 seg.
C. Depende del número de barras del gráfico.
D. El tiempo por defecto transición


3. ¿Es la sintaxis correcta?

```javascript
on("mouseover", function(d) {
d3.select(this)
.style("fill", "red");
})
```
A. Sí. => **CORRECTO**
B. No, porque falta la selección del objeto.
C. No, porque el evento mouseover no existe.
D. No, porque la llamada a la función es incorrecta


4. ¿Es la sintaxis correcta?
```javascript
on("outmouse", function(d) {
d3.select(this)
.style("fill", "red");
})
```
  - A. Sí. 
  - B. No, porque falta la selección del objeto.
  - C. No, porque el evento outmouse no existe. => **CORRECTO**
  - D. No, porque la llamada a la función es incorrecta


5. ¿Podemos escuchar eventos en los elementos p de D3?
  - A. Sí. => **CORRECTO**
  - B. No, porque hacen falta objetos que puedan aceptar un clic de ratón sobre ellos.
  - C. No, porque los eventos aplican solo a los datos.
  - D. No, porque p no es un elemento de D3


6. ¿Podemos escuchar/generar eventos en los elementos de D3?
  - A. Sí. => **CORRECTO**
  - B. No, porque hacen falta objetos que puedan aceptar un clic de ratón sobre ellos.
  - C. No, porque los eventos aplican solo a los datos.
  - D. No, porque rect no es un elemento de D3


7. ¿Qué conseguimos cuando utilizamos en la transición la función ?
  - A. Que la transición sea constante. => **CORRECTO**
  - B. Que la transición dure lo mínimo posible.
  - C. Que la transición de los objetos sea vertical.
  - D. Que la transición de los objetos sea horizontal.

8. Si queremos exportar nuestra visualización a un archivo svg, tenemos que:
  - A. Exportar nuestro gráfico con la función D3.exportSVG.
  - B. Copiar el código HTML generado y copiarlo en un archivo svg. => **CORRECTO**
  - C. No existe la posibilidad. Se pueden crear y visualizar gráficos SVG pero no exportarlos.
  - D. Ninguna de las anteriores.

9. Utilizando captura de pantalla para exportar nuestra visualización a otro formato:
  - A. Generamos un archivo Bitmaps. => **CORRECTO**
  - B. Generamos un archivo SVG.
  - C. Generamos un archivo PDF.
  - D. No es posible capturar la pantalla.

10. ¿Cuál es el comportamiento al aplicar la función ?
  - A. Los nodos se pueden arrastrar y, cuando sueltas el nodo, este se queda en esa misma posición.
  - B. Los nodos se pueden arrastrar y, cuando sueltas el nodo, vuelven a su posición original.
  - C. Los nodos se mueven de forma independiente por sí mismos en un ciclo continuo.
  - D. Ninguna de las anteriores => **CORRECTO**
--- 
## Videoclase 1. Introducción a Force Layout


- En el código de Force-Directed Graph proporcionado, ¿cuál es la función del siguiente fragmento?
```javascript
var force = d3.layout.force()

    .charge(-120)

    .linkDistance(30)

    .size([width, height])

    .nodes(data.nodes)

    .links(data.links)

    .start();
```
  - Establecer la distancia entre los nodos y la fuerza de repulsión.


- ¿Qué realiza el siguiente fragmento de código en el contexto del Force-Directed Graph?
```javascript
force.on("tick", function() {

    link.attr("x1", function(d) { return d.source.x; })

        .attr("y1", function(d) { return d.source.y; })

        .attr("x2", function(d) { return d.target.x; })

        .attr("y2", function(d) { return d.target.y; });

    node.attr("cx", function(d) { return d.x; })

        .attr("cy", function(d) { return d.y; });

});
```

  - Actualizar las posiciones de los nodos y enlaces en cada paso de la simulación. => Este fragmento se ejecuta en cada “tick” de la simulación, actualizando las posiciones de los nodos y enlaces, lo que permite que el grafo se mueva dinámicamente.


- ¿Qué efecto tiene la siguiente línea de código en la visualización de D3?  
```javascript
node.call(force.drag);
```
  - Permite que los nodos sean arrastrados por el usuario. => La línea node.call(force.drag) permite que los nodos sean arrastrados por el usuario en la visualización. Esto habilita la interacción en tiempo real con los nodos.

- ¿Qué tipo de datos se encuentran en el archivo stations_graph.json utilizado en el código?
```javascript
d3.json("stations_graph.json", function(json) {

    visualizeLayout(json);

});
```
  - Nodos y enlaces que representan paradas de metro y sus conexiones => El archivo stations_graph.json contiene información sobre los nodos (paradas de metro) y los enlaces (conexiones entre las paradas), lo que permite construir un grafo con las relaciones entre estas estaciones.


- En el código del Force-Directed Graph, ¿qué efecto tiene la línea charge(-120)?
```javascript
var force = d3.layout.force()

    .charge(-120)

    .linkDistance(30)

    .size([width, height])

    .nodes(data.nodes)

    .links(data.links)

    .start();
```
  - Controlar la fuerza de repulsión entre los nodos. => El parámetro .charge(-120) establece la fuerza de repulsión entre los nodos. Un valor negativo indica que los nodos se repelen entre sí, lo que contribuye a la distribución equilibrada de los nodos en el grafo.

## Videoclase 2. Actualización dinámica de gráficos en D3.js según eventos 

- ¿Qué elemento en D3.js permite añadir interactividad a un gráfico, como un evento de clic?
  - .on(“click”, function() {…}). => En D3.js, los eventos como un clic se gestionan mediante el método .on(). Específicamente, el código .on(“click”, function() {…}) es el que permite ejecutar una función cuando se hace clic en un elemento

- ¿Qué función se usa en D3 para animar una transición, permitiendo que un cambio en las propiedades de un gráfico se realice de manera suave?
  - .transition().  => La función .transition() en D3 permite animar los cambios en las propiedades de los elementos, aplicando un cambio gradual en lugar de inmediato. Esto se utiliza para hacer que el gráfico se mueva o cambie suavemente.

- ¿Cómo puedes actualizar la altura de las barras en un gráfico de barras al actualizar el dataset en D3.js?
  - Utilizando .attr(“height”, function(d) {…}). => Para actualizar la altura de las barras en D3.js, se utiliza el método .attr(“height”, function(d) {…}). Este método ajusta el atributo height de cada rectángulo (barra) en función de los datos. 

- ¿Qué método en D3.js se utiliza para definir la duración de una transición en milisegundos?
  - .duration() => El método .duration() se usa en D3.js para especificar la duración de una transición en milisegundos. Por ejemplo, .duration(3000) hace que la transición dure 3 segundos.

- ¿Qué ocurre si se aplica una transición solo a los rectángulos (rect) de un gráfico, pero no a los textos (text) asociados en D3.js?
  - Los rectángulos se moverán suavemente, pero el texto permanecerá fijo => Si no se aplica la transición al texto, los rectángulos se moverán suavemente mientras el texto se queda en su lugar. Esto puede causar una descoordinación visual en la animación si no se trata adecuadamente.

## Videoclase 3. Transiciones y animaciones en D3.js

-  ¿Qué sucede cuando se hace clic en una barra dentro del gráfico creado con D3.js utilizando el siguiente código?
```javascript
svg.selectAll("rect")

  .data(dataset)

  .on("click", function(d) {

     alert(d);

  })

  .transition()

   .ease("linear")

 .attr("y", function(d) {

     return h - yScale(d);

  })

  .attr("height", function(d) {

     return yScale(d);

  });
```
  - Se muestra el valor asociado a la barra en una ventana emergente.

- ¿Qué ocurre cuando se pasa el ratón sobre una barra dentro del gráfico con el siguiente código?

```javascript
svg.selectAll("rect")

  .data(dataset)

  .on("mouseover", function(d) {

    d3.select(this)

      .style("fill", "red");

  })

  .on("mouseout", function(){

    d3.select(this)

      .style("fill", function(d) {

         return "rgb(0, 0, " + (d * 10) + ")";

      });

  });
```
  - La barra cambia a color rojo cuando el ratón pasa por encima y vuelve a su color original al quitar el ratón.

- ¿Cuál es la principal ventaja de exportar un gráfico como SVG en lugar de usar una captura de pantalla (Bitmap)?
  - Los archivos SVG pueden modificarse y escalarse sin pérdida de calidad.

- ¿Cómo se puede exportar un gráfico de D3.js a formato PDF desde el navegador?
  - Utilizando el atajo de teclado “Ctrl + P” y eligiendo la opción de imprimir en formato PDF.

- ¿Qué método se recomienda para exportar un gráfico en D3.js a un archivo SVG para edición posterior?
  - Inspeccionando el elemento y copiando el contenido entre las etiquetas <svg>…</svg>.

# Tema 07. Power BI

1. Power BI es una herramienta que permite la visualización de datos:
- A. Correcto. No incorpora capacidades para el tratamiento y transformación de los datos.
- B. Incorrecto. Solo la versión Desktop permite la visualización de datos.
- C. Incorrecto. Solo la versión SaaS permite la visualización de datos.
- D. Correcto. Adicionalmente incorpora capacidades avanzadas para el tratamiento y transformación de los datos. => **Correcto**

2. Power BI permite el intercambio rápido entre la visualización de datos y la visualización de gráficas:
- A. Correcto. Desde el menú lateral izquierdo es posible intercambiar dichas vistas. => **Correcto**
- B. Correcto. Pulsando F5.
- C. Incorrecto. Una vez cargados los datos, ya solo nos movemos en su visualización.
- D. Incorrecto. Existe la opción de carga de datos y visualización posterior en modo gráfica. La visualización de los datos no es necesaria en el 80 % de las
ocasiones.

3. ¿Dónde se ubican las opciones de Filtros, Visualizaciones y Campos?
- A. En el menú lateral derecho. => **Correcto**
- B. No existe el menú de Filtros.
- C. No existe el menú de Visualizaciones.
- D. No existe el menú de Campos

4. ¿Qué fases ordenadas incorpora un proyecto de análisis y visualización de datos?
- A. Preparación – Obtención - Modelado – Visualización – Reporte de datos.
- B. Obtención – Modelado – Preparación – Modelado – Visualización – Reporte de datos.
- C. Obtención – Preparación – Modelado – Visualización – Reporte de datos. => **Correcto**
- D. Obtención – Visualización de datos.


5. El gestor de datos integrado de Power BI:
- A. Permite limpiar datos.
- B. Permite tratar los datos.
- C. Se denomina Query Manager.
- D. Todas las respuestas son correctas. => **Correcto**


6. Los filtros dinámicos de Power BI nos permiten seleccionar el rango deseado de datos, tanto desde el apartado Filtros como incorporando una visualización de Segmentación de Datos:
- A. Correcto. => **Correcto**
- B. Incorrecto. No existe la visualización Segmentación de Datos.
- C. Incorrecto. La visualización Segmentación de Datos no tiene esa finalidad.
- D. Incorrecto. El apartado Filtros sirve para escoger el tipo de gráfica deseada


7. En el momento de cargar los datos es posible editarlos antes de proceder a su visualización:
- A. Correcto. En este momento podemos utilizar la opción editar para hacer los cambios de formato que sean necesarios. => **Correcto**
- B. Correcto. Sin embargo, si modificamos los datos debemos guardarlos y volver a cargarlos para que recoja todas las modificaciones.
- C. Incorrecto. Power BI no incorpora dicha funcionalidad.
- D. Incorrecto. Power BI permite la edición de datos pero no antes de analizarlos visualmente.


8. Las visualizaciones tipo Mapa requiere la presencia de coordenadas en los datos:
- A. Correcto. No existe otra manera de hacerlo.
- B. No es necesario, porque el servicio de mapas de Power BI también es capaz de interpretar localidades en formato texto. => **Correcto**
- C. No es necesario, porque basta con indicárselo en los Filtros.
- D. Correcto. Las coordenadas GIS deben estar presentes en el dataset.


9. La gráfica tipo Funnel solo se aplica si los datos de los diferentes niveles tienen un orden decreciente formando un embudo:
- A. Incorrecto. El orden de los datos no es relevante y se pueden aplicar diferentes criterios para ordenarlos. => **Correcto**
- B. Incorrecto. Tienen que estar ordenados de forma creciente para forma el embudo.
- C. Correcto. Debes estar ordenados decrecientemente.
- D. Correcto. El embudo solo muestra datos que representen variaciones entre ellos


10. Los campos de los ejes y de los valores son definidos automáticamente por Power BI:
- A. Correcto. Así nos facilita la experiencia como usuarios.
- B. Incorrecto. Son definidos por el usuario. => **Correcto**
- C. Correcto y no se pueden modificar.
- D. Ninguna de las anteriores

--- 
## ◄ Videoclase 1. Conceptos básicos y configuración inicial

- ¿Qué característica de Power BI lo hace destacar en el análisis de datos empresariales según el cuadrante mágico de Gartner?
- Su capacidad para integrar múltiples fuentes de datos y generar visualizaciones interactivas.

- ¿Cuál es la opción de Power BI que permite el análisis personal gratuito sin necesidad de conexión a la nube?
- Power BI Desktop.

- ¿Cuál es la función principal del menú lateral izquierdo en Power BI?
- Acceder a diferentes vistas de los informes

- ¿Qué se puede hacer en el menú lateral derecho de Power BI?
- Aplicar filtros y seleccionar los campos para la visualización.

- ¿Cuál es una de las principales ventajas que ofrece Power BI en cuanto a su interfaz y facilidad de uso?
- Su interfaz es intuitiva y fácil de usar, incluso sin conocimientos técnicos avanzados.

## ◄ Videoclase 2. Obtención, transformación y modelado de datos

- ¿Cuál de las siguientes es una de las funciones principales de Power BI en el proceso de análisis de datos?
- Modelar datos para crear una estructura que facilite su posterior visualización. => En Power BI, una de las funciones clave es modelar los datos. Esto implica relacionar datos de diferentes fuentes y ajustarlos para facilitar su visualización, lo que ayuda a obtener información relevante para la toma de decisiones

- ¿Qué acción realiza el Query Manager de Power BI durante la preparación de los datos?
- Realiza transformaciones y limpia los datos => El Query Manager es una herramienta integrada en Power BI que permite realizar transformaciones sobre los datos, como eliminar columnas, cambiar formatos de campos o reemplazar valores, lo cual es esencial para preparar los datos antes de analizarlos o visualizarlos.

- ¿Qué herramienta de Power BI se utiliza para transformar y preparar los datos después de su importación?
- Query Manager. => El Query Manager es la herramienta integrada en Power BI que permite realizar transformaciones y preparaciones de los datos, como eliminar columnas o cambiar el formato de los campos, antes de su visualización o análisis. Esta es la funcionalidad que se usa durante el proceso de preparación de datos en Power BI.

- ¿Cuál es el propósito de la función “Obtener datos” en Power BI?
- Cargar datos desde diferentes fuentes como archivos, bases de datos o servicios en línea. => La función obtener datos de Power BI permite cargar información desde diversas fuentes, como archivos de Excel; bases de datos, como SQL Server, o servicios en línea, como Google Analytics, lo que facilita el análisis de datos integrados desde múltiples orígenes.

- ¿Qué opción se utiliza en Power BI para eliminar columnas o realizar otras transformaciones en los datos antes de cargarlos en el modelo?
- Query Manager => El Query Manager en Power BI es la herramienta que permite realizar transformaciones avanzadas sobre los datos, como eliminar columnas, cambiar formatos o reemplazar valores. Es esencial para preparar los datos antes de proceder con su modelado y visualización.

## ◄ Videoclase 3. Análisis y creación de visualizaciones

- ¿En Power BI, al crear una visualización y no seleccionar un tipo específico, ¿qué tipo de visualización se aplica por defecto?
- Tabla de datos. => Cuando no se selecciona un tipo específico de visualización en Power BI, por defecto se crea una tabla de datos. Esta visualización permite ver los datos en formato tabular sin ningún gráfico adicional.

- ¿Cuál es la herramienta en Power BI que permite aplicar filtros a los datos basados en campos específicos?
- La segmentación de datos =>  Power BI es una herramienta que permite activar filtros en campos específicos para segmentar y analizar subconjuntos de datos de manera eficiente.

- ¿Qué tipo de gráfico sería más adecuado para visualizar la evolución de un valor a lo largo del tiempo en Power BI?
- El gráfico de áreas =>  es ideal para mostrar cómo cambia un valor a lo largo del tiempo, permitiendo comparar la evolución de varias variables.

- ¿Qué debes hacer si un valor erróneo aparece en una visualización de Power BI debido a datos incorrectos?
- Excluir el valor erróneo haciendo clic sobre él y seleccionando «Excluir». => Si un valor erróneo aparece en una visualización, puedes excluirlo directamente desde el gráfico, lo que permite mantener la integridad de los datos mostrados sin modificar el dataset original.

- ¿Por qué sería útil aplicar un filtro para eliminar datos incompletos o erróneos en un análisis de Power BI?
- Para asegurar que el análisis se base sólo en datos completos y confiables. => Aplicar un filtro para eliminar datos incompletos o erróneos ayuda a garantizar la precisión de los resultados del análisis, asegurando que solo se utilicen datos completos y confiables.


# Tema 08. Qlik


1. Qlik Sense es una plataforma:
- A. Orientada a datos.
- B. Orientada a la visualización.
- C. Orientada al descubrimiento de la información.
- D. Todas las respuestas son válidas. => **Correcto**


2. Qlik integra directamente los datos:
- A. En una visualización.
- B. En la app. => **Correcto**
- C. En una fuente de datos.
- D. En un fichero de datos.

3. Qlik Datamarket es:
- A. Un repositorio de datos, con datasets tanto de uso libre como de pago. => **Correcto**
- B. Un mercado disponible para los usuarios que desean adquirir gráficas predefinidas.
- C. Un entorno abierto en el que los usuarios pueden compartir datasets.
- D. Todas las respuestas son válidas.

4. Una dimensión en Qlik es:
- A. Un gráfico.
- B. Un cálculo.
- C. La característica del dato. => **Correcto**
- D. Una tabla

5. Una medida en Qlik es:
- A. Un cálculo. => **Correcto**
- B. Un gráfico.
- C. La característica del dato. 
- D. Una tabla.


6. Cuando distribuimos los datos a lo largo del tiempo, estamos definiendo:
- A. La dimensión de la gráfica. => **Correcto**
- B. La medida de la gráfica.
- C. Un filtro de selección.
- D. Ninguna de las opciones es correcta.

7. El gestor de datos nos permite:
- A. Ver la estructura de las tablas y las relaciones existentes entre ellas. => **Correcto**
- B. Modificar la estructura de las tablas en el dataset de origen
- C. Trabajar con las tablas, pero sin modificar las relaciones.
- D. Gestionar los datos de la cuenta en Qlik Sense.

8. Las tablas pivotantes nos permiten:
- A. Analizar datos por múltiples medidas.
- B. Presentar dimensiones y medidas como filas y columnas de una tabla.
- C. Analizar datos por múltiples dimensiones.
- D. Todas las respuestas son válidas. => **Correcto**

9. Las historias de Qlik es el equivalente a:
- A. Un dashboard. => **Correcto**
- B. Una gráfica.
- C. Una captura de pantalla.
- D. Todas las respuestas anteriores son correctas.

10. Un marcador permite:
- A. Recordar una dimensión que nos ha resultado útil.
- B. Almacenar el resultado de aplicar un filtro. => **Correcto**
- C. Aplicar una medida de forma rápida.
- D. Ninguna de las anteriores


--- 
## Videoclase 1. Introducción a Qlik Sense: funcionalidades y entorno

- ¿Qué diferencia principal existe entre las versiones de Qlik Sense Business y Enterprise?
- La versión Business tiene un número limitado de espacios y capacidades de integración con API => La versión Business está orientada a pequeñas y medianas empresas con limitaciones en integración con API, número de espacios y otras funcionalidades avanzadas que están disponibles solo en la versión Enterprise

- ¿Cuál de las siguientes opciones es una acción inicial que se realiza al crear una nueva app en Qlik Sense?
- Seleccionar un conjunto de datos a través de los conectores de Qlik. => Al crear una nueva app, lo primero que se hace es seleccionar los datos que se utilizarán para crear las visualizaciones, ya sea desde un archivo local o utilizando fuentes de datos externas a través de los conectores de Qlik.

- ¿Qué funcionalidad permite a los usuarios de Qlik Sense crear filtros dinámicos en sus visualizaciones?
- El panel de filtrado. => El Panel de filtrado permite a los usuarios arrastrar y aplicar filtros de dimensiones a sus gráficos de forma dinámica, facilitando la personalización de las visualizaciones.

- ¿Qué es lo que define una dimensión en Qlik Sense al crear gráficos?
- La forma de agrupar los datos en el gráfico => En Qlik Sense, una dimensión es la característica del dato que ayuda a determinar cómo agrupar los datos en una visualización, como país, año o producto.

- En Qlik Sense, ¿qué sucede cuando se hace clic en la opción «Cargar datos» al agregar un nuevo dataset a una app?
- Los datos se cargan y se presentan en un modelo de datos estructurado. => Al hacer clic en «Cargar datos», Qlik Sense organiza y presenta los datos cargados en un modelo de datos estructurado, mostrando las relaciones entre las tablas y cómo se pueden utilizar en las visualizaciones.

## Videoclase 2. Exploración de los datos, filtros y tablas pivotantes

- ¿Cuál es el propósito principal de utilizar filtros en una visualización de datos?
- Ajustar los datos visualizados según ciertas dimensiones o criterios => Los filtros permiten ajustar los datos visibles en una visualización según dimensiones o criterios específicos, facilitando así el análisis enfocado.

- ¿Cuál es la principal utilidad de una tabla pivotante en la exploración de datos?
- Analizar datos desglosados por diferentes dimensiones y detectar inconsistencias. => Las tablas pivotantes permiten desglosar los datos por dimensiones y examinar más a fondo los resultados, ayudando a identificar posibles inconsistencias o valores erróneos.

- ¿Qué función tienen los marcadores en la herramienta de visualización de datos?
- Almacenar configuraciones de filtros para aplicarlos fácilmente más tarde. => Los marcadores permiten guardar configuraciones de filtros aplicados previamente, lo que facilita aplicar las mismas configuraciones de filtro en futuras sesiones.

- Qué función tiene la opción de etiquetas en las visualizaciones de datos?
- Cambiar el nombre de los campos en los ejes para hacerlos más comprensibles => La opción de etiquetas permite personalizar los nombres de los campos en los ejes, mejorando la comprensión de la visualización al usar términos más explicativos.

- ¿Qué ocurre cuando se selecciona la opción «Por dimensión» al modificar los colores en una gráfica?
- Se asigna un color único a cada categoría o dimensión. => La opción «Por dimensión» asigna un color único a cada categoría o dimensión, lo que facilita la diferenciación visual de los elementos en la gráfica.

## Videoclase 3. Creación de mapas geográficos y gráficos en Qlik Sense

- ¿Cuál es el propósito principal de utilizar mapas geográficos en las herramientas de visualización de datos?
- Representar la información de manera visual con datos asociados a la longitud y latitud. => Los mapas geográficos permiten asociar datos con ubicaciones específicas, utilizando coordenadas geográficas, lo que facilita la visualización de patrones y distribuciones geográficas.

- ¿Qué se debe hacer para cambiar el color de las áreas en un mapa geográfico?
- Seleccionar el campo de la población y elegir la opción de colores. => Cambiar el color de las áreas en un mapa generalmente se hace seleccionando una medida específica (como la población) y asignando colores en función de esa medida.

- ¿Qué tipo de dato es comúnmente utilizado para representar ubicaciones geográficas en un mapa?
- Códigos internacionales de países => Los códigos internacionales de países (como los definidos en ISO 3166) son utilizados para representar países en un mapa geográfico, permitiendo la visualización de datos por ubicación.

- ¿Qué función tienen las opciones de «Historias» en las herramientas de visualización de datos?
- Crear presentaciones interactivas que combinen texto, imágenes y gráficos. => Las historias permiten organizar los datos visualizados en una presentación dinámica, donde se combinan gráficos, texto y otros elementos visuales, como en una diapositiva interactiva.

- ¿Qué tipo de gráfico se utiliza para mostrar la relación entre dos variables, como la edad y el rendimiento en una actividad?
- Gráfico de dispersión => El gráfico de dispersión es ideal para mostrar la relación entre dos variables numéricas, como la edad y el rendimiento, permitiendo observar correlaciones o patrones en los datos.

# Tema 09. Tableau

1. Tableau es una herramienta que permite la visualización de datos:
- A. Correcto. Aunque no incorpora capacidades para el tratamiento y transformación de los datos.
- B. Incorrecto. Solo la versión Desktop permite la visualización de datos.
- C. Incorrecto. Solo la versión SaaS permite la visualización de datos.
- D. Correcto. Adicionalmente incorpora capacidades avanzadas para el tratamiento y transformación de los datos. => **Correcto** 

2. Tableau permite el intercambio rápido entre la visualización de datos y la visualización de gráficas:
- A. Correcto. Desde el menú inferior izquierdo es posible intercambiar dichas vistas. => **Correcto** 
- B. Correcto. Pulsando F5.
- C. Incorrecto. Una vez cargados los datos, ya solo nos movemos en su visualización.
- D. Incorrecto. Existe la opción de carga de datos y visualización posterior en
modo gráfica. La visualización de los datos no es necesaria en el 80 % de las
ocasiones.

3. ¿Dónde se ubican las opciones de asignación de colores y tamaños de los objetos gráficos?
- A. En el menú lateral izquierdo dentro del bloque de Marcas. => **Correcto** 
- B. No existen dichos menús.
- C. No existe el menú de asignación de tamaños.
- D. No existe el menú de asignación de colores

4. ¿Qué fases ordenadas incorpora un proyecto de análisis y visualización de datos?
- A. Preparación – Obtención - Modelado – Visualización – Reporte de datos.
- B. Obtención – Modelado – Preparación – Modelado – Visualización – Reporte de datos.
- C. Obtención – Preparación – Modelado – Visualización – Reporte de datos. => **Correcto** 
- D. Obtención – Visualización de datos.

5. Los campos de los ejes y de los valores son definidos automáticamente por Tableau:
- A. Correcto. Así nos facilita la experiencia como usuarios.
- B. Incorrecto. Son definidos por el usuario.
- C. Correcto y no se pueden modificar.
- D. Ninguna de las anteriores.

6. Las magnitudes principales que representan los ejes se definen:
- A. En la opción Detalle de la tarjeta Marcas.
- B. En los estantes de Filas y Columnas. => **Correcto** 
- C. En la opción Ejes de la tarjeta Marcas.
- D. Ninguna de las anteriores. Tableau selecciona las magnitudes oportunas en cada momento.

7. El tipo de visualización se puede modificar:
- A. En la tarjeta Páginas.
- B. En la tarjeta Marcas. => **Correcto** 
- C. En la opción Detalle de la tarjeta Marcas.
- D. Ninguna de las anteriores. Tableau autoselecciona el tipo de gráfica y no es modificable

8. En una gráfica de dispersión, el tamaño de los círculos de la gráfica será siempre proporcional al valor del dato que representa:
- A. Correcto.
- B. No necesariamente, salvo que depositemos en la opción Tamaño de la tarjeta Marcas el campo que queremos vincular al tamaño. => **Correcto** 
- C. No es una opción existente en Tableau.
- D. Incorrecto. No es posible modificar el tamaño de los elementos de una gráfica.

9. La opción de Descripción emergente permite definir el contenido de un tooltip.
- A. Incorrecto. Los tooltip son contenidos fijos no modificables.
- B. Correcto. Desde dicha opción podemos editar su contenido.
- C. Incorrecto. Los tooltip se pueden modificar pero haciendo clic en ellos.
- D. Incorrecto. Los tooltip se modifican pero desde la opción de dashboard.

10. La opción de Etiqueta permite definir el contenido de las etiquetas en los objetos de la visualización:
- A. Incorrecto. Las etiquetas son contenidos fijos no modificables.
- B. Correcto. Desde dicha opción podemos editar su contenido.
- C. Incorrecto. Las etiquetas se pueden modificar pero haciendo clic en ellas.
- D. Incorrecto. Las etiquetas se modifican pero desde la opción de dashboar


--- 
## Videoclase 1. Tableu: Introducción

- ¿Cuál es una de las principales razones por las que Tableau ocupa un lugar destacado en el cuadrante mágico de Gartner?
- Es altamente visual y ofrece análisis integral de datos. => Tableau se destaca por ser una herramienta de visualización de datos muy potente y visual, además de ofrecer capacidades avanzadas para análisis integral, lo que la posiciona como una solución líder en su categoría según Gartner.

- ¿Qué es VizQL y por qué es importante en Tableau?
- Es un lenguaje de consulta visual que permite transformar consultas en gráficos automáticamente

- ¿Cuál fue la contribución principal del sistema Polaris, desarrollado en Stanford, al software Tableau?
- Proporcionó una interfaz para explorar grandes bases de datos multidimensionales.

- ¿Cuál de las siguientes afirmaciones es correcta sobre el uso de Tableau?
- Tableau permite crear informes visualmente atractivos sin necesidad de programar.

- ¿Qué hecho marcó un cambio significativo en la historia de Tableau en 2019?
- La adquisición de Tableau por parte de Salesforce.

## Videoclase 2. Tableu: Instalación en interfaz

- ¿Cuál es una de las ventajas clave de Tableau Online en comparación con Tableau Server?
- Es una solución SaaS completamente hospedada en la nube, sin necesidad de configuración ni costos de hardware.

- ¿Qué función tiene el motor de datos de Tableau en el manejo de grandes volúmenes de información?
- Permite análisis ad hoc rápido de datos masivos, incluso en equipos de prestaciones normales.

- ¿Cuál es el propósito de los estantes de columnas y filas en la interfaz de Tableau?
- Organizar los datos dimensionales y numéricos para crear visualizaciones.

- ¿Qué función cumple el bloque de Filtros en la interfaz de Tableau?
- Definir qué datos incluir o excluir en las visualizaciones.

- ¿Cuál es una de las funcionalidades más destacadas del bloque de marcas en Tableau?
- Ofrece opciones intuitivas para estructurar, dar forma y enriquecer los datos visuales con elementos como color y etiquetas.

## Videoclase 3. Tableu: referencias de estantes y tarjetas
- ¿Qué sucede al arrastrar un campo al estante de columnas y otro al estante de filas en Tableau?
- Se crea un gráfico que muestra la relación entre los dos campos en el formato más adecuado. => Tableau utiliza los estantes de columnas y filas para organizar los datos y crear automáticamente un gráfico que represente la relación entre los campos. El tipo de gráfico se selecciona según el mejor formato para esos datos.

- ¿Cuál es la función principal de la opción color en la tarjeta marcas de Tableau?
- Diferenciar visualmente los datos según los valores de un campo. => La opción color en la tarjeta marcas permite distinguir los elementos de la visualización utilizando diferentes colores en función de los valores de los campos arrastrados, lo cual facilita la interpretación visual.

- ¿Qué efecto tiene la opción de tamaño en la tarjeta marcas?
- Modifica el tamaño de los objetos en función de los valores de un campo => La opción Tamaño permite modificar el tamaño de los elementos visuales, como barras o círculos, dependiendo de los valores asociados al campo seleccionado, destacando los datos más relevantes de manera proporcional..

- ¿Para qué se utiliza la opción detalle en la tarjeta marcas de Tableau?
- Para proporcionar información adicional sin alterar la estructura principal de la visualización. => La opción detalle permite incluir información adicional en la visualización sin modificar los estantes de columnas y filas, proporcionando niveles de detalle adicionales que enriquecen la representación gráfica.

- ¿Qué se logra al editar la descripción emergente en Tableau?
- Personalizar el texto que aparece al pasar el cursor sobre un gráfico. =>  La opción de descripción emergente permite personalizar los tooltips que aparecen cuando el usuario pasa el cursor sobre los elementos de la visualización. Esto ayuda a proporcionar información adicional o específica sobre los datos mostrados.

# Tema 10. 



--- 
## Videoclase 1. 

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

## Videoclase 1. 

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

## Videoclase 1. 

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
