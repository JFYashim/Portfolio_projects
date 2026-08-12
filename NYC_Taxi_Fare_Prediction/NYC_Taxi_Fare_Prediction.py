from pathlib import Path
import joblib
import streamlit as st

# Resolve path relative to this script
BASE_DIR = Path(__file__).resolve().parent


@st.cache_resource
def load_assets():
  model = joblib.load(BASE_DIR / "nyc_taxi_rf_model.pkl")
  scaler = joblib.load(BASE_DIR / "scaler.pkl")
  return model, scaler
