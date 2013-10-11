from django.db import models

# Create your models here.
class Cartella(models.Model):
	nameIT = models.CharField(max_length=10)
	nameEN = models.CharField(max_length=10)