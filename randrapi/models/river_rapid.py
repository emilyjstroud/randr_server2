from django.db import models
from .river import River
from .rapid import Rapid

class River_Rapid(models.Model):
  
  river = models.ForeignKey(River, on_delete=models.CASCADE)
  rapid = models.ForeignKey(Rapid, on_delete=models.CASCADE)
  
def __str__(self):
  return self.name
