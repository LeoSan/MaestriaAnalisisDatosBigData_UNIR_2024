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

## Clase 4: Expresiones de sistema en n8n para flujos profesionales

**Resumen**
Domina las expresiones de sistema de n8n para construir flujos profesionales y fiables. Con ellas puedes leer datos del nodo actual, identificar cada ejecución, incorporar el nombre del workflow o usar la fecha actual. Todo con doble llave {{ }}, expresiones de JavaScript y con previsualización del resultado en tiempo real.

**¿Qué son y por qué importan las expresiones de sistema de n8n?**

Las expresiones de sistema te permiten inyectar datos dinámicos en cualquier campo. Así evitas valores fijos y documentas mejor cada paso.

Acceder a datos del nodo con $json.
Identificar la ejecución con $execution.id para auditorías y errores.
Obtener metadatos con $workflow.name.
Usar fecha y hora actuales con $now.
Referenciar nodos por nombre con $node['Nombre'] y la sintaxis moderna $item.json.

**¿Cómo acceder a los datos del nodo con $json?**

Cuando abres un campo en edit fields, activa "expressions" y usa doble llave.

Ejemplos usando los campos mensaje y prioridad definidos en edit fields:


{{ $json.mensaje }}
{{ $json.prioridad }}

$json apunta al nodo previo conectado.
Útil para leer los valores actuales sin configurar nada extra.

**¿Cómo identificar la ejecución con $execution?**

Necesitas un identificador único por corrida del flujo. Úsalo para logs, auditorías o rastreo de errores.


{{ $execution.id }}
Genera un ID único por ejecución.
Ideal para adjuntar en respuestas o en registros.

**¿Cómo obtener metadatos y la fecha actual con $workflow y $now?**

Incluye el nombre del workflow en mensajes o logs.


{{ $workflow.name }}
Trabaja con la fecha y hora actual. Puedes mostrarla en ISO o aplicar format.


{{ $now.toIso }}
{{ $now.format }}
Son expresiones de JavaScript, por lo que puedes encadenar métodos.
Visualiza a la derecha la previsualización del valor antes de guardar.

**¿Cómo referenciar nodos por nombre sin romper el flujo?**

Cuando insertas un nodo intermedio (por ejemplo, un set que añade categoría: IT), $json puede cambiar porque apunta al nodo directamente anterior. En cambio, $node['Nombre'] apunta por nombre y no se rompe al reordenar.

**¿Por qué $json puede fallar al insertar nodos intermedios?**

Si agregas un set entre el nodo "Editar" y tu campo actual, $json ya no es el mismo.

$json se actualiza al nodo inmediatamente anterior.
Un cambio en la cadena de nodos puede romper referencias como {{ $json.prioridad }}.

**¿Cómo usar $node['Editar'] y la sintaxis moderna con $item.json?**

Para apuntar al nodo "Editar" por nombre y leer prioridad:


{{ $node['Editar'].json.prioridad }}
En la sintaxis más moderna, se trabaja con $item y luego con json:


{{ $item.json.prioridad }}
En ambos casos verás el mismo valor cuando no hay nodos intermedios.
Con nodos añadidos, $node['Editar'] mantiene la referencia estable.


**¿Qué práctica recomiendan para flujos estables?**

Preferir $node['NombreDelNodo'] para datos críticos.
Usar $json cuando el orden de nodos no cambiará.
Documentar con $execution.id y $workflow.name en tus logs.
Normalizar fechas con $now.toIso.

**¿Cómo replicar el ejercicio y consolidar el aprendizaje?**

Configura un trigger manual, un edit fields con mensaje y prioridad, y un set final para ver valores. Luego:

Prueba {{ $json.prioridad }} y {{ $node['Editar'].json.prioridad }} en el set.
Inserta un set intermedio que añada categoría: IT.
Ejecuta el workflow y observa cómo $json se rompe mientras $node sigue correcto.
Añade {{ $execution.id }}, {{ $workflow.name }} y {{ $now.toIso }} a tus campos.


## Clase 5: Validación de mensajes y respuestas estructuradas con JavaScript


**Resumen**
Mejora la calidad de tus automatizaciones con expresiones de sistema y JavaScript: valida el contenido, clasifica la prioridad y devuelve una respuesta estructurada por webhook con trazabilidad. Verás cómo combinar el nodo IF, funciones como length e includes, la condición ternaria y campos del workflow para un flujo más dinámico y claro.

**¿Cómo validar mensaje y longitud con JavaScript en el nodo IF?**

Para evitar respuestas pobres, se comprueba que el mensaje no esté vacío y que tenga al menos 10 caracteres. Se elige la condición Y en el nodo IF y se aplica la función de JavaScript para medir la longitud con autocompletado al pulsar el punto.

Activa la condición Y: mensaje no vacío y longitud mínima.
Usa la función: mensaje.length para contar caracteres.
Compara como número: mayor que 10.
Ejecuta y verifica que la condición se cumple.
Ejemplo de lógica en la condición:


mensaje !== '' && mensaje.length > 10
Así te aseguras de filtrar mensajes demasiado cortos antes de seguir.

**¿Cómo detectar y asignar prioridad con condición ternaria?**

