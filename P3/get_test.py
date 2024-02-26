import requests

url = "http://localhost:5000/bairros"

params = {
    'municipio': 'São Paulo'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    # A solicitação foi bem-sucedida, imprima os dados
    data = response.json()
    print("Município:", data['municipio'])
    print("Bairros:", data['bairros'])
elif response.status_code == 400:
    # Parâmetro de query ausente ou inválido
    print("Erro:", response.json()['error'])
elif response.status_code == 404:
    # Município não encontrado
    print("Erro:", response.json()['error'])
else:
    # Outro erro
    print("Erro:", response.text)
