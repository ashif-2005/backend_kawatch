from twilio.rest import Client

# Twilio account SID and authentication token
account_sid = 'AC4eb4231aadad14ce99b09e3a21803677'
auth_token = '54b5099ae786e3c61fb8d7fd94bb9408'

# Twilio phone number and recipient's phone number
from_number = '+13159225759'
to_number = '+919360412081'

# Message content
message = 'hi... lingu kutty.....'

# Create the Twilio client
client = Client(account_sid, auth_token)

# Send the WhatsApp message
message = client.messages.create(
    body=message,
    from_=f'whatsapp:{from_number}',
    to=f'whatsapp:{to_number}'
)

# Print the message SID
print(f'Message SID: {message.sid}')
