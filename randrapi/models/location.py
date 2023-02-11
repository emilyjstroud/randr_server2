from django.db import models

class Location(models.Model):
  
  uid = models.CharField(max_length=50)
  name = models.CharField(max_length=50)
  blurb = models.CharField(max_length=250)
  photo = models.URLField()
  
def __str__(self):
  return self.name
