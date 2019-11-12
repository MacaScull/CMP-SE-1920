import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#Code that authorizes the application to use all available resources in the Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id='9b9eac62786a44c6b5963349ef6edf1f', client_secret='96511a59b08d4e248f10a9439e256adf')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

class SpotifyAPI:
    def __init__(self):
        pass

    def search(self, sV): #Searches for a spotify track using a given search term
        search = spotify.search(q=sV, limit=1, type='track')
        search1 = search['tracks']
        search2 = search1['items']
        return(search2[0]['uri'])


