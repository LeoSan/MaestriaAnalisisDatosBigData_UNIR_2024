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
    ├── services/          # Lógica de negocio y procesamiento de datos
    │   ├── DataLoader.py  # Limpia y prepara los datos manejando el origen (CSV/Pandas)
    │   └── ChartFactory.py# Genera las gráficas interactivas inteligentes con Plotly
    └── templates/         # Archivos HTML con el diseño e integración de Tailwind CSS
        ├── base.html
        └── index.html
```

## 🛠 Tecnologías Utilizadas

*   **Backend:** Flask (Python 3.10+)
*   **Visualización:** Plotly (Interactivo)
*   **Datos:** Pandas, NumPy
*   **Diseño:** Tailwind CSS (Por CDN para prototipo rápido)
*   **Gestor de Paquetes:** uv

## 🚀 Pasos para Instalar y Ejecutar el Dashboard

Para ejecutar este proyecto de manera óptima y rápida, utilizaremos `uv`, un instalador y gestor de paquetes de Python ultra-rápido escrito en Rust. Sigue esta secuencia exacta de pasos:

### 1. Instalar `uv` en Mac
Abre tu terminal y ejecuta el siguiente comando para descargar e instalar `uv`:
```bash
pip install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
```
*(Es probable que debas reiniciar tu terminal o ejecutar `source ~/.zshrc` después de la instalación para que reconozca el comando).*

### 2. Instalar las dependencias del proyecto
Ubicado en la carpeta de tu proyecto (directorio `dashboard`), instala todas las librerías requeridas (Flask, Pandas, Plotly, Numpy) ejecutando:
```bash
uv add flask pandas plotly numpy
```
*`uv` creará automáticamente un entorno virtual y descargará las librerías al instante.*

### 3. Iniciar el Servidor
Una vez instaladas las dependencias, arranca la aplicación usando Streamlit a través de `uv`:
```bash
uv pip list
uv pip freeze > requirements.txt
uv run streamlit run run.py
```

### 4. Ver el Dashboard
Abre tu navegador web e ingresa a la siguiente dirección para interactuar con tu aplicación: 
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)
