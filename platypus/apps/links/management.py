import urllib2
from datetime import datetime
from time import strptime
try:
    from xml.etree import cElementTree as ET
except ImportError:
    import cElementTree as ET

from django.conf import settings
from django.utils import simplejson
from django.db.models import signals as d_signals

from platypus.apps.links import models as links_app
from platypus import signals

def initial_import(sender=None, **kwargs):
    ''' this function will grab ALL your delicious bookmarks. This should only be run once, past that, use the normal sync function.'''
    try:
        print "adding delicious links..."
        auth_handler = urllib2.HTTPBasicAuthHandler()
        auth_handler.add_password("del.icio.us API", "api.del.icio.us", settings.DELICIOUS_USERNAME, settings.DELICIOUS_PASSWORD)
        opener = urllib2.build_opener(auth_handler)
        tree = ET.parse(opener.open("https://api.del.icio.us/v1/posts/all?"))
        
        root = tree.getroot()
        
        for item in root.getchildren():
            print "adding a link..."
            link, created = links_app.Link.objects.get_or_create(url=item.attrib.get('href'), defaults={
                'title': item.attrib.get('description'),
                'body': item.attrib.get('extended'),
                'tags': item.attrib.get('tag'),
                'date_added': datetime(*strptime(item.attrib.get('time'), '%Y-%m-%dT%H:%M:%SZ')[:6]),
            })
            
            signals.sync_complete.send(
                sender=links_app,
                source='delicious',
                number=1
            )
            
            print "link '%s' added" % link.title
    except urllib2.HTTPError:
        print "something went wrong contacting delicious. Try again later."

d_signals.post_syncdb.connect(initial_import, sender=links_app)