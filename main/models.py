from django.db import models

# Create your models here.

class Image(models.Model):
	image = models.FileField(upload_to='img/%Y/%m/%d', blank=True)

class Good(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=2)
	images = models.ManyToManyField(Image)
