from pyechonest import track

class Echonest:
    def track_attributes(self, item):
        spotify_uri = item['track']['uri']
        spotify_track_name = item['track']['name']
        spotify_album_name = item['track']['album']['name']
        spotify_album_cover_url = item['track']['album']['images'][0]['url']
        try:
            t = track.track_from_id(spotify_uri)
            res = {
                'name': spotify_track_name,
                'spotify_uri': spotify_uri,
                'spotify_album_cover_url': spotify_album_cover_url,
                'spotify_album_name': spotify_album_name,
                'echonest_id': t.id,
                'speechiness': t.speechiness,
                'key': t.key,
                'energy': t.energy,
                'liveness': t.liveness,
                'tempo': t.tempo,
                'acousticness': t.acousticness,
                'instrumentalness': t.instrumentalness,
                'mode': t.mode,
                'time_signature': t.time_signature,
                'duration': t.duration,
                'loudness': t.loudness,
                'valence': t.valence,
                'danceability': t.danceability
            }
            return res
        except:
            print("Error occurred finding track '" + spotify_uri + "' using Echonest.")
