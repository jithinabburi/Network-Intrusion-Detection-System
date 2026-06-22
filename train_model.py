import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("data/live_dataset.csv")

X = df.drop("label", axis=1)
y = df["label"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

joblib.dump(
    model,
    "models/live_model.pkl"
)

print("Model Saved")