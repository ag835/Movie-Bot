from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import imdbscraper

app = Flask(__name__)

#Get list and put in plain text
movieList = imdbscraper.getTopMovies()
listMessage = imdbscraper.moviesString(movieList)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()
    #print(incoming_msg)
    responded = False
    
    if 'hi' in incoming_msg:
        msg.body('Hello there')
        responded = True
    if 'movies' in incoming_msg:
        msg.body('Top Movies:\n' + listMessage)
        responded = True
    if 'cat' in incoming_msg:
        msg.media('https://cataas.com/cat')
        responded = True
    if 'commands' in incoming_msg:
        msg.body("Commands:\nmovies\n[movie] info\n[movie] trailer\ncat")
        responded = True
    for movie in movieList:
        if movie.lower() + ' info' in incoming_msg:
            movieInfo = imdbscraper.getMovieInfo(movie.lower())
            infoMessage = imdbscraper.stringMovieInfo(movieInfo)
            msg.body(infoMessage)
            responded = True
        #if movie.lower() + ' trailer' in incoming_msg: (TODO)
            
    if not responded:
        msg.body("Type commands for a list of what I can do")
    ''' just in case
    if len(listMessage) > 1500:
        response = response[0:1500] + '...'
        #Twilio message limit is 1600 characters
    '''
    return str(response)


if __name__ == '__main__':
    app.run()
