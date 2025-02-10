import pickle
from flask import Flask, request, jsonify, render_template, url_for
import numpy as np
import pandas as pf
from sklearn.preprocessing import StandardScaler

application = Flask(__name__, static_folder='static')
app = application

# Load models
ridge_model = pickle.load(open("training_model/ridge.pkl", 'rb'))
standard_scaler = pickle.load(open("training_model/scaler.pkl", 'rb'))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
    try:
        # Get form data
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        # Scale input data
        new_data_scaled = standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        result = ridge_model.predict(new_data_scaled)[0]

        return render_template('home.html', result=result)
    
    except Exception as e:
        return render_template('home.html', result="Error: " + str(e))
    
@app.route('/predict')
def show_predict_page():
    return render_template("home.html", result=None)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
