import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='9b9eac62786a44c6b5963349ef6edf1f', client_secret='96511a59b08d4e248f10a9439e256adf')

spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

searchValue=input('Please enter a search term: ')



search = spotify.search(q=searchValue, limit=1, type='track')
search1 = search['tracks']
search2 = search1['items']
print(search2[0]['uri'])
