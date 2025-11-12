import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

data = pd.read_csv("diabetes.csv")
X = data[['Pregnancies', 'Glucose',	'BloodPressure', 'SkinThickness', 'Insulin','BMI',	'DiabetesPedigreeFunction',	'Age']]
y = data['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=47)
rf = RandomForestClassifier(random_state=47)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f'ACCURACY: {accuracy}')
with open('rf_model_test.pkl', 'wb') as f:
    pickle.dump( rf, f)