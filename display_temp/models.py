from django.db import models
from django.utils import timezone

# Create your models here.
class Temperture_Data(models.Model):
    #Database for storing date and temperture
   # tz = timezone('America/Vancouver')
    date = models.DateTimeField(auto_now_add=True)
    temperture =models.FloatField()
    arm = models.BooleanField()

    def __str__(self):
      return f"{self.temperture} {self.date} {self.arm} )"
