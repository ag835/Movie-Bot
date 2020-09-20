from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import imbdscraper

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()
    responded = False
    if 'hi' || 'hello' || 'hey' in incoming_msg:
        msg.body('Hello there')
        responded = True
    if 'movies' in incoming_mg:
        msg.body(print(scrapeData()))
        responded = True
    if 'cat' in incoming_msg:
        msg.body("Brownie pics soon")
        responded = True
    if not responded:
        msg.body("Check commands for a list of what I can do.")
    return str(response)


if __name__ == '__main__':
    app.run()


