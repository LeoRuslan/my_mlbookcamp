from flask import Flask
from flask import request, jsonify
import pickle

# we use model2.bin. It is in docker image
saved_model_name = 'model2.bin'
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
