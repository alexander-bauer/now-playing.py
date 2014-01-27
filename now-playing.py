#!/usr/bin/env python

# stdlib dependencies
import sys, os

# External dependencies
import pynotify

NOWPLAYING_FILE = os.path.expandvars("$HOME/.nowplaying")
NOWPLAYING_FORMAT = "{title} - {artist}"

class Hooks:
    def setNowPlaying(this, args):
        with open(NOWPLAYING_FILE, "w") as f:
            f.write(NOWPLAYING_FORMAT.format(**args))
    def sendNotification(this, args):
        # Test if the status change is of a pause. If so, don't send a
        # notification.
        try:
            if args["status"] == "paused":
                return
        except KeyError:
            pass

        # Try to initialize the notification. If it fails, return.
        if not pynotify.init("Now Playing"):
            return

        # Create the notification object, if applicable, and set the
        # priority to low.
        n = pynotify.Notification(args["title"],
                                  args["artist"])
        n.set_urgency(pynotify.URGENCY_LOW)
        n.set_timeout(2000) # milliseconds

        # Show the object. If it fails, fail silently.
        n.show()
    
    def runAll(this, args):
        for hook in this.registered:
            hook(args)

    def __init__(this):
        this.registered = []
        this.registered.append(this.setNowPlaying)
        this.registered.append(this.sendNotification)

def main():
    args = dict(zip(sys.argv[1::2], sys.argv[2::2]))
    
    # Set up a object containing the hooks.
    h = Hooks()
    h.runAll(args)

if __name__ == "__main__":
    sys.exit(main())
