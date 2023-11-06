import requests
request=requests.get("http://127.0.0.1:5000/predict")
print(request.json())