import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import snowflake.connector

# Spotify API credentials
client_id = 'b8fd29a6a70a4dc8b6c9d2676a899664'
client_secret = '5d841595feba41748439da2bfbc7ac43'

# Initialize Spotipy client
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Snowflake connection parameters
snowflake_config = {
    'user': 'NITHIN',
    'password': 'Nithin@2024',
    'account': 'azqcwil-tf37140',
    'database': 'PRODUCTSDATA',
    'schema': 'PUBLIC'
}

# Data to insert
play_history_data = [
    {
        "username": "31nheg6wm3pgwmgdmty6qdjexazi",
        "conn_country": "IN",
        "master_metadata_track_name": "Nee Yadalo Naaku",
        "master_metadata_album_artist_name": "Yuvan Shankar Raja",
        "master_metadata_album_album_name": "Awaara",
        "spotify_track_uri": "spotify:track:4wUOdPcYoqYZGM2wSdoLQu"
    },
    {
        "username": "31nheg6wm3pgwmgdmty6qdjexazi",
        "conn_country": "IN",
        "master_metadata_track_name": "Nee Yadalo Naaku",
        "master_metadata_album_artist_name": "Yuvan Shankar Raja",
        "master_metadata_album_album_name": "Awaara",
        "spotify_track_uri": "spotify:track:4wUOdPcYoqYZGM2wSdoLQu"
    },
    {
        "username": "31nheg6wm3pgwmgdmty6qdjexazi",
        "conn_country": "IN",
        "master_metadata_track_name": "Kaadhal Endral",
        "master_metadata_album_artist_name": "Yuvan Shankar Raja",
        "master_metadata_album_album_name": "Goa (Original Motion Picture Soundtrack)",
        "spotify_track_uri": "spotify:track:5jXrULyYKHjkAMk4TXZFoG"
    }
]

# Connect to Snowflake
conn = snowflake.connector.connect(**snowflake_config)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE OR REPLACE TABLE play_history (
    id INTEGER AUTOINCREMENT PRIMARY KEY,
    username VARCHAR(255),
    conn_country VARCHAR(255),
    master_metadata_track_name VARCHAR(255),
    master_metadata_album_artist_name VARCHAR(255),
    master_metadata_album_album_name VARCHAR(255),
    spotify_track_uri VARCHAR(255),
    playback_length INTEGER,
    song_url VARCHAR(255),
    album_image_url VARCHAR(255)
)
""")

# Insert data into the table
for entry in play_history_data:
    # Get track information
    track_info = sp.track(entry['spotify_track_uri'])
    
    # Extract image URLs
    album_image_url = track_info['album']['images'][0]['url'] if track_info['album']['images'] else None
    
    # Insert data into the table
    cursor.execute("""
    INSERT INTO play_history
    (username, conn_country, master_metadata_track_name,
    master_metadata_album_artist_name, master_metadata_album_album_name,
    spotify_track_uri, playback_length, song_url, album_image_url)
    VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """,
    (
        entry['username'], entry['conn_country'],
        entry['master_metadata_track_name'],
        entry['master_metadata_album_artist_name'],
        entry['master_metadata_album_album_name'],
        entry['spotify_track_uri'],
        entry.get('ms_played', 0),  # assuming playback_length is in milliseconds
        entry['spotify_track_uri'],  # assuming song_url is the same as spotify_track_uri
        album_image_url
    )
)

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()
