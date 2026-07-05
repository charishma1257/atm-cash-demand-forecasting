import pandas as pd

def create_features(df):

    # Date Features
    df['day_of_week'] = df['transactionTime'].dt.weekday
    df['month'] = df['transactionTime'].dt.month
    df['day'] = df['transactionTime'].dt.day
    df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)

    # Lag Features
    df['lag_1'] = df.groupby('atmId')['totalOutcome'].shift(1)
    df['lag_7'] = df.groupby('atmId')['totalOutcome'].shift(7)

    # Rolling Features
    df['rolling_7'] = (
        df.groupby('atmId')['totalOutcome']
        .shift(1)
        .rolling(7)
        .mean()
    )

    df['rolling_3'] = (
        df.groupby('atmId')['totalOutcome']
        .shift(1)
        .rolling(3)
        .mean()
    )

    # Remove missing values
    df = df.dropna()

    # Remove very small withdrawals
    df = df[df['totalOutcome'] > 1000]

    # One-hot encoding
    df = pd.get_dummies(df, columns=['atmCity'], drop_first=True)

    return df