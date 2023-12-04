from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length= 255)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.TextField(default='Rahim')
    
    def __str__(self):
        return f"Name: {self.name} - roll: {self.roll}" 
    
class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length= 255)
    father_name = models.TextField(max_length=200)
    address = models.TextField()