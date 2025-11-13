getwd()

setwd("C:\\Users\\Lenovo Pro\\Documents\\Proeduca\\UNIR\\Jun-Oct25\\AID\\Datasets\\")

df_Suecia <- read.csv('accidentes_Suecia.csv')

cols <- names(df_Suecia)

cols

dim(df_Suecia)

##########
# Analisis de información
##########

## Devuelve una descripción de cada una de las columnas
summary(df_Suecia)

##########
# Valores NA
##########

colSums(is.na(df_Suecia))

##########
# Correlación
##########

cor_S <- cor(df_Suecia)
cor_S

##########
# Regresión lineal
##########

reg_S <- lm(Y ~ X, data = df_Suecia)
summary(reg_S)

##########
# Gráfica
##########

plot(df_Suecia$X, df_Suecia$Y, xlab='Número de accidentes', ylab='Pago accidentes')+
abline(reg_S)

##########
# Predicciones
##########

nuevos_acc <- data.frame(X = c(49, 73, 89))
predict(reg_S, nuevos_acc)

##########
# Predicciones
##########

confint(reg_S)
confint(reg_S, level = 0.90)

# Grafico de dispersion y recta
plot(df_Suecia$X, df_Suecia$Y, xlab='Número de accidentes', ylab='Pago accidentes')+
abline(reg_S)

# Intervalos de confianza de la respuesta media:
# ic es una matriz con tres columnas: la primera es la prediccion, las otras dos son los extremos del intervalo
ic <- predict(reg_S, nuevos_acc, interval = 'confidence')
lines(nuevos_acc$X, ic[, 2], lty = 2)
lines(nuevos_acc$X, ic[, 3], lty = 2)

# Intervalos de prediccion
ic <- predict(reg_S, nuevos_acc, interval = 'prediction')
lines(nuevos_acc$X, ic[, 2], lty = 2, col = 'red')
lines(nuevos_acc$X, ic[, 3], lty = 2, col = 'red')

##########
# Diagnóstico del modelo
##########

residuos <- rstandard(reg_S)
val_ajustados <- fitted(reg_S)
plot(val_ajustados, residuos)

############################################################################
#				Regresión lineal múltiple				   #
############################################################################

df.heart <- read.csv('heart_data.csv')

##########
# Analisis de información
##########

summary(df.heart)

##########
# Valores NA
##########

colSums(is.na(df.heart))

##########
# Correlación
##########

cor_S <- cor(df.heart)
cor_S

##########
# Regresión lineal
##########

heart.lm<-lm(heart.disease ~ biking + smoking, data = df.heart)

summary(heart.lm)

plot(df.heart$biking, df.heart$heart.disease, xlab='biking', ylab='heart disease')+
abline(heart.lm)

##########
# Predicciones
##########

nueva.inf <- data.frame(biking = c(49.5, 73.2, 23.4), smoking = c(34.2, 10.3, 29.0))
predict(heart.lm, nueva.inf)

residuos <- resid(heart.lm)
plot(fitted(heart.lm), residuos)
# Se agrega una linea horizontal en 0
abline(0,0)