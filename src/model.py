from xgboost import XGBRegressor


def train_model(X_train, y_train):

    model = XGBRegressor(
        n_estimators=600,
        learning_rate=0.02,
        max_depth=10,
        subsample=0.9,
        colsample_bytree=0.9,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model