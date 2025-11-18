import express from "express";
import path from "path";
import fs from "fs/promises";
import dotenv from "dotenv";

// Cargo las variables de entorno del archivo .env
dotenv.config(); 

// __dirname no está disponible directamente con ES Modules, lo creamos
import { fileURLToPath } from "url";
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 3000;
// Obtener el nombre del archivo del .env, con un fallback por si no se define
const salesDataFilename = process.env.SALES_DATA_FILENAME || 'ventas.json';

// 1. Servir los archivos estáticos (HTML, CSS, JS, imágenes, ¡y el JSON!) de la carpeta 'public'
app.use(express.static(path.join(__dirname, "public")));

// 2. Genero la API para leer el JSON desde el archivo
app.get("/api/data", async (req, res) => {
    console.log("Petición recibida en /api/data");
    const filePath = path.join(__dirname, "public", "datos", salesDataFilename);
    console.log(`Intentando leer datos de: ${filePath}`);

    try {
        // Leo el archivo de forma asíncrona
        const data = await fs.readFile(filePath, "utf8");

        // Convierto el contenido JSON y enviarlo como respuesta
        res.json(JSON.parse(data));
        console.log("Datos de ventas.json servidos exitosamente.");
    } catch (error) {
        console.error("Error al leer ventas.json:", error);
        res.status(500).json({
            error: "No se pudieron obtener los datos de ventas. ❌",
        });
    }
});

// 3. Iniciar el servidor
app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
