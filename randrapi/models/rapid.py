from django.db import models

class Rapid(models.Model):
  
  level = models.IntegerField()
  
def __str__(self):
  return self.name
