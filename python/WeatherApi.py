import json
import requests

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=12345,us&appid=4e54ca6c84e78554467ec14acfadecce')

data = r.json()
print(data['weather'][0];'description')