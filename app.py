from flask import Flask, render_template, request
import requests
app = Flask(__name__)

API_KEY = '094d903b3c58e22de114cf2fa4d949f0'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    error = None
    if request.method == 'POST':
        city = request.form['city']
        p = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric',
            'lang': 'ru'
        }
        response = requests.get(BASE_URL, params=p)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temp': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'icon': data['weather'][0]['icon']
            }

        else:
            error = f'Город {city} не найден'

    return render_template('index.html', weather=weather_data, error=error)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

app.run(debug=True)