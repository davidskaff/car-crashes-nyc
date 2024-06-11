# Collision Course: NYC's Risky Roadways 🚗
By: Fikre Bedane, Jasleen Brar, Maria Jose Dupont and David Skaff

## Project Overview 🔍
The goal of this project was to predict when and where accidents were likely to occur in New York City to enhance public safety and improve city planning. This may help with informing traffic laws and policies, guiding the allocation of resources, and optimizing police presence. By identifying high-risk areas and times, the city can implement preventative measures, such as improved signage or increased patrols, to reduce accidents. Furthermore, these insights can inform urban planning decisions, such as where to install traffic calming measures or redesign intersections, contributing to a safer and more efficient city for all residents. We used a dataset containing information about past motor vehicle collisions in NYC. The dataset, sourced from Kaggle, included features such as the date and time of the crash, the borough in which it occurred, the zip code, latitude, longitude, number of persons injured or killed, contributing factors for the vehicles involved, and the types of vehicles.

## Data Pre-processing 📑
We started by importing necessary libraries and loading the dataset. The ‘BOROUGH’ column, which is categorical, was converted into numerical values using Label Encoding. We also created new features from the ‘CRASH DATETIME’ column: we extracted the hour, day of the week, month, and year. After these preprocessing steps, we defined our features (X) and target variable (y), and split the data into training and validation sets. We also standardized the features to have zero mean and unit variance.

## Model Training and Evaluation ⚙️
We initially trained a Decision Tree Classifier model on our training data. We made predictions on the validation set and evaluated the model’s performance using classification accuracy. The initial model achieved an accuracy of 0.31 on the validation set. To improve the model’s performance, we transitioned to a Sequential model from Keras. This model had two dense layers with 64 neurons each, and used the Adam optimizer with a learning rate of 0.001. We trained this model for 10 epochs with a batch size of 32. The accuracy of this model on the validation set was 0.38.

## Model Optimization 🔧
We performed several rounds of hyperparameter tuning to improve the model’s performance. In the first round of tuning, we increased the complexity of the model by increasing the number of neurons in each layer from 64 to 128. We also increased the number of epochs from 10 to 20, and increased the batch size from 32 to 64. Additionally, we adjusted the learning rate to 0.001. In the second round of tuning, we further increased the complexity of the model by increasing the number of neurons in each layer from 128 to 256. We also increased the number of epochs from 20 to 50, and increased the batch size from 64 to 128. We adjusted the learning rate to 0.0005, added dropout layers, and implemented early stopping to halt the training process when the model’s performance on the validation set stopped improving. After these steps, the model’s accuracy on the validation set increased to 0.4. We also calculated precision, recall, f1-score, and support for each class using the classification_report from sklearn.metrics.

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
Finally, we created a presentation to talk about our work.


![pic](https://images.unsplash.com/photo-1613042964418-89c800809319?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Y2FyJTIwY3Jhc2h8ZW58MHwwfDB8fHwy)

## Where to find our work
All our data analysis can be found in the folder named 'Data'. 
Our powerpoint presentation is labelled "Collision Course NYC's Risky Roadways.pdf".
Our Machine Learning analysis can be found in the folder named 'Machine Learning'.

A release is published on GitHub with a tag, making it easy for you to connect to the Tableau interface — a convenient step forward in accessing 
and utilizing powerful visualization tools.
