import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="4ced958746604be5ba4055a743a48dad",client_secret="80d312362e3e4e648d135eb3831fbe99"))

happy_lists = ['spotify:playlist:37i9dQZF1DXdPec7aLTmlC', 'spotify:playlist:37i9dQZF1DX4WYpdgoIcn6', 'spotify:playlist:4PY9rbCQSo2JvGdgREogIe', 'spotify:playlist:37i9dQZF1DWTwbZHrJRIgD']

sad_lists = ['spotify:playlist:37i9dQZF1DXbrUpGvoi3TS', 'spotify:playlist:37i9dQZF1DX7qK8ma5wgG1', 'spotify:playlist:07cKOg8bqOupkf5eRFJIY2', 'spotify:playlist:65Dd7x3Y2GOsxyIaMOMUzO']

neutral_lists = ['spotify:playlist:37i9dQZF1DWWQRwui0ExPn', 'spotify:playlist:6TtKChiUG2iRhJ7HL2Nshn', 'spotify:playlist:2KAl1ayr9hJLXbic137j4W', 'spotify:playlist:2rN3mSrzUcgjlj1TcEDTX7']

dull_lists = ['spotify:playlist:4Tplo3zpo39I2w8JvtcF9g', 'spotify:playlist:37i9dQZF1DX4fpCWaHOned', 'spotify:playlist:280hYAs0wM3CswUTZDVBif', 'spotify:playlist:3uisJm2MzCLy1l2ZCPZoRq']

def happy():
    uri = str(random.choice(happy_lists))
    response = sp.playlist_items(uri)
    
    for idx, track in enumerate(response['items'][:10]):
        t = track['track']
        print(idx+1, t['name'])
        print()

def sad():
    uri = random.choice(sad_lists)
    response = sp.playlist_items(uri)
    
    for idx, track in enumerate(response['items'][:10]):
        t = track['track']
        print(idx+1, t['name'])
        print()

def neutral():
    uri = random.choice(neutral_lists)
    response = sp.playlist_items(uri)
    
    for idx, track in enumerate(response['items'][:10]):
        t = track['track']
        print(idx+1, t['name'])
        print()
        
def dull():
    uri = random.choice(dull_lists)
    response = sp.playlist_items(uri)
    
    for idx, track in enumerate(response['items'][:10]):
        t = track['track']
        print(idx+1, t['name'])
        print()

def search(query):
    results = sp.search(q=str(query), limit=20)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx+1, track['name'])