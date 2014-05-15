import json, os

NOWPLAYING_FILE = os.path.expandvars("$HOME/.nowplaying")

def trigger(**songinfo):
    return True;

def execute(**songinfo):
    print("Executing statusfile")

    with open(NOWPLAYING_FILE, "w") as f:
        if "title" in songinfo and "artist" in songinfo:
            f.write("{title} - {artist}".format(**songinfo))

    with open(NOWPLAYING_FILE + ".json", "w") as f:
        json.dump(songinfo, f)
