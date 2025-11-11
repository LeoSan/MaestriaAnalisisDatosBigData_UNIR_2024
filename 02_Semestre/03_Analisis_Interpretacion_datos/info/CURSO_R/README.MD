## Curso de R 
### Pasos para Instalar R y RStudio

# Modulo 1
Instalar R y RStudio es como montar tu estación de trabajo de análisis de datos. Primero instalaremos el "motor" (R) y luego la "interfaz amigable" (RStudio).
---

### Paso 1: Instalar R (el Lenguaje y Entorno Base) Para MAC 

1.  **Ve a la página oficial de R:** Abre tu navegador web y dirígete a:.
    [https://www.r-project.org/](https://posit.co/download/rstudio-desktop/)

2.  En el enlace nos permite descargar su IDE y el lenguaje 

3. Como estamos en MAC podemos usar su instalador de manera sencilla 
    - Ejecutamos el [R-4.5.1-arm64.pkg] parecido a windows continuar + continuar 
        - Te instala una consola que puedes ejecutar los comandos de R
    - Ejeuctamos IDE [RStudio-2025.05.1-513.dmg] Este se instala arrastrando el dmg a la carpeta de de aplicaciones en pocas palabras es el IDE para R te permite codificar y escribir RMarkDown 

## Configuración del entorno en RStudio
**Notas**
- Es muy básica la configuracion podemos acceder en ella busando tools/ configuracion global 
- Imagen de Ejemplo
- [ejemplo](../info/info_001.png)
- Creadores Ross y Robert

# Modulo 2

# Unidad 2.1: 
- Se realiza la explicación de como generar operaciones basicas en este lenguaje:

```R

print("Hola mundo R")

# Declaraciones 
x<-10
y<-5 


# Operaciones 
suma <-x+y
resta <-x-y
multi <-x*y
divi <-x/y


# Como mostrar en consola 
print(suma)
print(resta)
print(multi)
print(divi)

# Cadenas String 

texto1 <- "Hol R"
print(texto1)

nombre <- "Juan"
saludo <- paste("Hola, ", nombre)
edad <- 37
print(saludo)

frase <- paste("Esto", "es", "R", sep='-')
print(frase)

## Mayusculas y Minusculas 
print(toupper(frase))
print(tolower(frase))

mensaje <- sprintf("Hola mi nombre es %s y tengo %d años", nombre, edad )
print(mensaje)  
  
## Valores Booleanos 
falso <-FALSE 
verdad <-TRUE


## Bloque codicional 

if (edad < 30){
  
  print('Felicidades aun no llegas al tercer piso')
  
}else{
  
  print('Felicidades llegaste al terce piso ')
}

```

# Unidad 2.2: Estructura de Datos en R. 

## Importancia de Estrcutura de datos 
- Son cruciales en al gestion de grande volumes de datos
- Permiten organizar y acceder a la información de manera eficiencte
- Ejemplo de Uso: Calcular Promedios, varianzas o realizar simulaciones

 ## Tipos: 
 ## Vectores: 
    - Concepto: son secuencias de elementos  que comparten el mismo tipo de datos. 
    - Podemos almacenar y operar  multiples datos de manera simultanea. 
    - facilita operaciones de filtrado ó promediar o sumar 

## Matrices
    - Concepto: Son extensiones de los vectores y son usadas para organizar datos en dos dimensiones Filas y Columnas 
    - son utiles para representar datos tabulares

## Estrcutura de Control 
    - Permiten la manipulación de los datos
    - Permite generar bucles para poder alcanzar el valor almacenado en vectores o matrices.
    - Radica en la capacidad de automatizar procesos
    - condicionales :  (if, else, else if)
    - Bucles : (for, while)



## VECTORES Y MATRICES EN R 

´´´R



# Los vectores son de un mismo tipo
vector_1 <-c(1,2,3,4,5)
vector 


vector_2 <-c("hola", "soy", "Vector", "Caracteres")
vector_2

## Valores secuencial 

a<- 1:10
a 


## Valores repetidos 
b<-rep(5, times=10)
b


## Valor metodo rep con c de concatenar 
c <-rep(c(1,2), times=4)
c 

## Metodo each 

d<-rep(c(1,2), each = 3)
d

e<-rep(c(1,2), times = 2, each = 3)
e

## Controlar la salida con el elemento length.out = 8
f<-rep(1:3, length.out = 8)
f


## acceder por posiciones 
g<-c("a", "b", "c")
g[0:2]


## Metodo de Secuencia seq(from, to, by, length.out)

seq(1,10,2)



## acceder por posiciones 
h<-c("a", "b", "c", "d", "f")
h[seq(1,4, by=2)]

## Graficos integrados 
x<-seq(0,2*pi, length.out =100)
y<-sin(x)

#plot(x,y,type="1")


## Puedes usar logica dentro de los corchetes del vector
v<-c(10,20,30,40,50,60,70)
v[v>25]
v[v %% 20==0 ]

v[2]<-99
v

## mean la media aritmetica, sd => desviacion standart
mean(v)
sd(v)
sort(v)
summary(v)


## Como usar Matrix se usa la palabra matrix(data, nrow, ncol, byrow=FALSE)

m<-matrix(1:6, nrow=2, ncol=3)
m

n<-matrix(1:8, nrow=2, ncol=3, byrow=FALSE)
n

## Como accedemos 

n[1,3] = 99
n

## Validr dimenciones usamos el metodo dim()
dim(n)
ncol(n)
nrow(n)

## Tambien podemos ejecutar operaciones entre matrices 
m +n
m -n
m *n

´´´

## EJERCICIO 

Estructuraría una matriz donde cada fila representaría un mes, y cada columna representaría una ciudad. Los valores dentro de la matriz serían los precios de las viviendas para ese mes y ciudad específica. Por ejemplo:
precios <- matrix(c(250000, 255000, 260000, 258000, 320000, 325000, 328000, 330000, 450000, 452000, 455000, 458000), nrow = 4, byrow = FALSE)
Le daré nombre a las filas y columnas:
colnames(precios) <- c("Barcelona", "Puerto la Cruz", "Lecheria")
rownames(precios) <- c("Ene-25", "Feb-25", "Mar-25", "Abr-25")
Para calcular la variación mensual, se necesitan funciones que permitan realizar operaciones entre las filas de la matriz, que lo haría en R así:
# Calcular la variación porcentual mensual
variacion_mensual <- (precios[2:nrow(precios), ] - precios[1:(nrow(precios)-1), ]) / precios[1:(nrow(precios)-1), ] * 100
# Añadir nombres de filas para la matriz de resultados
rownames(variacion_mensual) <- rownames(precios)[2:nrow(precios)]
# Imprimir la matriz de variaciones
print(variacion_mensual)


## Operadores aritméticos, lógicos y relacionales


```R
# Asignamos valores a dos variables
a <- 10
b <- 3

# Suma (+)
suma <- a + b
print(paste("Suma:", suma))  # Salida: 13

# Resta (-)
resta <- a - b
print(paste("Resta:", resta)) # Salida: 7

# Multiplicación (*)
multiplicacion <- a * b
print(paste("Multiplicación:", multiplicacion)) # Salida: 30

# División (/)
division <- a / b
print(paste("División:", division)) # Salida: 3.333...

# Exponenciación (^)
potencia <- a ^ 2
print(paste("Potencia:", potencia)) # Salida: 100

# Módulo (%%) - Devuelve el resto de una división
modulo <- a %% b
print(paste("Módulo:", modulo)) # Salida: 1


## Operadores Relacionales

x <- 5
y <- 12

# Mayor que (>)
print(paste("¿x es mayor que y?:", x > y)) # Salida: FALSE

# Menor que (<)
print(paste("¿x es menor que y?:", x < y)) # Salida: TRUE

# Igual a (==) - ¡Ojo! Se usan dos signos de igual.
print(paste("¿x es igual a y?:", x == y)) # Salida: FALSE

# No es igual a (!=)
print(paste("¿x no es igual a y?:", x != y)) # Salida: TRUE

# Mayor o igual que (>=)
print(paste("¿y es mayor o igual que x?:", y >= x)) # Salida: TRUE

# Menor o igual que (<=)
print(paste("¿x es menor o igual que 5?:", x <= 5)) # Salida: TRUE

## Operaciones Logicas

p <- TRUE
q <- FALSE

# AND (& o &&) - Devuelve TRUE solo si ambas condiciones son verdaderas.
print(paste("p Y q es:", p & q))   # Salida: FALSE
print(paste("p Y TRUE es:", p & TRUE)) # Salida: TRUE

# OR (| o ||) - Devuelve TRUE si al menos una de las condiciones es verdadera.
print(paste("p O q es:", p | q)) # Salida: TRUE
print(paste("FALSE O q es:", FALSE | q)) # Salida: FALSE

# NOT (!) - Invierte el valor lógico.
print(paste("NO p es:", !p)) # Salida: FALSE
print(paste("NO q es:", !q)) # Salida: TRUE
```

## La Estructura if, else if, else
Esta es la forma más clásica de tomar decisiones. Evalúa una condición y, si es verdadera, ejecuta un bloque de código. Puedes anidar varias condiciones para manejar múltiples escenarios.

Piensa en ello como dar instrucciones basadas en el clima: Si llueve, llevas paraguas. Si no, pero si está nublado, llevas una chaqueta. Si no, llevas gafas de sol.

```R
# Ejemplo: Calificar el desempeño de un estudiante
nota <- 85

if (nota >= 90) {
  print("Excelente, ¡tienes una A! 🏆")
} else if (nota >= 80) {
  print("Muy bien, tienes una B. 👍")
} else if (nota >= 70) {
  print("Aprobado, tienes una C.")
} else {
  print("Necesitas estudiar más, no aprobaste. 📚")
}

# Salida en este caso: "Muy bien, tienes una B. 👍"
```

La Función ifelse()
Esta es una versión compacta y muy útil del if-else, especialmente para trabajar con vectores (listas de datos). Aplica una condición a cada elemento de un vector y devuelve un resultado diferente dependiendo de si la condición es TRUE o FALSE.

```R
# Ejemplo: Clasificar números como pares o impares en un vector
numeros <- c(1, 4, 7, 10, 12, 15)

# Usamos el operador módulo (%%) para ver si el resto de la división por 2 es 0
resultado <- ifelse(numeros %% 2 == 0, "Par", "Impar")

print(resultado)

# Salida: "Impar" "Par" "Impar" "Par" "Par" "Impar"
```

La Estructura switch()
Es ideal cuando tienes una variable que puede tomar varios valores específicos y quieres ejecutar una acción diferente para cada uno. Es más limpio y legible que usar muchos else if.

```R
# Ejemplo: Asignar una actividad según el día de la semana
dia <- "Martes"

actividad <- switch(dia,
  "Lunes"   = "Empezar la semana con energía.",
  "Martes"  = "Reunión de equipo a las 10 AM.",
  "Miércoles" = "Día de análisis de datos.",
  "Jueves"  = "Planificar el fin de semana.",
  "Viernes" = "¡Día de pizza! 🍕",
  "Sábado"  = "Descansar o hacer ejercicio.",
  "Domingo" = "Prepararse para la nueva semana.",
  "Día no válido." # Valor por defecto si no coincide ninguno
)

print(actividad)

# Salida: "Reunión de equipo a las 10 AM."
```