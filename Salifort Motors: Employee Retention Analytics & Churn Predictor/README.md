# Salifort Motors: Employee Retention Analytics & Churn Predictor

## 👤 Author & Project Metadata
* **Author:** Jonathan Felix Yashim
* **Role:** Lead Data Analyst & Data Scientist
* **GitHub Profile:** [@JFYashim](https://github.com/JFYashim)
* **Portfolio Repository:** [JFYashim/Portfolio_projects](https://github.com/JFYashim/Portfolio_projects)
---

An end-to-end machine learning project utilizing the **PACE framework (Plan, Analyze, Construct, Execute)** to identify key drivers of employee turnover and predict retention risk. Features an interactive web dashboard built with **Streamlit** for real-time employee risk assessment.

---

## 📸 Interactive Web App
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)

> **Live Demo:** Access the hosted application to interactively adjust employee metrics (monthly hours, project load, tenure) and compute immediate retention risk scores.

---

## 📌 Project Overview & Problem Statement
Salifort Motors faced high voluntary turnover across key technical and support departments. The objective of this project is twofold:
1. **Uncover Core Workplace Drivers:** Determine why high-performing and mid-tenure employees leave.
2. **Predictive HR Intervention:** Build a production classification pipeline to flag high-risk employee profiles before they resign.

Using historical data from 11,991 employees (post-deduplication), we evaluated multiple machine learning models. The final **Random Forest Ensemble** achieved an **F1-Score of 0.96** and a **Recall of 0.93**, successfully identifying 93% of departing staff prior to exit.

---

## 🔍 Key Business Insights (PACE: Analyze Phase)

* 🔴 **Severe Burnout Among High Performers:** Staff logging **>240 hours/month** or handling **6+ projects** experienced a **>90% turnover rate**. Despite maintaining high evaluation scores (avg. 0.87), satisfaction dropped below 0.15.
* 🟡 **Career Stagnation at Year 4:** Turnover peaks sharply at **4 years of tenure (35.4% churn rate)**, particularly among staff without recent promotions or salary adjustments.
* 🔵 **Underutilization Risk:** A distinct secondary cluster of departures occurred among staff assigned to only **2 projects** with low monthly hours (130–150 hrs), driven by low engagement.

---

## 🛠️ Machine Learning Performance (PACE: Construct Phase)

Models were evaluated using 5-Fold Cross-Validation tuned specifically for minority class F1-Score:

| Model | Precision | Recall (Churn Class) | F1-Score | Accuracy | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | 0.79 | 0.81 | 0.80 | 0.82 | Baseline |
| **Decision Tree (`max_depth=3`)** | 0.88 | 0.92 | 0.90 | 0.93 | Rule Extraction |
| **Random Forest (Tuned)** | **0.98** | **0.93** | **0.96** | **0.98** | **Production Deployed** |

---

## 🚀 Streamlit Deployment Guide

### Project File Structure
```text
Portfolio_projects/
└── Salifort_Motors_Employee_Retention/
    ├── app.py                     # Streamlit interactive application
    ├── requirements.txt           # Python dependency manifest
    ├── random_forest_model.pkl    # Serialized Random Forest model artifact
    ├── data/
    │   └── HR_comma_sep.csv       # Employee dataset
    └── notebook/
        └── Salifort_Motors.ipynb  # End-to-end Jupyter Notebook (PACE Framework)
