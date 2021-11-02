import requests

url = 'http://localhost:9696/predict'

example = {'company': 'lenovo', 'product': 'ideapad 320-15ikbn', 'typename': 'notebook', 'inches': 15.6, 'screenresolution': 'full hd 1920x1080', 'cpu': 'intel core i5 7200u 2.5ghz', 'ram': '4gb', 'memory': '128gb ssd', 'gpu': 'intel hd graphics 620', 'opsys': 'no os', 'weight': '2.2kg', 'price_euros': 468.0}

res = requests.post(url=url, json=example).json()
print(res)
