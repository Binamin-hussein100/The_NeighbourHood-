from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.expressions import F
# Create your models here.

class NeigbourHood(models.Model):
    hood_name = models.CharField(max_length=30)
    location = models.TextField()
    occupants_count = models.IntegerField()
    
    def __str__(self):
        return self.hood_name
class Business(models.Model):
    business_name = models.CharField(max_length=50)
    neighbourhood = models.OneToOneField(NeigbourHood,unique=False,on_delete=models.CASCADE)
    business_email = models.EmailField()

class User(AbstractUser):
    name = models.CharField(max_length=30)
    neighborhood = models.OneToOneField(NeigbourHood,unique=False,on_delete=models.CASCADE)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
