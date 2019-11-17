import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.util import prompt_for_user_token

#Code that authorizes the application to use all available resources in the Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id='9b9eac62786a44c6b5963349ef6edf1f', client_secret='96511a59b08d4e248f10a9439e256adf')
#spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

class SpotifyAPI:
    def __init__(self):
        token = ''
        spotify = ''
        currentUserID = ''
        playlistID = ''
        self.songURIList = []

    def promptLogin(self, uN): #Gives the app the ability to access spotify user data, allowing the creation of playlists. Must be called each time the app is run, otherwise app won't work (Spotify username is only input needed)
        self.token = prompt_for_user_token(uN, scope='playlist-modify-private', client_id='9b9eac62786a44c6b5963349ef6edf1f', client_secret='96511a59b08d4e248f10a9439e256adf', redirect_uri='http://localhost')
        self.spotify = spotipy.Spotify(auth=self.token, client_credentials_manager=client_credentials_manager)
        currentUser = self.spotify.current_user()
        self.currentUserID = currentUser['id']

    def search(self, sV): #Searches for a spotify track using a given search term and appends the uri to a list of song URIs
        search = self.spotify.search(q=sV, limit=1, type='track')
        search1 = search['tracks']
        search2 = search1['items']
        self.songURIList.append(search2[0]['uri'])

    def createPlaylist(self, pN): #Creates an empty playlist using a given name and it's ID is recorded
        playlist = self.spotify.user_playlist_create(self.currentUserID,pN,public=False)
        self.playlistID = playlist['id']

    def addToPlaylist(self): #Adds the list of track URIs to the playlist created in createPlaylist
        self.spotify.user_playlist_add_tracks(self.currentUserID,self.playlistID, self.songURIList)
