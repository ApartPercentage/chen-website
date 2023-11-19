import requests
import json

url = "https://chen-website.leeyuchen0825.repl.co/project/1/api/predict"

data = {"content": "This is an email spam classifier"}

response = requests.post(url, json=data)

if response.status_code == 200:
  results = response.json()
  print("Content:", results['email'])
  print("Prediction:", results['prediction'])
else:
  print("Error:", response.status_code)
  print(response.text)
