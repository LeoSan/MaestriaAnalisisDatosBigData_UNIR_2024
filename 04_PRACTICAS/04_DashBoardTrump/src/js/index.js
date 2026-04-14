/**
 * Trump vs Brent Oil Correlation Engine
 * Powered by D3.js
 */

let fullData = null;
let currentYear = 'all';

async function initDashboard() {
    try {
        const response = await fetch('data/processed_data.json');
        fullData = await response.json();

        setupFilters();
        updateDashboard();
    } catch (error) {
        console.error('Error al cargar los datos:', error);
        document.querySelector('.loader').innerText = 'Error al cargar los datos. Verifica el archivo JSON.';
    }
}

function setupFilters() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentYear = btn.dataset.year;
            updateDashboard();
        });
    });
}

function updateDashboard() {
    if (!fullData) return;

    let filteredData = fullData.combined_series;

    if (currentYear !== 'all') {
        filteredData = fullData.combined_series.filter(d => d.date.startsWith(currentYear));
    }

    const series = filteredData.map(d => ({
        ...d,
        date: new Date(d.date)
    }));

    renderChart(series);

    // El sidebar solo muestra eventos REALES (con tweet)
    const eventsOnly = series.filter(s => s.tweet_url !== null);
    renderSidebar(eventsOnly);
    d3.select('#tweet-count').text(eventsOnly.length);
}

function renderSidebar(events) {
    const list = d3.select('#events-list');
    list.html('');

    if (events.length === 0) {
        list.append('p').attr('class', 'empty-msg').text('No hay eventos clave en este periodo.');
        return;
    }

    events.forEach(event => {
        const card = list.append('div').attr('class', 'event-card');

        const meta = card.append('div').attr('class', 'card-meta');
        meta.append('span').attr('class', 'card-date').text(event.date.toLocaleDateString('es-ES', { month: 'short', day: 'numeric', year: 'numeric' }));
        meta.append('span').attr('class', 'card-price').text(`$${event.price.toFixed(2)}`);

        card.append('p').attr('class', 'card-text').text(event.tweet_text);

        card.on('click', () => {
            window.open(event.tweet_url, '_blank');
        });
    });
}

function renderChart(series) {
    const container = d3.select('#chart-container');
    container.html('');

    const width = container.node().clientWidth;
    const height = 600;
    const margin = { top: 40, right: 40, bottom: 60, left: 60 };

    const svg = container.append('svg')
        .attr('width', '100%')
        .attr('height', height)
        .attr('viewBox', `0 0 ${width} ${height}`);

    // Escalas
    const x = d3.scaleTime()
        .domain(d3.extent(series, d => d.date))
        .range([margin.left, width - margin.right]);

    const y = d3.scaleLinear()
        .domain([d3.min(series, d => d.price) * 0.9, d3.max(series, d => d.price) * 1.1])
        .range([height - margin.bottom, margin.top]);

    // Ejes
    const xAxis = g => g
        .attr('transform', `translate(0,${height - margin.bottom})`)
        .call(d3.axisBottom(x).ticks(width / 100).tickSizeOuter(0))
        .call(g => g.selectAll('.tick text').attr('class', 'axis-label'))
        .call(g => g.select('.domain').attr('stroke', 'rgba(255,255,255,0.1)'));

    const yAxis = g => g
        .attr('transform', `translate(${margin.left},0)`)
        .call(d3.axisLeft(y).ticks(8))
        .call(g => g.selectAll('.tick text').attr('class', 'axis-label'))
        .call(g => g.select('.domain').attr('stroke', 'rgba(255,255,255,0.1)'))
        .call(g => g.selectAll('.tick line').attr('class', 'grid-line').attr('x2', width - margin.right - margin.left));

    svg.append('g').call(xAxis);
    svg.append('g').call(yAxis);

    // Gradiente de Área
    const area = d3.area()
        .x(d => x(d.date))
        .y0(y.range()[0])
        .y1(d => y(d.price))
        .curve(d3.curveMonotoneX);

    const defs = svg.append('defs');
    const gradient = defs.append('linearGradient')
        .attr('id', 'oil-gradient')
        .attr('x1', '0%').attr('y1', '0%').attr('x2', '0%').attr('y2', '100%');
    gradient.append('stop').attr('offset', '0%').attr('stop-color', '#3b82f6').attr('stop-opacity', 0.2);
    gradient.append('stop').attr('offset', '100%').attr('stop-color', '#3b82f6').attr('stop-opacity', 0);

    svg.append('path')
        .datum(series)
        .attr('fill', 'url(#oil-gradient)')
        .attr('d', area);

    // Línea de Precio
    const line = d3.line()
        .x(d => x(d.date))
        .y(d => y(d.price))
        .curve(d3.curveMonotoneX);

    svg.append('path')
        .datum(series)
        .attr('class', 'oil-line-path')
        .attr('d', line);

    // Marcadores de Eventos (Solo donde hay Tweets)
    svg.selectAll('.event-marker')
        .data(series.filter(d => d.tweet_url !== null))
        .enter()
        .append('circle')
        .attr('class', 'event-marker')
        .attr('cx', d => x(d.date))
        .attr('cy', d => y(d.price))
        .attr('r', 5);

    // Superficie invisible para Hover (Captura todos los puntos para ver el "No hay coincidencia")
    const focus = svg.append('g')
        .style('display', 'none');

    focus.append('circle')
        .attr('r', 8)
        .attr('fill', 'white')
        .attr('opacity', 0.3);

    svg.append('rect')
        .attr('width', width)
        .attr('height', height)
        .attr('fill', 'none')
        .attr('pointer-events', 'all')
        .on('mouseover', () => focus.style('display', null))
        .on('mouseout', () => focus.style('display', 'none'))
        .on('mousemove', function (event) {
            const bisect = d3.bisector(d => d.date).left;
            const x0 = x.invert(d3.pointer(event)[0]);
            const i = bisect(series, x0, 1);
            const d0 = series[i - 1];
            const d1 = series[i];
            const d = x0 - d0.date > d1.date - x0 ? d1 : d0;

            focus.attr('transform', `translate(${x(d.date)},${y(d.price)})`);
            showDetail(d, event);
        });

    // Funciones de interacción
    const detailPanel = d3.select('#detail-panel');

    function showDetail(d, event) {
        detailPanel.classed('hidden', false);
        
        // Posicionamiento dinámico para no tapar la gráfica
        const chartWidth = container.node().clientWidth;
        const mouseX = d3.pointer(event)[0];
        
        if (mouseX > chartWidth / 2) {
            detailPanel.style('left', '2rem').style('right', 'auto');
        } else {
            detailPanel.style('right', '2rem').style('left', 'auto');
        }

        d3.select('#detail-date').text(d.date.toLocaleDateString('es-ES', { year: 'numeric', month: 'long', day: 'numeric' }));
        d3.select('#detail-price').text(d.price.toFixed(2));
        d3.select('#detail-text').text(d.tweet_text);

        // Mostrar/Ocultar enlace
        const urlBtn = d3.select('#detail-url');
        if (d.tweet_url) {
            urlBtn.style('display', 'inline-block').attr('href', d.tweet_url);
        } else {
            urlBtn.style('display', 'none');
        }
    }
}

// Iniciar
initDashboard();
