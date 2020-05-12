from django.db import models

# Create your models here.

class Destination(models.Model):
    
    name = models.CharField(max_length=100, blank=True, default='DEFAULT VALUE')
    img = models.ImageField(upload_to='pics', null=True)
    desc = models.CharField(max_length=100, blank=True, default='DEFAULT VALUE')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)