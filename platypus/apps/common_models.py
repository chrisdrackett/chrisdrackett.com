import logging
from datetime import datetime

from django.db import models

from platypus.apps.updates.models import Update

class Base(models.Model):
    class Meta:
        abstract = True
        get_latest_by = 'date_added'

    # meta
    tags = TagField()
    published = models.BooleanField(default=True)
    allow_comments = models.BooleanField(default=True)
    updates = models.ManyToManyField(Update, related_name='link_update')
    date_added = models.DateTimeField(editable=False, blank=True)
    date_updated = models.DateTimeField(editable=False, blank=True)

    @permalink
    def get_url(self):
        return ('detail', None, {'app': self.app, 'id': self.id })

    def save(self, *args, **kwargs):
        if not self.date_added:
            self.date_added = datetime.utcnow()
        self.date_updated = datetime.utcnow()
        super(Base, self).save(*args, **kwargs)        