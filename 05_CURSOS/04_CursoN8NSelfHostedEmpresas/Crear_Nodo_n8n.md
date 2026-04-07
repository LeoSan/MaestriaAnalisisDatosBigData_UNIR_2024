# 👨‍🍳 Receta: Creación de Nodos Personalizados en n8n

Esta guía está diseñada paso a paso, como una receta de cocina, para que puedas crear, programar y probar tu propio nodo de n8n en tu Mac de manera secuencial y lógica.

Creamos nodo de forma Declarativa: ideal para conexiones directas y transformación simple de datos.

---

## 🛒 Ingredientes (Prerrequisitos)

Antes de empezar a cocinar, asegúrate de tener las herramientas preparadas en tu Mac:
1. **Node.js**: Se requiere una versión de largo soporte (LTS) como la **v20**.
   - *Tip:* Instálala usando `nvm install 22` ó con Homebrew `brew install node@22` y luego `brew link --overwrite node@22`. Te ahorrará muchísimos problemas.
2. **Git**: Para descargar la "masa base" oficial de n8n.
3. **Editor de código**: VS Code es el mejor cuchillo para este trabajo (idealmente con extensiones como `ESlint` y `Prettier`).

---

## 🥣 Paso 1: Preparar la Base (Clonar y Limpiar)

Vamos a descargar la plantilla vacía que nos da n8n y limpiar los ejemplos que trae por defecto para tener nuestro lienzo en blanco.

1. **Descarga la plantilla oficial:**
```bash
git clone https://github.com/n8n-io/n8n-nodes-starter mi-primer-nodo
cd mi-primer-nodo
```

2. **Limpia los sobrantes:**
Borra todo el contenido que viene dentro de las carpetas `nodes/` y `credentials/`. Queremos empezar desde cero. 
*⚠️ Muy importante:* Además de borrar los archivos, abre tu `package.json` y elimina las referencias a los viejos nodos y credenciales de ejemplo dentro del bloque `"n8n"`. El arreglo `"nodes"` y `"credentials"` debe quedar vacío por ahora.

3. **Ponle nombre a tu platillo:**
Abre el archivo `package.json` y cambia el atributo `"name"` por el nombre de tu propio proyecto. 
*Nota vital:* Para que n8n lo reconozca, **siempre debe empezar con `n8n-nodes-`**. 
> Ejemplo: `"name": "n8n-nodes-validador"`

---

## 🌪️ Paso 2: Mezclar los Ingredientes (Instalación)

Ahora vamos a instalar todas las herramientas y dependencias que requiere la masa para funcionar. Todo esto se hace en tu terminal, parado dentro del directorio de tu nodo.

```bash
npm install
npm install -g n8n-node-dev #lo instala de manera global para poder usarlo en cualquier parte de la terminal
```

> **⚠️ Posible Error al mezclar (`isolated-vm` falla):**
> Si al ejecutar `npm install` la terminal empieza a escupir texto rojo de errores (e.g. `node-gyp rebuild`), significa que tu versión actual de Node.js es demasiado moderna.
> *Solución rápida:* Verifica tu versión con `node -v`. Usa Node v20 (`nvm use 20` ó `brew link --overwrite node@20`), borra archivos corruptos si quedaron (`rm -rf node_modules package-lock.json`) y vuelve a ejecutar `npm install`.

---

## 👨‍💻 Paso 3: ¡A Cocinar! (Creando el Código del Nodo)

Llegó la hora de la lógica. Crearemos como ejemplo un **Validador de CURP Mexicana**.

1. **Prepara tu Ícono:**
   Crea una carpeta nueva en tu repositorio llamada `nodes/CurpValidator`.
   Busca una imagen en formato `.svg` o `.png` (la bandera de México, un DNI) y guárdala ahí dentro llamándola, por ejemplo, `curp-icon.svg`.

2. **Escribe el Código principal (TypeScript):**
   Dentro de esa misma carpeta (`nodes/CurpValidator/`), redacta un archivo llamado `CurpValidator.node.ts` con esta lógica:

```typescript
import {
	IExecuteFunctions,
	INodeExecutionData,
	INodeType,
	INodeTypeDescription,
	NodeOperationError,
} from 'n8n-workflow';

export class CurpValidator implements INodeType {
	description: INodeTypeDescription = {
		displayName: 'Validador de CURP',
		name: 'curpValidator',
		// Aquí usamos el parámetro 'icon' para vincular tu imagen personalizada
		icon: 'file:curp-icon.svg',
		group: ['transform'],
		version: 1,
		description: 'Valida si el formato de una CURP Mexicana es correcto',
		defaults: {
			name: 'Validador de CURP',
		},
		inputs: ['main'],
		outputs: ['main'],
		properties: [
			{
				displayName: 'CURP a Validar',
				name: 'curp',
				type: 'string',
				default: '',
				placeholder: 'Ej. GOZM930811HDFRNR08',
				description: 'La CURP de 18 caracteres a validar',
				required: true,
			},
		],
	};

	async execute(this: IExecuteFunctions): Promise<INodeExecutionData[][]> {
		const items = this.getInputData();
		const returnData: INodeExecutionData[] = [];

		// Regex estándar para validar la estructura de una CURP Mexicana
		const curpRegex = /^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$/;

		for (let itemIndex = 0; itemIndex < items.length; itemIndex++) {
			try {
				const curp = this.getNodeParameter('curp', itemIndex, '') as string;
				const curpLimpia = curp.trim().toUpperCase();

				// Validamos contra la expresión regular
				const isValid = curpRegex.test(curpLimpia);

				returnData.push({
					json: {
						curp: curpLimpia,
						es_valido: isValid,
						mensaje: isValid ? 'El formato de la CURP es VÁLIDO' : 'El formato de la CURP es INCORRECTO'
					},
					pairedItem: {
						item: itemIndex,
					},
				});
			} catch (error) {
				if (this.continueOnFail()) {
					items.push({ json: this.getInputData(itemIndex)[0].json, error, pairedItem: itemIndex });
				} else {
					if (error.context) {
						error.context.itemIndex = itemIndex;
						throw error;
					}
					throw new NodeOperationError(this.getNode(), error as Error, { itemIndex });
				}
			}
		}
		return [this.helpers.returnJsonArray(returnData.map(i => i.json))];
	}
}


```

