# 🛢️ Trump vs Brent Oil Correlation Dashboard

Una plataforma de análisis de datos de alto impacto que correlaciona la comunicación pública de Donald Trump con la volatilidad del mercado petrolero global (Brent Crude).

![Dashboard Preview](docs/assets/preview.png)

## 🌟 Logros del Proyecto

### 1. Dashboard Interactivo (D3.js)
- **Visualización Dinámica**: Gráficos de series temporales unificados entre precios de crudo y eventos sociales.
- **UI Premium**: Interfaz diseñada con **Glassmorphism**, modo oscuro y micro-animaciones para una experiencia de usuario de nivel profesional.
- **Filtros Inteligentes**: Capacidad de filtrado por año y exploración día a día mediante interacción de hover.
- **Análisis de Impacto**: Visualización clara de "No hay coincidencia" vs "Impacto Real" en momentos históricos.

### 2. Motor de Scraping Pro (Playwright + uv)
- **Mini-proyecto de Scraping Modular**: Estructura robusta diseñada para ser escalable y flexible.
- **Gestión Moderna con `uv`**: Implementación de `uv` como gestor de paquetes para una instalación y resolución de dependencias ultra-rápida.
- **Bypass de Obstáculos**: Algoritmos automáticos para cerrar anuncios (popups), aceptar banners de cookies y manejar el "Virtual Scroll" de Truth Social.
- **Extracción a Gran Escala**: Motor optimizado para capturar miles de mensajes (objetivo 2000+) con deduplicación en tiempo real y bajo consumo de memoria.

---

## 📂 Estestructura del Proyecto

```text
DashBoardTrump/
├── src/
│   ├── js/             # Lógica del Dashboard (index.js)
│   ├── css/            # Estilos Glassmorphism (style.css)
│   └── process_data.py # Script de normalización de datos FRED/Twitter
├── Scraping/           # Mini-proyecto independiente (Fase 2)
│   ├── src/            # Lógica modular: main.py, engine.py, parser.py
│   ├── data/           # Datos extraídos (JSON) y muestras de estructura
│   └── pyproject.toml  # Configuración del entorno 'uv'
├── data/               # Datasets consolidados para el dashboard
├── docs/               # Documentación técnica y activos visuales
└── index.html          # Punto de entrada de la aplicación
```

---

## 🛠️ Instalación y Uso

### Ver y Desarrollar el Dashboard (Frontend)
El proyecto utiliza **Vite** para una experiencia de desarrollo moderna y una construcción optimizada:
```bash
# Instalar dependencias
npm install

# Iniciar servidor de desarrollo con HMR (Recarga rápida)
npm run dev

# Generar la carpeta 'dist' para producción (Netlify)
npm run build

# Previsualizar el build final localmente
npm run preview
```

### Despliegue Manual (Netlify)
Para subir el dashboard a producción:
1. Ejecuta `npm run build` para generar la carpeta `dist/`.
2. Ve a tu panel de **Netlify** -> **Add new site** -> **Deploy manually**.
3. Arrastra la carpeta **`dist/`** generada.

### Ejecutar el Scraper (Python + Playwright)
Dentro de la carpeta `/Scraping`:
```bash
# Sincronizar e instalar navegadores
python3 -m uv sync
python3 -m uv run playwright install chromium

# Ejecutar la Gran Extracción (Ejemplo: 1000 posts)
python3 -m uv run src/main.py --limit 1000
```

> [!TIP]
> **Compatibilidad**: Si usas macOS y `uv` no responde directamente, usa siempre el prefijo **`python3 -m uv`**. El proyecto ha sido optimizado y verificado para ser **100% funcional** bajo esta estructura.

---

## 📈 Roadmap y Próximos Pasos
- [x] Correlación histórica Brent Oil vs Twitter (2017-2021).
- [x] Motor de Scraping para Truth Social (2025-2026).
- [x] Implementación de Análisis de Sentimiento (NLP) en los mensajes extraídos.
- [x] Gráficos comparativos de volatilidad "Antes vs Después" de mensajes clave.

---
*Este proyecto demuestra habilidades en Visualización de Datos, Web Scraping avanzado, Ingeniería de Software y Gestión de Proyectos de Ciencia de Datos.*
