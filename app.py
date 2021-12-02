import numpy as np
import os

from flask import Flask, render_template, redirect, request, jsonify
from flask_pymongo import PyMongo
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

import pickle

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') 


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)




model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    print(final_features)
    print(prediction)
    

    if prediction==0:
        return render_template('index.html',
                               prediction_text='Low chances of patient having stroke'.format(prediction),
                               )
    else:
        return render_template('index.html',
                               prediction_text='High chances of patient having stroke'.format(prediction),
                              )
@app.route('/data')
def data():
    # Below is the code for connecting to postgresql locally. 
    # connection_string = "postgres:postgres@localhost:5432/stroke_db"
    # engine = create_engine(f'postgresql://{connection_string}')

    results = db.session.query('(gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status, stroke) FROM stroke_data').all()
    
    return render_template('data.html', j_results = results)

@app.route('/explore')
def explore():

    return render_template('DataExplore.html')


if __name__ == "__main__":
    app.run(debug=True)