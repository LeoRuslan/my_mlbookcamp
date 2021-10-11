"""
{"contract": "two_year", "tenure": 12, "monthlycharges": 10}
"""
import requests

url = 'http://localhost:9696/predict'

customer = {
    "contract": "two_year", "tenure": 1, "monthlycharges": 10
}

res = requests.post(url=url, json=customer).json()
print(res)
