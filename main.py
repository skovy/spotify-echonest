import sys
from src.db import Database
from src.spotify import Spotify

def main():
    # collect the user's name if possible
    username = ""

    # modify the offset (optional second parameter) to start at an offset in
    # saved tracks, ex: if it fails at offset 200 or the script is killed change
    # the parameter to 200-220 (depending when it failed)
    offset = 0

    # the total number of tracks to retrieve an audio summary for, (optional
    # third parameter)
    total_tracks = 200

    if len(sys.argv) > 1:
        username = sys.argv[1]
        if len(sys.argv) > 2:
            offset = int(sys.argv[2])
        if len(sys.argv) > 3:
            total_tracks = int(sys.argv[3])
    else:
        print("Please pass your Spotify username as the first parameter.")
        sys.exit()

    # create and validate a Spotify session
    sp = Spotify(username)
    sp.parse_saved_tracks(offset, total_tracks)

if __name__ == "__main__":
    main()
