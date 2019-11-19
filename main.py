from newsDownloader import news
from termExtraction import terms
from spotifyConnection import SpotifyAPI

findNews = news()
findTerms = terms()
spotify = SpotifyAPI()

#Asks user for spotify username and calls to promptLogin, which gives app permission to create and add to playlists
userName = input('Please enter your username/email used for Spotify: ')
spotify.promptLogin(userName)

#Asks user for a name for the playlist
playlistName = input('Please enter the name of the playlist you would like to create: ')
spotify.createPlaylist(playlistName)

#Gets news from news API
findNews.getNews()


#Loops through news taken from API and uses findTerms to get the frequency of terms
for i in findNews.newsData:
    findTerms.tf(i)
    try:
        #Searches using filtered terms and appends to song list
        spotify.search(findTerms.frequencyData[0][0])
    except:
        findTerms.tfClear()
        continue

#Adds songs to playlist
spotify.addToPlaylist()

print('Playlist created successfully')