3. **Agrega el nodo al menú general (`package.json`):**
   Tu aplicación necesita saber que este archivo fue creado. Abre de nuevo el `package.json` raíz y busca el contenedor de n8n para agregar la ruta del compilado (`.js`):
```json
  "n8n": {
    "n8nNodesApiVersion": 1,
    "credentials": [],
    "nodes": [
      "dist/nodes/CurpValidator/CurpValidator.node.js"
    ]
  }
```

---

## 🔥 Paso 4: Hornear el Código (Compilar a JavaScript)

El código anterior lo escribimos en TypeScript (TS), que es tu código en crudo. n8n solo corre el formato JavaScript (JS). Hay que hornearlo antes de consumirlo:

```bash
npm run build
```
*(Nota de Chef: Obligatorio repetir este paso/comando cada vez que modifiques tu código, o tus cambios no se probarán).*

---

## 🍽️ Paso 5: Servir la Mesa y Probar (Ejecutar Nativo)

La documentación oficial recomienda **no usar Docker mientras desarrollas**, sino ejecutar n8n nativo, pues permite conectar tus carpetas mediante *links* y no requiere apagar o prender contenedores en cada cambio de prueba.

1. **Instala n8n en tu computadora Mac globalmente:**
   ```bash
   npm install n8n -g
   ```

2. **Crea el enlace simbólico del proyecto local:**
   Asegúrate de seguir ubicado en la carpeta del repositorio (`mi-primer-nodo`) y enlaza tu desarrollo a npm:
   ```bash
   npm link
   ```

3. **Conecta tu nodo enlazado a los custom nodes de n8n:**
   ```bash
   mkdir -p ~/.n8n/custom
   cd ~/.n8n/custom
   npm init -y
   
   # ATENCIÓN: El link debe ser del nombre (name) que le hayas puesto a tu package.json en el Paso 1
   npm link n8n-nodes-validador
   ```

4. **Arranca n8n para probarlo:**
   ```bash
   n8n start
   ```
   *(🚑 **Plan B:** Si la terminal te arroja un error que dice `command not found: n8n`, significa que tu computadora no registró la instalación global del comando. Ejecuta **`npx n8n start`** en su lugar. Nota: puedes ejecutar este comando desde cualquier carpeta de tu terminal, no tienes que estar dentro de `.n8n`).*

   Visita `http://localhost:5678` en tu navegador de internet, busca el bloque "Validador de CURP" y ahí estará tu plato terminado con el ícono listo.
   
5. **Tip de pro: Desarrollo Constante (Watch):**
   Si vas a estar realizando ajustes continuos al código, mantenerte escribiendo `npm run build` en cada cambio es cansado. Para solucionarlo, abre otra pestaña en la terminal en tu carpeta `mi-primer-nodo` y corre:
   ```bash
   npm run build:watch
   ```
   Ese comando se queda "escuchando" indefinidamente, y cada que guardes un archivo TypeScript en tu editor, se encargará de hacer el build automáticamente. ¡Solo tendrás que reiniciar n8n para ver tus cambios!

---

## 🥡 Paso Opcional: Empacar "Para llevar" (Usando Docker)

Si fuiste firme en: *"Yo todo lo trabajo en entornos virtuales y Docker"*, o llegó la hora de mandar tu nodo a producción, n8n es igual de capaz. 

Para inyectar tu nodo horneado (`dist/`) dentro de un contenedor Docker local (e ignorar el paso 5), usa la estrategia de volúmenes en tu archivo base `docker-compose.yml`. Quedaría así:

```yaml 
#docker-compose.yml
services:
  n8n:
    image: n8nio/n8n
    ports:
      - "5678:5678"
    volumes:
      # Los configs de sistema
      - ~/.n8n:/home/node/.n8n
      # AQUÍ INYECTAS TU NODO A DOCKER
      # La estructura es -> Ruta/En/Tu/Servidor:/Ruta/En/El/Contenedor
      - /Ruta/Completa/En/Tu/Mac/mi-primer-nodo:/home/node/.n8n/custom/node_modules/n8n-nodes-validador
      #- /Users/leonard/Documents/Dev/react/mi-primer-nodo:/home/node/.n8n/custom/node_modules/n8n-nodes-leonard
```

**¿Dónde se usa este archivo?**
Hay dos escenarios comunes:
1. **Producción/Servidor**: Si alojas n8n en un VPS (Ej. DigitalOcean, AWS), añadirás este volumen a tu `docker-compose.yml` que ya tienes en producción, apuntándolo hacia la carpeta del servidor donde subiste tus archivos del nodo.
2. **Pruebas Locales (En tu Mac)**: Si solo quieres experimentar con Docker localmente en lugar del paso 5 nativo, crea este archivo `docker-compose.yml` en la raíz de tu proyecto `mi-primer-nodo`, ajusta la `/Ruta/Completa/En/Tu/Mac/...` por tu ruta real absoluta y arranca el entorno con:
   ```bash
   docker compose up -d
   ```

*Importante: Si actualizas tu código y el volumen está activo, los cambios se reflejan al compilar (`npm run build`), pero siempre deberás reiniciar el contenedor de Docker para que n8n cargue los nodos desde cero.*
