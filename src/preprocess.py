import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)

    # Remove unnecessary columns
    df = df.drop(['atmName', 'atmAddress'], axis=1, errors='ignore')

    # Convert ATM IDs into numbers
    # Keep original ATM IDs
    df["ATM_ID"] = df["atmId"]

# Create numeric ID only for model
    df["atmId_encoded"] = pd.factorize(df["atmId"])[0]

    df.drop("atmId", axis=1, inplace=True)

    df.rename(columns={"atmId_encoded": "atmId"}, inplace=True)

    # Convert transactionTime into datetime
    df['transactionTime'] = pd.to_datetime(df['transactionTime'])

    # Sort data
    df = df.sort_values(['atmId', 'transactionTime'])

    return df