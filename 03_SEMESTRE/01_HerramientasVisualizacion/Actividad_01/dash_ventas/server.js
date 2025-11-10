import express from "express";

const app = express();
const PORT = 3000;

// Tu JSON de datos. (En el futuro esto vendría de una DB)
const data = [
  {
    producto: "Smartphone A",
    mes: "Enero",
    ventas: 120,
    ingresos: 24000,
    precio: 200,
  },
  {
    producto: "Smartphone B",
    mes: "Enero",
    ventas: 85,
    ingresos: 17000,
    precio: 200,
  },
  {
    producto: "Tablet X",
    mes: "Enero",
    ventas: 60,
    ingresos: 18000,
    precio: 300,
  },
  {
    producto: "Smartphone A",
    mes: "Febrero",
    ventas: 150,
    ingresos: 30000,
    precio: 200,
  },
  {
    producto: "Smartphone B",
    mes: "Febrero",
    ventas: 90,
    ingresos: 18000,
    precio: 200,
  },
  {
    producto: "Tablet X",
    mes: "Febrero",
    ventas: 70,
    ingresos: 21000,
    precio: 300,
  },
];

// --- TAREAS DEL SERVIDOR ---

// 1. Servir los archivos estáticos (HTML, CSS, JS) de la carpeta 'public'
// Esto es lo que permite que index.html se cargue.
app.use(express.static("public"));

// 2. Crear la API para simular la "fuente externa"
// Esto es lo que 'data-service.js' va a llamar.
app.get("/api/data", (req, res) => {
  console.log("Petición recibida en /api/data");
  res.json(data);
});

// 3. Iniciar el servidor
app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
