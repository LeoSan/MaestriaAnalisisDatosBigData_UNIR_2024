/**
 * Módulo Util.
 * Descripción: Permite generar un mensaje de validación para data vacia.
 */
export function metodoValidaData(data, DivArea) {
  // Validar si hay datos
  if (!data || data.length === 0) {
    console.warn("No hay datos para graficar. ❌");
    document.getElementById(DivArea).innerHTML =
        '<p style="text-align: center; color: #B7B8B6;">No hay datos disponibles. ❌</p>';
    return;
  }
}


/**
 * Módulo Util.
 * Descripción: permite generar la funcionalidad de un reloj.
 */
export function dibujaRelog(data){
    const now = new Date();

    // Formato de fecha: 10 de noviembre, 18:28:05
    const optionsDate = { day: "numeric", month: "long" };
    const dateString = now.toLocaleDateString("es-ES", optionsDate); // 'es-ES' para "de noviembre"

    // Formato de hora: HH:MM:SS
    const optionsTime = {
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hour12: false,
    };
    const timeString = now.toLocaleTimeString("es-ES", optionsTime);

    // Actualizar los elementos HTML
    const dateDisplay = document.getElementById("date-display");
    const timeDisplay = document.getElementById("time-display");

    if (dateDisplay) {
        dateDisplay.textContent = dateString;
    }
    if (timeDisplay) {
        timeDisplay.textContent = timeString;
    }

    // La "cantidad" en tu imagen es estática, pero podríamos hacerla dinámica si hubiese datos
    // Por ahora, la dejamos estática como en la imagen.
    const amountDisplay = document.getElementById("amount-display");
    if (amountDisplay) {
        amountDisplay.textContent = "$ 126,495.49"; // Monto fijo por ahora
    }
}
