"""
Let's use saved models!
1) Write a script for loading these models with pickle
2) Score this customer:
    {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}

What's the probability that this customer is churning?
"""

import pickle

saved_model_name = 'model1.bin'
saved_dv_name = 'dv.bin'

# load saving model
with open(saved_model_name, 'rb') as file_model:
    model = pickle.load(file_model)

# load saving DictVectorizer
with open(saved_dv_name, 'rb') as file_dv:
    dv = pickle.load(file_dv)

# customer for checking
example = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}

# transform customer to array
X = dv.transform(example)

# make predict
y_pred = model.predict_proba(X)[0, 1]
print('y_pred =', y_pred.round(3))
