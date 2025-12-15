function renderChart(divId, rawJson) {
    const figure = rawJson;
    const data = figure.data;     // Aquí están tus xValues, yValues
    const layout = figure.layout; // Aquí están tus títulos y ejes
    const config = { responsive: true };
    Plotly.newPlot(divId, data, layout, config);
}