"""
Now let's serve this model as a web service
Install Flask and Gunicorn (or waitress, if you're on Windows)
Write Flask code for serving the model
Now score this customer using requests:
    {"contract": "two_year", "tenure": 1, "monthlycharges": 10}

What's the probability that this customer is churning?
We use model1.bin.
"""
import requests

url = 'http://localhost:9696/predict'

customer = {
    "contract": "two_year", "tenure": 1, "monthlycharges": 10
}

res = requests.post(url=url, json=customer).json()
print(res)
