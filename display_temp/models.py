from django.db import models

# Create your models here.
class Temperture_Data(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    temperture =models.IntegerField()