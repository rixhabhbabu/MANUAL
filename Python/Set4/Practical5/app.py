from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f'The weather in {city} is {weather_description} with a temperature of {temperature}°C.'
    else:
        return f'Failed to fetch weather information. Error: {data.get("message", "Unknown error")}'

@app.route('/')
def home():
    return render_template('index_api.html')

@app.route('/weather', methods=['POST'])
def weather():
    api_key = 'your-openweathermap-api-key'  # Replace with your API key
    city = request.form.get('city')  # Use .get() to avoid KeyError if 'city' is missing
    if not city:
        return "City not provided. Please enter a city name."
    
    result = get_weather(api_key, city)
    return render_template('index_api.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)