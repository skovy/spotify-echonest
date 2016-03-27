### Spotify - Echonest

This basic script will authenticate with your Spotify account and retrieve the
most recently saved songs. An audio summary (if available) will be retrieved
from Echonest using the Spotify URI for each track.

The purpose of this is to provide data to work with locally to run analysis.

#### Install Dependencies

- `psycopg2` - PostgreSQL Python
- `spotipy` - Python Spotify Wrapper
- `pyechonest` - Python Echonest Wrapper

`pip install psycopg2 spotipy pyechonest`

#### Setup the Database to save the track data

```psql
# CREATE USER owner WITH PASSWORD 'h4ck3r';
# CREATE DATABASE spotifyechonest OWNER owner;
# \list
# \connect spotifyechonest
# \dt
```

#### Add Environment Variables for Spotify/Echonest API's

```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='http://localhost'
export ECHO_NEST_API_KEY='your-echonest-api-key'
```

#### Run the script

- `python main.py <spotify-username>`
- Spotify Authentication will open in your default browser
- Grant Access
- Copy the URL to the terminal when prompted (contains the Spotify code)
- The `tracks` table in the `spotifyechonest` database will contain the data
