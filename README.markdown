Requirements:
=============

* django trunk
* django tagging
* Element Tree

Instructions:
=============

Add relevant usernames and passwords to settings to get things to sync correctly.

Delicious
---------

platypus will sync *all* your delicious links from forever on syncdb as long as your provide the following in your settings file:

DELICIOUS_USERNAME = 'username'
DELICIOUS_PASSWORD = 'password'

If you need to do this again in the future, just run 'initial_import' from platypus/apps/delicious/sync.