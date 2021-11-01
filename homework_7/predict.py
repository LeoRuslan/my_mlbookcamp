import pickle
import pandas as pd
from flask import Flask
from flask import request, jsonify

from common_function import clean_dataset

saved_model_name = 'laptop_model_1_0.pkl'
saved_dv_name = 'laptop_dv.pkl'

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
    df_check = pd.DataFrame([example])
    _df = clean_dataset(df_check, clean_price_outliers=False, th_hold=0)

    # transform customer to array
    X = dv.transform(_df.to_dict(orient='records'))
    y_pred = model.predict(X)[0]
    result = {
        'laptop_price': int(y_pred)
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
