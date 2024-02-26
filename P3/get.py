import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Função para obter o ID do município pelo nome
def get_municipio_id(nome_municipio):
    url = f'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'
    response = requests.get(url)
    municipios = response.json()
    if municipios:
        for municipio in municipios:
            if municipio['nome'] == nome_municipio:
                print(municipio['id'])
                return municipio['id']
    else:
        return None

# Função para obter os bairros de um município pelo seu ID (Aqui consideramos um Distrito como um bairro)
def get_bairros_by_municipio_id(municipio_id):
    url = f'https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{municipio_id}/distritos'
    response = requests.get(url)
    bairros = [bairro['nome'] for bairro in response.json()]
    return bairros

@app.route('/bairros', methods=['GET'])
def get_bairros():
    municipio = request.args.get('municipio')

    if not municipio:
        return jsonify({'error': 'O parâmetro de query "municipio" é obrigatório.'}), 400

    municipio_id = get_municipio_id(municipio)

    if not municipio_id:
        return jsonify({'error': f'O município "{municipio}" não foi encontrado.'}), 404

    bairros = get_bairros_by_municipio_id(municipio_id)

    response = {
        'municipio': municipio,
        'bairros': bairros
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
