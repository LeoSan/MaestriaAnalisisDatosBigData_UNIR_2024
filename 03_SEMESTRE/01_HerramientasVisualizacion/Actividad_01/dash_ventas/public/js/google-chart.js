import { metodoValidaData } from "./util.js";

/**
 * Módulo para Google Charts.
 * Descripción: Obteniendo y procesando datos para gráficos de barras.
 */
export function procesarDatosGraficosBarras(data) {
    // 1. Valido que tenemos datos para procesar
    metodoValidaData(data, "msj-data-chart");

    // 2. Preparar los datos en el formato que Google Charts requiere para columnas agrupadas
    const productos = [...new Set(data.map((item) => item.producto))]; // Obtener productos únicos
    const meses = [...new Set(data.map((item) => item.mes))]; // Obtener mes unico
    const chartDataArray = [];

    chartDataArray.push(["Mes", ...productos]); // Añadir la fila de encabezados: ['Mes', 'Producto 1', 'Producto 2', ...]

    // Itero sobre cada mes y construir la fila de datos
    meses.forEach((meses) => {
        const row = [meses];
        // Para cada producto, encontrar sus ventas en el mes actual
        productos.forEach((product) => {
            const ventasEntrantes = data.find(
                (item) =>
                    item.mes === meses &&
                    item.producto === product &&
                    item.ventas !== undefined
            );
            row.push(ventasEntrantes ? ventasEntrantes.ventas : 0);
        });
        chartDataArray.push(row);
    });

    //console.log("Datos procesados ✅", chartDataArray);

    return chartDataArray;
}

/**
 * Módulo para Google Charts.
 * Objetivo: Visualización básica con Google Chart Library.
 * Implementa un gráfico de columnas que muestre la evolución de las
 * ventas mensuales por producto, con cada producto representado por una columna distinta.
 */
export function dibujarGraficosBarrasProductos(chartDataArray, DivArea) {
    // 3. Cargar la librería de Google Charts y dibujar el gráfico.
    google.charts.load("current", { packages: ["corechart"] });

    //Vamos a dibujar el gráfico una vez que la librería esté cargada
    google.charts.setOnLoadCallback(() => {
        const chartData = google.visualization.arrayToDataTable(chartDataArray);

        const options = {
            title: "Ventas Mensuales por Producto", // Nuevo título más descriptivo
            is3D:true,
            hAxis: {
                // Eje Horizontal (Meses)
                title: "Mes",
                titleTextStyle: { color: "#333" },
            },
            vAxis: {
                // Eje Vertical (Ventas)
                title: "Unidades Vendidas",
                minValue: 0,
                titleTextStyle: { color: "#333" },
            },
            bar: { groupWidth: "75%" }, // Ajustar el ancho de los grupos de barras
            isStacked: false, // ¡IMPORTANTE! Para columnas agrupadas (no apiladas)
            legend: { position: "top", alignment: "center", maxLines: 3 }, // Leyenda arriba y centrada para productos

            // Usamos tus colores, asegurándonos de tener uno para cada producto
            colors: ["#4cb5f5", "#34675C", "#B3C100"],

            chartArea: { width: "80%", height: "70%" }, // Ajustar el área para dar espacio a la leyenda
            animation: {
                duration: 1000,
                easing: "out",
                startup: true,
            },
            backgroundColor: { fill: "transparent" },
        };

        const chart = new google.visualization.ColumnChart(
            document.getElementById(DivArea)
        );
        chart.draw(chartData, options);
    });
}
