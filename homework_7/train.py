import pandas as pd
import pickle

from common_function import clean_dataset

from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor


# read data
df = pd.read_csv('laptop_price.csv', encoding="ISO-8859-1")

df.columns = df.columns.str.lower().str.replace(' ', '_')
categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)
for c in categorical_columns:
    df[c] = df[c].str.lower()

df = df.drop('laptop_id', axis=1)

df = clean_dataset(df)

# Split our data to train and test.
df_train, df_test = train_test_split(df, test_size=0.2, random_state=7)

# training target
y_train = df_train['log_price']
# testing target
y_test = df_test['log_price']

df_train = df_train.drop(['price_euros', 'log_price'], axis=1)
df_test = df_test.drop(['price_euros', 'log_price'], axis=1)

dv = DictVectorizer(sparse=False)

# preparation training dataset
train_dict = df_train.to_dict(orient='records')
X_train = dv.fit_transform(train_dict)

# preparation training dataset
test_dict = df_test.to_dict(orient='records')
X_test = dv.transform(test_dict)

# init model with best parameters
model = XGBRegressor(n_estimators=250, max_depth=5, objective='reg:squarederror',
                     learning_rate=0.1, subsample=0.6, colsample_bytree=0.5, eta=0.3)

# fit model
model.fit(X_train, y_train)

y_hat = model.predict(X_test)
print(mean_absolute_error(y_test.values.ravel(), y_hat).round(3))

# save model and dv to files.
pickle.dump(model, open('laptop_model_1_0.pkl', 'wb'))
pickle.dump(dv, open('laptop_dv.pkl', 'wb'))
