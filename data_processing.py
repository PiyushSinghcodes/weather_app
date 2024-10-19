import sqlite3
import pandas as pd
import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import config

def create_table():
    conn = sqlite3.connect(config.Config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_data (
            city TEXT,
            main TEXT,
            temp REAL,
            feels_like REAL,
            dt INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def retrieve_and_process():
    conn = sqlite3.connect(config.Config.DB_PATH)
    cursor = conn.cursor()

    for city in config.Config.CITIES:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.Config.API_KEY}"
        response = requests.get(url).json()
        
        print(f"Response for {city}: {response}")

        main = response['weather'][0]['main']
        temp = response['main']['temp'] - 273.15  # Convert Kelvin to Celsius
        feels_like = response['main']['feels_like'] - 273.15
        dt = response['dt']

        cursor.execute('''
            INSERT INTO weather_data (city, main, temp, feels_like, dt)
            VALUES (?, ?, ?, ?, ?)
        ''', (city, main, temp, feels_like, dt))
        
        # Print data insertion for debugging
        print(f"Inserted data for {city}: {main}, {temp}, {feels_like}, {dt}")

    conn.commit()
    conn.close()

def daily_summary():
    conn = sqlite3.connect(config.Config.DB_PATH)
    query = '''
        SELECT city, DATE(dt, 'unixepoch') as date, temp, main
        FROM weather_data
    '''
    df = pd.read_sql_query(query, conn)
    conn.close()
    

    grouped = df.groupby(['city', 'date'])

    summary_list = []
    
    for (city, date), group in grouped:
        avg_temp = group['temp'].mean()
        max_temp = group['temp'].max()
        min_temp = group['temp'].min()
        dominant_condition = group['main'].mode()[0]  # Get the most frequent condition
        
        summary_list.append({
            'city': city,
            'date': date,
            'avg_temp': avg_temp,
            'max_temp': max_temp,
            'min_temp': min_temp,
            'dominant_condition': dominant_condition
        })

    return summary_list

def check_alerts():
    conn = sqlite3.connect(config.Config.DB_PATH)
    query = f'''
        SELECT * FROM weather_data
        WHERE temp > {config.Config.ALERT_THRESHOLD}
        ORDER BY dt DESC
        LIMIT 2
    '''
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    alerts = df.to_dict(orient='records')
    return alerts

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            return None

    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None


create_table() 
