import { metodoValidaData } from "./util.js";

/**
 * Módulo para D3.js.
 * Objetivo: Visualización multidimensional con D3.js (Gráfico de Burbujas).
 * Muestra el producto por color, mes en eje X, ingresos en eje Y, y tamaño de burbuja por ingresos.
 * Incluye transiciones, animaciones y eventos interactivos (mouseover, click).
 */
export function dibujarGraficaD3Borbujas(data, DivArea) {
    // 1. Valido que tenemos datos para procesar
    metodoValidaData(data, "msj-data-d3");
    // 2. Limpiar el contenedor antes de dibujar un nuevo gráfico
    const chartDiv = d3.select("#" + DivArea);
    chartDiv.selectAll("*").remove();

    // 3. Crear un Tooltip para mostrar detalles al pasar el ratón sobre las burbujas
    const tooltip = d3
        .select("body")
        .append("div")
        .attr("class", "d3-tooltip")
        .style("position", "absolute")
        .style("opacity", 0)
        .style("background", "rgba(0,0,0,0.7)")
        .style("color", "#fff")
        .style("padding", "8px")
        .style("border-radius", "4px")
        .style("pointer-events", "none")
        .style("font-size", "0.85rem");

    // 4. Configuración del lienzo (SVG)
    const margin = { top: 40, right: 80, bottom: 60, left: 70 };
    const containerWidth = parseInt(chartDiv.style("width"));
    const width = containerWidth - margin.left - margin.right;
    const height = 400 - margin.top - margin.bottom;

    const svg = chartDiv
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

    // 5. Definir dominios y datos únicos
    const products = [...new Set(data.map((item) => item.producto))]; // Obtener productos únicos
    const months = [...new Set(data.map((item) => item.mes))]; // Obtener mes unico

    // 6. Definir Escalas
    // Escala X (Meses)
    const x = d3
        .scalePoint() // scalePoint para datos categóricos con puntos espaciados
        .domain(months)
        .range([0, width])
        .padding(0.5); // Espacio entre los puntos de los meses

    // Escala Y (Ingresos)
    const maxIngresos = d3.max(data, (d) => d.ingresos);
    const y = d3
        .scaleLinear()
        .domain([0, maxIngresos + maxIngresos * 0.15]) // Añadir padding superior
        .range([height, 0]);

    // Escala para el radio de la burbuja (basado en Ingresos)
    const minRadius = 5; // Radio mínimo para que las burbujas pequeñas sean visibles
    const maxRadius = 30; // Radio máximo
    const r = d3
        .scaleSqrt() // scaleSqrt es bueno para áreas, mejora la percepción visual
        .domain([0, maxIngresos]) // El tamaño de la burbuja se basa en los ingresos
        .range([minRadius, maxRadius]);

    // Escala de Color (Producto)
    const color = d3
        .scaleOrdinal()
        .domain(products)
        .range(["#4cb5f5", "#34675C", "#B3C100"]); // Tus colores para los productos

    // 7. Dibujar los Ejes
    // Eje X
    svg.append("g")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(x))
        .append("text")
        .attr("y", 35)
        .attr("x", width / 2)
        .attr("fill", "#000")
        .style("text-anchor", "middle")
        .text("Mes");

    // Eje Y
    svg.append("g")
        .call(d3.axisLeft(y).tickFormat((d) => `$${d.toLocaleString()}`)) // Formato de moneda
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", -margin.left + 15)
        .attr("x", -height / 2)
        .attr("fill", "#000")
        .style("text-anchor", "middle")
        .text("Ingresos");

    // Título del gráfico
    svg.append("text")
        .attr("x", width / 2)
        .attr("y", 0 - margin.top / 2)
        .attr("text-anchor", "middle")
        .style("font-size", "1rem")
        .style("font-weight", "bold")
        .text("Ingresos por Producto y Mes");

    // 8. Dibujar las Burbujas (Atributos iniciales)
    const bubbles = svg
        .append("g")
        .selectAll("circle")
        .data(data)
        .join("circle")
        .attr("class", "bubble")
        .attr(
            "cx",
            (d) => x(d.mes) + ((Math.random() - 0.5) * x.bandwidth()) / 4
        ) // Jitter horizontal
        .attr("cy", (d) => y(d.ingresos))
        .attr("fill", (d) => color(d.producto))
        .attr("opacity", 0.7)
        .attr("stroke", "#fff")
        .attr("stroke-width", 1.5)
        .attr("r", 0); // <-- Radio inicial de 0

    // 9. *** Manejo de Eventos (¡AHORA ADJUNTADO A LA SELECCIÓN!) ***
    // Adjuntamos los eventos a la selección 'bubbles' ANTES de la transición.
    bubbles
        .on("mouseover", function (event, d) {
            // 'this' es el elemento circle
            d3.select(this)
                .transition()
                .duration(100)
                .attr("opacity", 1)
                .attr("stroke", "#000")
                .attr("stroke-width", 2.5);

            // Mostrar Tooltip
            tooltip.transition().duration(200).style("opacity", 0.9);
            tooltip
                .html(
                    `
        <strong>Producto:</strong> ${d.producto}<br>
        <strong>Mes:</strong> ${d.mes}<br>
        <strong>Ventas:</strong> ${d.ventas.toLocaleString()} u.<br>
        <strong>Ingresos:</strong> $${d.ingresos.toLocaleString()}<br>
        <strong>Precio:</strong> $${d.precio.toLocaleString()}
      `
                )
                .style("left", event.pageX + 15 + "px")
                .style("top", event.pageY - 28 + "px");
        })
        .on("mouseout", function () {
            // No necesitamos 'event' o 'd' aquí
            // Quitar resaltado
            d3.select(this)
                .transition()
                .duration(200)
                .attr("opacity", 0.7)
                .attr("stroke", "#fff")
                .attr("stroke-width", 1.5);

            // Ocultar Tooltip
            tooltip.transition().duration(500).style("opacity", 0);
        })
        .on("click", (event, d) => {
            console.log("Clic en burbuja:", d);
            alert(
                `Detalle - ${d.producto} (${
                    d.mes
                }): Ingresos $${d.ingresos.toLocaleString()}`
            );
        });

    // 10. *** Animación de Entrada 
    // Ahora llamamos a .transition() sobre la selección 'bubbles' que ya tiene sus listeners.
    bubbles
        .transition()
        .duration(1000)
        .delay((d, i) => i * 100)
        .ease(d3.easeElasticOut)
        .attr("r", (d) => r(d.ingresos)); // Animar al radio final

    // 11. Leyenda (Era el paso 10, ahora es 11)
    const legend = svg
        .append("g")
        .attr("font-family", "sans-serif")
        .attr("font-size", 10)
        // ... (el resto de tu código de leyenda) ...
        .attr("transform", (d, i) => `translate(${width - 100},${i * 20})`);

    legend
        .append("rect")
        // ... (el resto de tu código de leyenda) ...
        .attr("fill", color)
        .attr("opacity", 0.7);

    legend
        .append("text")
        // ... (el resto de tu código de leyenda) ...
        .text((d) => d);
}

