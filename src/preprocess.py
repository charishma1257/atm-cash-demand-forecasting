import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)

    # Remove unnecessary columns
    df = df.drop(['atmName', 'atmAddress'], axis=1, errors='ignore')

    # Convert ATM IDs into numbers
    df['atmId'] = pd.factorize(df['atmId'])[0]

    # Convert transactionTime into datetime
    df['transactionTime'] = pd.to_datetime(df['transactionTime'])

    # Sort data
    df = df.sort_values(['atmId', 'transactionTime'])

    return df