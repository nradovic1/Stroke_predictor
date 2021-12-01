import numpy as np
import os

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

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
    print(final_features)
    prediction = model.predict(final_features)

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

    results = db.session.query().all

    return render_template('data.html',
                                data_text = results)


if __name__ == "__main__":
    app.run(debug=True)