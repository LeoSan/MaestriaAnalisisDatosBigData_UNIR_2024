# Curso de Workflows Profesionales con n8n

| Detalle | Información |
| :--- | :--- |
| **Publicado el** | 21 Agosto 2025 |
| **Profesor** | Idir Ouhab |
| **Fecha de Inicio** | 01/003/2026 |
| **Fecha de Fin** |  |

> En este curso aprenderás a construir automatizaciones profesionales en n8n, dominando expresiones avanzadas, subworkflows, lógica de enrutamiento, conexiones con IA y casos prácticos de integración con herramientas externas

<div align="center">
  <img src="imagen-2.png" alt="Global Certificate" width="70%"  />
</div>

| Curso | Certificado |
| :--- | :---: |
| Curso de Automatizaciones con n8n | [Ver PDF](./diploma-n8n-lowcode.pdf) |


---

## Clase 1: Automatización profesional con n8n: estructura y mantenibilidad

**¿Qué es automatizar con n8n de forma profesional?**

Automatizar bien no es solo lograr que corra hoy. Es construir con criterio para volver sin miedo y mejorar. Si “da miedo tocarlo”, no está bien hecho. La diferencia está en cómo nombras, estructuras y validas cada paso para que el flujo sea claro a primera vista.

**¿Qué errores revelan un flujo mal hecho?**

Nodos sin nombre.
Todo mezclado.
Sin validaciones.
Es una bomba de tiempo.

**¿Qué define un flujo profesional en n8n?**

Nombres claros en cada nodo.
Estructura limpia y legible.
Uso de set para organizar datos.
Subflujos que separan responsabilidades.
Validaciones que previenen fallos.
¿Cómo será el proyecto del asistente interno inteligente?

Construirás un asistente interno inteligente que orquesta tareas clave con claridad y registro. La propuesta combina análisis con inteligencia artificial y control operativo para no perder nada en el camino.

**¿Qué hace el asistente de principio a fin?**

Recibe solicitudes.
Analiza con IA y entiende qué se pide.
Detecta si una solicitud es urgente.
Avisa a quien corresponda.
Deja registro de lo que pasó.

**¿Por qué la base técnica importa antes de avanzar?**

Porque “nada de eso sirve si la base es un caos”. Antes de construir, afianza lo esencial: nombres, estructura, set, subflujos y validaciones. Así podrás mantenerlo y escalarlo sin miedo a romper nada cuando vuelvas más adelante.

**¿Qué habilidades y conceptos practicarás para mantener y escalar?**

Te enfocarás en lo que hace que un flujo sea confiable a largo plazo. La consigna es que funcione hoy y que puedas mantenerlo, escalarlo e integrarlo después sin fricción.

**¿Qué desarrollarás paso a paso?**

- Nombrado claro de nodos.
- Estructura limpia del flujo.
- Validaciones en puntos críticos.
- Uso de set para preparar y ordenar datos.
- Subflujos para modular procesos.
- Análisis con inteligencia artificial.
- Detección de urgencia.
- Notificaciones al responsable correcto.
- Registro consistente de eventos.

## Clase 3: Configuración de webhook básico en n8n

Resumen
Un workflow simple pero bien estructurado en n8n puede ser tu base para automatizaciones sólidas: recibe una petición, valida los datos y responde de forma controlada. Aquí se explica cómo crear un webhook, configurar su método HTTP, probar con JSON, extraer campos con set o edit fields, validar con if y responder con respond to webhook. Además, verás trucos como pin data y el uso de expresiones JavaScript para añadir lógica.

**¿Qué es un webhook y cómo configurarlo en n8n?**

Un webhook es una URL que expone tu workflow al exterior. Al recibir una petición HTTP, se ejecuta como punto de entrada del asistente. El proceso comienza creando el workflow, renombrándolo con un nombre claro y añadiendo el trigger tipo webhook.

**¿Cómo elegir método HTTP y path en el webhook?**

Selecciona método según la operación. Para enviar datos: POST.
Define el path legible. Cambia el que viene aleatorio por uno como “Asistente Interna”.
Observa la composición de la URL: dominio, segmento de webhook test y tu path.

**¿Cuándo usar test URL o production URL?**

En desarrollo usa test URL. Se activa al pulsar listen for test events o execute workflow.
En producción activa el workflow con el botón hasta que esté en verde.
Mantén producción apagado durante desarrollo para evitar ejecuciones no deseadas.

**¿Qué modos de respuesta y streaming existen?**

Acción por defecto: inmediata. Responde al instante.
Cuando el último nodo haya acabado: espera al final del flujo.
Usar otro nodo para contestar: selecciona respond to webhook para responder desde un nodo específico.
Streaming: envía datos a medida que se generan, útil con un agente de IA.

**¿Cómo probar y responder solicitudes HTTP con control?**

Probar de forma segura evita errores comunes. Puedes usar Postman o la app RequestBin para enviar un JSON con campos como usuario y mensaje.

**¿Cómo escuchar eventos de test y evitar errores 4xx?**

Copia la URL del webhook en tu herramienta de pruebas.
Antes de enviar, activa listen for test events o ejecuta el workflow.
Si ves “The request of hook is not registered”: no estaba escuchando el modo test.

**¿Qué revisar en esquema y body del request?**

Abre el nodo y usa la vista esquema para ver cabeceras y datos recibidos.
Identifica el body con los campos usuario y mensaje.
Si no hay respuesta inicial, agrega respond to webhook y vuelve a ejecutar.

**¿Cómo responder con JSON y usar expresiones?**

Configura respond to webhook para enviar un JSON con claves como estado y usuario.
Para el caso exitoso: estado “recibido” y el usuario insertado con expresiones.
Para el caso de error: estado “error” y detalle “el mensaje está vacío”.
Duplica nodos con botón derecho o atajos control C y control V.

**¿Cómo validar y transformar datos antes de responder?**

Convertir y validar datos te permite controlar el flujo. Usa set o edit fields para extraer solo lo necesario y if para decidir la ruta.

**¿Cómo extraer y renombrar campos con set o edit fields?**

Arrastra desde body los campos usuario y mensaje.
Define el tipo de cada campo: string, number, booleano, objeto o array.
Renombra eliminando el prefijo “body.” para quedarte con “usuario” y “mensaje”.
Ejecuta y valida que el output contenga solo esos dos datos.

**¿Cómo congelar datos con pin data para iterar más rápido?**

Usa pin data para fijar datos en un nodo y evitar reenviar peticiones.
Activa o desactiva con clic derecho en el nodo y opción pin.
Atajo rápido: tecla P para congelar o descongelar.

**¿Cómo validar con if que el mensaje no esté vacío?**

Añade el nodo if y arrastra el campo mensaje.
Selecciona la condición de texto “no está vacío”.
Rama verdadera: continúa y responde con éxito.
Rama falsa: responde con error y un detalle claro.

**¿Listo para un reto rápido?**

Vuelve a edit fields y crea un campo prioridad.
Usa expresiones JavaScript: si el mensaje contiene “urgente”, asigna “alta”; de lo contrario, “baja”.
Prueba, toma una captura y compártela en los comentarios.