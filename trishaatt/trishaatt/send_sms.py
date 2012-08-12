from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
account_sid = "AC0d6876c62dad85921396d0be389b68b3"
auth_token = "662e15601a3bdb6e6ca46f0c226ab750"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.sms.messages.create(to="+15126668669", from_="+15555555555",
                                     body="Hello there!")
