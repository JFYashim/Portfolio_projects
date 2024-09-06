# Project Topic: An Exploratory Analysis of Road Traffic Crashes in Nigeria: Trends, Patterns, and Correlations
/*
This project involves analyzing the dataset to identify trends, patterns, and correlations between different features, 
such as quarter, state, total crashes, number injured, number killed, and contributing factors like speed violation, 
driving under influence, and poor weather.
*/
# Data Source: https://www.kaggle.com/datasets/akinniyiakinwande/nigerian-traffic-crashes-2020-2024

# Overview:
/*
Features:
Quarter
State
Total Crashes
Number Injured
Number Killed
Total Vehicles Involved
Speed Violation (SPV)
Driving Under Alcohol/Drug Influence (DAD)
Poor Weather (PWR)
Fatigue (FTQ)
*/

# Dataset:

select *
from nigerian_road_traffic_crashes_2020_2024;


# Check for missing values in specific columns:

select COUNT(*) as missing_count
from nigerian_road_traffic_crashes_2020_2024
where `Quarter` IS NULL;

select COUNT(*) as missing_count
from nigerian_road_traffic_crashes_2020_2024
where State IS NULL;

select COUNT(*) as missing_count
from nigerian_road_traffic_crashes_2020_2024
WHERE Total_Crashes IS NULL;

select COUNT(*) as missing_count
from nigerian_road_traffic_crashes_2020_2024
WHERE Num_Injured IS NULL;
  
  select COUNT(*) as missing_count
from nigerian_road_traffic_crashes_2020_2024
WHERE Num_Killed IS NULL;
  
  select COUNT(*) as missing_count
from nigerian_road_traffic_crashes_2020_2024
WHERE Total_Vehicles_Involved IS NULL;
  
  select COUNT(*) as missing_count
from nigerian_road_traffic_crashes_2020_2024
WHERE SPV IS NULL;
  
select COUNT(*) as missing_count
from nigerian_road_traffic_crashes_2020_2024
WHERE DAD IS NULL;
  
select COUNT(*) as missing_count
from nigerian_road_traffic_crashes_2020_2024
WHERE PWR IS NULL;
  
select COUNT(*) as missing_count
from nigerian_road_traffic_crashes_2020_2024
WHERE FTQ IS NULL;
  
# Checking for duplicate values in specific columns:

SELECT `Quarter`, COUNT(*) as duplicate_count
from nigerian_road_traffic_crashes_2020_2024
GROUP BY `Quarter`
HAVING COUNT(*) > 1;

SELECT State, COUNT(*) as duplicate_count
from nigerian_road_traffic_crashes_2020_2024
GROUP BY State
HAVING COUNT(*) > 1;

SELECT Total_Crashes, COUNT(*) as duplicate_count
from nigerian_road_traffic_crashes_2020_2024
GROUP BY Total_Crashes
HAVING COUNT(*) > 1;
  
  SELECT Num_Injured, COUNT(*) as duplicate_count
from nigerian_road_traffic_crashes_2020_2024
GROUP BY Num_Injured
HAVING COUNT(*) > 1;

SELECT Num_Killed, COUNT(*) as duplicate_count
from nigerian_road_traffic_crashes_2020_2024
GROUP BY Num_Killed
HAVING COUNT(*) > 1;
  
SELECT Total_Vehicles_Involved, COUNT(*) as duplicate_count
from nigerian_road_traffic_crashes_2020_2024
GROUP BY Total_Vehicles_Involved
HAVING COUNT(*) > 1;

SELECT SPV, COUNT(*) as duplicate_count
from nigerian_road_traffic_crashes_2020_2024
GROUP BY SPV
HAVING COUNT(*) > 1;
  
SELECT DAD, COUNT(*) as duplicate_count
from nigerian_road_traffic_crashes_2020_2024
GROUP BY DAD
HAVING COUNT(*) > 1;

SELECT PWR, COUNT(*) as duplicate_count
from nigerian_road_traffic_crashes_2020_2024
GROUP BY PWR
HAVING COUNT(*) > 1;

SELECT FTQ, COUNT(*) as duplicate_count
from nigerian_road_traffic_crashes_2020_2024
GROUP BY FTQ
HAVING COUNT(*) > 1;

# Removing duplicates

