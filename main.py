import time
import requests
import json
import os
from twilio.rest import Client

number = os.getenv('TWILIO_NUMBER')

client = Client()

def text(recipient, message):
    client.messages.create(to=recipient, from_=number, body=message)

text('+12014495049', 'Hello!')

