import sys
from src.database import Database
from src.spotify import Spotify

def main():
    # collect the user's name if possible
    username = ""
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print "Please pass your Spotify username as the first parameter."
        sys.exit()

    # create and validate a Spotify session
    sp = Spotify(username)
    sp.parse_saved_tracks()

if __name__ == "__main__":
    main()
