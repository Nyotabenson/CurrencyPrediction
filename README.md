## CURRENCY PREDICTION

#### USD predictions

### 1. ABSTRACT
The uncertainty in currency fluctuations creates challenges for businesses, particularly in international trade, where accurate exchange rate forecasting is essential. 
This study develops a *predictive model* using historical currency data and engineered features to identify patterns influencing exchange rates. 
The results highlight the model's potential to support business decision-making, especially in import and export activities, offering a promising approach to improving strategies in a volatile economic environment.

### 2. INTRODUCTION
#### 2.1 Problem Statement
There is a strong demand for a predictive model that forecasts currency exchange rates with minimal data, reducing reliance on complex datasets. 
Accessing accurate economic, market, and geopolitical data is challenging, especially for resource-limited businesses. 
A simplified model would provide real-time predictions, improving decision-making while reducing costs and complexities.

### 3. Objectives
a) To develop a predictive model that can achieve high accuracy while requiring minimal input data.

b) To design a model capable of making reliable currency exchange rate predictions for the next 6-12 months.

c) To ensure that the model can adapt to various market conditions and account for long-term trends.

### 4. Scope
The model is built by training on data sourced from various reliable external providers. It focuses on 
identifying and incorporating features that are strongly correlated with currency price fluctuations. While 
challenges may arise, such as obtaining high-quality data and performing effective feature engineering, 
these will be addressed throughout the process. An important assumption in the project is that each 
feature included is initially assumed relevant, with irrelevant features being filtered out during the 
evaluation phase.
### 5. Methodology
#### 5.1 Time Series Overview
The dataset, sourced from the Central Bank of Kenya, includes key indicative exchange rates from October 2016 to January 2024, with approximately 1,803 entries. 
An Augmented Dickey-Fuller (ADF) test was performed to assess stationarity, revealing non-stationarity with a p-value above 0.05, indicating the null hypothesis could not be rejected.
https://www.centralbank.go.ke/rates/forex-exchange-rates/
#### 5.2 Regression and Feature Importance
Additional feature engineering introduced variables such as Day of Year, Election Year, and U.S. Election Year. 
Various regression models, including *Ridge, Lasso, Random Forest, and XGBRegressor,* were trained, improving accuracy to 28% but still below 50%. 
To enhance predictions, data from November 2024 to January 2025 and U.S. Interest Rate data from the Federal Reserve were added. 
The U.S. Interest Rate showed a positive correlation with USD exchange rates over time.

US Interest Rate-https://fred.stlouisfed.org/series/DGS1

![image](https://github.com/user-attachments/assets/5abbce6d-5d60-42ec-bc49-6eb1d713ed00)

Recursive Feature Elimination (RFE) was applied to identify key features affecting the target variable. Both LGBMRegressor and RandomForestRegressor selected similar features but ranked them differently. 
The final chosen features included *U.S-Interest Rate, Day of Year, Week of Year, Month, and Election Year.*

![image](https://github.com/user-attachments/assets/9b182d61-6e8f-445b-800a-a535311eceda)

#### 5.3 Model Training and Prediction Results
Training the models with unscaled data and all available features yielded the highest accuracy of 96%. 
Predictions on X_test were plotted alongside actual values, visually confirming the Random Forest model's strong performance in forecasting currency exchange rates, highlighting its reliability and effectiveness.

![image](https://github.com/user-attachments/assets/8ba54ae6-23c3-4fb7-9b92-bc394b80dd87)

### 6.0 Discussion
The selected features were all relevant for predicting currency exchange rates, with RandomForestRegressor and LightGBMRegressor achieving the highest accuracy. 
Other models, including XGBoost, GradientBoostRegressor, and AdaBoost, also performed well, exceeding 90% accuracy. Further optimization could enhance performance. 
Future work may include additional tuning, feature engineering, and sentiment analysis to improve accuracy by incorporating market sentiment and news trends into the model.
### 7.0 Discussion
This project successfully tackled currency exchange rate prediction, a crucial task for businesses in international markets. 
By developing a model requiring minimal input data, it simplified the forecasting process. 
Key features, including Interest Rates, time-related factors, and Election Year, significantly improved accuracy. 
The strong correlation between U.S. Interest Rates and USD Exchange Rates highlighted the importance of macroeconomic indicators. 
Future enhancements, such as sentiment analysis and additional economic factors, could further strengthen predictions. 
Overall, this project showcases the potential of machine learning in helping businesses navigate currency volatility and make informed strategic decisions.

### Regards
