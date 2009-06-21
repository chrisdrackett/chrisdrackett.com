Issues:
=======

Issues live here: http://chrisdrackett.lighthouseapp.com/projects/4133-platypus/overview

Requirements:
=============

* django trunk
* django tagging
* Element Tree
* [python lastfm (r77)](http://code.google.com/p/python-lastfm/)

Instructions:
=============

Add relevant usernames and passwords to settings to get things to sync correctly.

Delicious
---------

platypus will sync *all* your delicious links from forever on 'syncdb' as long as your provide the following in your settings file:

DELICIOUS_USERNAME = 'username'
DELICIOUS_PASSWORD = 'password'

If you need to do this again in the future, just run 'initial_import' from platypus/apps/links/management.py.

Last.fm
-------

to use last.fm syncing you are going to need access to the last.fm api. Sign up [here](http://www.last.fm/api): 

platypus will sync *all* your last.fm tracks and artists from forever on 'syncdb' as long as your provide the following in your settings file:

LASTFM_KEY = 'key'
LASTFM_USERNAME = 'username'

If you need to do this again in the future, just run 'initial_import' from platypus/apps/music/management.py.