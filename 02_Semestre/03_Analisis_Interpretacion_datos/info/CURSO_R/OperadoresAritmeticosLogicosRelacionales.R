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