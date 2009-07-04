from datetime import datetime

from django.db import models

from platypus.apps.common_models import Base

FELT = (
    (1,'Awesome'),
    (2,'So-So'),
    (3,'Sluggish'),
    (4,'Injured')
)

WEATHER = (
    (1, 'Sunny'),
    (2, 'Cloudy'),
    (3, 'Rainy'),
    (4, 'Snowy')
)

TERRAIN = (
    (1, 'Road'),
    (2, 'Trail'),
    (3, 'Treadmill'),
    (4, 'Track')
)

class Run(Base):
    class Meta:
        verbose_name_plural = 'Runs'
    
    distance = models.DecimalField()
    duration = models.PositiveIntegerField()
    calories = models.DecimalField()
    how_felt = models.CharField(blank=True, max_length=1, choices=FELT)
    weather = models.CharField(blank=True, max_length=1, choices=WEATHER)
    terrain = models.CharField(blank=True, max_length=1, choices=TERRAIN)
    
    def __unicode__(self):
        return str(self.runid)