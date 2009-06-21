import logging
from datetime import datetime

from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from platypus import signals

log = logging.getLogger('events.models')

class Event(models.Model):
    class Meta:
        get_latest_by = 'date_updated'

    source = models.CharField(max_length=100, db_index=True)
    number = models.PositiveIntegerField()

    date_updated = models.DateTimeField(null=True, editable=False)

    def save(self, *args, **kwargs):
        self.date_updated = datetime.utcnow()
        super(Event, self).save(*args, **kwargs)

def add_event(sender, source, number, **kwargs):
    all_done = False # if the latest event is from the same source, we'll
                     # change this to true and just update the latest event.
    try:
        event = Event.objects.latest()
        if event.source == source:
            event.number += number
            event.save()
            all_done = True
    except Event.DoesNotExist:
        pass
    
    if not all_done:
        Event.objects.create(
            source = source,
            number = number
        )
signals.sync_complete.connect(add_event)