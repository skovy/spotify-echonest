import spotipy
import spotipy.util as util
import time
from src.db import Database
from src.echonest import Echonest

class Spotify:
    def __init__(self, username):
        scope = 'user-library-read'
        self.en = Echonest()
        self.token = util.prompt_for_user_token(username, scope)
        self.db = Database()

    def saved_tracks(self, limit, offset):
        if self.token:
            sp = spotipy.Spotify(auth=self.token)
            results = sp.current_user_saved_tracks(limit, offset)
            if len(results['items']) == 0:
                print("No more saved tracks :(")
            return results['items']
        else:
            print("Can't get token")
            return []

    def parse_saved_tracks(self, num_of_songs, start = 0):
        offset = start # option to not start at the beginning
        limit = 20 # echonest rate limit :/
        while offset < num_of_songs:
            print("Request at offset " + str(offset))
            for item in self.saved_tracks(limit, offset):
                # get the song data using Echonest
                data = self.en.track_attributes(item)
                if data:
                    self.db.add_row(data)
            offset += limit
            time.sleep(60) # we only have 20 requests/minute
