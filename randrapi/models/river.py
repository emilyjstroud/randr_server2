from django.db import models
from .location import Location

class River(models.Model):
  
  name = models.CharField(max_length=50)
  blurb = models.CharField(max_length=250)
  photo = models.URLField()
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  rapids = models.PositiveIntegerField(null=True)
  
def __str__(self):
  return self.name
