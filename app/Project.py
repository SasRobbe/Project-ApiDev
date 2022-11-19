from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import random

app = FastAPI()

# Implementing security with CORS
origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:63342",
    "http://127.0.0.1:63342",
    "https://projectapidev-sasrobbe.cloud.okteto.net",
    "https://sasrobbe.github.io",
    "https://sasrobbe.github.io."
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# List with data (includes song-names, artists and playlists)
spotify_list = [
    {
        "songName": "Cry Baby",
        "artist": "The Neighbourhood",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "Cry",
        "artist": "Cigarettes After Sex",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "Teen Idle",
        "artist": "MARINA",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "YUKON (INTERLUDE)",
        "artist": "Joji",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "After Hours",
        "artist": "The Weeknd",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "Softcore",
        "artist": "The Neighbourhood",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "Teachers Pet",
        "artist": "Melanie Martinez",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "The Perfect Girl",
        "artist": "Mareux",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "Dead of Night",
        "artist": "Orville Peck",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "Jungle",
        "artist": "Emma Louise",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "Still Dont Know My Name",
        "artist": "Labrinth",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "Passion",
        "artist": "Mason & Julez",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "Sunflower",
        "artist": "Dominique Ilie",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "505",
        "artist": "Arctic Monkeys",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "Jessica",
        "artist": "girlfriends",
        "playlist": "Buttered ears"
    },
    {
        "songName": "I MISS 2003",
        "artist": "AS IT IS",
        "playlist": "Buttered ears"
    },
    {
        "songName": "Misery Business",
        "artist": "Paramore",
        "playlist": "Buttered ears"
    },
    {
        "songName": "adrenaline",
        "artist": "Zero 9:36",
        "playlist": "Buttered ears"
    },
    {
        "songName": "Darkside",
        "artist": "blink-182",
        "playlist": "Buttered ears"
    },
    {
        "songName": "ILL BE DAMNED",
        "artist": "Ryan Oakes, MOD SUN",
        "playlist": "Buttered ears"
    },
    {
        "songName": "Gasoline",
        "artist": "Halsey",
        "playlist": "Ye arc"
    },
    {
        "songName": "Blood // Water",
        "artist": "grandson",
        "playlist": "Ye arc"
    },
    {
        "songName": "HYPNOTIZED",
        "artist": "AViVA",
        "playlist": "Ye arc"
    },
    {
        "songName": "Dizzy",
        "artist": "MISSIO",
        "playlist": "Ye arc"
    },
    {
        "songName": "Feeling Like The End",
        "artist": "Joji",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "Die For You",
        "artist": "Joji",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "Before The Day Is Over",
        "artist": "Joji",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "Dissolve",
        "artist": "Joji",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "NIGHT RIDER",
        "artist": "Joji",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "Glimpse of Us",
        "artist": "Joji",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "BLAHBLAHBLAH DEMO",
        "artist": "Joji",
        "playlist": "Bus Vibes"
    },
    {
        "songName": "1AM FREESTYLE",
        "artist": "Joji",
        "playlist": "Bus Vibes"
    }
]


# define the classes
class spotify_out(BaseModel):
    songName: str
    artist: str
    playlist: str


class spotify_in(BaseModel):
    songName: str | None = Field(min_length=3)
    artist: str | None = Field(min_length=3)
    playlist: str | None = Field(min_length=3)


# gets a random song with their corresponding artist and playlist from the data defined above
@app.get("/spotify", response_model=spotify_out)
async def return_spotify():
    random_int = random.randint(0, len(spotify_list)-1)
    return spotify_list[random_int]


# add a new song with their corresponding artist and playlist
@app.post("/spotify", response_model=list[spotify_out])
async def insert_spotify(spotify: spotify_in):
    spotify_list.append(spotify.dict())
    return spotify_list


# gets all songs of a specific playlist from the data defined above
@app.get("/playlists")
async def return_playlist(
    playlist: str = Query(
        default="Bus Vibes",
        description="This parameter indicates which playlist should be returned by the API. All songs within that "
                    "playlist along with their artist will be returned."
    )
):
    songs = []
    for i in range(len(spotify_list)):
        if playlist == spotify_list[i]['playlist']:
            playlist_songs = {}
            playlist_songs["songName"] = spotify_list[i]['songName']
            playlist_songs["artist"] = spotify_list[i]['artist']
            playlist_songs["playlist"] = spotify_list[i]['playlist']
            songs.append(playlist_songs)
    return {"playlists": songs}


# gets all songs of a specific artist from the data defined above
@app.get("/artist/{getArtist}")
async def return_songs_of_artist(getArtist: str):
    songs2 = []
    for y in range(len(spotify_list)):
        if getArtist == spotify_list[y]['artist']:
            artist_songs = {}
            artist_songs["songName"] = spotify_list[y]['songName']
            artist_songs["artist"] = spotify_list[y]['artist']
            artist_songs["playlist"] = spotify_list[y]['playlist']
            songs2.append(artist_songs)
    return {"artists": songs2}
