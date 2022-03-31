import urllib.request
import json
import pprint


def get_current_temp(city, country):
    APIKEY = '895c1b03bc0f9a1178c91126bb892dbf'
    country_code = 'us'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    x = (response_data['main']['temp'])
    return x - 273.15

