getwd()

setwd("C:\\Users\\Lenovo Pro\\Documents\\Proeduca\\UNIR\\Jun-Oct25\\AID\\Datasets\\")

###########
## Lectura 
###########
df_boston <- read.csv('BostonHousing.csv')

names(df_boston)

##### Eliminar columna CAT..MEDV
df_boston <- subset(df_boston, select = -CAT..MEDV)

df_MEDV <- subset(df_boston, select = MEDV)

library(ggplot2)

# Create a histogram with a vertical line at the mean
ggplot(df_boston, aes(x = MEDV)) +
  geom_histogram(binwidth = 3, fill = "lightblue", color = "black") +
  labs(title = "Histogram with Mean Line (ggplot2)")

#########
## División del dataset en train y test
#########

library(caret)

set.seed(123)

train_percentage <- 0.8

trainIndex <- createDataPartition(df_boston$MEDV, p = train_percentage)

# Convert trainIndex to a numeric vector
trainIndex <- unlist(trainIndex)

training_data <- df_boston[trainIndex, ]
testing_data <- df_boston[-trainIndex, ]

#########################
## Sin transformación
#########################

model <- lm(MEDV ~ . , data = training_data)
residual <- model$residuals

plot(fitted(model), residual,
         main = "Residuals vs. Fitted Values",
         xlab = "Fitted Values",
         ylab = "Residuals")
abline(h = 0, col = "red", lty = 2) # Agrega una línea punteada roja en 0

summary(model)

# Predicciones
predictions <- predict(model, newdata = testing_data)

# Calculo de Mean Absolute Error (MAE)
mae <- mean(abs(predictions - actual_values))
cat("Mean Absolute Error (MAE):", mae, "\n")

# Calculo de Mean Squared Error (MSE)
mse <- mean((predictions - actual_values)^2)
cat("Mean Squared Error (MSE):", mse, "\n")

# Calculo de Root Mean Squared Error (RMSE)
rmse <- sqrt(mse)
cat("Root Mean Squared Error (RMSE):", rmse, "\n")

library(car)
vif(model)

#########################
## Transformación logaritmica
#########################

model_log <- lm(log(MEDV) ~ . , data = training_data)
val_residual <- model_log$residuals

plot(fitted(model_log), val_residual,
         main = "Residuals vs. Fitted Values",
         xlab = "Fitted Values",
         ylab = "Residuals")
abline(h = 0, col = "red", lty = 2) # Agrega una línea punteada roja en 0

summary(model_log)

# Predicciones
predictions_log <- predict(model_log, newdata = testing_data)

# Valores correctos
actual_values <- testing_data$MEDV  

# Calculo de Mean Absolute Error (MAE)
mae_log <- mean(abs(exp(predictions_log) - actual_values))
cat("Mean Absolute Error (MAE):", mae_log, "\n")

# Calculo de Mean Squared Error (MSE)
mse_log <- mean((exp(predictions_log) - actual_values)^2)
cat("Mean Squared Error (MSE):", mse_log, "\n")

# Calculo de Root Mean Squared Error (RMSE)
rmse_log <- sqrt(mse_log)
cat("Root Mean Squared Error (RMSE):", rmse_log, "\n")

vif(model_log)

#########################
## Transformación sqrt
#########################

model_sqrt <- lm(sqrt(MEDV) ~ . , data = training_data)
residual_sqrt <- model_sqrt$residuals

plot(fitted(model_sqrt), residual_sqrt,
         main = "Residuals vs. Fitted Values",
         xlab = "Fitted Values",
         ylab = "Residuals")
abline(h = 0, col = "red", lty = 2) # Agrega una línea punteada roja en 0

summary(model_sqrt)

# Predicciones
predictions_sqrt <- predict(model_sqrt, newdata = testing_data)

# Calculo de Mean Absolute Error (MAE)
mae_sqrt <- mean(abs(predictions_sqrt**2 - actual_values))
cat("Mean Absolute Error (MAE):", mae_sqrt, "\n")

# Calculo de Mean Squared Error (MSE)
mse_sqrt <- mean((predictions_sqrt**2 - actual_values)^2)
cat("Mean Squared Error (MSE):", mse_sqrt, "\n")

# Calculo de Root Mean Squared Error (RMSE)
rmse_sqrt <- sqrt(mse_sqrt)
cat("Root Mean Squared Error (RMSE):", rmse_sqrt, "\n")

vif(model_sqrt)

#########################
## Transformación Box-Cox
#########################

install.packages("MASS")
library(MASS)

bc <- boxcox(model, lambda = seq(-2, 2, 0.1))

lambda_bc <- bc$x[which.max(bc$y)]

model_bc <- lm(((MEDV^lambda_bc-1)/lambda_bc) ~ . , data = training_data)
residual_bc <- model_bc$residuals

plot(fitted(model_bc), residual_bc,
         main = "Residuals vs. Fitted Values",
         xlab = "Fitted Values",
         ylab = "Residuals")
abline(h = 0, col = "red", lty = 2) # Agrega una línea punteada roja en 0

summary(model_bc)

# Predicciones
predictions_bc <- predict(model_bc, newdata = testing_data)

inv_boxcox <- function(y, lambda) {
  if (lambda == 0) {
    return(exp(y))
  } else {
    return((lambda * y + 1)^(1 / lambda))
  }
}

predictions_org <- inv_boxcox(predictions_bc, lambda_bc)

# Calculo de Mean Absolute Error (MAE)
mae_org <- mean(abs(predictions_org - actual_values))
cat("Mean Absolute Error (MAE):", mae_bc, "\n")

# Calculo de Mean Squared Error (MSE)
mse_org <- mean((predictions_org - actual_values)^2)
cat("Mean Squared Error (MSE):", mse_org, "\n")

# Calculo de Root Mean Squared Error (RMSE)
rmse_org <- sqrt(mse_org)
cat("Root Mean Squared Error (RMSE):", rmse_org, "\n")

vif(model_bc)

######################
## Eliminando las variables con VIF mayor a 5
## VIF - factor de inflación de la varianza
######################

model_vif <- lm(log(MEDV) ~ CRIM + CHAS + NOX + RM + DIS + PTRATIO + 
            RAD + LSTAT, data = training_data)

summary(model_vif)

# Predicciones
predictions_vif <- predict(model_vif, newdata = testing_data)

# Calculo de Mean Absolute Error (MAE)
mae_vif <- mean(abs(exp(predictions_vif) - actual_values))
cat("Mean Absolute Error (MAE):", mae_log, "\n")

# Calculo de Mean Squared Error (MSE)
mse_vif <- mean((exp(predictions_vif) - actual_values)^2)
cat("Mean Squared Error (MSE):", mse_vif, "\n")

# Calculo de Root Mean Squared Error (RMSE)
rmse_vif <- sqrt(mse_vif)
cat("Root Mean Squared Error (RMSE):", rmse_vif, "\n")


# Create a histogram with a density curve
ggplot(df_boston, aes(x = MEDV)) +
  # Density for MEDV
  geom_density(aes(x = MEDV), color = "red", size = 1) +
  # Density for log(MEDV)
  geom_density(aes(x = log(MEDV)), color = "blue", size = 1) +
  # Density for sqrt(MEDV)
  geom_density(aes(x = sqrt(MEDV)), color = "green", size = 1) +
  # Density for sqrt(MEDV)
  geom_density(aes(x = MEDV**(1/3)), color = "orange", size = 1) +
  labs(title = "Histogram with Density Curve (ggplot2)")

