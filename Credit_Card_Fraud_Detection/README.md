# 💳 Credit Card Fraud Detection System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://jfy-credit-card-fraud-detection.streamlit.app/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

An end-to-end machine learning solution built using Google's **PACE** (Plan, Analyze, Construct, Execute) framework to identify fraudulent credit card transactions and support real-time risk assessment.

🔗 **Live Web Application:** [Credit card fraud detection System](https://jfy-credit-card-fraud-detection.streamlit.app/)

**Author:** Jonathan Felix Yashim  
**Role:** Lead Data Scientist / Data Analyst  

---

## 📌 Business Problem

Credit card fraud poses severe financial and operational challenges for financial institutions:
* **Extreme Class Imbalance:** Fraud accounts for less than **0.2%** of overall transaction volume (~1 in 600 transactions). Standard accuracy metrics fail here (a dummy model predicting "100% legitimate" achieves 99.8% accuracy while missing every fraud event).
* **Customer Friction vs. Protection:** False positives damage customer trust, while false negatives cause unrecoverable capital losses.

**Project Objective:** Build a cost-sensitive machine learning system that maximizes fraud capture rate (**Recall**) while providing local feature explanations to help fraud analysts investigate flagged transactions efficiently.

---

## Executive Summary
This project processes raw payment data and applies an automated risk model specifically tuned to detect rare threat patterns. It successfully catches 89% of all fraudulent transactions while keeping false alarms low, protecting revenue without causing unnecessary friction for legitimate customers.

---

## Dataset Profile & Exploratory Analysis
The dataset originates from the European cardholder transaction benchmark dataset (mlg-ulb/creditcardfraud).

* **Total Transactions:** 284,807 (Raw) ➔ 283,726 (Post-Deduplication)

* **Duplicate Rows Removed:** 1,081

* **Missing Values:** 0

* **Legitimate Transactions (Class 0):** 284,315 (99.827%) ➔ 283,253 (99.833%)

* **Fraudulent Transactions (Class 1):** 492 (0.173%) ➔ 473 (0.167%)

---

## Financial Metrics
* **Legitimate Median Amount:** $22.00

* **Fraudulent Median Amount:** $9.25

---

## Modeling Methodology
Raw Input Data ➔ Deduplication ➔ Stratified Train/Test Split (75/25) ➔ StandardScaler ➔ Balanced Logistic Regression

1.  **Preprocessing:** Exact duplicate records (1,081 rows) were removed prior to modeling to prevent data leakage between train and test sets.
2. **Data Splitting:** Stratified 75/25 train-test split to preserve class distribution across folds.

 * **Training Set:** 212,794 transactions

 * **Test Set:** 70,932 transactions (118 fraud cases; 0.166% fraud rate)
3. **Pipeline Architecture:**
 * **Feature Scaling:** StandardScaler applied to normalize feature magnitudes (Time, V1–V28, Amount).
 * **Algorithm:** LogisticRegression with class_weight='balanced' to weight positive fraud instances heavily during gradient optimization.

---

## 🚀 Key Performance & Metrics

Using cost-sensitive learning (`class_weight='balanced'`), the model was evaluated on **70,932 unseen test transactions** (118 fraud cases):

| Metric | Score / Value | Description |
| :--- | :--- | :--- |
| **Recall (Sensitivity)** | **89.0%** | Caught **105 out of 118** actual fraud cases in test set |
| **PR-AUC (Avg Precision)** | **0.677** | Summary measure across all operational decision thresholds |
| **Accuracy** | **97.0%** | Overall correct predictions across both classes |
| **False Positives** | **1,806** | Legitimate transactions flagged for analyst review |

---

## 🛠️ Pipeline & Web App Features

* **Real-time Single Scoring:** Enter 30 PCA features (`Time`, `V1`–`V28`, `Amount`) or load pre-configured test presets.
* **Local Feature Contributions:** Displays top features driving risk **UP** (drivers) or **DOWN** (reducers) for individual transactions.
* **Batch CSV Scoring:** Upload multi-row transaction files, view summary metrics, and download scored results with fraud probabilities.
* **Dual Path Resolution:** Robust relative path handling ensures seamless deployment on local machines and Streamlit Cloud.

---

## 📁 Repository Structure

```text
Credit_Card_Fraud_Detection/
├── models/
│   └── fraud_model.joblib       # Serialized StandardScaler + Logistic Regression pipeline
├── app.py                       # Interactive Streamlit web app (Single & Batch prediction)
├── credit_card_fraud.ipynb      # EDA, model training, and performance evaluation
├── requirements.txt             # Python environment dependencies
└── README.md                    # Complete project documentation
