#!/usr/bin/env python

import sys, os

NOWPLAYING_FILE = os.path.expandvars("$HOME/.nowplaying")
NOWPLAYING_FORMAT = "{title} - {artist}"

class Hooks:
    def setNowPlaying(this, args):
        with open(NOWPLAYING_FILE, "w") as f:
            f.write(NOWPLAYING_FORMAT.format(**args))
    
    def runAll(this, args):
        for hook in this.registered:
            hook(args)

    def __init__(this):
        this.registered = []
        this.registered.append(this.setNowPlaying)

def main():
    args = dict(zip(sys.argv[1::2], sys.argv[2::2]))
    
    # Set up a object containing the hooks.
    h = Hooks()
    h.runAll(args)

if __name__ == "__main__":
    sys.exit(main())
