from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import phonenumbers
from test2 import number
from test3 import data
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode
from flask import Flask,request,jsonify

app=Flask(__name__)
@app.route('/api',methods=['GET'])
def send_mesages():

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
            return (lat,lng)
            folium.Marker([lat, lng], popup=yourLocation).add_to((mymap))

        mymap.save('myLocation.html')

    def call():
        # Twilio Account SID and Auth Token
        account_sid = 'AC4eb4231aadad14ce99b09e3a21803677'
        auth_token = '54b5099ae786e3c61fb8d7fd94bb9408'

        def initiate_call(from_number, to_number):
            client = Client(account_sid, auth_token)

            response = VoiceResponse()
            response.say('I am in danger please help me')

            call = client.calls.create(
                from_=from_number,
                to=to_number,
                twiml=str(response)
            )

            return call.sid

        # Example usage
        from_number = '+13159225759'  # Your Twilio phone number
        to_number = '+919629158412'  # Phone number to call

        call_sid = initiate_call(from_number, to_number)

        if call_sid:
            return "Call initiated"
        else:
            print("Unable to initiate the call. Please check your Twilio credentials or inputs.")

    def message():
        # Twilio credentials
        account_sid = "AC4eb4231aadad14ce99b09e3a21803677"
        auth_token = "54b5099ae786e3c61fb8d7fd94bb9408"

        try:
            # Initialize the Twilio client
            client = Client(account_sid, auth_token)

            # Send the SMS
            client.messages.create(
                body="Hi karthi.... once again",
                from_="+13159225759",
                to="+919629158412"
            )

            return "SMS sent successfully"
        except Exception as e:
            return str(e)


if __name__=='__main__':
    app.run()
