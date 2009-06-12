Requirements:
=============

* django trunk
* django tagging
* Element Tree
* [pylastfm](http://github.com/chrisdrackett/pylastfm)

Instructions:
=============

Add relevant usernames and passwords to settings to get things to sync correctly.

Delicious
---------

platypus will sync *all* your delicious links from forever on syncdb as long as your provide the following in your settings file:

DELICIOUS_USERNAME = 'username'
DELICIOUS_PASSWORD = 'password'

If you need to do this again in the future, just run 'initial_import' from platypus/apps/links/sync.

Last.fm
-------

to sync with last.fm you need to setup an infinite session.

1. sign up for the last.fm API: http://www.last.fm/api
2. add your key, secret, username, and password to the platypus settings file (LASTFM_KEY, LASTFM_SECRET, LASTFM_USERNAME, LASTFM_PASSWORD)
3. run 'python setup.py' from within the platypus/apps/music folder. It will output a session key.
4. copy the session key into your settings file under LASTFM_SESSION
5. run the setup.py file again, it should print that things are working along with your username.