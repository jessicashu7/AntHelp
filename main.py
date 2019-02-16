from twilio.rest import Client

account_sid = "ACc6a3820d19ae360248f11bdaa7ad7209"
auth_token = "2c758c7caf207e0958b22eb9c81864db"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="this is a test message!",
                     from_='+16264273513',
                     to='+16265922324'
                 )

