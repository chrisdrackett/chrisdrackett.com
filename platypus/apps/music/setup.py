from pylast.pylast import SessionKeyGenerator, md5, User

from django.core.management import setup_environ

from platypus import settings

setup_environ(settings)

def setup():
    username = settings.LASTFM_USERNAME
    password = md5(settings.LASTFM_PASSWORD)

    if not settings.LASTFM_SESSION:
        session_key = SessionKeyGenerator(settings.LASTFM_KEY, settings.LASTFM_SECRET).get_session_key(username, password)
        print "add %s to LASTFM_SESSION in your settings file and run this file again to make sure everything is working." % session_key
    else:
        session_key = settings.LASTFM_SESSION
        user = User(username, settings.LASTFM_KEY, settings.LASTFM_SECRET, session_key)
        
        print "you are all set as %s!" % user.get_name()

if __name__ == '__main__':
    setup()