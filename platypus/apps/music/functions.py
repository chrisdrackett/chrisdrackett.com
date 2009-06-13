from pylast.pylast import *

from django.conf import settings

def get_user():
    return User(settings.LASTFM_USERNAME, settings.LASTFM_KEY, settings.LASTFM_SECRET, settings.LASTFM_SESSION)