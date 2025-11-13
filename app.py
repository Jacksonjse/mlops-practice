from flask import Flask, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open('rf_model_test.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=[GET])
def predict():

    features = [6, 90, 234, 115, 66.7, 45, 54, 98]
    input_features = np.array(features).reshape(1, -1)

    prediction = model.predict(input_features)[0]
    
    if prediction == 1:
        return jsonify({'prediction': 'Diabetic'})
    else:
        return jsonift({'prediction': 'Non-Diabetic'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)