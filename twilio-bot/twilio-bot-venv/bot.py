#https://www.twilio.com/blog/build-a-sms-chatbot-with-python-flask-and-twilio
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    #add webhook logic here and return a reponse
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()
    responded = False
    if 'quote' in incoming_msg:
        #add quote here
        responded = True
    if 'cat' in incoming msg:
        #add pic here
        responded = True
    if not responded:
        #return generic response here
    return str(response)

msg.body('this is the reponse text')
msg.media(image_url)


