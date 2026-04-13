# Guía: Técnicas Avanzadas de Prompting

El **Prompt Engineering** es el arte de estructurar las instrucciones para que un modelo de lenguaje (LLM) entregue el resultado más preciso, lógico y útil. Aquí ampliamos las técnicas clave mencionadas en tu curso, con ejemplos y casos de uso.

---

## 1. Zero-Shot Prompting (Sin ejemplos)
Es la forma más básica de interactuar. Le pides a la IA que realice una tarea basándose únicamente en su conocimiento previo, sin darle ejemplos de referencia.

- **Definición:** Resolución directa de una tarea sin entrenamiento previo en el prompt.
- **Ejemplo:** *"Clasifica el siguiente mensaje como Positivo o Negativo: 'Me encanta el nuevo sistema de colas en n8n'."*
- **Ventaja:** Rápido y eficiente.
- **Limitación:** Puede fallar en formatos complejos o tareas muy específicas.

---

## 2. Few-Shot Prompting (Con pocos ejemplos)
También conocido a veces como *"Free-shot"* en contextos de orientación mínima. Consiste en proporcionar de 2 a 5 ejemplos de entrada y salida para que el modelo "aprenda" el patrón antes de responder.

- **Definición:** Variante con orientación basada en demostraciones breves.
- **Ejemplo:**
  > Pregunta: Gato -> Respuesta: Animal
  > Pregunta: Manzana -> Respuesta: Fruta
  > Pregunta: Kubernetes -> Respuesta: ...
- **Ventaja:** Muy efectivo para forzar un formato exacto (ej. devolver un JSON específico).
- **Uso ideal:** Cuando necesitas que la IA siga un estilo muy particular.

---

## 3. Chain of Thought - CoT (Cadena de Pensamiento)
Esta técnica obliga al modelo a "mostrar su trabajo". Se le pide explícitamente que desglose el problema en pasos lógicos antes de dar la respuesta final.

- **Definición:** Explicitación de los pasos intermedios de razonamiento.
- **Frase mágica:** *"Piensa paso a paso"* o *"Desglosa la lógica antes de responder"*.
- **Ejemplo:** *"Si tengo 3 nodos de Kubernetes y cada uno tiene 2 pods de n8n, pero quiero escalar a un total de 12 pods, ¿cuántos pods adicionales necesito por nodo? Piensa paso a paso."*
- **Ventaja:** Reduce drásticamente los errores lógicos y matemáticos.

---

## 4. Self-Consistency (Auto-consistencia)
Es una evolución de la Cadena de Pensamiento (CoT). El modelo genera múltiples caminos de razonamiento para la misma pregunta y luego selecciona la respuesta que aparece con más frecuencia (Votación por mayoría).

- **Definición:** Compara múltiples trayectorias de pensamiento y elige la más repetida/lógica.
- **Cómo funciona:** La IA genera 3 o 5 explicaciones diferentes para un problema. Si en 4 de ellas llega al resultado "X", se asume que "X" es la respuesta correcta.
- **Uso ideal:** Problemas de lógica compleja o depuración de código crítico.

---

## 5. Ventanas Largas de Contexto (Long Context Windows)
Los modelos actuales (como Gemini 1.5 Pro o Claude 3.5 Sonnet) permiten "ventanas" de contexto enormes (desde 128k hasta 2 millones de tokens).

- **Definición:** Capacidad de conservar miles de páginas de instrucciones y hechos sin olvidar el inicio de la conversación.
- **Importancia:** Permite subir manuales completos de n8n, toda tu estructura de directorios de Kubernetes y el historial de logs en un solo prompt.
- **Efecto "Nada-en-el-medio":** Los modelos modernos están optimizados para no perder información relevante aunque esté enterrada en medio de un texto enorme.

---

## 6. Comparativa Rápida

| Técnica | ¿Cuándo usarla? | Nivel de Precisión |
| :--- | :--- | :--- |
| **Zero-Shot** | Tareas simples y directas. | Media |
| **Few-Shot** | Formatos específicos o clasificación. | Alta |
| **CoT** | Lógica, matemáticas y resolución de problemas. | Muy Alta |
| **Self-Consistency**| Tareas críticas donde el error no es opción. | Máxima |
| **Long Context** | Análisis de múltiples archivos o libros. | Contextual |

---

> [!TIP]
> **Combinación Ganadora:** Para tus despliegues de n8n en Kubernetes, la mejor técnica suele ser **Few-Shot + CoT**. Le das un ejemplo de un YAML que ya funciona y le pides que genere el nuevo desglosando el razonamiento de los recursos (CPU/RAM).
