"""
{"contract": "two_year", "tenure": 12, "monthlycharges": 10}
"""
import requests

url = 'http://localhost:9696/predict'

example = {'company': 'ooo', 'product': 'gl62m (i5-7300hq/8gb/1tb', 'typename': 'gaming', 'inches': 15.6, 'screenresolution': 'full hd 1920x1080', 'cpu': 'intel core i5 7300hq 2.5ghz', 'ram': '8gb', 'memory': '128gb ssd +  1tb hdd', 'gpu': 'nvidia geforce gtx 1050', 'opsys': 'windows 10', 'weight': '2.2kg', 'price_euros': 1089.0}

res = requests.post(url=url, json=example).json()
print(res)
