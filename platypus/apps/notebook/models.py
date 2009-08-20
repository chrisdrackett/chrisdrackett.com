from django.db import models
from django.conf import settings

from tagging.fields import TagField

class Entry(models.Model):
	class Meta:
		verbose_name_plural = 'Entries'
		get_latest_by = 'date'
		ordering = ['-date']

	title = models.CharField(max_length=150)
	body = models.TextField()
	body_more = models.TextField(blank=True)
	tags = TagField()
	date = models.DateTimeField(auto_now_add=True, editable=False)
	updates = models.ManyToManyField(Update, related_name='entry_update', blank=True, null=True)

	allow_comments = models.BooleanField(default=True)
	published = models.BooleanField(default=True)
	
	slug = models.SlugField(max_length=150, prepopulate_from=('title',), blank=True, editable=False, unique=True)
	
	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "%s/notebook/%s" % (settings.MY_URL.rstrip('/'), self.slug)

	def save(self):
		from platypus.extras.slugify import SlugifyUniquely
		if not self.slug:
			self.slug = SlugifyUniquely(self.title, self.__class__)
		super(self.__class__, self).save()