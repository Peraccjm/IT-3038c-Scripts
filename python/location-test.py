import geocoder
from geopy.geocoders import Nominatim

g =geocoder.ip('me')
data1 = g.latlng
print("The current latitude and longitude of this device is: ", data1)

geolocator = Nominatim(user_agent="me")

location = geolocator.reverse(data1)
print("The current location of this device is: " , location)
locationraw = location.raw
locationdata = locationraw['display_name'].split()
zipc = locationdata[12]
zipnew = zipc.rstrip(',')
print(zipnew)