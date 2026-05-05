# Radar de Tecnologías: Data Pipeline Modular 🚀

¡Bienvenido al proyecto **Radar de Tecnologías**! 
Este documento ha sido creado bajo la filosofía *Kaizen* (Mejora Continua) para que sirva no solo como manual de ejecución, sino como una **guía de estudio en Ingeniería de Datos y Arquitectura de Software**.

---

## 🎯 El Problema a Resolver

Queríamos analizar la **obsolescencia y el nivel de interacción** de diferentes lenguajes de programación (como PHP, Python, TypeScript, Java, C#, Go y R) a lo largo del tiempo (24 meses). Para ello, decidimos extraer datos de la **API de Stack Exchange**.

Sin embargo, al enfrentar un volumen de datos que crece mes a mes, un simple script secuencial (spaghetti code) fracasaría rápido. Los problemas comunes al hacer esto son:
1. **Límites de la API (Rate Limits):** Stack Exchange bloquea a los usuarios que hacen demasiadas peticiones seguidas.
2. **Memoria RAM Saturada (Out of Memory):** Descargar 24 meses de datos de 7 lenguajes e intentar mantenerlos todos en la memoria al mismo tiempo destruirá la RAM de la máquina.
3. **Mantenibilidad:** Si queremos cambiar la forma en que graficamos, no queremos tener que modificar la lógica de descarga.

---

## 🏗️ La Solución: Arquitectura de Datos Limpia (Modular)

Para resolver estos retos, construimos un **Data Pipeline Modular**. Esta arquitectura imita a los sistemas de nivel de producción en Big Data, separando el problema en componentes independientes:

### 1. Módulo Core (`/core`)
**El "Cerebro Administrativo"**
- **`config.py`:** Utiliza la librería `pydantic-settings`. En lugar de hardcodear variables en el código, lee un archivo oculto `.env` (donde pusimos tu API Key). Esto es una *buena práctica obligatoria* en la industria para la seguridad de credenciales.
- **`logger.py`:** Centraliza todos los `print` del sistema en un log profesional (`logs/extraction.log`), permitiendo depurar problemas sin saturar la consola visual.

### 2. Módulo de Extracción (`/extractor`)
**El "Minero Resiliente"**
- **`time_utils.py`:** Genera ventanas de tiempo mensuales (usando Timestamp UNIX, que es el estándar que exige Stack Exchange).
- **`client.py`:** Aquí aplicamos Ingeniería de Software avanzada. Usamos la librería `tenacity` (con el decorador `@retry`). ¿El porqué? Si la API de Stack Exchange nos devuelve un error `429 Too Many Requests` o nos manda un parámetro `backoff`, el código se pausa y reintenta automáticamente con un patrón exponencial. Así, **nuestro pipeline nunca "colapsa" por red**.

### 3. Módulo de Persistencia y Contratos (`/io_module`)
**El "Almacén Big Data"**
- **`storage.py`:** Aquí aplicamos el concepto de **Contrato de Datos (Data Contract)**. Tomamos el JSON desordenado de la API, extraemos *únicamente* los campos que nos interesan (score, views, answered) y nos aseguramos de que tengan el tipo de dato correcto (ej. `bool` para answered).
- **¿Por qué usamos formato Parquet?** En lugar de guardar en CSV o JSON, guardamos los fragmentos en formato **Parquet**. Al guardar fragmentos mes a mes en disco, liberamos la memoria RAM (el pipeline consume un mes, lo guarda, lo olvida y pasa al siguiente).

#### 💡 Teoría Kaizen: Parquet vs JSON/CSV en Big Data
Es común pensar que el formato binario (ilegible para humanos al abrirlo en un bloc de notas) de Parquet es una desventaja frente al texto plano de un JSON o CSV. Sin embargo, en Ingeniería de Datos los humanos no leen los archivos crudos (se leen mediante código, como Pandas). Las ventajas técnicas de Parquet son masivas:
1. **Row-based vs Column-based:** JSON y CSV leen datos por fila. Si tienes un archivo con 100 columnas y solo quieres promediar la columna "Score", la computadora debe cargar las 100 columnas a la memoria RAM. Parquet guarda los datos ordenados por columnas; si pides el "Score", va directamente a ese bloque en el disco duro, ignorando el resto. Esto salva tus recursos.
2. **Compresión Extrema:** Al agrupar datos del mismo tipo de forma contigua (puros números con números, puros textos con textos), los algoritmos de compresión hacen magia. Un archivo CSV de 1 GB puede pesar tan solo 150 MB en Parquet.
> **Analogía:** JSON es como buscar un teléfono en un libro tradicional leyendo hoja por hoja. Parquet es tener un índice avanzado que te lleva exactamente a la columna de teléfonos ignorando las direcciones.

### 4. Transformación de Negocio (`/analytics`)
**El "Cerebro Analítico"**
- **`processor.py`:** Una vez que TODOS los fragmentos `.parquet` están descargados de forma segura en disco, esta capa entra en acción. Lee todos los archivos simultáneamente (muy rápido gracias a que es Parquet), y usa `Pandas` para agrupar los datos (`groupby`) por tecnología y mes.
- Aquí es donde se calcula el valor del negocio: **Engagement Rate** (Score + Answers / Views) y **Health Index** (% de preguntas contestadas).

### 5. Visualización Estratégica (`/viz`)
**La "Presentación a Gerencia"**
- **`charts.py`:** Toma las métricas agrupadas finales (que ya son muy poquitos datos, por ende súper ligeros) y usa la librería `seaborn` para trazar una **Media Móvil de 3 meses**. La media móvil ayuda a suavizar los "picos" aleatorios de un mes a otro para revelar la tendencia real y subyacente de cada tecnología.

---

## ⚙️ Flujo del Orquestador (`main.py`)

Si observas el archivo `main.py`, verás que el código es extremadamente fácil de leer porque solo coordina módulos:

```python
# Flujo Lógico de main.py
1. Leer Configuración (qué lenguajes, cuántos meses)
2. Bucle (Por cada lenguaje -> Por cada mes):
      a. client.fetch_data() (descarga JSON)
      b. storage.save_raw_to_parquet() (guarda al disco y vacía RAM)
3. Termina descarga -> procesador.calculate_metrics() (une todo en un gran reporte)
4. charts.plot_rolling_mean() (pinta la foto final)
```

---

## 🚀 Cómo Ejecutar el Proyecto

Este proyecto cuenta con un entorno virtual para aislar las librerías (`requests`, `pandas`, `seaborn`, `tenacity`, `pyarrow`).

**Paso a paso:**
1. Abre tu terminal.
2. Navega al directorio del proyecto:
   ```bash
   cd /Users/fernando/Documents/DEV/AgenteIA/DashRadarTecnologia
   ```
3. Activa el entorno virtual (importante para que Python encuentre Pandas y las demás librerías):
   ```bash
   source venv/bin/activate
   ```
4. Ejecuta el orquestador maestro:
   ```bash
   python main.py
   ```
5. ¡Ve por un café! Dependiendo de la cantidad de lenguajes y meses (actualmente configurado a 7 lenguajes x 24 meses), el script pausará inteligentemente para no ser bloqueado por Stack Exchange. Al finalizar, tu gráfico estará listo en `reports/figures/volume_rolling_mean.png`.

---

## 📚 Glosario de Importaciones (Estudio Kaizen)

Para comprender profundamente cómo funciona este proyecto y aplicar esta arquitectura en el futuro, es vital entender las herramientas que lo componen. A continuación, desglosamos los `import` y `from` utilizados, divididos por categorías:

### 1. Librerías de Terceros (Ecosistema Data & Resiliencia)

Estas son herramientas creadas por la comunidad que instalamos vía `pip`. Son los cimientos del ecosistema de Big Data e Ingeniería de Software en Python.

*   **`import pandas as pd`**
    *   **Uso:** La "navaja suiza" del análisis de datos en Python. Se usa para manipular tablas de datos en memoria (DataFrames).
    *   **Ejemplo en el proyecto:** Agrupar los datos crudos por mes y lenguaje, y calcular promedios móviles (`rolling.mean()`).
*   **`import pyarrow as pa` / `import pyarrow.parquet as pq`**
    *   **Uso:** PyArrow es el motor detrás de la lectura y escritura del formato **Parquet**. Parquet es un formato columnar súper eficiente (comprime mucho más que CSV y lee más rápido), un estándar indispensable en entornos Big Data.
    *   **Ejemplo en el proyecto:** Guardar los datos extraídos en `/data/raw` usando formato columnar para optimizar espacio en disco.
*   **`import requests`**
    *   **Uso:** Permite hacer peticiones HTTP a servidores externos de forma sencilla.
    *   **Ejemplo en el proyecto:** Comunicarse con la API REST de Stack Exchange enviando parámetros como fechas y tags.
*   **`from tenacity import retry, wait_exponential...`**
    *   **Uso:** Tenacity es magia pura para sistemas distribuidos y conexiones de red. Permite "decorar" una función para que, si falla (ej. se cae la red o la API nos bloquea temporalmente con un `429 Too Many Requests`), lo intente de nuevo automáticamente siguiendo reglas de espera (backoff exponencial).
    *   **Ejemplo en el proyecto:** Envolver la función que llama a la API para que el pipeline no muera por una falla temporal de conexión.
*   **`from pydantic_settings import BaseSettings, SettingsConfigDict`**
    *   **Uso:** Pydantic es el estándar actual para validación de datos. `pydantic-settings` permite leer variables de entorno (desde un archivo `.env`) y validarlas estrictamente.
    *   **Ejemplo en el proyecto:** Asegurar que `STACK_API_KEY` se cargue de forma segura y que `LOOKBACK_MONTHS` sea estrictamente un número entero (int).
*   **`import matplotlib.pyplot as plt` / `import seaborn as sns`**
    *   **Uso:** Librerías estándar para visualización de datos estáticos en Python. Seaborn facilita aplicar paletas de colores y estilos profesionales a matplotlib.
    *   **Ejemplo en el proyecto:** Trazar el gráfico de líneas del promedio móvil de preguntas tecnológicas.

### 2. Librerías Estándar de Python (Built-in)

Estas vienen preinstaladas con Python, no requieren `pip install`.

*   **`from pathlib import Path`**
    *   **Uso:** Manejo moderno de rutas de archivos (orientado a objetos). Es superior al antiguo `os.path` porque el mismo código funciona en Windows, Mac y Linux sin preocuparse por las diagonales (`/` vs `\`).
    *   **Ejemplo en el proyecto:** `BASE_DIR = Path(__file__).parent.parent` para encontrar la carpeta raíz de nuestro proyecto dinámicamente, sin importar dónde se instale.
*   **`from typing import List, Dict, Any, Tuple`**
    *   **Uso:** "Type Hinting" (Anotaciones de tipo). No cambian cómo se ejecuta el código, pero le dicen a ti (y a tu editor como VS Code) qué tipo de dato debe ir en cada variable. Habilita el autocompletado y evita errores.
    *   **Ejemplo en el proyecto:** `def save_raw_to_parquet(data: List[Dict[str, Any]]) -> None:` (Se lee: la función recibe una Lista de Diccionarios y devuelve Nada).
*   **`import logging`**
    *   **Uso:** Módulo profesional para emitir mensajes (logs) en lugar de usar `print()`. Permite configurar niveles de severidad (INFO, WARNING, ERROR) y guardar los mensajes en archivos de texto, algo vital en aplicaciones productivas.
    *   **Ejemplo en el proyecto:** Usamos `logger.info("Extrayendo mes...")` en lugar de `print` para guardar el historial en `/logs/extraction.log`.
*   **`import time` / `import datetime` / `import calendar` / `from dateutil.relativedelta import relativedelta`**
    *   **Uso:** El manejo de tiempo es de los problemas más complejos en programación. `time` permite hacer pausas literales en el script; `datetime` y `calendar` manejan fechas; y `relativedelta` nos permite sumar o restar meses de forma inteligente (considerando años bisiestos y días variables del mes).
    *   **Ejemplo en el proyecto:** Transformar una fecha como "Enero 2024" al estándar UNIX Timestamp (segundos desde 1970) que exige la API.

### 3. Módulos Internos (Modularidad del código)

Son las importaciones que utilizamos para conectar nuestros propios archivos, cumpliendo el principio de separación de responsabilidades.

*   **`from core.config import config`**
    *   **Uso:** Importamos la instancia central que tiene nuestras variables de configuración para usarla en la extracción o el guardado de datos.
*   **`from core.logger import get_logger`**
    *   **Uso:** Función central para que cualquier archivo del proyecto pueda tener su propio registro de eventos sin reescribir configuración.
*   **`from extractor.client import StackExtractor`**, **`from analytics.processor import...`**
    *   **Uso:** En `main.py`, usamos estas importaciones para traer los diferentes "engranajes" y ensamblarlos en la máquina final que ejecuta el flujo de inicio a fin.

---


## 🌐 Fase 2: Aplicación Web "ShowDataAnalitys" (React + Vite)

Para visualizar el resultado de este pipeline y poder publicarlo en la nube (como Netlify) sin colapsar el navegador del usuario final, hemos implementado una **Static Data App** en la carpeta `/ShowDataAnalitys`.

Esta aplicación fue construida utilizando el patrón **MVC (Modelo-Vista-Controlador)** para garantizar su escalabilidad y fácil mantenimiento:

### 1. El Puente Backend-Frontend (Python)
El "Cerebro Analítico" de nuestro pipeline (`processor.py`) fue modificado para exportar la metadata procesada a un archivo hiper-ligero `dashboard_data.json` dentro de la carpeta pública del frontend. Este JSON contiene las agregaciones ya listas para graficar, aislando al frontend (React) de cualquier procesamiento matemático complejo.

### 2. Arquitectura MVC en React
- **Model (`src/models/dataService.ts`)**: Define el tipado fuerte de los datos (TypeScript) y expone la función asíncrona para consumir el `dashboard_data.json` de la carpeta pública de forma eficiente.
- **Controller (`src/hooks/useDashboardData.ts`)**: Un Custom Hook de React que orquesta la lógica de negocio. Extrae los lenguajes únicos, maneja los estados asíncronos (cargando, error) y controla el motor de filtrado global (por Lenguaje o búsqueda de texto libre).
- **View (`src/components/`)**: Componentes puramente visuales que reaccionan a los datos del controlador. Integramos 5 visualizaciones profesionales:
    - `<BubbleChartComponent />`: Gráfica interactiva de Burbujas (Tiempo vs Health Index vs Volumen) usando `recharts`.
    - `<TreemapChartComponent />`: Distribución jerárquica del volumen histórico.
    - `<RadarChartComponent />`: Análisis comparativo multidimensional (Volumen, Engagement, Salud).
    - `<WordCloudChartComponent />`: Nube de tecnologías basada en la popularidad global (`react-wordcloud`).
    - `<DataTableComponent />`: Tablero de datos crudos con capacidades de búsqueda en tiempo real.

### 🚀 Listo para Despliegue (Netlify)
La aplicación utiliza el ecosistema de Vite, lo que la hace ultra-rápida. Para desplegarla, simplemente al correr `npm run build` se empaqueta toda la lógica en una carpeta `/dist`, la cual consta únicamente de HTML, CSS, JavaScript estático y el pequeño archivo JSON. ¡Esta es la receta perfecta para un hosting de alto rendimiento y bajo costo en Netlify!

## TASK
Tareas: Dashboard Web "ShowDataAnalitys"
[x] Fase 1: Python Data Pipeline
[x] Modificar analytics/processor.py para exportar dashboard_data.json.
[x] Ejecutar main.py para validar la generación del JSON.
[x] Fase 2: Setup Frontend (React + Vite)
[x] Crear proyecto Vite ShowDataAnalitys usando React + TS.
[x] Instalar dependencias (recharts, react-wordcloud, tailwindcss para estilos rápidos si es necesario).
[x] Mover dashboard_data.json a la carpeta public/ de React (o importarlo estáticamente).
[x] Fase 3: Arquitectura MVC & Controladores
[x] Crear src/models/dataService.ts para leer la data.
[x] Crear src/hooks/useDashboardData.ts para transformar los datos para las gráficas.
[x] Fase 4: Componentes Visuales (Views)
[x] Crear componente de Tabla de Datos Filtrable.
[x] Crear <BubbleChart /> (Tiempo vs Engagement vs Volumen).
[x] Crear <TreemapChart /> (Volumen Histórico por Lenguaje).
[x] Crear <RadarChart /> (Análisis Multidimensional).
[x] Crear <WordCloudChart /> (Nube de 7 tags basada en volumen).
[x] Fase 5: Pruebas y Despliegue
[x] Ensamblar el Dashboard completo en App.tsx.
[x] Nota: La carpeta del proyecto Vite está lista. Debes correr npm install y npm run build en tu entorno para generar la carpeta dist para Netlify. 