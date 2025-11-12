# Herramientas de Visualización

## Tema 1. Introducción a las herramientas de visualización


Los datos y sus relaciones no son siempre algo fácil de entender. Mientras que
algunas personas pueden mirar una hoja de cálculo y encontrar instintivamente la
información que necesitan y sus relaciones dentro de una maraña de cifras, otras
necesitamos un poco de ayuda, y ahí es donde la visualización de datos puede ser la
solución.

> La visualización puede ayudarnos a tratar con información más compleja.

## 1.2. Librerías y herramientas de visualización

Se divide en dos tipos de herramientas 

> Herramientas para desarrolladores 

> Google Chart
Es la librería de visualizaciones utilizada por Google Spreadsheets, siendo la API de
gráficos de Google. Se trata de una potente y sencilla librería, con una gran variedad
de gráficos disponibles.


> D3.js
Es una librería de JavaScript que utiliza HTML, CSS y JavaScript para mostrar
algunos diagramas y gráficos sorprendentes de una variedad de fuentes de datos.

Esta librería, más que la mayoría, es capaz de algunas visualizaciones muy
avanzadas con complejos conjuntos de datos. D3 tiene una poderosa capacidad para
gestionar gráficos vectoriales en formato SVG (Scalable Vector Graphics).

> R
¿Cuántas otras herramientas tienen un motor de búsqueda completo
(https://rseek.org/) dedicado a ellas? R es un paquete estadístico enormemente
potente, utilizado para analizar grandes conjuntos de datos, aunque con una curva
de aprendizaje proporcional a sus elevadas capacidades. Esta librería requiere la
utilización de Python como lenguaje de programación.

Según la consultora de mercado Gartner, en la actualidad, las principales
plataformas modernas de analítica e inteligencia de negocio (Analytics and business
intelligence, ABI) ya no se diferencian por sus capacidades en la visualización
de datos. En su lugar, su diferenciación reside, por un lado, en cómo se integran con
el resto de las aplicaciones corporativas de analítica e informes y, por otro, en sus
capacidades aumentadas que les permiten acelerar las fases de preparación de los
datos y generación de conocimiento para el negocio.

--- 

> Herramientas para usuarios no desarrolladoress 


> Tableau
Repleto de gráficos, tablas y mapas, Tableau Public es una popular herramienta de
visualización de datos. Los usuarios pueden arrastrar y soltar fácilmente los datos en
el sistema y ver cómo se actualizan en tiempo real.

> PowerBI
Es la propuesta de Microsoft que nos permite conectar diferentes orígenes de datos,
transformarlos, limpiarlos, relacionarlos y visualizarlos de forma eficiente y sencilla.
Accede a la página oficial de Power BI:

> Qlik
Es una herramienta que se centra en ofrecer al usuario final la posibilidad de extraer
y manipular directamente los datos, creando informes sencillos y todo esto sin la
necesidad de pasar por un equipo de desarrollo. Es decir, maximiza la facilidad de
uso para usuarios no desarrolladores.

> Carto
Es realmente una herramienta que hay que conocer. La facilidad con la que puedes
combinar datos tabulares con mapas es insuperable. Por ejemplo, puedes alimentar
un archivo CSV de cadenas de direcciones y lo convertirá en latitudes y longitudes,
además, las trazará en un mapa.

## 1.3. HTML, CSS y JavaScript


Esta es una asignatura completamente práctica, por lo que a la hora de utilizar las
herramientas y librerías que requieren lenguajes de programación, asumiremos que
sabes qué es HTML, CSS y JavaScript. En caso de que no tengas conocimiento
previo, te recomiendo echar un vistazo a los siguientes tutoriales:

> HTML
HTML es un lenguaje de marcas utilizado para el desarrollo de páginas web. Es una
forma de codificar con base en marcas o etiquetas que contienen información
adicional acerca de la estructura del texto o su presentación.
HTML define la estructura y contenido, pero no define su estilo visual.
Para eso se usará CSS

- HTML: https://www.w3schools.com/html/

> CSS
CSS nos permite generalizar y definir el estilo de la página HTML que se visualizará
en el navegador y de cada elemento HTML de manera exacta. De esta forma, CSS
aísla el contenido de la presentación.

De forma similar a JavaScript, el código se ha de introducir entre las tags: y .
Seguiremos el ejemplo anterior, ¿qué pasa si añadimos al anterior ejemplo el
siguiente CSS?

- CSS: https://www.w3schools.com/css/


> JavaScript
JavaScript nos permite añadir un poco de interacción más avanzada. Se suele definir
el contenido de las funciones dentro de dos etiquetas: y . Entre ellas introduciremos
el contenido que deseamos. Mejor expliquémoslo con un ejemplo tomado d

- JavaScript: https://www.w3schools.com/js/


## 1.4. Editor código: Brackets

Brackets es un editor de código fuente abierto, gratuito y creado por la empresa
Adobe Systems, orientado al desarrollo web. Está enfocado hacia el desarrollo web
de frontend (HMTL, CSS y JavaScript).

Otra facilidad incorporada en Brackets es que utiliza un código de colores bastante
visible. Es decir, cuando haces clic en cualquier etiqueta HTML, se marca en color
verde tanto el principio como el fin del párrafo, siempre que esté bien cerrado. Si no
es así, el resto de etiquetas posteriores las marca en rojo. Esta facilidad ayuda a no
cometer errores debido a etiquetas que queden abiertas.


## Tema 2. Google Chart. Introducción y principales visualizaciones

## 2.1. Introducción y objetivos

Google Chart Library es la librería de visualizaciones utilizada por Google
Spreadsheets. 

Google utiliza esta funcionalidad en la hoja de cálculo que han
implementado y esto nos permite infinitas posibilidades donde estas librerías son una
pequeña funcionalidad.

Piensa en real-time analytics, potentes algoritmos procesando los datos en el backend, visualizaciones de la actividad en Twitter con los contenidos de los tweets ensí..., un gran abanico de posibilidades donde, como expertos en analytics, pondréis el límite a las aplicaciones de la empresa con la que colabores. 

Al fin y al cabo, las visualizaciones son la representación alternativa de la información


## 2.2. Ejemplos de varias visualizaciones

> Pie chart
-  var chart = new google.visualization.PieChart(document.getElementById('chart_div'));

**ENLACES**
- https://developers.google.com/chart/interactive/docs/quick_start?hl=es-419
- https://developers.google.com/chart/interactive/docs/gallery

```HTML
<html>
  <head>
    <!--Load the AJAX API-->
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">

      // Load the Visualization API and the corechart package.
      google.charts.load('current', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.charts.setOnLoadCallback(drawChart);

      // Callback that creates and populates a data table,
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart() {

        // Create the data table.
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Topping');
        data.addColumn('number', 'Slices');
        data.addRows([
          ['Mushrooms', 3],
          ['Onions', 1],
          ['Olives', 1],
          ['Zucchini', 1],
          ['Pepperoni', 2]
        ]);

        // Set chart options
        var options = {'title':'How Much Pizza I Ate Last Night',
                       'width':400,
                       'height':300};

        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
  </head>

  <body>
    <!--Div that will hold the pie chart-->
    <div id="chart_div"></div>
  </body>
</html>
```

**¿Cómo cargamos la librería de Google Chart a nuestro HTML?**
```HTML
<script src="https://www.gstatic.com/charts/loader.js"></script>
<script>
google.charts.load('current', {packages: ['corechart']});
google.charts.setOnLoadCallback(drawChart);
...
</script>
```

La primera línea de este ejemplo se ocupa de cargar el propio «cargador» o de la
librería. Esta sentencia solo debe ejecutarse una vez, independientemente de
cuántas gráficas vayamos a pintar. 

**¿Qué es lo que hace nuestra función drawChart?**

Primero hemos de crear nuestros datos.

>  es una estructura de datos con la que trabaja JavaScript, no muy diferente a lo que podría ser un array de arrays en Java o C

**Después se definen las opciones del gráfico como título y dimensiones:**


> Horizontal bar chart
- var chart = new google.visualization.BarChart(document.getElementById('Sarah_chart_div'));


> Column bar chart
var chart = new
google.visualization.ColumnChart(document.getElementById
('Sarah_chart_div'));

> Geo chart

var chart = new google.visualization.GeoChart
(document.getElementById('regions_div'));
chart.draw(data, options);

## 2.3. Conectando con Google Spreadsheets y archivos CSV

Los datos de las visualizaciones no tienen por qué estar incrustados en el código
fuente de nuestro fichero .html. Si fuera así, cada vez que quisiéramos mostrar
información, deberíamos abrirlo y modificarlo, lo cual no es ni práctico ni realista.
Para ello las visualizaciones recurren a leer los datos de fuentes de datos externas.


**Google Spreadsheets**
Si queremos evitar modificar el código JavaScript cada vez que modificamos los
datos, podemos conectar los gráficos a hojas de cálculo existentes. El proceso se
explica en el siguiente enlace.


Ejemplo: código completo de Google Spreadsheets

```html
<html>
<head>
<script type="text/javascript"
src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
google.charts.load("current", {packages:["corechart"]});
google.setOnLoadCallback(drawChart);
function drawChart() {
var query = new google.visualization.Query(
'https://docs.google.com/spreadsheet/ccc?
key=0Atw2BTU52lOCdEZpUlVIdmxGOWZBR2tuLXhYN2dQTWc&usp
=drive_web#gid=0');
query.send(handleQueryResponse);
}
function handleQueryResponse(response) {
if (response.isError()) {
alert('Error in query: ' + response.getMessage() + ' ' +
response.getDetailedMessage());
return;
}
var data = response.getDataTable();
var chart = new google.visualization.
ColumnChart(document.getElementById('columnchart'));
chart.draw(data, { legend: { position: 'none' } });
}
</script>
<title>Data from a Spreadsheet</title>
</head>
<body>
<span id='columnchart'></span>
</body>
</html>
```

Los archivos CSV normalmente se utilizan para importar o exportar
información de bases de datos.
En este ejercicio también utilizaremos jQuery, una librería de código abierto de
JavaScript, para el tratamiento del fichero CSV. El código adaptado sería el
siguiente:


Ejemplo: código adaptado de CSV
```
<html>
<head>
<title>Google Chart Example</title>
<script type="text/javascript"
src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/
jquery.min.js">
</script>
<script src="jquery.csv-0.71.js"></script>
<script type="text/javascript"
src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
google.charts.load("current", {packages:["corechart"]});
google.setOnLoadCallback(drawChart);
function drawChart() {
// grab the CSV
$.get("https://docs.google.com/spreadsheet/pub?
key=0AhNdznUnSazTdElCVTRTYzF6Zm9DSmlUQkx1NE5DY1E&output
=csv",
function(csvString) {
// Transformar CSV a array utilizando jQuery
var arrayData = $.csv.toArrays(csvString, {onParseValue:
$.csv.hooks.castToScalar});
// Convertir array a DataTable
var data =
new google.visualization.arrayToDataTable(arrayData);
// Generar gráfica desde el DataTable
var chart = new



```
## 2.4. Gestionar eventos

Google Charts genera eventos que se pueden tratar y gestionar. Estos eventos se
suelen disparar por acciones de usuario, como por ejemplo cuando se hace clic en
una gráfica. Se puede registrar un método JavaScript que sea llamado cuando
ocurran dichos eventos e incluso acceder a la información asociada a los mismos.
Cada gráfica y cada interacción definen sus propios eventos y la información
asociada. En la documentación de Google Chart explican con detalle los posibles
eventos:



## Tema 03. Tema 3. D3.js. Introducción y funcionalidades

## 3.1. Introducción y objetivos

## 3.2. Definición e instalación

## 3.3. Elementos básicos de D3.js. Generando elementos HTML

## 3.4. Trabajando con datos reales y elementos en el HTML

## 3.5. Ventajas de D3.js


## Tema 04. 


## Tema 05. 


## Tema 06. 


## Tema 07. 


## Tema 08. 



## Tema 09. 


## Tema 10. 

