from datetime import datetime

from django.db import models

from platypus.apps.common_models import Base

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_added = models.DateTimeField(editable=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.date_added:
            self.date_added = datetime.utcnow()
        super(Category, self).save(*args, **kwargs)

class Choice(models.Model):
    category = models.ForeignKey(Category)

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_added = models.DateTimeField(editable=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.date_added:
            self.date_added = datetime.utcnow()
        super(Choice, self).save(*args, **kwargs)

class Item(Base):
    category = models.ForeignKey(Category)
    text = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True)
    number = models.DecimalField(max_digits=8, decimal_places=2)
    choice = models.ForeignKey(Choice, limit_choices_to={'category': self.category})