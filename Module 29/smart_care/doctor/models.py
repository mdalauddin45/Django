from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Specialization(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    
    def __str__(self) :
        return self.name
    
class Designation(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    
    def __str__(self) :
        return self.name
    
class AvailableTime(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) :
        return self.name

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctor/images/')
    designation = models.ManyToManyField(Designation)
    specialization = models.ManyToManyField(Specialization)
    availabletime = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    fee = models.IntegerField()
    meetlink = models.CharField(max_length=100)
    
    def __str__(self) :
        return f"{self.user.first_name} {self.user.last_name}"