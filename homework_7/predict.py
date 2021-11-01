import pickle
import numpy as np
import pandas as pd

from common_function import clean_dataset

saved_model_name = 'laptop_model_1_0.pkl'
saved_dv_name = 'laptop_dv.pkl'

# load saving model
with open(saved_model_name, 'rb') as file_model:
    model = pickle.load(file_model)

# load saving DictVectorizer
with open(saved_dv_name, 'rb') as file_dv:
    dv = pickle.load(file_dv)

# customer for checking
example = {'company': 'hp', 'product': '15-bs017nv (i7-7500u/8gb/256gb/radeon', 'typename': 'notebook', 'inches': 15.6, 'screenresolution': 'full hd 1920x1080', 'cpu': 'intel core i7 7500u 2.7ghz', 'ram': '8gb', 'memory': '256gb ssd', 'gpu': 'amd radeon 530', 'opsys': 'windows 10', 'weight': '1.91kg', 'price_euros': 719.0}

df_check = pd.DataFrame([example])
print(df_check)
_df = clean_dataset(df_check, clean_price_outliers=False, th_hold=0)

# transform customer to array
X = dv.transform(_df.to_dict(orient='records'))

# make predict
y_pred = np.exp(model.predict(X))[0]
print('y_pred =', int(y_pred), '$')
