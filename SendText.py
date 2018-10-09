from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Axxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# Your Auth Token from twilio.com/console
auth_token  = '[AuthToken]'

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="[phone number]", 
    from_="+12408337709",
    body="Just built my first SMS app using Twilio",)

print(message.sid)
