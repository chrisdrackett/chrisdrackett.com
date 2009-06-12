import string

from django.conf import settings

def sync_links():
    feed_items = feedparser.parse("http://feeds.delicious.com/v2/rss/%s" % settings.DELICIOUS_USERNAME)

    for item in feed_items:
        link, created = Link.objects.get_or_create(url=item['u'], defaults={
            'title': item['d'],
            'body': item['n'],
            'tags': string.join(item['t'],' '),
            'date_added': datetime(*strptime(item['dt'], '%Y-%m-%dT%H:%M:%SZ')[:6]),
        })