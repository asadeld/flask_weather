from flask import Flask, render_template, request
import requests
app = Flask(__name__)

API_KEY = '094d903b3c58e22de114cf2fa4d949f0'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    error = None
    city_dict = {}
    city = ['Москва', 'Пекин', "Стамбул", "Вашингтон", "Берлин", 'Париж']

    for c in city:
        p = {
            'q': c,
            'appid': API_KEY,
            'units': 'metric',
            'lang': 'ru'
        }
        response_requests = requests.get(BASE_URL, params=p)
        data_ = response_requests.json()
        city_dict[c] = {
            'city': data_['name'],
            'temp': data_['main']['temp'],
            'feels_like': data_['main']['feels_like'],
            'description': data_['weather'][0]['description'],
            'humidity': data_['main']['humidity'],
            'icon': data_['weather'][0]['icon']
        }

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

    return render_template('index.html', weather=weather_data, error=error, city_dict=city_dict)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

app.run(debug=True)

'''
rgb
000
fff
f00

0
1
2
3
4
5
6
7
8
9
a
b
c
d
e
f

r  g  b
58 a1 f0

fff
rgb(255, 255, 255)
rgb(0, 0, 0)
rgb(255, 0, 0)


users = {'login': 'user1', 'password': '12345'}
print(users.items()) # [('login', 'user1'), ('password', '12345)]

for key in {'login': 'user1', 'password': '12345'}:
    print(key)

'''