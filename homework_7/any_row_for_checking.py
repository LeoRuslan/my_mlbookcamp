import pandas as pd
import random

df = pd.read_csv('laptop_price.csv', encoding="ISO-8859-1")

df.columns = df.columns.str.lower().str.replace(' ', '_')
categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)
for c in categorical_columns:
    df[c] = df[c].str.lower()

df = df.drop('laptop_id', axis=1)

print(df.iloc[random.randint(0, len(df)), :].to_dict())
