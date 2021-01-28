import bs4
import requests
from urllib.request import Request, urlopen
from datetime import datetime, timedelta


def getMovies():
    #Set the range of release dates, from x months ago to last month
    today = datetime.today()
    months = 7
    offset = 3
    lastMonth = (today - timedelta(days=30)).strftime("%Y-%m-%d")
    dateFrom = (today - timedelta(days=31*months-offset)).strftime('%Y-%m-%d')

    #Get and set up the webpage
    url = 'https://www.imdb.com/search/title/?title_type=feature&release_date='+str(dateFrom)+','+str(lastMonth)+'&countries=us&languages=en'
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    movieContainers = soup.find_all('div', class_ = 'lister-item mode-advanced')
    
    return movieContainers

#Retrieve the top movies from a certain time period in a list
def getTopMovies():
    movieContainers = getMovies()
    topMovies = []
    limit = 15
 
    #Get movie titles
    for i in range(limit):
        movie = movieContainers[i]
        title = movie.h3.a.text
        topMovies.append(title)

    return topMovies

#Format the list of movies into a string for the text message
def moviesString(movieList):
    output = ''
    for i in range(len(movieList)):
        output += str(i+1) + '. ' + movieList[i] + '\n'

    return output

def getMovieInfo(movie):
    #for movie in movielist:
    #if title == movie
    #get info and store in list
    movieInfo = {}
    movieContainers = getMovies()
    for container in movieContainers:
        title = container.h3.a.text
        if title.lower() == movie:

            year = container.h3.find('span', class_ = 'lister-item-year text-muted unbold')
            year = year.text

            rating = container.p.find('span', class_ = 'certificate').text
            runtime = container.p.find('span', class_ = 'runtime').text

            genres = container.p.find('span', class_ = 'genre').text.strip()

            summary = container.find_all('p', class_ = 'text-muted')
            summary = summary[1].text.strip()

            '''
            needs more cleaning/formatting:
            castcrew = movie.find('p', class_ = "").text.strip()
            print(castcrew)
            '''

            imdb = float(container.strong.text)

            #Get metascore if it exists (fix)
            if container.find('span', class_ = 'metascore favorable') is not None:
                metascore = container.find('span', class_ = 'metascore favorable')
            elif container.find('span', class_ = 'metascore mixed') is not None:
                metascore = container.find('span', class_ = 'metascore mixed')
            else:
                container = container.find('span', class_ = 'metascore unfavorable')
            metascore = int(metascore.text)

            movieInfo = {
                'title': title,
                'year': year,
                'rating': rating,
                'runtime': runtime,
                'genres': genres,
                'summary': summary,
                'imdb': imdb,
                'metascore': metascore
                }

    return movieInfo
                  
def stringMovieInfo(movieInfo):
    
    output = ''
    
    output += movieInfo['title'] + ' ' + movieInfo['year'] + '\n'
    output += movieInfo['rating'] + ' | ' + movieInfo['runtime'] + '\n'
    output += movieInfo['genres'] + '\n'
    output += movieInfo['summary'] + '\n'
    output += 'IMDb rating: ' + str(movieInfo['imdb']) + '\n'
    output += 'Metascore: ' + str(movieInfo['metascore'])
    print(output)

    return output

def getWebpage(url):
    
    res = Request(url)
    #res.raise_for_status()
    webpage = urlopen(res).read()
    soup = bs4.BeautifulSoup(webpage, 'html.parser')

    return soup

#TODO
def getMovieTrailer(movie):

    inner_soup = getWebpage(movie["imdb_link"])
    print(inner_soup)
    


'''
for testing
movie = 'soul'
#print(getMovieInfo(movie))
movieInfo = getMovieInfo(movie)
#stringMovieInfo(getMovieInfo(movie))
#webPage = getWebpage('http://imdb.com')
#getMovieTrailer('Soul')
'''
    
