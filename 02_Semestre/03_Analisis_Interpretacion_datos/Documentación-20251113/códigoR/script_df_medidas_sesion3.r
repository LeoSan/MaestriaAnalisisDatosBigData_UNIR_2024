getwd()

setwd("C:\\Users\\Lenovo Pro\\Documents\\Proeduca\\UNIR\\Jun-Oct25\\AID\\Datasets\\")

df_stroke <- read.csv('healthcare-dataset-stroke-data.csv')

cols <- names(df_stroke)

cols

dim(df_stroke)

# Ver columnas
#df_stroke[1]

# Ver fila 3, columna 3
df_stroke[3,3]

# Ver filas 1 a 5
df_stroke[c(1:5),]

#Ver columnas 1 a 3
#df_stroke[cols[c(1:3)]]

##########
# Filtar información
##########

# Datos "N/A" en bmi
df_na = subset(df_stroke, bmi == "N/A")
df_na[c(20:25),]
class(df_stroke$bmi)

# Reemplazar los valores "N/A" de la columna bmi por la media

#install.packages('stringr')
library(stringr)

df_stroke$bmi <- str_replace(df_stroke$bmi,'N/A','0')
class(df_stroke$bmi)
df_stroke$bmi<-as.numeric(as.character(df_stroke$bmi))
class(df_stroke$bmi)
df_stroke$bmi <- replace(df_stroke$bmi, df_stroke$bmi == 0, mean(df_stroke$bmi))

# Filtrar mujeres
df_Female <- subset(df_stroke, gender == "Female")
df_Female[c(1:5),]
dim(df_Female)

# Filtrar hombres que nunca han fumado
df_Male_nosmoking <- subset(df_stroke, gender == "Male" & smoking_status == "never smoked")
df_Male_nosmoking[c(1:5),]
dim(df_Male_nosmoking)

# Filtrar personas cuya edad es menor o igual a 40 y tienen hipertension o una enfermedad del corazon
df_lesse40_enf <- subset(df_stroke, age <=40 & (heart_disease == 1 | hypertension == 1))
dim(df_lesse40_enf)
df_lesse40_enf[c(5:10),]

##########
# Medidas de tendencia central
##########

# Calcular la media de la edad
mean(df_stroke$age)
mean(df_stroke[["age"]])
mean(df_stroke[, 3])

# Calcular la moda de la edad
library(DescTools)
# Si el paquete no esta instalado ejecutar la siguiente línea y cargar nuevamente la libreria
#install.packages('DescTools')
Mode(df_stroke[["age"]])

# Calcular la mediana de la edad
median(df_stroke$age)

##########
# Medidas de dispersión
##########

#Rango
print(max(df_stroke[["age"]])-min(df_stroke[["age"]]))

# Varianza
var(df_stroke[["age"]])

# Desviación típica o estándar
sd(df_stroke[["age"]])

##########
# Gráficos de caja
##########
boxplot(df_stroke$age)
# boxplot(df_stroke$bmi)

##########
# Datos categoricos
##########
library(ggplot2)
#install.packages('ggplot2')
ggplot(df_stroke, aes(x=reorder(ever_married, ever_married, function(x)-length(x)))) +geom_bar(fill='red') +  labs(x='Ever married')

###########
# Histogramas
###########

Edad <- df_stroke$age
hist(Edad)