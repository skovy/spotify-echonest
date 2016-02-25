import spotipy
import spotipy.util as util
from database import Database
from echonest import Echonest

class Spotify:
    def __init__(self, username):
        scope = 'user-library-read'
        self.en = Echonest()
        self.token = util.prompt_for_user_token(username, scope)
        self.db = Database()

    def saved_tracks(self):
        if self.token:
            sp = spotipy.Spotify(auth=self.token)
            results = sp.current_user_saved_tracks()
            return results['items']
        else:
            print "Can't get token"
            return []

    def parse_saved_tracks(self):
        for item in self.saved_tracks():
            # get the song data using Echonest
            data = self.en.track_attributes(item['track']['uri'])
            if data:
                self.db.add_row(data)
