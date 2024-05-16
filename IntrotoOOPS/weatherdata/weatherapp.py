from flask import Flask, render_template, request
import plotly.graph_objs as go
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return round(celsius, 2)

def get_weather(city):
    country = 'ind'
    api_key = 'ed3d2466c45243bcb5d1996e4c8a1248'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&APPID={api_key}'
    
    response = requests.get(url)
    data = response.json()
    
    timezone = data['timezone']
    week_name, time = get_time(timezone)

    weather = {
        'city': city,
        'description': data['weather'][0]['main'],
        'temperature': kelvin_to_celsius(data['main']['temp']),
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'name': data['name'],
        'timezone': timezone,
        'week_name': week_name,
        'time': time
    }

    return weather

def get_time(timezone):
    current_time = datetime.utcnow() + timedelta(seconds=timezone)
    week_name = current_time.strftime("%A")
    time = current_time.strftime("%I:%M %p")
    return week_name, time

def generate_temperature_graph(temperature_data):
    dates = temperature_data['dates']
    temperatures = temperature_data['temperatures']

    # Create trace for temperature data
    trace = go.Scatter(x=dates, y=temperatures, fill='tozeroy', mode='none', name='Temperature (°C)')

    # Create layout
    layout = go.Layout(
        title='Temperature Trend',
        xaxis=dict(title='Date'),
        yaxis=dict(title='Temperature (°C)'),
        margin=dict(l=20, r=20, t=20, b=20)  # Adjust margins for smaller graph
    )

    # Create figure with trace and layout
    fig = go.Figure(data=[trace], layout=layout)

    # Convert figure to HTML
    temperature_graph = fig.to_html(full_html=False)

    return temperature_graph

def get_daily_temperature(city, date):
    country = 'ind'
    api_key = 'ed3d2466c45243bcb5d1996e4c8a1248'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&APPID={api_key}'
    
    response = requests.get(url)
    data = response.json()
    
    temperature = kelvin_to_celsius(data['main']['temp'])

    return temperature

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)


        temperature_data = {
            'dates': [],
            'temperatures': []
        }

  
        for i in range(7):
            date = (datetime.utcnow() - timedelta(days=i)).strftime('%Y-%m-%d')
            temperature_data['dates'].append(date)
            temperature_data['temperatures'].append(get_daily_temperature(city, date))

        temperature_graph = generate_temperature_graph(temperature_data)

        return render_template('index.html', weather_data=weather_data, temperature_graph=temperature_graph)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
