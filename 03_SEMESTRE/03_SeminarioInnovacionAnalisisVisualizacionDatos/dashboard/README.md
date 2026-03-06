# Dashboard MVC en Flask

Este proyecto implementa un dashboard analítico utilizando una arquitectura Modelo-Vista-Controlador (MVC) con Python, Flask, Plotly y Tailwind CSS.

## 🗂 Estructura del Proyecto

El repositorio sigue la siguiente organización:

```text
dashboard/
├── run.py                 # Arranca el servidor (Punto de entrada)
├── pyproject.toml         # Configuración de dependencias (uv)
└── app/
    ├── __init__.py        # Inicialización de la aplicación Flask
    ├── routes.py          # Controlador que maneja las rutas web
    ├── controllers/       # Lógica central del negocio (MVC)
    │   └── dashboard_controller.py
    ├── services/          # Procesamiento de datos y analítica
    │   └── DataLoader.py  # Limpia y prepara los datos desde CSV/Pandas
    ├── static/            # Archivos estáticos de frontend
    │   └── js/
    │       └── main.js    # Lógica interactiva de UI (Dark mode, PDF, Plotly)
    └── templates/         # Archivos HTML con Jinja2 e integración de Tailwind CSS
        ├── base.html      # Plantilla principal (Navbar, Footer, Layout global)
        ├── index.html     # Vista principal del Dashboard (Ensambla componentes)
        ├── nosotros.html  # Vista institucional del equipo
        ├── fuentes.html   # Vista de bibliografía y referencias
        └── components/    # Módulos reutilizables del Dashboard
            ├── evolution_section.html    # Gráfico de serie de tiempo
            ├── kmens_random_section.html # Machine Learning (K-Means & Random Forest)
            ├── kpi_section.html          # Tarjetas superiores de indicadores
            ├── map_section.html          # Mapas coropléticos
            └── table_sections.html       # Sidebar de filtros y tabla de datos
```

## 🛠 Tecnologías Utilizadas

*   **Backend:** Flask (Python 3.10+)
*   **Visualización:** Plotly (Interactivo)
*   **Datos:** Pandas, NumPy
*   **Diseño:** Tailwind CSS (Por CDN para prototipo rápido)
*   **Gestor de Paquetes:** uv

## � Pre-Requisitos (Antes de instalar)

Este sistema requiere **Python 3.10 o superior** y el gestor de paquetes `pip` instalados en tu computadora. Si aún no los tienes, sigue estos pasos fundamentales:

