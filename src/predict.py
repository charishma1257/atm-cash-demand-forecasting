import joblib

from preprocess import load_data
from feature_engineering import create_features

# Load trained model
model = joblib.load("../models/atm_model.pkl")

# Load and preprocess data
df = load_data("../data/atm_transactions.csv")
df = create_features(df)

# Features
X = df.drop(["totalOutcome", "transactionTime"], axis=1)

# Prediction
predictions = model.predict(X)

df["Predicted_Withdrawal"] = predictions

print(df[["atmId", "Predicted_Withdrawal"]].head())

# Save predictions
df.to_csv("../data/predictions.csv", index=False)

print("Predictions saved successfully!")