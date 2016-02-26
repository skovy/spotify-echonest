from pyechonest import track

class Echonest:
    def track_attributes(self, id, name):
        try:
            t = track.track_from_id(id)
            res = {
                'name': name,
                'spotify_uri': id,
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
            print "Error occurred finding track '" + id + "' using Echonest."