### En Windows
1. Ve al [sitio oficial de descargas de Python para Windows](https://www.python.org/downloads/windows/).
2. Descarga el instalador ejecutable (ej. Python 3.11 o 3.12).
3. **Paso muy importante:** Al abrir el instalador interactivo, asegúrate de marcar la casilla **"Add Python to PATH"** en la parte inferior *antes* de hacer clic en "Install Now".
4. Tras finalizar, abre `cmd` o PowerShell y verifica con: `python --version` y `pip --version`.

### En Mac/Linux
1. **Mac (con Homebrew):** Abre tu terminal y ejecuta: `brew install python`
2. **Linux (Ubuntu/Debian):** Ejecuta: `sudo apt update && sudo apt install python3 python3-pip`
3. Verifica la instalación ejecutando: `python3 --version` y `pip3 --version`.

---

## �🚀 Instalación y Configuración del Entorno

Para instalar este proyecto de manera óptima, recomendamos utilizar `uv`, un gestor de paquetes de Python ultra-rápido. Si `uv` falla, siempre puedes usar el clásico `pip` de Python.

### 1. Instalar `uv` (Recomendado)
- **En Windows (Abre PowerShell y ejecuta):**
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```
  *(Nota Crítica: Cierra la terminal y vuelve a abrirla después de la instalación para que Windows reconozca el comando).*
- **En Mac/Linux:**
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### 2. Instalar las dependencias (Plugins)
Ubicado en la carpeta principal del proyecto (`dashboard`), instala todas las librerías necesarias:
```bash
# Método A: Usando uv (Crea un entorno virtual ultra-rápido)
uv add flask pandas plotly numpy scikit-learn

# Método B: Alternativa clásica si uv fallara
pip install flask pandas plotly numpy scikit-learn
```

## 🏃‍♂️ Ejecución y Buenas Prácticas

Una vez instalados todos los plugins, sigue este flujo de trabajo para asegurar que la aplicación corra de manera óptima y limpia:

1. **Validar Entorno**: Asegúrate de que no haya librerías faltantes.
   ```bash
   uv pip list
   ```
2. **Limpiar y Congelar**: Es buena práctica mapear un snapshot de las versiones exactas por si necesitas desplegarlo en un servidor clásico.
   ```bash
   uv pip freeze > requirements.txt
   ```
3. **Levantar el Dashboard**: Ejecuta el controlador en modo desarrollo de Flask.
   ```bash
   uv run python run.py
   ```
   *(Si no utilizas uv, puedes simplemente ejecutar: `python run.py`)*

4. **Ver el Dashboard**: Abre tu navegador web e interactúa con tu aplicación en: 
   👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🆕 Últimas Actualizaciones

### Paso 2: Panel Superior de Indicadores Clave de Riesgo (KPIs)
Se implementó un panel superior para visualizar el estado de cuatro variables críticas relacionadas al riesgo de abandono escolar:
1. **Tasa de Abandono Primaria (%)**
2. **Carencia de Salud (%)**: Incluye lógica de semáforo (Jinja2). Si supera el 50%, se activa una alerta visual (rojo) indicando alto riesgo de abandono.
3. **Razón de Ingreso (Índice)**
4. **Vivienda Piso Tierra (%)**

**Detalles Técnicos (Patrón MVC):**
*   **Controlador (`dashboard_controller.py`)**: Se calcula el promedio matemático de las variables clave (`.mean()`) desde el DataFrame ya filtrado en Pandas, se redondean a 2 decimales y se envían como variables de contexto al renderizar la plantilla HTML. *(Nota: Se actualizó la lógica para usar la nueva columna `PERIODO_ANIO` según el dataset optimizado).*
*   **Vista (`index.html`)**: Se diseñó una cuadrícula en CSS Grid (TailwindCSS) con 4 "Cards". La tarjeta de Salud utiliza sintaxis de Jinja2 (`{% if kpi_salud > 50 %}`) para aplicar clases CSS dinámicas de emergencia.

### Paso 3: Mapas Coropléticos Interactivos
Se integró visualización geoespacial avanzada comparando la **Tasa de Abandono Primaria** versus la **Carencia de Salud**. Ambos mapas están en paralelo para facilitar el análisis visual de la correlación (dónde hay mayor carencia coincidiendo con mayores abandonos).

**Detalles Técnicos:**
*   **Backend (`plotly.express`)**: Se generan dos figuras coropléticas usando `px.choropleth`. Las figuras analizan el DataFrame cruzado contra un GeoJSON delimitando los estados de México, y las dibuja usando una rampa de color invertida (`RdYlGn_r` – donde el semáforo apunta que "Rojo" es de mayor criticidad). Estas figuras se serializan y envían a la vista como cadenas JSON (`plotly.utils.PlotlyJSONEncoder`).
*   **Frontend**: 
    1.  Importación de librería nativa para JavaScript (`plotly-latest.min.js`).
    2.  Asignación arquitectónica limpia separando HTML de JS. Se pasaron las cadenas de Jinja2 a constructores globales en el objeto `window` de JS.

### Paso 4: Evolución Temporal y Divergencia
Visualización de una Serie de Tiempo (Line Chart interactivo) entre 2021 y 2024 que resuelve matemáticamente y expone la situación sobre de la Tasa de Abandono Escolar en el tiempo.

**Detalles Técnicos:**
*   **Backend (`plotly.graph_objects`)**: Se crea un dataframe consolidado nuevo agrupando (`groupby`) la Tasa Promedio por año de todo "Nacional". Posteriormente, y dentro de la misma gráfica de áreas/trazas múltiples interactiva (`go.Scatter`), se empalma la línea de tendencia específica del Estado que el usuario haya seleccionado en el momento.
*   **Frontend**: Refactorización del código in-line. Implementamos centralización de Scripts en `app/static/js/main.js` para inicializar el gráfico (`Plotly.newPlot`), respetando fielmente el patrón puro de desarrollo MVC y proveyendo un espacio base listo (`container-fluid`) pero reconfigurado para 100% Tailwind (con backdrop-filters fluidos) en el cliente final HTML.

### Paso 5: Diagnóstico Predictivo y Perfiles de Vulnerabilidad (Machine Learning)
Para completar el panorama de toma de decisiones, se integró una capa de Inteligencia Artificial (Machine Learning) utilizando `scikit-learn` en el backend para predecir y agrupar comportamientos anómalos.

**Gráfico 1: Factores de Riesgo (Random Forest)**
*   Se expone el Feature Importance de un modelo Random Forest previamente entrenado. Este modelo reveló matemáticamente que la **Carencia de Salud (0.22)** es el principal detonante de abandono. Se visualiza con un `px.bar` horizontal (escala de rojos).

**Gráfico 2: K-Means Clustering Dinámico (2024)**
*   Se realiza una segmentación No Supervisada en tiempo real. 
*   **Backend:** Se filtran los datos crudos exclusivamente para 2024. Las variables clave (`CARENCIA_SALUD`, `INSEG_ALIMENTARIA`, `TASA_ABANDONO_PRIMARIA`) pasan por una estandarización (`StandardScaler`) antes de alimentar al algoritmo de agrupamiento espectral **K-Means** (`n_clusters=3`).
*   **Perfiles:** El modelo clasifica automáticamente a los Estados dentro de tres arquetipos ("Riesgo Moderado", "Riesgo Crítico", "Anomalía"). Se renderiza como un `px.scatter` donde cada cluster se mapea con una paleta de colores de Tailwind (`#3b82f6`, `#ef4444`, `#f59e0b`).
*   **Frontend**: Ambos gráficos fueron maquetados usando CSS Grid de Tailwind (`grid-cols-1 lg:grid-cols-2`) de forma "responsive", listos en la sección inferior que cierra el cuerpo principal analítico del Dashboard.

### Paso 6: UI/UX y Funcionalidades de Exportación
Se realizaron mejoras significativas en la experiencia de usuario y presentación formal del proyecto.

**Modo Oscuro / Claro (Dark Mode Toggle):**
*   Implementación de un selector de temas en la barra de navegación que intercambia clases `dark` de Tailwind CSS a nivel raíz (`<html>`).
*   **Persistencia:** La preferencia elegida por el usuario se guarda en el `localStorage` del navegador.
*   **Adaptabilidad Plotly:** Los gráficos interactivos escuchan el evento de cambio y mutan sus colores de fuente y plantillas base (`plotly_dark` a `plotly_white`) dinámicamente usando `Plotly.relayout` sin necesidad de recargar la página.

**Generación de Reportes PDF:**
*   Se integró la librería `html2pdf.js` para permitir la exportación de todo el dashboard visible a un documento PDF tipo infografía. Mediante un botón en el menú, se captura el nodo DOM principal (`<main>`), se escala para mantener la resolución (`html2canvas`) y se emite un archivo prestablecido formato *Legal* apaisado (*landscape*).

**Nuevas Vistas Informativas:**
*   **Página "Nosotros":** Ruta `/nosotros` que renderiza una tarjeta de presentación institucional del equipo de trabajo, mostrando los nombres de los integrantes y los detalles oficiales del Máster Profesional de la Universidad Internacional de La Rioja (UNIR).
*   **Página "Fuentes de Datos":** Ruta `/fuentes-de-datos` que engloba la bibliografía consultada en orden alfabético y proporciona un enlace directo al Dataset final analítico y estructurado alojado en la nube (Google Sheets), garantizando la reproducibilidad Open Source del monitor.
