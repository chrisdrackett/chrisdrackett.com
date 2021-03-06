from django.db import models
from django.conf import settings

from platypus.apps.common_models import Base

class Artist(Base):
    class Meta:
        verbose_name_plural = 'Artists'
    
    name = models.CharField(max_length=250)
    mbid = models.CharField(max_length=36)
    url = models.URLField(max_length=300)
    image = models.URLField(null=True)
    
    def __unicode__(self):
        return self.name

class Track(Base):
    class Meta:
        verbose_name_plural = 'Tracks'

    name = models.CharField(max_length=250)
    artist = models.ForeignKey(Artist)
    url = models.URLField(max_length=300)
    
    def __unicode__(self):
        return self.name
    
    @property
    def playcount(self):
        itemCount = 0
        for item in self.weeklyupdate_set.all():
            itemCount += item.playcount
        return itemCount

    @property
    def current_position(self):
        return self.weeklyupdate_set.latest().position

    @property
    def get_short_history(self):
        history = []
        for item in self.weeklyupdate_set.latest()[:10]:
            state = {}
            state['chart'] = item.position
            state['playcount'] = item.playcount
            histroy.append(state)
        return history

class TrackUpdate(Base):
    class Meta:
        verbose_name_plural = 'Weekly Updates'

    track = models.ForeignKey(Track)
    position = models.IntegerField()
    playcount = models.IntegerField()
    start_date = models.DateTimeField()