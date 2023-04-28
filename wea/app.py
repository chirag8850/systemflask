from flask import Flask, render_template, request

import requests

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])

def index():

    weather_data = {}

    if request.method == 'POST':

        city = request.form['city']

        api_key = '62fdb9eea451a3795e04fd4ea61bb81e'

        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        response = requests.get(url, timeout=10)

        data = response.json()

        if data.get('cod') != '404':

            weather_data = {

                'city': data['name'],

                'temperature': data['main']['temp'],

                'description': data['weather'][0]['description'],

                'icon': data['weather'][0]['icon']

            } 

        else:

            weather_data = {'error': 'City not found'}

    return render_template('index.html', weather_data=weather_data)



if __name__ == '__main__':

    app.run(debug=True)

