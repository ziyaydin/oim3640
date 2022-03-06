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
