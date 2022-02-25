from django.db import models

# Create your models here.
class Info(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    choose = models.CharField(max_length=200)
