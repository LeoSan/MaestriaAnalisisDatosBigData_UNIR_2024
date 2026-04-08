# 👨‍🍳 Receta: El Nodo Programático (Estilo "Cuchillo de Chef") 🔪

Esta receta es para cuando la "comida rápida" (modo declarativo) no es suficiente y necesitas control total sobre la cocina. Pasaremos de rellenar formularios a escribir la lógica pura en JavaScript/TypeScript usando la función `execute`.

---

## 🧐 ¿Por qué usar el estilo Programático?

| Estilo Declarativo (Standard) | Estilo Programático (Chef) |
| :--- | :--- |
| **Rápido:** Defines la API en el `routing`. | **Flexible:** Controlas cada paso con código. |
| **Rígido:** Difícil de manejar respuestas complejas. | **Poderoso:** Manejas bucles, transformaciones y errores a medida. |
| **Automático:** n8n hace la petición por ti. | **Manual:** Tú disparas la petición (`httprequest`). |

> [!TIP]
> Úsalo cuando la API que estás conectando tiene respuestas "feas", requiere múltiples pasos lógicos, o cuando necesitas validar datos antes de enviarlos.

---

## 🥣 Paso 1: Limpiar la mesa (Preparación del `Description`)

Para que un nodo sea programático, debemos **eliminar el automatismo**. 

1. Abre tu archivo `.node.ts`.
2. En la sección `properties`, **elimina** cualquier referencia a `routing`.
3. El `routing` lo hacíamos así (esto se debe BORRAR):
   ```typescript
   // ❌ ELIMINAR ESTO:
   // routing: { request: { method: 'GET', url: '/v1/user' } }
   ```
4. Ahora las propiedades solo sirven para capturar datos del usuario (inputs), no para hacer la llamada.

---

## 👨‍💻 Paso 2: La Función `execute` (El Motor)

Aquí es donde ocurre la magia. Copia este esqueleto y vamos a desglosarlo:

```typescript
async execute(this: IExecuteFunctions): Promise<INodeExecutionData[][]> {
    // 1. Obtener los ingredientes (datos del nodo anterior)
    const items = this.getInputData();
    const returnData: INodeExecutionData[] = [];

    // 2. Procesar cada "plato" (item) que llega
    for (let i = 0; i < items.length; i++) {
        try {
            // 3. Extraer parámetros del formulario (UI)
            const email = this.getNodeParameter('email', i) as string;

            // 4. Pedir la llave de la despensa (Credenciales)
            const credentials = await this.getCredentials('miApiCredencial');
            const apiKey = credentials?.apiKey as string;

            // 5. ¡A cocinar! (Hacer la petición HTTP manual)
            const response = await this.helpers.httprequest({
                method: 'GET',
                url: 'https://api.verificador.com/v1/validar',
                qs: { 
                    email: email, 
                    key: apiKey 
                },
                headers: { 
                    'Accept': 'application/json' 
                },
                json: true, // Esto parsea el JSON automáticamente
            });

            // 6. Preparar el plato para servir (Formatear el Output)
            // Si la API devuelve un array, iteramos; si no, lo envolvemos en uno.
            const results = Array.isArray(response) ? response : [response];

            for (const result of results) {
                returnData.push({
                    json: {
                        email: email,
                        valido: result.status === 'valid',
                        score: result.reputation_score,
                    },
                    pairedItem: i, // Mantiene la conexión con el input original
                });
            }

        } catch (error) {
            // 7. Si algo se quema, manejar el error
            if (this.continueOnFail()) {
                returnData.push({ json: { error: error.message }, pairedItem: i });
                continue;
            }
            throw new NodeOperationError(this.getNode(), error as Error, { itemIndex: i });
        }
    }

    // 8. Entregar el pedido
    return [returnData];
}
```

---

## 🔑 Claves del Chef (Conceptos Importantes)

### 1. `this.getInputData()`
Es tu carrito de compras. Contiene todos los datos que vienen del nodo anterior. Siempre debemos iterar sobre ellos para no perder información.

### 2. `this.getCredentials('Nombre')`
n8n busca las credenciales que el usuario configuró. El nombre dentro del paréntesis debe coincidir **exactamente** con el `name` definido en tu archivo de credenciales.

### 3. `this.helpers.httprequest`
Es tu herramienta multiusos. Sustituye al `routing`. 
*   **qs:** Query Strings (`?email=...`).
*   **body:** Datos para POST/PUT.
*   **json: true:** Muy importante para que n8n entienda que la respuesta es un objeto y no texto plano.

### 4. `returnData` y `pairedItem`
n8n espera que devuelvas un array de objetos con una propiedad `json`.
El `pairedItem: i` es vital: le dice a n8n "esta salida corresponde a este ingrediente de entrada", permitiendo que los resultados se mapeen correctamente en el editor.

---

## ⚠️ Errores Típicos (Evita que se queme el plato)

1.  **Mala conexión de credenciales:** Si en el código pides `getCredentials('ApiKeyCamel')` pero en tu archivo de credenciales el nombre es `apiKeyCamel` (minúscula), fallará. ¡Ojo con las mayúsculas!
2.  **Duplicidad:** Si dejas `routing` en la descripción Y además usas `httprequest` en `execute`, el nodo podría intentar hacer dos llamadas o confundirse. **Limpia siempre el Description**.
3.  **No retornar nada:** Si el bucle termina y no haces `return [returnData]`, n8n mostrará un error de ejecución.

---

## 🚚 Paso 3: Entrega y Prueba

Una vez terminada la lógica, el proceso es el mismo de siempre pero asegúrate de limpiar:

1.  **Build:** `npm run build` (para pasar de TS a JS).
2.  **Link (si es necesario):** `npm link`.
3.  **Reiniciar:** Detén n8n y vuelve a lanzarlo (`npx n8n start`).
4.  **Test:** Añade un "Trigger Manual", conecta tu nuevo nodo, pon un email de prueba y ¡voilà!

> [!IMPORTANT]
> Si el output no sale como esperas, usa `console.log(response)` antes del paso 6 para ver en la terminal qué te está respondiendo la API exactamente.
