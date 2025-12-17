# 🇪🇺 Euro Gini Analytics Dashboard

> **Actividad Grupal:** Análisis de desigualdad en países europeos usando el coeficiente de Gini.  
> **Asignatura:** Visualización Interactiva de la Información - UNIR.

## 📋 Descripción

Este proyecto es una aplicación web desarrollada en **Python (Flask)** diseñada para analizar la evolución de la desigualdad en Europa. 

Su objetivo principal es cumplir con los requerimientos académicos de **comparar visualizaciones correctas vs. visualizaciones manipuladas** (escalas truncadas, paletas confusas, falta de contexto) para entender la ética en el análisis de datos.

## 🚀 Cómo Ejecutar el Proyecto (Instalación)

Puedes levantar el proyecto de dos formas. Elige la que prefieras:

### Opción A: Usando `uv` (Recomendada, más rápida)
Si tienes el gestor de paquetes moderno `uv` instalado, esto es automático.

1.  **Sincronizar:**
    ```bash
    uv sync
    ```
2.  **Ejecutar:**
    ```bash
    uv run run.py
    ```

### Opción B: Usando `pip` (Python estándar)
Si prefieres el método tradicional.

1.  **Crear entorno virtual (opcional pero recomendado):**
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

2.  **Instalar librerías:**
    ```bash
    pip install flask pandas plotly numpy
    ```

3.  **Ejecutar:**
    ```bash
    python run.py
    ```

👉 **Una vez corriendo, abre tu navegador en:** [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🏗 Arquitectura

El proyecto sigue una estructura **MVC** limpia:

* **`run.py`**: Arranca el servidor.
* **`/app/routes.py`**: Controlador que maneja las rutas web.
* **`/app/services`**:
    * `DataLoader`: Limpia y prepara los datos del CSV.
    * `ChartFactory`: Genera las gráficas inteligentes (Plotly).
* **`/app/templates`**: Archivos HTML con el diseño.

## 📚 Estado de la Actividad

| Módulo / Gráfica | Tipo de Visualización | Estado |
| :--- | :--- | :---: |
| **Parte 1: Evolución** | Líneas Multi-serie (España vs Suecia) | ✅ Listo |
| **Parte 1: Error** | Gráfico manipulado (Eje truncado) | ✅ Listo |
| **Parte 2: Contexto** | Scatter Plot (Gini vs PIB) - Riqueza vs Igualdad | ✅ Listo |
| **Parte 3: Crisis** | Análisis COVID-19 (Alemania) - Realidad Histórica | ✅ Listo |
| **Parte 3: Manipulación** | Cherry Picking (Solo 2019-2020) | ✅ Listo |
| **Parte 4: Proyección** | Reforma Fiscal Progresiva (Predicción) | ✅ Listo |

## 🛠 Tecnologías

*   **Backend:** Flask (Python 3.10+)
*   **Visualización:** Plotly (Interactivo)
*   **Datos:** Pandas, NumPy
*   **Diseño:** Tailwind CSS