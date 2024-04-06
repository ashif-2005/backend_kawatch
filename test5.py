from twilio.rest import Client

# Twilio credentials
account_sid = "AC4eb4231aadad14ce99b09e3a21803677"
auth_token = "54b5099ae786e3c61fb8d7fd94bb9408"




try:
    # Initialize the Twilio client
    client = Client(account_sid, auth_token)

    # Send the SMS
    client.messages.create(
        body="hi i am mohammed ashif......",
        from_="+13159225759",
        to="+919629498023"
    )

    print("SMS sent successfully")
except Exception as e:
    print(str(e))