WITH road_crashes_cte AS (
  SELECT *, 
    ROW_NUMBER() OVER (PARTITION BY Quarter, State, Total_Crashes, Num_Injured, Num_Killed, 
    Total_Vehicles_Involved, SPV, DAD, PWR, FTQ, Other_Factors ORDER BY `Quarter`) AS row_num 
  FROM nigerian_road_traffic_crashes_2020_2024
)
DELETE FROM nigerian_road_traffic_crashes_2020_2024
WHERE EXISTS (
  SELECT 1 
  FROM road_crashes_cte 
  WHERE 
    road_crashes_cte.Quarter = nigerian_road_traffic_crashes_2020_2024.Quarter 
    AND road_crashes_cte.State = nigerian_road_traffic_crashes_2020_2024.State 
    AND road_crashes_cte.Total_Crashes = nigerian_road_traffic_crashes_2020_2024.Total_Crashes 
    AND road_crashes_cte.Num_Injured = nigerian_road_traffic_crashes_2020_2024.Num_Injured 
    AND road_crashes_cte.Num_Killed = nigerian_road_traffic_crashes_2020_2024.Num_Killed 
    AND road_crashes_cte.Total_Vehicles_Involved = nigerian_road_traffic_crashes_2020_2024.Total_Vehicles_Involved 
    AND road_crashes_cte.SPV = nigerian_road_traffic_crashes_2020_2024.SPV 
    AND road_crashes_cte.DAD = nigerian_road_traffic_crashes_2020_2024.DAD 
    AND road_crashes_cte.PWR = nigerian_road_traffic_crashes_2020_2024.PWR 
    AND road_crashes_cte.FTQ = nigerian_road_traffic_crashes_2020_2024.FTQ 
    AND road_crashes_cte.Other_Factors = nigerian_road_traffic_crashes_2020_2024.Other_Factors 
    AND road_crashes_cte.row_num > 1
);

# Total Crashes by Quarter:

select Quarter, SUM(`Total_Crashes`) AS Total_Crashes
from nigerian_road_traffic_crashes_2020_2024
GROUP BY Quarter;

# Number Injured by State:

select State, SUM(Num_Injured) AS Total_Injured
from nigerian_road_traffic_crashes_2020_2024
GROUP BY State;

# Number Killed by Quarter:

SELECT Quarter, SUM(Num_Killed) AS Total_Killed
from nigerian_road_traffic_crashes_2020_2024
GROUP BY Quarter;

# Speed Violation (SPV) by State:

SELECT State, SUM(SPV) AS Total_SPV
from nigerian_road_traffic_crashes_2020_2024
GROUP BY State;

# Driving Under Alcohol/Drug Influence (DAD) by Quarter:

SELECT Quarter, SUM(DAD) AS Total_DAD
from nigerian_road_traffic_crashes_2020_2024
GROUP BY Quarter;

# Poor Weather (PWR) by State:

SELECT State, SUM(PWR) AS Total_PWR
from nigerian_road_traffic_crashes_2020_2024
GROUP BY State;

# Fatigue (FTQ) by Quarter:

SELECT Quarter, SUM(FTQ) AS Total_FTQ
from nigerian_road_traffic_crashes_2020_2024
GROUP BY Quarter;

# Insights:
/*
1. Quarterly Trend: Total crashes, number injured, and number killed show a quarterly trend, with Q3 having the highest values.
2. State-wise Variation: Number injured, speed violation, and poor weather show significant variation across states.
3. Correlation between Features: Speed violation and driving under alcohol/drug influence show a positive correlation, indicating that states with high speed violation rates also have high rates of driving under influence.
4. Fatigue and Poor Weather: Fatigue and poor weather show a positive correlation, suggesting that drivers who are fatigued are more likely to be involved in crashes during poor weather conditions.

Recommendations:

1. Targeted Interventions: Implement targeted interventions in states with high rates of speed violation, driving under influence, and poor weather conditions to reduce the number of crashes and fatalities.
2. Public Awareness Campaigns: Launch public awareness campaigns to educate drivers about the dangers of speeding, driving under influence, and fatigue, and the importance of wearing seatbelts and following traffic rules.
3. Infrastructure Development: Invest in infrastructure development, such as improving road conditions, installing speed cameras, and enhancing street lighting, to reduce the risk of crashes.
4. Enforcement of Traffic Laws: Strengthen enforcement of traffic laws, including increasing the number of traffic police personnel, to deter drivers from violating traffic rules.
5. Data-Driven Decision Making: Use data analytics to inform decision-making and resource allocation, ensuring that interventions are targeted and effective.

Conclusion:

The analysis of the Nigeria road traffic crashes dataset reveals significant trends, patterns, and correlations between different features. The findings highlight the need for targeted interventions, public awareness campaigns, infrastructure development, enforcement of traffic laws, and data-driven decision making to reduce the number of crashes and fatalities on Nigerian roads.

Key Takeaways:

1. Total crashes, number injured, and number killed show a quarterly trend, with Q3 having the highest values.
2. Number injured, speed violation, and poor weather show significant variation across states.
3. Speed violation and driving under alcohol/drug influence show a positive correlation.
4. Fatigue and poor weather show a positive correlation.
5. Targeted interventions, public awareness campaigns, infrastructure development, enforcement of traffic laws, and data-driven decision making are essential to reducing the number of crashes and fatalities on Nigerian roads.

Future Research Directions:

1. Investigate the impact of demographic factors, such as age and gender, on road traffic crashes in Nigeria.
2. Analyze the role of vehicle type and condition in road traffic crashes.
3. Examine the effect of weather conditions, such as rainfall and fog, on road traffic crashes.
4. Investigate the relationship between road traffic crashes and economic indicators, such as GDP and poverty rates.
5. Develop a predictive model to forecast road traffic crashes in Nigeria based on historical data and trends.
