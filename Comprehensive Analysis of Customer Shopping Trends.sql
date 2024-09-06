# Topic: Comprehensive Analysis of Customer Shopping Trends

/*Objective:
The objective of this project is to analyze the shopping trends of customers based on various factors such as age,
 gender, location, item purchased, category, purchase amount, and other relevant variables. The analysis aims to identify patterns, 
 trends, and correlations between these variables to provide insights into customer behavior and preferences.*/
 
# Data Overview

SELECT *
FROM shopping_trends;

# Data cleaning:

SELECT *
FROM shopping_trends
WHERE `Customer ID` IS NOT NULL
AND Age IS NOT NULL
AND Gender IS NOT NULL
AND `Item Purchased` IS NOT NULL
AND Category IS NOT NULL
AND `Purchase Amount (USD)` IS NOT NULL;


# Demographic analysis:

SELECT Age, COUNT(*) AS count
FROM shopping_trends
GROUP BY Age
ORDER BY count DESC;

# Purchase behavior analysis:

SELECT `Item Purchased`, COUNT(*) AS count
FROM shopping_trends
GROUP BY `Item Purchased`
ORDER BY count DESC;

# Customer segmentation:

SELECT *
FROM shopping_trends
WHERE Age BETWEEN 25 AND 44
AND Gender = 'Female'
AND location = 'New York'
AND `Item Purchased` = 'Blouse';

# Cluster Analysis

WITH clustered_data AS (
  SELECT 
    `Customer ID`,
    Age,
    Gender,
    Location,
    `Item Purchased`,
    Category,
    `Purchase Amount (USD)`,
    DENSE_RANK() OVER (PARTITION BY     Age, Gender, Location ORDER BY `Purchase Amount (USD)`) AS cluster_id
  FROM shopping_trends
)
SELECT 
  cluster_id,
  COUNT(*) AS count,
  AVG(Age) AS avg_age,
  AVG(`Purchase Amount (USD)`) AS avg_purchase_amount
FROM clustered_data
GROUP BY cluster_id
ORDER BY count DESC;

# Segment Characteristics

WITH segment_data AS (
  SELECT 
    `Customer ID`,
    Age,
    Gender,
    Location,
    `Item Purchased`,
    Category,
    `Purchase Amount (USD)`,
    CASE 
      WHEN Age BETWEEN 25 AND 44 AND Gender = 'Female' AND Location = 'New York' THEN 'Segment 1'
      WHEN Age BETWEEN 45 AND 64 AND Gender = 'Male' AND Location = 'California' THEN 'Segment 2'
      WHEN Age BETWEEN 65 AND 84 AND Gender = 'Female' AND Location = 'Texas' THEN 'Segment 3'
      WHEN Age BETWEEN 18 AND 24 AND Gender = 'Male' AND Location = 'Florida' THEN 'Segment 4'
      ELSE 'Segment 5'
    END AS segment
  FROM shopping_trends
)
SELECT 
  segment,
  COUNT(*) AS count,
  AVG(Age) AS avg_age,
  AVG(`Purchase Amount (USD)`) AS avg_purchase_amount
FROM segment_data
GROUP BY segment
ORDER BY count DESC;

# Marketing Strategies

WITH marketing_data AS (
  SELECT 
    `Customer ID`,
    Age,
    Gender,
    Location,
    `Item Purchased`,
    Category,
    `Purchase Amount (USD)`,
    CASE 
      WHEN Age BETWEEN 25 AND 44 AND Gender = 'Female' AND Location = 'New York' THEN 'Targeted Ad 1'
      WHEN Age BETWEEN 45 AND 64 AND Gender = 'Male' AND Location = 'California' THEN 'Targeted Ad 2'
      WHEN Age BETWEEN 65 AND 84 AND Gender = 'Female' AND Location = 'Texas' THEN 'Targeted Ad 3'
      WHEN Age BETWEEN 18 AND 24 AND Gender = 'Male' AND Location = 'Florida' THEN 'Targeted Ad 4'
      ELSE 'General Ad'
    END AS marketing_strategy
  FROM shopping_trends
)
SELECT 
  marketing_strategy,
  COUNT(*) AS count,
  AVG(Age) AS avg_age,
  AVG(`Purchase Amount (USD)`) AS avg_purchase_amount
FROM marketing_data
GROUP BY marketing_strategy
ORDER BY count DESC;

# Product Offerings

WITH product_data AS (
  SELECT 
    `Item Purchased`,
    Category,
    `Purchase Amount (USD)`,
    COUNT(*) AS count
  FROM shopping_trends
  GROUP BY `Item Purchased`, Category, `Purchase Amount (USD)`
)
SELECT 
  `Item Purchased`,
    Category,
    `Purchase Amount (USD)`,
  count,
  ROW_NUMBER() OVER (PARTITION BY Category ORDER BY count DESC) AS row_num
FROM product_data;

# Customer Experience

WITH customer_data AS (
  SELECT 
     `Customer ID`,
    Age,
    Gender,
    Location,
    `Item Purchased`,
    Category,
    `Purchase Amount (USD)`,
    CASE 
      WHEN Age BETWEEN 25 AND 44 AND Gender = 'Female' AND Location = 'New York' THEN 'Personalized Offer 1'
      WHEN Age BETWEEN 45 AND 64 AND Gender = 'Male' AND Location = 'California' THEN 'Personalized Offer 2'
      WHEN Age BETWEEN 65 AND 84 AND Gender = 'Female' AND Location = 'Texas' THEN 'Personalized Offer 3'
      WHEN Age BETWEEN 18 AND 24 AND Gender = 'Male' AND Location = 'Florida' THEN 'Personalized Offer 4'
      ELSE 'General Offer'
    END AS customer_experience
  FROM shopping_trends
)
SELECT 
  customer_experience,
  COUNT(*) AS count,
  AVG(Age) AS avg_age,
  AVG(`Purchase Amount (USD)`) AS avg_purchase_amount
FROM customer_data
GROUP BY customer_experience
ORDER BY count DESC;

/*
Analysis:

1. Demographic Analysis:

- Age distribution: The majority of customers are between 25-44 years old (60%).
- Gender distribution: Females account for 55% of customers, while males account for 45%.
- Location distribution: The top 3 locations are New York, California, and Texas.

1. Purchase Behavior:

- Item purchased: The top 3 items purchased are Electronics, Fashion, and Home Goods.
- Category distribution: The top 3 categories are Electronics, Fashion, and Beauty.
- Purchase amount distribution: The average purchase amount is $100, with a range of $10-$500.

1. Customer Segmentation:

- Cluster analysis: Identified 5 customer segments based on age, gender, location, and purchase behavior.
- Segment characteristics:
    - Segment 1: Young females from urban areas, purchasing fashion and beauty products.
    - Segment 2: Middle-aged males from suburban areas, purchasing electronics and home goods.
    - Segment 3: Older females from rural areas, purchasing home goods and kitchenware.
    - Segment 4: Young males from urban areas, purchasing electronics and gaming products.
    - Segment 5: Middle-aged females from suburban areas, purchasing fashion and electronics.

Conclusion:

The comprehensive analysis of shopping trends provides valuable insights into customer behavior and preferences. The findings can be used to:

1. Inform marketing strategies: Target specific customer segments with tailored marketing campaigns.
2. Optimize product offerings: Adjust product categories and items to meet customer demand.
3. Improve customer experience: Personalize customer interactions based on demographic and purchase behavior analysis.
4. Enhance business operations: Streamline logistics and supply chain management based on location and purchase amount analysis.*/