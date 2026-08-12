import datetime
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
import streamlit as st

# Set base directory relative to this script
BASE_DIR = Path(__file__).resolve().parent

# Page setup
st.set_page_config(
    page_title="NYC Taxi Fare Predictor", page_icon="🚕", layout="centered"
)


# Load model and scaler
@st.cache_resource
def load_assets():
  model = joblib.load(BASE_DIR / "nyc_taxi_rf_model.pkl")
  scaler = joblib.load(BASE_DIR / "scaler.pkl")
  return model, scaler


try:
  model, scaler = load_assets()
  assets_loaded = True
except Exception as e:
  st.error(f"Error loading model files: {e}")
  assets_loaded = False

st.title("🚕 NYC Taxi Fare Predictor")
st.write("Enter the trip details below to calculate the predicted base fare.")

if assets_loaded:
  with st.form("prediction_form"):
    st.subheader("Trip Details")

    col1, col2 = st.columns(2)

    with col1:
      pickup_date = st.date_input("Pickup Date", datetime.date.today())
      pickup_time = st.time_input("Pickup Time", datetime.time(12, 0))
      trip_distance = st.number_input(
          "Trip Distance (miles)",
          min_value=0.1,
          max_value=100.0,
          value=2.5,
          step=0.1,
      )

    with col2:
      duration_minutes = st.number_input(
          "Estimated Duration (minutes)",
          min_value=1.0,
          max_value=300.0,
          value=12.0,
          step=0.5,
      )
      rate_code = st.selectbox(
          "Rate Code",
          options=[1, 2, 3, 4, 5, 6],
          format_func=lambda x: {
              1: "1 - Standard Rate",
              2: "2 - JFK Airport",
              3: "3 - Newark",
              4: "4 - Nassau / Westchester",
              5: "5 - Negotiated Fare",
              6: "6 - Group Ride",
          }[x],
      )

    submit = st.form_submit_button("Predict Fare", use_container_width=True)

 if submit:
        pickup_datetime = datetime.datetime.combine(pickup_date, pickup_time)
        hour_of_day = pickup_datetime.hour
        day_of_week = pickup_datetime.weekday()
        month = pickup_datetime.month

        input_data = pd.DataFrame([{
            "trip_distance": trip_distance,
            "duration_minutes": duration_minutes,
            "hour_of_day": hour_of_day,
            "day_of_week": day_of_week,
            "month": month,
            "RatecodeID": rate_code,
        }])

        # Dynamically reorder and match columns expected by the scaler
        if hasattr(scaler, "feature_names_in_"):
            input_data = input_data[scaler.feature_names_in_]

        scaled_features = scaler.transform(input_data)
        prediction = model.predict(scaled_features)[0]
    st.success(f"### Estimated Fare: **${prediction:.2f}**")
    st.caption(
        "Note: Prediction reflects base fare excluding tips, tolls, and extra"
        " surcharges."
    )
