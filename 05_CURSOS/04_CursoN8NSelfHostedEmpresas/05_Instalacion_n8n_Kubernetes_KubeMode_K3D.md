# Guía Detallada: Instalación de n8n en Kubernetes para un Entorno Escalable (Kube/Queue Mode) con K3D, PostgreSQL y Redis

En esta guía abordaremos un escenario más avanzado y cercano a producción. Montaremos un clúster local ligero utilizando **K3D** y desplegaremos la arquitectura escalable de n8n.

En este modelo (comúnmente llamado **Queue Mode**), hay una separación de responsabilidades:
1. Un **Nodo Principal (Main)** que atiende la interfaz web y programa (pone en cola) las tareas.
2. Múltiples **Nodos Hijos (Workers)** que están escuchando la cola y realizan el trabajo real de fondo (cálculos, conexiones a APIs).
3. **Redis** gestiona las colas de las tareas generadas por el Main.
4. **PostgreSQL** respalda las credenciales, configuraciones de los workflows y el historial.

Además, expondremos el portal usando un **Ingress**, un recurso nativo de Kubernetes que actúa como un proxy inverso.

---

## 1. Prerrequisitos de tu Máquina

1. **Docker instalado y en ejecución.**
2. **K3D instalado**: Es una herramienta ultraligera para crear y borrar clústeres Kubernetes completos en segundos dentro de contenedores de Docker.
   - Mac/Linux: `curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash`
   - o vía Homebrew en Mac: `brew install k3d`
3. **`kubectl`** instalado.

---

## 2. Creación del Clúster Kuberntes con K3D

Vamos a crear el clúster asegurándonos de abrir y redirigir los puertos de red de nuestra máquina anfitriona hacia el "Load Balancer" interno (Ingress) de K3D.

Ejecuta el siguiente comando en tu terminal:

```bash
k3d cluster create mi-cluster-n8n \
  --servers 1 \
  --agents 2 \
  -p "8080:80@loadbalancer"
```

> **Explicación del Comando:**
> - `create mi-cluster-n8n`: Nombra nuestro nuevo clúster de prueba.
> - `--servers 1 --agents 2`: Levanta 1 "cerebro" maestro y 2 "trabajadores" Kubernetes (simula 3 computadoras físicas).
> - `-p "8080:80@loadbalancer"`: Abre el puerto 8080 en el "localhost" de tu Mac y lo conecta directo al puerto 80 del controlador Ingress dentro del clúster. Esto es vital para el paso final.

Verifica que el clúster está listo:
```bash
kubectl cluster-info
kubectl get nodes
```

---

## 3. Estructura del Proyecto y Manifiestos a Crear

Diseña la siguiente estructura de carpetas en tu proyecto Kuberetes:

```text
n8n-k3d/
├── 01-config/
│   ├── configmap.yaml
│   └── secret.yaml
├── 02-data/
│   ├── redis.yaml
│   ├── postgres.yaml
│   └── pvc.yaml
├── 03-app/
│   ├── n8n-main.yaml
│   ├── n8n-worker.yaml
│   └── n8n-service.yaml
└── 04-networking/
    └── ingress.yaml
```

---

## 4. Definición de Recursos Clave (Archivos YAML)

### A. Configuraciones y Secretos (`01-config/`)

Creamos el **ConfigMap** (para variables estáticas) y el **Secret** (para contraseñas). El separar estos recursos es vital para una gestión segura.

**Archivo: `01-config/configmap.yaml`**
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: n8n-env
data:
  DB_TYPE: "postgresdb"
  DB_POSTGRESDB_HOST: "postgres-svc"
  DB_POSTGRESDB_PORT: "5432"
  EXECUTIONS_MODE: "queue" # <- Esto activa la delegación de tareas a los Workers
  QUEUE_BULL_REDIS_HOST: "redis-svc"
  QUEUE_BULL_REDIS_PORT: "6379"
  N8N_PORT: "5678"
```

**Archivo: `01-config/secret.yaml`**
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: n8n-credentials
type: Opaque
stringData:
  DB_POSTGRESDB_DATABASE: "n8n_prod"
  DB_POSTGRESDB_USER: "n8n_user"
  DB_POSTGRESDB_PASSWORD: "Mypassword123"
  N8N_ENCRYPTION_KEY: "llave-de-encriptacion-secreta-larga"
```

### B. Dependencias de Datos (`02-data/`)

**Archivo: `02-data/pvc.yaml`** (Reservando el almacenamiento de la Base de Datos)
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: postgres-disk
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
```

**Archivo: `02-data/postgres.yaml`**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres
spec:
  replicas: 1
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
        envFrom:
        - secretRef:
            name: n8n-credentials
        - configMapRef:
            name: n8n-env
        # Las variables secretas se mezclan aquí por convención pero deben mapearse exactas o usar variables nativas de PG:
        env:
        - name: POSTGRES_DB
          valueFrom: { secretKeyRef: { name: n8n-credentials, key: DB_POSTGRESDB_DATABASE } }
        - name: POSTGRES_USER
          valueFrom: { secretKeyRef: { name: n8n-credentials, key: DB_POSTGRESDB_USER } }
        - name: POSTGRES_PASSWORD
          valueFrom: { secretKeyRef: { name: n8n-credentials, key: DB_POSTGRESDB_PASSWORD } }
        volumeMounts:
        - name: disk
          mountPath: /var/lib/postgresql/data
      volumes:
      - name: disk
        persistentVolumeClaim:
          claimName: postgres-disk
---
apiVersion: v1
kind: Service
metadata:
  name: postgres-svc
spec:
  selector:
    app: postgres
  ports:
  - port: 5432
```

