from django.db import models

class Sugestion(models.Model):
	title = models.CharField(max_length=80)
	description = models.TextField()
	pub_date = models.DateTimeField('date published')
	#author
	#thumbsup
	#thumbsdown
	#location
	#tags