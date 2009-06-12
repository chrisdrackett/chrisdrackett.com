from datetime import datetime
from time import strptime
import string

from django.conf import settings
from django.utils import simplejson

def sync_links():
    links = json.loads(urllib.urlopen("http://feeds.delicious.com/v2/rss/%s" % settings.DELICIOUS_USERNAME).read())
    
    for item in links:
        link, created = Link.objects.get_or_create(url=item['u'], defaults={
            'title': item['d'],
            'body': item['n'],
            'tags': string.join(item['t'],' '),
            'date_added': datetime(*strptime(item['dt'], '%Y-%m-%dT%H:%M:%SZ')[:6]),
        })