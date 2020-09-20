'''TODO:
#connect to Twilio / SMS service
#look into how to remove whitespace from cast / not get html ghost element
#look into how to get x movies if some are skipped bc of ratings (list?)
#maybe use a dictionary?
#why did the output speed decrease so much?
#clean up this mess
'''

import bs4
import requests
from datetime import datetime, timedelta

def scrapeData():

    #Set the range of release dates, from x months ago to last month
    today = datetime.today()
    months = 7
    offset = 3
    lastMonth = (today - timedelta(days=30)).strftime("%Y-%m-%d")
    dateFrom = (today - timedelta(days=31*months-offset)).strftime('%Y-%m-%d')

    #Get and set up the webpage
    res = requests.get('https://www.imdb.com/search/title/?title_type=feature&release_date='+str(dateFrom)+','+str(lastMonth)+'&countries=us&languages=en')
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    #parse x movies
    numMovies = 16
    for x in range(1, numMovies):

        #get title
        elem = soup.select('div.lister-item:nth-child('+str(x)+') > div:nth-child(3) > h3:nth-child(1) > a:nth-child(2)')
        title = elem[0].text.strip()

        #get ratings and votes
        elem = soup.select('div.lister-item:nth-child('+str(x)+') > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > strong:nth-child(2)')
        userRating = elem[0].text.strip()
        elem = soup.select('div.lister-item:nth-child('+str(x)+') > div:nth-child(3) > p:nth-child(6) > span:nth-child(2)')
        userVotes = elem[0].text.strip()
        elem = soup.select('div.lister-item:nth-child('+str(x)+') > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > span:nth-child(1)')
        if len(elem) != 0:
            metascore = elem[0].text.strip()
        else:
            metascore = 'N/A '


        #Skip poorly rated movies
        #might not matter much since results are sorted by popularity
        if (float(userRating) < 5 and int(metascore) < 50):
            continue

        '''#get rating, runtime, and genres
        elem = soup.select('div.lister-item:nth-child('+str(x)+') > div:nth-child(3) > p:nth-child(2) > span:nth-child(1)')
        certificate = elem[0].text.strip()
        elem = soup.select('div.lister-item:nth-child('+str(x)+') > div:nth-child(3) > p:nth-child(2) > span:nth-child(3)')
        runtime = elem[0].text.strip()
        elem = soup.select('div.lister-item:nth-child('+str(x)+') > div:nth-child(3) > p:nth-child(2) > span:nth-child(5)')
        genre = elem[0].text.strip()

        #get description
        elem = soup.select('div.lister-item:nth-child('+str(x)+') > div:nth-child(3) > p:nth-child(4)')
        desc = elem[0].text.strip()

        #get cast and crew
        elem = soup.select('div.lister-item:nth-child('+str(x)+') > div:nth-child(3) > p:nth-child(5)')
        cast = elem[0].text.strip()

        #elem = soup.select('div.lister-item:nth-child('+str(x)+') > div:nth-child(3) > p:nth-child(5) > a:nth-child(1)')
        #director = elem[0].text.strip()

        #test = cast.strip()
        #print('Director: ' + director + ' | ' + cast)'''

        #print info
        print(title)
        '''print(userRating + ' (' + userVotes + ' votes)\t' + metascore + ' Metascore')
        print(certificate + ' | ' + runtime + ' | ' + genre)
        print(desc)
        print(cast)'''

        print()

//print(scrapeData())
