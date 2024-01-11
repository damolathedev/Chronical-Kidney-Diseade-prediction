from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd
from utils.dummies import dummies
import os

import pandas as pd

app = Flask(__name__)

model = joblib.load('/home/damola/Desktop/ckd/app/utils/clf_model.joblib')

@app.route('/')
def home():
    return render_template('input_page.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = request.form['age']
        blood_pressure = request.form['blood_pressure']
        specific_gravity = request.form['specific_gravity']
        albumin = request.form['albumin']
        sugar = request.form['sugar']
        red_blood_cells = request.form['red_blood_cells']
        pus_cell = request.form['pus_cell']
        pus_cell_clumps = request.form['pus_cell_clumps']
        bacteria = request.form['bacteria']
        blood_glucose_random = request.form['blood_glucose_random']
        blood_urea = request.form['blood_urea']
        serum_creatinine = request.form['serum_creatinine']
        sodium = request.form['sodium']
        potassium = request.form['potassium']
        hemoglobin = request.form['hemoglobin']
        packed_cell_volume = request.form['packed_cell_volume']
        white_blood_cell_count = request.form['white_blood_cell_count']
        red_blood_cell_count = request.form['red_blood_cell_count']
        hypertension = request.form['hypertension']
        diabetes_mellitus = request.form['diabetes_mellitus']
        coronary_artery_disease = request.form['coronary_artery_disease']
        appetite = request.form['appetite']
        pedal_edema = request.form['pedal_edema']
        anemia = request.form['ane']

        # Create a DataFrame with the input data
        data = {
            'rbc': [red_blood_cells],
            'pc': [pus_cell],
            'pcc': [pus_cell_clumps],
            'ba': [bacteria],
            'htn': [hypertension],
            'dm': [diabetes_mellitus],
            'cad': [coronary_artery_disease],
            'appet': [appetite],
            'pe': [pedal_edema],
            'ane': [anemia],
            'age': [float(age)],
            'bp': [float(blood_pressure)],
            'al': [int(albumin)],
            'su': [int(sugar)],
            'bgr': [float(blood_glucose_random)],
            'bu': [float(blood_urea)],
            'sc': [float(serum_creatinine)],
            'sod': [float(sodium)],
            'pot': [float(potassium)],
            'hemo': [float(hemoglobin)],
            'pcv': [float(packed_cell_volume)],
            'wc': [float(white_blood_cell_count)],
            'rc': [float(red_blood_cell_count)],
            'sg': [float(specific_gravity)]
        }

        script_dir = os.path.dirname(os.path.realpath(__file__))
        csv_path = os.path.join(script_dir, 'utils', 'dataset.csv')
        dataset = pd.read_csv(csv_path)
        dataset = dataset.drop("classification", axis=1)
        print(dataset.columns)
        df = pd.DataFrame(data)
        
        print(dummies(dataset, df))
        
        input_features = dummies(dataset, df)
        
        # Make prediction using the loaded model
        prediction = model.predict(input_features.reshape(1, -1))

        # Prepare the response
        # Assuming prediction is numeric    
        prediction_result = "CKD" if int(prediction[0]) == 1 else "Not CKD"

        return render_template('input_page.html', prediction_result=prediction_result)

    except Exception as e:
        return render_template('input_page.html', error=str(e))

if __name__ == '__main__':
    # Run the Flask app on localhost and port 5000
    app.run(debug=True)

