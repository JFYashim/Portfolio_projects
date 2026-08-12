# NYC Taxi Fare Prediction

**Author & Lead Data Scientist:** Jonathan Felix Yashim  
**GitHub:** [@JFYashim](https://github.com/JFYashim)  
**Role:** Lead Data Analyst / Data Scientist  
**Methodology:** Google PACE Framework (Plan, Analyze, Construct, Execute)  

---

## Project Overview

An end-to-end machine learning project analyzing the 2017 Yellow Taxi Trip Dataset to build predictive models for estimating taxi fare amounts in New York City. This repository demonstrates data preprocessing, feature engineering, and model evaluation comparing Linear Regression against a tuned Random Forest Regressor.

🚀 **Live Interactive Notebook:** [NYC_Taxi_Fare_Prediction.ipynb](https://github.com/JFYashim/Portfolio_projects/blob/main/NYC_Taxi_Fare_Prediction/Notebook/NYC_Taxi_Fare_Prediction.ipynb)

* **Dataset Scale & Prep:** Cleaned and extracted spatial and temporal attributes across 22,699 trip records spanning 18 initial specifications, achieving high data quality.
* **Primary Pricing Drivers:** Trip distance and trip duration heavily dominate taxi fares, accounting for over 96% of feature importance in price prediction.
* **Target Variable Strategy:** Evaluated directly on base `fare_amount` (excluding extra surcharges, tolls, and tips) to eliminate target leakage.
* **Feature Engineering:** Extracted `duration_minutes`, `hour_of_day`, `day_of_week`, and `month` from timestamps, and applied One-Hot Encoding to categorical location IDs and rate codes.

---

## Business Context

Accurate fare estimation is essential for ride-hailing platforms, taxi services, and passengers seeking pricing transparency. Given fluctuating demand patterns and varying traffic conditions across New York City, an analytical pricing model is required to protect driver earnings while maintaining predictable customer rates.

### Core Problem Statement
How can the business optimize fare estimation and trip cost modeling to deliver highly accurate pre-ride price predictions while isolating key operational cost drivers?

### Research Questions
* **Distance vs. Duration:** How strongly do `trip_distance` and `duration_minutes` combine to drive final fare amounts across NYC boroughs?
* **Ratecode Premiums:** What is the financial impact of special rate codes (e.g., JFK airport flat rates) on base fare predictions?
* **Temporal Variance:** How do pickup hours (`hour_of_day`) and days of the week impact trip duration and overall fare distribution?

---

## Model Performance & Metric Summary

All algorithms were evaluated using standard regression metrics on scaled numerical features:

| Model Name | MAE ($) | RMSE ($) | R² Score |
| :--- | :--- | :--- | :--- |
| **Linear Regression (Baseline)** | 1.83 | 3.08 | 0.9208 |
| **Random Forest Regressor (Tuned)** | **0.38** | **1.50** | **0.9813** |

---

## Analytical Findings

* **Trip Distance Dominance:** Trip distance is the primary metric driving fare calculations, contributing ~78.7% of total feature importance in the Random Forest model.
* **Duration Impact:** Trip duration in minutes represents the second largest driver (~17.5% importance), effectively capturing traffic delay surcharges.
* **Ratecode Influence:** Special rate codes (`RatecodeID`) account for ~2.8% combined feature importance, primarily capturing fixed-rate airport transfers.

---

## Strategic Recommendations

1. **Automate Pre-Ride Quotes:** Deploy the tuned Random Forest Regressor model ($0.38 MAE) to generate automated, real-time fare estimates for passengers before ride confirmation.
2. **Isolate Traffic Factors:** Incorporate dynamic route duration estimates alongside raw trip distance to improve pricing accuracy during peak congestion hours.
3. **Standardize Special Rates:** Maintain explicit categorical encoding for airport and out-of-city rate codes to prevent pricing anomalies on non-standard routes.

---

## Repository Structure

```text
NYC_Taxi_Fare_Prediction/
├── Data/                       # Raw and processed dataset files
├── Notebook/
│   └── NYC_Taxi_Fare_Prediction.ipynb   # Main Jupyter Notebook
├── nyc_taxi_rf_model.pkl       # Saved Random Forest model
├── scaler.pkl                  # Fitted StandardScaler object
└── README.md                   # Project documentation
