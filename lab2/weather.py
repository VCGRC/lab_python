import requests
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

s_city = 'moscow'
data = requests.get("http://api.openweathermap.org/data/2.5/forecast",params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': os.environ.get('WEATHER_API')}).json()

print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",'{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",i['weather'][0]['description'], ">")
    print("____________________________")