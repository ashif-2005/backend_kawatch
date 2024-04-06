from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode
import requests

account_sid = 'AC4eb4231aadad14ce99b09e3a21803677'
auth_token = '54b5099ae786e3c61fb8d7fd94bb9408'
number="+919629158412"
API_KEY = 'k6AF02uec6xQEzvhF-XB_wdqffYPoVNOjApiS2NK6jY'
latitude = 8.392831
longitude = 93.650594


def send_message():

    client = Client(account_sid, auth_token)

    response = VoiceResponse()
    response.say('I am in danger please help me')

    call = client.calls.create(
        from_='+13159225759',
        to='+919360412081',
        twiml=str(response)
    )
    

    # from_number = ''  
    # to_number = '' 

    # call_sid = initiate_call(from_number, to_number)

    # if call_sid:
    #     print(f"Call initiated. Call SID: {call_sid}")
    # else:
    #     print("Unable to initiate the call. Please check your Twilio credentials or inputs.")

    # print(call.sid)

    client= Client(account_sid, auth_token)

    client.messages.create(
        body="Hi karthi.....",
        from_="+13159225759",
        to="+919629498023"
    )

    # print("SMS sent successfully")

# accessing the map
    url = f"https://discover.search.hereapi.com/v1/discover?apiKey={API_KEY}&at={latitude},{longitude}&q=police"


    response = requests.get(url)


    data = response.json()

    if 'items' in data:
        num_police_stations = len(data['items'])

        # print("Number of Police Stations:", num_police_stations)
        # for i in range(len(data['items'])):
        #     return data['items'][i]['position'])
    # else:
    #     print("No police stations found nearby.")

    sanNumber = phonenumbers.parse(number)
    yourLocation = geocoder.description_for_number(sanNumber, "en")
    # print(yourLocation)

    service_provider = phonenumbers.parse(number)
    # print(carrier.name_for_number(service_provider, "en"))

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
    # return call.sid
    return "call sent , message sent , got location "
