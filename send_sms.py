from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)

my_msg = 'Who am I? Who am I trying to be? Not myself, anyone but myself. Living in a fantasy to bury the reality, Making myself the mystery, A strong facade disguising the misery. Empty, but beyond the point of emptiness, Full to brim with fake confidence, A guard that will never be broken, Because I broke a long time ago. I’m hurting but don’t tell anyone. No one needs to know. Don’t show or you’ve failed. Always okay, always fine, always on show. The show must go on. It will never stop. The show must not go on, But I know it will. I give up. I give up giving up. I am lost. I don’t need to be saved, I need to be found.'

message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
