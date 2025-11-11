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
export async function dibujaRelog(TotalIngresos) {
    const now = new Date();
    const optionsDate = { day: "numeric", month: "long", year: "numeric" };
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
    const amountDisplay = document.getElementById("amount-display");

    if (dateDisplay) {
        dateDisplay.innerHTML = "";
        const calendarIcon = document.createElement("i");
        calendarIcon.classList.add("fas", "fa-calendar-alt"); // Clase de Font Awesome
        dateDisplay.appendChild(calendarIcon);
        dateDisplay.append(` ${dateString}`);
    }
    // ICONO PARA LA HORA (Reloj)
    if (timeDisplay) {
        timeDisplay.innerHTML = "";
        const clockIcon = document.createElement("i");
        clockIcon.classList.add("fas", "fa-clock"); // Clase de Font Awesome
        timeDisplay.appendChild(clockIcon);
        timeDisplay.append(` ${timeString}`);
    }

    // ICONO PARA EL MONTO (Dinero)
    if (amountDisplay) {
        amountDisplay.innerHTML = "";
        const moneyIcon = document.createElement("i");
        moneyIcon.classList.add("fas", "fa-dollar-sign");

        amountDisplay.appendChild(moneyIcon);
        amountDisplay.append(` ${TotalIngresos.toLocaleString()} `);
    }
}

export function sumaTotalIngresos(data) {
    // Formato de fecha: 10 de noviembre, 18:28:05
    const totalIngresos = data.reduce(
        (acc, item) => acc + Number(item.ingresos || 0),
        0
    );
    return totalIngresos;
}
