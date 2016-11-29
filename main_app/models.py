from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Treasure(models.Model) :
	user = models.ForeignKey(User)
	name = models.CharField(max_length = 100)
	value = models.DecimalField(max_digits=10, decimal_places=2)
	material = models.CharField(max_length = 100)
	location = models.CharField(max_length = 100)
	image = models.ImageField(upload_to = 'treasure_images', default = 'media/default.png')
	likes = models.IntegerField()

	
	def __str__(self):
		return self.name

class Location(models.Model):
	name = models.CharField(max_length=100)
	predators = models.CharField(max_length=100)
	num_restaurants = models.IntegerField()
	img_url = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name