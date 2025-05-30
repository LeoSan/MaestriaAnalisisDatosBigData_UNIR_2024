# Primera Clase 
> 26 Mayo 2025 - Presencial 

- Profesora: Adriana Cervantes Castillo 

# Resumen de Clase de IA: Clasificación y Árboles de Decisión

## Clasificación

* **Objetivo:** Asignar una etiqueta o clase a una nueva instancia basada en datos etiquetados previos.
* **Proceso:**
    1.  Datos etiquetados (ejemplos - instancias).
    2.  Entrenar un modelo (ej. ID3, K-NN).
    3.  Asignar una etiqueta a una nueva instancia.
    4.  Evaluación del modelo.

## Árbol de Decisión

* **Definición:** Estructura de datos jerárquica formada por ramas y nodos que representan decisiones y sus posibles resultados.
* **Algoritmo ID3:**
    1.  Seleccionar el conjunto de datos.
    2.  Definir datos de entrenamiento y prueba.
    3.  Calcular la entropía de la clase.
    4.  Calcular la ganancia de información para cada atributo.
    5.  Repetir hasta que todos los ejemplos pertenezcan a la misma clase, todos los atributos estén incluidos en un camino del árbol, o no queden más ejemplos.
* **Características del ID3:**
    * Basado en búsqueda greedy (el mejor atributo clasificador es el nodo raíz).
    * Construye árboles top-down (de arriba a abajo).
    * Utiliza selección de atributos basada en la teoría de la información (ganancia de información, reducción de entropía).
    * El atributo con mayor ganancia de información es el más útil para la clasificación.
* **Algoritmo CART (Árbol de Clasificación y Regresión):**
    * Construye un árbol dividiendo iterativamente los datos en subconjuntos más pequeños basado en una métrica de división óptima.
    * **Inicio:** El conjunto de datos inicial es la raíz.
    * **División recursiva:** Evalúa posibles divisiones usando un criterio específico, selecciona la división óptima y crea dos nodos hijos.
    * **Parada:** El proceso se detiene al cumplir ciertos criterios (profundidad máxima del árbol, número mínimo de ejemplos en nodos terminales).

## Métodos de Selección de Atributos

* Tasa de ganancia
* Índice Gini
* Ganancia de información

## Medidas de Rendimiento

* **Verdaderos positivos (TP):** El algoritmo clasifica como positivo y realmente son positivos.
* **Falsos positivos (FP):** El algoritmo clasifica como positivo pero realmente son negativos.
* **Verdaderos negativos (TN):** El algoritmo clasifica como negativo y realmente son negativos.
* **Falsos negativos (FN):** El algoritmo clasifica como negativo pero realmente son positivos.
* **Recall/Sensibilidad (TPR):** TP / (TP + FN) - Capacidad de detectar la clase positiva.
* **Especificidad:** TN / (TN + FP) - Capacidad de descartar instancias negativas.
* **Ratio de falsos positivos (FPR):** FP / (FP + TN) - Proporción de negativos clasificados como positivos.
* **Curva ROC (Receiver Operating Characteristic):** Grafica TPR vs. FPR a diferentes umbrales.
    * El área bajo la curva ROC (AUC) varía entre 0.5 (sin distinción) y 1 (clasificación perfecta).










