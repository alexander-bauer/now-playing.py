# External dependencies
import pynotify

def trigger(**songinfo):
    # Test if the status change is of a pause. If so, don't send a
    # notification.
    if "status" in songinfo and status == "paused":
        return False
    else:
        return True


def execute(**songinfo):
    # Try to initialize the notification. If it fails, return.
    if not pynotify.init("Now Playing"):
        return

    # Check if an album art URI has been provided, and if so,
    # supply it.
    uri = ""
    if "art" in songinfo:
        if not "://" in art:
            uri = "file://" + art

    # Create the notification object, if applicable, and set the
    # priority to low.
    n = pynotify.Notification(title,
                              artist,
                              art)
    n.set_urgency(pynotify.URGENCY_LOW)
    n.set_timeout(2000) # milliseconds

    # Show the object. If it fails, fail silently.
    n.show()
