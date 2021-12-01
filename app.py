import numpy as np
import os

from flask import Flask, render_template, redirect, request, jsonify
from flask_pymongo import PyMongo
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import pickle

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') 
# # or "sql:///db.sql"

# # Remove tracking modifications
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
    

    # output = round(prediction[0], 2)
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

    # results = engine.execute('SELECT * FROM stroke_data').fetchall()
   
    # j_results = jsonify({'result': [dict(row) for row in results]})


    return render_template('data.html') 

@app.route('/explore')
def explore():

    return render_template('DataExplore.html')


if __name__ == "__main__":
    app.run(debug=True)