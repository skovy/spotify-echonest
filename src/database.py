import psycopg2

class Database:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.connect()
        self.create_table()

    def connect(self):
        try:
            self.conn = psycopg2.connect("dbname='spotifyechonest' user='owner' host='localhost' password='h4ck3r'")
            self.cur = self.conn.cursor()
        except:
            print "Unable to connect to the database."

    def create_table(self):
        # make sure we have a connection first
        if self.conn == None:
            print "No database connection."
            return false

        # create the songs table
        sql = """CREATE TABLE IF NOT EXISTS tracks (
            id serial PRIMARY KEY,
            name varchar unique,
            spotify_uri varchar,
            echonest_id varchar,
            speechiness float,
            key int,
            energy float,
            liveness float,
            tempo float,
            acousticness float,
            instrumentalness float,
            mode float,
            time_signature int,
            duration float,
            loudness float,
            valence float,
            danceability float);"""

        self.cur.execute(sql)
        self.conn.commit()

    def add_row(self, data):
        self.cur.execute(
            """INSERT INTO tracks (name, spotify_uri, echonest_id, speechiness, key, energy,
            liveness, tempo, acousticness, instrumentalness, mode,
            time_signature, duration, loudness, valence, danceability) VALUES (
            %(name)s,
            %(spotify_uri)s,
            %(echonest_id)s,
            %(speechiness)s,
            %(key)s,
            %(energy)s,
            %(liveness)s,
            %(tempo)s,
            %(acousticness)s,
            %(instrumentalness)s,
            %(mode)s,
            %(time_signature)s,
            %(duration)s,
            %(loudness)s,
            %(valence)s,
            %(danceability)s);""", data)
        self.conn.commit()

    def close():
        self.cur.close()
        self.conn.close()
