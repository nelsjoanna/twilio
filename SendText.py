from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACfe1e178ecc6c9236796d1cfccda868bf"
# Your Auth Token from twilio.com/console
auth_token  = "fa1c9ff3fb857a1af2e811f516c86d3b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17038015678", 
    from_="+12408337709",
    body="Just built my first SMS app using Twilio",)

print(message.sid)
