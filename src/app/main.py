# Steps 15–18: Train logistic regression model, evaluate, and predict test set

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    print("[INFO] Loading datasets...")
    train = pd.read_csv("src/data/train.csv")
    test  = pd.read_csv("src/data/test.csv")

    print("\n✅ train.csv shape:", train.shape)
    print("✅ test.csv shape:", test.shape)

    # --- Step 14 Review: Data Cleaning + Preparation ---
    print("\n[INFO] Cleaning data...")
    train["Age"].fillna(train["Age"].median(), inplace=True)
    test["Age"].fillna(test["Age"].median(), inplace=True)
    train["Sex"] = train["Sex"].map({"male": 0, "female": 1})
    test["Sex"] = test["Sex"].map({"male": 0, "female": 1})
    train["Embarked"].fillna("S", inplace=True)
    test["Fare"].fillna(test["Fare"].median(), inplace=True)
    print("[CLEAN] Filled missing Age values with median.")
    print("[CLEAN] Encoded Sex as numeric 0/1.")
    print("[CLEAN] Filled missing Embarked with 'S'.")
    print("[CLEAN] Filled missing Fare in test set with median.")


    # choose features
    features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]
    X = train[features]
    y = train["Survived"]

    # --- Step 15 ---
    print("\n[INFO] Splitting data (80/20)...")
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"Training samples: {X_train.shape[0]}, Validation samples: {X_val.shape[0]}")

    print("\n[TRAIN] Training Logistic Regression model...")
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    print("[TRAIN] Model trained successfully!")

    # --- Step 16 ---
    y_pred_train = model.predict(X_train)
    y_pred_val   = model.predict(X_val)
    train_acc = accuracy_score(y_train, y_pred_train)
    val_acc   = accuracy_score(y_val, y_pred_val)
    print(f"\n[METRICS] Training Accuracy:  {train_acc:.4f}")
    print(f"[METRICS] Validation Accuracy: {val_acc:.4f}")

    # --- Step 17: test.csv prediction ---
    print("\n[PREDICT] Making predictions on test.csv...")
    X_test = test[features]
    predictions = model.predict(X_test)

    # save prediction
    output = pd.DataFrame({
        "PassengerId": test["PassengerId"],
        "Survived": predictions
    })
    output_path = "src/data/predictions.csv"
    output.to_csv(output_path, index=False)
    print(f"[OUTPUT] Predictions saved to {output_path}")

    # --- Step 18 ---
    if "Survived" in test.columns:
        test_acc = accuracy_score(test["Survived"], predictions)
        print(f"[METRICS] Test Accuracy: {test_acc:.4f}")
    else:
        print("[INFO] Kaggle test.csv has no Survived labels — skipping test accuracy.")

    print("\n[DONE] Steps 15–18 completed successfully ✅")

if __name__ == "__main__":
    main()
