# Guía Detallada: Instalación de n8n en Kubernetes con PostgreSQL y Redis

Esta guía está diseñada para llevarte paso a paso por el proceso de despliegue de n8n utilizando PostgreSQL como base de datos (para guardar configuraciones y flujos) y Redis (para gestión de colas/ejecuciones asíncronas). Está elaborada asumiendo que tienes conocimientos generales de sistemas, despliegues y contenedores, pero partiendo desde cero en **Kubernetes**.

---

## 1. Prerrequisitos (Lo que debes tener antes de empezar)

Para poder ejecutar esta guía en el futuro (ya sea en un entorno Azure AKS, AWS EKS, Google GKE o de forma local), necesitarás:

1.  **Un clúster de Kubernetes en ejecución**: El entorno físico o en la nube que hospedará y correrá tus servicios.
2.  **`kubectl` instalado en tu máquina**: Es la herramienta de terminal oficial. Funciona como un cliente remoto que utilizas para enviar comandos y órdenes hacia tu clúster de Kubernetes usando la API.
3.  **Configuración de Storage (Volúmenes)**: El clúster de Kubernetes debe estar preparado para asignar discos físicos (Persistent Volumes) para que la base de datos de datos no se borre al reiniciarse. En las nubes como Azure, esto suele venir listo por defecto.

---

## 2. Estructura de Directorios a Crear

En Kubernetes (a diferencia de Docker Compose), no se usa un solo archivo gigante, sino que es altamente recomendable y considerado una "buena práctica" organizar las configuraciones (llamadas manifiestos YAML) en una estructura de carpetas modular por cada servicio. 

Prepárate creando la siguiente estructura en tu proyecto:

```bash
n8n-k8s-deployment/
├── 00-namespaces/
│   └── namespace.yaml          # Define el entorno aislado
├── 01-config/
│   └── secrets.yaml            # Contraseñas y claves confidenciales
├── 02-redis/
│   ├── deployment.yaml         # Configuración del servidor Redis
│   └── service.yaml            # Configuración de red interna de Redis
├── 03-postgres/
│   ├── pvc.yaml                # Solicitud del disco duro (Persistencia)
│   ├── deployment.yaml         # Configuración del servidor Postgres
│   └── service.yaml            # Configuración de red interna de Postgres
└── 04-n8n/
    ├── deployment.yaml         # Aplicación principal de n8n
    └── service.yaml            # Exposición de red pública de n8n
```

---

## 3. Guía de Ejecución y Explicación de Comandos

A continuación, llenaremos los archivos indicados en la estructura y ejecutaremos el comando para "aplicarlos" a Kubernetes.

### Paso 1: Crear un `Namespace`

En Kubernetes, un Namespace es una partición o "carpeta" dentro del clúster general. Te permite aislar todo lo referente a este proyecto para que no se mezcle con otras aplicaciones que pudieras tener instaladas.

**Archivo: `00-namespaces/namespace.yaml`**
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: n8n-system
```

**Comando de Configuración:**
```bash
kubectl apply -f 00-namespaces/namespace.yaml
```
> **¿Qué hace este comando?**
> - **`kubectl`**: Interactúa con tu clúster.
> - **`apply`**: Indica que quieres crear (o actualizar si ya existe) el estado descrito.
> - **`-f`**: Significa `--filename`. Le dice al comando qué archivo leer.

---

### Paso 2: Crear `Secrets` (Gestión de Credenciales)

Necesitamos guardar contraseñas. Un objeto `Secret` en Kubernetes guarda esta info en formato codificado (Base64) y se inyecta de forma segura a los contenedores.

**Archivo: `01-config/secrets.yaml`**
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: n8n-secrets
  namespace: n8n-system # Aseguramos que viva en nuestro namespace
type: Opaque
stringData:
  POSTGRES_USER: "n8n_db_user"
  POSTGRES_PASSWORD: "SuperSecurePassword123"
  POSTGRES_DB: "n8n_database"
  N8N_ENCRYPTION_KEY: "tu-llave-secreta-para-n8n-generada-de-forma-aleatoria"
```

**Comando de Configuración:**
```bash
kubectl apply -f 01-config/secrets.yaml
```

---

### Paso 3: Desplegar la Base de Datos `PostgreSQL`

Requiere de tres conceptos en Kubernetes: Un **PersistentVolumeClaim** (pedir disco duro para que no se borre la data), un **Deployment** (el motor manejando el contenedor) y un **Service** (el cable de red para comunicarse).

**Archivo: `03-postgres/pvc.yaml`**
```yaml
apiVersion: v1
kind: PersistentVolumeClaim # Solicitud de Volumen Persistente
metadata:
  name: postgres-pvc
  namespace: n8n-system
spec:
  accessModes:
    - ReadWriteOnce # Permite lectura/escritura a un nodo
  resources:
    requests:
      storage: 10Gi # Tamaño del disco duro
```

**Archivo: `03-postgres/deployment.yaml`**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres
  namespace: n8n-system
spec:
  replicas: 1 # Cuántas bases de datos iguales quieres (solo 1 para Postgres)
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:16
        env:
        - name: POSTGRES_DB
          valueFrom:
            secretKeyRef:
              name: n8n-secrets
              key: POSTGRES_DB
        - name: POSTGRES_USER
          valueFrom:
            secretKeyRef:
              name: n8n-secrets
              key: POSTGRES_USER
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: n8n-secrets
              key: POSTGRES_PASSWORD
        ports:
        - containerPort: 5432
        volumeMounts:
        - name: postgres-data # Monta el disco duro virtual a la ruta del server
          mountPath: /var/lib/postgresql/data
      volumes:
      - name: postgres-data
        persistentVolumeClaim:
          claimName: postgres-pvc # El PVC que creamos antes
