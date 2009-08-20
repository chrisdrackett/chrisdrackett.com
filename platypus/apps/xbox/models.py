from django.db import models
from django.conf import settings

from tagging.fields import TagField

STATUS = (
	('M', 'Movie'),
	('G', 'Game'),
	('T', 'TV'),
	('X', 'Xbox'),
	('O', 'Off')
)

class Status(models.Model):
	class Meta:
		verbose_name_plural = 'Xbox Status'
		get_latest_by = 'date'
		ordering = ['-date']

	status = models.CharField(max_length=200)
	info = models.CharField(max_length=200)
	use = models.CharField(max_length=1, choices=STATUS)
	tags = TagField()
	date = models.DateTimeField(auto_now_add=True, editable=False)

	allow_comments = models.BooleanField(default=True)
	published = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.status
		
	class Admin:
		ordering = ['-date']
		list_display = ('status', 'date', 'tags', 'published', 'allow_comments')
		list_filter = ('date','allow_comments','published')

	def get_absolute_url(self):
		return "%s/xbox/%s/" % (settings.MY_URL.rstrip('/'), self.date.strftime("%Y/%B/%d").lower())

	def _get_comment_count(self):
		from django.contrib.contenttypes.models import ContentType
		from django.contrib.comments.models import Comment
		ctype = ContentType.objects.get(name__exact='entry')
		num_comments = Comment.objects.filter(content_type=ctype.id, object_id=self.id).count()
		return num_comments
	comment_count = property(_get_comment_count)

class Score(models.Model):
	class Meta:
		verbose_name_plural = 'Xbox Gamerscore'
		get_latest_by = 'date'
		ordering = ['-date']

	date = models.DateField(auto_now_add=True, editable=False)
	gamerscore = models.IntegerField()
	
	def __unicode__(self):
		return unicode(self.gamerscore)

	class Admin:
		ordering = ['-date']

def get_gamer_score(*args, **kwargs):
	#TODO run once a day
	import urllib
	import time
	import datetime

    try:
        from xml.etree import cElementTree as ET
    except ImportError:
        import cElementTree as ET

	try:
		tree = ET.parse(urllib.urlopen('http://duncanmackenzie.net/services/GetXboxInfo.aspx?GamerTag=drackett'))
		x = tree.getroot()
		
		try:
			last = Score.objects.latest()
			if last.date != datetime.date.today():
				a = Score( gamerscore = int(x.find('GamerScore').text), )
				a.save()
		except Score.DoesNotExist:
			a = Score( gamerscore = int(x.find('GamerScore').text), )
			a.save()
		return "GamerScore: Success!"
	except:
		return "GamerScore: Fail!"
		
	
def sync_xbox(*args, **kwargs):
	import urllib
	import elementtree.ElementTree as ET
	
	try:
		tree = ET.parse(urllib.urlopen('http://duncanmackenzie.net/services/GetXboxInfo.aspx?GamerTag=drackett'))
		x = tree.getroot()
		presence = x.find('PresenceInfo')
		stop_this = False

		
		if presence.find('Online').text != "false":
			if presence.find('Title').text == "Xbox 360 HD DVD Player":
				current_use = u"M"
				current_status = u"HD-DVD"
			elif presence.find('Title').text == "Xbox 360 Dashboard":
				if presence.find('Info2').text == "Watching a video":
					current_use = u"M"
					current_status = u"DVD"
				else:
					current_use = u"X"
					current_status = u"Xbox 360 Dashboard"
			elif presence.find('Title').text == "Windows Media Center":
				current_use = u"T"
				current_status = u"TV"
			elif presence.find('Title').text == "www.xbox.com":
				stop_this = True
			else:
				current_use = u"G"
				current_status = unicode(presence.find('Title').text)
		else:
			current_use = u"Off"
			current_status = u"None"

		try:
			last = Status.objects.latest()
			if last.status != current_status:
					s = Status(
						status = current_status,
						use = current_use,
						info = unicode(presence.find('Info2').text).replace("\n", " "),
						tags = "xbox360 status " + current_status.replace(" ", "_"),
					)
					if current_use == u"Off":
						s.published = False
					s.save()
			else:
				if last.info != unicode(presence.find('Info2').text).replace("\n", " "):
					s = Status(
						status = current_status,
						use = current_use,
						info = unicode(presence.find('Info2').text).replace("\n", " "),
						tags = "xbox360 status " + current_status.replace(" ", "_"),
					)
					if current_use == u"Off":
						s.published = False
					s.save()
		except Status.DoesNotExist:
			s = Status(
						status = current_status,
						use = current_use,
						info = unicode(presence.find('Info2').text).replace("\n", " "),
						tags = "xbox360 status " + current_status.replace(" ", "_"),
					)
			if current_use == u"Off":
				s.published = False
			s.save()
		return True
	except:
		return False