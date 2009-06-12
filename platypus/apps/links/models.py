from django.db import models

from platypus.apps.common_models import Base

class Link(Base):
    class Meta:
        verbose_name_plural = 'Links'
    
    url = models.URLField(verify_exists=False, max_length=300)
    title = models.CharField(max_length=200)
    body = models.TextField()
    
    def __unicode__(self):
        return self.title