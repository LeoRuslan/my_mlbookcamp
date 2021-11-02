import pickle
import pandas as pd
import numpy as np
from flask import Flask
from flask import request, jsonify

from common_function import clean_dataset, is_in_company_list

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
    if not is_in_company_list(example['company']):
        result = {
            'message': 'Sorry, but now we can not predict price for this company'
        }
        return jsonify(result)

    df_check = pd.DataFrame([example])
    _df = clean_dataset(df_check, clean_price_outliers=False, th_hold=0)

    # transform example to array
    X = dv.transform(_df.to_dict(orient='records'))
    y_pred = np.exp(model.predict(X)[0])
    result = {
        'laptop_price': str(int(y_pred)) + '€'
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
