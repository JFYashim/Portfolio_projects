# Predicting Credit Card Fraud Transactions for a Fintech Payment Company

## Author

**Jonathan Felix Yashim**  
GitHub: [@JFYashim](https://github.com/JFYashim)

## Overview

This project develops and evaluates a machine-learning baseline for identifying potentially fraudulent credit-card transactions. It is framed around a fintech payments company that must prevent fraud without unnecessarily interrupting legitimate customer payments.

The analysis follows the PACE framework: Plan, Analyse, Construct, and Execute.

 **Research question:** How accurately can machine-learning models identify fraudulent card transactions while minimising false alerts on legitimate customer payments?

## Business problem

Fraudulent card transactions create financial losses for a fintech company and its customers. However, flagging too many genuine transactions can lead to unnecessary payment declines, poor customer experience, and lost revenue.

The aim is to build a fraud-risk model that can:

- Identify a high proportion of fraudulent transactions
- Prioritise high-risk transactions for review or extra authentication
- Balance fraud prevention against false alerts

This model is intended as an alert-ranking and decision-support tool, not an automatic payment-decline system.

## Dataset

Source: [Kaggle – Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

| Item | Description |
| --- | --- |
| Records | 284,807 transactions |
| Fraud cases | 492 (approximately 0.173%) |
| Target | `Class`: `0` = legitimate, `1` = fraud |
| Features | `Time`, `V1`–`V28`, and `Amount` |

### Data dictionary

| Column(s) | Meaning |
| --- | --- |
| `Time` | Seconds elapsed since the first transaction. |
| `V1`–`V28` | Anonymous PCA-transformed transaction features. |
| `Amount` | Transaction value. |
| `Class` | Transaction label: `0` legitimate, `1` fraud. |

## PACE framework

### Plan

- Define fraud detection as a binary classification task.
- Focus on precision and recall rather than accuracy, because fraud is rare.
- Use a stratified train/test split.

### Analyse

- Check data shape, missing values, duplicates, and class distribution.
- Visualise class imbalance.
- Compare transaction amounts for fraud and legitimate transactions.

### Construct

- Remove 1,081 duplicate records.
- Split data into 75% training and 25% test data.
- Scale features using `StandardScaler`.
- Train a class-weighted Logistic Regression model.

### Execute

- Evaluate using a classification report, confusion matrix, precision–recall curve, and average precision.
- Translate results into fintech business recommendations.

## Methodology

A Logistic Regression model was trained using scaled transaction features. Class weighting was applied because fraudulent transactions are rare, helping the model give greater attention to fraud cases.

## Results

The model was evaluated on 70,932 test transactions, including 118 fraud cases.

| Metric | Result |
| --- | ---: |
| Fraud recall | 89.0% |
| Fraud precision | 5.5% |
| False alerts | 1,806 |
| Average precision | 0.677 |

## Key insights

- Fraud represents only 0.173% of all transactions.
- The model caught 105 of 118 fraudulent test transactions.
- Only 5.5% of its fraud alerts were genuine fraud, creating a large review workload.
- Accuracy alone is not useful for this problem.
- The median fraud amount was lower than the legitimate median amount, so amount alone is not a reliable fraud rule.

## Recommendations

1. Use the model to rank risk, not automatically decline every flagged transaction.
2. Route high-risk transactions to extra authentication or manual review.
3. Choose the fraud threshold with business teams, based on fraud loss, customer impact, and review cost.
4. Monitor precision, recall, alert volumes, and transaction patterns over time.
5. Add production features such as device, merchant category, transaction velocity, customer history, and location.

## Limitations

- `V1`–`V28` are anonymised, so their business meaning cannot be explained.
- This is a baseline learning project, not a production fraud system.
- The data is historical and lacks live transaction context.
- A real deployment should use time-based validation rather than only a random train/test split.
- Production use would require security, fairness, compliance, monitoring, and human-review processes.
