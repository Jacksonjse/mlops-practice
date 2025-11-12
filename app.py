from flask import Flask, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open('rf_model_test.pkl', 'rb') as f:
    model = pickle.load(f)

accuracy = 0.7597402597402597

@app.route('/predict', methods = ['GET'])
def predict():

    features = [6, 90, 54, 24, 0, 14.77, 0.34, 30]

    input_features = np.array(features).reshape(1, -1)
    prediction = model.predict(input_features)[0]

    if prediction == 1:
        return jsonify({'prediction': 'Diabetic'})
        
    else:
        return jsonify({'prediction': 'Non-Diabetic'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)