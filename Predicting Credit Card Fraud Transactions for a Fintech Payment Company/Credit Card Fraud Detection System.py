import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Credit Card Fraud Detector", layout="wide")

# Load the entire pipeline (contains both scaler + model)
@st.cache_resource
def load_pipeline():
    return joblib.load('fraud_model.joblib')

fraud_model = load_pipeline()

st.title("💳 Credit Card Fraud Detection System")
st.markdown("Enter the 30 raw feature values or upload a CSV file to analyze transaction risk.")

tab1, tab2 = st.tabs(["Single Transaction", "Batch CSV Upload"])

# --- TAB 1: Single Prediction ---
with tab1:
    st.subheader("Manual Input")
    
    col1, col2 = st.columns(2)
    with col1:
        time_sec = st.number_input("Time (Seconds)", min_value=0, value=0)
    with col2:
        amount = st.number_input("Amount ($)", min_value=0.0, value=100.0, step=10.0)
    
    st.markdown("**V1 to V28 Features**")
    pca_features = []
    cols = st.columns(4)
    for i in range(1, 29):
        val = cols[(i - 1) % 4].number_input(f"V{i}", value=0.0, format="%.4f")
        pca_features.append(val)

    if st.button("Predict Risk"):
        # Match the expected 30 features: Time, V1-V28, Amount
        feature_values = [time_sec] + pca_features + [amount]
        
        # Define feature names matching training data
        feature_names = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']
        input_df = pd.DataFrame([feature_values], columns=feature_names)
        
        # Pipeline automatically scales input_df and predicts
        prediction = fraud_model.predict(input_df)[0]
        probability = fraud_model.predict_proba(input_df)[0][1]

        st.divider()
        if prediction == 1:
            st.error(f"⚠️ **High Fraud Risk Detected!** (Fraud Probability: {probability:.2%})")
        else:
            st.success(f"✅ **Legitimate Transaction** (Fraud Probability: {probability:.2%})")

# --- TAB 2: Batch CSV Prediction ---
with tab2:
    st.subheader("Batch Input")
    uploaded_file = st.file_uploader("Upload CSV file (Must contain Time, V1-V28, and Amount columns)", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data Preview:", df.head())
        
        if st.button("Run Batch Detection"):
            # Ensure correct feature order
            feature_names = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']
            
            preds = fraud_model.predict(df[feature_names])
            probs = fraud_model.predict_proba(df[feature_names])[:, 1]
            
            df['Fraud_Prediction'] = preds
            df['Fraud_Probability'] = probs
            
            st.write("### Prediction Results")
            st.dataframe(df)
            
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Predictions CSV", data=csv, file_name="fraud_predictions.csv", mime="text/csv")
