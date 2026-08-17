# Credit Card Fraud Detection Pipeline

An end-to-end machine learning solution built using Google's **PACE (Plan, Analyze, Construct, Execute)** framework to identify fraudulent credit card transactions and support real-time risk assessment.

**Author:** Jonathan Felix Yashim  
**Role:** Lead Data Scientist / Data Analyst  

---

## Business Core Problem

Credit card fraud poses a severe operational and financial challenge for payment processors and financial institutions:

* **Direct Financial Losses:** Undetected fraudulent transactions lead to chargeback penalties, stolen capital, and increased insurance premiums.
* **Customer Friction vs. Protection:** Blocking legitimate transactions (False Positives) damages customer trust, while failing to block fraud (False Negatives) leads to unrecoverable losses.
* **Extreme Class Imbalance:** Fraud accounts for less than **0.2%** of overall transaction volume (~1 in 600 transactions). Standard accuracy metrics fail here, as a model predicting "100% legitimate" achieves 99.8% accuracy while missing every single fraud attempt.

**Project Objective:** Build a cost-sensitive machine learning pipeline that maximizes fraud capture rate (**Recall**) while providing local feature explanations to help analysts investigate flagged transactions efficiently.

---

## Repository Structure

```text
credit-card-fraud-detection/
├── models/
│   └── fraud_model.joblib       # Serialized StandardScaler + Logistic Regression pipeline
├── app.py                       # Interactive Streamlit web app (Single & Batch prediction)
├── credit_card_fraud.ipynb      # EDA, model training, and performance evaluation
├── requirements.txt             # Python environment dependencies
└── README.md                    # Complete project documentation

```

Executive SummaryThis project cleans raw transactional data, addresses class imbalance via cost-sensitive learning (class_weight='balanced'), and trains a scikit-learn pipeline capable of catching 89.0% of all fraudulent events while maintaining an Average Precision (PR-AUC) score of 0.677.Dataset Profile & Exploratory AnalysisThe dataset originates from the European cardholder transaction benchmark dataset (mlg-ulb/creditcardfraud).MetricRaw Dataset ValuePost-Deduplication ValueTotal Transactions284,807283,726Duplicate Rows Removed01,081Missing Values00Legitimate Transactions (Class 0)284,315 (99.827%)283,253 (99.833%)Fraudulent Transactions (Class 1)492 (0.173%)473 (0.167%)Financial MetricsLegitimate Median Amount: $22.00Fraudulent Median Amount: $9.25Modeling MethodologyPlaintextRaw Input Data ➔ Deduplication ➔ Stratified Train/Test Split (75/25) ➔ StandardScaler ➔ Balanced Logistic Regression
Preprocessing: Exact duplicate records (1,081 rows) were removed prior to modeling to prevent data leakage between train and test sets.Data Splitting: Stratified 75/25 train-test split to preserve class distribution across folds.Training Set: 212,794 transactionsTest Set: 70,932 transactions (118 fraud cases; 0.166% fraud rate)Pipeline Architecture:Feature Scaling: StandardScaler applied to normalize feature magnitudes (Time, V1–V28, Amount).Algorithm: LogisticRegression with class_weight='balanced' to weight positive fraud instances heavily during gradient optimization.Performance & EvaluationTest Set Metrics (at Default 0.5 Decision Threshold)MetricScore / OutputDescriptionRecall (Sensitivity)89.0%Caught 105 out of 118 fraud cases in the test set.Average Precision (PR-AUC)0.677Summary measure across all operational decision thresholds.Precision5.5%Share of flagged transactions that were actual fraud.False Positives1,806Legitimate transactions flagged for review.Classification ReportPlaintext              precision    recall  f1-score   support

  Legitimate       1.00      0.97      0.99     70814
       Fraud       0.05      0.89      0.10       118

    accuracy                           0.97     70932
   macro avg       0.53      0.93      0.55     70932
weighted avg       1.00      0.97      0.99     70932
Deployment Artifact & Web InterfaceThe trained pipeline is deployed via a Streamlit web interface (app.py), enabling both manual transaction risk assessment and batch CSV processing.Saved Path: models/fraud_model.joblibExpected Input Vector: 30 numerical features ordered as ['Time', 'V1', 'V2', ..., 'V28', 'Amount'].
