from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)
    instrument_type = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name