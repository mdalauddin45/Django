from django.db import models

# Create your models here.

class Author(models.Model):
    # if you declear that JCharField you can must write max_length
    name = models.CharField(max_length=255)
    bio = models.TextField()
    phone_no = models.CharField(max_length=12)
    
    def __str__(self):
        return self.name