<img src="https://user-images.githubusercontent.com/83081310/143724214-f9c48d84-96bd-45b9-9d79-ed9c18584fe8.png">

## Stroke predictor:
According to World Health Organisation (WHO), stroke are the second leading cause of death and the third leading cause of disability globally. Stroke is the sudden death of some brain cells due to lack of oxygen when the blood flow to the brain is lost by blockage or rupture of an artery to the brain, it is also a leading cause of dementia and depression. Current guidelines for primary prevention of stroke advocate the use of risk prediction models to identify individuals at high risk of cardiovascular disease (CVD) including stroke.

With 1.2 billion clinical documents being produced in the United States every year, We built a stroke predictor using data analytic and machine learning so predicting stroke can be acquired conveniently and at a low cost.

## Technologies: 
* Python/Pandas/Sklearn/pickel
* PostgreSQL
* Flask
* HTML/CSS/Bootstrap
* Tableau
* Heroku 

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
* The data is higly unbalanced,meaning the number of people have heart stroke is actually negligible as compared to the ones not having it. Therefore, while modeling and training data, either over sampling or under sampling has to be done to obtain best results.
* After comparing randomForest Classifier,KNN models, we decided to use SMOTE and ENN.
