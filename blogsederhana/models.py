from __future__ import unicode_literals

from django.db import models
#from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
#from tinymce.models import HTMLField
from time import time

class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)
		
def generate_filename(instance, filename):
    ext = filename.split('.')[-1]
    return 'images/' + str(int(time())) + '.' + ext

class Post(models.Model):
	title = models.CharField(max_length=100)
	body = RichTextUploadingField()
	picture = models.ImageField("Picture", blank=True, null=True)
	created = models.DateTimeField()
	#author = models.ForeignKey(User, null=True, blank=True)
	tags = TaggableManager()
	publish = models.BooleanField(default=True)

	objects = EntryQuerySet.as_manager()

	def __unicode__(self):
		return self.title

class AboutUs(models.Model):
	title = models.CharField(max_length=100)
	picture = models.ImageField("Picture", blank=True, null=True)
	description = RichTextUploadingField()

	def __unicode__(self):
		return self.title

class ContactUs(models.Model):
	title = models.CharField(max_length=100)
	facebook_url = models.CharField(max_length=100)
	twitter_url = models.CharField(max_length=100)
	instagram_url = models.CharField(max_length=100)
	github_url = models.CharField(max_length=100)
	description = RichTextUploadingField()

	def __unicode__(self):
		return self.title
		