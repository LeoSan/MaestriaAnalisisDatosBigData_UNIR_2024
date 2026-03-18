# Guía de Instalación: n8n Community Edition en Mac (Local)

Esta guía explica cómo instalar la versión gratuita e ilimitada de n8n en tu Mac utilizando Docker. Este método es el recomendado porque es seguro, aislado y no interfiere con el resto de tu sistema.

## Requisitos Previos

Solo necesitas tener instalado **Docker Desktop** en tu Mac.

1.  Descarga Docker Desktop desde la página oficial: [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)
2.  Asegúrate de bajar la versión correcta para tu procesador:
    *   **Apple Silicon:** Si tienes un Mac con chip M1, M2, M3, etc.
    *   **Intel:** Si tienes un Mac más antiguo.
3.  Instálalo arrastrándolo a tu carpeta de Aplicaciones y ábrelo. Sabrás que está funcionando cuando veas el ícono de la ballena en la barra superior y diga "Engine running".

---

## Pasos de Instalación y Ejecución

### 1. Crear un Espacio de Almacenamiento (Volumen)

Para que tus flujos de trabajo (workflows) y credenciales no se borren cuando apagues n8n, debemos crear un volumen en Docker.

Abre la aplicación **Terminal** en tu Mac y ejecuta el siguiente comando:

```bash
docker volume create n8n_data
```

### 2. Iniciar n8n

En la misma Terminal, ejecuta el siguiente comando para descargar e iniciar n8n. Este comando conecta el volumen que creaste y expone la aplicación en el puerto `5678`.

```bash
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
```

### 3. Acceder a la Interfaz

Una vez que la Terminal muestre que el servidor ha iniciado (verás un mensaje indicando que el editor es accesible), abre tu navegador web y ve a la siguiente dirección:

```text
http://localhost:5678
```

La primera vez que ingreses, el sistema te pedirá crear una cuenta local de administrador. Esta cuenta es solo para tu instalación local y no requiere conexión a internet para validarse.

---

## Gestión del Servidor Local

*   **Para apagar n8n:** Ve a la ventana de la Terminal donde está corriendo el comando y presiona `Control + C`.
*   **Para volver a encenderlo:** Simplemente vuelve a abrir la Terminal y ejecuta el mismo comando del **Paso 2**. Toda tu información seguirá intacta gracias al volumen de Docker (`n8n_data`).


**Comandos para gestionar n8n en Docker**

-- Datos local : cuenca623@gmil.com
-- MMNleo2344%&/