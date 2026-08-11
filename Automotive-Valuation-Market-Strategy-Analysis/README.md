# Automotive Valuation & Market Strategy Analysis

**Author & Lead Data Scientist:** Jonathan Felix Yashim  
**GitHub:** [@JFYashim](https://github.com/JFYashim)  
**Role:** Lead Data Analyst / Data Scientist  
**Methodology:** Google PACE Framework (Plan, Analyze, Construct, Execute)

---

## Project Overview

This project provides an end-to-end data analysis and valuation strategy model built on 5,500 automobile records. The objective is to establish an empirical framework for pre-owned vehicle pricing, trade-in appraisals, and regional inventory allocation to maximize gross profit margins and reduce days-on-market.

> 🚀 **Live Interactive App:** [Vehicle Valuation App](https://jfy-vehicle-valuation-app.streamlit.app)


* **Dataset Scale & Prep:** Cleaned and imputed missing values across 5,500 vehicle records spanning 18 specifications, achieving 100% data retention.
* **Primary Pricing Drivers:** Vehicle age and mileage dominate depreciation, while engine size and horsepower show negligible impact on final resale prices.
* **Condition Penalties:** Recorded accident histories reduce average resale prices by 59% to 73%.
* **Feature Engineering:** Derived `Vehicle_Age` and applied frequency encoding to high-cardinality features (`Make`, `Model`, `Location`, `Color`) for predictive modeling readiness.

---


## Business Context

A nationwide used-car dealership network is transitioning from subjective, intuition-based trade-in appraisals to an automated, data-driven pricing model. Given consumer access to transparent online pricing platforms, an analytical framework is required to protect profit margins and accelerate inventory turnover.

---

## Core Problem Statement

How can the business optimize unit pricing, trade-in valuations, and regional inventory distribution to maximize gross profit margins while minimizing days-on-market for pre-owned vehicles?

---

## Research Questions

* **The Power Premium:** Do larger engines (`Engine_Size`) and higher horsepower (`Horsepower`) command higher selling prices across different body styles?
* **Depreciation & Mileage:** How strongly do `Vehicle_Age` and total `Mileage` combine to drive down vehicle resale value?
* **Accident Penalty:** What is the financial impact of a recorded accident (`Accident_History`) on listing prices?
* **Regional Preferences:** How does vehicle demand vary by location (`Location_Freq`), and do regional markets favor specific body styles (`Body_Type`)

## Data Hygiene & Imputation Summary

All missing data points were resolved using domain-appropriate statistical imputation methods:

| Feature Category | Missing Count | Imputation Method | Post-Clean Missing |
| :--- | :--- | :--- | :--- |
| `Transmission` | 827 | Most Frequent Value (Mode) | 0 |
| `Engine_Size` | 844 | Grouped Median (`Make` / `Model`) | 0 |
| `Horsepower` / `Torque` | 800 / 799 | Grouped Median (`Make` / `Model`) | 0 |
| `Accident_History` | 812 | Imputed as 0 (No Logged Accidents) | 0 |
| `Service_History` | 855 | Grouped as 'Unknown' | 0 |

---

## Analytical Findings

* **Engine Performance vs. Price:** Engine size and horsepower display negligible correlation with selling price across body types (SUVs: -0.13 correlation for engine size; Sedans: -0.07). Performance metrics alone do not justify price markups.
* **Depreciation Impact:** Vehicle age (-0.80 correlation) and mileage (-0.68 correlation) are the two single largest drivers of price drops.
* **Accident Penalty:** Clean-history vehicles average **$15,530** (median **$12,916**), whereas vehicles with recorded accidents average **$6,300** (median **$3,481**).
* **Regional Demand Trends:** Inventory demand is stable across regional locations, with Sedans making up ~40% of demand across all top markets.

---

## Key Visualizations

### 1. Horsepower vs. Selling Price Across Body Types
![Horsepower vs Selling Price](Visuals/Horsepower%20vs.%20Selling%20Price%20Across%20Body%20Types.png)

### 2. Vehicle Age vs. Selling Price Depreciation
![Vehicle Age vs Selling Price](Visuals/Vehicle%20Age%20vs.%20Selling%20Price%20Depreciation.png)
---
## Strategic Recommendations

1. **Automate Appraisal Baselines:** Set trade-in offers and list prices primarily on `Vehicle_Age` and `Mileage` rather than engine displacement or horsepower options.
2. **Enforce Condition Discounts:** Apply an immediate 50%–60% baseline discount on trade-ins with recorded accident histories (`Accident_History = 1`) to ensure realistic resale margins and speed up turn time.
3. **Condition-Based Stock Distribution:** Base regional inventory transfers on vehicle age, mileage, and condition rather than shifting stock based on location alone.

---

## Repository Structure

```text
Automotive-Valuation-Market-Strategy-Analysis/
├── Data/                     # Raw and processed datasets
├── NoteBooks/                # Jupyter notebook analysis
├── Visuals/                  # Key generated visualization charts
│   ├── Horsepower vs. Selling Price Across Body Types.png
│   └── Vehicle Age vs. Selling Price Depreciation.png
├── README.md                 # Project documentation & findings
├── requirements.txt          # Python dependencies
└── vehicle_valuation_app.py  # Interactive Streamlit valuation app
