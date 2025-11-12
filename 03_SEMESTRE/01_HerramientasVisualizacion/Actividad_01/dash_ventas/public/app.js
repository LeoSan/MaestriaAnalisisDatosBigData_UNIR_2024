// --- Importaciones --- 
import { dibujaRelog, sumaTotalIngresos, sumaTotalUnidades,extraeMinimoUnidades, extraeMaximoUnidades, pintarflasCard } from "./js/util.js";
import { fetchData } from "./js/data-service.js";
import { procesarDatosGraficosBarras, dibujarGraficosBarrasProductos} from "./js/google-chart.js";
import { dibujarGraficaD3Borbujas } from "./js/d3-chart.js";

// --- Constantes ---
const TIEMPO_ACTUALIZACION_SEG = 300; // 5 minutos = 300 segundos
const UN_SEGUNDO_MS = 1000;
const timerElement = document.getElementById("countdown-timer");


// --- Variables de Estado ---
let segundosRestantes = TIEMPO_ACTUALIZACION_SEG;

/**
 * Metodo.
 * Descripción: Función que contiene toda la lógica de actualización de graficas y datos.
 */
async function actualizarDatosYGraficos() {
    // 1. Obtener los datos usando el servicio.
    const data = await fetchData();
    const totalIngresos = sumaTotalIngresos(data);
    const totalUnidades = sumaTotalUnidades(data);
    const totalUnidadesMax = extraeMaximoUnidades(data);
    const totalUnidadesMin = extraeMinimoUnidades(data);
    const asp = totalUnidades > 0 ? totalIngresos / totalUnidades : 0; //ASP (Average Selling Price)
    // 2. Proceso la data en el metodo específico...
    const DatosProcesado = procesarDatosGraficosBarras(data);
    dibujarGraficosBarrasProductos(DatosProcesado, "gchart_div");
    dibujarGraficaD3Borbujas(data, "d3_chart_div");
    // 3. Pinta las FlashCards
    pintarflasCard(totalIngresos, "total-ingresos");
    pintarflasCard(totalUnidades, "total-unidades");
    pintarflasCard(totalUnidadesMax, "precio-maximo");
    pintarflasCard(totalUnidadesMin, "precio-minimo");
    pintarflasCard(asp, "asp-value");
}

/**
 * Metodo.
 * Descripción: Actualiza el texto del contador en el DOM.
 */
function actualizarContadorVisual() {
    if (!timerElement) return; // Salir si el elemento no existe

    const minutos = Math.floor(segundosRestantes / 60);
    const segundos = segundosRestantes % 60;

    // Formato M:SS (ej. 4:05)
    const textoTimer = `${minutos}:${segundos < 10 ? "0" : ""}${segundos}`;
    timerElement.textContent = `(Próxima actualización en ${textoTimer})`;
}


/**
 * Metodo.
 * Descripción: Gestiona la cuenta atrás y dispara la actualización. 
 */
async function gestionarTickActualizacion() {
    segundosRestantes--; // Restamos un segundo

    if (segundosRestantes <= 0) {
        if (timerElement) timerElement.textContent = "(Actualizando...)";
        await actualizarDatosYGraficos();
        segundosRestantes = TIEMPO_ACTUALIZACION_SEG; // 2. Reiniciamos el contador
        actualizarContadorVisual(); 
    } else {
        // Actualizamos la vista del contador en cada tick
        actualizarContadorVisual();
    }
}

/** Metodo Principal.
 * Descripción: Configura eventos e inicia la actualización periódica.
 */ 
async function main() {
    // 1. Configuro el evento para el botón de actualizar gráficos
    const updateButton = document.getElementById("updateButton");
    if (updateButton) {
        updateButton.addEventListener("click", async () => {
            if (timerElement) timerElement.textContent = "(Actualizando...)";
            // 1. Ejecutar actualización
            await actualizarDatosYGraficos();
            // 2. Actualizar vista (mostrar "en 5:00")
            segundosRestantes = TIEMPO_ACTUALIZACION_SEG;
            actualizarContadorVisual();
        });
    }
    // 2. Ejecutamos la actualización por PRIMERA VEZ al cargar la página.
    if (timerElement) timerElement.textContent = "(Cargando datos...)";
    await actualizarDatosYGraficos();

    // 3. Mostramos el contador inicial (ej. "en 5:00")
    actualizarContadorVisual();

    // 4. Configuro el intervalo para que se ejecute CADA SEGUNDO.
    setInterval(gestionarTickActualizacion, UN_SEGUNDO_MS);// Cuenta Regresiva 5 minutos
    setInterval(() => dibujaRelog(), UN_SEGUNDO_MS);//Pinto el reloj cada segundo
}

// 5. Ejecutar la función 'main' cuando el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", main);
