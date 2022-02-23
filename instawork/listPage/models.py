from pyexpat import model
from django.db import models

# Create your models here.
class Member(models.Model):
    Name = models.CharField(max_length=100)
    isAdmin = models.BooleanField(default=False)
    Phone = models.CharField(max_length=12)
    Email = models.CharField(max_length=100)
    
