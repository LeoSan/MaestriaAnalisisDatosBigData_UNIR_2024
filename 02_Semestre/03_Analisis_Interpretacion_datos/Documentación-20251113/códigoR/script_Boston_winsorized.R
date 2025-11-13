getwd()

setwd("C:\\Users\\Lenovo Pro\\Documents\\Proeduca\\UNIR\\Jun-Oct25\\AID\\Datasets\\")

###########
## Lectura 
###########
df_boston <- read.csv('BostonHousing.csv')

##### Eliminar columna CAT..MEDV
df_boston <- subset(df_boston, select = -CAT..MEDV)

##### Columnas y tipos de datos
sapply(df_boston, class)

###########
## Estadistica descriptiva 
###########

summary(df_boston)

###########
## Distribución de datos
###########

# Se elimina la columna TAX, MEDV 
df_boston_1 <- subset(df_boston, select = -c(TAX, MEDV))
sapply(df_boston_1, class)

#boxplot(df_boston)

library(ggplot2)
# Boxplot variable TAX
ggplot(df_boston, aes(x=0, y=TAX)) +
	geom_boxplot() +
	coord_flip()

# Boxplot todas resto de variables independientes
ggplot(stack(df_boston_1), aes(x = ind, y = values )) +
  geom_boxplot() +
  coord_flip() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

############
## Variable de salida MEDV
############

# Diagrama de caja y bigote
ggplot(df_boston, aes(x=0, y=MEDV)) +
	geom_boxplot() +
	coord_flip()

# Histograma
ggplot(df_boston, aes(x = MEDV)) +
	geom_histogram(binwidth = 3, fill = "lightblue", color = "blue") + 
	labs(title = "MEDV", x = "Values", y = "Count") +
	theme_minimal()

############
## Correlación de Pearson
############

corr <- round(cor(df_boston), 2)

library(reshape2)
melt_corr <- melt(corr)

melt_corr$Var2 <- factor(melt_corr$Var2, levels = rev(unique(melt_corr$Var2)))

heatmap_cor <- ggplot(data = melt_corr, aes(x=Var1, y=Var2, fill=value)) + 
	geom_tile(color="white") +
	scale_fill_gradient(low = "lightgray", high = "red") + # Set color gradient
	theme_minimal() + # Set theme
	labs(x = "X Axis", y = "Y Axis", title = "Correlación de Pearson") + # Labels
	theme(axis.text.x = element_text(angle = 45, hjust = 1)) + # heatmap_plot_with_values <- heatmap_cor +
	geom_text(aes(label = value), color = "white", size = 3)

heatmap_cor

ggplot(df_boston, aes(x = RM, y = MEDV)) +
  geom_point(color = "blue") +
  labs(x = "RM", y = "MEDV") +
  ggtitle("Gráfico de dispersión de RM vs. MEDV")

ggplot(df_boston, aes(x = LSTAT, y = MEDV)) +
  geom_point(color = "red") +
  labs(x = "LSTAT", y = "MEDV") +
  ggtitle("Gráfico de dispersión de LSTAT vs. MEDV")

# Validación de NaN
sum(is.nan(as.matrix(df_boston)))

# Verificar los ceros
zeros_per_column <- colSums(df_boston == 0)
print(zeros_per_column)

##########
## Detección de outliers
##########

numerical_data <- df_boston[, sapply(df_boston, is.numeric)]

# Calculate IQR for all numerical columns
iqrs_all_columns <- sapply(numerical_data, IQR)
print(iqrs_all_columns)

func_iqr <- function(df_col){
	q1 <- quantile(df_col, 0.25)
	q3 <- quantile(df_col, 0.75)
	iqr_val <- IQR(df_col)


	# Define outlier bounds
	lower_bound <- q1 - 1.5 * iqr_val
	upper_bound <- q3 + 1.5 * iqr_val

	# Identify outliers
	outliers <- df_col[df_col < lower_bound | df_col > upper_bound]
	return(outliers)
}

outliers_MEDV <- func_iqr(df_boston$MEDV)

outliers_col <- apply(df_boston, 2, func_iqr)
print(outliers_col)

# Calculate quartiles and IQR
q1 <- quantile(df_boston$MEDV, 0.25)
q3 <- quantile(df_boston$MEDV, 0.75)
iqr_val <- IQR(df_boston$MEDV)


# Define outlier bounds
lower_bound <- q1 - 1.5 * iqr_val
upper_bound <- q3 + 1.5 * iqr_val

# Identify outliers
outliers <- df_boston$MEDV[df_boston$MEDV < lower_bound | df_boston$MEDV > upper_bound]
print(outliers)

###########
## Winsorize
###########

lst_outliers <- c("CRIM", 'ZN', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'LSTAT')

library(dplyr)
library(DescTools)

df_win_boston <- df_boston

winsorize_own <- function(x, lower = 0.1, upper = 0.9){
  qnt <- quantile(x, probs = c(lower, upper), na.rm = TRUE)
  x[x < qnt[1]] <- qnt[1]
  x[x > qnt[2]] <- qnt[2]
  return(x)
}

# Aplicarlo
for (col in lst_outliers) {
  print(col)
  df_win_boston[[col]] <- winsorize_own(df_win_boston[[col]])
}

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

model <- lm(MEDV ~ . , data = training_data)

summary(model)

# Predicting on the test set
predictions <- predict(model, newdata = testing_data)

# getting true value of test data
actual_values <- testing_data$MEDV  # Actual values from the test set

# Calculating Mean Absolute Error (MAE)
mae <- mean(abs(predictions - actual_values))
cat("Mean Absolute Error (MAE):", mae, "\n")

# Calculating Mean Squared Error (MSE)
mse <- mean((predictions - actual_values)^2)
cat("Mean Squared Error (MSE):", mse, "\n")

# Calculating Root Mean Squared Error (RMSE)
rmse <- sqrt(mse)
cat("Root Mean Squared Error (RMSE):", rmse, "\n")


#########
## Modelo datos windorizados
#########

trainIndex_win <- createDataPartition(df_win_boston$MEDV, p = train_percentage)

# Convert trainIndex to a numeric vector
trainIndex_win <- unlist(trainIndex_win)

training_win_data <- df_win_boston[trainIndex_win, ]
testing_win_data <- df_win_boston[-trainIndex_win, ]

model_win <- lm(MEDV ~ . , data = training_win_data)
val_residual_win <- model_win$residuals

plot(fitted(model_win), val_residual_win,
     main = "Residuals vs. Fitted Values",
     xlab = "Fitted Values",
     ylab = "Residuals")
abline(h = 0, col = "red", lty = 2) # Adds a dashed red line at y=0

summary(model_win)

# Predicting on the test set
predictions_win <- predict(model_win, newdata = testing_win_data)

# getting true value of test data
actual_win_values <- testing_win_data$MEDV  # Actual values from the test set

# Calculating Mean Absolute Error (MAE)
mae_win <- mean(abs(predictions_win - actual_win_values))
cat("Mean Absolute Error (MAE):", mae_win, "\n")

# Calculating Mean Squared Error (MSE)
mse_win <- mean((predictions_win - actual_win_values)^2)
cat("Mean Squared Error (MSE):", mse_win, "\n")

# Calculating Root Mean Squared Error (RMSE)
rmse_win <- sqrt(mse_win)
cat("Root Mean Squared Error (RMSE):", rmse_win, "\n")