```

**Archivo: `03-postgres/service.yaml`**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: postgres # ESTE SERÁ el "host" de base de datos
  namespace: n8n-system
spec:
  selector:
    app: postgres
  ports:
  - port: 5432
    targetPort: 5432
```

**Comandos de Configuración:**
```bash
kubectl apply -f 03-postgres/pvc.yaml
kubectl apply -f 03-postgres/deployment.yaml
kubectl apply -f 03-postgres/service.yaml
```

---

### Paso 4: Desplegar `Redis`

Redis se usa en n8n como un "message broker". Si n8n recibe muchas cargas, usa Redis para ponerlas en cola (`queue mode`) de manera ordenada. Para Redis, generalmente en desarrollos iniciales, la memoria de solo caché está bien (no necesita volumen).

**Archivo: `02-redis/deployment.yaml`**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis
  namespace: n8n-system
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - name: redis
        image: redis:7-alpine
        ports:
        - containerPort: 6379
```

**Archivo: `02-redis/service.yaml`**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: redis # ESTE SERÁ el "host" del redis
  namespace: n8n-system
spec:
  selector:
    app: redis
  ports:
  - port: 6379
    targetPort: 6379
```

**Comandos de Configuración:**
```bash
kubectl apply -f 02-redis/deployment.yaml
kubectl apply -f 02-redis/service.yaml
```

---

### Paso 5: Desplegar la Aplicación `n8n`

Finalmente, conectamos n8n a los `Services` de PostgreSQL y Redis creados en pasos anteriores.

**Archivo: `04-n8n/deployment.yaml`**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: n8n
  namespace: n8n-system
spec:
  replicas: 1 # Como usamos redis y Postgres, aquí podríamos aumentar réplicas luego para escalar horizontálmente
  selector:
    matchLabels:
      app: n8n
  template:
    metadata:
      labels:
        app: n8n
    spec:
      containers:
      - name: n8n
        image: docker.n8n.io/n8nio/n8n:latest
        env:
        # DB Postgres
        - name: DB_TYPE
          value: "postgresdb"
        - name: DB_POSTGRESDB_HOST
          value: "postgres" # Nombre del Service de Postgres
        - name: DB_POSTGRESDB_PORT
          value: "5432"
        - name: DB_POSTGRESDB_DATABASE
          valueFrom:
            secretKeyRef:
              name: n8n-secrets
              key: POSTGRES_DB
        - name: DB_POSTGRESDB_USER
          valueFrom:
            secretKeyRef:
              name: n8n-secrets
              key: POSTGRES_USER
        - name: DB_POSTGRESDB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: n8n-secrets
              key: POSTGRES_PASSWORD
        
        # Redis y Colas
        - name: EXECUTIONS_MODE
          value: "queue"
        - name: QUEUE_BULL_REDIS_HOST
          value: "redis" # Nombre del Service de Redis
        - name: QUEUE_BULL_REDIS_PORT
          value: "6379"
          
        # Claves Generales
        - name: N8N_ENCRYPTION_KEY
          valueFrom:
            secretKeyRef:
              name: n8n-secrets
              key: N8N_ENCRYPTION_KEY
        ports:
        - containerPort: 5678
```

**Archivo: `04-n8n/service.yaml`**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: n8n-service
  namespace: n8n-system
spec:
  type: LoadBalancer # Ésta configuración en Azure/AWS ordena asignar una IP Pública real
  selector:
    app: n8n
  ports:
  - port: 80 # Puerto público a través de internet
    targetPort: 5678 # Puerto por el cual n8n está escuchando adentro
```

**Comandos de Configuración:**
```bash
kubectl apply -f 04-n8n/deployment.yaml
kubectl apply -f 04-n8n/service.yaml
```

---

## 4. Comandos "Cheat-Sheet" de Diagnóstico

Ya que es tu primer contacto con Kubernetes, no conocer los comandos de depuración te puede generar frustración. Aquí tienes los indispensables que deberás usar obligatoriamente para saber cómo va la cosa:

- **Saber si todo arrancó correctamente:**
  ```bash
  kubectl get pods -n n8n-system
  ```
  *(Deberías ver `n8n`, `postgres`, y `redis`. Asegúrate de que bajo la columna "Status" digan `Running`)*

- **Buscar en qué IP se encuentra publicado tu n8n (o porqué puerto):**
  ```bash
  kubectl get service -n n8n-system
  ```
  *(Busca tu servicio `n8n-service` e identifícalo bajo la columna `EXTERNAL-IP`. Esta IP es la que pondrás en tu navegador Chrome. Nota: Se demorará 2~5 minutos en que Azure/AWS te generen la IP, mientras tanto dirá `<pending>`.*

- **Ver la consola (Logs) de n8n para ver errores de la base de datos o Redis:**
  ```bash
  kubectl logs deployment/n8n -n n8n-system -f
  ```
  *(El `-f` significa "follow". Verás cómo se va escribiendo en tiempo real toda la información de encendido y errores. Se sale de este modo apretando `Ctrl + C`)*

- **Para borrar tu instalación completa y empezar de nuevo con solo un comando (Botón de pánico):**
  ```bash
  kubectl delete namespace n8n-system
  ```
  *(Esto borra la carpeta base del proyecto que hicimos en el paso 1, y Kubernetes en cascada reciclará el LoadBalancer de AWS/Azure, destruirá la base de datos, el redis, el volumen y las contraseñas. Limpieza automática total).*
