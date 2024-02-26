import requests

birthdate = "2001-11-05"
future_date = "2026-11-05"

data = {
    "name": "Nome Sobrenome",
    "birthdate": birthdate,
    "date": future_date
}

url = "http://localhost:5000/age"
response = requests.post(url, json=data)

print(response.json())

