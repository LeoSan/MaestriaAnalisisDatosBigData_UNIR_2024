# 🤖 Documentación: Bot Reclutador Python (n8n + Gemini + MongoDB)

## 📌 Resumen de la Arquitectura
Este flujo automatizado conecta, piensa, limpia, almacena y notifica. Su objetivo es leer correos de plataformas de empleo (Adzuna/LinkedIn), usar IA para extraer solo vacantes relevantes ("Python Developer Mid"), guardar un registro histórico en una base de datos y enviar una alerta limpia al celular.

### 🔄 El Flujo (Pipeline)
1. **Conecta:** Gmail Trigger (Escucha nuevos correos).
2. **Piensa y Genera:** AI Agent con Gemini (Analiza, filtra y extrae datos en JSON).
3. **Limpia:** Code Node en JS (Procesa el JSON y maneja errores).
4. **Almacena:** MongoDB (Guarda la vacante como un documento).
5. **Notifica:** Telegram (Envía la alerta formateada al usuario).

---

## 🛠️ Paso a Paso y Tropiezos (Lecciones Aprendidas)

### Paso 1: El Disparador (Gmail Trigger)
* **Lo que hicimos:** Configuramos n8n para que escuche la bandeja de entrada buscando el remitente de Adzuna y palabras clave.
* **El Tropiezo:** Al principio no encontrábamos el cuerpo del correo (`textHtml`) porque los correos complejos lo esconden dentro del `payload`. 
* **La Solución:** Descubrimos que activando el nodo podíamos acceder directamente a la variable limpia `text` en el `OUTPUT`, simplificando la entrada para la IA.

### Paso 2: El Cerebro (AI Agent - Gemini)
* **Lo que hicimos:** Le dimos el rol de "Experto Reclutador IT" usando el *System Message* y le pasamos el texto del correo en el *User Prompt*. Le pedimos que devolviera un JSON estricto.
* **Los Tropiezos:**
    1. **El "Chat Trigger" fantasma:** n8n esperaba un chat en vivo. Tuvimos que cambiar el *Source* a `Define below` para que leyera nuestra instrucción estática.
    2. **El "Fallback Model":** El flujo marcaba error rojo porque estaba activada la opción de usar una segunda IA de respaldo que no existía. Lo apagamos.
    3. **Datos literales:** La IA leía el texto `{{ $json.text }}` en lugar del contenido real. Lo solucionamos arrastrando la "burbuja" de la variable directamente al cuadro de texto.

### Paso 3: Limpieza de Datos (Code JavaScript)
* **Lo que hicimos:** Usamos código para separar el JSON que entregó Gemini en variables individuales (`puesto`, `empresa`, `link`, etc.) para poder usarlas libremente.
* **El Tropiezo:** Al principio intentamos hacer un `JSON.parse()` a un texto, pero luego ajustamos el prompt de la IA y esta empezó a devolver un objeto real, lo que rompió el código.
* **La Solución (Nivel Pro):** Escribimos un nuevo código accediendo directo a `$json.output` e implementamos un bloque `try-catch`. Así, si la IA alguna vez falla o alucina, el código no se rompe; simplemente envía un mensaje de "Error de procesamiento", volviendo al bot **resiliente**.

### Paso 4: Almacenamiento (MongoDB Atlas)
* **Lo que hicimos:** Conectamos una base de datos NoSQL para tener un registro (CRM) de todas las vacantes detectadas.
* **Los Tropiezos:** 1. **Nodos equivocados:** Primero usamos *MongoDB Vector Store* y *MongoDB Tool*. Estos son para búsquedas complejas de IA, no para guardar datos simples.
    2. **Mala ubicación en el lienzo:** Conectamos la base de datos *dentro* del AI Agent (como un Tool). Esto impedía que MongoDB viera los datos limpios del nodo JavaScript.
* **La Solución:** Borramos las herramientas, usamos el nodo estándar de **MongoDB** (Insert Document) y lo colocamos en la **línea principal (Main Flow)**, justo entre la limpieza de datos y Telegram.

### Paso 5: Notificación (Telegram)
* **Lo que hicimos:** Creamos un bot con `@BotFather` y usamos su Token. 
* **El toque final:** Aplicamos formato Markdown para que la alerta llegue estructurada, con emojis, negritas y el enlace de postulación claro y directo.

---

## 🧠 Conceptos Clave Aprendidos
1. **Main Flow vs. Tools:** El flujo principal (línea verde) es la ruta de los datos. Los *Tools* son solo consultas temporales que hace la IA "en su escritorio" antes de dar un resultado.
2. **Memoria en IA:** La IA tiene amnesia por defecto. La memoria (Window Buffer) solo se usa para chats bidireccionales donde necesitas recordar el historial, no para procesar eventos aislados (como correos individuales).
3. **Resiliencia (`try-catch`):** Nunca confíes ciegamente en el formato de salida de una IA. Siempre prepara un plan B en el código para atrapar errores sin detener todo el sistema.

