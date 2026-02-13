import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import mlflow
import yaml
import os

def train():

    # Read parameters
    with open("ml/params.yml") as f:
        params = yaml.safe_load(f)

    learning_rate = params["learning_rate"]
    epochs = params["epochs"]

    mlflow.set_experiment("KT-House-Price")

    with mlflow.start_run():

        df = pd.read_csv("data/data.csv")

        X = df[["sqft", "bedrooms", "bathrooms"]]
        y = df["price"]

        # For LinearRegression learning_rate & epochs are dummy,
        # but we log them to show parameter tracking
        model = LinearRegression()
        model.fit(X, y)

        predictions = model.predict(X)
        mae = mean_absolute_error(y, predictions)

        # Log parameters from YAML
        mlflow.log_param("learning_rate", learning_rate)
        mlflow.log_param("epochs", epochs)
        mlflow.log_metric("MAE", mae)

        os.makedirs("api", exist_ok=True)
        joblib.dump(model, "api/model.pkl")

        print("Training completed successfully")

if __name__ == "__main__":
    train()
