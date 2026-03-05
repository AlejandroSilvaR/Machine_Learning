"""
    Streamlit UI for Wizeline ML Regression Model.

    This app allows:
    - Uploading a CSV file
    - Generating predictions
    - Downloading the prediction results
"""

import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "model.pkl"

st.set_page_config(page_title="Wizeline ML Predictor", layout="centered")

st.title("📊 Wizeline Regression Predictor")
st.write("Upload a CSV file with 20 feature columns to generate predictions.")

# Load model
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("Preview of uploaded data:")
    st.dataframe(df.head())

    if st.button("Generate Predictions"):
        preds = model.predict(df)

        result_df = pd.DataFrame({"target_pred": preds})

        st.success("Predictions generated successfully!")

        st.dataframe(result_df)

        st.download_button(
            label="Download Predictions CSV",
            data=result_df.to_csv(index=False),
            file_name="predictions.csv",
            mime="text/csv"
        )