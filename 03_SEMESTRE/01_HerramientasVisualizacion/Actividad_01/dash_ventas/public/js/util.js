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
  }else{
    document.getElementById(DivArea).innerHTML =
        '';

  }
}


/**
 * Módulo Util.
 * Descripción: permite generar la funcionalidad de un reloj.
 */
export async function dibujaRelog(TotalIngresos, isValida=true) {
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
}

export function sumaTotalIngresos(data) {
    // Formato de fecha: 10 de noviembre, 18:28:05
    const totalIngresos = data.reduce(
        (acc, item) => acc + Number(item.ingresos || 0),
        0
    );
    return totalIngresos;
}
export function sumaTotalUnidades(data) {
    // Formato de fecha: 10 de noviembre, 18:28:05
    const totalIngresos = data.reduce(
        (acc, item) => acc + Number(item.ventas || 0),
        0
    );
    return totalIngresos;
}
export function extraeMaximoUnidades(data) {
    const precios = data.map((item) => item.precio);
    const precioMax = Math.max(...precios);
    return precioMax;
}
export function extraeMinimoUnidades(data) {
    const precios = data.map((item) => item.precio);
    const precioMin = Math.min(...precios);
    return precioMin;
}


export function pintarflasCard(valor_unitario, tipo) {
    let valor = 0;
    let nomSelector = tipo;
    switch (tipo) {
        case "total-ingresos":
            valor = valor_unitario.toLocaleString("es-ES");
            break;
        case "total-unidades":
            valor = valor_unitario;
            break;
        case "precio-maximo":
            valor = valor_unitario.toLocaleString("es-ES", {
                style: "currency",
                currency: "USD",
                minimumFractionDigits: 0,
            });
            break;
        case "precio-minimo":
            valor = valor_unitario.toLocaleString("es-ES", {
                style: "currency",
                currency: "USD",
                minimumFractionDigits: 0,
            });
            break;
        case "asp-value":
            valor = valor_unitario.toLocaleString("es-ES", {
                style: "currency",
                currency: "USD",
                minimumFractionDigits: 2,
            });
            break;
    }
    const divCard = document.getElementById(nomSelector);
    divCard.setHTMLUnsafe(` ${valor} `);

}
