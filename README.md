# Titanic Disaster Project

This project trains logistic regression models in **Python** and **R** to predict passenger survival on the Titanic dataset.

Overview

This repository contains two containerized environments: one in Python and one in R that build and train logistic regression models to predict passenger survival from the Titanic disaster (April 15, 1912). Both environments are fully reproducible using Docker.
You can follow the instructions below to run both containers and reproduce the results.

Repository Structure
titanic-disaster/
├── Dockerfile                
├── requirements.txt           
├── README.md                  
├── src/
│   ├── app/                   # Python script
│   │   └── main.py
│   ├── r_app/                 # R container and script
│   │   ├── Dockerfile
│   │   └── main.R
│   └── data/                  # Data folder
└── .gitignore

Step 1 — Clone the Repository
Step 2 — Download the Data
You need to manually download the Kaggle Titanic dataset because it cannot be uploaded to GitHub. Go to: https://www.kaggle.com/competitions/titanic/data

Download the following files:

train.csv
test.csv
gender_submission.csv

Move them into: titanic-disaster/src/data/

Step 3 — Run the Python Docker Container
Build the image
docker build -t titanic-app .

Run the container
docker run --rm -v "$PWD/src/data:/app/src/data" titanic-app

Expected Output
[INFO] Loading datasets...
✅ train.csv shape: (891, 12)
✅ test.csv shape: (418, 11)

[TRAIN] Training Logistic Regression model...
[METRICS] Training Accuracy: 0.7963
[METRICS] Validation Accuracy: 0.7877
[OUTPUT] Predictions saved to src/data/predictions.csv
[DONE] Steps 15–18 completed successfully ✅

Output File
src/data/predictions.csv

Step 4 — Run the R Docker Container
Build the image
docker build -t titanic-r -f src/r_app/Dockerfile src/r_app

Run the container
docker run --rm -v "$PWD/src/data:/app/src/data" titanic-r

Expected Output
[INFO] Loading dataset...
✅ train.csv shape: 891 rows 12 cols
[TRAIN] Model trained successfully!
[METRICS] Training Accuracy:  0.8093
[METRICS] Validation Accuracy: 0.7472
[OUTPUT] Predictions saved to src/data/predictions_R.csv
[DONE] R steps 14–21 completed successfully ✅

Output File
src/data/predictions_R.csv

Step 5 — Model Summary
Environment	Language	Algorithm	Accuracy (Train / Validation)	Output
Python	scikit-learn	Logistic Regression	~0.79 / ~0.78	predictions.csv
R	glm (caret)	Logistic Regression	~0.81 / ~0.75	predictions_R.csv

Step 6 — Expected Results

After running both containers, two output files will be created:

src/data/predictions.csv
src/data/predictions_R.csv


Each contains predicted survival outcomes for all passengers in test.csv.
The scripts print informative progress messages (e.g., data cleaning, model training, accuracy, and output paths) directly to the terminal.



Shuoyu (Dorrie) Ge
Machine Learning & Data Science
Northwestern University