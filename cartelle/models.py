from django.db import models

# Create your models here.
class Cartella(models.Model):
	nameIT = models.CharField(max_length=40)
	nameEN = models.CharField(max_length=40)