En Edit Fields, añade el campo Prioridad como expresión. Inserta el mensaje y aplica includes para detectar si contiene la palabra “urgente”. Luego usa la condición ternaria para etiquetar: alta o normal.

Convierte el campo a expresión con “=”.
Inserta el mensaje y aplica includes: busca “urgente”.
Devuelve “alta” o “normal” con la ternaria.
Ejemplo:


mensaje.includes('urgente') ? 'alta' : 'normal'
Si el texto no contiene “urgente”, la prioridad resultará normal.

**¿Cómo enriquecer la respuesta con fecha, flujo y ejecución para el webhook?**

Suma contexto a la respuesta agregando Fecha, Flujo y Ejecución_id. Trabaja con expresiones del sistema y devuelve un objeto claro. Esto aporta trazabilidad y mejora la lectura.

**¿Cómo generar la fecha con NOW y formato ISO?**

Crea el campo Fecha como texto y usa la variable de sistema NOW. Dale un formato legible con toISO.

Escribe “=” y abre llaves para activar la expresión.
Inserta NOW y convierte con toISO.
Ejemplo:


{{ $now.toISO() }}
Obtendrás la fecha actual en formato estándar, fácil de interpretar.

**¿Cómo identificar workflow y execution id en la respuesta?**

Añade el nombre del workflow y el identificador de ejecución. Cuando se ejecute, el id aparecerá automáticamente.

Campo Flujo: toma el nombre del workflow.
Campo ejecución_id: usa execution.id y define el tipo correcto.
Ejemplos:


{{ $workflow.name }}
{{ $execution.id }}
Si ves que ejecución_id sale como texto, cambia a número para mantener consistencia.

**¿Cómo construir el cuerpo JSON y probar con pin?**

Puedes mapear manualmente o devolver todo con JSON desde el nodo anterior. Si no dominas JavaScript, arrastra campo por campo y previsualiza.

Construye el objeto con: mensaje, prioridad, fecha, flujo, ejecución_id.
Alternativa avanzada: devolver el JSON completo del nodo anterior.
Usa botón derecho: pin para congelar datos y probar sin reenviar.
Luego unpin para volver a datos en vivo.
Activa Execute workflow para escuchar en modo test.
Observa que ejecución_id se incrementa en cada petición.
Maneja errores: indica cuando el mensaje está vacío o demasiado corto.
Ejemplo de respuesta estructurada para el webhook:


{
  "mensaje": "Crear tarea en proyecto del backend",
  "prioridad": "normal",
  "fecha": "2024-01-01T12:00:00.000Z",
  "flujo": "NombreDelWorkflow",
  "ejecucion_id": 270
}
Puntos clave que aplicarás de inmediato:

Expresiones de sistema para enriquecer datos.
Funciones de JavaScript: length, includes, toISO.
Condición ternaria para clasificar prioridad.
Campos de contexto: workflow.name y execution.id.
Buenas prácticas: prueba con pin/unpin, ajusta tipos y valida entradas.



```javascript
{{$json}}

{{ $execution }}

{{ $workflow }}

{{ $workflow.name }}

{{ $now }}

{{ $now.toISO() }}

{{ $now.format('dd-MM-yyyy') }}



{{ $nodeVersion }}

{{ $('Code').item.json.mensaje  }}
{{ $node['Code'].json.mensaje }}

{{ $('Webhook').item.json.body.mensaje }}

{{ $workflow.name }}
{{ $workflow.id }}

``` 

## Clase 6: Subworkflows en n8n para organizar flujos complejos

**Resumen**
Aprende qué es un subworkflow en N8N y cómo aplicarlo para mantener tu flujo principal limpio y legible. Entiende su lógica equivalente a una función: recibe un input, ejecuta una lógica y devuelve una respuesta. Además, conoce cómo se ejecuta con el nodo Execute to workflow y qué datos retorna para integrarlos sin fricción.

**¿Qué es un subworkflow en N8N y para qué sirve?**

Un subworkflow es simplemente otro workflow que se ejecuta desde uno principal. En la práctica, funciona como una función: recibe un input, ejecuta una lógica y devuelve una respuesta. Al aplicarlos, se pasa “de esto a esto otro”, es decir, el diseño se aclara y el flujo principal queda más limpio y legible.

**¿Cómo pensar en un subworkflow: como una función?**

Recibe un input claro.
Ejecuta una lógica definida.
Devuelve una respuesta concreta.


**¿Cómo se ejecuta y qué datos devuelve en N8N?**

En N8N, un subworkflow se ejecuta mediante el nodo Execute to workflow. Este nodo devuelve los datos del último nodo del subworkflow, lo que facilita encadenar resultados sin pasos intermedios innecesarios.

Nodo de ejecución: Execute to workflow.
Salida disponible: datos del último nodo.
Beneficio directo: el flujo principal se mantiene limpio y legible.


**¿Qué palabras clave y habilidades se destacan?**

Subworkflows: otro workflow que se ejecuta desde el principal.
Flujo principal limpio y legible: objetivo de organización.
N8N: plataforma donde se orquesta la ejecución.
Nodo Execute to workflow: ejecuta el subworkflow y expone la salida.
Datos del último nodo: respuesta consumible del subworkflow.
Automatización más profesional: resultado esperado al implementarlos.

## Clase 07: Subworkflows reutilizables con IA para clasificar mensajes