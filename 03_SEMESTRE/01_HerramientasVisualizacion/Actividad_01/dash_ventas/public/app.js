import { metodoValidaData, dibujaRelog } from "./js/util.js";  
import { fetchData } from "./js/data-service.js";
import {
  procesarDatosGraficosBarras,
  dibujarGraficosBarrasProductos,
} from "./js/google-chart.js";

import { dibujarGraficaD3Borbujas } from "./js/d3-chart.js";

import  {eventoBtnActualizarGrafica} from "./js/even-board.js";



/**
 * Módulo Principal.
 * Función principal asíncrona que coordina la obtención y el dibujo
 */
async function main() {
    // 1. Obtener los datos usando el servicio.
    const data = await fetchData(); // La variable 'data' ahora contiene el JSON

    //Valida Data
    metodoValidaData(data, "gchart_div");

    // 2. Proceso la data en el metodo específico para generar el arreglo para google charts
    const DatosProcesado = procesarDatosGraficosBarras(data);
    dibujarGraficosBarrasProductos(DatosProcesado, "gchart_div");
    dibujarGraficaD3Borbujas(data, "d3_chart_div");

    // 3. Configuro el evento para el botón de actualizar gráficos
    eventoBtnActualizarGrafica(
        fetchData,
        procesarDatosGraficosBarras,
        dibujarGraficosBarrasProductos
    );

    // 4. Dibuja el reloj con los datos obtenidos
    dibujaRelog(data);
    setInterval(dibujaRelog, 1000);
}

// 4. Ejecutar la función 'main' cuando el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", main);
