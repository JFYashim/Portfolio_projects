import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Page configuration
st.set_page_config(
    page_title="Salifort Motors - Employee Retention Predictor",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Salifort Motors: Employee Retention Analytics & Churn Predictor")
st.markdown("""
This application uses a Random Forest Machine Learning model to evaluate employee retention risk 
and identify key drivers of turnover within Salifort Motors.
""")

# Load dataset and train baseline model
@st.cache_resource
def load_and_train_model():
    # Synthetic data generation matching Salifort Motors schema for standalone execution
    np.random.seed(42)
    n_samples = 1000
    
    data = pd.DataFrame({
        'satisfaction_level': np.random.uniform(0.1, 1.0, n_samples),
        'last_evaluation': np.random.uniform(0.3, 1.0, n_samples),
        'number_project': np.random.randint(2, 8, n_samples),
        'average_montly_hours': np.random.randint(96, 310, n_samples),
        'time_spend_company': np.random.randint(2, 10, n_samples),
        'Work_accident': np.random.choice([0, 1], n_samples, p=[0.85, 0.15]),
        'promotion_last_5years': np.random.choice([0, 1], n_samples, p=[0.98, 0.02]),
        'salary': np.random.choice(['low', 'medium', 'high'], n_samples, p=[0.45, 0.45, 0.10])
    })
    
    # Target rule approximation based on PACE insights
    churn_conditions = (
        (data['average_montly_hours'] > 240) | 
        (data['number_project'] >= 6) | 
        ((data['time_spend_company'] == 4) & (data['promotion_last_5years'] == 0))
    )
    data['left'] = np.where(churn_conditions, 1, 0)
    
    # Encoding
    salary_map = {'low': 0, 'medium': 1, 'high': 2}
    data['salary_encoded'] = data['salary'].map(salary_map)
    
    features = [
        'satisfaction_level', 'last_evaluation', 'number_project',
        'average_montly_hours', 'time_spend_company', 'Work_accident',
        'promotion_last_5years', 'salary_encoded'
    ]
    
    X = data[features]
    y = data['left']
    
    rf = RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42)
    rf.fit(X, y)
    
    return rf, features

model, feature_names = load_and_train_model()

# Sidebar - User Inputs
st.sidebar.header("📊 Input Employee Metrics")

satisfaction = st.sidebar.slider("Satisfaction Level", 0.0, 1.0, 0.65, 0.01)
last_evaluation = st.sidebar.slider("Last Evaluation Score", 0.0, 1.0, 0.72, 0.01)
number_project = st.sidebar.slider("Number of Projects Assigned", 2, 7, 4)
monthly_hours = st.sidebar.slider("Average Monthly Hours Worked", 90, 320, 200)
tenure = st.sidebar.slider("Tenure at Company (Years)", 1, 10, 3)
work_accident = st.sidebar.selectbox("Work Accident History", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
promotion = st.sidebar.selectbox("Promoted in Last 5 Years", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
salary_str = st.sidebar.selectbox("Salary Bracket", ["low", "medium", "high"])

salary_map = {'low': 0, 'medium': 1, 'high': 2}
salary_encoded = salary_map[salary_str]

# Create input frame
input_data = pd.DataFrame([[
    satisfaction, last_evaluation, number_project,
    monthly_hours, tenure, work_accident,
    promotion, salary_encoded
]], columns=feature_names)

# Make Prediction
prediction = model.predict(input_data)[0]
probability = model.predict_proba(input_data)[0][1]

# Display Results
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Retention Assessment")
    risk_pct = probability * 100
    
    if prediction == 1:
        st.error(f"⚠️ **High Churn Risk Detected**")
        st.metric(label="Predicted Risk Score", value=f"{risk_pct:.1f}%")
        st.warning("Action Recommended: Review workload metrics and schedule a stay interview.")
    else:
        st.success(f"✅ **Low Churn Risk**")
        st.metric(label="Predicted Risk Score", value=f"{risk_pct:.1f}%")
        st.info("Employee metrics fall within stable retention bounds.")

with col2:
    st.subheader("📌 Key Workplace Risk Factors")
    if monthly_hours > 240:
        st.write("🔴 **Overwork Warning:** Monthly hours exceed 240 hours/month.")
    if number_project >= 6:
        st.write("🔴 **Project Overload:** Assigned to 6 or more simultaneous projects.")
    if tenure == 4 and promotion == 0:
        st.write("🟡 **Career Stagnation:** 4-year tenure mark reached without recent promotion.")
    if number_project == 2 and monthly_hours < 150:
        st.write("🔵 **Underutilization:** Low engagement risk (2 projects, <150 hrs).")
    if monthly_hours <= 240 and number_project < 6 and not (tenure == 4 and promotion == 0):
        st.write("🟢 No immediate PACE risk flags triggered for this profile.")