from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

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
    print(f"Call initiated. Call SID: {call_sid}")
else:
    print("Unable to initiate the call. Please check your Twilio credentials or inputs.")
