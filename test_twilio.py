# test_twilio.py
import os
from dotenv import load_dotenv
load_dotenv()

from twilio.rest import Client

sid = os.getenv("TWILIO_ACCOUNT_SID")
token = os.getenv("TWILIO_AUTH_TOKEN")
from_phone = os.getenv("TWILIO_FROM_PHONE")
to_list = [p.strip() for p in os.getenv("TWILIO_TO_PHONE","").split(",") if p.strip()]

client = Client(sid, token)
for to in to_list:
    try:
        msg = client.messages.create(body="Test message from SkySentinel (threat is activated secure your area)", from_=from_phone, to=to)
        print("Sent to", to, "sid=", msg.sid)
    except Exception as e:
        print("Failed to send to", to, e)
