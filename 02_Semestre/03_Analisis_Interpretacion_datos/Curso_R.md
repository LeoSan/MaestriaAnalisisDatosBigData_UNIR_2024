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

## Unidad 2.1: 
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

