from django.db.models import signals

from platypus.apps.music.sync import lastfm_sync
from platypus.apps.music import models as music_app

signals.post_syncdb.connect(lastfm_sync, sender=music_app)