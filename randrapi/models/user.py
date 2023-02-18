from django.db import models

class User(models.Model):
  
  uid = models.CharField(max_length=50)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=75)
  
  def __str__(self):
      return self.name
