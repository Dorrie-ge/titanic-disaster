🛳️ Titanic Survival Prediction (Python & R)
📘 Overview

This repository contains two complete environments — one in Python and one in R — that build and train logistic regression models to predict passenger survival from the Titanic disaster (April 15, 1912).

Both environments are fully containerized with Docker, so the grader can reproduce all results by following this README without installing any additional packages.

📁 Repository Structure
titanic-disaster/
├── Dockerfile                 # Python Dockerfile
├── requirements.txt           # Python dependencies
├── README.md                  # This instruction file
├── src/
│   ├── app/                   # Python container scripts
│   │   └── main.py
│   ├── r_app/                 # R container scripts
│   │   ├── Dockerfile
│   │   └── main.R
│   └── data/                  # Place data here (not included)
└── .gitignore

🧩 Step 1 — Clone the Repository

In your terminal:

git clone https://github.com/your-username/titanic-disaster.git
cd titanic-disaster


(Replace your-username with your GitHub username if needed.)

🧩 Step 2 — Download the Data

You must manually download the Kaggle Titanic dataset (not included in this repo).

Go to:
👉 https://www.kaggle.com/competitions/titanic/data

Download the following files:

train.csv

test.csv

gender_submission.csv

Place them inside:

titanic-disaster/src/data/


✅ Your local folder should now look like:

src/data/train.csv
src/data/test.csv
src/data/gender_submission.csv

🐍 Step 3 — Run the Python Docker Container
🧱 Build the Docker image

From the project root folder (titanic-disaster):

docker build -t titanic-app .

▶️ Run the container
docker run --rm -v "$PWD/src/data:/app/src/data" titanic-app

🧾 Expected Output

The terminal should print:

[INFO] Loading datasets...
✅ train.csv shape: (891, 12)
✅ test.csv shape: (418, 11)

[TRAIN] Training Logistic Regression model...
[METRICS] Training Accuracy: 0.7963
[METRICS] Validation Accuracy: 0.7877
[OUTPUT] Predictions saved to src/data/predictions.csv
[DONE] Steps 15–18 completed successfully ✅

📂 Output File
src/data/predictions.csv

📈 Step 4 — Run the R Docker Container
🧱 Build the Docker image
docker build -t titanic-r -f src/r_app/Dockerfile src/r_app

▶️ Run the container
docker run --rm -v "$PWD/src/data:/app/src/data" titanic-r

🧾 Expected Output

The terminal should print:

[INFO] Loading dataset...
✅ train.csv shape: 891 rows 12 cols
[TRAIN] Model trained successfully!
[METRICS] Training Accuracy:  0.8093
[METRICS] Validation Accuracy: 0.7472
[OUTPUT] Predictions saved to src/data/predictions_R.csv
[DONE] R steps 14–21 completed successfully ✅

📂 Output File
src/data/predictions_R.csv

🧮 Step 5 — Model Summary
Environment	Language	Algorithm	Accuracy (Train / Validation)	Output
Python	scikit-learn	Logistic Regression	~0.79 / ~0.78	predictions.csv
R	glm (caret)	Logistic Regression	~0.81 / ~0.75	predictions_R.csv
🧰 Step 6 — Local (Non-Docker) Run (Optional)
Run Python locally
pip install -r requirements.txt
python src/app/main.py

Run R locally
install.packages(c("tidyverse", "caret"))
source("src/r_app/main.R")

🏁 Step 7 — What the Grader Should See

After running both containers, the grader should have:

src/data/predictions.csv
src/data/predictions_R.csv


Both files contain predicted survival outcomes for all passengers in test.csv.

All steps print informative progress messages to the terminal (e.g., data cleaning, model training, accuracy scores, prediction output).

🧾 Notes

Both containers are self-contained and reproducible.

Only train.csv and test.csv are required inputs.

.gitignore ensures no datasets are uploaded to GitHub.

Each container outputs a clear [DONE] message when finished.