**Archivo: `02-data/redis.yaml`**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis
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
---
apiVersion: v1
kind: Service
metadata:
  name: redis-svc
spec:
  selector:
    app: redis
  ports:
  - port: 6379
```

### C. Despliegue de n8n Escalable (`03-app/`)

Aquí la magia de Kubernetes entra en acción: El nodo principal ("Main") maneja la interfaz y el "Worker" ejecuta las tareas. Ambos leen los secretos compartidos.

**Archivo: `03-app/n8n-main.yaml`**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: n8n-main
spec:
  replicas: 1 # Si pones más de 1 aquí tendrías un load-balancer, pero n8n prefiere que escales WORKERS.
  selector:
    matchLabels:
      app: n8n-main
  template:
    metadata:
      labels:
        app: n8n-main
    spec:
      containers:
      - name: n8n
        image: docker.n8n.io/n8nio/n8n:latest
        envFrom:
        - configMapRef:
            name: n8n-env
        - secretRef:
            name: n8n-credentials
        ports:
        - containerPort: 5678
```

**Archivo: `03-app/n8n-worker.yaml`**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: n8n-worker
spec:
  replicas: 2 # ¡AQUÍ ESTÁ LA ESCALABILIDAD! Tenemos 2 workers en paralelo procesando.
  selector:
    matchLabels:
      app: n8n-worker
  template:
    metadata:
      labels:
        app: n8n-worker
    spec:
      containers:
      - name: worker
        image: docker.n8n.io/n8nio/n8n:latest
        command: ["n8n", "worker"] # Este comando transforma la imagen web en un esclavo puro de red
        envFrom:
        - configMapRef:
            name: n8n-env
        - secretRef:
            name: n8n-credentials
```

**Archivo: `03-app/n8n-service.yaml`** (El servicio para llegar al Main UI)
```yaml
apiVersion: v1
kind: Service
metadata:
  name: n8n-web-svc
spec:
  selector:
    app: n8n-main
  ports:
  - port: 80
    targetPort: 5678
```

### D. Acceso Exponiendo con Ingress (`04-networking/`)

K3d viene con **Traefik** como ingress controller pre-instalado. Vamos a usarlo para rutear peticiones HTTP al `n8n-web-svc`.

**Archivo: `04-networking/ingress.yaml`**
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: n8n-ingress
  annotations:
    ingress.kubernetes.io/ssl-redirect: "false"
spec:
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: n8n-web-svc
            port:
              number: 80
```

---

## 5. Lanzamiento!

Una vez todos tus archivos YAML están en sus carpetas, puedes aplicarlos por orden de dependencia (o todos a la vez dictando la carpeta principal). 

```bash
# Entra a la carpeta de tu estructura
kubectl apply -f 01-config/
kubectl apply -f 02-data/
kubectl apply -f 03-app/
kubectl apply -f 04-networking/
```

---

## 6. Validación con `kubectl` para Dejarlo Operativo

Al lanzar todo, la base de datos es la más pesada y tomará unos milisegundos más. Validemos cómo está la salud de tu entorno escalable:

### 1. Comprobar que todos los pods nacieron bien:
```bash
kubectl get pods
```
Deberías ver algo similar a esto:
```text
NAME                          READY   STATUS    RESTARTS   AGE
postgres-5c4...              1/1     Running   0          2m
redis-9b8...                 1/1     Running   0          2m
n8n-main-7f9...              1/1     Running   0          1m
n8n-worker-6df... (worker 1) 1/1     Running   0          1m
n8n-worker-6df... (worker 2) 1/1     Running   0          1m
```
*Si tienes `2` pods bajo el prefijo `n8n-worker`, ¡tienes la arquitectura escalable funcionando exitosamente!*

### 2. Validar conexiones exitosas y base de datos (Logs):
Para saber si el nodo Main logró conectarse al Postgres y levantar la interfaz:
```bash
# Reemplaza 'n8n-main-XXXX' con el nombre de tu pod principal
kubectl logs -f pod/n8n-main-XXXX
```
Asegúrate de ver un: `Editor is now accessible via...`

### 3. ¡Entrar al portal Front-End a través del Ingreso!
No tenemos LoadBalancer, sino un **Ingress**. Gracias a K3D que mapeó el puerto `8080`, solo abre tu navegador y entra a:

👉 **http://localhost:8080**

¡Ahí tendrás tu instancia de n8n empresarialmente configurada a un clúster emulado y enviando su carga a los workers en el fondo!

## Comandos Extra de Limpieza
Cuando termines de probar, para destruir todo el clúster sin dejar rastro de disco ni de red:
```bash
k3d cluster delete mi-cluster-n8n
```



