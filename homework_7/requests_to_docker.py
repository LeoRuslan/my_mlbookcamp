"""
{"contract": "two_year", "tenure": 12, "monthlycharges": 10}
"""
import requests

url = 'http://localhost:9696/predict'

example = {
    'company': 'hp', 'product': '15-bs017nv (i7-7500u/8gb/256gb/radeon', 'typename': 'notebook', 'inches': 15.6, 'screenresolution': 'full hd 1920x1080', 'cpu': 'intel core i7 7500u 2.7ghz', 'ram': '8gb', 'memory': '256gb ssd', 'gpu': 'amd radeon 530', 'opsys': 'windows 10', 'weight': '1.91kg', 'price_euros': 719.0
}

res = requests.post(url=url, json=example).json()
print(res)
