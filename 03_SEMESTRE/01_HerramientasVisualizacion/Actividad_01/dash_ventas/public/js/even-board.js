import {dibujaRelog, sumaTotalIngresos } from "./util.js";
import { dibujarGraficaD3Borbujas } from "./d3-chart.js";
import {procesarDatosGraficosBarras, dibujarGraficosBarrasProductos} from "./google-chart.js";

/**
 * Módulo Eventos.
 * Descripción: Para manejar eventos en el tablero de ventas Permite actualizar los gráficos al hacer clic en el botón.
 */
export function eventoBtnActualizarGrafica(
    fetchData
) {
    const updateButton = document.getElementById("updateButton");
    if (updateButton) {
        updateButton.addEventListener("click", async () => {
            const data = await fetchData(); // La variable 'data' ahora contiene el JSON
            const chartDataArray = procesarDatosGraficosBarras(data);
            dibujarGraficosBarrasProductos(chartDataArray, "gchart_div");
            dibujaRelog(sumaTotalIngresos(data));
            dibujarGraficaD3Borbujas(data, "d3_chart_div");
        });
    }
}
