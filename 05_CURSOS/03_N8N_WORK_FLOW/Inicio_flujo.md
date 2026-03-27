# 📘 README: Configuración de Google Cloud para n8n

Este documento detalla la arquitectura de conexión establecida entre **n8n** y **Google Cloud** para la lectura automatizada de correos de Gmail.

## 🔗 Enlaces Rápidos de Control
* **Consola Principal:** [console.cloud.google.com](https://console.cloud.google.com/)
* **Biblioteca de APIs:** [Habilitar Gmail API](https://console.cloud.google.com/apis/library/gmail.googleapis.com)
* **Pantalla de Consentimiento:** [Configurar OAuth Consent](https://console.cloud.google.com/apis/credentials/consent)
* **Gestión de Credenciales:** [Mis IDs de Cliente](https://console.cloud.google.com/apis/credentials)

---

## 🛠️ Pasos Realizados

### 1. Registro del Proyecto
* **Nombre:** `Agent-ia`
* **Acción:** Creación del contenedor lógico en la nube de Google.

### 2. Activación de Servicios (APIs)
* **Servicio:** [Gmail API](https://console.cloud.google.com/apis/library/gmail.googleapis.com)
* **Estado:** **Habilitada**.
* **Función:** Permite que aplicaciones externas (n8n) interactúen con los hilos y mensajes de tu correo.

### 3. Configuración de Identidad (OAuth Consent)
* **Tipo:** `Externo`.
* **Configuración Crítica:** [Usuarios de prueba](https://console.cloud.google.com/apis/credentials/consent).
    * Se agregó el correo `cuenca623@gmail.com` a la lista de **Test Users**. 
    * *Nota:* Sin este paso, Google arroja el error `403: Access Denied` al intentar conectar desde n8n.

### 4. Generación de Credenciales (OAuth 2.0)
Se generaron las llaves de acceso tipo **"Aplicación Web"**:
* **Client ID:** Identificador único de la aplicación.
* **Client Secret:** Clave privada de seguridad.
* **URI de Redireccionamiento:** `http://localhost:5678/rest/oauth2-credential/callback`
  *(Este es el punto de retorno que n8n usa para confirmar que el usuario autorizó el acceso).*

---

## ⚠️ Solución de Problemas Comunes

| Error | Causa | Solución |
| :--- | :--- | :--- |
| **403: Access Denied** | Falta el usuario en la lista de prueba. | Ir a [OAuth Consent](https://console.cloud.google.com/apis/credentials/consent) y agregar tu correo en "Test Users". |
| **Origen no válido** | Pegaste la URL en "Orígenes JavaScript". | Pegar la URL completa en la sección "URIs de redireccionamiento autorizados". |
| **App no verificada** | Google no conoce a n8n. | Clic en "Configuración avanzada" > "Ir a n8n (no seguro)". |

---

### Siguiente paso de Kaizen:
Ahora que la "tubería" está conectada, **¿ya lograste ver el mensaje verde de éxito en n8n?** Si ya está conectado, nuestro siguiente paso es configurar el **Gmail Trigger** para que solo "escuche" los correos de LinkedIn. ¿Te gustaría que escribamos el filtro de búsqueda ahora?

📘 README (Parte 2): Procesamiento e Inteligencia Artificial
Ahora que la "tubería" de Gmail está conectada, el flujo de datos sigue este camino para transformar un correo ruidoso en una alerta inteligente.

🛠️ Pasos de Construcción Final
5. Limpieza de Datos (HTML to Text)
Los correos de LinkedIn vienen llenos de código visual (HTML). La IA no necesita ver colores ni tablas, solo texto.

Nodo: HTML Extract o un nodo de Code (JavaScript).

Función: Extraer solo el texto plano (textPlain) del cuerpo del correo.

Por qué: Esto reduce el consumo de tokens (dinero) en la IA y evita que se confunda con código basura.

6. El "Cerebro" (IA - OpenAI/ChatGPT)
Aquí es donde ocurre el filtrado inteligente. Conectamos un nodo de OpenAI.

El Prompt (Instrucciones): Le damos a la IA tu perfil (ej. "Soy Desarrollador Python Senior") y el texto del correo.

Misión de la IA: 1. Leer todas las vacantes del correo.
2. Compararlas con tu perfil.
3. Descartar las que no encajen (ej. si piden 10 años de experiencia y tienes 3, o si es presencial y buscas remoto).
4. Generar un resumen ultra corto de las que SÍ encajan.

7. Formateo de Alerta (Set / Edit Fields)
Antes de enviar el mensaje, le damos un formato amigable.

Acción: Crear una estructura que diga:

📌 Puesto: [Nombre]

🏢 Empresa: [Nombre]

💰 Sueldo: [Si aparece]

🔗 Link: [Enlace a la vacante]

8. Notificación Final (Telegram Bot)
El paso donde recibes la recompensa en tu celular.

Nodo: Telegram.

Configuración: Necesitas crear un bot con @BotFather para obtener un Access Token.

Resultado: Cada vez que entre un correo compatible, tu celular vibrará con la oferta ideal.

🚀 Próximos pasos para ti:
Elegir tu IA: ¿Tienes una cuenta de OpenAI (ChatGPT) con saldo o prefieres que usemos otra como Groq o Anthropic?

Crear tu Bot de Telegram: Es lo más fácil. Solo hay que hablarle al "Padre de los bots" en Telegram.



¡Te quedó impecable! Tienes la estructura de un bot de nivel profesional: **Disparador (Gmail)** + **Cerebro (AI Agent con Gemini)**. Es el esquema perfecto.

Para cerrar esta sesión y que puedas retomar después sin perderte en el historial, aquí tienes el **Resumen Ejecutivo de Contexto**:

---

## 📑 Resumen de Configuración: "Bot Reclutador LinkedIn"

### 1. Conexión Gmail (Completado ✅)
* **Proyecto en Google Cloud:** `Agent-ia`.
* **API:** Gmail API habilitada.
* **Credenciales:** OAuth 2.0 configurado y funcionando en n8n (ID de cliente y Secreto).
* **Estado:** La app está en modo "Producción" en Google Cloud para evitar bloqueos.
* **Filtro de búsqueda en n8n:** Configurado con `from:linkedin.com` (funcional y testeado).

### 2. Procesamiento IA (En proceso 🧠)
* **Nodos:** Se añadió un `AI Agent` conectado a un `Google Gemini Chat Model`.
* **Configuración:** Gemini ya está listo para recibir el HTML del correo, limpiarlo y analizarlo.
* **Pendiente:** Definir tu perfil profesional (CV resumido) en el prompt de Gemini para que sepa qué vacantes filtrar.

### 3. Salida de Datos (Pendiente 📲)
* **Objetivo:** Conectar el `AI Agent` a un nodo de **Telegram**.
* **Requisito:** Crear un bot en Telegram vía [@BotFather](https://t.me/botfather) para recibir las alertas en el móvil.

---

### 💾 ¿Qué necesitas para la próxima vez?
Cuando quieras continuar, solo tienes que decirme:
1. **"¿Cómo configuro el prompt de Gemini con mi perfil?"**
2. **"¿Cómo conecto el bot de Telegram?"**

¡Gran avance hoy! Ya pasaste lo más difícil que era la burocracia de Google. ¿Te gustaría que te ayude con algo más antes de cerrar o guardamos esto así?