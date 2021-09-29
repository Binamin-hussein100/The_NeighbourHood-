from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.

class NeigbourHood(models.Model):
    hood_name = models.CharField(max_length=30)
    location = models.TextField()
    occupants_count = models.IntegerField()
    
    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls,neighborhood_id):
        neighborhood = cls.objects.get(id=neighborhood_id)
        return neighborhood

    def update_neighborhood(self,name):
        self.name = name
        self.save()
    
    def __str__(self):
        return self.hood_name
class Business(models.Model):
    business_name = models.CharField(max_length=50)
    neighbourhood = models.ForeignKey(NeigbourHood,null=False,unique=False,on_delete=models.CASCADE,default=1)
    business_email = models.EmailField()


    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,business_id):
        business = cls.objects.get(id=business_id)
        return business

    def update_business(self,name):
        self.name = name
        self.save()
        
    def __str__(self):
        return self.business_name
    
class User(AbstractUser):
    name = models.CharField(max_length=30)
    neighborhood = models.ForeignKey(NeigbourHood,blank=True, null=True,on_delete=models.CASCADE,default=1)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField()
    neigbourHood =  models.CharField(max_length=30)
    profile_pic = CloudinaryField('image')
        
    