from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=200)
    musicians = models.ForeignKey(Musician, on_delete=models.CASCADE)  
    album_release_date = models.DateField()
    ratting = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    
    def __str__(self):
        return self.album_name