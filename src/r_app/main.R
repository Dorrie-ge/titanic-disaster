# Step 23–24: Titanic logistic regression in R

library(tidyverse)
library(caret)

cat("[INFO] Loading dataset...\n")
train <- read.csv("src/data/train.csv")
test  <- read.csv("src/data/test.csv")

cat("✅ train.csv shape:", dim(train)[1], "rows", dim(train)[2], "cols\n")
cat("✅ test.csv shape:", dim(test)[1], "rows", dim(test)[2], "cols\n")

# --- Cleaning ---
cat("\n[INFO] Cleaning data...\n")
train$Age[is.na(train$Age)] <- median(train$Age, na.rm = TRUE)
test$Age[is.na(test$Age)] <- median(test$Age, na.rm = TRUE)
train$Sex <- ifelse(train$Sex == "male", 0, 1)
test$Sex  <- ifelse(test$Sex == "male", 0, 1)
train$Embarked[is.na(train$Embarked)] <- "S"
test$Fare[is.na(test$Fare)] <- median(test$Fare, na.rm = TRUE)

features <- c("Pclass", "Sex", "Age", "SibSp", "Parch", "Fare")

cat("\n[INFO] Splitting data (80/20)...\n")
set.seed(42)
train_index <- createDataPartition(train$Survived, p = 0.8, list = FALSE)
train_set <- train[train_index, ]
val_set   <- train[-train_index, ]

cat("Training samples:", nrow(train_set), "Validation samples:", nrow(val_set), "\n")

# --- Train model ---
cat("\n[TRAIN] Fitting logistic regression model...\n")
model <- glm(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare,
             data = train_set, family = binomial())

cat("[TRAIN] Model trained successfully!\n")

# --- Accuracy ---
cat("\n[METRICS] Evaluating model...\n")
train_pred <- ifelse(predict(model, train_set, type = "response") > 0.5, 1, 0)
val_pred   <- ifelse(predict(model, val_set, type = "response") > 0.5, 1, 0)

train_acc <- mean(train_pred == train_set$Survived)
val_acc   <- mean(val_pred == val_set$Survived)

cat(sprintf("[METRICS] Training Accuracy:  %.4f\n", train_acc))
cat(sprintf("[METRICS] Validation Accuracy: %.4f\n", val_acc))

# --- Prediction on test.csv ---
cat("\n[PREDICT] Generating predictions on test.csv...\n")
test_pred <- ifelse(predict(model, test, type = "response") > 0.5, 1, 0)

output <- data.frame(PassengerId = test$PassengerId, Survived = test_pred)
output_path <- "src/data/predictions_R.csv"
write.csv(output, output_path, row.names = FALSE)
cat("[OUTPUT] Predictions saved to", output_path, "\n")

cat("\n[DONE] R steps 14–21 completed successfully ✅\n")
