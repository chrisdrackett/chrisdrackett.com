import lastfm
from datetime import datetime

from django.conf import settings

from platypus import signals
from platypus.apps.music.models import TrackUpdate, Track, Artist

def lastfm_sync(*args, **kwargs):
    api = lastfm.Api(settings.LASTFM_KEY)
    user = api.getUser(settings.LASTFM_USERNAME)
    
    track_number = 0
    artist_number = 0
    
    for chart in user.weeklyTrackChartList:
        if not TrackUpdate.objects.filter(start_date=chart.start):
            print "getting tracks for chart from %s" % chart.start
            for track in chart.tracks:
                try:
                    track._fillInfo()
                except:
                    pass
                try:
                    image = track.artist.image['large']
                except:
                    image = None
                
                artist, a_created = Artist.objects.get_or_create(name=track.artist.name, defaults={
                    'mbid': track.artist.mbid,
                    'url': track.artist.url,
                    'image': image
                })
                print "adding artist %s" % artist.name
                
                if a_created:
                    print "The above is new..."
                    artist_number += 1
                
                new_track, t_created = Track.objects.get_or_create(id=track.id, defaults={
                    'url': track.url,
                    'name': track.name,
                    'artist': artist
                })
                print "adding track %s" % new_track.name
                
                if t_created:
                    print "The above is new..."
                    track_number += 1
                
                TrackUpdate.objects.create(
                    track=new_track,
                    playcount=track.stats.playcount,
                    position=track.stats.rank or 1,
                    start_date=chart.start,
                    date_added=chart.start
                )
                print "adding track update."
    if artist_number > 0:
        signals.sync_complete.send(
            sender=self,
            source="lastfm_artist",
            number=artist_number
        )
    if track_number > 0:
        signals.sync_complete.send(
            sender=self,
            source="lastfm_track",
            number=track_number
        )

