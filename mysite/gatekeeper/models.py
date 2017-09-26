from django.db import models
from django.contrib.auth.models import User

class Sugestion(models.Model):
	"""
	Creates a sugestion of pitch.
	"""
	title = models.CharField(max_length=80)
	description = models.TextField()
	pub_date = models.DateTimeField('date published')
	#author
	#thumbsup
	#thumbsdown
	#location
	#tags

	def __str__(self):
		return self.title

class Journalist(User):
	"""
	People who can consume the sugestions of pitch.
	"""
	#herited from User:
	#username
	#password
	#email
	#first_name
	#last_name
	
	company = models.CharField(max_length=40)
	
	def __str__(self):
		return self.username
	
class Citizen(User):
	"""
	People whom make sugestions of pitch.
	"""	
	neighbourhood = models.CharField(max_length=80)	