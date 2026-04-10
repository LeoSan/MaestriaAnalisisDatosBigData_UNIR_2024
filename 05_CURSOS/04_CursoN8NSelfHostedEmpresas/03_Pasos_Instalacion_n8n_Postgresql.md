# Pasos de Instalación de n8n con PostgreSQL usando Docker Compose

Este documento detalla el proceso para desplegar una instancia de **n8n** (versión 1.106) utilizando **PostgreSQL 16** como motor de persistencia de base de datos. 

---

## 1. Objetivo
Lograr una instalación robusta y persistente de n8n en un entorno local (macOS) utilizando contenedores, permitiendo que todos los flujos y configuraciones se guarden en una base de datos externa en lugar del archivo SQLite por defecto.

## 2. Requisitos Previos

Para completar esta instalación, asegúrate de tener lo siguiente en tu MAC:

1.  **Docker Desktop para Mac**: [Descargar e instalar](https://www.docker.com/products/docker-desktop/).
2.  **Terminal**: iTerm2, Terminal.app o el terminal integrado de VS Code.
3.  **Docker Compose**: Incluido con Docker Desktop. Verifica con:
    ```bash
    docker compose version
    ```
4.  **Permisos de Administrador**: Para ejecutar comandos de Docker y crear carpetas.

---

## 3. Estructura del Proyecto

Dentro de tu directorio de curso, hemos creado la siguiente estructura:

```text
n8n-deployment/
├── .env                # Archivo secreto con credenciales
└── docker-compose.yml   # Manifiesto de orquestación de servicios
```

> [!IMPORTANT]
> El archivo `.env` es fundamental para no exponer contraseñas directamente en el código del manifiesto de Docker.

---

## 4. Configuración de Archivos

### A. El archivo `.env`
Este archivo define las variables que usarán ambos contenedores. Hemos configurado valores por defecto seguros para el ejercicio:

*   **POSTGRES_USER**: admin
*   **POSTGRES_DB**: n8n_db
*   **GENERIC_TIMEZONE**: America/Mexico_City

### B. El archivo `docker-compose.yml`
El manifiesto define dos servicios principales:

1.  **postgres**: Utiliza la imagen `postgres:16-alpine` (ligera y segura).
2.  **n8n**: Utiliza la versión `1.106.1`. Depende de que Postgres esté "saludable" (`healthcheck`) antes de iniciar.

### C. Desglose detallado del Manifiesto (docker-compose.yml)

Para entender qué está pasando "detrás de cámaras", aquí tienes los elementos más resaltantes:

| Elemento | Función Esencial |
| :--- | :--- |
| **`version: '3.8'`** | Define la compatibilidad del manifiesto con las funciones modernas de Docker. |
| **`image`** | Indica la imagen oficial y versión exacta. Usar versiones fijas (como `1.106.1`) evita sorpresas por actualizaciones automáticas. |
| **`environment`** | Inyecta las variables del archivo `.env`. Esto mantiene tus contraseñas seguras y fuera del código principal. |
| **`volumes`** | Garantiza la **persistencia**. Sin esto, al borrar el contenedor perderías todos tus workflows y usuarios. |
| **`healthcheck`** | Función que monitorea si Postgres está realmente listo para recibir datos, no solo si el proceso arrancó. |
| **`depends_on`** | Establece el orden de encendido: n8n espera pacientemente a que Postgres esté **saludable** antes de intentar conectarse. |
| **`ports`** | Mapea el puerto del contenedor al de tu MAC. `5678:5678` significa que el puerto 5678 de tu máquina se conecta directamente al de n8n. |

---

## 5. Pasos de Instalación

Sigue estos pasos en tu terminal:

### Paso 1: Navegar al directorio
```bash
cd /Users/leonard/Documents/Dev/MaestriaAnalisisDatosBigData_UNIR_2024/05_CURSOS/04_CursoN8NSelfHostedEmpresas/n8n-deployment
```

### Paso 2: Levantar los servicios
Ejecuta el siguiente comando para iniciar la descarga de imágenes y el arranque en segundo plano:

```bash
docker compose up -d
```

### Paso 3: Verificar logs (Opcional)
Para confirmar que n8n se conectó correctamente a la base de datos:

```bash
docker compose logs -f n8n
```
*Busca una línea que diga: "n8n ready. Welcome to n8n!"*

---

## 6. Verificación y Acceso

1.  **Acceso Web**: Abre tu navegador en [http://localhost:15010](http://localhost:15010).
2.  **Registro Inicial**: Crea tu cuenta de propietario (email y password). Estos datos se guardarán automáticamente en Postgres.
3.  **Verificación en Base de Datos**:
    *   Usa un cliente como DBeaver o el explorador de BD de tu IDE.
    *   Host: `localhost` | Port: `5432` | User: `admin` | Pass: `admin` | DB: `n8n_db`.
    *   Refresca las tablas y verás las tablas creadas por n8n (`user_entity`, `workflow_entity`, etc.).

---

## 7. Comandos Útiles

| Tarea | Comando |
| :--- | :--- |
| Detener n8n | `docker compose stop` |
| Borrar contenedores (mantiene datos) | `docker compose down -v` |
|Ver logs de postgresql | `docker compose logs postgres` |
|Ver directamente la bd | `docker exec -it postgres psql -U admin -d n8n_db` |
| Ver estado | `docker compose ps` |
| Ver logs de BD | `docker compose logs postgres` |

> [!TIP]
> Si deseas cambiar la versión de n8n en el futuro, solo edita la línea `image: n8nio/n8n:1.106.1` en el archivo `docker-compose.yml` y ejecuta `docker compose up -d` nuevamente.
