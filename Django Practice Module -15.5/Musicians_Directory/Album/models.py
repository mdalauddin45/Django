from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    album_name  = models.CharField(max_length=225)
    musicians = models.ManyToManyField(Musician)
    release_date  = models.DateField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    