from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/age', methods=['POST'])
def calculate_age():
    data = request.get_json()

    #Verificação do corpo da requisição
    if not all(key in data for key in ('name', 'birthdate', 'date')):
        return jsonify({'error': 'Garanta que o corpo da requisição esteja completo.'}), 400

    birthdate = datetime.strptime(data['birthdate'], '%Y-%m-%d')
    date = datetime.strptime(data['date'], '%Y-%m-%d')

    #Verificação se a data é no futuro
    if date <= datetime.now():
        return jsonify({'error': 'A data fornecida deve ser no futuro.'}), 400

    age_now = calculate_age_at_date(birthdate, datetime.now())
    age_then = calculate_age_at_date(birthdate, date)

    response = {
        'quote': f"Olá, {data['name']}! Você tem {age_now} anos e em {date.strftime('%d/%m/%Y')} você terá {age_then} anos.",
        'ageNow': age_now,
        'ageThen': age_then
    }

    return jsonify(response)

def calculate_age_at_date(birthdate, date):
    age = date.year - birthdate.year - ((date.month, date.day) < (birthdate.month, birthdate.day))
    return age

if __name__ == '__main__':
    app.run(debug=True)
