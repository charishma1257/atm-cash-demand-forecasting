import joblib
import pandas as pd

from preprocess import load_data
from feature_engineering import create_features

# Load trained model
model = joblib.load("../models/atm_model.pkl")

# Load and preprocess data
df = load_data("../data/atm_transactions.csv")
df = create_features(df)

# Features
X = df.drop(
    ["totalOutcome", "transactionTime", "ATM_ID"],
    axis=1
)

# Prediction
predictions = model.predict(X)

# Create clean results
results = pd.DataFrame({
    "ATM ID": df["ATM_ID"],
    "Predicted Withdrawal": predictions
})
results = (
    results.groupby("ATM ID", as_index=False)
    .agg({"Predicted Withdrawal": "mean"})
)

results["Predicted Withdrawal"] = results["Predicted Withdrawal"].round(2)
# Refill Status
results["Refill Status"] = results["Predicted Withdrawal"].apply(
    lambda x: "Refill Required" if x >= 4500 else "Sufficient Cash"
)

# Priority
results = results.sort_values(
    by="Predicted Withdrawal",
    ascending=False
).reset_index(drop=True)

results["Priority"] = range(1, len(results) + 1)

# Arrange columns
results = results[
    [
        "Priority",
        "ATM ID",
        "Predicted Withdrawal",
        "Refill Status"
    ]
]
print(results.head())

# Save predictions
results.to_csv("../data/predictions.csv", index=False)

print("Predictions saved successfully!")