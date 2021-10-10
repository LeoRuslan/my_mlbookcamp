"""
Let's use saved models!
1) Write a script for loading these models with pickle
2) Score this customer:
    {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}

What's the probability that this customer is churning?
"""
from flask import Flask
from flask import request, jsonify
import pickle

saved_model_name = 'model1.bin'
saved_dv_name = 'dv.bin'

# load saving model
with open(saved_model_name, 'rb') as file_model:
    model = pickle.load(file_model)

# load saving DictVectorizer
with open(saved_dv_name, 'rb') as file_dv:
    dv = pickle.load(file_dv)

app = Flask('churn')


@app.route('/predict', methods=['POST'])
def predict():
    example = request.get_json()
    X = dv.transform(example)
    y_pred = model.predict_proba(X)[0, 1]
    result = {
        'probability': y_pred.round(3)
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
