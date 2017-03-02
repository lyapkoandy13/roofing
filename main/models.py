from django.db import models

# Create your models here.

class Good(models.Model):
	name = models.CharField(max_length=255, blank=True)
	description = models.CharField(max_length=255, blank=True)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	image = models.FileField(upload_to='img/%Y/%m/%d')
