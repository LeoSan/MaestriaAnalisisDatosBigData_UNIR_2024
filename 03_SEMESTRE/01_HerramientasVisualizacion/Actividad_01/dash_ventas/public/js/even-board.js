
/**
 * Módulo Eventos.
 * Descripción: Para manejar eventos en el tablero de ventas Permite actualizar los gráficos al hacer clic en el botón.
 */
export function eventoBtnActualizarGrafica(fetchData, procesarDatosGraficosBarras, dibujarGraficosBarrasProductos) {
    const updateButton = document.getElementById("updateButton");
    if (updateButton) {
        updateButton.addEventListener("click", async () => {
            const data = await fetchData(); // La variable 'data' ahora contiene el JSON
            const DatosProcesado = procesarDatosGraficosBarras(data);
            dibujarGraficosBarrasProductos(DatosProcesado, "gchart_div");
        });
    }
}