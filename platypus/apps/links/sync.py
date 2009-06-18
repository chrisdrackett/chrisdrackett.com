import string, urllib
from datetime import datetime
from time import strptime

from django.conf import settings
from django.utils import simplejson

from platypus import signals
from platypus.apps.links.models import Link

def delicious_sync():
    links = simplejson.loads(urllib.urlopen("http://feeds.delicious.com/v2/json/%s" % settings.DELICIOUS_USERNAME).read())
    
    number = 0
    source = 'delicious'
    
    for item in links:
        link, created = Link.objects.get_or_create(url=item['u'], defaults={
            'title': item['d'],
            'body': item['n'],
            'tags': string.join(item['t'],' '),
            'date_added': datetime(*strptime(item['dt'], '%Y-%m-%dT%H:%M:%SZ')[:6]),
        })
        if created:
            number += 1
        
    if number > 0:
        signals.sync_complete.send(
            sender=self,
            source=source,
            number=number
        )