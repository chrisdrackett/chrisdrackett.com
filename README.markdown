Issues:
=======

Issues live here: http://chrisdrackett.lighthouseapp.com/projects/4133-platypus/overview

Requirements:
=============

* django trunk
* django tagging
* Element Tree
* [python lastfm (r77)](http://code.google.com/p/python-lastfm/)
* [iso8601](http://pypi.python.org/pypi/iso8601/)

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

Nike+
-----

To use Nike+ you need to turn on sharing on the nike+ website. You then need to add your runner id to settings.

NIKE_PLUS_ID = 'runner_id'

This can be found in the sharing URL that nike gives you, for example my url is:

http://nikerunning.nike.com/nikeplus/?l=runners,runs,77576987,runID,1544907350

in this URL my id is 77576987.


