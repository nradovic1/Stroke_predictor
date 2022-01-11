<img src="https://user-images.githubusercontent.com/83081310/143724214-f9c48d84-96bd-45b9-9d79-ed9c18584fe8.png">

## Stroke predictor:
According to World Health Organisation (WHO), stroke are the second leading cause of death and the third leading cause of disability globally. Stroke is the sudden death of some brain cells due to lack of oxygen when the blood flow to the brain is lost by blockage or rupture of an artery to the brain, it is also a leading cause of dementia and depression. Current guidelines for primary prevention of stroke advocate the use of risk prediction models to identify individuals at high risk of cardiovascular disease (CVD) including stroke.

With 1.2 billion clinical documents being produced in the United States every year, We built a stroke predictor using data analytic and machine learning so predicting stroke can be acquired conveniently and at a low cost.

## Technologies: 
![image](https://img.shields.io/badge/technologies-Python-orange)/Pandas//pickle
![image](https://img.shields.io/badge/technologies-Pandas-orange)
![image](https://img.shields.io/badge/technologies-Sklearn-orange)
![image](https://img.shields.io/badge/technologies-PostgreSQL-orange)
![image](https://img.shields.io/badge/technologies-SQLAlchemy-orange)
![image](https://img.shields.io/badge/technologies-Flask-orange)
![image](https://img.shields.io/badge/technologies-HTML/CSS/Bootstrap-orange)
![image](https://img.shields.io/badge/technologies-Tableau-orange)
![image](https://img.shields.io/badge/technologies-Matplotlib-orange)
![image](https://img.shields.io/badge/technologies-Seaborn-orange)
![image](https://img.shields.io/badge/technologies-Heroku-orange)
![image](https://img.shields.io/badge/technologies-Sklearn-orange)


## Stages: 
1. Identify features and target values
2. Encoding and features scaling
3. Compile, train and evaluate the model
4. Compare models
5. Import model by Flask
6. Create interactive web app using Javascript, HTML and CSS
7. Deployment on Heroku

## Data Source
Dataset is obtained at https://data.mendeley.com/datasets/x8ygrw87jw/1. It includes more than 40,000 rows and 12 of columns, which include 11 of features, such as bmi, heart disease, etc, and 1 target value column. 

## Data cleaning and data preparation
### To remove following items:
* Null
* columns of non-features, e.g. ID
* Features scaling

## Model selection
* The data is higly unbalanced,meaning the number of people have heart stroke is actually negligible as compared to the ones not having it. Therefore, while modeling and training data, either over sampling or under sampling has to be done to obtain best results. SMOTEENN is another option were the majority is undersampled and the minority is oversampled.
* After comparing many different classification models such as RandomForestClassifier,KNClassification, LogisticRegression, SVC and many more, we decided to use SMOTEENN and KNClassification classifier with parameters of (n_neighbors=3, weights='distance'). Not only was this the most accurate model with over 92% accuracy, it has a significantly higher recall then any other model. This is very important since this is regarding important health matters, having a false negative can be very dangerous.


## Connecting to PostgreSQL
* With SQLAlchemy, we exported the data to a server in Pgadmin4/PostgreSQL that was later connected to the Heroku server fpr the app

## Deployment of model
* Flask app is created as a backbone of the model and data.
* A webpage is made using HTML/CSS/Bootstrap to display the app
* Heroku app is created that connects to Github repository for all of the code.

## Please visit our deployment at https://strokepredictorgatech.herokuapp.com
