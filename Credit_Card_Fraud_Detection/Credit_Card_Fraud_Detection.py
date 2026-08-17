import os
import joblib
import streamlit as st
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(page_title="Credit Card Fraud Detector", layout="wide")

# Load the entire pipeline using robust relative pathing
@st.cache_resource
def load_pipeline():
    model_path = os.path.join(os.path.dirname(__file__), 'models', 'fraud_model.joblib')
    return joblib.load(model_path)

fraud_model = load_pipeline()

# --- Helper Function for Risk Gauge ---
def render_risk_gauge(probability):
    """Generates an HTML/CSS string for a simple horizontal risk bar."""
    prob_percent = probability * 100
    
    if prob_percent >= 50:
        bar_color = "#dc3545"  # Red (High Risk)
        text_color = "white"
    elif prob_percent >= 15:
        bar_color = "#ffc107"  # Yellow (Medium Risk)
        text_color = "black"
    else:
        bar_color = "#28a745"  # Green (Low Risk)
        text_color = "white"

    display_width = max(prob_percent, 14.0)

    gauge_html = f"""
    <div style="width: 100%; background-color: #e0e0e0; border-radius: 10px; margin: 15px 0; border: 1px solid #ccc; overflow: hidden;">
        <div style="width: {display_width:.1f}%; background-color: {bar_color}; color: {text_color}; text-align: center; padding: 10px 0; font-weight: bold; font-size: 1.1rem; border-radius: 10px; transition: width 0.5s;">
            {prob_percent:.1f}% Risk
        </div>
    </div>
    """
    return gauge_html


def get_feature_contributions(pipeline, input_df, feature_names, top_n=5):
    """Calculates top features pushing probability UP or DOWN for a single prediction."""
    # Fallback to index positions if named steps differ
    scaler = pipeline.named_steps.get('scale', pipeline.steps[0][1])
    model = pipeline.named_steps.get('model', pipeline.steps[-1][1])
    
    # Scale input and multiply by model coefficients
    scaled_vals = scaler.transform(input_df)[0]
    coefs = model.coef_[0]
    contributions = scaled_vals * coefs
    
    df_contrib = pd.DataFrame({
        'Feature': feature_names,
        'Value': input_df.iloc[0].values,
        'Contribution': contributions
    })
    
    risk_drivers = df_contrib.sort_values(by='Contribution', ascending=False).head(top_n)
    risk_reducers = df_contrib.sort_values(by='Contribution', ascending=True).head(top_n)
    
    return risk_drivers, risk_reducers

# ----------------------------------------

st.title("💳 Credit Card Fraud Detection System")
st.markdown("Enter the 30 raw feature values or upload a CSV file to analyze transaction risk.")

tab1, tab2 = st.tabs(["Single Transaction", "Batch CSV Upload"])

feature_names = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']

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
        feature_values = [time_sec] + pca_features + [amount]
        input_df = pd.DataFrame([feature_values], columns=feature_names)
        
        prediction = fraud_model.predict(input_df)[0]
        probability = fraud_model.predict_proba(input_df)[0][1]

        st.divider()
        st.subheader("Analysis Results")

        col_metric, col_gauge = st.columns([1, 2])
        with col_metric:
            st.metric(label="Fraud Probability", value=f"{probability:.2%}")
        with col_gauge:
            st.markdown(render_risk_gauge(probability), unsafe_allow_html=True)

        if prediction == 1:
            st.error(f"⚠️ **High Fraud Risk Detected!** (Fraud Probability: {probability:.2%})")
        else:
            st.success(f"✅ **Legitimate Transaction** (Fraud Probability: {probability:.2%})")

        # --- Local Feature Explanations ---
        st.divider()
        st.subheader("🔍 Local Feature Explanations")
        st.caption("Key factors driving this specific transaction prediction score.")
        
        drivers, reducers = get_feature_contributions(fraud_model, input_df, feature_names)
        
        col_drivers, col_reducers = st.columns(2)
        with col_drivers:
            st.markdown("🚨 **Top Risk Drivers (Pushing Risk UP)**")
            st.dataframe(
                drivers.style.format({'Value': '{:.4f}', 'Contribution': '{:+.4f}'}),
                hide_index=True,
                use_container_width=True
            )
        with col_reducers:
            st.markdown("🛡️ **Top Risk Reducers (Lowering Risk)**")
            st.dataframe(
                reducers.style.format({'Value': '{:.4f}', 'Contribution': '{:+.4f}'}),
                hide_index=True,
                use_container_width=True
            )

# --- TAB 2: Batch CSV Prediction ---
with tab2:
    st.subheader("Batch Input")
    uploaded_file = st.file_uploader("Upload CSV file (Must contain Time, V1-V28, and Amount columns)", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data Preview:", df.head())
        
        if st.button("Run Batch Detection"):
            missing_cols = [col for col in feature_names if col not in df.columns]
            
            if missing_cols:
                st.error(f"❌ Missing required columns in CSV: `{', '.join(missing_cols)}`")
            else:
                preds = fraud_model.predict(df[feature_names])
                probs = fraud_model.predict_proba(df[feature_names])[:, 1]
                
                df['Fraud_Prediction'] = preds
                df['Fraud_Probability'] = probs
                
                st.write("### Prediction Results")
                st.dataframe(df)
                
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button("Download Predictions CSV", data=csv, file_name="fraud_predictions.csv", mime="text/csv")
