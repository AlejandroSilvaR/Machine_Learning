"""
    FastAPI application for serving trained regression model.

    Provides:
    - Single prediction endpoint
    - Batch prediction endpoint
"""

from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
from typing import List
from pathlib import Path

# Api global variables:
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "model.pkl"

# Create APP and load final model:
app = FastAPI(title="Wizeline ML Regression API")
model = joblib.load(MODEL_PATH)

# Define inputs:
class Features(BaseModel):
    feature_0: float
    feature_1: float
    feature_2: float
    feature_3: float
    feature_4: float
    feature_5: float
    feature_6: float
    feature_7: float
    feature_8: float
    feature_9: float
    feature_10: float
    feature_11: float
    feature_12: float
    feature_13: float
    feature_14: float
    feature_15: float
    feature_16: float
    feature_17: float
    feature_18: float
    feature_19: float

# Post Request (Endpoint) for single prediction "Input=JSON":
@app.post("/predict")
def predict(data: Features):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)
    return {"prediction": float(prediction[0])}

# Post Request (Endpoint) for multiple predictions "Input=Registers"
@app.post("/batch_predict")
def batch_predict(data: List[Features]):
    df = pd.DataFrame([item.dict() for item in data])
    preds = model.predict(df)
    return {"predictions": preds.tolist()}