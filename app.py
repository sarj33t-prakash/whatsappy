import os
from dotenv import load_dotenv

from random import random

import openai
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

load_dotenv()

# OpenAI API Key
openai.api_key = os.getenv('OPEN_AI_KEY')

# Set Credentials obtained from your Twilio Account Dashboard & setup Twilio Client
account_sid = os.getenv('TWILIO_AC_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# from number - Set your virtual mobile number obtained after registering with Twilio
# to number - denotes the mobile number on which you want to receive whatsapp messages like your own number
from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+917016048948'

# model engine to be used while interacting with OpenAi based ChatGPT Module
model_engine = "text-davinci-003"

# Flask App Initialize
app = Flask(__name__)


# Root route of the Flask Web App
# 'Hello World' string is returned when you navigate to your App's URL in browser.
@app.route("/")
def hello():
    return "Hello From Python Flask!"


# Route Redirects this is what we defined as callbacks on Twilio WhatsApp SandBox
# this would be something like the Url where you have hosted this Web Flask App
@app.route("/sms", methods=['POST', 'GET'])
def sms_reply():
    """
        This is the body contents which you send to this Bot from your WhatsApp Number.
        We get the body contents and process it accordingly.
    """
    msg = request.form.get('Body')

    """
        We check if the body contents starts with the prefix "ask"
        then the same is used to trigger the OpenAI ChatGPT for generating AI based text conversation
    """
    if msg.startswith("!ask "):
        resp = MessagingResponse()
        query_key = msg[5:]
        response = generate_ai_response(query_key)          # Generate response
        msg = resp.message(response)
        return str(resp)

    elif msg.startswith("!aimg "):
        resp = MessagingResponse()
        query_key = str(msg[6:])

        image = generate_ai_image(query_key)                # Generate Image

        if image is not None:
            msg = resp.message("Image from OpenAI")         # attach caption to img
            msg.media(image)                                # attach image as media
        return str(resp)


# Function to generate AI Responses
def generate_ai_response(query_key):
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=query_key,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.8,
    )
    if completion.choices[0].text is not None:
        return completion.choices[0].text
    else:
        return ""


# Function to generate AI Images
def generate_ai_image(query_key):
    links = openai.Image.create(
        prompt=query_key,
        n=2,
        size="1024x1024"
    )
    if links is not None and links["data"] is not None:
        image_urls = links["data"]
        if image_urls is not None:
            url = image_urls[0]
            return url["url"]
        else:
            return ""


if __name__ == "__main__":
    app.run(debug=True, port=8000)
