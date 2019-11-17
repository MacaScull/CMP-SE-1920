from newsDownloader import news
from termExtraction import terms
from spotifyConnection import SpotifyAPI

findNews = news()
findTerms = terms()
spotify = SpotifyAPI()

findNews.getNews()
findTerms.tf(findNews.newsData[0])
spotify.search(findTerms.frequencyData[0][0])
