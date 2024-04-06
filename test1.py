import phonenumbers
from test2 import number
from test3 import data
from phonenumbers import geocoder
import folium


sanNumber=phonenumbers.parse(number)

yourlocation=geocoder.description_for_number(sanNumber,"en")

print(yourlocation)

from phonenumbers import carrier
service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode("ea817b35bf9a486b91c5be4cba6358ad")

query=str(yourlocation)

results=geocoder.geocode(query)

print(results)
lat=data['items'][0]['position']['lat']
lng=data['items'][0]['position']['lng']
mymap= folium.Map(location=[lat,lng],zoom_start=9)


for i in range(len(data['items'])):
    lat=data['items'][i]['position']['lat']
    lng=data['items'][i]['position']['lng']
    folium.Marker([lat, lng],popup=yourlocation).add_to((mymap))

mymap.save('myLocation.html')


