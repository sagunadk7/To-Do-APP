from django.db import models

class Services(models.Model):
    task = models.CharField(max_length=30)
    date = models.DateField()

# Create your models here.
