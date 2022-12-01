import json
import requests
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")


print('Please enter your zip code:')
zip = 45248
r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=4e54ca6c84e78554467ec14acfadecce' % zip)
data =r.json()
print(data)
print(data['weather'][0]['description'])
ktemp = data['main']['temp']
ftemp = (ktemp - 273.15) * (9/5) + 32
print(ftemp)
print(data['main']['humidity'])