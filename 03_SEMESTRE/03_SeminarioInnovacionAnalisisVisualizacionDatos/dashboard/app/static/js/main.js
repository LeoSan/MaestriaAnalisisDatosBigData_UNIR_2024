/**
 * main.js
 * Repositorio central de scripts interactivos para el Dashboard MVC.
 * Aquí puedes incluir más funciones y lógica front-end en el futuro.
 */

document.addEventListener("DOMContentLoaded", function () {

    // =========================================================================
    // INICIALIZACIÓN DE MAPAS PLOTLY (Paso 3)
    // =========================================================================

    // Obtenemos los datos inyectados globalmente desde el backend (Flask/Jinja2)
    const mapaAbandonoData = window.mapaAbandonoData;
    const mapaSaludData = window.mapaSaludData;

    // Objeto configuración para que Plotly los haga completamente dinámicos
    const configPlotly = { responsive: true, displayModeBar: false };

    // Renderizar Mapa 1: Tasa de Abandono Primaria
    const containerAbandono = document.getElementById('mapa_abandono');
    if (containerAbandono && mapaAbandonoData) {
        if (Object.keys(mapaAbandonoData).length > 0) {
            Plotly.newPlot('mapa_abandono', mapaAbandonoData.data, mapaAbandonoData.layout, configPlotly);
        } else {
            containerAbandono.innerHTML = "<p class='text-slate-500'>No hay datos suficientes para mostrar el mapa de abandono.</p>";
        }
    }

    // Renderizar Mapa 2: Carencia de Salud
    const containerSalud = document.getElementById('mapa_salud');
    if (containerSalud && mapaSaludData) {
        if (Object.keys(mapaSaludData).length > 0) {
            Plotly.newPlot('mapa_salud', mapaSaludData.data, mapaSaludData.layout, configPlotly);
        } else {
            containerSalud.innerHTML = "<p class='text-slate-500'>No hay datos suficientes para mostrar el mapa de salud.</p>";
        }
    }

    // =========================================================================
    // INICIALIZACIÓN GRÁFICO EVOLUCIÓN TEMPORAL (Paso 4)
    // =========================================================================

    const evolucionTemporalData = window.evolucionTemporalData;
    const containerEvolucion = document.getElementById('grafico_evolucion');

    if (containerEvolucion && evolucionTemporalData) {
        if (Object.keys(evolucionTemporalData).length > 0) {
            Plotly.newPlot('grafico_evolucion', evolucionTemporalData.data, evolucionTemporalData.layout, configPlotly);
        } else {
            containerEvolucion.innerHTML = "<p class='text-slate-500 text-center py-10'>No hay datos suficientes para mostrar el gráfico de evolución.</p>";
        }
    }

    // =========================================================================
    // INICIALIZACIÓN GRÁFICAS MACHINE LEARNING (Paso 5)
    // =========================================================================

    // Gráfico 1: Random Forest (Importancia de factores)
    const rfBarData = window.rfBarData;
    const containerRf = document.getElementById('grafico_rf');

    if (containerRf && rfBarData && Object.keys(rfBarData).length > 0) {
        Plotly.newPlot('grafico_rf', rfBarData.data, rfBarData.layout, configPlotly);
    } else if (containerRf) {
        containerRf.innerHTML = "<p class='text-slate-500 text-center py-10'>No hay datos para mostrar el modelo predictivo.</p>";
    }

    // Gráfico 2: K-Means Clustering
    const kmeansScatterData = window.kmeansScatterData;
    const containerKmeans = document.getElementById('grafico_kmeans');

    if (containerKmeans && kmeansScatterData && Object.keys(kmeansScatterData).length > 0) {
        Plotly.newPlot('grafico_kmeans', kmeansScatterData.data, kmeansScatterData.layout, configPlotly);
    } else if (containerKmeans) {
        containerKmeans.innerHTML = "<p class='text-slate-500 text-center py-10'>No hay datos para mostrar el análisis de clustering.</p>";
    }

    // =========================================================================
    // ESPACIO PARA FUTUROS SCRIPTS / COMPONENTES
    // =========================================================================

    // function nuevaFuncionalidad() {
    //     ...
    // }

});
