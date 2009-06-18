from datetime import datetime

from platypus.apps.music.functions import get_user
from platypus.apps.music.models import WeeklyUpdate, Track, Artist

def sync_tracks(*args, **kwargs):
    user = get_user()
    for from_date, to_date in user.get_weekly_chart_dates():
        if not WeeklyUpdate.objects.filter(ident=from_date):
            tracks = user.get_weekly_track_charts(from_date, to_date)
            
            for track in tracks:
                WeeklyUpdate.objects.create(
                    track=Track.objects.get_or_create(id=track.get_item().get_id(), defaults={
                        'url': track.get_item().get_url(),
                        'name': track.get_item().get_title(),
                        'artist': Artist.objects.get_or_create(mbid=track.get_item().get_artist().get_mbid(), defaults={
                            'name': track.get_item().get_artist().get_name(),
                            'url': track.get_item().get_artist().get_url(),
                            'image': track.get_item().get_artist().get_image_url()
                        })[0]
                    })[0],
                    playcount=track.get_weight(),
                    position=track.get_position(),
                    ident=from_date,
                    date_added=datetime.fromtimestamp(int(from_date))
                )