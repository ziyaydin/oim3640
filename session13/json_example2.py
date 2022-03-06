weather = {'coord': {'lon': -71.29, 'lat': 42.3}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'base': 'stations', 'main': {'temp': 284.87, 'pressure': 1024, 'humidity': 62, 'temp_min': 283.71, 'temp_max': 286.15}, 'visibility': 16093, 'wind': {'speed': 4.6, 'deg': 10, 'gust': 9.3}, 'rain': {'1h': 0.51}, 'clouds': {'all': 90}, 'dt': 1570731925, 'sys': {'type': 1, 'id': 5255, 'country': 'US', 'sunrise': 1570704703, 'sunset': 1570745544}, 'timezone': -14400, 'id': 4954738, 'name': 'Wellesley', 'cod': 200}


# what is current temperature?

import urllib.request
import json

APIKEY = '895c1b03bc0f9a1178c91126bb892dbf'
city = 'Wellesley'
country_code = 'us'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

# print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
print(response_data['main']['temp'])

# How do we get current temperature?

