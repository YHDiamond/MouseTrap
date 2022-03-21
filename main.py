import time
import requests
import json
import os
from twilio.rest import Client
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN)


number = os.getenv('TWILIO_NUMBER')

client = Client()

def text(recipient, message):
    client.messages.create(to=recipient, from_=number, body=message)

caught = False

while True:


    if (GPIO.input(21)):
        if not caught:
            time.sleep(1)
            if (GPIO.input(21)):
                print("Motion Detected!")
                text('+12014495049', 'Mouse exist!')
                caught = True
    else: 
        if (caught):
            time.sleep(300)
            if (not GPIO.input(21)):
                caught = False
        
    