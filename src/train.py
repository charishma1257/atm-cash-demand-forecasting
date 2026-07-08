import pandas as pd

from sklearn.model_selection import train_test_split

from preprocess import load_data
from feature_engineering import create_features
from model import train_model
from evaluate import evaluate_model
import joblib

# Load Data
df = load_data("../data/atm_transactions.csv")

# Feature Engineering
df = create_features(df)

# Split Data
y = df["totalOutcome"]
X = df.drop(
    ["totalOutcome", "transactionTime", "ATM_ID"],
    axis=1
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    shuffle=False
)

# Train Model
model = train_model(X_train, y_train)

# Evaluate Model
y_pred = evaluate_model(model, X_test, y_test)
joblib.dump(model, "../models/atm_model.pkl")

print("Model saved successfully!")