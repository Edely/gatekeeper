from django.db import models

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
