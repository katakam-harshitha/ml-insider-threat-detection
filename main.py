from flask import Flask, render_template, request
import joblib
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load models
scaler = joblib.load('scaler.pkl')
rf_model = joblib.load('random_forest.pkl')
dt_model = joblib.load('decision_tree.pkl')
xgb_model = joblib.load('xgboost.pkl')
cnn_model = load_model('cnn_model.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/threat_identification')
def threat_identification():
    return render_template('threat_identification.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            O = float(request.form['O'])
            C = float(request.form['C'])
            E = float(request.form['E'])
            A = float(request.form['A'])
            N = float(request.form['N'])

            input_data = np.array([[O, C, E, A, N]])
            input_scaled = scaler.transform(input_data)

            # Use Best Model
            result_rf = rf_model.predict(input_scaled)
            result_dt = dt_model.predict(input_scaled)
            result_xgb = xgb_model.predict(input_scaled)
            result_cnn = cnn_model.predict(input_scaled)[0][0]

            # Final prediction based on majority voting
            final_result = int((result_rf + result_dt + result_xgb + result_cnn) > 2)
            prediction = "Threat Detected" if final_result == 1 else "No Threat"
        except Exception as e:
            prediction = f"Error: {e}"

        return render_template('result.html', prediction=prediction)
    return render_template('predict.html')

if __name__ == '__main__':
    app.run()
