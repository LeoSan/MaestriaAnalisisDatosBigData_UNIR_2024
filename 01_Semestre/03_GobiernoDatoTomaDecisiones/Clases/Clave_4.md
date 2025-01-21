## Clase 4: 14 Enero 

>[!NOTE]
> Notas de la clase  -> El deber ser es tener el Director de TI, Director de Bases de Datos y Director de Seguridad de información, pero no podemos ser juez y parte.
> Un dato erroneo puede ser el causante de una serie de malas decisiones. 
> MDM Master Data Management 

![image](https://github.com/user-attachments/assets/f86c389f-f464-4eef-b23a-06245d2da27a)

- Datos: elementos sin procesar de si solo no generan conocimiento.
- Información es un conjunto de datos con contexto.
- Conocomiento: conjunto de información ya validados y refinados. 
- Experiencia conocimiento aplicado facilitando una mejor compresion de situaciones complejas

**clasificación Datos** 
- Datos Estructurados      -> Una Base SQL
- Datos semi-estructurados -> XML, Json, scv
- Datos no estructurados   -> Videos, audio, imaganes, correo electronicos, registro de chats 
Ciclo de Vida

**El ciclo de vida del Dato:**

- Se Crea:
    - Inicio del proceso.
    - Generación de algo nuevo o original.
    - Puede referirse a la producción de bienes, servicios, ideas, etc.
- Se Almacena:
    - Guardado o conservación de lo creado.
    - Puede implicar un almacenamiento físico o digital.
    - Se asegura la disponibilidad futura del elemento.
- Se Usa:
    - Utilización del elemento almacenado.
    - Consumo o aprovechamiento de sus características o funciones.
- Se Distribuye:
    - Difusión o entrega del elemento a otros.
    - Puede involucrar la venta, el intercambio o la donación.
- Se Archiva:
    - Organización y preservación de registros o información relacionada.
    - Facilita la búsqueda y recuperación futura.
- Se Destruye:
    - Finalización del ciclo de vida.
    - Eliminación o desecho del elemento.
    - Puede ser debido a obsolescencia, daño o finalización de su utilidad.

graph LR
A(Crea) --> B(Almacena)
B --> C(Usa)
C --> D(Distribuye)
D --> E(Archiva)
E --> F(Destruye)
F --> A

 
## Datos Maestros
Los datos maestros son una solución esencial para abordar el problema de la dispersión de datos en múltiples fuentes. Al unificar la información de clientes, empleados, proveedores y productos en una única fuente de verdad, se mejora la calidad de los datos, se optimizan los procesos y se facilita la toma de decisiones.

**Beneficios clave:**

* **Unificación:** Elimina duplicidades e inconsistencias.
* **Calidad:** Garantiza la precisión y confiabilidad de los datos.
* **Eficiencia:** Agiliza los procesos y operaciones.
* **Toma de decisiones:** Proporciona una visión completa de la información.

**Implementación exitosa**

Para implementar con éxito los datos maestros, es crucial contar con una sólida gobernanza de datos que asegure la calidad, seguridad y accesibilidad de la información.

**Palabras clave:** datos maestros, unificación de datos, calidad de datos, gobernanza de datos

## Cómo implementar un sistema de gestión de datos maestros
### Pasos clave:
1. **Planificación:** Definir objetivos, alcance y datos maestros clave.
2. **Coordinación:** Involucrar a todas las partes interesadas.
3. **Modelado:** Crear modelos de datos para representar la estructura.
4. **Integración:** Consolidar datos en un repositorio centralizado.
5. **Calidad de datos:** Implementar controles para garantizar la calidad.
6. **Sincronización:** Mantener los datos actualizados en tiempo real.
7. **Gobernanza:** Establecer reglas y políticas para la gestión de los datos.


## Pasos Clave para la Creación de un Repositorio de Datos Maestros

La creación de un repositorio de datos maestros es fundamental para garantizar la consistencia y calidad de la información en una organización. A continuación, se detallan los pasos clave:

### 1. Definición del Modelo
* Identificar el escenario de aplicación y definición.

### 2. Determinar la Calidad de los Datos
* Evaluar la calidad inicial de los datos.
* Determinar y medir impactos en la operación y negocio.

### 3. Propiedad y Responsabilidad
* Definir roles y permisos de acceso.

### 4. Seguridad y Protección de Datos
* Establecer niveles de servicio.
* Implementar medidas contra amenazas externas.
* Establecer una estrategia de respaldo.

## Cómo Planificar tu Estrategia MDM

La implementación de una estrategia MDM requiere una planificación cuidadosa que considere los siguientes aspectos:

1. **Enfoque en la calidad de datos a largo plazo.**
2. **Aceptación del liderazgo.**
3. **MDM como transformación cultural.**
4. **Responsabilidades y rendición de cuentas.**
5. **Selección adecuada de la solución MDM.**
6. **Escalabilidad de la solución.**
7. **Gobernanza de datos centralizada.**
8. **Definición y medición de métricas de efectividad.**

**Flujos de Datos del gobierno de Datos**
![image](https://github.com/user-attachments/assets/6f357758-fd8a-458d-ace5-bbfc1186cf56)

## **Resumen Ordenado:**
> La imagen representa un flujo de datos desde sistemas productores (ERP, CRM, etc.) hasta sistemas consumidores (eCommerce, aplicaciones móviles, etc.) a través de una plataforma de Gestión de Datos Maestros (MDM).

- Los datos se extraen de diversas fuentes (bases de datos, archivos, etc.) y se cargan en un Data Lake.
- Los datos se procesan y transforman mediante ETL y reglas de gobernanza.
- Los datos maestros se almacenan en un repositorio centralizado (MDM).
- Los datos se validan y se sincronizan con los sistemas consumidores a través de API y web hooks.
- Los sistemas consumidores utilizan los datos maestros para diversas tareas, como la personalización de la experiencia del cliente, la toma de decisiones y la generación de informes.
- Se utilizan herramientas de análisis y visualización para obtener insights a partir de los datos

## Diagrama de un Sistema de Gestión de Datos Maestros (MDM)

**Descripción:**

El diagrama ilustra el flujo de datos desde sistemas de origen (productores) hasta sistemas de destino (consumidores) a través de una plataforma de Gestión de Datos Maestros (MDM).

**Componentes clave:**

* **Sistemas Productores:** ERP (Sistemas de Planificación de Recursos Empresariales), CRM (Gestión de Relaciones con el Cliente), PLM ( Gestión del Ciclo de Vida del Producto), bases de datos, archivos, activos digitales.
* **Ingestión de Datos:** API, ETL, carga de archivos.
* **Data Lake:** Almacenamiento masivo de datos en bruto.
* **MDM:** Repositorio centralizado de datos maestros.
* **Sincronización de Datos:** API, web hooks, integración de terceros.
* **Sistemas Consumidores:** eCommerce, aplicaciones móviles, sistemas de análisis, etc.
* **Otros Elementos:** Descubrimiento de datos, linaje, inteligencia artificial.

**Flujo de Datos:**
1. Los datos se extraen de diversas fuentes y se cargan en el Data Lake.
2. Los datos se procesan y transforman mediante ETL y reglas de gobernanza.
3. Los datos maestros se almacenan en el repositorio MDM.
4. Los datos se validan y se sincronizan con los sistemas consumidores.
5. Los sistemas consumidores utilizan los datos para diversas tareas.

**Beneficios del MDM:**
* Mejora de la calidad de los datos.
* Mayor consistencia de la información.
* Toma de decisiones más informada.
* Optimización de procesos.
* Mayor agilidad en la respuesta a los cambios del negocio.
* Mayor satisfacción del cliente 

## **Ejemplo**
- Paso 1
![image](https://github.com/user-attachments/assets/0edb7895-8c27-4b57-bb58-7a8645246cbc)

- Paso 2
![image](https://github.com/user-attachments/assets/77dfb3e7-eb8e-4eba-9163-f8703b7e1f52)

- Paso 3
![image](https://github.com/user-attachments/assets/cb52aa51-d903-4b09-a04e-4ee778c75d6f)
  
- Paso 4
Me falto esta 

- Paso 5
![image](https://github.com/user-attachments/assets/87b17954-d3fb-4ddc-98fc-7bc2a1fb29b5)

- Paso 6
![image](https://github.com/user-attachments/assets/cb7a128b-7f8d-466e-ba03-c9cffeb275f2)

- Paso 7
![image](https://github.com/user-attachments/assets/7fc63ef7-cf8d-4ad4-94db-a3af87b9b491)
