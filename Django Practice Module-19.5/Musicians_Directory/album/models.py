from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=200)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)  
    album_release_date = models.DateField()
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.album_name