#!/usr/bin/env python

# stdlib dependencies
import sys, os, json

# Get the utility for importing plugins.
import enabled as plugins

NOWPLAYING_FILE = os.path.expandvars("$HOME/.nowplaying")
NOWPLAYING_FORMAT = "{title} - {artist}"

class Hooks:
    def setNowPlaying(this, args):
        with open(NOWPLAYING_FILE, "w") as f:
            f.write(NOWPLAYING_FORMAT.format(**args))

        with open(NOWPLAYING_FILE + ".json", "w") as f:
            json.dump(args, f)

    def runAll(this, args):
        for hook in this.registered:
            hook(args)

    def __init__(this):
        this.registered = []
        this.registered.append(this.setNowPlaying)
        this.registered.append(this.sendNotification)

def main():
    songinfo = dict(zip(sys.argv[1::2], sys.argv[2::2]))
    
    # Run all of the plugins with the songinfo.
    plugins.execute(**songinfo)

if __name__ == "__main__":
    sys.exit(main())
