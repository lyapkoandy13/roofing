from django.db import models

# Create your models here.

class Good(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	image = models.FileField(upload_to='static/main/img/', max_length=100, blank=True)