import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
client_id = 'b8fd29a6a70a4dc8b6c9d2676a899664'
client_secret = '5d841595feba41748439da2bfbc7ac43'

# Initialize Spotipy client
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Spotify track URI
spotify_track_uri = 'spotify:track:4wUOdPcYoqYZGM2wSdoLQu'

# Get track information
track_info = sp.track(spotify_track_uri)

# Extract image URLs
image_urls = [image['url'] for image in track_info['album']['images']]

# Print image URLs
print("Image URLs:")
for url in image_urls:
    print(url)
