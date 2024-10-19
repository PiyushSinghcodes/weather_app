from flask import Flask, render_template, request
from data_processing import retrieve_and_process, daily_summary, check_alerts,get_weather
import datetime


app = Flask(__name__)

@app.template_filter('time_formatter')
def time_formatter(value):
    return datetime.datetime.fromtimestamp(value).strftime('%Y-%m-%d %H:%M:%S')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summary')
def summary():
    data = daily_summary()
    return render_template('summary.html', summary=data)

@app.route('/alerts')
def alerts():
    data = check_alerts()
    return render_template('alerts.html', alerts=data)

@app.route('/weather_data', methods=['GET', 'POST'])
def weather_data():
    if request.method == 'POST':
        city = request.form['city']
        api_key = '4633c79a0a8dca369aa4e4719bb0081a'
        weather_data = get_weather(api_key, city)
        return render_template('weather_data.html', weather_data=weather_data)

    return render_template('weather_data.html', weather_data=None)

if __name__ == '__main__':
    app.run(debug=True)
