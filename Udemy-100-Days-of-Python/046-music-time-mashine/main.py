import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100
date = input("Which year do yo want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
songs_html = soup.select("li ul li h3")
songs = [song.getText().strip() for song in songs_html]

# Spotify Authentication
CLIENT_ID = "YOUT SPORIFY ID"
CLIENT_SECRET = "YOUT SPORIFY SECRET"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://example.com",  # or your spotify redirect URL
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt",
        username="YOUT SPORIFY USERNAME",
    )
)

user_id = sp.current_user()["id"]

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(
    user=user_id,
    name= f"{date} Billboard 100",
    public=False
)

# Adding songs found into the new playlist
sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=song_uris
)