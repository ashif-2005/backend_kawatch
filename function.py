import phonenumbers
from test2 import number
from test3 import data
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode

def create_location_map():
    sanNumber = phonenumbers.parse(number)
    yourLocation = geocoder.description_for_number(sanNumber, "en")
    print(yourLocation)

    service_provider = phonenumbers.parse(number)
    print(carrier.name_for_number(service_provider, "en"))

    geocoder_instance = OpenCageGeocode("ea817b35bf9a486b91c5be4cba6358ad")

    query = str(yourLocation)
    results = geocoder_instance.geocode(query)


    lat = data['items'][0]['position']['lat']
    lng = data['items'][0]['position']['lng']
    mymap = folium.Map(location=[lat, lng], zoom_start=9)

    for i in range(len(data['items'])):
        lat = data['items'][i]['position']['lat']
        lng = data['items'][i]['position']['lng']
        print(lat,lng)
        folium.Marker([lat, lng], popup=yourLocation).add_to((mymap))

    mymap.save('myLocation.html')

create_location_map()