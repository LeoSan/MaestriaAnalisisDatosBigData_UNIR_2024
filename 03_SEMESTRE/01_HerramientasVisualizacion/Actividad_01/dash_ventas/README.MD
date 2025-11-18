# Estructura del proyecto

```
/mi-dashboard
│
├── node_modules/         <-- Paquetes Funcionales para el ambiente Node.js 
│
├── package.json          <-- Lista de Paquetes para la actividad
├── package-lock.json
│
├── server.js             <-- Servidor Express (Backend)
│
└── /public               <-- Repositorio Principal (Presentación)
    │
    ├── index.html        <-- Plantilla html que permite la visualización
    │
    ├── app.js            <-- Script Interactivo (Orquestador CLiente)
    │
    ├── /js
    │    ├── google-chart.js <-- Lógica para graficar google Chart (Grafico 1)
    │    └── d3-chart.js     <-- Lógica para graficar la funcionalidad de grafica deburbuja (Grafico 2)
    │    └── util.js         <-- Lógica modular y flexible permitiendo tener calculos, validaciones, llamados APi, para mantener la modularidad y flexibilidad. (Utilidades)
    └── /css
         ├── global.css      <-- Archivo de limpieza csss
         └── dash_venta.css  <-- Archivo para generar el estilo deseado visual para la actividad
```

# Pasos para iniciar un proyecto en Node.js


1. **Instalar Node.js**:
   - Descarga e instala Node.js desde su [sitio oficial](https://nodejs.org/).
   - Verifica la instalación ejecutando:
     ```bash
     node -v
     npm -v
     ```

2. **Inicializar el proyecto**:
   - Abre una terminal en el directorio del proyecto y ejecuta:
     ```bash
     npm init -y
     ```
     Esto creará un archivo `package.json` con la configuración básica del proyecto.

3. **Instalar dependencias**:
   - Para instalar dependencias necesarias, usa:
     ```bash
     npm install <nombre_paquete>
     ```
     Por ejemplo, para instalar Express:
     ```bash
     npm install express
     ```

4. **Crear el archivo principal**:
   - Crea un archivo principal, como `server.js`, y escribe el código inicial del servidor o aplicación.

5. **Ejecutar el proyecto**:
   - Ejecuta el archivo principal con Node.js:
     ```bash
     npm run dev 
     ```

6. **Configurar un archivo `.gitignore`**:
   - Asegúrate de incluir un archivo `.gitignore` para excluir archivos y carpetas innecesarias como `node_modules/`.


7. **Instalar herramientas adicionales**:
   - Instala nodemon para reiniciar automáticamente el servidor durante el desarrollo:
     ```bash
     npm install --save-dev nodemon
     ```
   - Ejecuta el proyecto con nodemon:
     ```bash
     npx nodemon index.js
     ```


# **Documentar el proyecto**:
   
   1. Descripción de la Actividad 
    - Esta actividad consiste en generar un mini dashboard para aplicar los conocimientos adquiridos en la materia de visualización de datos. 
    - Objetivos: 
            - 1. 
            - 2. 
            - 3.
            - 4.  
    - Desarrollo Front - Diseño Interfaz Dashboard 
            - Para el proyecto usaré colores Frescos y Energeticos de una paleta de colores imagen adjunta muestra colores: 
            - ![PALETA COLORES](public/images/image.png)
            - #4cb5f5 
            - #B7B8B6
            - #34675C
            - #B3C100

    - Desarrollo Back - Codificación  
        - Descripción:   
        - Paradigma: 
        - Patron de Diseño: