import requests

# url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
# data = {'url': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Pug_600.jpg'}

url = 'https://b1xk4hfq34.execute-api.us-east-2.amazonaws.com/dog_cat_test/predict'
data = {'url': 'https://upload.wikimedia.org/wikipedia/commons/1/18/Vombatus_ursinus_-Maria_Island_National_Park.jpg'}

result = requests.post(url, json=data).json()
print(result)
