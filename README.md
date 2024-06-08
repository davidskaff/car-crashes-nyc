# Collision Course: NYC's Risky Roadways 🚗
By: Fikre Bedane, Jasleen Brar, Maria Jose Dupont and David Skaff

## Project Overview 🔍
The goal of our project was to predict where (borough) and when (crash datetime) vehicle accidents will occur in New York City. We used a dataset containing information about past motor vehicle collisions in NYC. The dataset, sourced from Kaggle, included features such as the date and time of the crash, the borough in which it occurred, the zip code, latitude, longitude, number of persons injured or killed, contributing factors for the vehicles involved, and the types of vehicles.

## Data Pre-processing 📑
We started by importing necessary libraries and loading the dataset. The 'BOROUGH' column, which is categorical, was converted into numerical values using one-hot encoding. The 'CRASH DATETIME' column was converted from string to datetime, and then we extracted the hour and day of the week as new features. After these preprocessing steps, we defined our features (X) and target variable (y), and split the data into training and testing sets.

## Model Training and Evaluation ⚙️
We initialized a Decision Tree Classifier model and trained it on our training data. We made predictions on the test data and evaluated the model's performance using classification accuracy. We also performed feature importance analysis to understand which features were most influential in the model's predictions.

## Model Optimization 🔧
To improve the model's performance, we performed cross-validation and used RandomizedSearchCV for hyperparameter tuning. We compared the performance of the initial model and the optimized model, and documented the results in a CSV file.

## Tableau Visualizations 📉
We also worked on tableau visualizations for vehicle crashes in NYC. The visualizations include:
- Number of persons injured and killed by city
- Frequency of collision occurrences
- Number of records by city
- Deaths over time
- Injury incidents over time

## Python Data Analysis 📊
We also worked on a python regular data analysis which gave us insights into road accidents in New York City. The analysis focused on three key aspects:
- Number of Injuries per Year in NYC
- Number of Fatalities per Year in NYC
- Most Common Cause of Accidents in NYC


We found that 2013 had the highest number of accidents, the highest number of fatalities by vehicle accidents, and the most common cause of accidents over the years was 'Unspecified'. This analysis helps in understanding the trends and factors contributing to road accidents in the city over time.

## Presentation 💡
Finally, we created a presentation to talk about our work. Our project demonstrates a thorough application of machine learning, from data preprocessing and model training to optimization and prediction. The impressive accuracy score of 0.99 indicates that our model is highly effective at predicting the location and time of future vehicle accidents in NYC based on the provided features.


![pic](https://images.unsplash.com/photo-1613042964418-89c800809319?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Y2FyJTIwY3Jhc2h8ZW58MHwwfDB8fHwy)
